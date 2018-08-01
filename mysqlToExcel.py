#!/usr/bin/env python3
#_*_ coding:utf-8 _*_

import sys
import xlwt
import MySQLdb
import datetime

db = MySQLdb.connect(
    "**",
    "**",
    "**",
    "**",
    charset='utf8'
)

sql = "select * from 20180507temp"
cursor = db.cursor()
count = cursor.execute(sql)
print count

sheet_name="20180801temp"

cursor.scroll(0, mode='absolute')
results = cursor.fetchall()
fields = cursor.description
workbook = xlwt.Workbook()

sheet = workbook.add_sheet(sheet_name, cell_overwrite_ok=True)
out_path="E:\\tmp\\20180801temp.xlsx"

for field in range(0, len(fields)):
    sheet.write(0, field, fields[field][0])

row = 1
col = 0
for row in range(1, len(results) + 1):
    for col in range(0, len(fields)):
        sheet.write(row, col, u'%s' % results[row - 1][col])

workbook.save(out_path)