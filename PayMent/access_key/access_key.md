### 此文件夹模块下存放用于支付的密钥及重要数据
#### 新增文件
1. wx_key.py 内容:
```python
# 微信小程序的appid和secret
MINIPROGRAM={
    'APP_ID':'appid',
    'SECRET':'secret'
}

# 微信商户id和支付交易秘钥
MCH={
    'MCH_ID':'id',
    'MCH_KEY':'secret'
}
```