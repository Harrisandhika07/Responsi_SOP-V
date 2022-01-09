#Responsi SOP V
#manajemen ram

def menu():
    print("===============pilihan menu====================")
    print(" 1 . simulasi manajemen ram")
    print(" 2 . simulasi penjadwalan round robin")
    print(" 3 . keluar")
    print("===============================================")

def manajemen_ram():
    ram = int(input("masukan jumlah kapasitas RAM awal (GB) : "))
    petabit = int(input("masukan jumlah petabit (GB) : "))
    so = int(input("masukan jumlah ram yang dipakai oleh so (GB) : "))
    kapasitasprogram1 = int(input("masukan jumlah kapasitas program 1 (GB) : "))
    kapasitasprogram2 = int(input("masukan jumlah kapasitas program 2 (GB) : "))
     #rumus ram terpakai
    ramterpakai1 = (so + kapasitasprogram1)
    ramterpakai2 = (ramterpakai1 + kapasitasprogram2)

     #rumus petabit
    petabit = (ram / petabit)
    petabitakhir =(petabit * 1048576)#KBps

     #rumus ram tersisa
    ramtersisa1 = (ram - so)
    ramtersisa2 = (ramtersisa1 - kapasitasprogram1)
    ramtersisa3 = (ramtersisa2 - kapasitasprogram2)

    print("------------HARIS A-----------------")
    print("kapasitas total RAM : ",ram, "GB")
    print("total petabit : ",petabit, "GB")
    print("kapasitas per petabit : ",petabitakhir, "KBps")
    print("total RAM terpakai : ",ramterpakai2, "GB")
    print("total RAM tidak terpakai : ",ramtersisa3,"GB")
    print("jumlah blok bernilai 1 : ",ramterpakai2 )
    print("jumlah blok bernilai 0 : ",ramtersisa3 )

def manajemen_rr():
    if __name__ =="__main__":
        print("masukan nilai yang ingin dihitung : ")
    total_waktu_proses = int(input())
    jumlah_waktu  = 0
    jumlah_waktu_tunggu = 0
    proses = []
    waktu_tunggu = 0
    waktu_penyelesaian = 0

    for _ in range(total_waktu_proses):

        print("Masukkan waktu kedatangan proses dan waktu burst")
        input_info = list(map(int, input().split(" ")))
        kedatangan, burst, sisa_waktu = input_info[0], input_info[1], input_info[1]
        proses.append([kedatangan, burst, sisa_waktu, 0])

    print("masukan jumlah quantum waktu : ")
    quantum_waktu = (int(input()))

    while jumlah_waktu != 0 :
         for i in range(len(proses)) :
           if proses[i][2] <= quantum_waktu and proses[i][2] >= 0:
                jumlah_waktu_tunggu += proses[i][2]
                jumlah_waktu -= proses[i][2]
           elif proses[i][2] > 0 :
                proses[i][2] -= quantum_waktu
                jumlah_waktu -= quantum_waktu
                jumlah_waktu_tunggu += quantum_waktu

           if proses[i][2] == 0 and proses[i][3] != 1:
                waktu_tunggu += jumlah_waktu_tunggu - proses[i][0] - proses[i][1]
                waktu_penyelesaian += jumlah_waktu_tunggu - proses[i][0]
                proses[i][3] = 1

    print("\nJumlah rata-rata waktu : ", (waktu_tunggu * 1) / total_waktu_proses)
    print("Jumlah rata-rata waktu tunggu : ", (jumlah_waktu_tunggu * 1) / total_waktu_proses)

menu()
pilihan = int(input("pilih nomor : "))

if pilihan == 1 :
    manajemen_ram()
elif pilihan == 2 :
    manajemen_rr()
elif pilihan == 3 :
    print("anda telah keluar dari program")
    exit()
else :
    print("yang anda inputkan salah")