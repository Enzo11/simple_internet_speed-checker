import pyspeedtest
import time

st = pyspeedtest.SpeedTest("www.google.com")
st1 = pyspeedtest.SpeedTest("www.yahoo.com")



ping =st.ping()
#download =st1.download()
#upload =st2.upload()
print("Ping Result =",ping)

#time.sleep(2)
download =st1.download()
#print("Checking your download speed.")
#time.sleep(1)
#print("Checking your download speed..")
#time.sleep(1)
#print("Checking your download speed...")
#time.sleep(1)
print("Your Download speed is =",download)
#print(download)
