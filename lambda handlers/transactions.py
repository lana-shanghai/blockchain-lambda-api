import json
import boto3
s3 = boto3.client('s3')


def lambda_handler(event, context):
    start = event['start']
    end = event['end']
    
    start = int(start)
    end = int(end)
    blocks = []
    for b in range(start, end+1):
        blocks.append(str(b))
    blocks = tuple(blocks)
    
    query = "select blockNumber, hash, transactionIndex, 'from', 'to', isMainChain FROM S3Object where blockNumber in " + str(blocks)  + " limit 30"
    print(query)

    response = s3.select_object_content(
        Bucket='blockchain-api-challenge',
        Key='blockchain_data/tx.csv',
        Expression=query,
        ExpressionType='SQL',
        InputSerialization={
            'CompressionType': 'NONE',
            'CSV': {
                'FileHeaderInfo': 'USE',
                'FieldDelimiter': ',',
                'RecordDelimiter': '\n'
            }
        },
        OutputSerialization={            
            'JSON': {
                'RecordDelimiter': '\n'
            }
        }
    )
   
    print(response)
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
        'body': records
    }