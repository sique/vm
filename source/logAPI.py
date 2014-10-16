
import datetime

class logAPI:

	def __init__(self,logfile):
		self.logfile = logfile


	 #make log in file
    	def writeAPILog(self,code,url,dataset,result):
		if self.logfile:
	   		try:
		    	 log = open(self.logfile,'a')
		    	 log.write(" / ".join((datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),code,url,dataset,result)) + "\n")
                    	 log.close()
                	except Exception, err:
                    	 print err
  

    	def writeSystemLog(self,stage):
	 	if self.logfile:
	 	    try:
			log = open(self.logfile,'a')
			log.write(" , ".join((datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),stage)) + "\n")
                	log.close()
             	    except Exception, err:
                	print err

   