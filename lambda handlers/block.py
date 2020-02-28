import json
import boto3
s3 = boto3.client('s3')


def lambda_handler(event, context):
    blockHash = str(event['blockHash'])
    query = "select * FROM S3Object where hash = '" + blockHash  +"' limit 1"

    response = s3.select_object_content(
        Bucket='blockchain-api-challenge',
        Key='blockchain_data/eth-ropsten-blocks.csv',
        Expression=query,
        ExpressionType='SQL',
        InputSerialization={
            'CompressionType': 'NONE',
            'CSV': {
                'FileHeaderInfo': 'USE'
            }
        },
        OutputSerialization={            
            'JSON': {
                'RecordDelimiter': '\n'
            }
        }
    )
   
    records = ''
    for events in response['Payload']:
        if 'Records' in events:
            records = events['Records']['Payload'].decode('utf-8')
            print(records)
            
        elif 'Stats' in events:
            statsDetails = events['Stats']['Details']
            print("Bytes scanned: ")
            print(statsDetails['BytesScanned'])
            print("Bytes processed: ")
            print(statsDetails['BytesProcessed'])    
    
    if records == '':
        return {
            'statusCode': 200,
            'body': 'page does not exist'
        }
        
    return {
        'statusCode': 200,
        'body': json.loads(records)
    }
    