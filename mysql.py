#!/usr/bin/env python3
#_*_ coding:utf-8 _*_

import pymysql
import xlrd
import datetime

db = pymysql.connect(
    "**",
    "**",
    "**",
    "**",
    charset='utf8'
)

cursor = db.cursor()

sql = 'insert into 20180507temp (name,sex,card_num,phone,community_id, degree,cm_major,cm_graduate_school,cm_duty,cm_marital,cm_holder,cm_remark) values (%s,%s, %s, %s,%s,%s,%s,%s,%s,%s,%s, %s)'
party = xlrd.open_workbook("E:\\tmp\\20180507temp.xlsx")
sheet = party.sheet_by_name("20180507temp")
for r in range(1, sheet.nrows):
    values =(sheet.cell(r, 0).value, sheet.cell(r, 1).value, sheet.cell(r, 2).value, sheet.cell(r, 3).value,
             sheet.cell(r, 4).value, sheet.cell(r, 6).value,sheet.cell(r, 7).value,
             sheet.cell(r, 8).value, sheet.cell(r, 9).value, sheet.cell(r, 10).value, sheet.cell(r, 11).value,
             sheet.cell(r, 12).value)
    cursor.execute(sql, values)
db.commit()
cursor.close()
db.close()