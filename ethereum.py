from geth import LiveGethProcess # mainnet
from geth import LoggingMixin, DevGethProcess #private local chain for testing
from web3 import Web3, EthereumTesterProvider
from eth_tester import EthereumTester

w3 = Web3(EthereumTesterProvider())
w3.isConnected()

#geth = LiveGethProcess()
geth = DevGethProcess('data1', '/Users/skywalker721/Desktop/go-ethereum/data1') # 해당 파일 경로를 넣어줍니다.
geth.start()

firstbytecode = input("First input : ")
secondbytecode = input("Second input : ")