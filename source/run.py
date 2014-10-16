import bitcoinPOS
import threading


pos = bitcoinPOS.bitcoinPOS()


t = threading.Thread(target=pos.transactionLoop)

t.start()

pos.gui.root.mainloop()