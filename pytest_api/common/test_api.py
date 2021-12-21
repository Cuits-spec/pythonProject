import requests
import pytest
import json
import sys
sys.path.append('/Users/K/PycharmProjects/pythonProject/')



# import os
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)


class HttpRequest:
    @staticmethod
    def http_request(url, data=None, http_method=None, cookie=None):
        try:
            if http_method.upper() == "GET":
                res = requests.get(url, data, cookies=cookie)
                print(res.json())
            elif http_method.upper() == "POST":
                res = requests.post(url, data, cookies=cookie)
            else:
                print("输入的请求方法不对")
        except Exception as e:
            print("请求报错了:{0}".format(e))
            raise e
        return res  # 返回结果


from pytest_api.common import read1

cases = read1.read_data('/Users/K/PycharmProjects/pythonProject/pytest_api/data/test_api.xlsx', 'Sheet1')

http = HttpRequest()


@pytest.mark.parametrize('case_info', cases)
def test_read(case_info):
    # print(case_info['url'])
    res = http.http_request(url=case_info['url'], http_method=case_info['method'], data=eval(case_info['data']))
    print(res.json())

    print(case_info['status_code'])
    # print(type(case_info['expect']))
    # assert res.json()['success'] == case_info['expect']['success']
    assert res.status_code == case_info['status_code']


if __name__ == '__main__':
    pytest.main(['-s', 'test_api.py'])
    print(sys.path)
