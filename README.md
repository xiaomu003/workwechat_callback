# workwechat_callback
workwechat_callback 是为了简化开发者对企业微信API回调接口的使用而设计的。

本库仅做示范用，并不保证完全无bug。

另外，作者会不定期更新本库，但不保证与官方API接口文档同步，因此一切以官方文档为准。

更多来自个人开发者的其它语言的库推荐：

    python: https://github.com/sbzhu/weworkapi_python
    ruby: https://github.com/mycolorway/wework
    php: https://github.com/sbzhu/weworkapi_php
    golang : https://github.com/doubliekill/EnterpriseWechatSDK 1006401052yh@gmail.com

#搭建环境

需要搭建python3.5+django2.1框架开发环境，参阅python官方文档以及django2.1的配置。本文基于linux环境开发。
接入过程

首先，如果你没有企业微信的话，需要在企业微信官网注册一个企业。

在自建应用详情页，点击“接收消息”的“设置API接收”按钮，进入配置页面。

按要求填写应用的URL、Token以及EncodingAESKey：

    URL 是企业后台接收企业微信推送请求的访问协议和地址，支持http或https协议
    Token 可由企业任意填写，用于生成签名
    EncodingAESKey 用于消息体的加密，是AES密钥的Base64编码

随后记录这些参数，将其填写到 callback/views.py  的对应字段。
#初始化项目



项目解密逻辑主要逻辑封装在  由企业微信体用的下载的python版本WXBizMsgCrypt.py进行兼容目前python3.5可以正常运行
对应的处理逻辑均在callback/views.py在我们可以根据实际场景修改其中逻辑。

项目配置完成后，我们可以使用以下命令进行后台运行server：

nohup python3


在设置API接收页面点击保存，回调完成，此时在应用中发送一条文本，视频，图片消息，应用会被动回复已发送的内容。

其他代码逻辑，根据业务需求，修改对应的函数或模块。
#项目目录结构


