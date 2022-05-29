#Telegram Bot to find the steam account associated with the entered ID

import telebot
import random
import time

# Default Values
API_TOKEN_FILE = "user_token.txt"


try:
    with open(API_TOKEN_FILE, 'r') as token_file:
        bot_token = token_file.read().strip()
except FileNotFoundError:
    print("No API Token file found")
    exit(1)

bot = telebot.TeleBot(bot_token)


def checkID(message):                                               #Checks to see if entered value is correct
    if message.text.isdigit() and len(message.text) <= 17:          #Steam ID cannot be alphabetical or longer than 17 characters
        return True
    elif message.text[0] == '/':
        bot.send_message(message.chat.id, 'I dont understand that command')
    else:
        bot.send_message(message.chat.id, 'The ID you sent is invalid.')

def convertID(ID):
    return int(ID) + 76561197960265728                              #Converts SteamID32 to SteamID64


@bot.message_handler(commands=['start'])                            #Start Command
def bot_start(message):
    bot.send_message(message.chat.id, 'You can send me a Steam or Dota 2 ID to find the account')

@bot.message_handler(commands=['help'])                             #Help Command
def bot_help(message):
    bot.send_message(message.chat.id, 'You can send me a Steam or Dota 2 ID to find the account')
    bot.send_message(message.chat.id, 'For Example, 76561198312899054 or 352633326')

@bot.message_handler(commands=['random'])                           #Generates random steam IDs
def randomID(message):
    random_ID = random.randint(1,1000000000)
    bot.send_message(message.chat.id, f'https://steamcommunity.com/profiles/{convertID(random_ID)}')

@bot.message_handler(commands=['spam'])                             #Wonder what this does? xD
def spammer(message):
    while True:
        random_ID = random.randint(1,1000000000)
        bot.send_message(message.chat.id, f'https://steamcommunity.com/profiles/{convertID(random_ID)}')
    
        
@bot.message_handler(func=checkID)                                  #Main code to get the steam accounts
def SteamID(message):                                               #Converts SteamID32 to SteamID64 using
    try:                                                            #the above function if required and then
        if len(message.text) <17:                                   #puts it after the general URL for accounts
            ID = convertID(message.text)  
            bot.send_message(message.chat.id, f'https://steamcommunity.com/profiles/{ID}')
        elif len(message.text) ==17:
            ID = message.text
            bot.send_message(message.chat.id, f'https://steamcommunity.com/profiles/{ID}')
        else:
            bot.send_message(message.chat.id, 'Error!')
    except:
        bot.send_message(message.chat.id, 'Send me the Account ID rather than the username')
        bot.send_message(message.chat.id, 'For Example, 76561198312899054 or 352633326')
    
    
print("Script Running...")
while True:                                                         #Makes sure the bot is constantly active
    try:                                                            #If it goes down then retries after 10 secs
        bot.polling()
    except:
        time.sleep(10)

