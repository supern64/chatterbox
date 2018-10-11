# ChatterBox bot
# Requires chatterbot and discord.py rewrite installed
# Configs should be put in a file called config.json

import discord
import json
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
chatbot = ChatBot("Roboto",
                    logic_adapters=[
                      "chatterbot.logic.BestMatch",
                      "chatterbot.logic.MathematicalEvaluation",
                      {
                        'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                        'input_text': 'Who am I talking to?',
                        'output_text': "You're talking to an AI"
                      },
                      "chatterbot.logic.TimeLogicAdapter",
                      {
                        'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                        'threshold': 0.65,
                        'default_response': ['I am sorry, but I do not understand.',
                                            "Umm... I don't get it...",
                                            "Sorry. I don't really get it.",
                                            "I didn't understand what you meant. Sorry."]
                      }])
chatbot.set_trainer(ChatterBotCorpusTrainer)
try:
    config = json.load(open('config.json'))
    token = config['token']
    status = config['status']
    prefix = config['prefix']
except:
    print("Loading JSON failed. Make sure you have the correct format of configuration in a file named config.json")
client = discord.Client()

@client.event
async def on_ready():
    print("{0.name} is ready!".format(client.user))
    if status == "":
        pass
    else:
        game = discord.Game(status)
        await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author == client.user or message.author.bot:
        return
    if message.content.startswith(message.guild.me.mention) or message.content.startswith("{0}chat".format(prefix)):
        if message.content.startswith(message.guild.me.mention):
            arg = message.content[len(message.guild.me.mention):].strip()
        else:
            arg = message.content[len('{0}chat'.format(prefix)):].strip()
        await message.channel.trigger_typing()
        await message.channel.send("{0.mention}, {1}".format(message.author, chatbot.get_response(arg)))
    elif message.content == "{0}train".format(prefix):
        await message.channel.send("Training... (This might take a while)")
        chatbot.train("chatterbot.corpus.english")
        await message.channel.send("Done!")
client.run(token)