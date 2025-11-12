# . Membuat sebauh perogram Lulus/Tidak lulus.
lulus = input("Apakah kamu lulus ujian? [ya/tidak] ")
if lulus == "ya":
  print("Selamat kamu dinyatakn lulus ujian")
else:
  print("Maaf, kamu dinyatakan tidak lulus ujian")

total_belanja = int(input("Masukan total belanja: Rp "))

bayar_belanja = int(total_belanja)

if total_belanja >= 100000:
  print("selamat, kamu mendapatkan minuman dingin tea")
  print("dan kamu juga mendapatkan diskon 5%")

  diskon = total_belanja * 5/100
  bayar = total_belanja - diskon

# Cetak struck
print(f"Total yang harus di bayarkan: Rp %s" % bayar)
print(f"Terima kasih sudah berbelanja di toko kami")
print(f"Jangan lupa datang lagi yaa....")