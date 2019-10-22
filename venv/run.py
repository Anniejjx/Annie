import unittest
from test_fabu.utill.util import get_time,CASEPATH,REPORTPATH
from HTMLTestReportCN import HTMLTestRunner
datetime=get_time()
tests=unittest.defaultTestLoader.discover(CASEPATH)
f=open(REPORTPATH+'/'+datetime+'.html','wb')
runner=HTMLTestRunner(stream=f,title='自动化测试报告',tester='雷诺，蓝晴')
runner.run(tests)
f.close()