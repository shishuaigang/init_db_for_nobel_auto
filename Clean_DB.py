# coding=utf-8
import pymssql


class clean_DB(object):
    @staticmethod
    def clean():
        conn = pymssql.connect(host="192.168.31.99\\sql2012", user="sgshi", password="ssg12345!",
                               database="NobelTest")
        cur = conn.cursor()
        print "Connect database successfully"
        cur.execute("Use NobelTest EXEC  CP_Produce_OrderInit 'F7651B56-961B-4410-8332-5399B2147A81'")
        print "Clean done\n Ready to import order"
        conn.commit()
        cur.close()
        conn.close()
