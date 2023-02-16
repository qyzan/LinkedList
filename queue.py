import time #delay untuk setiap inputan
#Operasi Create
s = []
total_per_hari = 1
#Operasi is Empety
def isEmpty (s):
    if len(s) <= 0 :
        return True
    else : 
        return False
#Operasi isFull
def isFull (s):
    if total_per_hari == 3:
        return True
    else :
        return False
        
#Operasi Enqueue
def tambah_pasien(s,data):
    global total_per_hari
    x = {'nama':data, 'no_pasien':total_per_hari}
    s.append(x)
    total_per_hari = total_per_hari + 1
    print('No Antrian %s = %s'%(x['no_pasien'],x['nama']))

#Operasi Dequeue    
def panggil_pasien (s):
    if isEmpty(s) :
        return print('Antrian Pasien Sedang Kosong')
    else : 
        p = (s.pop(0))
        return print('Memanggil Pasien No', str(p['no_pasien']), str(p['nama']))

def Tampil_Semua(s) :
    if (len(s) == 0):
        print("Data Antrian Masih Kosong. \nSilahkan Masukkan Data Antrian Terlebih Dahulu.")
    else:
        print ("\t-Semua Data-")
        for i in s: 
            time.sleep(0.2)
            print (">",'No.',i['no_pasien'], i['nama'])
        

while True:
    try:
        print('\t[-Program Antrian Pasien-] \n[1] {satu}\n[2] {dua}\n[3] {tiga}\n[4] {empat}'
            .format(
                satu = 'Tambah Antrian',
                dua = 'Panggil Pelanggan',
                tiga = 'Tampil Daftar Antrian',
                empat = 'Keluar'
            )
            
        )
        inputan = int(input("Silahkan Pilih : "))
        print ('-'*36)
        if (inputan == 1):
            pushinput = input("Masukkan data : ")
            if (isFull(s) == True):
                print ('Kapasitas Pasien Sudah Mencapai Batas Hari Ini')
                print('Silahkan Datang Kembali Besok \n -Terima Kasih-')
                if (isEmpty(s)) :
                    break
            tambah_pasien(s,pushinput)
        elif (inputan == 3):
            Tampil_Semua(s)
            x = input("Continue? (yes/no) : ").lower()
            if (x == 'yes'):
                print("-"*36)
                continue
            elif (x == 'no'):
                print ('Terima Kasih')
                break
            elif(x != 'yes' or x != 'no'):
                print('-'*36)
                print('Salah Input')
                break
            else:
                print('-'*36)
                print('> Terima Kasih')
                break

        elif (inputan == 2):
            panggil_pasien(s)
        elif (inputan == 4):
            print("> Terima Kasih")
            break
        else:
            print ("Masukkan angka sesuai Menu")
        print("\n")
        time.sleep(0.6)

    except:
        time.sleep(0.5) 
        print ('\n-Pilih dengan angka bukan huruf-\n-Jika Ingin Berhentik Ketik "4"-\n')
        continue