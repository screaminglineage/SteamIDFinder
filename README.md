# SteamIDFinder
Telegram bot which can find a steam account from a given Steam ID or Dota 2 ID

## Contents
  1.  [Introduction](#introduction)
  2.  [Installation](#installation)
  3.  [Usage](#usage)
      - [Searching with Steam IDs](#searching-with-steam-ids)
      - [Bot Commands](#bot-commands)
 ---

## Installation

1. The script can be used by first cloning the repo 

`git clone "https://github.com/screaminglineage/SteamIDFinder.git"`

and then copying over the python script into any folder you wish.

2. A Telegram bot needs to be generated along with an API key using BotFather (https://t.me/botfather). Enter the command `/newbot` in the BotFather bot and then follow the instructions.
3. The API key should be placed in a file called `user_token.txt` which must be placed in the same directory as the script.
4. Run the Script and Enjoy!



## Introduction

After running the script and ensuring that `Script Running...` appears, the bot might take about **5**-**10** seconds to initialize. You can test if the bot is working by entering the commands `/help` or `/start`.
After that a Steam or Dota 2 ID can be sent to the bot and it will return back the user profile belonging to that ID

## Usage

### Searching with Steam IDs

Sending a long Steam ID, such as "76561198312899054", or short Dota 2, like "352633326", will cause the bot to return back the Steam Profile associated with that ID.


### Bot Commands
  - `/start` - gives a short description of the bot
  - `/help` - gives the same above description with 1 more line for an example
  - `/random` - gives a random steam profile link (most of these will either be inactive/disable/special accounts) this option is honestly there just for fun

There is atleast another hidden option but even if you discover it, its best not to actually run it

