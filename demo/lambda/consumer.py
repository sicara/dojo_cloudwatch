import time


def handler(event, context):
    sqs_message = event["Records"][0]["body"]
    if int(sqs_message) % 2 == 0:
        time.sleep(15)
    print(sqs_message)
