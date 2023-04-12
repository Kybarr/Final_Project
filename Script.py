import datetime
import random

def Membuat_nomor_Transaksi():
    nomor_transaksi = random.randint(100000, 999999)
    return nomor_transaksi

def tambah_item(item_list, nama_item, jumlah_item, harga_item):
    item_list.append({'Nama': nama_item, 'Jumlah': jumlah_item, 'harga_item': harga_item})

def perbarui_nama_item(item_list, item_lama, item_baru):
    for item in item_list:
        if item['Nama'] == item_lama:
            item['Nama'] = item_baru

def perbarui_jumlah_item(item_list, nama, jumlah_baru):
    for item in item_list:
        if item['Nama'] == nama:
            item['Jumlah'] = jumlah_baru

def perbarui_harga_item(item_list, nama, harga_baru):
    for item in item_list:
        if item['Nama'] == nama:
            item['harga_item'] = harga_baru

def hapus_item(item_list, nama):
    for item in item_list:
        if item['Nama'] == nama:
            item_list.remove(item)
            print(f'Item {nama} telah dihapus dari keranjang')
            return

    print(f'Item {nama} tidak ditemukan di keranjang')

def print_struk(nama_pembeli, nomor_transaksi, item_list):
    now = datetime.datetime.now()
    print('-------------------------------------------------')
    print('-------------------------------------------------')
    print(f'       STRUK BELANJA  NOMOR TRANSAKSI {nomor_transaksi}  ')
    print('-------------------------------------------------')
    print('-------------------------------------------------')
    print(f'Tanggal: {now.strftime("%d-%m-%Y")}')
    print(f'Waktu  : {  now.strftime("%H:%M:%S")}\n')
    print(f'Nama Pembeli: {nama_pembeli}\n')

    total_harga = 0
    for item in item_list:
        subtotal = item['Jumlah'] * item['harga_item']
        total_harga += subtotal
        print(f'{item["Nama"]} x{item["Jumlah"]}: Rp {subtotal}')
    print(f'Total: Rp {total_harga}')
    print('=================================================')

item_list = []
cart_list = []

print('-------------------------------------------------')
print('-------------------------------------------------')
print('SELAMAT DATANG DI ANDI MART SELAMAT BERBELANJA')
print('-------------------------------------------------')
print('-------------------------------------------------')

print("Masukkan Nama Anda  ")
nama_pembeli = input("=")

while True:
    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("-=-=-=-=-=-=-=-=-= WELCOME -=-=-=-=-=-=-=-=-=-=-=-")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("-=-=-=-=-=-=-=-+  CUSTOMERS -=-=-=-=-=-=-=-=-=-=-=")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    if len(item_list) == 0:
        print("Tidak ada item yang ada di keranjang\n")
    else:
        print("Berikut ini adalah daftar item yang sudah ada di keranjang:\n")
        for item in item_list:
            print('----------------------------------------------------------------------------')
            print(f'Nama Item : {item["Nama"]} |Jumlah Item : x{item["Jumlah"]} | Harga Barang : Rp {item["Jumlah"] * item["harga_item"]}    |')
            print('----------------------------------------------------------------------------')

        
    print("\nSilakan pilih menu di bawah ini:")
    print("1. Tambah item ke keranjang")
    print("2. Update nama item di keranjang")
    print("3. Perbarui jumlah item di keranjang")
    print("4. Perbarui harga item di keranjang")
    print("5. Hapus item dari keranjang")
    print("6. Hapus semua item yang ada di keranjang")
    print("7. Lihat Struk Belanja")
    print("8. Lihat Keranjang")
    print("9. Keluar dari program")
    print("Masukkan pilihan Anda ")
    pilihan = input("=")

    if pilihan == '1':
        nama_item = input("Masukkan nama item yang ingin ditambahkan: ")
        jumlah_item = int(input("Masukkan jumlah item yang ingin ditambahkan: "))
        harga_item = int(input("Masukkan harga item: "))
        tambah_item(item_list, nama_item, jumlah_item, harga_item)
        print(f'{jumlah_item} {nama_item} telah ditambahkan ke keranjang')

    elif pilihan == '2':
        item_lama = input("Masukkan nama item lama: ")
        item_baru = input("Masukkan nama item baru: ")
        perbarui_nama_item(item_list, item_lama, item_baru)
        print(f'Nama item {item_lama} telah diubah menjadi {item_baru}')

    elif pilihan == '3':
        nama_item = input("Masukkan nama item: ")
        jumlah_baru = int(input("Masukkan jumlah item yang baru: "))
        perbarui_jumlah_item(item_list, nama_item, jumlah_baru)
        print(f'Jumlah item {nama_item} telah diubah menjadi {jumlah_baru}')

    elif pilihan == '4':
        nama_item = input("Masukkan nama item: ")
        harga_baru = int(input("Masukkan harga item yang baru: "))
        perbarui_harga_item(item_list, nama_item, harga_baru)
        print(f'Harga item {nama_item} telah diubah menjadi {harga_baru}')

    elif pilihan == '5':
        nama_item = input("Masukkan nama item yang ingin dihapus: ")
        hapus_item(item_list, nama_item)

    elif pilihan == '6':
        item_list.clear()
        print('semua item dikeranjang sudah dihapus')

    elif pilihan == '7':
        nomor_transaksi = Membuat_nomor_Transaksi()
        print_struk(nama_pembeli, nomor_transaksi, item_list)
        item_list = []

    elif pilihan == '8':
        print('Berikut ini adalah daftar item yang sudah ada di keranjang:\n')
        for item in item_list:
            print(f'{item["Nama"]} x{item["Jumlah"]}: Rp {item["Jumlah"] * item["harga_item"]}')

    elif pilihan == '9':
        print('Terimakasih Sudah Mengunjungi Toko Kami Silahkan Datang Kembali')
        break

    else:
        print("Pilihan tidak valid, silakan masukkan angka pilihan yang benar!")