import psycopg2
from psycopg2.extras import DictCursor
conn = psycopg2.connect(
    host = "127.0.0.1",
    user = "postgres",
    password = "оооо",
    port = 5432,
    dbname = "phonebook"
)

a = int(input("What do u want?"))
#if conn:
#    print('connected')

cursor = conn.cursor(cursor_factory= DictCursor)
def ins ():
    id = input()
    fname= input()
    lname = input()
    pnumber = input()
    sql = f"INSERT INTO phonebook (id, fname, lname, pnumber) VALUES('{id}', '{fname}', '{lname}', '{pnumber}')"
    cursor.execute(sql)
    conn.commit()

def showall():
    cursor.execute("SELECT * FROM phonebook")
    res = cursor.fetchall()
    print(res)

def showpart():
    what = input()
    if (what == "id"):
        id = int(input())
        sql=f"SELECT * FROM phonebook WHERE (id = '{id}')"
        cursor.execute(sql)
        res = cursor.fetchall()
        print(res)
    if (what == "fname"):
        fname = input()
        sql=f"SELECT * FROM phonebook WHERE (fname = '{fname}')"
        cursor.execute(sql)
        res = cursor.fetchall()
        print(res)
    if (what == "lname"):
        lname = input()
        sql=f"SELECT * FROM phonebook WHERE (lname = '{lname}')"
        cursor.execute(sql)
        res = cursor.fetchall()
        print(res)
    if (what == "pnumber"):
        pnumber = int(input())
        sql=f"SELECT * FROM phonebook WHERE (pnumber = '{pnumber}')"
        cursor.execute(sql)
        res = cursor.fetchall()
        print(res)
    
def deleting():
    what = input()
    if (what == "id"):
        id = int(input())
        sql=f"DELETE FROM phonebook WHERE id = '{id}'"
        cursor.execute(sql)
       
    if (what == "fname"):
        fname = input()
        sql=f"DELETE FROM phonebook WHERE fname = '{fname}'"
        cursor.execute(sql)
        
    if (what == "lname"):
        lname = input()
        sql=f"DELETE FROM phonebook WHERE lname = '{lname}'"
        cursor.execute(sql)
    if (what == "pnumber"):
        pnumber = int(input())
        sql=f"DELETE FROM phonebook WHERE pnumber = '{pnumber}'"
        cursor.execute(sql)
        


if (a==1):
    showall()
elif(a==2):
    ins()
elif(a==3):
    showpart()
elif(a==4):
    deleting()