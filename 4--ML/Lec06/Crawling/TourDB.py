import pymysql
class MyDB:
    def __init__(self):
        self.db_init()
    def db_init(self):
        self.con = pymysql.connect(
            host='127.0.0.1', user='root', 
            password='1234', db='pythondb',
            charset='utf8')

    def db_free(self):
        if self.con:
            self.con.close()

    def tour_crawlingInsert(self,title, price, term, area):
        sql = '''insert into tour_crawling
                (title, price, term , area)
                value(%s,%s,%s,%s) '''
        with self.con.cursor() as cursor :
            cursor.execute(sql,(title, price, term, area))
        self.con.commit()

if __name__ == "__main__":
    db = MyDB()
    db.tour_crawlingInsert('test', '12000만원', '0000/01/01-0000/02/02', '달나라')
    db.db_free()