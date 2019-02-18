import requests
import time
import json
# q = "未达到退休年龄的单位职工非因工死亡，单位是否需要支付死亡待遇。可以享受哪些死亡待遇"
q = {"question": "下面来点简单的小例子说明把"}
# a = "具体办法见（川人社发〔2013〕54号）文件。领取条件：（1）在服刑或劳教期间死亡的，不发给死亡待遇；（2）政府规定实行火葬而未实行的（经有关部门批准可不火葬的少数民族人员或其他人员、向医疗机构自愿捐献遗体人员、失踪经人民法院宣告死亡人员除外），不支付丧葬补助费；（3）下列情况不支付一次性抚恤金：无直系亲属或法定供养关系的人；被有权机关认定为涉嫌犯罪造成死亡的；经司法部门结论为畏罪自杀造成死亡的；犯罪被人民法院判处执行死刑的."
# a = "者因其他原因，使人民的安全健康和国家资财遭到严重威胁，需要紧急处理的；（二）生产设备、交通运输线路、公共设施发生故障，影响生产和公众利益，必须及时抢修的；（三）必须利用法定节日或公休假日的停产期间进行设备检修、保养的；（四）为完成国防紧急任务，或者完成上级在国家计划外安排的其他紧急生产任务，以及商业、供销企业在旺季完成收购、运输、加工农副产品紧急任务的。政策依据：《劳动部〈贯彻国务院关于职工工作时间的规定〉的实施办法》（劳部发〔1995〕143号）第七条1995年3月26日"
start = time.time()
url = "http://192.168.102.232:5000/FQA/%s" % json.dumps(q)
print(url)
result_list = json.loads(requests.get(url).text)
result_list.sort(key=lambda a: a[1], reverse=True)
for i in result_list:
    print(i[0])
    print(i[1])
    print(i[2])
    print(i[3])
    print("*"*20)
print("consume: %s" % (time.time() - start))

