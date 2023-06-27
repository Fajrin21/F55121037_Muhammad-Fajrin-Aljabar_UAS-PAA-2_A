# F55121037_Muhammad-Fajrin-Aljabar_UAS-PAA-2_A

Nama  : Muhammad Fajrin Aljabar
Nim   : F55121037
Kelas : A

**Kesimpulan Sorting & ShortestPath**
**Analisis Algoritma Bubble Sort:**
Bubble Sort adalah salah satu algoritma pengurutan sederhana yang bekerja dengan membandingkan dan menukar elemen-elemen adjacent dalam sebuah array secara berulang hingga array terurut secara keseluruhan. Berikut adalah analisis dari algoritma Bubble Sort yang terdapat dalam kode program:
**Waktu Eksekusi:**

Algoritma Bubble Sort memiliki kompleksitas waktu rata-rata O(n^2), di mana n adalah jumlah elemen dalam array.
Pada setiap iterasi, algoritma melakukan perbandingan dan penukaran pada elemen-elemen adjacent.
Jika array terurut secara terbalik, maka algoritma akan memerlukan n iterasi untuk mengurutkan array tersebut.
Pada kasus terbaik, di mana array sudah terurut secara ascending, algoritma akan memiliki kompleksitas waktu O(n), namun pada umumnya kompleksitasnya O(n^2).

**Kelebihan:**
Implementasi yang sederhana dan mudah dipahami.
Cocok digunakan pada kasus-kasus di mana jumlah elemen yang diurutkan relatif kecil.

**Kekurangan:**
Bubble Sort memiliki performa yang relatif buruk dibandingkan dengan algoritma pengurutan lainnya, terutama pada kasus-kasus dengan jumlah elemen yang besar.
Algoritma ini cenderung lambat karena memerlukan banyak iterasi dan pertukaran elemen.

**Worst Case:**
Pada kasus terburuk, algoritma Bubble Sort akan memerlukan waktu eksekusi yang paling lama.
Jika array tidak terurut dan berada dalam urutan terbalik, maka setiap elemen akan memerlukan iterasi penukaran hingga mencapai posisi yang tepat.
Dalam hal ini, kompleksitas waktu Bubble Sort adalah O(n^2), di mana n adalah jumlah elemen dalam array.

**Best Case:**
Pada kasus terbaik, algoritma Bubble Sort memiliki keunggulan ketika array sudah terurut secara ascending.
Jika array sudah terurut, maka algoritma hanya akan melakukan perbandingan sekali pada setiap iterasi.
Dalam hal ini, kompleksitas waktu Bubble Sort adalah O(n), di mana n adalah jumlah elemen dalam array.

**Average Case:**
Pada kasus rata-rata, algoritma Bubble Sort memiliki kompleksitas waktu O(n^2).
Algoritma akan melakukan iterasi sebanyak n kali untuk memastikan bahwa array sudah terurut secara keseluruhan.
Jumlah penukaran dan perbandingan yang dilakukan pada setiap iterasi akan bergantung pada urutan elemen dalam array.



**Analisis Algoritma Insertion Sort:**
Insertion Sort adalah algoritma pengurutan yang bekerja dengan membagi array menjadi dua bagian: bagian terurut dan bagian belum terurut. Pada setiap iterasi, algoritma memilih elemen dari bagian belum terurut dan memasukkannya ke tempat yang tepat dalam bagian terurut. Berikut adalah analisis dari algoritma Insertion Sort yang terdapat dalam kode program:

**Waktu Eksekusi:**
Algoritma Insertion Sort memiliki kompleksitas waktu rata-rata O(n^2), di mana n adalah jumlah elemen dalam array.
Pada setiap iterasi, algoritma membandingkan elemen saat ini dengan elemen-elemen sebelumnya dalam bagian terurut.
Jika elemen saat ini lebih kecil, algoritma memindahkan elemen-elemen yang lebih besar ke posisi selanjutnya dan menyisipkan elemen saat ini pada posisi yang tepat.
Pada kasus terbaik, di mana array sudah terurut secara ascending, algoritma akan memiliki kompleksitas waktu O(n), namun pada umumnya kompleksitasnya O(n^2).

**Kelebihan:**
Implementasi yang sederhana dan mudah dipahami.
Lebih cepat daripada Bubble Sort dalam beberapa kasus tergantung pada data yang diurutkan.
Cocok digunakan pada kasus-kasus di mana jumlah elemen yang diurutkan relatif kecil atau array sudah hampir terurut.

**Kekurangan:**
Insertion Sort memiliki performa yang buruk pada kasus-kasus dengan jumlah elemen yang besar.
Algoritma ini memerlukan banyak perpindahan elemen saat memasukkan elemen ke dalam bagian terurut.

**Worst Case:**
Pada kasus terburuk, algoritma Insertion Sort akan memerlukan waktu eksekusi yang paling lama.
Jika array tidak terurut dan berada dalam urutan terbalik, maka setiap elemen akan memerlukan perbandingan dengan semua elemen sebelumnya dalam bagian terurut.
Dalam hal ini, kompleksitas waktu Insertion Sort adalah O(n^2), di mana n adalah jumlah elemen dalam array.

**Best Case:**
Pada kasus terbaik, algoritma Insertion Sort memiliki keunggulan ketika array sudah terurut secara ascending.
Jika array sudah terurut, maka algoritma hanya perlu melakukan perbandingan dengan elemen sebelumnya dalam bagian terurut dan tidak perlu melakukan perpindahan elemen.
Dalam hal ini, kompleksitas waktu Insertion Sort adalah O(n), di mana n adalah jumlah elemen dalam array.

**Average Case:**
Pada kasus rata-rata, algoritma Insertion Sort memiliki kompleksitas waktu O(n^2).
Algoritma akan membandingkan setiap elemen dengan elemen sebelumnya dalam bagian terurut, dan jika diperlukan, akan melakukan perpindahan elemen.
Jumlah perbandingan dan perpindahan yang dilakukan pada setiap iterasi akan bergantung pada urutan elemen dalam array.

**Kesimpulan:**
Dalam kode program tersebut, Bubble Sort dan Insertion Sort digunakan untuk mengurutkan array dengan elemen-elemen yang sudah didefinisikan. Kedua algoritma ini memiliki kompleksitas waktu yang relatif buruk pada kasus-kasus dengan jumlah elemen yang besar. Jika digunakan pada jumlah elemen yang kecil, keduanya dapat menghasilkan hasil pengurutan yang benar. Namun, jika digunakan pada jumlah elemen yang besar, lebih disarankan untuk menggunakan algoritma pengurutan yang lebih efisien seperti Merge Sort atau Quick Sort.



**Analisis Algoritma TSP (Traveling Salesman Problem):**
**Worst Case:**
Pada kasus terburuk, algoritma TSP menggunakan pendekatan heuristik yang tidak menjamin solusi optimal.
Algoritma ini menggunakan pendekatan approximate (seperti algoritma nearest neighbor) untuk mencari solusi yang memungkinkan, tetapi tidak menjamin solusi terbaik.
Kompleksitas waktu algoritma TSP tergantung pada metode heuristik yang digunakan. Dalam kasus ini, algoritma menggunakan pendekatan approximate dari library NetworkX, yang dapat memiliki kompleksitas waktu eksponensial pada beberapa kasus dengan jumlah simpul yang besar.

**Best Case:**
Pada kasus terbaik, algoritma TSP menggunakan metode heuristik yang menghasilkan solusi optimal.
Namun, pendekatan approximate yang digunakan pada algoritma ini umumnya tidak menghasilkan solusi terbaik dalam kasus terbaik.
Kompleksitas waktu algoritma TSP tetap tergantung pada metode heuristik yang digunakan.

**Average Case:**
Pada kasus rata-rata, algoritma TSP menggunakan pendekatan approximate yang menghasilkan solusi yang cukup baik secara umum.
Algoritma ini dapat mencapai solusi yang mendekati optimal, tetapi tidak menjamin solusi terbaik dalam semua kasus.
Kompleksitas waktu algoritma TSP tetap tergantung pada metode heuristik yang digunakan.
Kesimpulan Algoritma TSP:

Algoritma TSP menggunakan pendekatan approximate untuk mencari solusi yang memungkinkan dalam permasalahan jalur terpendek untuk mengunjungi setiap simpul (node) dalam graf.
Kompleksitas waktu algoritma TSP bervariasi tergantung pada metode heuristik yang digunakan.
Algoritma ini cocok digunakan pada kasus dengan jumlah simpul yang relatif kecil atau dalam situasi di mana solusi yang mendekati optimal sudah cukup memadai.
Namun, algoritma ini dapat menghadapi kendala dalam kasus dengan jumlah simpul yang sangat besar, karena pendekatan approximate tidak menjamin solusi terbaik.
Lebih disarankan untuk menggunakan algoritma eksakta yang khusus dirancang untuk menyelesaikan permasalahan TSP dalam kasus dengan jumlah simpul yang besar.

**Analisis Algoritma Dijkstra:**
**Worst Case:**
Pada kasus terburuk, algoritma Dijkstra akan memerlukan waktu eksekusi yang paling lama.
Jika graf memiliki jumlah simpul yang sangat besar atau memiliki banyak jalur terhubung, algoritma akan memerlukan banyak perbandingan dan pembaruan jarak terpendek pada setiap simpul.
Kompleksitas waktu algoritma Dijkstra dalam kasus terburuk adalah O((V + E) log V), di mana V adalah jumlah simpul (vertices) dan E adalah jumlah tepi (edges) dalam graf.

**Best Case:**
Pada kasus terbaik, algoritma Dijkstra memiliki keunggulan ketika simpul tujuan dapat dicapai dengan sedikit perbandingan dan pembaruan jarak terpendek.
Jika simpul tujuan adalah tetangga langsung dari simpul awal, maka algoritma hanya perlu satu iterasi untuk menemukan jalur terpendek.
Dalam hal ini, kompleksitas waktu algoritma Dijkstra adalah O(V), di mana V adalah jumlah simpul dalam graf.

**Average Case:**
Pada kasus rata-rata, algoritma Dijkstra mencari jalur terpendek dengan kompleksitas waktu O((V + E) log V).
Algoritma akan melakukan perbandingan dan pembaruan jarak terpendek pada setiap simpul dalam graf, sehingga kompleksitasnya bergantung pada ukuran graf.

**Kesimpulan Algoritma Dijkstra:**
Algoritma Dijkstra digunakan untuk mencari jalur terpendek antara dua simpul dalam graf dengan bobot tepi yang tak negatif.
Algoritma ini efisien dalam menemukan jalur terpendek pada graf dengan jumlah simpul yang relatif kecil dan bobot tepi yang tak negatif.
Namun, kompleksitas waktu algoritma Dijkstra meningkat secara eksponensial seiring dengan peningkatan jumlah simpul dan tepi dalam graf.
Lebih baik menggunakan algoritma lain seperti Algoritma A* untuk kasus dengan graf yang lebih besar atau dengan bobot tepi yang tidak terlalu terbatas.
Algoritma Dijkstra juga cocok untuk kasus-kasus di mana keberadaan jalur terpendek sangat penting.




