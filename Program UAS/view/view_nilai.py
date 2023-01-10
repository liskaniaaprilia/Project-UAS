from model.daftar_nilai import*


def cetak_daftar_nilai():
    if len(data_mahasiswa) <= 0:
        no_data()
    else:
        print("Daftar Nilai")
        print()
        print("=======================================================================")
        print("|      Nama      |     NIM     | Tugas |  UTS  |  UAS  |     Akhir    |")
        print("=======================================================================")
        for a in data_mahasiswa.items():
            print(f"| {a[0]:15} | {a[1][0]:10} | {a[1][1]:5} | {a[1][2]:5} | {a[1][3]:5} | {a[1][4]:12} |")
            print("=======================================================================")


def cetak_hasil_pencarian():
    if len(data_mahasiswa) <= 0:
        cari_data()