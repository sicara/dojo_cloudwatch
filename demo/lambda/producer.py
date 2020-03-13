import os
from typing import List

import boto3

SQS_QUEUE_NAME = os.getenv('SQS_QUEUE_NAME')


def send_messages_to_queue(messages: List[str], sqs_queue_name: str):
    sqs = boto3.resource("sqs")
    queue = sqs.get_queue_by_name(QueueName=sqs_queue_name)
    for message in messages:
        queue.send_message(MessageBody=message)


def handler(event, context):
    messages = [str(i) for i in range(10)]

    send_messages_to_queue(
        messages=messages,
        sqs_queue_name=SQS_QUEUE_NAME,
    )
