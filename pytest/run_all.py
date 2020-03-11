# -*- coding: UTF-8 -*-
# coding=utf-8
'''
Created on 2020/3/9
@File  : run_all.py
@author: ZL
@Desc  :
'''

import pytest
import os
import sys
import subprocess

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', rootPath + '\\testresults\\pytestresult\\data', "-m=apitest"])
    subprocess.run(['allure', 'generate', rootPath + '/testresults/pytestresult/data', '-o',
                    rootPath + '/testresults/pytestresult/data/html', '--clean'], shell=True)

    # filename = rootPath + '\\testresults\\pytestresult\\data\\html' + '\\' + 'index.html'
    # send_email = SendEmail()
    # send_email.send_email(filename)
