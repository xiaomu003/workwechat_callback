# workwechat_callback


weworkapi_callback 是为了简化开发者对企业微信API回调接口的使用而设计的。

本库仅做示范用，并不保证完全无bug。

另外，作者会不定期更新本库，但不保证与官方API接口文档同步，因此一切以官方文档为准。

更多来自个人开发者的其它语言的库推荐：

- python2: https://github.com/sbzhu/weworkapi_python
- ruby: https://github.com/mycolorway/wework
- php: https://github.com/sbzhu/weworkapi_php
- golang : https://github.com/doubliekill/EnterpriseWechatSDK 1006401052yh@gmail.com

Requirement

# 搭建环境

需要搭建python3.5.2+django2.2开发环境，参阅[python官方文档]以及[django2.1的配置]。本文基于linux环境开发。

[python官方文档]: https://www.python.org/
[django2.2的配置]: https://www.djangoproject.com/

# 接入过程

首先，如果你没有企业微信的话，需要在[企业微信官网]注册一个企业。

在[自建应用]详情页，点击“接收消息”的“设置API接收”按钮，进入配置页面。

按要求填写应用的URL、Token以及EncodingAESKey：

- __URL__ 是企业后台接收企业微信推送请求的访问协议和地址，支持http或https协议
- __Token__ 可由企业任意填写，用于生成签名
- __EncodingAESKey__ 用于消息体的加密，是AES密钥的Base64编码

随后记录这些参数，将其填写到 `callback/views.py` 的对应字段。

[企业微信官网]: https://work.weixin.qq.com/
[自建应用]: https://work.weixin.qq.com/api/doc#10025

## 初始化项目

示例用到了python  django2.2框架，请开发者自行安装此库再使用。



项目解密逻辑主要逻辑封装在  由企业微信体用的下载的python2版本WXBizMsgCrypt.py进行兼容目前python3.5可以正常运行



- WXBizMsgCrypt.py文件封装了WXBizMsgCrypt接口类，提供了用户接入企业微信的三个接口，Sample.py文件提供了如何使用这三个接口的示例，ierror.py提供了错误码。
- WXBizMsgCrypt封装了VerifyURL, DecryptMsg, EncryptMsg三个接口，分别用于开发者验证接收消息的url、接收消息的解密以及开发者回复消息的加密过程。使用方法可以参考Sample.py文件。
- 本代码用到了pycrypto第三方库，请开发者自行安装此库再使用。



对应的处理逻辑均在[callback/views.py]在我们可以根据实际场景修改其中逻辑。

##  运行项目

项目配置完成后，我们可以项目目录下使用以下命令运行server：

```bash
nohup python manage.py reunserver 0.0.0.0:8080 &
```

在设置API接收页面点击保存，回调完成，此时在应用中发送一条文本，视频，图片消息，应用会被动回复已发送的内容。

其他代码逻辑，根据业务需求，修改对应的函数或模块。

[callback/views.py]: https://github.com/xiaomu003/workwechat_callback/blob/master/work_wechat/callback/views.py







