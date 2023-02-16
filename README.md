# LinkedList
LinkedList atau daftar berantai adalah salah satu struktur data yang berguna dalam pemrograman. Dalam LinkedList, setiap elemen (node) terdiri dari data dan pointer ke elemen berikutnya dalam daftar. Dalam Python, kita dapat membuat LinkedList dengan menggunakan class dan objek.
Penggunaan resource harap digunakan dengan baik.

<img width="227" alt="image" src="https://user-images.githubusercontent.com/94363381/219299725-c28419d9-c416-41be-b63a-3f90cc82bdc5.png">

# queue
Queue dapat diimplementasikan menggunakan modul queue. Modul ini menyediakan beberapa kelas dan fungsi untuk membuat dan mengelola antrian (queue). 
import queue
#### Example
#### Membuat objek Queue
q = queue.Queue()

#### Menambahkan elemen ke dalam Queue
q.put(10)
q.put(20)
q.put(30)

#### Mendapatkan elemen pertama dari Queue
print(q.get())  # Output: 10

#### Cek apakah Queue kosong
print(q.empty())  # Output: False

#### Cek ukuran dari Queue
print(q.qsize())  # Output: 2
