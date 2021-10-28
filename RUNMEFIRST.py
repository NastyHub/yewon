import sqlite3


#데이터베이스를 설정함
#봇 돌리기 전에 실행해주세요

conn = sqlite3.connect("database.db")
c = conn.cursor()

#혹시 초기화 하려면 아랫줄 샾(#) 지워주세요
c.execute("""DROP TABLE playermoney""")
c.execute("""DROP TABLE banklist""")
c.execute("""DROP TABLE blackmarket""")

c.execute("""CREATE TABLE playermoney(userid INTEGAR, nickname TEXT, wallet INTEGAR, blackmoney INTEGAR, bank INTEGAR)""")
c.execute("""CREATE TABLE banklist(bankname TEXT, bankid INTEGAR, interest INTEGAR, totalmoney INTEGAR, conversionrate INTEGAR, auth_key INTEGAR)""")
c.execute("""CREATE TABLE blackmarket(fee INTEGAR, moneyleft INTEGAR, auth_key INTEGAR)""")

c.execute("""INSERT INTO banklist VALUES("찬우은행", 1, 0, 0, 0, 123)""")
c.execute("""INSERT INTO banklist VALUES("국민은행", 2, 0, 0, 0, 123)""")
c.execute("""INSERT INTO blackmarket VALUES(0, 0, 123)""")


conn.commit()