# Author: Evan Erickson
# Language: Python3
# Backend: AWS / Serverless / AWS Lambda


# Objective:
# Lambda function: Parsing cloud front log streams and sending data to an email


# How to use: 
# Make sure you have cloudwatch enabled and it is creating logs for a given event (such as an ec2 or Lambda function).
# Once you have those logs, you can create a lambda function in the lambda console and select a cloudwatch log trigger. 
# The cloudwatch logs will be sent in a event object.


# Useful tips, you cannot parse the event object with dot notation. You need to use ['varName'].

import json
import boto3
import gzip
import base64
import os

sns_client = boto3.client('sns')

def lambda_handler(event, context):
  
    # Convert the event into useable format and then log the output.
    decoded_event = json.loads(gzip.decompress(base64.b64decode(event['awslogs']['data'])))
    print(decoded_event)
    
    # If you want to play around with the event to see what the data structure like, uncomment the lines below:
        # print(decoded_event['logGroup'])
        # print(decoded_event['logStream'])
        # print(decoded_event['logEvents'][0]['message'])

    
    # Parse the response even more and make it more readable. This is where you might want to edit what you see...
    # I just displayed the logGroup, logStream, annd logEvents[1]message but you can play around with it.
    # Make sure you pay attention to the fact that they are using [] to parse instead of a ".".
    body = '''
    LogGroup: {loggroup}
    Logstream: {logstream}
    Filter Match: {filtermatch}
    '''.format(
        loggroup = decoded_event['logGroup'],
        logstream = decoded_event['logStream'],
        filtermatch = decoded_event['logEvents'][1]['message'],
    )
    print(body)
    
    
    # Next, input your SNS topic ARN below. To create an SNS topic, go to the SNS and then create topic. 
    # I suggest giving it a name tying it to the lambda and the cloudwatch logs.
    # Next, click on the SNS topic. You should see a bunch of info, including an ARN. Copy that and paste it below for use later.
    # Click add a subscription (aka a receiver of the log data). Input the type you want, in this case email.
    # Then, confirm in your email inbox that you want to opt into the topic.
    # Lastly, paste the ARN in line 53. 
   
    # This is a simple SNS python publish function. I call it on line 57. It accepts one param which is the body that we are printing (console.logging) on line 40. 
    # If you want to change the body, do so above. 
    
    def send_message(body):
        sns = sns_client.publish(
            TopicArn = os.environ.get('SNS_TOPIC_ARN'),
            Message = body,
        )
        
    send_message(body);
        
    
