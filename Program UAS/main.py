from view.view_nilai import *
from model.daftar_nilai import *


while True:
    print()
    print("Pilih Menu")
    print()
    print("|1| Tambah Data")
    print("|2| Ubah Data")
    print("|3| Hapus Data")
    print("|4| Cari Data")
    print("|5| Lihat Data")
    print("|6| Keluar Program")
    tanya = int(input(">> PILIH MENU : "))

    if tanya == 1:
        tambah_data()
    elif tanya == 2:
        ubah_data()
    elif tanya == 3:
        hapus_data()
    elif tanya == 4:
        cari_data()
    elif tanya == 5:
        cetak_daftar_nilai()
    elif tanya == 6:
        print("Program Selesai")
        break