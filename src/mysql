import pymysql

db = pymysql.connect(
    "&&",
    "&&",
    "&&",
    "&&"
)

cursor = db.cursor()

cursor.execute("select * from p_party_member limit 1")
data = cursor.fetchall()
print data
db.close()