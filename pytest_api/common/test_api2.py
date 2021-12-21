import requests
import pytest


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


# if __name__ == '__main__':
#     url = "https://api.apiopen.top/getJoke?page=1&count=2&type=video"
#
#     # data = {"page":"1","count":"2","type":"video"}
#     res=HttpRequest().http_request(url=url,data=None, http_method="get")
#     print(res)

# from pytest_api.common import read1
# cases = read1.read_data('../../pytest_api/data/test_api.xlsx', 'Sheet1')

http = HttpRequest()

test_data = [{'url': 'http://appdev.api.versa-ai.com/user/auth/mobileAccount', 'method': 'POST',
              'data': {'appSource': 'appstore', 'appVersion': '5.2.2', 'appkey': 'test', 'clientType': 'app',
                       'countryCode': 'CN',
                       'deviceId': '0D6E3B76-0820-47D0-8295-FB689642B430',
                       'idfa': '90848FCF-53AD-4AA7-BCCB-FF7194338185',
                       'isoCode': '86', 'lang': 'zh-cn', 'mnet': 'wifi', 'mobileNo': '15137610001',
                       'mobileType': 'iPhone12,1',
                       'mobileTypeCode': 'iPhone12,1', 'osType': 'iOS', 'osVersion': '14.6', 'password': '123456',
                       'sign': '3B6A5C20C911A0345E27A68F4E70CFD6', 'timestamp': '1635333153917'},
              'Status_code': 200,
              'Expect_res': {'responseCode': '0000', 'responseMsg': '成功', 'result': {'uid': '519940105613135872', 'registerTime': 1614939381199, 'avatar': '', 'nickname': '151****0001', 'userToken': 'Tewhgy4_QryeZ-vvSqkF6A', 'mobileIsoCode': '86', 'mobileNo': '15137610001', 'praiseCount': 0, 'followCount': 2, 'fansCount': 0, 'workCount': 5, 'isFollow': False, 'following': 0, 'isPasswordSet': True, 'status': 1, 'unreadMessageCount': 0, 'countryCode': 'CN', 'isVip': 1, 'vipExpireDate': 1743955199000}, 'success': True}}
             ]


@pytest.mark.parametrize('case_info',test_data)
def test_read(case_info):
    # print(case_info['url'])
    print(case_info['data'])
    print(case_info['Status_code'])
    print(case_info['Expect_res']['success'])
    res = http.http_request(url=case_info['url'], data=case_info['data'], http_method=case_info['method'])
    print(res.json())
    print(res.json()['success'])
    # assert res.json() == case_info['Expect_res']
    assert res.json()['success'] == case_info['Expect_res']['success']





if __name__ == '__main__':
    pytest.main(['-sv', 'test_api2.py'])