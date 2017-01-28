# piazza-slackbot
A super simple bot to send Slack notifications when new posts are added to a Piazza page.

# Instructions

## Requirements
The bot is written in Python 3 and requires the following packages:
```
slacker
piazza-api
time
```

## Set-up
To set this up you need to have access to a page on Piazza and have a Slack account with the necessary permissions.

Then follow this [link](https://my.slack.com/services/new/bot) to create a bot. Once you have created a bot make sure to save the API token, which you will use to authorize your bot.

As you probably don't want your bot notifying the entire #general channel each time it posts it is useful to set up a new channel for the bot. Once you have created the channel you can then add the bot by clicking `Channel Settings` > `Invite team members to join...` > and then select your bot from the list.

You will need to add your credentials for both Piazza and Slack into the relevant places in the file `slackbot.py`. All the areas where you need to input information are marked with `TODO`. Simply add the relevant information to the strings.

## Usage
I suggest using `screen` to run the bot on a machine where it can run constantly without any interruptions. Simply open a new screen window, run the bot, and then detach from the window.

The bot is set up to constantly print out statements in the window to show that it is running, although you can comment this out if you wish.
