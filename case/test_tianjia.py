import requests
import unittest
from test_fabu.page.page_base import get_data
from test_fabu.utill.util import get_txt,url,url_event

g=get_data()
class fabu(unittest.TestCase):

    '''添加发布会模块'''
    def setUp(self):
        self.u=url()+url_event()
    def test_case1(self):
        '''name为空时，发布会发布失败'''

        f = get_txt()
        data={}
        data['eid']=f.get_num(0,100)
        data['name']=''
        data['status']=f.get_num(0,1)
        data['limit']=f.get_num(20,200)
        data['address']=f.get_address()
        data['start_time']=f.get_datetime()
        r=requests.post(self.u,data)
        res=r.json()
        print(res)
        g.con_mysql()
        sql='select * from sign_event where id="%d" and name="%s";'
        select_result=g.execute_sql(sql %(data['eid'],data['name']))

        try:
            self.assertTrue('parameter error', 'massage')
            self.assertEqual(0, select_result)
            self.assertTrue(10021, 'status')

        except:
            print('Fail')
            raise Exception

    def test_case2(self):

        '''成功发布一条发布会'''

        f = get_txt()
        self.data = {}
        self.data['eid'] = f.get_num(1, 100)
        self.data['name'] = f.get_name() + '电影发布会'
        self.data['status'] = f.get_num(0, 1)
        self.data['limit'] = f.get_num(20, 200)
        self.data['address'] = f.get_address()
        self.data['start_time'] = f.get_datetime()
        r = requests.post(self.u, self.data)
        self.res = r.json()
        print(self.res)
        g.con_mysql()

        sql = 'select * from sign_event where id="%d" and name="%s";'
        select_result = g.execute_sql(sql % (self.data['eid'], self.data['name']))

        try:
            self.assertTrue('add event success', 'massage')
            self.assertEqual(1, select_result)
            self.assertTrue(10000, 'status')

        except:
            print('Fail')
            raise Exception
    def test_case3(self):

        '''eid为空时，发布会发布失败'''

        f = get_txt()
        self.data = {}

        self.data['name'] = f.get_name() + '电影发布会'
        self.data['status'] = f.get_num(0, 1)
        self.data['limit'] = f.get_num(20, 200)
        self.data['address'] = f.get_address()
        self.data['start_time'] = f.get_datetime()
        r = requests.post(self.u, self.data)
        self.res = r.json()
        print(self.res)
        g.con_mysql()

        sql = 'select * from sign_event where name="%s";'
        select_result = g.execute_sql(sql % (self.data['name']))


        try:
            self.assertTrue('parameter error', 'massage')
            self.assertEqual(0, select_result)
            self.assertTrue(10021, 'status')

        except:
            print('Fail')
            raise Exception
    def tearDown(self):
        g.close()

if __name__=='__main__':
    unittest.main()
