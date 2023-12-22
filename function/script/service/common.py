import copy
import json
import os
from time import sleep

import numpy as np
from cv2 import imread

from function.common.bg_keyboard import key_down_up
from function.common.bg_mouse import mouse_left_click
from function.common.bg_p_compare import find_p_in_w, loop_find_p_in_w, loop_find_ps_in_w
from function.common.bg_p_screenshot import capture_picture_png
from function.get_paths import paths
from function.script.scattered.gat_handle import faa_get_handle
from function.script.scattered.get_battle_plan_list import get_battle_plan_list
from function.script.scattered.read_json_to_stage_info import read_json_to_stage_info
from function.script.service.in_battle.round_of_battle import RoundOfBattle
from function.script.service.in_battle.round_of_game import round_of_game


class FAA:
    def __init__(self, channel="锑食", zoom=1.0, player="1P", character_level=1,
                 is_use_key=True, is_auto_battle=True, is_auto_collect=False):

        # 获取窗口句柄
        self.channel = channel
        self.handle = faa_get_handle(channel=self.channel, mode="flash")
        self.handle_browser = faa_get_handle(channel=self.channel, mode="browser")
        self.handle_360 = faa_get_handle(channel=self.channel, mode="360")

        # 缩放
        self.zoom = zoom  # float 1.0 即百分百

        # 角色|等级|是否使用钥匙|卡片|收集战利品
        self.player = player
        self.character_level = character_level
        self.is_use_key = is_use_key
        self.is_auto_battle = is_auto_battle
        self.is_auto_collect = is_auto_collect

        # 每个副本的战斗都不一样的参数 使用内部函数调用更改
        self.is_group = False
        self.battle_plan = None
        self.stage_info = None

    """调用输入关卡配置和战斗配置, 在战斗前进行该操作"""

    def get_config_for_battle(self, is_group=False, battle_plan_index=0, stage_id="NO-1-1"):
        """
        :param is_group: 是否组队
        :param battle_plan_index: 战斗方案的索引
        :param stage_id: 关卡的id
        :return:
        """

        self.is_group = is_group

        def read_json_to_battle_plan():
            battle_plan_list = get_battle_plan_list(with_extension=True)
            battle_plan_path = "{}\\{}".format(
                paths["battle_plan"],
                battle_plan_list[battle_plan_index]
            )
            with open(battle_plan_path, "r", encoding="UTF-8") as file:
                return json.load(file)

        self.battle_plan = read_json_to_battle_plan()
        self.stage_info = read_json_to_stage_info(stage_id)

    """封装好的对窗口的动作"""

    def action_get_stage_name(self):
        """在关卡备战界面 获得关卡名字"""
        stage_id = "Unknown"  # 默认名称
        img1 = capture_picture_png(handle=self.handle, raw_range=[0, 0, 950, 600])[468:484, 383:492, :3]
        # 关卡名称集 从资源文件夹自动获取, 资源文件命名格式：关卡名称.png
        stage_text_in_ready_check = []
        for i in os.listdir(paths["picture"]["ready_check_stage"]):
            if i.find(".png") != -1:
                stage_text_in_ready_check.append(i.split(".")[0])
        for i in stage_text_in_ready_check:
            if np.all(img1 == imread(paths["picture"]["ready_check_stage"] + "\\" + i + ".png", 1)):
                stage_id = i
                break
        return stage_id

    def action_get_task(self, target: str):
        """
        获取公会任务列表
        :param target:
        :return: [
            {
                "stage_id":str,
                "max_times":,
                "task_card":str,
                "ban_card":None
            },
        ]
        """
        # 点跳转
        loop_find_p_in_w(raw_w_handle=self.handle,
                         raw_range=[0, 0, 950, 600],
                         target_path=paths["picture"]["common"] + "\\bottom_menu\\goto.png",
                         target_sleep=1,
                         click=True,
                         click_zoom=self.zoom)

        # 点任务
        if target == "guild":
            # 公会任务 guild
            loop_find_p_in_w(raw_w_handle=self.handle,
                             raw_range=[0, 0, 950, 600],
                             target_path=paths["picture"]["common"] + "\\bottom_menu\\goto_guild_task.png",
                             target_sleep=1,
                             click=True,
                             click_zoom=self.zoom)
            # 点一下 让左边的选中任务颜色消失
            loop_find_p_in_w(raw_w_handle=self.handle,
                             raw_range=[0, 0, 950, 600],
                             target_path=paths["picture"]["guild_task"] + "\\ui.png",
                             target_sleep=0.5,
                             click=True,
                             click_zoom=self.zoom)
        if target == "spouse":
            # 情侣任务 spouse
            loop_find_p_in_w(raw_w_handle=self.handle,
                             raw_range=[0, 0, 950, 600],
                             target_path=paths["picture"]["common"] + "\\bottom_menu\\goto_spouse_task.png",
                             target_sleep=1,
                             click=True,
                             click_zoom=self.zoom)

        # 读取
        task_list = []
        # 公会任务 guild
        if target == "guild":
            path = paths["picture"]["guild_task"]
            for i in range(7):
                # 遍历任务
                for j in os.listdir("{}\\{}\\".format(path, str(i + 1))):
                    # 找到任务 加入任务列表
                    find_p = find_p_in_w(raw_w_handle=self.handle,
                                         raw_range=[0, 0, 950, 600],
                                         target_path="{}\\{}\\{}".format(path, str(i + 1), j),
                                         target_tolerance=0.999)
                    if find_p:
                        # 任务携带卡片默认为None
                        task_card = "None"
                        # 去除.png
                        j = j.split(".")[0]
                        # 处理解析字符串
                        num_of_line = j.count("_")
                        if num_of_line == 0:
                            stage_id = j
                        else:
                            my_list = j.split("_")
                            stage_id = my_list[0]
                            if num_of_line == 1:
                                if not my_list[1].isdigit():
                                    task_card = my_list[1]
                            elif num_of_line == 2:
                                task_card = my_list[2]
                        # 添加到任务列表
                        task_list.append({"is_group": True,
                                          "stage_id": stage_id,
                                          "max_times": 1,
                                          "task_card": task_card,
                                          "list_ban_card": [],
                                          "dict_exit": {"other_time": [0], "last_time": [3]}})

        # 情侣任务 spouse
        if target == "spouse":
            path = paths["picture"]["spouse_task"]
            for i in ["1", "2", "3"]:
                # 任务未完成
                find_p = find_p_in_w(raw_w_handle=self.handle,
                                     raw_range=[0, 0, 950, 600],
                                     target_path="{}\\NO-{}.png".format(path, i),
                                     target_tolerance=0.999)
                if find_p:
                    # 遍历任务
                    for j in os.listdir("{}\\{}\\".format(path, i)):
                        # 找到任务 加入任务列表
                        find_p = find_p_in_w(raw_w_handle=self.handle,
                                             raw_range=[0, 0, 950, 600],
                                             target_path="{}\\{}\\{}".format(path, i, j),
                                             target_tolerance=0.999)
                        if find_p:
                            task_list.append({"is_group": True,
                                              "stage_id": j.split(".")[0],
                                              "max_times": 1,
                                              "task_card": "None",
                                              "list_ban_card": [],
                                              "dict_exit": {"other_time": [0], "last_time": [3]}})

        # 关闭公会任务列表(红X)
        self.action_exit(exit_mode="normal_x")

        return task_list

    """receive task reward"""

    def action_task_guild(self):
        # 点跳转
        loop_find_p_in_w(raw_w_handle=self.handle,
                         raw_range=[0, 0, 950, 600],
                         target_path=paths["picture"]["common"] + "\\bottom_menu\\goto.png",
                         target_sleep=1,
                         click=True,
                         click_zoom=self.zoom)
        # 点任务
        loop_find_p_in_w(raw_w_handle=self.handle,
                         raw_range=[0, 0, 950, 600],
                         target_path=paths["picture"]["common"] + "\\bottom_menu\\goto_guild_task.png",
                         target_sleep=1,
                         click=True,
                         click_zoom=self.zoom)
        # 循环遍历点击完成
        while True:
            # 点一下 让左边的选中任务颜色消失
            loop_find_p_in_w(raw_w_handle=self.handle,
                             raw_range=[0, 0, 950, 600],
                             target_path=paths["picture"]["guild_task"] + "\\ui.png",
                             target_sleep=0.5,
                             click=True,
                             click_zoom=self.zoom)
            result = loop_find_p_in_w(raw_w_handle=self.handle,
                                      raw_range=[0, 0, 950, 600],
                                      target_path=paths["picture"]["guild_task"] + "\\completed.png",
                                      target_tolerance=0.99,
                                      click_zoom=self.zoom,
                                      click=True,
                                      target_failed_check=5,  # 1+4s 因为偶尔会弹出美食大赛完成动画4s 需要充足时间！这个确实脑瘫...
                                      target_sleep=0.5)
            if result:
                loop_find_p_in_w(raw_w_handle=self.handle,
                                 raw_range=[0, 0, 950, 600],
                                 target_path=paths["picture"]["guild_task"] + "\\gather.png",
                                 target_tolerance=0.99,
                                 click_zoom=self.zoom,
                                 click=True,
                                 target_failed_check=2,
                                 target_sleep=2)  # 2s 完成任务有显眼动画
            else:
                break
        # 退出任务界面
        self.action_exit(exit_mode="normal_x")

    def action_task_spouse(self):
        # 点跳转
        loop_find_p_in_w(raw_w_handle=self.handle,
                         raw_range=[0, 0, 950, 600],
                         target_path=paths["picture"]["common"] + "\\bottom_menu\\goto.png",
                         target_sleep=1,
                         click=True,
                         click_zoom=self.zoom)
        # 点任务
        loop_find_p_in_w(raw_w_handle=self.handle,
                         raw_range=[0, 0, 950, 600],
                         target_path=paths["picture"]["common"] + "\\bottom_menu\\goto_spouse_task.png",
                         target_sleep=1,
                         click=True,
                         click_zoom=self.zoom)
        # 循环遍历点击完成
        while True:
            result = loop_find_p_in_w(raw_w_handle=self.handle,
                                      raw_range=[0, 0, 950, 600],
                                      target_path=paths["picture"]["spouse_task"] + "\\completed.png",
                                      target_tolerance=0.99,
                                      click_zoom=self.zoom,
                                      click=True,
                                      target_failed_check=2,
                                      target_sleep=2)  # 2s 完成任务有显眼动画)
            if not result:
                break
        # 退出任务界面
        self.action_exit(exit_mode="normal_x")

    def action_task_offer_reward(self):
        # 防止活动列表不在
        self.change_activity_list(1)

        # 点击进入OR界面
        loop_find_p_in_w(raw_w_handle=self.handle,
                         raw_range=[0, 0, 950, 600],
                         target_path=paths["picture"]["common"] + "\\顶部菜单\\X年活动.png",
                         target_sleep=2,
                         click=True,
                         click_zoom=self.zoom)

        # 循环遍历点击完成
        while True:
            result = loop_find_p_in_w(raw_w_handle=self.handle,
                                      raw_range=[0, 0, 950, 600],
                                      target_path=paths["picture"]["common"] + "\\offer_reward_get_loot.png",
                                      target_tolerance=0.99,
                                      target_failed_check=2,
                                      click_zoom=self.zoom,
                                      click=True,
                                      target_sleep=2)
            if not result:
                break

        # 退出任务界面
        self.action_exit(exit_mode="normal_x")

    def action_task_receive_rewards(self, task_type: str):
        """
        收取任务奖励
        :param task_type: "guild" or "spouse" or "offer_reward"
        :return:
        """
        print("[{}][收取任务奖励][{}] 开始收取".format(self.player, task_type))

        if task_type == "guild":
            self.action_task_guild()
        if task_type == "spouse":
            self.action_task_spouse()
        if task_type == "offer_reward":
            self.action_task_offer_reward()

        print("[{}][收取任务奖励][{}] 已全部领取".format(self.player, task_type))

    def change_activity_list(self, serial_num: int):
        """检测顶部的活动清单, 1为第一页, 2为第二页(有举报图标的一页)"""

        target = find_p_in_w(raw_w_handle=self.handle,
                             raw_range=[0, 0, 950, 600],
                             target_path=paths["picture"]["common"] + "\\顶部菜单\\举报.png")

        if serial_num == 1:
            if target:
                mouse_left_click(handle=self.handle,
                                 x=int(785 * self.zoom),
                                 y=int(30 * self.zoom),
                                 sleep_time=0.5)

        if serial_num == 2:
            if not target:
                mouse_left_click(handle=self.handle,
                                 x=int(785 * self.zoom),
                                 y=int(30 * self.zoom),
                                 sleep_time=0.5)

    """battle enter / in combat / exit"""

    def check_level(self):
        """检测角色等级和关卡等级(调用于输入关卡信息之后)"""
        if self.character_level < self.stage_info["level"]:
            return False
        else:
            return True

    def action_goto_map(self, map_id):
        """
        用于前往各地图,0.美味阵,1.美味岛,2.火山岛,3.火山遗迹,4.浮空岛,5.海底,6.营地
        """

        # 点击世界地图
        if not loop_find_p_in_w(raw_w_handle=self.handle,
                                raw_range=[0, 0, 950, 600],
                                target_path=paths["picture"]["common"] + "\\顶部菜单\\大地图.png",
                                click_zoom=self.zoom,
                                target_sleep=1.5,
                                click=True,
                                target_failed_check=10):
            print("10s没有找到右上大地图...请找个符合要求的位置重启脚本...")

        # 点击对应的地图
        my_path = paths["picture"]["map"] + "\\" + str(map_id) + ".png"
        loop_find_p_in_w(raw_w_handle=self.handle,
                         raw_range=[0, 0, 950, 600],
                         target_path=my_path,
                         target_tolerance=0.99,
                         click_zoom=self.zoom,
                         target_sleep=2,
                         click=True)

    def action_goto_stage(self, room_creator: bool = True, extra_action_first_time: bool = False):
        """
        只要右上能看到地球 就可以到目标关卡
        Args:
            room_creator: 是房主；仅房主创建关卡；
            extra_action_first_time: 魔塔关卡下 是否是第一次打(第一次塔需要进塔 第二次只需要选关卡序号)
        """

        # 拆成数组["关卡类型","地图id","关卡id"]
        stage_list = self.stage_info["id"].split("-")
        stage_0 = stage_list[0]  # type
        stage_1 = stage_list[1]  # map
        stage_2 = stage_list[2]  # stage

        def click_set_password():
            """设置进队密码"""
            mouse_left_click(handle=self.handle,
                             x=int(491 * self.zoom),
                             y=int(453 * self.zoom),
                             sleep_time=0.5)
            mouse_left_click(handle=self.handle,
                             x=int(600 * self.zoom),
                             y=int(453 * self.zoom),
                             sleep_time=0.5)
            key_down_up(handle=self.handle,
                        key="backspace")
            key_down_up(handle=self.handle,
                        key="1")
            sleep(1)

        def change_to_region(region_id: int = 2):
            mouse_left_click(handle=self.handle,
                             x=int(820 * self.zoom),
                             y=int(85 * self.zoom),
                             sleep_time=0.5)

            my_list = [85, 110, 135, 160, 185, 210, 235, 260, 285, 310, 335]
            mouse_left_click(handle=self.handle,
                             x=int(779 * self.zoom),
                             y=int(my_list[region_id - 1] * self.zoom),
                             sleep_time=2)

        def main_no():
            # 防止被活动列表遮住
            self.change_activity_list(2)

            # 进入对应地图
            self.action_goto_map(map_id=stage_1)

            # 切区
            my_dict = {"1": 8, "2": 2, "3": 1, "4": 2, "5": 2}
            change_to_region(region_id=my_dict[stage_1])

            # 仅限主角色创建关卡
            if room_creator:
                # 选择关卡
                my_path = paths["picture"]["stage"] + "\\" + self.stage_info["id"] + ".png"
                loop_find_p_in_w(raw_w_handle=self.handle,
                                 raw_range=[0, 0, 950, 600],
                                 target_path=my_path,
                                 click_zoom=self.zoom,
                                 target_tolerance=0.995,
                                 target_sleep=1, click=True)

                # 设置密码
                click_set_password()

                # 创建队伍
                my_path = paths["picture"]["common"] + "\\battle\\before_create_room.png"
                loop_find_p_in_w(raw_w_handle=self.handle,
                                 raw_range=[0, 0, 950, 600],
                                 target_path=my_path,
                                 click_zoom=self.zoom,
                                 target_sleep=1, click=True)

        def main_mt():
            if extra_action_first_time:
                # 防止被活动列表遮住
                self.change_activity_list(2)

                # 前往海底
                self.action_goto_map(map_id=5)

                # 选区
                change_to_region(region_id=2)

            if room_creator and extra_action_first_time:
                # 进入魔塔
                my_path = paths["picture"]["stage"] + "\\MT.png"
                loop_find_p_in_w(raw_w_handle=self.handle,
                                 raw_range=[0, 0, 950, 600],
                                 target_path=my_path,
                                 click_zoom=self.zoom,
                                 target_sleep=2,
                                 click=True)

                # 根据模式进行选择
                my_dict = {"1": 46, "2": 115, "3": 188}
                mouse_left_click(self.handle, int(my_dict[stage_1] * self.zoom), int(66 * self.zoom), sleep_time=0.5)

            if room_creator:
                # 选择了密室
                if stage_1 == "3":
                    my_path = paths["picture"]["stage"] + "\\" + self.stage_info["id"] + ".png"
                    loop_find_p_in_w(raw_w_handle=self.handle,
                                     raw_range=[0, 0, 950, 600],
                                     target_path=my_path,
                                     click_zoom=self.zoom,
                                     target_sleep=0.3,
                                     click=True)
                # 选择了单双人爬塔
                else:
                    # 等于0则为爬塔模式 即选择最高层 从下到上遍历所有层数
                    if stage_2 == "0":
                        # 到魔塔最低一层
                        mouse_left_click(handle=self.handle,
                                         x=int(47 * self.zoom),
                                         y=int(579 * self.zoom),
                                         sleep_time=0.3)

                        for i in range(11):
                            # 下一页
                            mouse_left_click(handle=self.handle,
                                             x=int(152 * self.zoom),
                                             y=int(577 * self.zoom),
                                             sleep_time=0.1)

                            for j in range(15):
                                mouse_left_click(
                                    handle=self.handle,
                                    x=int(110 * self.zoom),
                                    y=int(int(542 - (30.8 * j)) * self.zoom),
                                    sleep_time=0.1)

                    else:
                        # 到魔塔最低一层
                        mouse_left_click(handle=self.handle,
                                         x=int(47 * self.zoom),
                                         y=int(579 * self.zoom),
                                         sleep_time=0.3)
                        # 向右到对应位置
                        my_left = int((int(stage_2) - 1) / 15)
                        for i in range(my_left):
                            mouse_left_click(handle=self.handle,
                                             x=int(152 * self.zoom),
                                             y=int(577 * self.zoom),
                                             sleep_time=0.3)
                        # 点击对应层数
                        mouse_left_click(handle=self.handle,
                                         x=int(110 * self.zoom),
                                         y=int(int(542 - (30.8 * (int(stage_2) - my_left * 15 - 1))) * self.zoom),
                                         sleep_time=0.3)

                # 进入关卡
                my_path = paths["picture"]["common"] + "\\battle\\before_select_stage_magic_tower_start.png"
                loop_find_p_in_w(raw_w_handle=self.handle,
                                 raw_range=[0, 0, 950, 600],
                                 target_path=my_path,
                                 click_zoom=self.zoom,
                                 target_sleep=1,
                                 click=True)

        def main_cs():
            # 防止活动列表不在
            self.change_activity_list(1)

            # 点击进入跨服副本界面
            loop_find_p_in_w(raw_w_handle=self.handle,
                             raw_range=[0, 0, 950, 600],
                             target_path=paths["picture"]["common"] + "\\顶部菜单\\跨服远征.png",
                             target_sleep=2,
                             click=True,
                             click_zoom=self.zoom)

            if room_creator:
                # 创建房间
                mouse_left_click(self.handle, int(853 * self.zoom), int(553 * self.zoom), sleep_time=0.5)

                # 选择地图
                my_x = int(stage_1) * 101 - 36
                mouse_left_click(self.handle, int(my_x * self.zoom), int(70 * self.zoom), sleep_time=1)

                # 选择关卡 设置勾选密码 并创建房间
                my_dict = {
                    "1": [124, 248], "2": [349, 248], "3": [576, 248], "4": [803, 248],
                    "5": [124, 469], "6": [349, 469], "7": [576, 469], "8": [803, 469]}
                mouse_left_click(
                    self.handle,
                    int(my_dict[stage_2][0] * self.zoom),
                    int(my_dict[stage_2][1] * self.zoom),
                    sleep_time=0.5)

                # 选择密码输入框
                my_dict = {
                    "1": [194, 248], "2": [419, 248], "3": [646, 248], "4": [873, 248],
                    "5": [194, 467], "6": [419, 467], "7": [646, 467], "8": [873, 467]}
                mouse_left_click(
                    self.handle,
                    int(my_dict[stage_2][0] * self.zoom),
                    int(my_dict[stage_2][1] * self.zoom),
                    sleep_time=0.5)

                # 输入密码
                key_down_up(self.handle, "1")

                # 创建关卡
                my_dict = {  # X+225 Y+221
                    "1": [176, 286], "2": [401, 286], "3": [629, 286], "4": [855, 286],
                    "5": [176, 507], "6": [401, 507], "7": [629, 507], "8": [855, 507]}
                mouse_left_click(
                    self.handle,
                    int(my_dict[stage_2][0] * self.zoom),
                    int(my_dict[stage_2][1] * self.zoom),
                    sleep_time=1)
            else:
                # 刷新
                mouse_left_click(self.handle, int(895 * self.zoom), int(80 * self.zoom), sleep_time=3)
                # 复位
                mouse_left_click(self.handle, int(602 * self.zoom), int(490 * self.zoom), sleep_time=0.1)
                for i in range(20):
                    find = loop_find_p_in_w(raw_w_handle=self.handle,
                                            raw_range=[0, 0, 950, 600],
                                            target_path=paths["picture"]["common"] + "\\cross_server_1p.png",
                                            click_zoom=self.zoom,
                                            click=True,
                                            target_sleep=2.0,
                                            target_failed_check=1.0)
                    if find:
                        break
                    else:
                        mouse_left_click(self.handle, int(700 * self.zoom), int(490 * self.zoom), sleep_time=0.1)
                        # 下一页

                # 输入密码 确定进入
                key_down_up(handle=self.handle, key="1")
                mouse_left_click(self.handle, int(490 * self.zoom), int(360 * self.zoom), sleep_time=0.1)

        def main_or():
            # 防止活动列表不在
            self.change_activity_list(1)

            # 点击进入悬赏副本
            my_path = paths["picture"]["common"] + "\\顶部菜单\\X年活动.png"
            loop_find_p_in_w(raw_w_handle=self.handle,
                             raw_range=[0, 0, 950, 600],
                             target_path=my_path,
                             click_zoom=self.zoom,
                             target_sleep=2,
                             click=True)

            # 根据模式进行选择
            my_dict = {"1": 260, "2": 475, "3": 710}
            mouse_left_click(handle=self.handle,
                             x=int(my_dict[stage_1] * self.zoom),
                             y=int(411 * self.zoom),
                             sleep_time=2)

            # 切区
            my_dict = {"1": 8, "2": 2, "3": 2}
            change_to_region(region_id=my_dict[stage_1])

            # 仅限创房间的人
            if room_creator:
                # 设置密码
                click_set_password()
                # 创建队伍
                mouse_left_click(handle=self.handle,
                                 x=int(583 * self.zoom),
                                 y=int(500 * self.zoom),
                                 sleep_time=0.5)

        def main_ex():
            # 防止被活动列表遮住
            self.change_activity_list(2)

            # 进入对应地图
            self.action_goto_map(map_id=6)

            # 不是营地
            if stage_1 != "1":
                # 找船
                loop_find_p_in_w(raw_w_handle=self.handle,
                                 raw_range=[0, 0, 950, 600],
                                 target_path="{}\\EX-Ship.png".format(paths["picture"]["stage"]),
                                 click_zoom=self.zoom,
                                 target_sleep=1.5,
                                 click=True)
                # 找地图图标
                loop_find_p_in_w(raw_w_handle=self.handle,
                                 raw_range=[0, 0, 950, 600],
                                 target_path="{}\\EX-{}.png".format(paths["picture"]["stage"], stage_1),
                                 click_zoom=self.zoom,
                                 target_sleep=1.5,
                                 click=True)

            # 切区
            change_to_region(region_id=2)

            # 仅限主角色创建关卡
            if room_creator:
                # 选择关卡
                my_path = "{}\\{}.png".format(paths["picture"]["stage"], self.stage_info["id"])
                loop_find_p_in_w(raw_w_handle=self.handle,
                                 raw_range=[0, 0, 950, 600],
                                 target_path=my_path,
                                 click_zoom=self.zoom,
                                 target_sleep=0.5,
                                 click=True)

                # 设置密码
                click_set_password()

                # 创建队伍
                my_path = "{}\\battle\\before_create_room.png".format(paths["picture"]["common"])
                loop_find_p_in_w(raw_w_handle=self.handle,
                                 raw_range=[0, 0, 950, 600],
                                 target_path=my_path,
                                 click_zoom=self.zoom,
                                 target_sleep=0.5,
                                 click=True)

        if stage_0 == "NO":
            main_no()
        elif stage_0 == "MT":
            main_mt()
        elif stage_0 == "CS":
            main_cs()
        elif stage_0 == "OR":
            main_or()
        elif stage_0 == "EX":
            main_ex()
        else:
            print("请输入正确的关卡名称！")

    def action_battle_normal(self, battle_mode: int, task_card: str, list_ban_card: list):
        """从类中继承主要方法 方便被调用"""

        # 调用 InBattle 类 生成实例, 从self中填充数据
        round_of_battle = RoundOfBattle(
            handle=self.handle,
            zoom=self.zoom,
            player=self.player,
            is_use_key=self.is_use_key,
            is_auto_battle=self.is_auto_battle,
            is_auto_collect=self.is_auto_collect,
            path_p_common=paths["picture"]["common"],
            stage_info=self.stage_info,
            battle_plan=copy.deepcopy(self.battle_plan),
            is_group=self.is_group
        )

        round_of_battle.action_battle_normal(
            battle_mode=battle_mode,
            task_card=task_card,
            list_ban_card=list_ban_card
        )

    def action_round_of_game(
            self, deck: int, delay_start: bool, battle_mode: int, task_card: str, list_ban_card: list):
        """
        一轮游戏
        """

        round_of_game(
            handle=self.handle,
            zoom=self.zoom,
            paths=paths,
            player=self.player,
            stage_info_id=self.stage_info["id"],
            action_battle_normal=self.action_battle_normal,
            deck=deck,
            delay_start=delay_start,
            battle_mode=battle_mode,
            task_card=task_card,
            list_ban_card=list_ban_card
        )

    def action_exit(self, exit_mode):
        """
        退出
        "none" 或者 瞎填 -不退出 0
        "normal_x" - 普通的右上红叉 2
        "back_one_level"-右下回退到上一级 1
        "sports_land" - 直接到竞技岛  3
        "exit_offer_reward" - 悬赏的右上角红叉关闭
        "food_competition" - 美食大赛领取
        "exit_game" -游戏内退出
        """

        handle = self.handle
        zoom = self.zoom

        """右下 回退到上一级"""
        if exit_mode == "back_one_level":
            loop_find_p_in_w(raw_w_handle=handle,
                             raw_range=[0, 0, 950, 600],
                             target_path=paths["picture"]["common"] + "\\bottom_menu\\back.png",
                             target_failed_check=100,
                             target_sleep=1.5,
                             click=True,
                             click_zoom=zoom)

        """右上 红叉"""
        if exit_mode == "normal_x":
            loop_find_p_in_w(raw_w_handle=handle,
                             raw_range=[0, 0, 950, 600],
                             target_path=paths["picture"]["common"] + "\\battle\\before_exit_x.png",
                             target_failed_check=100,
                             target_sleep=1.5,
                             click=True,
                             click_zoom=zoom)

        """右下 前往竞技岛"""
        if exit_mode == "sports_land":
            loop_find_p_in_w(raw_w_handle=handle,
                             raw_range=[0, 0, 950, 600],
                             target_path=paths["picture"]["common"] + "\\bottom_menu\\goto.png",
                             target_tolerance=0.99,
                             target_failed_check=100,
                             target_sleep=1.5,
                             click=True,
                             click_zoom=zoom)

            loop_find_p_in_w(raw_w_handle=handle,
                             raw_range=[0, 0, 950, 600],
                             target_path=paths["picture"]["common"] + "\\bottom_menu\\goto_arena.png",
                             target_tolerance=0.99,
                             target_failed_check=100,
                             target_sleep=1.5,
                             click=True,
                             click_zoom=zoom)

        """悬赏窗口关闭"""
        if exit_mode == 4:
            loop_find_p_in_w(raw_w_handle=handle,
                             raw_range=[0, 0, 950, 600],
                             target_path=paths["picture"]["common"] + "\\offer_reward_exit.png",
                             target_tolerance=0.99,
                             target_failed_check=100,
                             target_sleep=1.5,
                             click=True,
                             click_zoom=zoom)

        """美食大赛领取专用, 从一般关卡打完后开始"""
        if exit_mode == "food_competition":

            # 记录一下是否有完成任何一次任务
            found_flag = False
            # 先回到竞技岛
            loop_find_p_in_w(raw_w_handle=handle,
                             raw_range=[0, 0, 950, 600],
                             target_path=paths["picture"]["common"] + "\\bottom_menu\\goto.png",
                             target_tolerance=0.99,
                             target_failed_check=100,
                             target_sleep=1.5,
                             click=True,
                             click_zoom=zoom)

            loop_find_p_in_w(raw_w_handle=handle,
                             raw_range=[0, 0, 950, 600],
                             target_path=paths["picture"]["common"] + "\\bottom_menu\\goto_arena.png",
                             target_tolerance=0.99,
                             target_failed_check=100,
                             target_sleep=1.5,
                             click=True,
                             click_zoom=zoom)

            # 找到活动第一页 并进入活动页面
            self.change_activity_list(serial_num=1)

            # 循环查找进入美食大赛界面
            while True:
                # 循环查找
                find = loop_find_p_in_w(
                    raw_w_handle=handle,
                    raw_range=[0, 0, 950, 600],
                    target_path=paths["picture"]["common"] + "\\顶部菜单\\美食大赛.png",
                    target_tolerance=0.99,
                    target_failed_check=1,
                    target_sleep=1.5,
                    click=True,
                    click_zoom=zoom)

                if find:
                    my_dict = {0: 362, 1: 405, 2: 448, 3: 491, 4: 534, 5: 570}
                    for i in range(6):
                        # 先移动一次位置
                        mouse_left_click(handle=handle, x=int(536 * zoom), y=int(my_dict[i] * zoom), sleep_time=0.1)
                        # 找到就点一下领取, 1s内找不到就跳过
                        while True:
                            find = loop_find_p_in_w(
                                raw_w_handle=handle,
                                raw_range=[0, 0, 950, 600],
                                target_path=paths["picture"]["common"] + "\\美食大赛_领取.png",
                                target_tolerance=0.95,
                                target_failed_check=1,
                                target_sleep=0.5,
                                click_zoom=zoom,
                                click=True)
                            if find:
                                # 领取升级有动画
                                print("[{}] 美食大赛 完成任务!".format(self.player))
                                sleep(6)
                                # 更新是否找到flag
                                found_flag = True
                            else:
                                break

                    # 退出美食大赛界面
                    mouse_left_click(handle=handle, x=int(888 * zoom), y=int(53 * zoom), sleep_time=0.5)
                    break

            # 如果没有完成任何任务, 卡注5s
            if not found_flag:
                sleep(5)
                print("[{}] 没有在美食大赛完成任何任务, 请注意哦!".format(self.player))

        """游戏内退出游戏"""
        if exit_mode == "exit_game":
            # 游戏内退出
            mouse_left_click(handle=self.handle,
                             x=int(1050 * self.zoom),
                             y=int(582 * self.zoom),
                             sleep_time=0.5)
            # 确定游戏内退出
            mouse_left_click(handle=self.handle,
                             x=int(454 * self.zoom),
                             y=int(386 * self.zoom),
                             sleep_time=0.5)

    """reload game"""

    def reload_game(self):
        zoom = self.zoom
        while True:
            # 点击刷新按钮 该按钮在360窗口上
            loop_find_p_in_w(
                raw_w_handle=self.handle_360,
                raw_range=[0, 0, 2000, 2000],
                target_path=paths["picture"]["common"] + "\\login\\0_refresh.png",
                target_tolerance=0.99,
                target_sleep=3,
                click=True,
                click_zoom=zoom)

            # 是否在 选择服务器界面 - 判断是否存在 最近玩过的服务器ui(4399 or qq空间)
            result = loop_find_ps_in_w(
                raw_w_handle=self.handle_browser,
                raw_range=[0, 0, 2000, 2000],
                target_opts=[
                    {
                        "target_path": paths["picture"]["common"] + "\\login\\1_last_server_4399.png",
                        "target_tolerance": 0.99,
                    }, {
                        "target_path": paths["picture"]["common"] + "\\login\\1_last_server_qq.png",
                        "target_tolerance": 0.99,
                    }
                ],
                target_return_mode="or")

            if not result:
                print("[{}] [Warning] 未找到进入输入服务器, 可能随机进入了未知界面, 重新刷新".format(self.player))
                continue
            else:
                """尝试根据qq或4399的不同ui 进入最近进入的服务器"""
                result = find_p_in_w(
                    raw_w_handle=self.handle_browser,
                    raw_range=[0, 0, 2000, 2000],
                    target_path=paths["picture"]["common"] + "\\login\\1_last_server_4399.png",
                    target_tolerance=0.99
                )
                if result:
                    # 点击进入服务器
                    mouse_left_click(handle=self.handle_browser,
                                     x=int(result[0] * zoom),
                                     y=int((result[1] + 30) * zoom),
                                     sleep_time=0.5)
                result = find_p_in_w(
                    raw_w_handle=self.handle_browser,
                    raw_range=[0, 0, 2000, 2000],
                    target_path=paths["picture"]["common"] + "\\login\\1_last_server_qq.png",
                    target_tolerance=0.99
                )
                if result:
                    # 点击进入服务器
                    mouse_left_click(handle=self.handle_browser,
                                     x=int(result[0] * zoom),
                                     y=int((result[1] + 30) * zoom),
                                     sleep_time=0.5)

                """查找 - 关闭 健康游戏公告"""
                # 查找健康游戏公告
                target_path = paths["picture"]["common"] + "\\login\\2_health_game_advice.png"
                result = loop_find_p_in_w(
                    raw_w_handle=self.handle_browser,
                    raw_range=[0, 0, 2000, 2000],
                    target_path=target_path,
                    target_tolerance=0.97,
                    target_failed_check=10,
                    target_sleep=0.5,
                    click=False)
                if not result:
                    print("[{}] 未找到健康游戏公告, 刷新".format(self.player))
                    continue
                else:
                    # 重新获取句柄, 此时游戏界面的句柄已经改变
                    self.handle = faa_get_handle(channel=self.channel, mode="flash")

                    # 关闭健康游戏公告
                    loop_find_p_in_w(
                        raw_w_handle=self.handle,
                        raw_range=[0, 0, 950, 600],
                        target_path=paths["picture"]["common"] + "\\login\\3_health_game_advice_enter.png",
                        target_tolerance=0.97,
                        target_failed_check=15,
                        click=True,
                        click_zoom=zoom)

                    # [可能发生] 每日必充界面关闭
                    loop_find_p_in_w(
                        raw_w_handle=self.handle,
                        raw_range=[0, 0, 950, 600],
                        target_path=paths["picture"]["common"] + "\\login\\4_exit.png",
                        target_tolerance=0.99,
                        target_failed_check=2,
                        click=True,
                        click_zoom=zoom)

                    break

    def sign_in(self):
        handle = self.handle
        zoom = self.zoom
        self.change_activity_list(1)

        """VIP签到"""
        target_path = paths["picture"]["common"] + "\\sign_in\\vip.png"
        loop_find_p_in_w(
            raw_w_handle=handle,
            raw_range=[0, 0, 950, 600],
            target_path=target_path,
            target_tolerance=0.99,
            target_failed_check=1,
            target_sleep=1,
            click=True,
            click_zoom=zoom)

        mouse_left_click(
            handle=handle,
            x=int(740 * zoom),
            y=int(190 * zoom),
            sleep_time=0.5)

        mouse_left_click(
            handle=handle,
            x=int(225 * zoom),
            y=int(280 * zoom),
            sleep_time=0.5)

        self.action_exit(exit_mode="normal_x")

        """每日签到"""
        loop_find_p_in_w(
            raw_w_handle=handle,
            raw_range=[0, 0, 950, 600],
            target_path=paths["picture"]["common"] + "\\sign_in\\daily_sign_in.png",
            target_tolerance=0.99,
            target_failed_check=1,
            target_sleep=1,
            click=True,
            click_zoom=zoom)

        loop_find_p_in_w(
            raw_w_handle=handle,
            raw_range=[0, 0, 950, 600],
            target_path=paths["picture"]["common"] + "\\sign_in\\daily_sign_in_enter.png",
            target_tolerance=0.99,
            target_failed_check=1,
            target_sleep=1,
            click=True,
            click_zoom=zoom)

        self.action_exit(exit_mode="normal_x")

        """美食活动"""

        loop_find_p_in_w(
            raw_w_handle=handle,
            raw_range=[0, 0, 950, 600],
            target_path=paths["picture"]["common"] + "\\sign_in\\food_activation.png",
            target_tolerance=0.99,
            target_failed_check=1,
            target_sleep=1,
            click=True,
            click_zoom=zoom)

        loop_find_p_in_w(
            raw_w_handle=handle,
            raw_range=[0, 0, 950, 600],
            target_path=paths["picture"]["common"] + "\\sign_in\\food_activation_enter.png",
            target_tolerance=0.99,
            target_failed_check=1,
            target_sleep=1,
            click=True,
            click_zoom=zoom)

        self.action_exit(exit_mode="normal_x")

        """塔罗寻宝"""
        loop_find_p_in_w(
            raw_w_handle=handle,
            raw_range=[0, 0, 950, 600],
            target_path=paths["picture"]["common"] + "\\sign_in\\tarot.png",
            target_tolerance=0.99,
            target_failed_check=1,
            target_sleep=1,
            click=True,
            click_zoom=zoom)

        loop_find_p_in_w(
            raw_w_handle=handle,
            raw_range=[0, 0, 950, 600],
            target_path=paths["picture"]["common"] + "\\sign_in\\tarot_enter.png",
            target_tolerance=0.99,
            target_failed_check=1,
            target_sleep=1,
            click=True,
            click_zoom=zoom)

        loop_find_p_in_w(
            raw_w_handle=handle,
            raw_range=[0, 0, 950, 600],
            target_path=paths["picture"]["common"] + "\\sign_in\\tarot_exit.png",
            target_tolerance=0.99,
            target_failed_check=1,
            target_sleep=1,
            click=True,
            click_zoom=zoom)

    def quest(self):
        """领取普通任务奖励"""
        handle = self.handle
        zoom = self.zoom

        while True:
            # 点任务
            find = loop_find_p_in_w(
                raw_w_handle=handle,
                raw_range=[0, 0, 950, 600],
                target_path=paths["picture"]["common"] + "\\bottom_menu\\quest.png",
                target_tolerance=0.99,
                target_failed_check=1,
                target_sleep=0.5,
                click=True,
                click_zoom=zoom)

            if find:
                # 复位滑块
                mouse_left_click(handle=handle, x=int(413 * zoom), y=int(155 * zoom), sleep_time=0.25)

                for i in range(7):
                    # 找到就点一下, 找不到就跳过
                    while True:
                        find = loop_find_p_in_w(
                            raw_w_handle=handle,
                            raw_range=[0, 0, 950, 600],
                            target_path=paths["picture"]["common"] + "\\任务_完成.png",
                            target_tolerance=0.95,
                            target_failed_check=1,
                            target_sleep=0.5,
                            click_zoom=zoom,
                            click=True)
                        if find:
                            # 领取奖励
                            mouse_left_click(handle=handle, x=int(643 * zoom), y=int(534 * zoom), sleep_time=0.2)
                        else:
                            break

                    # 滑块向下移动3次
                    for j in range(3):
                        mouse_left_click(handle=handle, x=int(413 * zoom), y=int(524 * zoom), sleep_time=0.05)

                self.action_exit(exit_mode="normal_x")
                break

    def fed_and_watered(self):
        """公会施肥浇水功能"""
        # 暂存常用变量
        handle = self.handle
        zoom = self.zoom
        try_time = 0

        print("[{}] 开始公会浇水施肥".format(self.player))

        # 回到初始城镇
        self.action_goto_map(map_id=0)

        # 进入公会
        mouse_left_click(handle=self.handle, x=int(320 * self.zoom), y=int(220 * self.zoom), sleep_time=1)

        # 循环到任务完成
        while True:
            # 进入任务界面
            # mouse_left_moveto(handle=self.handle, x=int(757 * self.zoom), y=int(410 * self.zoom))
            mouse_left_click(handle=self.handle, x=int(745 * self.zoom), y=int(430 * self.zoom), sleep_time=0.001)
            # mouse_left_moveto(handle=self.handle, x=int(700 * self.zoom), y=int(300 * self.zoom))
            mouse_left_click(handle=self.handle, x=int(700 * self.zoom), y=int(350 * self.zoom), sleep_time=2)
            # 检测施肥任务完成情况 任务是进行中的话为True
            find = loop_find_ps_in_w(
                raw_w_handle=handle,
                raw_range=[0, 0, 950, 600],
                target_opts=[
                    {
                        "target_path": paths["picture"]["guild_task"] + "\\fed_0.png",
                        "target_tolerance": 0.99,
                    }, {
                        "target_path": paths["picture"]["guild_task"] + "\\fed_1.png",
                        "target_tolerance": 0.99,
                    }
                ],
                target_return_mode="or",
                target_failed_check=2)
            # 退出任务界面
            mouse_left_click(handle=self.handle, x=int(854 * self.zoom), y=int(55 * self.zoom), sleep_time=0.5)

            if not find:
                print("[{}] 已完成公会浇水施肥, 尝试次数:{}".format(self.player, try_time))
                break
            else:

                """进入施肥界面"""
                while True:
                    mouse_left_click(handle=self.handle, x=int(745 * self.zoom), y=int(430 * self.zoom),
                                     sleep_time=0.001)
                    mouse_left_click(handle=self.handle, x=int(800 * self.zoom), y=int(350 * self.zoom), sleep_time=2)
                    find = loop_find_p_in_w(
                        raw_w_handle=handle,
                        raw_range=[0, 0, 950, 600],
                        target_path=paths["picture"]["guild_task"] + "\\ui.png",
                        target_tolerance=0.95,
                        target_failed_check=1,
                        target_sleep=0.5,
                        click_zoom=zoom,
                        click=True)
                    if find:
                        break

                if try_time != 0:

                    # 点击全部工会
                    mouse_left_click(handle=self.handle, x=int(798 * self.zoom), y=int(123 * self.zoom), sleep_time=0.5)
                    # 跳转到最后
                    mouse_left_click(handle=self.handle, x=int(843 * self.zoom), y=int(305 * self.zoom), sleep_time=0.5)
                    # 以倒数第二页从上到下为1-4, 第二页为5-8次尝试对应的公会 以此类推
                    for i in range(try_time // 4 + 1):
                        # 向上翻的页数
                        mouse_left_click(handle=self.handle, x=int(843 * self.zoom), y=int(194 * self.zoom),
                                         sleep_time=0.5)
                        # 点第几个
                        my_dict = {1: 217, 2: 244, 3: 271, 4: 300}
                        mouse_left_click(handle=self.handle,
                                         x=int(810 * self.zoom),
                                         y=int(my_dict[try_time % 4] * self.zoom),
                                         sleep_time=0.5)
                # 采摘一次
                mouse_left_click(handle=self.handle, x=int(785 * self.zoom), y=int(471 * self.zoom), sleep_time=1)

                # 浇水一次
                mouse_left_click(handle=self.handle, x=int(785 * self.zoom), y=int(362 * self.zoom), sleep_time=1)
                # 等待一下 确保没有完成的黑屏
                loop_find_p_in_w(
                    raw_w_handle=handle,
                    raw_range=[0, 0, 950, 600],
                    target_path=paths["picture"]["common"] + "\\battle\\before_exit_x.png",
                    target_tolerance=0.95,
                    target_failed_check=5,
                    target_sleep=0.5,
                    click=False)
                print("{}次尝试, 浇水后, 已确认无任务完成黑屏".format(try_time))

                # 施肥一次
                mouse_left_click(handle=self.handle, x=int(785 * self.zoom), y=int(418 * self.zoom), sleep_time=1)
                # 等待一下 确保没有完成的黑屏
                loop_find_p_in_w(
                    raw_w_handle=handle,
                    raw_range=[0, 0, 950, 600],
                    target_path=paths["picture"]["common"] + "\\battle\\before_exit_x.png",
                    target_tolerance=0.95,
                    target_failed_check=5,
                    target_sleep=0.5,
                    click=False)
                print("{}次尝试, 施肥后, 已确认无任务完成黑屏".format(try_time))

                # 点X回退一次
                mouse_left_click(handle=self.handle, x=int(854 * self.zoom), y=int(55 * self.zoom), sleep_time=1.5)

                try_time += 1

        # 退出工会
        self.action_exit(exit_mode="normal_x")

    def cross_server_reputation(self):
        self.get_config_for_battle(is_group=False, battle_plan_index=0, stage_id="CS-1-2")
        self.action_goto_stage(room_creator=True, extra_action_first_time=True)
        sleep(60.5)  # 休息60.5s 等待完成
        # 游戏内退出
        self.action_exit(exit_mode="exit_game")


if __name__ == '__main__':
    def main():
        faa = FAA(channel="ti")
        faa.reload_game()


    main()
