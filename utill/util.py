import csv,os
from faker import Faker
import time
BASEPATH=os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CASEPATH=os.path.join(BASEPATH,'case')
IMGPATH=os.path.join(BASEPATH,'img')
REPORTPATH=os.path.join(BASEPATH,'report')
PAGEPATH=os.path.join(BASEPATH,'page')
DATAPATH=os.path.join(BASEPATH,'data')

def url():
    ur='http://127.0.0.1:8000/api/'
    return ur
def url_add():
    add='add_guest/'
    return add
def url_sec():
    sec='sec_get_event_list/'
    return sec
def url_event():
    event='add_event/'
    return event
class get_txt():
    fake = Faker(locale='zh_CN')
    def get_num(self, m, n):
        return self.fake.random_int(m, n)
    def get_name(self):
        return self.fake.name()
    def get_address(self):
        return self.fake.province() + '.' + self.fake.city()
    def get_datetime(self):
        return self.fake.future_datetime()
    def get_email(self):
        return  self.fake.email()
    def get_phone(self,m):
        return  m+self.fake.phone_number()[2:]


def get_time():
    return time.strftime('%y_%m_%d %H-%M-%S', time.localtime())