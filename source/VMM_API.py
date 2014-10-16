__author__='ESEL'
import requests
from time import sleep
import json

class VMM_API:


	def __init__(self,vmID):
		self.hostURL = 'http://54.199.149.113/vmmAPI'
    		self.vm_address = -1
		self.centralize_address = -1
		self.vm_id = vmID
		self.vm_password = -1


	def initialize(self):
		payload = {'vm_id': self.vm_id}
        	api_url = self.hostURL+'/initialize'
        	
		result = False

		try:
	            r = requests.get(api_url, params=payload, verify=True)
	            res = r.text
		    print res
	            
		    decoded = json.loads(res)
		    print(decoded)		

		    result = decoded['success']
		    
		    if(result):
		    	self.vm_address = decoded['vm_address']
		    	self.centralize_address = decoded['centralize_address']
			self.vm_password = decoded['vm_password']
		    
		except:
		    print('bb')
	            result = False
	        
		return result



	def report(self,status,specificData):

		api_url = self.hostURL+'/vmreport'
        	
		payload = {'status': status,'id' : self.vm_id, 'data' : specificData}
        	
		try:
	            r = requests.get(api_url, params=payload, verify=True)
	            res = r.text
		    print res
	            
		    decoded = json.loads(res)

		    print(ee)

		    result = eval(res,{},{})['success']
			
	        except:
	            pass





