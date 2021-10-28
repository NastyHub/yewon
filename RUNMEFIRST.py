import sqlite3


#데이터베이스를 설정함
#봇 돌리기 전에 실행해주세요

conn = sqlite3.connect("database.db")
c = conn.cursor()

#혹시 초기화 하려면 아랫줄 샾(#) 지워주세요
#c.execute("""DROP TABLE playermoney, bankinfo, blackmarket""")

c.execute("""CREATE TABLE playermoney(id integar, wallet integar, bank integar)""")
c.execute("""CREATE TABLE bankinfo(interest integar, totalmoney integar, conversionrate integar, auth_key integar)""")
c.execute("""CREATE TABLE blackmarket(rate integar, moneyleft integar, auth_key integar)""")

c.execute("""INSERT INTO bankinfo VALUES(0, 0, 0, 123)""")
c.execute("""INSERT INTO blackmarket VALUES(0, 0, 0, 123)""")

conn.commit()