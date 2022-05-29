#Telegram Bot to find the steam account associated with the entered ID

import telebot
import random
import time

# Default Values
API_TOKEN_FILE = "user_token.txt"       # API Token file name
RETRY_INTERVAL = 10                     # Seconds to wait before retrying if bot ever goes down


# Getting API Token from file
try:
    with open(API_TOKEN_FILE, 'r') as token_file:
        bot_token = token_file.read().strip()
except FileNotFoundError:
    print("No API Token file found")
    exit(1)
bot = telebot.TeleBot(bot_token)


# Checks to see if entered value is correct
def checkID(message):                                               
    # Steam ID cannot be alphabetical or longer than 17 characters
    if message.text.isdigit() and len(message.text) <= 17:          
        return True
    elif message.text[0] == '/':
        bot.send_message(message.chat.id, 'I dont understand that command')
    else:
        bot.send_message(message.chat.id, 'The ID you sent is invalid.')

#Converts SteamID32 to SteamID64
def convertID(ID):
    return int(ID) + 76561197960265728                              


# Telegram Chat Commands
# Start Command
@bot.message_handler(commands=['start']) 
def bot_start(message):
    bot.send_message(message.chat.id, 'You can send me a Steam or Dota 2 ID to find the account')

# Help Command
@bot.message_handler(commands=['help'])
def bot_help(message):
    bot.send_message(message.chat.id, 'You can send me a Steam or Dota 2 ID to find the account')
    bot.send_message(message.chat.id, 'For Example, 76561198312899054 or 352633326')

# Generates random steam IDs
@bot.message_handler(commands=['random'])                           
def randomID(message):
    random_ID = random.randint(1,1000000000)
    bot.send_message(message.chat.id, f'https://steamcommunity.com/profiles/{convertID(random_ID)}')

# Wonder what this does? xD
@bot.message_handler(commands=['spam'])
def spammer(message):
    while True:
        random_ID = random.randint(1,1000000000)
        bot.send_message(message.chat.id, f'https://steamcommunity.com/profiles/{convertID(random_ID)}')
    
        
# Gets the Steam account URL and sends it in chat
@bot.message_handler(func=checkID)                                 
def SteamID(message):                                             
    try:                                                         
        if len(message.text) < 17:  
            ID = convertID(message.text)  
            bot.send_message(message.chat.id, f'https://steamcommunity.com/profiles/{ID}')
        elif len(message.text) == 17:
            ID = message.text
            bot.send_message(message.chat.id, f'https://steamcommunity.com/profiles/{ID}')
        else:
            bot.send_message(message.chat.id, 'Error!')
    except:
        bot.send_message(message.chat.id, 'Send me the Account ID rather than the username')
        bot.send_message(message.chat.id, 'For Example, 76561198312899054 or 352633326')


def main(retry_interval):    
    print("Script Running...")
    # Retries after a certain time if bot ever goes down
    while True:                                   
        try:                                     
            bot.polling()
        except:
            time.sleep(retry_interval)

main(RETRY_INTERVAL)
