# AWS Lambda - Parsing Cloudwatch Data and sending the response via email.

Author: Evan Erickson
Language: Python3
Backend: AWS / Serverless / AWS Lambda

# Objective:
Lambda function: Parsing cloud front log streams and sending data to an email


# How to use it:
You will be taking your cloudwatch logs, and adding a lambda trigger so that everytime there are new logs, you can publish an email or do something with that info.

In this example, our Lambda will be sending emails with SNS. However, you could do whatever you want with the log data, maybe run some logic to inact a certain function, for example: change user priviledges based upon log data.

Useful tips, you cannot parse the event object with dot notation. You need to use ['varName'].
