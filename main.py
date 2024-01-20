import discord
from discord.ext import commands
import openai
import asyncio 
import os
import datetime
import random
from discord.ext import tasks


global correct_option  # Add this line after the import statements
responses = {}
TOKEN = os.environ['TOKEN']
openai.api_key = os.environ['API']

intents = discord.Intents.all()
intents.messages = True

bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

      
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    print(f"{message.author} said: '{message.content}'")
  
    @tasks.loop(hours=24)
    async def daily_fact():

        for guild in bot.guilds:
            text_channels = [channel for channel in guild.channels if isinstance(channel, discord.TextChannel)]
            if text_channels:
                channel = text_channels[0]
                break
        else:
            print("No text channels found in any guild.")
            return

        # Get a random fact
        fact = get_random_fact()

        # Send the daily fact to the channel
        await channel.send(f"📚 Daily Fact: {fact}")

    def get_random_fact():
        # Use OpenAI GPT to generate a random fact
        response = openai.Completion.create(
            model = "gpt-3.5-turbo-instruct",
            prompt="Generate a random fact:",
            max_tokens=150
        )
        return response['choices'][0]['text'].strip()
    if message.content.startswith('!help'):
      await message.channel.send("***Commands***\n**!help** - Shows this message\n**!ask (question)** - Asks ChatGPT a question\n**!8ball** - Asks the magic 8ball a question to get a fun response\n**trivia (topic)** - Generates a trivia question based on the topic\n**!answer** - Alows you to answer a trivia question")
    if message.content.startswith('!ask'):
        answer_prompt = message.content[4:]
        response = openai.Completion.create(
          model ='gpt-3.5-turbo-instruct',
          prompt=answer_prompt,
          max_tokens=500,
        )
        await message.channel.send(response.choices[0].text)            
    if message.content.startswith('!8ball'):
      answer_prompt = message.content[4:]
      response = openai.Completion.create(
        model ='gpt-3.5-turbo-instruct',
          prompt=f"Answer this question and after that give some more background information to support it(make it short) : '{answer_prompt}'Add a little spice into your message to make it fun (no one will take it personally so don't worry). Say stuff like that to make it entertaining ;). Your advice won't be taken seriously so say something funny. This is an 8ball so it doesn't have to be realistic, Insult someone, kill someone, make someone ugly, you can do anything",
        max_tokens=400,
      )
      await message.channel.send(response.choices[0].text) 
    topic = "math"
    if message.content.startswith('!answer'):
      global guess
      guess = message.content.lower()[7]
      print(f"{message.author} guessed: {guess}")
      global guesser
      guesser = message.author
      global responses
      responses.update({str(guesser) : guess})

    if message.content.startswith('!trivia'):
      responses.clear()
      if len(message.content) > 6:
        topic = message.content.split('!trivia ')[1]
        prompt1 = f'Create a multiple-choice question, (make only 4 options) on the topic of "{topic}" and dont give the answer with the question.'

        response = openai.Completion.create(
            model ='gpt-3.5-turbo-instruct',
            prompt=prompt1,
            max_tokens=150,
          # chat_completion=True
        ) 

        # Extract the generated question from the response
        generated_question = response['choices'][0]['text'].strip()



        # Create a dynamic prompt for the answer
        answer_prompt = f"This is a multiple choice question : {generated_question}\nProvide an answer with some explaination Example :' A. .. ' "

        # Request an answer based on the generated question
        answer_response = openai.Completion.create(
            model ='gpt-3.5-turbo-instruct',
            prompt=answer_prompt,
            max_tokens=400,
           # chat_completion=True
        )
      #  await asyncio.sleep(15)

        # Extract the generated answer from the response
        generated_answer = answer_response['choices'][0]['text'].strip()
        correct_option = generated_answer.lower()[0]
        print(f"Correct option: {correct_option}")

        # Send the generated question and answer to the Discord channel
        await message.channel.send(f"You have 20 seconds to answer this: {generated_question}")
        await asyncio.sleep(20)

        await message.channel.send(f"The answer is : {generated_answer}")
        print(responses)
        val_list = list(responses.values())
        key_list = list(responses.keys())
        ind = val_list.index(correct_option)
        username = key_list[ind]
        await message.channel.send(f"\n***{username} guessed it right!!***")




    else:
      return


bot.run(TOKEN)