# LinkedList
LinkedList atau daftar berantai adalah salah satu struktur data yang berguna dalam pemrograman. Dalam LinkedList, setiap elemen (node) terdiri dari data dan pointer ke elemen berikutnya dalam daftar. Dalam Python, kita dapat membuat LinkedList dengan menggunakan class dan objek.
Penggunaan resource harap digunakan dengan baik.

<img width="227" alt="image" src="https://user-images.githubusercontent.com/94363381/219299725-c28419d9-c416-41be-b63a-3f90cc82bdc5.png">
# ------------
# Queue
Queue dapat diimplementasikan menggunakan modul queue. Modul ini menyediakan beberapa kelas dan fungsi untuk membuat dan mengelola antrian (queue). 
import queue
**Pada Resource ini penggunaan queue pada antrian pasien**
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

<img width="242" alt="image" src="https://user-images.githubusercontent.com/94363381/219301818-a9810bac-bc35-434a-bf97-5e7bc308177b.png">

# -----------
# Tree
Tree adalah struktur data yang terdiri dari node atau simpul yang terhubung melalui edge atau sisi. Setiap simpul pada tree dapat memiliki beberapa simpul anak, kecuali simpul-simpul yang berada pada level terakhir atau disebut sebagai daun (leaf).

Dalam Python, tree dapat diimplementasikan menggunakan kelas dan objek. Berikut ini adalah contoh implementasi sederhana dari tree dalam Python:

class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = []
    def add_child(self, node):
        self.children.append(node)
    def traverse(self):
        print(self.data)
        for child in self.children:
            child.traverse()

Pada contoh di atas, kita menggunakan kelas TreeNode untuk merepresentasikan simpul pada tree. Setiap simpul memiliki beberapa properti, yaitu data dan children. Properti data digunakan untuk menyimpan nilai atau data pada simpul, dan properti children digunakan untuk menyimpan daftar simpul anak. Method add_child digunakan untuk menambahkan simpul anak ke dalam simpul tertentu. Method traverse digunakan untuk mengeksekusi fungsi print untuk semua simpul pada tree, dimulai dari simpul yang diinisialisasi.

**Contoh penggunaan kelas TreeNode: (Terdapat pada resource)**
