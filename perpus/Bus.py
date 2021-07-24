import data_bus
print("1. Tambah Bus")
print("2. Ubah Bus")
print("3. Hapus Bus")
print("4. Tampilkan Bus")
print("5. Cari Bus")
menu2= int (input('[Member] pilih='))
if (menu2==1):
    Kilometer=input("Kilometer:")
    Body=input("Body:")
    Mesin=input("Mesin:")
    data=[Kilometer,Body,Mesin]
    data_bus.add(data)
elif(menu2==2):
    nomor_bus=input("No Bus:")
    Kilometer=input("Kilometer:")
    Body=input("Body:")
    Mesin=input("Mesin:")
    data=[Kilometer,Body,Mesin,nomor_bus]
    data_bus.edit(data)
elif (menu2==3):
    nomor_bus=input('No. Bus:')
    data=[nomor_bus]
    confirm=input('Yakin cancel Bus ini?[y/n]')
    if(confirm=="y"):
        data_bus.delete(data)
    else:
        print('Data batal di hapus')
elif (menu2==4):
    data_bus.show()

elif (menu2==5):
    nomor_bus=input('No. Bus:')
    data=[nomor_bus]
    data_bus.search(data)
else:
    print('Menu tidak tersedia')

