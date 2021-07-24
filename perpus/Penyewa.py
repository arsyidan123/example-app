import member
print("1. Tambah Penyewa")
print("2. Ubah Penyewa")
print("3. Penyewa Cancel")
print("4. Tampilkan JOB")
print("5. Cari Penyewa")
menu2= int (input('[Member] pilih='))
if (menu2==1):
    nama=input("Nama:")
    alamat=input("Alamat:")
    tujuan=input("Tujuan:")
    data=[nama,alamat,tujuan]
    member.add(data)
elif(menu2==2):
    id_member=input("No Penyewa:")
    nama=input('Nama:')
    alamat=input('alamat:')
    tujuan=input('tujuan:')
    data=[nama,alamat,tujuan,id_member]
    member.edit(data)
elif (menu2==3):
    id_member=input('No. penyewa:')
    data=[id_member]
    confirm=input('Yakin cancel penyewa ini?[y/n]')
    if(confirm=="y"):
        member.delete(data)
    else:
        print('Data batal di hapus')
elif (menu2==4):
    member.show()

elif (menu2==5):
    id_member=input('No. member:')
    data=[id_member]
    member.search(data)
else:
    print('Menu tidak tersedia')
