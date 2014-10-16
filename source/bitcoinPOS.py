import bitAPI
import gui
from time import sleep
import VMM_API
import threading
import logAPI

class bitcoinPOS:

	def __init__(self):
		self.amt = 0
		self.logfile = '/home/pi/btcpos.cvs'
		self.logger = logAPI.logAPI(self.logfile)
		self.stage = 'Main Called'
		self.gui = gui.gui()
		self.vmBitcoinAddress = -1
		self.vmBitcoinPassword = -1
		self.centralizeAddress = -1
		self.status = 200
		

	def newTransaction(self):
		
		print('Loading...')
		
		self.logger.writeSystemLog(self.stage)

		self.loadSettings()
		
		self.VMM_API = VMM_API.VMM_API(self.vmID)
		
		if(self.vmBitcoinAddress == -1):
			self.VMM_API.initialize()	
			self.logger.writeSystemLog('Initialize')
			
			self.vmBitcoinAddress = self.VMM_API.vm_address
			self.vmBitcoinPassword = self.VMM_API.vm_password
			self.centralizeAddress = self.VMM_API.centralize_address
		
		self.api = bitAPI.bitcoinAPI(self.vmBitcoinAddress,self.vmBitcoinPassword,self.logfile)
		
		self.report()
		
		self.gui.waitScreen()
	
		self.logger.writeSystemLog('Ready')

		print('insert value(USD) please')
		input = raw_input()
		
		
		self.logger.writeSystemLog('Start transaction')		

		self.stage = 'toBTC'
		
		amt = input
		print('amount :' + str(amt) + '$')

		bitAmt = self.api.toBTC(amt,'USD')
		print('To BTC : '+ str(bitAmt))

		print('=== make QRcode ===')

		bitcoinAddress = self.api.getNewBitcoinAddress()
		qr_image = self.api.getQRCode(bitcoinAddress,bitAmt)
		qr_image.save('qr.gif')
		
		self.gui.clearGUI()
		self.gui.paymentScreen(qr_image,bitcoinAddress,bitAmt,amt)
		
		print('===check payment - polling===')


		self.stage = 'TRANSACTION'
		self.logger.writeSystemLog('Wait for payment')

		paymentConfirm = self.api.waitForPayment(bitcoinAddress,bitAmt)

		if paymentConfirm:
			self.gui.clearGUI()
			self.gui.endScreen(bitAmt)
			print('===payment done===')
			self.api.sendPaymentToAddress(self.vmBitcoinAddress,self.centralizeAddress,self.vmBitcoinPassword,bitAmt)
		
		else:
			print('===payment cancel===')
			self.logger.writeSystemLog('payment canceled')


		self.stage = 'END'
		self.logger.writeSystemLog('transaction ended')
		
		sleep(3)
		self.gui.clearGUI()
		
	
	def transactionLoop(self):
		while True:
		   self.newTransaction()

	def loadSettings(self):
		try:
			file = open('setting.txt','r')
			
			self.vmID = file.readlines()
		except Exception, err:
			self.vmID = -1
	
	def report(self):
		t = threading.Thread(target=self.reportingLoop)
		t.start()

	def reportingLoop(self):
		while True:
			self.VMM_API.report(self.status,'data')
			sleep(600)

