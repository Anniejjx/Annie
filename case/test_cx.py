import requests
import unittest
from test_fabu.page.page_base import get_data
from test_fabu.utill.util import get_txt,url,url_sec
g=get_data()
class Chaxun(unittest.TestCase):
    '''验证发布会查询模块'''
    def setUp(self):
        self.u=url()+url_sec()
    def tearDown(self):
        g.close()


    def test_case5(self):
        '''用eid查询发布会成功'''


        self.data={}
        self.data['eid']=1011


        r=requests.get(self.u,self.data,auth=('bohe','jjx123456'))
        self.res=r.json()
        print(self.res)
        g.con_mysql()
        sql='select * from sign_event where id="%d";'
        select_result=g.execute_sql(sql %(self.data['eid']))

        self.assertTrue('success', 'massage')
        self.assertEqual(1, select_result)
        self.assertTrue(200, 'status')





    def test_case6(self):

        '''用name查询发布会成功'''


        self.data = {}
        self.data['name'] = '周星驰电影发布会'

        r = requests.get(self.u, self.data, auth=('bohe', 'jjx123456'))
        self.res = r.json()
        print(self.res)

        g.con_mysql()
        sql = 'select * from sign_event where name="%s";'
        select_result = g.execute_sql(sql % (self.data['name']))

        self.assertTrue('success', 'massage')
        self.assertEqual(1, select_result)
        self.assertTrue(200, 'status')



if __name__=='__main__':
    unittest.main()