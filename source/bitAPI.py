import requests
import qrencode
import datetime
from time import sleep
import logAPI

class bitcoinAPI:

    def __init__(self,username,password,logfile):
        
        self.username=username
        self.password=password
	self.logfile = logfile
	self.logfile = '/home/pi/btcpos.cvs'
	self.logger = logAPI.logAPI(self.logfile)


    #returns new address or ""
    def getNewBitcoinAddress(self,label=None):
        payload = {'password': self.password, 'label': label}
	
        gen_address_url = 'https://blockchain.info/merchant/' + self.username + '/new_address'
	
        address = ""
        try:
            r = requests.get(gen_address_url, params=payload, verify=True)
            address = eval(r.text,{},{})['address']
            self.logger.writeAPILog('getNewAddress',gen_address_url,str(payload),r.text)

	except:
            pass
        return address

    #returns wallet balance or -1
    def getWalletBalance(self):
        payload = {'password': self.password}
        get_balance_url = 'https://blockchain.info/merchant/' + self.username + '/balance'
        balance = -1
        try:
            r = requests.get(get_balance_url, params=payload, verify=True)
            print r.text
            balance = eval(r.text,{},{})['balance']
	    self.logger.writeAPILog('getWalletBalance',gen_address_url,str(payload),r.text)

        except:
            pass
        return balance

    #returns address balance or -1
    def getAddressBalance(self,address,confirmations='0'):
        
	get_balance_url = 'https://blockchain.info/q/addressbalance/' + address
        balance = -1
	
        try:
            r = requests.get(get_balance_url, verify=True)
            balance = eval(r.text,{},{})
	    self.logger.writeAPILog('getBalance',get_balance_url,address,r.text)

        except:
            pass
        return balance



    #returns current bitcoin value or -1
    def toBTC(self,value,currency):
        payload = {'currency': currency, 'value': value}
        to_btc_url = 'https://blockchain.info/tobtc'
        btotal=-1
        try:
            r = requests.get(to_btc_url, params=payload,verify=True)
            if r.status_code == 200:
                btotal=float(r.text)
            self.logger.writeAPILog('toBTC',to_btc_url,str(payload),r.text)

        except:
            pass
        return btotal

    #returns last USD/BTC rate or -1
    def getBTCRate(self):
        ticker_url = 'https://blockchain.info/ticker'
        rate = -1
        try:
            r = requests.get(ticker_url)
            rate = eval(r.text,{},{})['USD']['last']
        except:
            pass
        return rate
    

    def waitForPayment(self,address,bitamount,confirmations=0):
 	confirmed = False
	count = 0
	while not count >= 30 and not confirmed:
		if self.getAddressBalance(address,confirmations) >= bitamount:
			confirmed = True
		else:
			count = count+1
		sleep(1)
	return confirmed


        #returns True or False if payment goes through or not
    def sendPaymentToAddress(self,from_address,to_address,password,bitamount,fee=0.0005):
        bitamount=str(int((float(bitamount)-fee) * 100000000)) #take out miner fee and convert to satoshi
        payload = {'password': password,'to' : to_address, 'from' :from_address,'amount':bitamount}
        send_payment_url = 'https://blockchain.info/merchant/' + self.username + '/payment'
        payment_message = False
	
	self.logger.writeAPILog('sendPayment',send_payment_url,str(payload),'R')

        try:
            r = requests.get(send_payment_url, params=payload, verify=True)
            print r.text
            payment_message = eval(r.text,{},{})['message']
	    self.logger.writeAPILog('sendPayment',send_payment_url,str(payload),r.text)

        except:
            pass
        return payment_message



    #returns payment-URI-encoded QR Code image(100x100px)
    def getQRCode(self,address, amount, label=None, message=None):
        amount = 'amount=' + str(amount) #+ 'X8'
        label = '' if not label else '&label='+label
        message = '' if not message else '&message='+message
        qr_str = 'bitcoin:'+address+'?'+amount + label + message
        im = qrencode.encode(qr_str,3)
        return im[2].resize((128,128))



