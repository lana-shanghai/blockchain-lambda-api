# Blockchain data API

An API to query blockchain data, including blocks, transactions, and balances.

## Description

The lambdas folder contains the lambda functions hit by the API calls. 

## Endpoints

### transaction

Returns the details of a transaction for a given transaction hash.

#### Parameters

```
txHash
```

#### Example

```
https://7uolfkr4xd.execute-api.us-east-1.amazonaws.com/prod/transaction?txHash=0x88df016429689c079f3b2f6ad39fa052532c56795b733da78a91ebe6a713944b
```

### ethbalance

Returns the balance in ETH for a given address.

#### Parameters

```
address
```

#### Example

```
https://7uolfkr4xd.execute-api.us-east-1.amazonaws.com/prod/ethbalance?address=0x52bc44d5378309EE2abF1539BF71dE1b7d7bE3b5
```

### block

#### Parameters

```
blockhash
```

#### Example

```
https://7uolfkr4xd.execute-api.us-east-1.amazonaws.com/prod/block?blockHash=0x0001f8a5cbade6892fde733c478f3cbf943b884eb5ad6ceef73cd6ec070d5c7f
```

### history

Returns 30 transactions per page.

#### Parameters

```
page
```

#### Example

```
https://7uolfkr4xd.execute-api.us-east-1.amazonaws.com/prod/history?page=3
```

### transactions

Returns the transactions that happened between two block numbers.

#### Parameters

```
start, end
```

#### Example

```
https://7uolfkr4xd.execute-api.us-east-1.amazonaws.com/prod/transactions?start=6613639&end=6613739
```

