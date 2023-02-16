class Node : #buat class untuk sampul linked list (node)
    def __init__(self, Nama = None, Nim = None, next = None):
        self.Nama = Nama
        self.next = next
        self.Nim = Nim

    def __str__(self): #mengembalikan data node
        self.Nim
        self.Nama
        return

class LinkedList : #buat class untuk linked list
    def __init__(self, head = None):
        self.head = head #kepala dari sampul

    def printall(self):
        if self.head == None:
            return print('Data Sedang Kosong!')
        else :
            node = self.head # deklarasikan variable baru dengan head (kepala dari sampul (node))
            while(node.next != None): # melakukan perulangan untuk menampilkan semua data yang tersimpan dalam setiap sampul (node)
                print(node.Nama,":",node.Nim, end=" -> ") 
                node = node.next # data yang sudah ditampilkan akan di lanjutkan ke data yang selanjutnya
            
            print(node.Nama,":",node.Nim)

    def add_data(self, Nama, Nim): # nambah data 
        newNode = Node(Nama, Nim) # deklarasikan variable baru untuk node baru
        if self.head == None: # periksa apakah node dalam keadaan kosong atau tidak
            self.head = newNode
        else:
            table = self.head # buat variable baru untuk kepala sampul (node), jika syarat if tidak terpenuhi
            while(table.next != None): 
                table = table.next # kemudian data sudah sukses di tambahkan menggunakan perulangan
            table.next = newNode

    def add_front_data(self, Nama, Nim): # nambah data dari depan
        newNode = Node(Nama,Nim)
        if(self.head == None):
            self.head = newNode
        else :
            prevHead = self.head # buat variable untuk menampung node yang sudah ada
            self.head = newNode # data yang diinput dijadikan kepala sampul
            newNode.next = prevHead # dimasukkan ke variable yang sudah menampung node yang sudah ada

    def remove_data (self, key): 
        table = self.head # buat variable baru untuk menampung data node
        # jika key yang dimasukkan adalah head dari node mka kita perlu untuk memindahkannya ke data selanjutnya
        if key == table.Nama: 
            self.head = table.next
            table = None # data akan dikosongkan jika if terpenuhi
        else :
            while table is not None: # melakukan perulangan untuk menemukan data yang dimasukkan di dalam data node
                if table.Nama == key:
                    break
                prev = table
                table = table.next
            prev.next = table.next 
            table = None # jika data sudah ketemu maka data akan langsung dikosongkan

    def pop (self):
        if self.head == None:
            return
        else:
            node = self.head
            prevNode = node
            if node.next == None:
                self.head = None
            while node.next != None:
                prevNode = node
                node = node.next

            prevNode.next = None
            del node


LL = LinkedList()
while True :
    try : 
        print('\t[-Program Linked List-] \n[1] {satu}\n[2] {dua}\n[3] {tiga}\n[4] {empat}'
                .format(
                    satu = 'Nambah Data Node',
                    dua = 'Delete Data Node',
                    tiga = 'Tampil Semua Data Node',
                    empat = 'Keluar'
                )
                
        )

        inputan = int(input("Masukkan Pilihan : "))
        if inputan == 1 :
            while True:
                print ('-'*36)
                print('\t[-Program Add Data-] \n[1] {satu}\n[2] {dua}\n[3] {tiga}'
                    .format(
                        satu = 'Nambah Data',
                        dua = 'Nambah Data Node Dari Depan',
                        tiga = 'Exit'
                    ))
                pilih = int (input("Masukkan Pilihan : "))
                if pilih == 2 :
                    x = (input("Masukkan Nama : ")).title()
                    x2 = input("Masukkan NIM : ")
                    LL.add_front_data(x, x2)
                    print ("Sukses Menambahkan Data")
                    continue
                elif pilih == 1 :
                    x1 = input("Masukkan Nama : ").title()
                    x3 = input ("Masukkan NIM : ")
                    LL.add_data(x1, x3)
                    print ('Sukses Menambahkan Data')
                    continue
                elif pilih == 3 :
                    break
            print ('-'*36)

        if inputan == 2:
            while True :
                print ('-'*36)
                print('\t[-Program Add Data-] \n[1] {satu}\n[2] {dua}\n[3] {tiga}'
                    .format(
                        satu = 'Delete Data dari Belakang',
                        dua = 'Delete Data',
                        tiga = 'Exit'
                    ))
                pilih = int (input("Masukkan Pilihan : "))
                if pilih == 1:
                    if LL.head == None:
                        LL.printall()
                        print ('-'*36)
                        break
                    else:
                        LL.pop()
                        print ("Delete Sukses")
                        continue
                elif pilih == 2:
                    if LL.head == None:
                        LL.printall()
                        print ('-'*36)
                        break
                    try :
                        LL.printall()
                        print ('-'*36)
                        x = input("Masukkan Data Nama Mahasiswa Yang Mau Di Delete : ").title()
                        LL.remove_data(x)
                        print ("Delete Sukses")
                        continue
                    except:
                        LL.printall()
                        print('Data Yang Dimasukkan Tidak Sesuai')
                        continue

                elif pilih == 3:
                    break

        if inputan == 3:
            print ('-'*36)
            LL.printall()
        
        if inputan == 4:
            break
    except: 
        print("Masukkan Pilihan dengan Benar!")
        print("-"*36)


'''    
LL = LinkedList()
LL.head = Node("1")
d1 = Node("2")
d2 = Node("3")
d3 = Node("4")

LL.head.next = d1
d1.next = d2
d2.next = d3
'''
'''
LL = LinkedList ()
p = input("Data : ")
LL.add_data("5")
LL.add_data("6")
LL.remove_data("1")
LL.add_front_data(p)
#LL.pop()
LL.printall()
'''