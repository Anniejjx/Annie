import requests
import unittest
from test_fabu.page.page_base import get_data
from test_fabu.utill.util import get_txt,url,url_add,IMGPATH,get_time
g = get_data()
class Tianjia(unittest.TestCase):
    '''添加嘉宾模块'''
    def setUp(self):

        self.u=url()+url_add()

    def tearDown(self):

        g.close()
    def test_case3(self):
        '''成功添加一名手机号第二位为3的嘉宾'''

        f=get_txt()
        self.data={}
        self.data['eid']=1011
        self.data['realname']=f.get_name()
        self.data['phone']=f.get_phone('13')
        self.data['email']=f.get_email()
        r=requests.post(self.u,self.data)
        self.res=r.json()
        print(self.res)
        g.con_mysql()
        sql='select * from sign_guest where phone="%s" and realname="%s";'
        select_result=g.execute_sql(sql %(self.data['phone'],self.data['realname']))

        self.assertTrue('add guest success','massage')
        self.assertEqual(1,select_result)
        self.assertTrue(10000, 'status')
    def test_case4(self):
        '''添加一位手机号第二位为2的手机号添加嘉宾失败'''

        f = get_txt()
        self.data = {}
        self.data['eid'] = 1011
        self.data['realname'] = f.get_name()
        self.data['phone'] = f.get_phone('12')
        self.data['email'] = f.get_email()
        r = requests.post(self.u, self.data)
        self.res = r.json()
        print(self.res)

        g.con_mysql()
        sql = 'select * from sign_guest where phone="%s" and realname="%s";'
        select_result = g.execute_sql(sql % (self.data['phone'], self.data['realname']))

        self.assertTrue('phone error','massage')
        self.assertEqual(0,select_result)
        self.assertTrue(10027, 'status')


    def test_case5(self):
        '''添加一位手机号第一位为2的手机号添加嘉宾失败'''

        f = get_txt()
        self.data = {}
        self.data['eid'] = 1011
        self.data['realname'] = f.get_name()
        self.data['phone'] = f.get_phone('25')
        self.data['email'] = f.get_email()
        r = requests.post(self.u, self.data)
        self.res = r.json()
        print(self.res)

        g.con_mysql()
        sql = 'select * from sign_guest where phone="%s" and realname="%s";'
        select_result = g.execute_sql(sql % (self.data['phone'], self.data['realname']))

        self.assertTrue('phone error','massage')
        self.assertEqual(0,select_result)
        self.assertTrue(10027, 'status')


    def test_case6(self):
        '''添加一位手机号为12的手机号添加嘉宾失败'''

        f = get_txt()
        self.data = {}
        self.data['eid'] = 1011
        self.data['realname'] = f.get_name()
        self.data['phone'] = f.get_phone('151')
        self.data['email'] = f.get_email()
        r = requests.post(self.u, self.data)
        self.res = r.json()
        print(self.res)

        g.con_mysql()
        sql = 'select * from sign_guest where phone="%s" and realname="%s";'
        select_result = g.execute_sql(sql % (self.data['phone'], self.data['realname']))

        self.assertTrue('phone error', 'massage')
        self.assertEqual(0, select_result)
        self.assertTrue(10027, 'status')


if __name__=='__main__':
    unittest.main()