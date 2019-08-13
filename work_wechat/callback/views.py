from django.shortcuts import render

from django.http import HttpResponse
from callback.tool.callback.WXBizMsgCrypt import WXBizMsgCrypt
from callback.tool.XmlProces import XmlProces
import xml.etree.ElementTree as ET


def cburl(request,msg_signature,timestamp,nonce,echostr):
    sToken = "Token"
    sEncodingAESKey = "EncodingAESKey "
    sCorpID = "CorpID "
    wxcpt = WXBizMsgCrypt(sToken, sEncodingAESKey, sCorpID)
    if request.method == 'GET':
        print("the GET method")
        msg_signature = request.GET.get('msg_signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        echostr = request.GET.get('echostr')
        wxcpt = WXBizMsgCrypt(sToken, sEncodingAESKey, sCorpID)
        ret, sEchoStr = wxcpt.VerifyURL(msg_signature, timestamp, nonce, echostr)
        if (ret != 0):
            print("ERR: VerifyURL ret: " + str(ret))

        return HttpResponse('%s' % sEchoStr)


    if (request.method == 'POST'):
        print("the POST method")
        postxml = request.body
        msg_signature = request.GET.get('msg_signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')

        ret, sMsg = wxcpt.DecryptMsg(postxml, msg_signature, timestamp, nonce)
        if (ret != 0):
            print("ERR: VerifyURL ret: " + str(ret))
            return HttpResponse(str(ret))
        #print('接收到未解密的xml{}'.format(postxml))
        #print('接收到解密的xml{}'.format(sMsg))



        print('==========================')
        #进行xml的解析
        rxml = ET.fromstring(sMsg)
        type=rxml.find('MsgType')
        type_text=type.text
        '''
        文本,图片,视频需要进行被动回复
        '''

        if type_text =='text':
            dia={
                'ToUserName':rxml.find('FromUserName').text,
                'FromUserName':rxml.find('ToUserName').text,
                'CreateTime':timestamp,
                'MsgType':type_text,
                # 'Content':rxml.find('Content').text
                'Content':rxml.find('Content').text
            }
            dia_xml=XmlProces()
            dia_print=dia_xml.trans_dict_to_xml(dia)
            #print('构造未加密的xml= {}'.format(dia_print))


            ret1, sEncryptMsg = wxcpt.EncryptMsg(dia_print, nonce)
            #print('构造加密的xml= {}'.format(sEncryptMsg))

            if (ret1 != 0):
                print("ERR: EncryptMsg ret: " + str(ret1))
                return HttpResponse(str(ret1))
            return HttpResponse(sEncryptMsg)


        elif  type_text in('image','video') :
            dia = {
                'ToUserName': rxml.find('FromUserName').text,
                'FromUserName': rxml.find('ToUserName').text,
                'CreateTime': timestamp,
                'MsgType': type_text,
                type_text.title(): {'MediaId': rxml.find('MediaId').text}
            }
            print(type_text.title())
            dia_xml = XmlProces()
            dia_print = dia_xml.trans_dict_to_xml(dia)
            #print('构造未加密的xml= {}'.format(dia_print))

            ret2, sEncryptMsg = wxcpt.EncryptMsg(dia_print, nonce)
            #print('构造加密的xml= {}'.format(sEncryptMsg))
            if (ret2 != 0):
                print("ERR: EncryptMsg ret: " + str(ret2))
                return HttpResponse(str(ret2))
            return HttpResponse(sEncryptMsg)


        else:
            if (ret != 0):
                print("ERR: DecryptMsg ret: " + str(ret))
                return HttpResponse(str(ret))
            return HttpResponse('success')





# Create your views here.

