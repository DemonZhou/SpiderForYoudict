import pymysql
class DB :
    def __init__(self):
        pass

    def Add(self, word, zhmeaning, cont):
        try :
            conn = pymysql.connect(host='localhost',user='root',passwd='root',db='youdict',charset='utf8')
            cur = conn.cursor()
            cur.execute("Insert into youdict (word,zhmeaning,cont) VALUES (%s,%s,%s) ", (word, zhmeaning, cont))
            conn.commit()
        except Exception as e :
            print (e)
            conn.rollback()
        finally:
            cur.close()
            conn.close()