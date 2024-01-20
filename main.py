import discord
from discord.ext import commands
import openai
import asyncio
import os

DISCORD_TOKEN = os.environ['TOKEN'] # gets token from environment variable
openai.api_key = os.environ['OPENAI_API_KEY'] # gets api key from environment variable

intents = discord.Intents.all()
intents.messages = True #sets message intents as true, to enable the bot to send messages
bot = discord.Client(command_prefix='!', intents=intents)

responses = {} #dictionary that stores the responses of the users for the MCQ's

@bot.event
async def on_ready():
  print(f' We have logged in as {bot.user.name}') #this for confirmation on our side

@bot.event
async def on_message(message):
  if message.author == bot.user: # prevents the bot from chatting with itself, and 
    return


  if message.content.startswith('!help'):
    await message.channel.send("!ask (your question) - Asks ChatGPT a question. \n!8ball (your question) - Gives an 8ball response for . \n!help - Shows this message. !trivia (topic) - Generates a multiple-choice question on the given topic \n!answer (your answer) - Allows you to give your answer for the multiple-choice question to see if you're right. ") #describes what the command to chatgpt is and what the command is

  if message.content.startswith('!ask'):
    askprompt = message.content.split("!ask")
    response = openai.Completion.create(
      model = "gpt-3.5-turbo-instruct",
      prompt = askprompt,
      max_tokens = 500
      )
    await message.channel.send(response.choices[0].text)


  if message.content.startswith('!trivia'):
    topic = message.content.split("!trivia")
    triviaprompt = (f"Create a multiple choice question with 4 options on the topic: {topic}. ")
    response = openai.Completion.create(
      model = "gpt-3.5-turbo-instruct",
      prompt = triviaprompt,
      max_tokens = 500,
      temperature = 0.7
      )
    generated_question = await message.channel.send(response.choices[0].text)


  if message.content.startswith('!answer'):
    global guess
    guess = message.content.lower()[8]
    response.update({message.author: guess})
    print = (f"{message.author} guessed {guess}")



  if message.content.startswith('!8ball'):
    eightball = message.content.split("!8ball")
    ballprompt = (f"Answer the question : '{eightball}'. Once you are done answering the question, give a small explaination on why you chose the answer you gave. Remember to make it funny and spicy. Don't worry about insulting anyone because this is made just for entertainment purposes. This is an 8ball so make it as creative as possible ")
    response = openai.Completion.create(
      model = "gpt-3.5-turbo-instruct",
      prompt = ballprompt,
      max_tokens = 400,
    )
    await message.channel.send(response.choices[0].text)



bot.run(DISCORD_TOKEN)

