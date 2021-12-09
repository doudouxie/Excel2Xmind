#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time：2020/6/2 13:57
# @Email: am1122@163.com
# @Author: 'Nemo'
import csv
from config import ConfigParser


def format_case(case):
    # {'module': '3. 订单管理（模块）',
    #  'preset': None,
    #  'priority': '3',
    #  'test_results': '添加已锁定用户，新增失败',
    #  'test_steps': '添加已锁定用户，新增失败',
    #  'test_title': '添加已锁定用户，新增失败'}

    module = '/' + case['module'].replace('（', '(').replace('）', ')')  # 将模块中的中文括号替换成英文括号
    row = [
        module,
        case['test_title'],
        case['preset'],
        case['test_steps'],
        case['test_results'],
        '',
        case['priority'],
        case['category'],
        case['stage']
    ]

    return row

def format_all_cases(all_map_cases):
    file_header = ["所属模块", "用例标题", "前置条件", "步骤", "预期", "关键词", "优先级", "用例类型", "适用阶段"]
    rows = [file_header]
    for map in all_map_cases:
        for case in map['test_cases']:
            rows.append(format_case(case))
    return rows


def case2zentao(zentao_file, xmind):

    with open(zentao_file, 'w', encoding=ConfigParser.get_config('encoding', 'sys'), newline='') as f:
        writer = csv.writer(f)
        writer.writerows(format_all_cases(xmind))


if __name__ == '__main__':
    from parsercases import ParserCases
    from pprint import pprint

    p = ParserCases('../test/test_zentao.xmind')
    pprint(p.all_map_case)

    case2zentao('../test/test.csv', p.all_map_case)
