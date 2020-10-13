# -*- coding: utf-8 -*-
#倒入模块
from wxpy import *
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer


#初始化机器人
#chatbot = ChatBot('Dr.Qian')
chatbot = ChatBot(
            'Dr.Qian',
            #指定logic模块
            logic_adapters = [
            "chatterbot.logic.BestMatch",
            "chatterbot.logic.MathematicalEvaluation",
            "chatterbot.logic.TimeLogicAdapter"
            ],
            database = 'chatterbot'
)

#用中文语料库训练机器人
chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train('chatterbot.corpus.chinese')

#特定语句训练
#chatbot.set_trainer(ListTrainer)
#chatbot.train(['你叫什么',
#             '你好，我是钱博士，你也可以叫我天才钱'])

#接入微信机器人
bot = Bot(cache_path = True)

@bot.register(Group, TEXT)
def reply(msg):
    print(msg)
    if msg.is_at:
        return chatbot.get_response(msg.text).text

#堵塞线程、并进入 Python 命令行
embed()
