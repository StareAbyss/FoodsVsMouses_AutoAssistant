# FAA_FoodsVsMouses_AutoAssistant

一款名叫中国页游《美食大战老鼠》的自动助手, 一键完成所有日常任务。  
An automatic assistant for a Chinese webpage game called Foods Vs Mouses, Complete all daily tasks with one click.

本软件基于图像识别 + 自动放卡完成战斗, 不支持任何作弊功能(秒杀或更多)。  
This software is based on image recognition, and does not support any cheating function (flash killing and more).

本软件尚处于开发阶段, 已实现功能见下。  
This software is still in the development stage and its functions have been implemented as shown below.

该工具开发初衷是圆梦十年前的童年愿望 (悲)    
The original intention of developing this tool is to fulfill a childhood wish ten years ago (XP)

# 关于
* 反馈交流QQ群 - 1群 - 2000人 - 786921130 - 推荐
* 反馈交流QQ群 - 2群 - 500人  - 142272678
* 爱发电赞助支持FAA - [点我跳转](https://afdian.net/a/zssy_faa)

# 下载
* Github-Relese - 包含FAA的稳定发行版. [点我跳转](https://github.com/StareAbyss/FoodsVsMouses_AutoAssistant/releases)    
* 交流QQ群-群文件 - 包含FAA的稳定发行版和内部测试版, 更有玩家社区维护的大量战斗方案和美食大赛资源供您使用.
* 注: Github的源码会实时更新, 仅Relese不包含不稳定的测试版本.

# 预览

* 运行主页
![image](https://github.com/StareAbyss/FoodsVsMiceAutoAssistant/assets/112901226/9ac6e0c5-1182-45da-b3ae-bc19e67335d0)
* 流程配置
![image](https://github.com/StareAbyss/FoodsVsMiceAutoAssistant/assets/112901226/505e4291-69a1-4e3a-8743-25a2590e1cb7)
* 高级选项
![image](https://github.com/StareAbyss/FoodsVsMiceAutoAssistant/assets/112901226/d4f3fc71-9b8f-4c00-8b9f-b2caa1431128)
* 战斗方案编辑器
![image](https://github.com/StareAbyss/FoodsVsMiceAutoAssistant/assets/112901226/d6a411a2-bc43-4388-943b-30e7304ba0dd)

# 主要功能 Main

    FAA
    │
    ├─ 自动日常- 非战斗类流程
    │   ├─ VIP - 每日签到 & 礼卷领取
    │   ├─ 常规每日签到
    │   ├─ 美食活动 - 每日免费许愿
    │   ├─ 寻宝塔罗 & 法老宝藏 - 免费抽取
    │   ├─ 公会 - 会长发布公会任务
    │   ├─ 公会 - 花园浇水 / 施肥 / 摘果
    │   ├─ 自动领取任务奖励
    │   └─ 自动使用消耗品
    │   └─ 自动删除无用道具, 主要是技能书. 需要高级设置 - 设定二级密码.
    │   └─ 公会副本商店 - 兑换暗晶. 需要高级设置 - 设定二级密码.
    │
    ├─ 流水线刷本 - 战斗类流程
    │   ├─ 双人 公会任务 + 领取
    │   ├─ 双人 情侣任务 + 领取
    │   ├─ 双人 悬赏 + 领取
    │   ├─ 单人 魔塔
    │   ├─ 双人 魔塔
    │   ├─ 塔魔 单人密室
    │   ├─ 单人&双人 跨服副本
    │   ├─ 单人&双人 勇士本
    │   ├─ 单人&双人 火山遗迹
    │   ├─ 单人&双人 自定义单本连刷
    │   ├─ 单人&双人 无限跨服副本刷威望
    │   ├─ 全自动美食大赛(战令任务), 需要当期任务图库支持.
    │   └─ 自定义任务列表 - 接口开放, 可完全自定义的任务列表, 只需书写.json文件
    │
    ├─ 自动放卡战斗
    │   ├─ 模仿人类思考方式的算法实现, 从目标阵容和卡片与位置重要性角度进行合理放卡.
    │   ├─ 单人双人均可支持.
    │   ├─ 上手轻松, 可高度自定义的战斗方案, 攻略各种高难副本, 魔塔164 / 天妇罗 / 音乐节夜 均不在话下, 更可根据个人box创建独属于您的方案.
    │   ├─ 一文件 = 一份战斗方案, 便于分享您的奇思, 获取他人的妙想.
    │   ├─ 内置战斗方案编辑器, 超轻松快捷可视化编辑, 无需写代码.
    │   ├─ 大量内置配置, 轻松上手入门.
    │   ├─ 全自动 承载卡, 仅需将对应卡片放入卡组中, 无需在战斗方案进行额外设置, 即可根据关卡自适应放置!
    │   ├─ 全自动 极寒冰沙, 仅需将对应卡片放入卡组中, 无需在战斗方案进行额外设置, 即可根据战况自适应放置!
    │   ├─ 全自动 幻幻鸡 / 创造神, 仅需将对应卡片放入卡组中, 仅需在战斗方案设置各卡片被复制的优先级, 即可根据战况自适应放置完成复制!
    │   ├─ 自动使用武器技能.
    │   └─ 自动鼠标模拟拾取.
    │
    └─ 其他特性
        ├─ 无限跨服一分钟刷威望.
        ├─ 自动定时启动, 真正做到设置一次, 点击一下, 自动刷一周!
        └─ 战利品和开宝箱历史记录保存, 识图储存为文本文件, 统计副本掉率.

# 用户使用必读

* 仅需要轻度使用, 可阅读 `[入门]FAA从入门到神殿.pdf` 轻松部署.
* 重度使用, 可认真通读下文, 部分存在于轻度pdf的文档的部分可能不再赘述.

## 兼容性支持

* 操作系统 - `Windows7及以上`
* 浏览器 - `360游戏大厅`
    * 请务必使用`极速模式`进行游戏, 即Chrome内核.
    * 如果您需要使用两个及以上游戏橘色, 请务必点击窗口右上角, 开启`多窗口模式`, 否则无法正常运行.
    * `窗口滚动条` 贴到 `最上最左`, 否则刷新时会自动调整导致坐标错位.
    * 在每一次重新打开游戏窗口后, 请 `完成至少一次区服选择` 并刷新后, 才能正常获取到上一次登录的服务器.
* 游戏渠道
    * 4399渠道服
        * v0.9.1+ 支持, 无需额外配置.
        * 该渠道服玩家可以使用云游戏的air网址进入游戏, 以获得更流畅的游戏体验.
    * QQ游戏大厅渠道服
        * v1.0.7+ 支持, 无需额外配置.
    * QQ空间渠道服
        * v0.9.1+ 支持, 需额外截图, 并在运行期间在电脑上登录对应QQ账号, 以进行快速登录.
        * 先将操作系统调整为`100%缩放倍率`.
        * 在项目目录中的 `resource/picture/common/用户自截` 中修改空间服登录界面截图, 可通过运行 `直达用户自截.bat` 快速抵达.
        * 需在快捷登录界面分别截图1P和2P上半部分QQ头像为 `.png` 格式.
    * 3366渠道服
        * 不支持. 原因如下, 该区服过于冷门, 且与QQ空间渠道服的进入方式有一定冲突, 若兼容会影响QQ空间渠道服用户的体验.

## 角色

* 大多数作战前, 由2P邀请1P.
  * P2必须加P1为好友, 且为 `唯一` 好友(P1不受限).
  * 游戏内设定 `仅接受来自好友` 的邀请, 否则会被某些乱七八糟的邀请扰乱流程.
* 最好保证P1和P2 `等级` 足够进入大多数副本, 且点掉首次进入副本前的 `橙色图标` , 否则无法正常进入关卡.
* 会自动设定关卡密码, 防止有人进入扰乱.
* 跨服作战前, 由1P邀请2P.
  * 一般默认1P练度高方便创建房间.
  * 需额外截图.
      * 先将操作系统调整为`100%缩放倍率`.
      * 在项目目录中的 `resource/picture/common/用户自截/cross_server_1P.png` 图片进行修改, 可通过运行 `直达用户自截.bat` 快速抵达.
      * 需1P创建跨服房间, 2P进行截图, 保存为 `.png` 格式.

## 软件中重要信息的填写

* 窗口名和游戏名称
    * 当你填写错误
        * 低版本(v0.9.1-)会直接导致 `软件闪退`.
        * 高版本(v1.0.0+)会直接弹窗 `提醒不启动`.
    * 360游戏大厅在 `添加游戏` 时, 你所填写的 `游戏名称`, 为软件中需要填写的 `游戏名称`.
    * 360游戏大厅在 `添加小号` 时, 你所填写的 `角色名字`, 为软件中需要填写的 `1P和2P的窗口名`.
    * 360游戏大厅中第一个启动的角色, 其窗口名需要空置, 请保持每次启动360游戏大厅时第一个开启的角色是相对固定的. 
    * 具体可以参考下图.
        * 将鼠标悬停在windows任务栏中的360游戏大厅的窗口上, 启动1P和2P时可以看到. 为 角色名称 | 游戏名称 或 游戏名称.
        * 其中 仅有游戏名称, 为第一个启动的角色, 对应在软件中, 其窗口名空置.
        * 其中 角色名称 | 游戏名称, 为之后启动的角色, 对应在软件中, 填写角色名称.
    ![image](https://github.com/StareAbyss/FoodsVsMouses_AutoAssistant/assets/112901226/80dea34e-5c84-43ce-932b-838c168bbdbd)


* 角色等级
    * 用于在任务需要完成高等级解锁的副本, 但角色等级不足时, 直接跳过对应任务, 防止卡死, 请如实填写.

* 屏幕缩放
    * 用于保证点击的缩放位置正确
    * win10 win11 用户, 桌面右键显示设置, 缩放和布局, 缩放中的数值, 记住它 然后在软件中进行选择.       
    * 低版本(v0.9.1-)填错不会有报错和卡死, 但运行会异常; 高版本(v1.0.0+)将自行获取.

## 内置战斗方案

本软件支持高度可自定义的共享式战斗方案, 但也包含了大量成熟的 `内置战斗方案`, 以满足大多数玩家的使用需求.  
考虑到版本更新和文档维护的滞后性, 更 `推荐使用方案编辑器直接查看` 各个内置方案的卡组和说明文本, 下文仅供参考.
更新版本: v1.1.2

* 默认卡组(含默认-激进)

    默认设置为[卡组1]    
    用于通勤, 可通杀大多数关卡, 包括: 所有公会任务 / 所有情侣任务 / 大多数悬赏第12关 / 火山遗迹 / 勇士 / 单人魔塔125 / 双人魔塔上限未知 / 跨服巫毒12(或更高)   
    如果需要完成 `需要携带某卡片` 的公会任务, 必须使用该卡组, 或仿照卡组, 空格收尾, 之后携带承载卡  

    |    | 1   | 2   | 3    | 4   | 5   | 6   | 7   | 8  | 9   | 10  | 11 | 12  |
    |:---|:----|:----|:-----|:----|:----|:----|:----|:---|:----|:----|:---|:----|
    | 1P | 小火炉 | 海星类 | 专业防空 | 瓜皮类 | 喷壶类 | 油灯类 | 布丁类 | 空格 | 木盘子 | 麦芽糖 | 气泡 | 咖啡粉 |
    | 2P | 小火炉 | 海星类 | 专业防空 | 瓜皮类 | 喷壶类 | 油灯类 | 布丁类 | 空格 | 木盘子 | 麦芽糖 | 气泡 | 咖啡粉 |
    
    注: 卡组2P不使用布丁, 但为了使2P单独作为1P作战使用默认方案时能摆放布丁, 故带上


* 花瓶卡组

    摆烂, 什么都不干, 一般可以是1P默认, 2P花瓶, 作用同默认卡组

    |    | 1  | 2   | 3   | 4  | 5   | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
    |:---|:---|:----|:----|:---|:----|:--|:--|:--|:--|:---|:---|:---|
    | NP | 空格 | 木盘子 | 麦芽糖 | 气泡 | 咖啡粉 |   |   |   |   |    |    |    |


* 生煎锅速刷卡组

    * 默认设置为[卡组2]  
    * 用于简单副本的灰烬速刷, 例如神殿/深渊
    * 普通版

    |    | 1   | 2   | 3    | 4   | 5   | 6   | 7   | 8    | 9   | 10  | 11  | 12  |
    |:---|:----|:----|:-----|:----|:----|:----|:----|:-----|:----|:----|:----|:----|
    | 1P | 小火炉 | 生煎锅 | 专业防空 | 瓜皮类 | 喷壶类 | 油灯类 | 冰淇淋 | 投掷增益 | 防漏卡 | 木盘子 | 麦芽糖 | 咖啡粉 |    |
    | 2P | 小火炉 | 生煎锅 | 专业防空 | 瓜皮类 | 喷壶类 | 油灯类 | 冰淇淋 | 木盘子  | 麦芽糖 | 咖啡粉 |     |
    
    * 电棍升级版

    |    | 1   | 2   | 3    | 4   | 5   | 6   | 7    | 8      | 9   | 10  | 11  | 12  |
    |:---|:----|:----|:-----|:----|:----|:----|:-----|:-------|:----|:----|:----|:----|
    | 1P | 小火炉 | 生煎锅 | 专业防空 | 瓜皮类 | 喷壶类 | 油灯类 | 投掷增益 | 雷电长棍面包 | 冰淇淋 | 木盘子 | 麦芽糖 | 咖啡粉 |
    | 2P | 小火炉 | 生煎锅 | 防漏卡  | 瓜皮类 | 喷壶类 | 油灯类 | 任意占位 | 雷电长棍面包 | 冰淇淋 | 木盘子 | 麦芽糖 | 咖啡粉 |

    * 任意占位: 电棍升级版中2P出现占位,是为了保持2P作为1P作战时,可以携带投掷增幅以同一卡组进行单人作战, 雷电长棍面包攻击间隔效果只取决于1P的电棍星级, 因为仅1P摆设上方电棍  
    * 防漏卡: 可以选择海星, 散点追踪(雪球兔/冰神), 群体轰炸(龙虾炮/火箭猪), 单体追踪(一转章鱼烧/忍忍鸡) 等卡片.

* 单人魔塔139卡组

    默认设置为[卡组3]

    |    | 1   | 2   | 3    | 4   | 5   | 6   | 7    | 8    | 9   | 10  | 11  | 12  |
    |:---|:----|:----|:-----|:----|:----|:----|:-----|:-----|:----|:----|:----|:----|
    | 1P | 小火炉 | 海星类 | 专业防空 | 瓜皮类 | 冰淇淋 | 喷壶类 | 辣椒粉类 | 辣椒粉类 | 瓜皮类 | 瓜皮类 | 木盘子 | 麦芽糖 | 

* 单人魔塔149卡组

    默认设置为[卡组3]

    |    | 1   | 2   | 3   | 4   | 5    | 6   | 7   | 8   | 9   | 10   | 11   | 12   | 13 |
    |:---|:----|:----|:----|:----|:-----|:----|:----|:----|:----|:-----|:-----|:-----|:---|
    | 1P | 布丁类 | 冰淇淋 | 小火炉 | 海星类 | 专业防空 | 喷壶类 | 瓜皮类 | 瓜皮类 | 瓜皮类 | 辣椒粉类 | 辣椒粉类 | 辣椒粉类 |


* 高难卡组

    默认设置为[卡组4]  
    用于攻克部分难度较高的关卡, 例如 街区 钟楼 音乐节日夜, 双人魔塔,
    如在雷城使用该卡组, 请不要用猫枪, 会导致瓦力鼠爆炸

    |    | 1   | 2   | 3    | 4   | 5   | 6    | 7    | 8    | 9      | 10  | 11  | 12  | 13  |
    |:---|:----|:----|:-----|:----|:----|:-----|:-----|:-----|:-------|:----|:----|:----|:----|
    | 1P | 小火炉 | 海星类 | 专业防空 | 瓜皮类 | 冰淇淋 | 辣椒粉类 | 辣椒粉类 | 辣椒粉类 | 雷电长棍面包 | 布丁类 | 咖啡粉 | 木盘子 | 麦芽糖 |
    | 2P | 小火炉 | 海星类 | 专业防空 | 瓜皮类 | 冰淇淋 | 辣椒粉类 | 辣椒粉类 | 辣椒粉类 | 雷电长棍面包 | 咖啡粉 | 木盘子 | 麦芽糖 |     |


* 雪山和冰跨卡组
    * 默认不设置为
    * 用于攻克雪山和冰跨8-9, 因为比较特别的需要海盐粉.

    |    | 1   | 2   | 3    | 4   | 5   | 6   | 7   | 8   | 9 | 10 | 11 | 12 |
    |:---|:----|:----|:-----|:----|:----|:----|:----|:----|:--|:---|:---|:---|
    | 1P | 小火炉 | 海星类 | 专业防空 | 瓜皮类 | 冰淇淋 | 喷壶类 | 海盐粉 | 咖啡粉 |   |    |
    | 2P | 小火炉 | 海星类 | 专业防空 | 瓜皮类 | 冰淇淋 | 喷壶类 | 海盐粉 | 咖啡粉 |   |    |



## 练度(默认卡组)

* 指定卡
  * 气泡: 推荐9星, 推荐1转, 否则可能会出现部分关卡中途大批量破裂拖慢进度.
  * 小火炉: 1P推荐12星2转. 低星会在部分难度较高关卡翻车.
  * 冰淇淋: 推荐9星. 
  * 海盐粉: 推荐9星. 推荐1转减费.
* 可同类替换
  * 承载卡
    * 会智能判断关卡可用承载卡及其位置, 在进入战斗后将自动添加至放卡方案顶. 上文的木盘子+麦芽糖+咖啡粉仅为示范.
    * 在卡组末尾带上水上+岩浆/海底/空中两张承载卡即可, 上文的木盘子+麦芽糖+咖啡粉仅为示范. 有多余空格可以带魔法软糖以加快铺场速度.
    * 推荐木盘子和麦芽糖是由于其平民且0耗火, 对通关速度有帮助.
  * 海星类: 炭烧海星 1P推荐[12星+技能7+2转]. 1转会在部分高难度关卡翻车. 2P至少[9星+1转].
  * 专业防空: 糖葫芦 推荐9星+技能5. 
  * 喷壶类: 需要5x5范围, 推荐狮子座精灵. 
  * 布丁类: 樱桃反弹布丁/狗布丁/牛布丁 等...
  * 瓜皮类: 包含 瓜皮护罩/处女座/赫拉/生日帽/扑克牌护罩 等...
  * 辣椒粉类: 包含 爆炸汪/辣椒粉/肉松清明粿, 均为廉价或赠送卡, 可以用 老鼠夹子\面粉袋\10周年烟花\产火充足情况下的其他炸弹卡 替代.
  * 油灯类: 任意全图照明卡, 包含 一转油灯/肉松清明粿/防萤草 等...

## 部署步骤

* 下载最新版本zip并解压
    * 脚本所在目录前的所有目录内不能有任何中文路径 (最新版本待测试, 目前来看中文路径似乎不影响运行了...)
    * 不要随意移动内部的文件, 如果你不知道你正在做什么.
* 根据上文要求 更改卡组 好友等 ...
* 启动 **点此一键启动.bat**, 可以为它创建快捷方式到桌面以方便启动.

## 大赛功能

* 大赛功能方案仅在每期大赛最后七天更新
* 大赛功能时, 使用 **<1-默认-1P和2P>** 进行战斗, 无编程基础不建议尝试修改, 不要用任何随意命名的方案抢占文件名排序时该方案的位置.
* 大赛功能时, 炭烧海星/糖葫芦炮弹/小火炉/木盘子等 **<任务常用卡不得进行同类替换>** , 魔法软糖只能用于替换麦芽糖不能用于替换木盘子.
* 大赛功能时, 请自备一张任意转职的 **<酒杯灯>** 绑定卡, 应对ban小火炉的情况, 在要求产火量的关卡补充产火.
* 大赛功能时, 请自备绑定的不在默认卡组内的任务所需卡, 常见的有换气扇, 可乐炸弹等...
* 大赛功能时, 卡组仅支持放在 **<第一个卡组位>** .
* 大赛功能开始前, 会在群内通知需要提前手打的部分高难度且有后续任务的关卡, 敬请留意.
* 大赛功能结束后, 部分高难度任务未完成, 为正常情况, 为方案故意设计而非疏漏.
* 大赛方案分为, 常规/单人/双人, 三个版本:
  * 常规为1P从头打到尾, 不保障2P完成有单人任务作为前置的任务.
  * 单人和双人为经过特别设计的常规方案拆成两段, 1P先运行单人部分, 完成后将2P名字填到1P再次运行单人部分, 最后正常完成多人部分, 可以最少次数完成两个号的所有任务.

## 其他须知

* 如点击启动按钮后不闪退且没有任何反应, 右键以管理员身份运行 main/main.exe 可以解决该问题.
* 本软件采用通用 **<全自动>** 进图组队+战斗, 由于鼠标唯一的特性, 执行期间:
    * 请 **<不要运行任何会抢占鼠标的应用>** , 包括但不限于: FPS/鼠标转动视角的游戏, 被远程控制等...
    * 可以放在后台进行游戏, 但 **<请不要最小化窗口>** , 会导致图像无法被获取.
* 做任务的卡在需要时, 将自动从对应的已有的 **<绑定卡片>** 中添加.
* 请 **<保证背包格子充足>** 后启动. 背包不足时, 会继续战斗, 可以通过保留物品数量为1防止某些战利品被卡掉,
  但无法保障签到或领取奖励等操作成功.
* 本软件出入开发测试阶段, 防bug损失建议:
    * **<设定二级密码 + 使用中不输入>**
    * **<有一定的礼卷防翻牌异常>**
    * **<高星不绑卡挂拍卖/提前转移>**
* 软件会自动截图记录战利品储存于软件根目录logs文件夹中, 若不需要或占用了过大储存, 可以将图片删除.

## 地图代号说明

地图代号包含: 地图类型-地图序号-关卡序号!
在1.3.1+版本将内置在软件中方便查看!(任务列表 - 点击查看关卡代号一览)
![image](https://github.com/StareAbyss/FoodsVsMiceAutoAssistant/assets/112901226/ae7de59c-7bfa-43d2-ac38-2147555c28e9)

# 自定义和部分自动战斗实现的说明

customize_todo 目录中为 <自定义战斗序列> 的配置文件.  
battle_plan 目录中为 <战斗方案> 的配置文件夹. 现已支持方案编辑器, 进行可视化互动式编辑.

### 文件名

请使用 **<数字-任务中文文本.json>** 作为文件名.  
由于本软件记忆系统默认排序下的序数(索引)作为配置文件以保存, 因此为保证默认方案的顺序不被打乱, 强烈建议 **<首位数字大于所有默认方案>**

### 自定义战斗序列

支持范围包括 NO CS OR EX 中的副本.
    
    [
        {
            "player": list, // 参战角色, [1]/[2]/[1,2]/[2,1] 分别代表 1P单人/2P单人/1P房主双人/2P房主双人
            "deck": int, // 使用第几个格子的卡组, 1-6
            "battle_plan_1p": int, // 1P使用的战斗方案的index序号, 名称排序从0开始从上到下
            "battle_plan_2p": int, // 2P使用的战斗方案的index序号, 名称排序从0开始从上到下
            "stage_id": str, // 地图代号, 详见地图代号部分
            "max_times": int, // 战斗次数
            "quest_card": str, // 任务需要的卡片, "None"为无, 有则填写 详见下文
            "ban_card_list": list[str,str,...], // 禁止携带的卡片, 空列表即为不ban, 详见下文
            "dict_exit": {
                "other_time_player_a": [str,str...], // 完成战斗后, 如果不是该副本最后一次作战, player_a 之后的退出动作代号序列
                "other_time_player_b": [str,str...], //完成战斗后, 如果不是该副本最后一次作战, player_b 之后的退出动作代号序列
                "last_time_player_a": [str,str...]  // 完成战斗后, 如果是该副本最后一次作战, player_a 之后的退出动作代号序列
                "last_time_player_b": [str,str...]  // 完成战斗后, 如果是该副本最后一次作战, player_b 之后的退出动作代号序列
            }
        },
        ...
    [


  
* 退出动作字符串(dict_exit)
    * "普通红叉"
    * "回到上一级"
    * "竞技岛"
    * "关闭悬赏窗口"
    * "美食大赛领取"
    * "游戏内退出"

## 战斗方案

### 放卡方式讲解

    战斗刚开始时, 将按顺序进行以下步骤：
        1. 放人物
        2. 铲地图自带卡
        3. 识别承载卡智能生成承载卡放置方案 (v0.9.0+)
    之后进入战斗循环, 直到发现战斗结束的标志物. 判断是否正常结束游戏.
    战斗循环期间, 本程序定义的放卡以轮为单位
    每轮会从上到下进行放置卡片操作
    卡片的 id 对应卡组格子序号 先点击选中
    然后根据 location 位置对应的 棋盘中序号("x-y") 点击对应位置
    该卡片参数 ergodic 遍历 为 true 真, 就按顺序点击所有对应位置, 
    该卡片参数 queue 队列 为 true 真, 一轮放卡后, 该卡的 location 第一个值将被挪到最后
    在放完每一张卡后, 一轮结束
    每轮最短时间为 7 + 需要放置位置最多的卡的数量 * 放卡间隔s 以保证选中后无效点击多次在接近最后一次成功放卡的情况下, 下一轮点击卡片时cd已经转好.
    
    值得一提的是, id 显然并不需要从小到大排序, 也不需要从上到下为[1,2,3,4,5,6]
    一个id也可以多次出现, 通过配置不同的 遍历和队列参数以及目标位置, 来达成更细致的战术效果

### 配置文件解析

这部分如果是使用战斗方案编辑器的用户可以直接跳过...

    {
        "player": [战斗网格str,...] // 战斗开始时放玩家角色的位置, 可以为多个
        "card": [
            {
                "tips": str,  //  只是提示文字, 可以不写
                "id": int,  //  对应卡组的第N个卡, 1和2是木盘和麦芽不可占用, 否则会破坏自动计算放承载卡的功能. 
                "name": str,  // <非转职完整中文卡片名称, 不写转职编号>, 用于ban卡, 一般可以乱填, 但必须有该字段.
                "location": [战斗网格str,...] // 该卡需要放的位置, 一般为多个, 若为[]空值, 即不放卡
                "ergodic" : bool, // 见下文
                "queue": bool, // 见下文
            },
        ... // 更多字典, 更多卡片
        ]
    }

* 战斗网格str :"x-y"
    * xy均为从1开始,
    * 以左上角为"1-1", 左下角为"1-7", 右上角为"9-1", 右下角为"9-7", 以此类推
    * 由于任务用卡片在卡组中的位置为根据card中list的长度 + 2(两种承载卡) 计算.

* 关于 添加任务卡片后(quest_card) 和 移除禁止卡片后(ban_card) 的方式
    * 在进入房间选择卡组后, 先根据 quest_card 字段, 在 resource/picture/card/房间 中 查找符合的图片, 并加入卡组
    * 再根据 ban_card_list 字段从现有卡组的前11张卡中, 在 resource/picture/card/房间 中 查找符合的图片, 移除已有部分
    * quest_card/ban_card 字段中一张卡片名称格式: 非转职完整中文卡片名称[-转职编号], 例如 炭烧海星-1 或 炭烧海星
        * 不含[-转职编号], 添加卡片时, 会从0-n序号查找, 加入序号最低的卡片, 移除卡片时, 会移除0-n序号中所有符合的卡片
        * 填写[-转职编号], 会添加或移除指定变种的卡片
    * 添加任务卡片后, 战斗方案中将会移除第七列所有非承载卡的放置, 并根据战斗方案中"card"字段中"id"的最大值+1, 作为其"id", 放置位置选择第七列
    * 移除禁止卡片后, 战斗方案中将根据"name"字段移除对应"card"字段中的dic, 并根据被移除的"id"字段, 使大于该"id"的其他卡片"id"字段-1, 以完成智能适配

* 任务卡的自动放卡机制
    * 软件会自动根据任务读取所需的任务卡, 在运行时放置于右手第一个空格, 并以 **配置方案中最大id + 1** 作为其顺序位置
    * 如有需携带不使用的卡, 可以将其location字段值设置为[], 即可不破坏自动使用任务卡功能

* 关于承载卡的放置
    * 在配置文件中录入了绝大部分关卡的承载卡需求情况.
    * 当该战斗为组队进行时, 1P和2P会分辨承担奇数和偶数位的承载卡放置任务.
    * v0.8.1 及以前
        * 当读取到对应关卡的承载卡配置时, 会自动将卡组的第一张卡认为是木盘子, 第二张卡认为是麦芽糖, 加入战斗方案, 自动放置.
        * 这是自定义的作战方案一般以第三张卡书写的开始的原因, 因为1/2被木盘子和麦芽糖默认占用了. 如果强行占用该位置, 会导致该功能失效, 出现意想不到的错误.
        * 是为了配置方案的通用性做出的规范和牺牲.
    * v0.9.0 以后
        * 在进入战斗后, 将根据根据识别到的所有垫子卡, 寻找关卡可用的承载卡的交集, 获取可用垫子卡
        * 根据可用垫子卡, 智能生成战斗方案, 添加至每一轮放卡的末位
        * 目前支持的卡片有 木盘子 麦芽糖 棉花糖 气泡 魔法软糖 (暂不支持过于冷门的猫猫盘等)

###  ergodic 和 queue 详解

ergodic(遍历); queue(队列) 代表了自动战斗放卡实现的两种重要思想.

* 不同版本中的含义
  * 在1.3.0以前 一轮大约7s自动放卡一遍所有被设置的卡片, 实际时间会根据总计需要的点击次数智能计算, 间隔为 最长有效放卡耗时 + 7s, 下文中的一轮指[最长有效放卡耗时 + 7s] 
  * 在1.3.0及以后 自动放卡进行了较大更改, 下文中[一轮]指[一张卡的一次尝试使用]

* 遍历, 代表了是否需要补充卡片的思想.    
  * 不遍历
    * 代表不需要补充卡片.
    * [每一轮] 只在 [该卡的第一个部署位置放一次]. 
  * 遍历 
    * 代表需要补充卡片.
    * [每一轮] 放卡都会以从上到下的顺序将 [该卡的所有部署位置放一次].

* 队列, 代表了是否有优先级的思想.      
  * 具体来说是让目标的 [部署位置列表(location_list)], 每一次放卡后, 将其第一位放到末尾.       
  * 不队列
    * 代表着该卡的从上到下顺序有优先级意义.
    * 会从前到后进行放置保证战略要地发挥作用.           
  * 队列该卡片
    * 代表着该卡均匀且广泛的布局更为重要.
    * 可以防止由于地图机制导致一直在错误的位置放卡损卡.     

将之组合, 可以得到玩家一般游戏过程中的四种常见策略(其中一种无意义)    
![image](https://github.com/StareAbyss/FoodsVsMouses_AutoAssistant/assets/112901226/99156bc9-fd39-4fe9-abe2-f42e4c1652cf)

还是不能理解吗~ 那看图表!  
假设你降你某卡的位置设定按顺序为 1 2 3 4

| 第N次使用该卡 | 遍历X 队列X | 遍历√ 队列X | 遍历X 队列√ | 遍历√ 队列√ |
|:--------|:--------|:--------|:--------|:--------|
| 1       | 1       | 1234    | 1       | 1234    |
| 2       | 1       | 1234    | 2       | 2341    |
| 3       | 1       | 1234    | 3       | 3412    |
| 4       | 1       | 1234    | 4       | 4123    |
| 5       | 1       | 1234    | 1       | 1234    |
 
# 免责声明

* 本软件使用 AGPL 3.0 协议开源、免费，仅供学习交流使用。若您遇到商家使用本软件进行代练并收费，可能是设备与时间等费用，产生的问题及后果与本软件无关.
* 本软件处于 **<开发测试阶段>** , 初次执行过程中建议 **<关注执行情况>** 
* 若执行中因bug导致任何问题, 请立刻 **<刷新游戏窗口>** + **<叉掉退出软件>**, 本人不负任何法律责任.
* 再次说明 防bug损失建议:
    * **<设定二级密码 + 使用中不输入>**
    * **<有一定的礼卷防翻牌异常>**
    * **<高星不绑卡挂拍卖/提前转移>**

# 开发者部署

## 项目结构

    root
     │
     ├─ config 配置文件 使用json格式
     │   ├─ settings.py 对应ui的主要配置文件
     │   └─ opt_stage_info.json 大部分常见关卡的信息, 在战斗时会读取用于去除对障碍的无效点击/铲除地图自带卡/放承载卡.
     │
     ├─ battle_plan 内含大量默认的战斗方案. 也可以自行添加自定义战斗方案
     │
     ├─ customize_todo 配置文件 使用json格式
     │   ├─ opt_customize_from_csv.py 用于将csv格式的战斗方案转化为对应的json格式, 美食大赛用
     │   ├─ opt_customize_todo.csv csv格式的自定义战斗方案
     │   ├─ opt_customize_todo.json 在执行自定义战斗时, 将读取此方案
     │   └─ opt_customize_todo_example.json 自定义战斗方案的模板文件
     │
     ├─ function(打包后为main)
     │   │   
     │   ├─ common 包含各种工具类, 后台进行 截图/找图/按键/点击等
     │   │   
     │   ├─ globals 包含各种全局变量类
     │   │   │
     │   │   ├─ get_paths.py 管理项目相对目录的全局变量表
     │   │   │
     │   │   ├─ init_resources.py 管理项目的预加载资源, 以减少I/O量
     │   │   │
     │   │   └─ thread_action_queue.py
     │   │       ├─ ThreadActionQueueTimer类 Qthread线程类, 用于定时执行动作队列, 包含添加键鼠操作到其队列中的函数.
     │   │       └─ T_ACTION_QUEUE_TIMER实例 前者的实例, 被MainWindow_2类调用其关闭和启动. 在需要添加键鼠操作时也被调用.
     │   │   
     │   ├─ battle 包含各种战斗类
     │   │   │
     │   │   ├─ FAABattle.py 项目核心
     │   │   │   └─FAABattle类 用于实现各种单账号的战斗操作并封装, 例如关卡和地图的进出, 卡片的使用
     │   │   │
     │   │   ├─ CardManager.py
     │   │   ├─ CardQueue.py
     │   │   └─ Card.py 关系较为复杂, 协同实现队列式战斗, 项目的技术核心
     │   │   
     │   ├─ script 主要功能函数
     │   │   │   
     │   │   ├─ analyzer_of_loot_logs.py 用于识图分析战利品记录, 并将其写入json文件
     │   │   │   
     │   │   ├─ FAA.py 项目核心
     │   │   │   └─ FAA类, 用于实现各种单账号的基本操作并封装, 例如关卡和地图的进出, 各种奖励的领取等, 项目核心
     │   │   │
     │   │   ├─ QMW_0_load_ui_file.py
     │   │   │   └─QMainWindowLoadUI类 继承自 QMainWindow类, 读取ui, 构筑少量通用方法, 包括有色消息打印, 软件开启的默认提示信息.
     │   │   │
     │   │   ├─ QMW_1_load_opt.py
     │   │   │   └─ QMainWindowLoadSettings类 继承自 QMainWindowLoadUI, 构筑[settings.josn - opt数组 - ui界面]间的数据传输方法, 构成配置文件管理.
     │   │   │
     │   │   ├─ QMW_2_service.py 项目核心
     │   │   │   ├─ QMainWindowService类 继承自 QMainWindowLoadSettings类 , 管理多线程任务的创建、开始和关闭, 实例化FFA类和Todo线程类, 管理事项流程的开始与结束, 并绑定槽函数函数和按钮事件
     │   │   │   ├─ TODO线程类 以两个FAA类实例为参数, 调用FAA中封装好的各项核心功能, 实现需要多账号同步/异步完成的各种功能, 实例化并激活CardManager类实现高复杂度战斗, 并在其run方法中执行整个事项流程.
     │   │   │   └─ main函数, 程序的主入口, 实例化MainWindow_2类并启动总体事件循环, 开启软件.
     │   │   │
     │   │   └─ scattered 散乱的杂项函数 
     │   │       ├─ get_channel_name.py 根据输入的1p2p名称和游戏名称, 获取窗口名称
     │   │       ├─ get_handle.py 根据窗口名称和需要的窗口层级, 获取对应句柄
     │   │       ├─ get_battle_plan_list.py 获取opt中的战斗方案名称列表, 返回为list
     │   │       └─ ...
     │   │   
     │   ├─ get_paths.py 根据exe和pycharm运行环境 获取root路径. 并保存了大多数资源文件的路径到 paths全局变量 以便调用.
     │   │   
     │   └─ main.py 主函数, 调用QMW_2_todo中的主函数作为快捷入口. 打包的目标
     │
     ├─ logs 战利品记录图保存位置
     │
     ├─ resource 资源文件
     │   │
     │   ├─ logo 图标资源
     │   │   
     │   ├─ picture 图片资源文件
     │   │   │
     │   │   ├─ card 卡片图片, 用于在ban卡和添加任务卡时, 寻找点击
     │   │   │   ├─ 战斗 战斗中的卡片截图, 为有费用使用的亮度版本, 用于识别承载卡位置
     │   │   │   └─ 房间 房间中的卡片截图, 用于携带任务卡或移除禁用卡
     │   │   │ 
     │   │   ├─ common 一些通用的界面图片
     │   │   │   ├─ 用户自截 需要用户自己截图才能正常使用的部分, 包含两张用于在QQ大厅服进行登录的截图, 一张用于完成跨服副本的截图
     │   │   │   └─ ... 
     │   │   │ 
     │   │   ├─ item 背包中各种物品的截图, 用于使用消耗品
     │   │   ├─ map 大地图中各个地区的图片, 用于跳转
     │   │   ├─ number 用于识图房间号, 暂时无用
     │   │   ├─ stage 各个关卡的图片, 用于选择正确的关卡
     │   │   ├─ stage_ready_cheack 房间界面左下的地图图片, 原用于识别当前所在关卡, 现废弃
     │   │   ├─ task_guild 公会任务相关图片, 其中带序号的文件夹代表从上到下第几个任务
     │   │   ├─ task_spouse 情侣任务相关图片, 其中带序号的文件夹代表从左到右第几个任务
     │   │   └─ get_new_picture.py 用于截图获取房间界面左下角的地图图片, 现废弃
     │   │   
     │   └─ ui .ui文件
     │
     ├─ README.md 自述文档
     ├─ LICENSE 开源协议, 也用于确定项目根目录位置
     └─ requirements.txt 使用的lib带版本

路径做了处理 pycharm和打包为.exe(以main.py为目标)后都可以轻松运行~ 
Link Start!

# 致谢

* 图像识别：[opencv](https://github.com/opencv/opencv.git)
* 图形化界面：[PyQt5](https://github.com/PyQt5/PyQt5.git)
* 感谢交流群的各位小伙伴对本软件的测试和相关建议 ~
* 感谢八重垣天知, 对本软件的开发和测试的大力支持!
