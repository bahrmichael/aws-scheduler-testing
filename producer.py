import json
import os
import sys
from datetime import datetime, timedelta
from random import randrange

import boto3

client = boto3.client('sns')


def handle(event, context):
    input_topic = os.environ.get('INPUT_TOPIC_ARN')
    target = os.environ.get('OUTPUT_TOPIC_ARN')
    run(100, input_topic, target)


def run(target, input_topic, amount):
    start = datetime.utcnow()
    for i in range(0, amount):
        delay = randrange(60 * 5)
        scheduled_time = (datetime.utcnow() + timedelta(seconds=delay)).isoformat()
        payload = {
            'payload': scheduled_time,
            'date': scheduled_time,
            'target': target,
            'user': 'test-user'
        }

        client.publish(
            TopicArn=input_topic,
            Message=json.dumps(payload)
        )

        if (i + 1) % 10 == 0:
            total_millis = (datetime.utcnow() - start).total_seconds() * 1000
            print(f'total: {i+1}, {int(total_millis / (i+1))}ms per event')


if __name__ == '__main__':
    arguments = sys.argv[1:]
    if len(arguments) >= 1:
        target = arguments[0]
    else:
        print('You must specify the output topic as the first parameter')
        exit()

    if len(arguments) >= 3:
        input_topic = arguments[2]
    else:
        input_topic = 'arn:aws:sns:us-east-1:256608350746:scheduler-input-prod'

    if len(arguments) >= 2:
        amount = int(arguments[1])
    else:
        amount = 100

    run(target, input_topic, amount)
