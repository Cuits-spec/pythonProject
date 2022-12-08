import requests
import json
import pytest

def login_token():
    token_url = 'https://devapi.jingsocial.com/api/user/users/login'
    token_headers1 = {
        'content-type': 'application/json;charset=UTF-8'
    }
    token_data = {"username": "kejianwei", "password": "zQ=S2VqaWFud2VpLjEyM", "validCode": ""}

    result = requests.post(url=token_url, headers=token_headers1, json=token_data)
    return (result.json() ['data'] ['identity'] ['authorization'])

class HttpRequest:

    def http_request(self, method, **kwargs):
        """获取请求参数"""
        params = kwargs.get("params")
        headers = kwargs.get("headers")
        headers['Authorization'] = login_token()
        url = kwargs.get("url")
        data = kwargs.get("data")
        json = kwargs.get("json")
        files = kwargs.get("files")

        if method == 'get':
            try:
                res = requests.get(url=url, params=params, headers=headers)
                print('正在进行get请求...响应如下')
                return res
            except Exception as e:
                print(f'get请求失败，原因是{e}')

        elif method == 'post':
            try:
                res = requests.post(url=url, params
                =params, headers=headers, data=data, json=json, files=files)
                print('正在进行post请求...响应如下：')
                return res
            except Exception as e:
                print(f'post请求失败，原因是{e}')

        elif method == 'put':
            try:
                res = requests.put(url=url, params
                =params, headers=headers, data=data, json=json, files=files)
                print('正在进行put请求...响应如下：')
                return res
            except Exception as e:
                print(f'put请求失败，原因是{e}')

        elif method == 'delete':
            try:
                res = requests.delete(url=url, params
                =params, headers=headers, data=data, json=json, files=files)
                print('正在进行delete请求...响应如下：')
                return res
            except Exception as e:
                print(f'delete请求失败，原因是{e}')

        else:
            try:
                res = requests.Request
                return res
            except Exception as e:
                print('api请求方式暂不支持')


from read_excel import read_data

cases = read_data('../test_api/Excelread/test_api.xlsx', 'Sheet2')
# print(type(cases))

test_data = [{'url': 'https://devapi.jingsocial.com/api/material/content/library/create', 'method': 'post',
              'headers': "{'Content-Type': 'application/json', 'J-CustomerUUID': '657ab8920581edbb'}",
              'data': '{"permission_ids": ["3474726f-2716-4534-ba32-fa5c3008d0d6"],"library_name": "哈哈哈","content_access_level": "2"}',
              'status_code': 200, 'expect': None},
             {'url': 'https://devapi.jingsocial.com/api/material/content/library/create', 'method': 'post',
              'headers': "{'Content-Type': 'application/json', 'J-CustomerUUID': '657ab8920581edbb'}",
              'data': '{"permission_ids": ["3474726f-2716-4534-ba32-fa5c3008d0d6"],"library_name": "哈哈哈","content_access_level": "2"}',
              'status_code': 200, 'expect': None}]

for i in test_data:
    for key,value in i.items():
        print(value)


https = HttpRequest()
@pytest.mark.parametrize('case_info', test_data)
def test_read(case_info):
    x = requests.post(test_data["url"])
    # res = https.http_request(method=test_data.get('method'), url=test_data['url'], headers=test_data['headers'], data=test_data['data'])
    # print(x)
    # print(type(x))




# if __name__ == '__main__':
#     pytest.main(['-s', 'test_htps.py'])