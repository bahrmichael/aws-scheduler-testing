import time
from datetime import datetime
from uuid import uuid4

from pynamodb.exceptions import PutError

from model import MeasuredDuration


def handle(event, context):
    delays = []
    for record in event['Records']:
        print(record)
        payload = record['Sns']['Message']
        execution_time = datetime.fromisoformat(payload)
        delta = int((datetime.utcnow() - execution_time).total_seconds() * 1000)
        print(f'delay: {delta}')
        delays.append(delta)

    with MeasuredDuration.batch_write() as batch:
        retries = []
        for delay in delays:
            item = MeasuredDuration()
            item.id = str(uuid4())
            item.delay = delay
            try:
                batch.save(item)
            except PutError as e:
                print(e)
                time.sleep(.200)
                retries.append(delay)

        while len(retries) > 0:
            delay = retries.pop(0)
            item = MeasuredDuration()
            item.id = str(uuid4())
            item.delay = delay
            try:
                batch.save(item)
            except PutError as e:
                print(e)
                time.sleep(.200)
                retries.append(delay)

    print('Processed %d records' % len(event['Records']))
