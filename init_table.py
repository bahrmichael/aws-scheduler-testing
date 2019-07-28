import boto3

client = boto3.client('dynamodb')


def create():
    name = 'aws-scheduler-testing'
    response = client.list_tables()
    if name in response['TableNames']:
        print('Table %s already exists. Please delete it first.' % name)
        return
    client.create_table(
        TableName=name,
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            }
        ],
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            }
        ],
        BillingMode='PAY_PER_REQUEST',
    )
    print('%s created' % name)


if __name__ == '__main__':
    create()
