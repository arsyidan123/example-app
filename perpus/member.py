import mysql.connector
import connect

db = connect.koneksi()

#menambahkan data
def add(data):
    cursor = db.cursor()
    sql="""INSERT INTO penyewa (nama,alamat,tujuan) VALUES (%s,%s,%s)"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data Penyewa berhasil ditambahkan!'.format(cursor.rowcount))

#menaampilkan seluruh data
def show():
    cursor=db.cursor()
    sql="""SELECT*FROM penyewa"""
    cursor.execute(sql)
    result=cursor.fetchall()
    print("+--+----------------------------+---------------+---------------+")
    print("|ID|Nama\t\t\t|Alamat","\t|","Tujuan","\t|")
    print("+--+----------------------------+---------------+---------------+")
    for data in result:
        print("|",data[0],"|",data[1],"\t\t\t|",data[2],"\t|",data[3],"\t|")
        print("+--+----------------------------+---------------+---------------+")

#mengubah data dalam tabel
def edit(data):
    cursor = db.cursor()
    sql="""UPDATE penyewa SET nama=%s,alamat=%s,tujuan=%sWHERE no=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data member berhsil dirubah!'.format(cursor.rowcount))

#meghapus data dari tabel member
def delete(data):
    cursor=db.cursor()
    sql="""DELETE FROM penyewa WHERE no=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data member berhasil dihapus!'.format(cursor.rowcount))

#mencari data dalam tabel member
def search(data):
    cursor=db.cursor()
    sql="""SELECT*FROM penyewa WHERE no=%s"""
    cursor.execute(sql,data)
    result=cursor.fetchall()
    print("+--+----------------------------+---------------+---------------+")
    print("|ID|Nama\t\t\t|Alamat","\t|","Tujuan","\t|")
    print("+--+----------------------------+---------------+---------------+")
    for data in result:
        print("|",data[0],"|",data[1],"\t\t\t|",data[2],"\t|",data[3],"\t|")
        print("+--+----------------------------+---------------+---------------+")    
