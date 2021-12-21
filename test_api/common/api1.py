# 封装调用http接口请求
import requests
import pytest
import json
import sys
# sys.path.append('/Users/K/PycharmProjects/pythonProject/pytest_api/common/api1.py')
# pytest终端找不到模版main函数能找到

class HttpRequest:

    def http_request(self, url, params, method):
        respones = ''
        if method.upper() == 'POST':
            try:
                respones = requests.post(url, params)
                print('正在进行post请求...响应如下：', respones)
            except Exception as e:
                print(f'post请求失败，原因是{e}')

        elif method.upper == 'GET':
            try:
                respones = requests.get(url, params)
                print('正在进行get请求...响应如下')
            except Exception as e:
                print(f'get请求失败，原因是{e}')
        return respones


http = HttpRequest()

import pytest_api

from pytest_api.common import read1

cases = read1.read_data('../../pytest_api/data/test_api.xlsx', 'Sheet1')

test_data = [{'url': 'http://appdev.api.versa-ai.com/user/auth/mobileAccount', 'method': 'POST',
              'data': "{'appSource': 'appstore','appVersion': '5.2.2','appkey': 'test','clientType': 'app',\n'countryCode': 'CN','deviceId': '0D6E3B76-0820-47D0-8295-FB689642B430','idfa': '90848FCF-53AD-4AA7-BCCB-FF7194338185','isoCode': '86','lang': 'zh-cn','mnet': 'wifi','mobileNo': '15137610001','mobileType': 'iPhone12,1','mobileTypeCode': 'iPhone12,1','osType': 'iOS','osVersion': '14.6','password': '123456','sign': '3B6A5C20C911A0345E27A68F4E70CFD6','timestamp': '1635333153917'}",
              'Status_code': 200,
              'Expect_res': '{"responseCode": "0000","responseMsg": "成功","result": {"uid": "519940105613135872","registerTime": 1614939381199,"avatar": "","nickname": "151****0001","userToken":"KO_UUfhmT0iQ6k3h5RMRwA","mobileIsoCode": "86","mobileNo": "15137610001","praiseCount": 0,"followCount": 2,"fansCount": 0,"workCount": 5,"isFollow": false,"following": 0,"isPasswordSet": true,"status": 1,"unreadMessageCount": 0,"countryCode": "CN","isVip": 1,\n"vipExpireDate": 1696867199000},"success": true}'}]




@pytest.mark.parametrize('case_info',cases)
def test_read(case_info):
    # print(case_info['url'])
    res = http.http_request(url=case_info['url'], params=case_info['data'], method=case_info['method'])
    print(res)
    print(case_info['expect'])
    # assert res.status_code == case_info['status_code']
    print(type(case_info['expect']))
    assert res.json() == eval(case_info['expect'])
#
if __name__ == '__main__':
    pytest.main(['-s', 'api1.py'])








