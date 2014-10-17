__author__ = 'ESEL'

import tkFont
from Tkinter import *

class gui:

	def __init__(self):
	    self.qr_panel,self.address_panel,self.bitamount_panel,self.amount_panel,self.wait_panel,self.end_img_panel,self.end_panel=None,None,None,None,None,None,None
	    self.createGUI()



	def createGUI(self):
	    self.root = Tk()
	    W = self.root.winfo_screenwidth()
            H = self.root.winfo_screenheight()
   	    geom = str(W)+'x'+str(H)+'+0+0'
	 
	    self.root.geometry(geom)
	    self.root.configure(background='black')
	    self.root.overrideredirect(True)
        

	def waitScreen(self):
	    self.root.configure(background ='white')
	    photo = PhotoImage(file='bitcoin_accepted.gif')
	    self.wait_panel = Label(self.root,image = photo,borderwidth=0,pady=100)
	    self.wait_panel.image=photo
	    self.wait_panel.pack()


	def paymentScreen(self,img,address,bitamount,amount):
	    self.root.configure(background='white')
	    photo = PhotoImage(file='qr.gif')
            self.qr_panel = Label(self.root,image = photo)
	    self.qr_panel.image = photo
	    
    	    f=tkFont.Font(family='Helvetica',size=10,weight=tkFont.BOLD)
	    self.address_panel = Label(self.root , text = address,font=f)
	    self.address_panel.configure(background='white')

    	    f=tkFont.Font(family='Helvetica',size=16,weight=tkFont.BOLD)
	    self.bitamount_panel = Label(self.root , text = str(bitamount) + ' BTC',font=f)
	    self.bitamount_panel.configure(background='white')
	
	    f=tkFont.Font(family='Helvetica',size=16,weight=tkFont.BOLD)
	    self.amount_panel = Label(self.root , text = 'price : '+str(amount) + ' USD',font=f)
	    self.amount_panel.configure(background='white')
			

	    self.qr_panel.grid(column=0,row=0,columnspan=4,rowspan=3,padx=40,pady=10)
	    self.address_panel.grid(column=0,row=5,padx=6,pady=3)
	    self.amount_panel.grid(column=0,row=4,padx=12,pady=3)
	    self.bitamount_panel.grid(column=0,row=3,padx=12,pady=3)
	
	def endScreen(self,bitamount):
	    self.root.configure(background='white')
	    photo = PhotoImage(file='thanks.gif')
            self.end_img_panel = Label(self.root,image = photo,borderwidth=0,pady=100)
	    self.end_img_panel.image = photo

	    f=tkFont.Font(family='Helvetica',size=10,weight=tkFont.BOLD)
	    self.end_panel = Label(self.root , text = str(bitamount) + 'BTC payment confirmed',font=f)
	    self.end_panel.configure(background='white')		
	    
	    self.end_img_panel.grid(column=0,row=0,columnspan=4,rowspan=3,padx=30,pady=20)
	    self.end_panel.grid(column=0,row=3,padx=10,pady=10)


	def clearGUI(self):
	    if self.qr_panel:
		self.qr_panel.grid_forget()
	    if self.address_panel:
		self.address_panel.grid_forget()
	    if self.bitamount_panel:
		self.bitamount_panel.grid_forget()
	    if self.amount_panel:
		self.amount_panel.grid_forget()
	    if self.wait_panel:
		self.wait_panel.pack_forget()
	    if self.end_panel:
		self.end_panel.grid_forget()
	    if self.end_img_panel:
		self.end_img_panel.grid_forget()
		
	    









