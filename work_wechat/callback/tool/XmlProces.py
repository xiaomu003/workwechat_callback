
class XmlProces:
    def trans_dict_to_xml(self,data):
        """
        将 dict 对象转换成企业微信交互所需的 XML 格式数据

        :param data: dict 对象
        :return: xml 格式数据
        """

        xmli = []
        for k in data.keys():

            v = data.get(k)
            if k not in ('CreateTime', 'image', 'Image','Video','video'):
                v = '<![CDATA[{}]]>'.format(v)
            if isinstance(v,dict):
                xml2=[]
                for i in v.keys():
                    j=v.get(i)
                    l = '<![CDATA[{}]]>'.format(j)
                    xml2.append('<{key}>{value}</{key}>'.format(key=i, value=l))
                v='{}'.format(''.join(xml2))
            xmli.append('<{key}>{value}</{key}>'.format(key=k, value=v))

        return '<xml>{}</xml>'.format(''.join(xmli))
