import json
import urllib3

def lambda_handler(event, context):
    txHash = event['txHash']
    pool = urllib3.PoolManager()
    params = '{"jsonrpc":"2.0","method":"eth_getTransactionByHash","params":["' + txHash + '"],"id":1}'
    r = pool.urlopen(
        method='POST', 
        url='https://cloudflare-eth.com', 
        headers={'Content-Type':'application/json'}, 
        body=params
    ).data
    
    return {
        'transactionHash': json.loads(r)["result"]["hash"],
        'blockNumber': int(json.loads(r)["result"]["blockNumber"], 16),
        'blockHash': json.loads(r)["result"]["blockHash"],
        'from': json.loads(r)["result"]["from"],
        'to': json.loads(r)["result"]["to"],
        'valueHEX': json.loads(r)["result"]["value"],
        'valueETH': int(json.loads(r)["result"]["value"], 16)/10**18
    }
    