# piazza-slackbot
A simple bot that sends Slack notifications when new posts are added to a Piazza page.

## Why?
To get notifications without having to check the Piazza website or have email notifications clog up your inbox.

# Instructions

## Requirements
The bot is written in Python 3 and requires the following packages:
```
slacker
piazza-api
```

## Testing Setup

Create a Python 3 virtual environment, then activate it:
```bash
> virtualenv -p python3 .venv
> source .venv/bin/activate
```

Then install requirements with:
```bash
> pip3 install -r requirements.txt
```

## Slack Setup
To set this up you need to have access to a page on Piazza and have a Slack account with the necessary permissions.

Then follow this [link](https://my.slack.com/services/new/bot) to create a bot. Once you have created a bot make sure to save the API token as you will need it to authenticate your bot.

Consider setting up a new channel for the bot so that it doesn't overrun the #general discussion. Once you have created the channel you can then add the bot by clicking `Channel Settings` > `Invite team members to join...` > and selecting your bot from the list of users.

You will need to add your credentials for both Piazza and Slack into the relevant places in the file `slackbot.py`. All the areas where you need to input information are marked with `TODO`. Simply add the relevant information to the empty strings.

An optional parameter `include_link` can be passed to the main function to include or exclude a URL to the post when the message is sent. This is set to true by default but can be changed if you do not want to include links.

## Lambda Setup
The bot has been reconfigured for 2019 to run on [AWS Lambda](https://aws.amazon.com/lambda/). Usage falls well within the AWS free tier. It can be setup as follows:

1. Navigate to the Lambda page within the AWS console, and click *Create function*
2. Create a function with a Python 3.x runtime and a new execution role. Provide this role with the *AWSLambdaBasicExecutionRole* policy (this just gives the function permission to write to CloudWatch logs).
3. Navigate to the CloudWatch page within the AWS console, and click on _Events_ > _Rules_.
4. Create a new rule, using a schedule. Add your Lambda function as the target. Make sure to set this interval to be the same as you have configured within the function code (current value is 10 minutes).
5. Configure the AWS CLI on your local machine if you have not already. Install the CLI ([Mac instructions](https://docs.aws.amazon.com/cli/latest/userguide/install-macos.html)) the run `aws configure`. You can generate an access key ID and secret access key in the AWS console from _Your Name_ > _My Security Credentials_ > _Access keys_.
6. Follow the instructions describe [here](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html) to create an AWS Lambda Deployment Package with Additional Dependencies, and deploy from your local system.
7. Return to the AWS console, and change the _handler_ field of your Lambda function to be `slackbot.update_handler`

The bot will then send a notification to the relevant Slack channel whenever a new post is added to Piazza, including a hyperlink to the relevant post.

*Note: The bot will also post links to private messages sent to the user whose Piazza credentials are being used. All users in the channel will be able to see the link but it will only work for the authorized user.*

# Contributions

Please feel free to fork this project and make a pull request if you have an contributions you would like to make.
