import sys
import os
import allure
import pytest
# from common import read1
from pytest_api.common import read1
from pytest_api.common import test_api

http1 = test_api.HttpRequest()
cases = read1.read_data('../pytest_api/data/test_api.xlsx', 'Sheet1')


# print(cases)

@pytest.mark.parametrize('case_info', cases)
def test_read(case_info):
    # print(case_info['url'])
    res = http1.http_request(url=case_info['url'], http_method=case_info['method'], data=eval(case_info['data']))
    print(res.json())

    print(case_info['status_code'])
    # print(type(case_info['expect']))
    # assert res.json()['success'] == case_info['expect']['success']
    assert res.status_code == case_info['status_code']


if __name__ == '__main__':
    # pytest.main(['-s', 'run.py'])

    # 此时生成的测试报告为json格式
    pytest.main(["-s", "--alluredir", "./allure_report", "run.py"])
    # 把生成的测试报告转成html格式
    os.system('allure generate ./allure_report/ -o ./allure_report/html/ --clean')


