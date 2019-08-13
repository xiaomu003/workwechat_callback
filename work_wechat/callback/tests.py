from django.test import TestCase
from callback.tool.callback.WXBizMsgCrypt import Prpcrypt
# Create your tests here.
import base64
import string
import random
import hashlib
import time
import struct
from Crypto.Cipher import AES
import xml.etree.cElementTree as ET
import sys
import socket
# reload(sys)

# sys.setdefaultencoding('utf-8')


a= 'ZtiWBTUom0oQgG8ze2FzPiuiknRbv/E+MQwidPF+nUCk9ThIZM7tvIJWUSusnTf4b0DZuLCYEs7Hl9ZGA/ln9vujd191JBGMolWLob4AoiMoyq+RavjuGC9pa/eeaHkpvBKMtxFxGb6NscGv3sKBm0ELcz9CH/xSbrzwIC6ptqvQ1HJwDFiGkyPcQ8GuDsX+/EYKrQtCLIMaKGaEAIQLT4A8WOEFaqQtPfi+cdrtrJ3LheRbnmzoCZx4lnz3uMVUsR7tmte6VC4OLxDsQ4kOwYriQlkQThUcYBqBg92no7KwyLT8c8iKG6CwyUfALO2h6Y6BtjWdOIplA/Y9B0I/zBZsmylrP3e2e/15ZNoS2Q/nRxV6ubQsAmNO1qJ3zY9=='


def decrypt(text):
    # def decrypt(self,text):
    """对解密后的明文进行补位删除
    @param text: 密文
    @return: 删除填充补位后的明文

    """
    print('需要解密的xml:%s' % text)
    sEncodingAESKey='EOTdyLkc5d8Dwx1jU5t70ljqu7tnDVJftF9k93A8dBM'
    cryptor = AES.new(base64.b64decode(sEncodingAESKey+"="), AES.MODE_CBC, base64.b64decode(sEncodingAESKey+"=")[:16])
    # 使用BASE64对密文进行解码，然后AES-CBC解密
    # plain_text  = cryptor.decrypt(base64.b64decode(text)).decode('utf-8','ignore')
    print(len(text))
    plain_text = cryptor.decrypt(base64.b64decode(text)).decode('utf-8')

    # pad = ord(plain_text[-1])
    pad = ord(str(plain_text, encoding='utf-8', errors='ignore')[-1])
    # 去掉补位字符串
    # pkcs7 = PKCS7Encoder()
    # plain_text = pkcs7.encode(plain_text)
    # 去除16位随机字符串
    content = plain_text[16:-pad]
    # xml_len = socket.ntohl(struct.unpack(
    #     "I", bytes(content[: 4], encoding='utf-8'))[0])
    xml_len = socket.ntohl(struct.unpack("I", content[: 4])[0])
    xml_content = content[4: xml_len + 4]
    # from_receiveid = content[xml_len+4:]
    from_receiveid = content[xml_len + 4:].decode('utf-8')

    return 0, xml_content

decrypt(a)

print(decrypt(a))
