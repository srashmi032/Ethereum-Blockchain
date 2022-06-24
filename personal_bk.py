from web3 import Web3

ganache_url="HTTP://127.0.0.1:7545"

web3=Web3(Web3.HTTPProvider(ganache_url))

#print(web3.isConnected())

#print(web3.eth.blockNumber)

account_1="0x43fe53C00c4135bA875896Cb7b66A14DA9F608dE"
account_2="0xeCdAFa377991CA40b219b1Cbf6C287D7FE212fba"

private_key="ae31996d9514922f0f7775b137718a6dc65833c1d083a12058938897c0493fd3"


#build a transaction

#get nonce, nonce prevents transaction from being performed twice

nonce=web3.eth.getTransactionCount(account_1)

tranx={
	'nonce':nonce,
	'to':account_2,
	'value':web3.toWei(1,'ether'),
	'gas':2000000,# gas limit, its basically is some amount of 
	#cryptocurrency whenever u are sending transaction, its just unit like gallons of gas in 
	#car, multiply by gasprice
	#gwei is larger denomination of way smaller than ethereum
	'gasPrice':web3.toWei('50','gwei')
}

# sign the transaction
signed_tx=web3.eth.account.signTransaction(tranx,private_key)

#send transaction
tx_hash=web3.eth.sendRawTransaction(signed_tx.rawTransaction)
# get tranx hash
print (web3.toHex(tx_hash))


