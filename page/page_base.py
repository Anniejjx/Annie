
import pymysql
class get_data():
    def con_mysql(self):
        try:
            self.con = pymysql.connect('localhost', 'root', 'root', 'learn')
        except:
            print('数据库连接失败')
        else:
            self.cur = self.con.cursor()
        return self.con,self.cur
    def execute_sql(self,sql):
        return self.cur.execute(sql)

    def close(self):
        self.cur.close()
        self.con.close()

