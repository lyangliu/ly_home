#!/usr/bin/python
#_*_ UTF-8 _*_

import requests
import json

'''
response = requests.get('http://httpbin.org')
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)
'''

'''
requests.post('http://httpbin.org/post')
requests.put('http://httpbin.org/put')
requests.delete('http://httpbin.org/delete')
requests.head('http://httpbin.org/get')
request.optional('http://htttpbin.org/get')

'''
'''
response = requests.get('http://httpbin.org')      #请求命令
print(response.text)


response = requests.get('http://httpbin.org/get?name=germey&age=22')   #带参数的请求命令方法一
print(response.text)

data = {
        name:germey
        age:22
        }
response = requests.get('http://httpbin.org/get',params = data)   #带参数的请求命令方法二
print(response.text)

'''

response = requests.get('http://httpbin.org/get')
print(type(response.text))
print(response.json())
print(json.loads(response.text))
print(type(response.json()))


response = requests.get("https://github.com/favicon.ico")
print(type(response.text),type(response.content))
print(response.text)
print(response.content)




