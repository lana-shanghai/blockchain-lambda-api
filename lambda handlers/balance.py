import json
import urllib3

def lambda_handler(event, context):
    address = str(event['address']).lower()
    #address = '0xb2930B35844a230f00E51431aCAe96Fe543a0347'
    pool = urllib3.PoolManager()
    params = '{"jsonrpc":"2.0","method":"eth_getBalance","params":["' + address + '", "latest"],"id":1}'
    
    r = pool.urlopen(
        method='POST', 
        url='https://cloudflare-eth.com', 
        headers={'Content-Type':'application/json'}, 
        body=params
    ).data
    
    return {
        'balance': int(json.loads(r)["result"], 16)/10**18
    }