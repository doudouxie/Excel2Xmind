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
Temp4 ={'我的（模块）': {'券包（子模块1）': {'优惠券中心（子模块2）': {'领取优惠券（功能点）': {'cases': {'/*1*/测试2，是否能领取未开始的优惠券/*（前置条件）进入我的>领取优惠券*/': {'1. 选择还未开始的优惠券\n2. 点击领取': ['1', '.', ' ', '提', '示', '：', '未', '到', '领', '取', '时', '间']}, '/*6*/tc：测试1，是否能领取未开始的优惠券/*（前置条件）进入我的>领取优惠券*/': {'1. 选择还未开始的优惠券\n2. 点击领取': ['1', '.', ' ', '提', '示', '：', '未', '到', '领', '取', '时', '间']}}}}}}, 'X产品1（#105）': {'订单管理（子模块）': {'订单列表（子模块）': {'新增订单（功能点）': {'cases': {'/*1*/添加上架商品，选择有效用户，新增成功/*笔记：前置条件*/': {'1. 选择商品 c001\n2. 选择用户 nemo\n3. 选择收货地址\n4. 点击保存按钮': ['1', '.', ' ', '加', '载', '商', '品', '信', '息', '\n', '2', '.', ' ', '加', '载', '用', '户', '信', '息', '\n', '3', '.', ' ', '加', '载', '收', '货', '地', '址', '信', '息', '\n', '4', '.', ' ', '提', '示', '保', '存', '成', '功']}, '/*2*/添加未上架商品，新增失败': {'Null': ['N', 'u', 'l', 'l']}, '/*4*/添加已锁定用户，新增失败': {'Null': ['N', 'u', 'l', 'l']}}}}}}}

design_sheet1(Temp4)

#read_xmind()