from hoshino.util import get_list_environ, get_environ, get_bool_environ
import os

"""这是一份实例配置文件

将其修改为你需要的配置，并将文件夹config_example重命名为config
"""

# hoshino监听的端口与ip
# HOST = get_environ('HOST', '0.0.0.0')  # Windows部署使用此条配置
# HOST = '172.17.0.1'   # linux + docker使用此条配置
# docker桥的ip可能随环境不同而有变化
# 使用这行命令`ip addr show docker0 | grep -Po 'inet \K[\d.]+'`查看你的docker桥ip
# HOST = '172.18.0.1'   # 阿里云的linux + docker多数情况是这样
HOST = '0.0.0.0'      # 开放公网访问使用此条配置（不安全）
PORT = int(get_environ('PORT', 8000)) #这里配置机器人默认监听端口

DEBUG = True if os.environ.get('DEBUG') else False  # 调试模式

SUPERUSERS = get_list_environ('SUPERUSERS', [123456])  # 填写超级用户的QQ号，可填多个用半角逗号","隔开
NICKNAME = get_environ('NICKNAME', '星乃')  # 机器人的昵称。呼叫昵称等同于@bot，可用元组配置多个昵称

COMMAND_START = {get_environ('COMMAND_START', '')}  # 命令前缀（空字符串匹配任何消息）
COMMAND_SEP = set()  # 命令分隔符（hoshino不需要该特性，保持为set()即可）

USE_CQPRO = True  # 是否使用Pro版酷Q功能（酷Q已凉，Mirai默认支持CQPRO特性）

# 发送图片的协议
# 可选 http, file, base64
# 建议Windows部署使用file协议
# 建议Linux部署配合本地web server使用http协议
# 如果你不清楚上面在说什么，请用base64协议（发送大图时可能会失败）
RES_PROTOCOL = get_environ('RES_PROTOCOL', 'file') #默认使用文件方式
# 资源库文件夹，需可读可写，windows下注意反斜杠转义
RES_DIR = get_environ('RES_DIR', r'./res/') #该地址表示"res"文件夹应位于与启动程序"run.py"处于同一目录下
# 使用http协议时需填写，原则上该url应指向RES_DIR目录
RES_URL = get_environ('RES_URL', 'http://127.0.0.1:5000/static/')

# 允许私聊
ALLOW_PRIVATE = get_bool_environ('ALLOW_PRIVATE', True)
# ICP内容
ICP_CONTENT = get_environ('ICP_CONTENT')
# 启用的模块
# 初次尝试部署时请先保持默认
# 如欲启用新模块，请认真阅读部署说明，逐个启用逐个配置
# 切忌一次性开启多个
# 请根据各自情况开启
MODULES_ON = {
    # 'authMS', #机器人授权插件
    'auth_inspect', #原版自带授权
    'bot_manager', #群管理
    'bot_manager_web', #群管理网页版
    'dice', #骰娘
    'group_master', #群聊天功能，如反骑空士，屏蔽词禁言拉黑，群回复，随机复读，加\退群提醒，睡眠套餐
    # 'hourcall', #报时功能
    # 'kancolle',
    # 'mikan',
    # 'pcrclanbattle', #Hoshino自带会战，本程序为yobot缝合怪版故不启用
    'priconne', #jjc查询，随机插件
    # 'setu', #色图插件，使用的Lolicon API https://api.lolicon.app/#/setu
    # 'translate',  #翻译姬
    # 'twitter', #推特转发功能，需要推特开发者账号API
    'yobot', #yobot会战管理插件
    'buy_potion_reminder', #买药提醒
    'clanrank', #工会排名查询查件
    'clanbattle_report', #生成会战报告
    # 'shitu', #识图
    'shifan', #识番
    'voiceguess', #根据语音猜角色
    'pcravatarguess', #根据头像猜角色
    'pcrdescguess', #根据描述猜角色
}
