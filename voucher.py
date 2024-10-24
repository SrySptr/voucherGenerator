import random
import time
import os
import pyfiglet
from pyfiglet import Figlet

def voucherMaker():
    os.system('cls' if os.name == 'nt' else 'clear')

    for i in range(2):
        time.sleep(0.2)
    print("<< ======================================== >>")
    print("||                                         ||")
    print("||      AppleID VoucherGenerator           ||")
    print("||      Made By : Suryo Saputro            ||")
    print("||      Github : SrySptr                   ||")
    print("||      Instagram : www39.srysptr.go.blok  ||")
    print("||                                         ||")
    print("<< ======================================== >>")
    print(" ")
    def generateVoucher():
        satu = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        dua = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        tiga = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        empat = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        lima = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        one = random.choice(satu)
        two = random.choice(dua)
        three = random.choice(tiga)
        four = random.choice(empat)
        five = random.choice(lima)
        kode = one+two+three+four+five
        return kode

    jml = int(input("Masukkan jumlah voucher yang akan di generate : "))
    namaFile = input("Masukkan nama file : ")
    filename = namaFile+".txt"
    with open(filename, "w") as file:
        for _ in range(jml):
            voucher = generateVoucher()
            file.write(voucher + "\n")

    for i in range(3):
        time.sleep(0.1)
    print(" ")
    print(f"Kode Voucher telah disimpan sebagai {filename}")
    print(" ")
    print("<< ======================================== >>")
    print(" ")
    aww = str(input("Ingin Melanjutkan? y/N : "))
    if aww == "y" or aww == "Y":
        voucherMaker()
    elif aww == "n" or aww == "N":
        os.system('cls' if os.name == 'nt' else 'clear')
        exit()

voucherMaker()