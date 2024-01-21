import discord
from discord.ext import commands
import openai
import asyncio 
import os
from tabulate import tabulate
import requests

global correct_option  
leaderboard = {}
responses = {}
TOKEN = os.environ['TOKEN']
openai.api_key = os.environ['API']
leaderboard = {}
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
    if message.content.startswith('!suggestbook'):
      prompt = f"Suggest a book based on the following theme/themes : {message.content.split('!suggestbook')}. Also give some background information on the book."
      response = openai.Completion.create(
        model ='gpt-3.5-turbo-instruct',
        prompt=prompt,
        max_tokens=100,
      )
      await message.channel.send(response.choices[0].text)
      await message.channel.send(response.choices[0].text)   

    if message.content.startswith('!translate'):
      message_content = message.content.split(' ', 1)[1]
      #message_content = message_content.split(' ', 1)[1]
      prompt = "Detect the language of the following text: " + message_content
      response = openai.Completion.create(
        model = 'gpt-3.5-turbo-instruct',
        prompt=prompt,
      )
      answer = response.choices[0].text
      await message.channel.send(f"According to our sources, this language seems to be : {answer}\n")
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
        prompt = f"Translate this into English: {text_to_translate}"
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
      await message.channel.send("***Commands***\n**!help** -     Shows this message\n**!ask (question)** - Have a doubt that needs to be answered? Use the ask function to ask a general question to BrightBot!\n**!8ball** - The function of fun has arrived! Use the 8ball function to have some fun in your study breaks and free time. Here you can input a topic you want to bot to talk about, and watch as BrightBot gives the spiciest of answers.\n**!trivia (topic)** - Are your studies too boring? Don't worry, help has arrived. Use the Trivia function to generate a trivia question on any topic of your choice. While entering the function, don't forget to specify the time limit you want to be able to answer in, which will help in increasing your thinking speed. Collaborate with your friends to double the fun!\n**!answer** - Can you think of an answer? If you can, use the answer function to answer the trivia questions and to check if your answer is right.\n**!translate** (target_language) (text) - Can't understand a certain language? Yet again, help has arrived. Use the translate function to translate text from one language to another.\n**!funfact** - Want to know more about the world? The fun fact function will generate a random fun fact that will provide you with new information!\n**!leaderboard** - What makes quizes fun without a proper pointing system? Use this command to find the score of each user. Remember, to get more points, answer more trivia questions!\n**!news** - Get the latest and top 10 trending news straight from BBC to be updated on world happenings and events.\n**!suggestbook** - Searching for a book that gives you the information you want to know about, but can't find any? Look no further! With the suggest book function, find the books you are looking for with specific topics and paticular information!")

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
      guess = message.content.lower()[8]
      print(f"{message.author} guessed: {guess}")
      global guesser
      guesser = message.author
      global responses
      responses.update({str(guesser) : guess})

    if message.content.startswith('!trivia'):
      responses.clear()
      if len(message.content) > 10:
        time = '20'
        time = message.content[-2:]
        time = int(time)

        if time < 10 or time > 40:
          await message.channel.send("The time must be between 10 and 40 seconds! Try again.")
        else:
          topic = message.content[8:-2]
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
          answer_prompt = f"This is a multiple choice question : {generated_question}\nProvide an answer with some explaination Example :' A. .. ' Remember, the answer has to first start with the correct letter and then go to the rest. "

          # Request an answer based on the generated question
          answer_response = openai.Completion.create(
              model ='gpt-3.5-turbo-instruct',
              prompt=answer_prompt,
              max_tokens=400,
             # chat_completion=True
          )

          # Extract the generated answer from the response
          generated_answer = answer_response['choices'][0]['text'].strip()
          correct_option = generated_answer.lower()[0]
          print(f"Correct option: {correct_option}")

         # if message.content.startswith('!leaderboard'):


          # Send the generated question and answer to the Discord channel
          await message.channel.send(f"You have {time} seconds to answer this: {generated_question}")
          await asyncio.sleep(time)

          await message.channel.send(f"The answer is : {generated_answer}")
          print(responses)
          val_list = list(responses.values())
          key_list = list(responses.keys())
          ind = val_list.index(correct_option)
          username = key_list[ind]
          print(responses)
          await message.channel.send(f"\n***{username} guessed it right!!\nCongratulations, you have recieved 1 point! KEEP IT UP!***")
          global leaderboard
          leaderboard[username] = leaderboard.get(username, 0) + 1
          print(leaderboard)

    if message.content.startswith('!leaderboard'):
      sorted_dict = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
      final_leaderboard = tabulate(sorted_dict, headers=["Name", "Score"], tablefmt="simple")
      print(final_leaderboard)  
      await message.channel.send("\t\t\t***LEADERBOARD***\n" + final_leaderboard)
    if message.content.startswith('!news'):      
      prompt = "Give me the latest news in english"
      query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": os.environ['newsAPI']
      }
      main_url = " https://newsapi.org/v1/articles"
      res = requests.get(main_url, params=query_params)
      open_bbc_page = res.json()
      article = open_bbc_page["articles"]
      results = []
      for ar in article:
          results.append(ar["title"])
      await message.channel.send(f"**TRENDING NEWS IN BBC :**")
      for i in range(len(results)):
          await message.channel.send (f"{i+1}. {results[i]}")
          

    

      
    else:
      return


bot.run(TOKEN)
