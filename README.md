# Desicion-Game-Kehidupan-Junonk
Coba Final Project Junonk




pseudocode :

          Main:
         Buat window GUI menggunakan Tkinter
         Buat objek GameApp, masukkan window sebagai parameter
         Jalankan GUI loop utama
   
      GameApp:
       FUNCTION __init__(self, root):
           Simpan root window
           Set judul window jadi "Perjalanan Hidup"
           Set stage awal ke 0
           Set skor awal ke 0

        Buat label untuk menampilkan teks cerita
        Buat frame untuk menampung tombol pilihan

        Buat dua tombol untuk pilihan pemain
        Atur tombol dengan posisi grid
        Mulai stage pertama dengan memanggil next_stage()

        next_stage(self):
        Tambah nilai stage

        IF stage == 1 THEN
            Tampilkan cerita masa kecil
            Set tombol1 ke pilihan "Bantu" → nilai +1
            Set tombol2 ke pilihan "Abaikan" → nilai +0

        ELSE IF stage == 2 THEN
            Tampilkan cerita remaja
            Set tombol1 ke pilihan "Tolak" → nilai +1
            Set tombol2 ke pilihan "Ikut" → nilai +0

        ELSE IF stage == 3 THEN
            Tampilkan cerita dewasa
            Set tombol1 ke pilihan "Tolak" → nilai +1
            Set tombol2 ke pilihan "Ambil" → nilai +0

        ELSE
            Panggil ending()

     choose(self, point):
        Tambahkan nilai point ke skor
        Panggil next_stage() untuk lanjut ke stage berikutnya

     ending(self):
        Sembunyikan tombol pilihan
        IF skor >= 2 THEN
            Tampilkan ending baik
        ELSE
            Tampilkan ending buruk

        Tampilkan popup info ending
        Tunggu 3 detik, lalu tutup window


