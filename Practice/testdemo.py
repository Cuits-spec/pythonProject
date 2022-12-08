import requests

list_url = 'https://devapi.jingsocial.com/api/material/content/library/index'
create_url = 'https://devapi.jingsocial.com/api/material/content/library/create'
update_url = 'https://devapi.jingsocial.com/api/material/content/library/update'
theme_url = 'https://devapi.jingsocial.com/api/material/content/subject/d5ZrUMbESqMJvAQwpN2f6o'
delete_url = 'https://devapi.jingsocial.com/api/material/content/library/delete'
params = {'content_access_level': 2}
headers = {
    'Content-Type': 'application/json', 'J-CustomerUUID': '657ab8920581edbb'}
json1 = {
    "permission_ids": [
        "3474726f-2716-4534-ba32-fa5c3008d0d6"
    ],
    "library_name": "gff",
    "content_access_level": "2"
}
json2 = {
    "subject_name":"h44"
}
update_json = {
    "permission_ids": [
        1,
        2,
        3
    ],
    "library_uuid": "xnJGLjaWFR4CEqjj7WF7GL",
    "library_name": "老干部hhh",
    "content_access_level": 2
}
detele_json = {
    "library_uuid":"6ouRUMxpmsEB7bwjqp4w2N"
}
r = requests.delete(url=delete_url, headers=headers, json=detele_json)
# print(r.json())


def login_token():
    token_url = 'https://devapi.jingsocial.com/api/user/users/login'
    token_headers1 = {
        'content-type': 'application/json;charset=UTF-8'
    }
    token_data = {"username": "kejianwei", "password": "zQ=S2VqaWFud2VpLjEyM", "validCode": ""}

    result = requests.post(url=token_url, headers=token_headers1, json=token_data)
    return (result.json() ['data'] ['identity'] ['authorization'])

# a = login_token()
# print(a)

def theme_list():
    headers['Authorization'] = login_token()
    theme_list_url = 'https://devapi.jingsocial.com//api/material/content/subject'
    # headers = headers
    # headers = { 'Content-Type': 'application/json', 'J-CustomerUUID': '657ab8920581edbb'}
    res = requests.get(url=theme_list_url, headers=headers)
    # print(res.headers)
    return res.json()

b = theme_list()



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









if __name__ == '__main__':
    http = HttpRequest()
    url = 'https://devapi.jingsocial.com//api/material/content/subject'
    result = http.http_request(method='get', url=url, headers=headers)
    print(result.json())


