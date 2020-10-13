import itchat
from itchat.content import *
#回复用ID
userId = ''

# 群信息
@itchat.msg_register([TEXT,PICTURE], isGroupChat = True)
def group_reply(msg):
    group_id = msg['FromUserName'];
    group = itchat.search_chatrooms(userName=group_id)
    print(group['NickName'] + "群的 " + msg['ActualNickName'] + " 发来的消息\n" + getText(msg) )

    if msg.isAt:
        global userId
        userId = msg['FromUserName']
        xbAnswer(msg)


# 公众号消息
@itchat.msg_register([TEXT,PICTURE], isMpChat = True)
def map_reply(msg):
    text = getText(msg)
    global userId
    if msg['Type'] == 'Picture':
        msg['Text'](msg['FileName'])
        itchat.send_image(msg['FileName'],userId)
    else:
        itchat.send_msg(text,userId)


# 获取文字
def getText(msg):
    if msg['Type'] == 'Text':
        return msg['Text']
    else:
        return "发送的其他类型回复"

# 向智能小冰提问
def xbAnswer(msg):
    xb = itchat.search_mps(name='小冰')[0]
    quest = getText(msg)
    if msg['Type'] == 'Picture':
        msg['Text'](msg['FileName'])
        itchat.send_image(msg['FileName'],xb['UserName'])
    else:
        itchat.send_msg(quest, xb['UserName'])

itchat.auto_login(hotReload = True)
itchat.run()
