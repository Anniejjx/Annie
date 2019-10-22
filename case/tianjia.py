import requests
import unittest
from test_fabu.page.page_base import get_data
from test_fabu.utill.util import get_txt
g = get_data()
class fabu(unittest.TestCase):

    def setUp(self):
        pass
    def test1(self):
        url='http://127.0.0.1:8000/api/add_event/'
        f=get_txt()
        data={}
        data['eid']=f.get_num(1,100)
        data['name']=f.get_name()
        data['status']=f.get_num(0,1)
        data['limit']=f.get_num(20,200)
        data['address']=f.get_address()
        data['start_time']=f.get_datetime()
        r=requests.post(url,data)
        res=r.json()
        print(res)


        g.con_mysql()
        sql='select * from sign_event where id="%d" and name="%s";'
        select_result=g.execute_sql(sql %(data['eid'],data['name']))

        if res['message']=='add event success' and res['status']==10000 and select_result==1:
            print('pass')
        else:
            print('Fail')
    def test_case2(self):
        '''name为空时，发布会发布失败'''
        self.url='http://127.0.0.1:8000/api/add_event/'
        f = get_txt()
        self.data={}
        self.data['eid']=f.get_num(0,100)
        self.data['name']=''
        self.data['status']=f.get_num(0,1)
        self.data['limit']=f.get_num(20,200)
        self.data['address']=f.get_address()
        self.data['start_time']=f.get_datetime()
        r=requests.post(self.url,self.data)
        self.res=r.json()
        print(self.res)
        g.con_mysql()
        sql='select * from sign_event where id="%d" and name="%s";'
        select_result=g.execute_sql(sql %(self.data['eid'],self.data['name']))
        print(select_result)
        if self.res['message']=='parameter error' and self.res['status']==10021 and select_result==0:
            print('pass')
        else:
            print('Fail')

    def tearDown(self):
        global g
        g.close()
if __name__=='__main__':
    unittest.main()
