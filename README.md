Nama: Ghina Nabila Gunawan\
NPM: 2206825914\
Kelas: PBP-B\

**TUGAS 3**\

**===== Perbedaan Form POST dan Form GET dalam Django =====**\
    1. Form POST:\
    - Ketika data dikirim menggunakan metode POST, data akan dikirimkan dalam HTTP request body, sehingga data tidak terlihat di URL.\
    - Data yang dikirim melalui POST cocok untuk data sensitif atau data yang besar.\
    - Biasanya digunakan saat kita ingin mengirim data yang akan menyebabkan perubahan pada server,\ seperti membuat entri baru di basis data.\

    2. Form GET:\
    - Ketika data dikirim menggunakan metode GET, data akan \ditambahkan ke URL sebagai parameter query string.\
    - Data yang dikirim melalui GET seharusnya tidak sensitif dan \sebaiknya tidak mengandung data yang sangat besar.\
    - Biasanya digunakan saat kita ingin melakukan pencarian atau \mengakses server-side resource tanpa mempengaruhi status server.\

**===== Perbedaan antara XML, JSON, dan HTML dalam konteks pengiriman data =====**\
    1. XML (eXtensible Markup Language):\
    - XML adalah markup language yang digunakan untuk mendefinisikan\ struktur data yang dapat disesuaikan.\
    - XML menggunakan tag yang dapat disesuaikan oleh user untuk \mendefinisikan elemen-elemen data.\
    - XML lebih kompleks dan berat dibandingkan JSON dan HTML.\
    - Digunakan dalam beberapa konteks, seperti pertukaran data antar\ aplikasi dan penyimpanan konfigurasi.\
\
    2. JSON (JavaScript Object Notation):\
    - JSON adalah lightweight data format yang digunakan untuk\ pertukaran data antara aplikasi modern web.\
    - JSON menggunakan objek JavaScript untuk mewakili data dalam format teks./
    - JSON lebih mudah dibaca/diterjemahkan dalam bahasa manusia/ dan lebih mudah diurai oleh mesin dibandingkan XML./
    - Digunakan secara luas dalam RESTful API dan komunikasi antar aplikasi.\
\
    3. HTML (HyperText Markup Language):\
    - HTML adalah markup language yang digunakan untuk membuat tampilan halaman web.\
    - HTML menggambarkan struktur dan tampilan konten pada halaman web.\
    - HTML digunakan oleh web browser untuk merender halaman web.\
    - Digunakan untuk membuat user interface pada web.\
\


**===== Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern =====**\
    - JSON memiliki format yang ringan dan mudah dibaca oleh manusia \sehingga memudahkan debugging dan pengembangan.\
    - JSON dapat dengan mudah diurai oleh bahasa pemrograman yang berbeda,\ sehingga memudahkan komunikasi antara berbagai platform dan teknologi.\
    - JSON menggunakan objek JavaScript, sehingga secara alami cocok \dengan bahasa pemrograman JavaScript yang banyak digunakan di sisi web client.\
    - Dalam arsitektur RESTful API, JSON sering digunakan sebagai format \pertukaran data karena kesederhanaannya dan kemampuannya untuk \merepresentasikan berbagai jenis data.\
    - Sebagian besar bahasa pemrograman modern memiliki dukungan JSON \yang kuat, membuatnya mudah diimplementasikan di berbagai platform.\

**===== Implementasi Step-by-Step =====**\
✅ Membuat input form untuk menambahkan objek model pada app sebelumnya.
    - Membuat berkas baru pada direktori 'main' dengan nama 'forms.py' untuk membuat struktur form yang dapat menerima data produk baru.
    - Menambahkan impor pada berkas 'views.py' yaitu 'HttpResponseRedirect' , 'ProductForm' , dan 'reverse'.
    - Membuat fungsi baru dengan nama 'create_product' pada berkas tersebut yang menerima parameter 'request'.
    - Mengubah fungsi 'show_main' pada berkas 'views.py' dengan ' 'items': Item.objects.all(), ' .
    - Membuat berkas HTML baru dengan nama 'create_product.html' pada direktori 'main/templates'.
    - Membuka 'main.html' dan menambahkan beberapa baris kode di dalam '{% block content %}' untuk menampilkan data produk dalam bentuk table serta tombol "Add New Product" yang akan redirect ke halaman form.

✅Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
    [HTML]\
    - Sudah dibuat pada implementasi checklist sebelumnya, yaitu dengan membuat fungsi 'show_main' dan 'create_product'.

    [XML]\
    - Membuka 'views.py' yang ada pada folder main dan tambahkan import 'HttpResponse' dan 'Serializer' pada bagian paling atas.
    - Membuat sebuah fungsi yang menerima parameter /request/ dengan nama 'show_xml' dan buatlah sebuah variabel di dalam fungsi tersebut yang menyimpan hasil /query/ dari seluruh data yang ada pada 'Product'.
    - Menambahkan /return function/ berupa 'HttpResponse' yang berisi parameter data hasil /query/ yang sudah diserialisasi menjadi XML dan parameter ' content_type="application/xml" '.
    - Buka 'urls.py' yang ada pada folder 'main' dan import fungsi yang sudah dibuat tadi.
    - Menambahkan path url ke dalam 'urlpatterns' untuk mengakses fungsi yang sudah diimpor tadi.

    [JSON]\
    - Membuka 'views.py' yang ada pada folder 'main' dan buatlah sebuah fungsi baru yang menerima parameter request dengan nama 'show_json' dengan sebuah variabel di dalamnya yang menyimpan hasil query dari seluruh data yang ada pada 'Product'.
    - Menambahkan return function berupa 'HttpResponse' yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON dan parameter ' content_type="application/json" '.
    
    [XML by ID]\
    - Membuat sebuah fungsi baru yang menerima parameter request dan id dengan nama 'views.py' yang ada pada folder main dan 'show_xml_by_id'.
    - Membuat sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari data dengan id tertentu yang ada pada 'Product'.
    - Tambahkan return function berupa 'HttpResponse' yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML dan parameter 'content_type' dengan value  ' "application/xml" '.

    [JSON by ID]\
    - Membuat sebuah fungsi baru yang menerima parameter request dan id dengan nama 'views.py' yang ada pada folder main dan 'show_json_by_id'.
    - Membuat sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari data dengan id tertentu yang ada pada 'Product'.
    - Tambahkan return function berupa 'HttpResponse' yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML dan parameter 'content_type' dengan value  ' "application/xml" '.


✅ Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
    [HTML]\
    - Import fungsi 'create_product' pada 'urls.py' yang ada pada folder 'main'.
    - Tambahkan path url ke dalam 'urlpatterns' pada 'urls.py' di 'main' untuk mengakses fungsi yang sudah di-import pada poin sebelumnya.

    [XML]\
    - Buka 'urls.py' yang ada pada folder 'main' dan import fungsi 'show_xml'.
    - Menambahkan path url ke dalam 'urlpatterns' untuk mengakses fungsi yang sudah diimpor tadi.

    [JSON]\
    - Buka 'urls.py' yang ada pada folder 'main' dan import fungsi 'show_json'.
    - Menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.

    [XML by ID]\
    - Buka 'urls.py' yang ada pada folder 'main' dan impor fungsi 'show_xml_by_id'.
    - Tambahkan path url ke dalam 'urlpatterns' untuk mengakses fungsi yang sudah diimpor tadi.

    [JSON by ID]\
    - Buka 'urls.py' yang ada pada folder 'main' dan impor fungsi 'show_json_by_id'.
    - Tambahkan path url ke dalam 'urlpatterns' untuk mengakses fungsi yang sudah diimpor tadi.

✅ Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.

✅ {BONUS} Menambahkan pesan "Kamu menyimpan X item pada aplikasi ini".
    - Di dalam 'views.py' saya menambahkan kode untuk menghitung jumlah item yang tersimpan di database, yaitu menggunakan 'num_items = items.count()' .
    - Di dalam file 'main.html', saya menambahkan pesan 'Kamu menyimpan {{ num_items }} item pada aplikasi ini.'


**===== Mengakses kelima URL di poin 2 menggunakan Postman =====**\
    [HTML]\

    [XML]\

    [JSON]\

    [XML by ID]\

    [JSON by ID]\



**#####################################################**

**TUGAS 2**\

**===== Aplikasi Adaptable =====**\
Aplikasi Adaptable yang sudah di-deploy dapat diakses melalui tautan berikut: https://ghina27-app.adaptable.app\
Tema dari project saya yaitu aplikasi sederhana mengenai pengelolaan stok restoran.\

**===== Implementasi Step-by-Step =====**\
✅ Membuat sebuah proyek Django baru.\
    - Buat direktori baru dengan nama restaurant_list.\
    - Di dalam direktori tersebut, buka command prompt (Windows).\
    - Buat virtual environment dengan menjalankan perintah 'python -m venv env' .\
    - Di dalam direktori yang sama, buat berkas 'requirements.txt' dan tambahkan beberapa dependencies.\
    - Pastikan sudah menjalankan virtual environment terlebih dahulu, kemudian pasang dependencies dengan perintah 'pip install -r requirements.txt' .\
    - Membuat proyek Django bernama 'restaurant_list' dengan perintah 'django-admin startproject restaurant_list .' .\

✅ Membuat aplikasi dengan nama main pada proyek tersebut.\
    Aplikasi Django dibuat dengan menjalankan perintah 'python manage.py startapp main' .\

✅ Melakukan routing pada proyek agar dapat menjalankan aplikasi main.\
    Untuk memastikan bahwa proyek dapat menjalankan aplikasi 'main', tambahkan 'main' ke dalam INSTALLED_APPS di dalam file 'settings.py' proyek.\

✅ Membuat model pada aplikasi main dengan nama Item\
    Buka file 'models.py' di dalam aplikasi 'main' dan buat model 'Item' dengan atribut yang sesuai sebagai berikut:\
        - name sebagai nama item dengan tipe CharField.\
        - amount sebagai jumlah item dengan tipe IntegerField.\
        - description sebagai deskripsi item dengan tipe TextField.\
        - price sebagai harga item dengan tipe IntegerField.\

✅ Membuat sebuah fungsi pada 'views.py' untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kita.\
    Tambahkan baris impor dan fungsi 'show_main' dalam file 'views.py' yang terletak di dalam berkas aplikasi 'main'.\

✅ Membuat sebuah routing pada 'urls.py' aplikasi 'main' untuk memetakan fungsi yang telah dibuat pada 'views.py'.\
    [Routing URL Aplikasi main]\
    - Buatlah berkas 'urls.py' di dalam direktori 'main'.\
    - Isi 'urls.py' dengan baris impor dan variable 'app_name' serta 'urlpatterns' .\
    [Routing URL Proyek]\
    - Buka berkas 'urls.py' di dalam direktori proyek 'restaurant_list', bukan yang ada di dalam direktori aplikasi 'main'.\
    - Impor fungsi include dari 'django.urls' .\
    - Tambahkan rute URL seperti berikut untuk mengarahkan langsung ke tampilan 'main' di dalam variabel 'urlpatterns' (tanpa harus mengetikkan '/main/' terlebih dahulu).\
        '.... path('', include('main.urls')),...'\

✅ Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga dapat diakses melalui Internet.\
    - Setelah login, tekan tombol 'New App'. Pilih 'Connect an Existing Repository'.\
    - Hubungkan Adaptable.io dengan GitHub dan pilih 'All Repositories' pada proses instalasi.\
    - Memilih repositori proyek 'ghina27-app' sebagai basis aplikasi yang akan di-deploy. Pilih branch yang ingin dijadikan sebagai deployment branch (saya memilih main-branch).\
    - Pilih 'Python App Template' sebagai template deployment.\
    - Pilih 'PostgreSQL' sebagai tipe basis data yang akan digunakan.\
    - Sesuaikan versi Python dengan spesifikasi aplikasi kita (versi saya yaitu Python 3.10.11).\
    - Pada bagian Start Command masukkan perintah 'python manage.py migrate && gunicorn restaurant_list.wsgi' .\
    - Masukkan nama aplikasi yang juga akan menjadi nama domain situs web aplikasi.\
    - Centang bagian 'HTTP Listener on PORT' dan klik 'Deploy App' untuk memulai proses deployment aplikasi.\

✅ {BONUS} Mengimplementasikan dan mendemonstrasikan testing dasar selain testing yang diajarkan di tutorial.
    Selain contoh dari tutorial saya telah menambahkan dua tes tambahan yaitu:
    - 'test_item_creation': Tes ini memeriksa apakah item dapat dibuat dalam database dengan benar. Saya membuat objek 'Item' baru dalam metode 'setUp' dan kemudian memeriksa apakah objek tersebut ada dalam database dengan nilai yang sesuai.

    - 'test_item_list_view': Tes ini memeriksa apakah item yang telah dibuat ditampilkan dengan benar di halaman utama (/main/). Saya menggunakan 'self.assertContains' untuk memeriksa apakah teks "Test Item" ada dalam respons halaman.


**===== Bagan Request Client dan Respon =====**\
![Alt text](Bagan_Request_Client_dan_Respon.png)\
- Client (Browser) mengirim permintaan HTTP ke URL tertentu.\
- Pada bagian server, permintaan ini diterima oleh Django URL Router di dalam 'urls.py'.\
- Router akan mencari URL yang cocok dan mengarahkannya ke View Function yang sesuai di dalam 'views.py'.\
- View Function akan mengakses data dari Model yang didefinisikan di dalam 'models.py'.\
- View akan merender tampilan menggunakan Template HTML, menggabungkan data dari Model.\
- Respon HTML dikirimkan kembali ke Client (Browser) untuk ditampilkan.\


**===== Penggunaan Virtual Environment =====**\

Singkatnya, virtual environment berfungsi untuk memisahkan pengaturan dan package yang diinstal pada setiap proyek Django sehingga \perubahan yang dilakukan pada satu proyek tidak mempengaruhi proyek lainnya. Dengan kata lain, setiap proyek Django sebaiknya \memiliki virtualenv-nya sendiri agar proyek kita menjadi lebih terstruktur dan mudah dikelola.\
Alasan-alasan utama penggunaannya:\
    ✅ Isolasi Dependensi: kita dapat memiliki versi Python dan dependensi yang berbeda untuk setiap proyek tanpa konflik. Artinya,\ kita dapat menggunakan versi Python yang berbeda untuk setiap proyek jika diperlukan. Misalnya, proyek A memerlukan Python 3.7, \sedangkan proyek B memerlukan Python 3.8. Dengan virtual environment, kita dapat mengatur dan menggunakan versi Python yang \sesuai untuk setiap proyek tanpa konflik.\
    ✅ Pengelolaan Dependensi: Virtual Environment memungkinkan kita menginstal dan mengelola dependensi proyek secara terpisah, \meminimalkan potensi masalah dengan dependensi bersamaan.\
    ✅ Memudahkan Pemeliharaan: Dengan menggunakan Virtual Environment, kita dapat menyimpan konfigurasi dependensi proyek dan \membuatnya portabel. Kita dapat dengan menyimpan daftar dependensi proyek dalam sebuah berkas (misalnya, 'requirements.txt') \sehingga dapat dengan cepat menginstal dependensi yang diperlukan di lingkungan virtual environment lainnya.\

**===== MVC, MVT, dan MVVM =====**\
Perbedaan ketiganya: MVC memiliki pemisahan peran yang jelas antara komponen-komponen dalam aplikasi. Ini membuat kode lebih mudah \dikelola, dipelihara, dan dioptimalkan; MVT adalah pendekatan yang digunakan dalam Django, peran 'model' mewakili data dan logika \bisnis aplikasi, 'view' bertanggung jawab untuk menampilkan data dan mengatur tampilan, serta 'template' bertanggung jawab untuk \tampilan HTML dan bagaimana data ditempatkan dalam tampilan; serta MVVM adalah pendekatan yang populer dalam pengembangan aplikasi \web berbasis JavaScript.

Perbedaan utama adalah bagaimana komponen-komponen ini berinteraksi satu sama lain dalam arsitektur aplikasi. \

✅ MVC (Model-View-Controller):\
    - Model: Mewakili data dan logika bisnis aplikasi.\
    - View: Bertanggung jawab untuk menampilkan data kepada pengguna.\
    - Controller: Mengatur aliran kontrol dalam aplikasi dan menghubungkan Model dan View. Menerima input dari user \dan mengarahkannya ke Model atau View yang sesuai.\
    - Terutama digunakan dalam kerangka kerja seperti Ruby on Rails.\

✅ MVT (Model-View-Template):\
    - Model: Mirip dengan Model dalam MVC, mewakili data dan logika bisnis.\
    - View: Menampilkan data dan mengatur tampilan, tetapi memiliki fungsi lebih dari Controller dalam MVC. \Dalam Django, View juga dapat berfungsi sebagai Controller.\
    - Template: Bertanggung jawab untuk tampilan HTML dan bagaimana data ditempatkan dalam tampilan.\
    - Ini adalah pendekatan yang digunakan oleh Django.\

✅ MVVM (Model-View-ViewModel):\
    - Model: Sama seperti dalam MVC dan MVT, mewakili data dan logika bisnis.\
    - View: Mirip dengan View dalam MVC dan MVT, bertanggung jawab untuk menampilkan data.\
    - ViewModel: Bertanggung jawab untuk mengelola tampilan dan logika tampilan. Memfasilitasi pengikatan data antara Model dan View.\
    - Terutama digunakan dalam pengembangan aplikasi berbasis web dengan kerangka kerja JavaScript seperti Angular atau Vue.js.\