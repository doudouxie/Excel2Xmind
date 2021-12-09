import xmind
from xmind.core.markerref import MarkerId

def read_xmind():
    workbook = xmind.load('test.xmind')
    print(workbook.getData())

def design_sheet1(dicts):
    workbook = xmind.load('test1.xmind')
    sheet = workbook.getPrimarySheet()
    sheet.setTitle('First Sheet')
    root_topic = sheet.getRootTopic()
    root_topic.setTitle('root node')
    dict_item(dicts,root_topic)
    xmind.save(workbook)

def dict_item(dicts,topic):
    for key in dicts:
        subtopic = topic.addSubTopic()
        subtopic.setTitle(key)
        subtopic.addMarker(MarkerId.priority1)
        subtopic.setPlainNotes('note')
        if isinstance(dicts[key],dict):
            dict_item(dicts[key],subtopic)
    return True

Temp ={"智能合板":{"无任务":{"刷新按钮":"步骤描述"},"H22":22,"H23":{"H31":1}}}
Temp2 ={"智能合板":{"无任务":{"刷新按钮1":"步骤描述"},"H22":22,"H23":{"H31":1}}}
Temp3 = dict(Temp,**Temp2)
Temp4 = {'a': {'b': {'c': {'d': ['ab', 'ef']}, 'd': ['aa']}, 'f': {'c': ['xx']}}}
design_sheet1(Temp4)

#read_xmind()