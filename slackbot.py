"""
This is a simple Slackbot that will
check a Piazza page for new posts every 1 minute.
Every time a new post is observed a notification will
be sent out
"""

import json
from datetime import datetime
from piazza_api import Piazza
from slacker import Slacker
from time import sleep

#Accessing Piazza and loading data
piazza_id = "" #TODO this is the suffix of the piazza url
piazza_email = "" #TODO your email
piazza_password = "" #TODO your piazza piazza_password
p = Piazza()
p.user_login(email=piazza_email, password=piazza_password)
network = p.network(piazza_id)

#Accessing Slack and configuring the bot
slack_token = "" #TODO Your slack API token goes here
bot=Slacker(slack_token) #authorizing bot
channel="" #TODO Name of the channel to post to
bot_name = "" #TODO Name of your slackbot
update_interval=10 # update frequency in minutes

#URL for posts on the page
POST_BASE_URL = "https://piazza.com/class/"+piazza_id+"?cid="

def get_latest_posts(feed,latest_duration=update_interval):
    latest_posts = []
    current_time = datetime.utcnow()

    for post in feed:
        post_updated = datetime.strptime(post["updated"], "%Y-%m-%dT%H:%M:%SZ")
        post_age = (current_time - post_updated).total_seconds()
        post_age_in_minutes = post_age / 60
        if "pin" not in post and post_age_in_minutes < latest_duration:
            latest_posts.append((post["nr"],post["subject"]))

    return latest_posts

def check_for_new_posts(network=network,include_link=True):
    latest_posts = get_latest_posts(network.get_feed()['feed'])
    for post_id,post_title in latest_posts:
        attachment = None
        message = None
        if include_link is True:
            attachment = [
                {
                    "fallback": post_title,
                    "title": post_title,
                    "title_link": POST_BASE_URL+str(post_id),
                    "text": "This post is either new or has been updated. Follow the link to view this post on Piazza",
                    "color": "good"
                }
            ]
        else:
            message="New post on Piazza!"
        bot.chat.post_message(channel,message, \
        as_user=bot_name,parse='full',attachments=attachment)

def update_handler(event,context):
    check_for_new_posts()
