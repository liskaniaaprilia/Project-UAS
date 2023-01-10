from view.input_nilai import*

data_mahasiswa = {}


def tambah_data():
    global data_mahasiswa
    print()
    print("Tambah Data")
    nama = nama_input()
    nim = nim_input()
    tugas = tugas_input()
    uts = uts_input()
    uas = uas_input()
    nilai_akhir = (tugas*30/100)+(uts*35/100)+(uas*35/100)
    data_mahasiswa[nama] = [nim, tugas, uts, uas, nilai_akhir]
    return data_mahasiswa


def ubah_data():
    print()
    print("Ubah Data Mahasiswa")
    nama = input("Nama        : ")
    if nama in data_mahasiswa.keys():
        nim   = input    ("NIM         : ")
        tugas = int(input("Nilai Tugas : "))
        uts   = int(input("Nilai UTS   : "))
        uas   = int(input("Nilai UAS   : "))
        nilaiakhir = ((tugas) * 30 / 100 + (uts) * 35 / 100 + (uas) * 35 / 100)
        data_mahasiswa[nama] = [nim, tugas, uts, uas, nilaiakhir]
    else:
        print("Data nilai{0} tidak ada".format(nama))


def hapus_data():
    print()
    print("Hapus Data Mahasiswa")
    nama = input("Nama       : ")
    if nama in data_mahasiswa.keys():
        del data_mahasiswa[nama]
    else:
        print("Data {0} tidak ada".format(nama))
    return


def cari_data():
    print()
    print("Cari Data Mahasiswa")
    nama = input("Nama        : ")
    print()
    for nama in data_mahasiswa.items():
        print("=======================================================================")
        print("|      Nama      |     NIM     | Tugas |  UTS  |  UAS  |     Akhir    |")
        print("=======================================================================")
        print(f"| {nama[1][0]:15} | {nama[0]:10} | {nama[1][1]:5} | {nama[1][2]:5} | {nama[1][3]:5} | {nama[1][4]:12} |")
        print("=======================================================================")


def no_data():
    print()
    print("Daftar Nilai")
    print()
    print("=======================================================================")
    print("|      Nama      |     NIM     | Tugas |  UTS  |  UAS  |     Akhir    |")
    print("=======================================================================")
    print("|                            TIDAK ADA DATA                           |")
    print("=======================================================================")





