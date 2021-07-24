import mysql.connector
import connect

db = connect.koneksi()

#menambahkan data
def add(data):
    cursor = db.cursor()
    sql="""INSERT INTO bus (kilometer,body,mesin) VALUES (%s,%s,%s)"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data bus berhasil ditambahkan!'.format(cursor.rowcount))

#menaampilkan seluruh data
def show():
    cursor=db.cursor()
    sql="""SELECT*FROM bus"""
    cursor.execute(sql)
    result=cursor.fetchall()
    print("+--+----------------------------+---------------+---------------+")
    print("|Nomor Bus\t|Kilometer\t|Body","\t\t|","Mesin","\t|")
    print("+--+----------------------------+---------------+---------------+")
    for data in result:
        print("|",data[0],"\t\t|",data[1],"\t\t|",data[2],"|",data[3],"\t|")
        print("+--+----------------------------+---------------+---------------+")

#mengubah data dalam tabel
def edit(data):
    cursor = db.cursor()
    sql="""UPDATE bus SET kilometer=%s,body=%s,mesin=%sWHERE nomor_bus=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data member berhsil dirubah!'.format(cursor.rowcount))

#meghapus data dari tabel member
def delete(data):
    cursor=db.cursor()
    sql="""DELETE FROM bus WHERE nomor_bus=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data bus berhasil dihapus!'.format(cursor.rowcount))

#mencari data dalam tabel member
def search(data):
    cursor=db.cursor()
    sql="""SELECT*FROM bus WHERE nomor_bus=%s"""
    cursor.execute(sql,data)
    result=cursor.fetchall()
    print("+--+----------------------------+---------------+---------------+")
    print("|Nomor Bus\t|Kilometer\t|Body","\t\t|","Mesin","\t|")
    print("+--+----------------------------+---------------+---------------+")
    for data in result:
        print("|",data[0],"\t\t|",data[1],"\t\t|",data[2],"|",data[3],"\t|")
        print("+--+----------------------------+---------------+---------------+")
