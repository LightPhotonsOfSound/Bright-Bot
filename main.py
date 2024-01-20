import discord
from discord.ext import commands
import openai
import asyncio 
import os


global correct_option  
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
  
    if message.content.startswith('!funfact'):
      prompt = "Generate a random fun fact"
      response = openai.Completion.create(
        model ='gpt-3.5-turbo-instruct',
        prompt=prompt,
        max_tokens=100,
      )
      await message.channel.send(response.choices[0].text)   
    if message.content.startswith('!translate'):
      if message.content.startswith('!translate spanish'):
        prompt = "Translate this into spanish: " + message.content.split('!translate spanish ')[1]
        response = openai.Completion.create(
          model ='gpt-3.5-turbo-instruct',
          prompt=prompt,  
        )
        translation = response.choices[0].text
        prompt = "Give the english pronounciation of the spanish text: " + translation
        response = openai.Completion.create(
          model ='gpt-3.5-turbo-instruct',
          prompt=prompt,
        )
        pronounciation = response.choices[0].text
        await message.channel.send(f"The translation is: {translation}\n\n The pronounciation is :{pronounciation}")
      elif message.content.startswith('!translate french'):
        prompt = "Translate this into french: " + message.content.split('!translate french ')[1]
        response = openai.Completion.create(
          model ='gpt-3.5-turbo-instruct',
          prompt=prompt,  
        )
        translation = response.choices[0].text
        prompt = "Give the english pronounciation of the french text: " + translation
        response = openai.Completion.create(
          model ='gpt-3.5-turbo-instruct',
          prompt=prompt,
        )
        pronounciation = response.choices[0].text
        await message.channel.send(f"The translation is: {translation}\n\n The pronounciation is :{pronounciation}")

      elif message.content.startswith('!translate german'):
        prompt = "Translate this into german: " + message.content.split('!translate german ')[1]
        response = openai.Completion.create(
          model ='gpt-3.5-turbo-instruct',
          prompt=prompt,  
        )
        translation = response.choices[0].text
        prompt = "Give the english pronounciation of the german text: " + translation
        response = openai.Completion.create(
          model ='gpt-3.5-turbo-instruct',
          prompt=prompt,
        )
        pronounciation = response.choices[0].text
        await message.channel.send(f"The translation is: {translation}\n\n The pronounciation is :{pronounciation}")

      elif message.content.startswith('!translate mandarin'):
        prompt = "Translate this into mandarin: " + message.content.split('!translate mandarin ')[1]
        response = openai.Completion.create(
          model ='gpt-3.5-turbo-instruct',
          prompt=prompt,  
        )
        translation = response.choices[0].text
        prompt = "Give the english pronounciation of the mandarin text: " + translation
        response = openai.Completion.create(
          model ='gpt-3.5-turbo-instruct',
          prompt=prompt,
        )
        pronounciation = response.choices[0].text
        await message.channel.send(f"The translation is: {translation}\n\n The pronounciation is :{pronounciation}")

      elif message.content.startswith('!translate hindi'):
        prompt = "Translate this into hindi: " + message.content.split('!translate hindi ')[1]
        response = openai.Completion.create(
          model ='gpt-3.5-turbo-instruct',
          prompt=prompt,  
        )
        translation = response.choices[0].text
        prompt = "Give the english pronounciation of the hindi text: " + translation
        response = openai.Completion.create(
          model ='gpt-3.5-turbo-instruct',
          prompt=prompt,
        )
        pronounciation = response.choices[0].text
        await message.channel.send(f"The translation is: {translation}\n\n The pronounciation is :{pronounciation}")

      elif message.content.startswith('!translate arabic'):
        prompt = "Translate this into arabic: " + message.content.split('!translate arabic ')[1]
        response = openai.Completion.create(
          model ='gpt-3.5-turbo-instruct',
          prompt=prompt,  
        )
        translation = response.choices[0].text
        prompt = "Give the english pronounciation of the arabic text: " + translation
        response = openai.Completion.create(
          model ='gpt-3.5-turbo-instruct',
          prompt=prompt,
        )
        pronounciation = response.choices[0].text
        await message.channel.send(f"The translation is: {translation}\n\n The pronounciation is :{pronounciation}")
      

      elif message.content.startswith('!translate russian'):
        prompt = "Translate this into russian: " + message.content.split('!translate russian ')[1]
        response = openai.Completion.create(
          model ='gpt-3.5-turbo-instruct',
          prompt=prompt,  
        )
        translation = response.choices[0].text
        prompt = "Give the english pronounciation of the russian text: " + translation
        response = openai.Completion.create(
          model ='gpt-3.5-turbo-instruct',
          prompt=prompt,
        )
        pronounciation = response.choices[0].text
        await message.channel.send(f"The translation is: {translation}\n\n The pronounciation is :{pronounciation}")

      elif message.content.startswith('!translate english'):
        text_to_translate = message.content.split('!translate english ')[1]
        prompt = f"Translate this into English: {text_to_translate}, and tell which language the text is from"
        response = openai.Completion.create(
            model='gpt-3.5-turbo-instruct',
            prompt=prompt,
            max_tokens=500,
        )
        translation = response.choices[0].text
        await message.channel.send(f"The translation is: {translation}")
      
      else:
        await message.channel.send("At the moment, we only provide translation to english, spanish, french, german, mandarin, hindi, arabic, russian... but feel free to use other all functions without hesitation!")
      
      
    if message.content.startswith('!help'):
      await message.channel.send("***Commands***\n**!help** - Shows this message\n**!ask (question)** - Asks ChatGPT a question\n**!8ball** - Asks the magic 8ball a question to get a fun response\n**!trivia (topic)** - Generates a trivia question based on the topic\n**!answer** - Alows you to answer a trivia question**!translate (target_language) (text)** - Translates the text to the specified language\n**!funfact** - Generates a random fun fact\n**!translate (target_language) (text)** - Translates the text to the specified language and gives the english pronounciation")

    
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