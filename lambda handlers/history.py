import json
import boto3
s3 = boto3.client('s3')


def lambda_handler(event, context):
    page = event['page']
    
    page = int(page)
    ind = (page - 1) * 30
    pages = []
    for p in range(ind, ind+30):
        pages.append(str(p))
    pages = tuple(pages)
    
    query = "select ind, blockNumber, hash, transactionIndex, 'from', 'to', isMainChain FROM S3Object where index in " + str(pages)  + " limit 30"
    

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