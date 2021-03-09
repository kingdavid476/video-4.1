#Loops and Iteration 
'''
Menentukan waktu luang yang dapat membantu penyusunan jadwal setiap harinya
'''


print("========= Selamat Datang di Alat Pembantu Penghitung Waktu Luang  =========")
waktu = 24 

while waktu <= 24 :
    kegiatan = str(input("Apakah kegiatan yang ingin anda lakukan ? Ketik tidak ada apabila tidak ada lagi kegiatan :" ))
    if kegiatan == "tidak ada" :
        print("Sisa waktu luang anda adalah",waktu,"jam")
        break
    else :
        pass
    waktu_kegiatan = float(input("Berapa lamakah anda akan melakukan kegiatan tersebut (dalam jam) ? :"))
    waktu = waktu - waktu_kegiatan
    if waktu > 0 :
        print(kegiatan,"akan menghabiskan waktu",waktu_kegiatan,"jam","dan anda masih memiliki sisa waktu",waktu,"jam")
    elif waktu == 0 : 
        print("Anda tidak memiliki waktu luang")
        break
    elif waktu < 0 :
        print("Kegiatan anda melebihi batas waktu per harinya,disarankan untuk merubah jadwal anda")
        break