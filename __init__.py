from xml.dom.minidom import parseString
import json

if __name__ == '__main__':
    P='''<?xml version="1.0" encoding="UTF-8" ?>
<product>
    <id name="4-6480368 xyz 2019-11-27T09:44:05+00:00 42377149217171 AZ_SC9991_Dark_Wenge">1</id>
    <amount name="Principal">2711.02</amount>
    <amount name="Tax">487.98</amount>
    <fee name="TCS-IGST">-27.11</fee>
    <fee name="Commission">-319.90</fee>
    <fee name="Commission IGST">-57.58</fee>
    <fee name="FixedClosingFee">-59.00</fee>
    <fee name="FixedClosingFee IGST">-10.62</fee>
</product>'''
    doc=parseString(P)
    X=['id','amount','fee']
    d =dict()
    dt=dict()
    for i in X:
        temp=doc.getElementsByTagName(i)
        dtt=dict()
        for j in temp:
            dtt[j.getAttribute('name')]=j.childNodes[0].data
        dt[i]=dtt
    d['product']=dt
    result=json.dumps(d)
    print(result)


