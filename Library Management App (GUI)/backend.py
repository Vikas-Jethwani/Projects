# Author : Vikas Jethwani(Stan.Vj)
import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    curr = conn.cursor()
    curr.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")   # pass NULL as id for auto-increment
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    curr = conn.cursor()
    curr.execute("INSERT INTO book VALUES(NULL,?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    curr = conn.cursor()
    curr.execute("SELECT * FROM book")
    rows = curr.fetchall()
    conn.close()
    return rows

def search(title='', author='', year='', isbn=''):
    conn = sqlite3.connect("books.db")
    curr = conn.cursor()
    curr.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = curr.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))   # inside a tuple to avoid SQL injections
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))
    conn.commit()
    conn.close()



connect()
