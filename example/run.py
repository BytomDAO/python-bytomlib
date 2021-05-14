# coding:utf-8


from pybtmsdk import BytomAPI

api = BytomAPI()

ret = api.wallet_info()
print(ret)