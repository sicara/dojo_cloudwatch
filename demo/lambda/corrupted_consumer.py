import os
import time
import uuid
from datetime import date
from decimal import Decimal

import boto3

REGION_NAME = "eu-west-1"
DDB_NAME = os.getenv('DDB_NAME')


def write_to_dynamodb(table_name: str, item: dict):
    dynamodb = boto3.resource("dynamodb", region_name=REGION_NAME)
    table = dynamodb.Table(table_name)
    table.put_item(Item=item)


def handler(event, context):
    sqs_message = event["Records"][0]["body"]
    print(f"Message: {sqs_message}")
    ddb_item = {
        "_id": str(uuid.uuid4()),
        "_created": Decimal(time.time()),
        "message": sqs_message
    }

    # PROCESS 1 - INFRA ERROR
    time.sleep(2 * int(sqs_message))

    # PROCESS 2 - APPLI ERROR
    if sqs_message == "3":
        ddb_item["date"] = date.today()

    write_to_dynamodb(table_name=DDB_NAME, item=ddb_item)
