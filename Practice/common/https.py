import requests


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



test_data = [{'url': 'https://devapi.jingsocial.com/api/material/content/library/index', 'method': 'get',
                  'params': {'content_access_level': 2},
                  'headers': {'Content-Type': 'application/json', 'J-CustomerUUID': '657ab8920581edbb'},
                  'data': None, 'status_code': 200}]


if __name__ == '__main__':
    a = login_token()
    print(a)

    x = HttpRequest()
    res = x.http_request(method=test_data[0]['method'], url=test_data[0]['url'], params=test_data[0]['params'], headers=test_data[0]['headers'], data=test_data[0]['data'])
    print(res.json())

