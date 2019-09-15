import time 
from pytz import timezone 
import datetime
from datetime import datetime
import pytz
 

def from_date (epoch):
    now_epoch = epoch
    my_datetime = datetime.fromtimestamp(now_epoch, tz= pytz.timezone('Asia/Jakarta'))
    a = my_datetime.strftime('%Y%m%d%H%M')
    # print(a)
    return a
def timestamp ():
    now_epoch = datetime.now().timestamp() 
    my_datetime = datetime.fromtimestamp(now_epoch, tz= pytz.timezone('Asia/Jakarta'))
    a = my_datetime.strftime('%Y%m%d%H%M')
    # print(a)
    return a
 

def DeliSecond():
    ts = datetime.now().timestamp() 
    tt = datetime.utcnow().timestamp()
    return ts
    
 

if __name__ == "__main__":
    # today_in_numb(1562425642)   
    
    pass