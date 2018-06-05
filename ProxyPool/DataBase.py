from ProxyPool.Config import *
import pymysql
import traceback


class DataBase():
    def __init__(self):
        sqlCmd = "CREATE TABLE IF NOT EXISTS {}({} INT PRIMARY KEY AUTO_INCREMENT,{} VARCHAR(255) UNIQUE ,{} INTEGER ) ;".format(
            TABLENAME, "ID", "IP", "PORT")
        print(sqlCmd)
        try:
            self.conn = pymysql.connect(host=HOST, port=PORT, user=USRNAME, passwd=PASSWORD, db=DBNAME)
            cur = self.conn.cursor()
            cur.execute(sqlCmd)
        except:
            print("Init is error!!!")

    def AddItem(self, ip, port):
        sqlCmd = r"INSERT INTO {}({},{}) VALUES ('{}',{})".format(TABLENAME, "IP", "PORT", ip, port)
        try:
            cur = self.conn.cursor()
            cur.execute(sqlCmd)
            self.conn.commit()
        except Exception as e:
            f = open("log.txt", 'a')
            traceback.print_exc(file=f)
            f.flush()
            f.close()
            pass
        finally:
            pass

    def ShowAll(self):
        try:
            cur = self.conn.cursor()
            sqlCmd = "SELECT * FROM {}".format(TABLENAME)
            cur.execute(sqlCmd)
            rows = cur.fetchall()
            for row in rows:
                print(row)
        except:
            print("ShowAll is error!!!")
        finally:
            pass


if __name__ == "__main__":
    db = DataBase()
    for x in range(0, 100):
        ip = "192.168.0." + str(x)
        port = x
        db.AddItem(ip, port)
    db.ShowAll()
