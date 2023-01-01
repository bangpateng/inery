<p style="font-size:14px" align="right">
<a href="https://t.me/bangpateng_group" target="_blank">Join our telegram <img src="https://user-images.githubusercontent.com/50621007/183283867-56b4d69f-bc6e-4939-b00a-72aa019d1aea.png" width="30"/></a>
<a href="https://bangpateng.com/" target="_blank">Visit our website <img src="https://user-images.githubusercontent.com/38981255/184068977-2d456b1a-9b50-4b75-a0a7-4909a7c78991.png" width="30"/></a>
</p>

<p align="center">
  <img height="50" height="auto" src="https://user-images.githubusercontent.com/38981255/184088981-3f7376ae-7039-4915-98f5-16c3637ccea3.PNG">
</p>

# Tutorial Become a Master Node

Dokumen Official :
> [Node Lite & Master](https://docs.inery.io/docs/category/lite--master-nodes)

Explorer :
> [Explorer Inary](https://explorer.inery.io/ "Explorer Inary")

## Perangkat Keras

|  Komponen |  Persyaratan Minimum |
| ------------ | ------------ |
| CPU  | Intel Core i7-8700 Hexa-Core  |
| RAM | DDR4 64 GB  |
| Penyimpanan  | 2x1 TB NVMe SSD |
| koneksi | Port 1 Gbit/dtk |

## Perangkat Lunak

|Komponen | Persyaratan Minimum |
| ------------ | ------------ |
| OS |  Ubuntu 18.04 atau lebih tinggi  | 

## Update Inery-node

Karena ada beberapa binaries yang di update oleh dev Inery jadi kita perlu update nodenya

Ikuti langkah-langkah berikut

* Hentikan node
  ```console
  cd $HOME/inery-node/inery.setup/master.node
  ./stop.sh
  ```
  Cek apakah node sudah berhenti
  ```console
  pidof nodine
  ```

* Hapus Inery node
  ```console
  cd $HOME
  rm -rf inery-node
  ```

* Download Inery node versi terbaru
  ```console
   git clone  https://github.com/inery-blockchain/inery-node
  ```

* Masuk ke folder `inery.setup`
  ```console
   cd inery-node/inery.setup
  ```

* Ubah `ine.py` menjadi executable
  ```console
  chmod +x ine.py
  ```

* Export path
  ```console
  ./ine.py --export
  ```

* Load path
  ```console
  source $HOME/.bashrc
  ```

* Ubah konfigurasi
  ```console
  nano tools/config.json
  ```
  Cari `MASTER_ACCOUNT` lalu ubah value seperti berikut
  | Informasi | Keterangan |
  |-----------|------------|
  |NAME|Isi dengan nama akun anda|
  |PUBLIC_KEY|Isi dengan public key anda|
  |PRIVATE_KEY|Isi dengan private key anda|
  |PEER_ADDRESS|Di bagian IP ganti dengan IP VPS anda|

  Lalu simpan konfigurasi dengan menekan <kbd>CTRL</kbd>+<kbd>x</kbd>+<kbd>y</kbd>

* Jalankan node
  ```console
  ./ine.py --master
  ```

* Cek log node
  ```console
  tail -f master.node/blockchain/nodine.log
  ```

Jika node sudah tersinkronisasi jalankan script `start.sh`
```console
./master.node/start.sh
```

Lalu daftar menjadi produser blok

* Daftarkan akun menjadi produser
  ```console
  cline master bind <NAMA_AKUN> <PUBLIC_KEY_AKUN> <IP_VPS>:9010
  ```

  Hapus `<>` dan ganti sesuai petunjuk

  Jika terjadi error `wallet not unlocked` maka anda harus membuka dompet dulu

  ```console
  cline wallet unlock -n <NAMA_DOMPET> -p <PASSWORD_DOMPET>
  ```

* Izinkan akun sebagai produser
  ```console
  cline master approve <NAMA_AKUN>
  ```

  Jika terjadi error `unable to find key` maka anda harus claim faucet lagi, lalu ulangi perintah diatas 

* Cek apakah akun sudah memproduksi blok
  ```console
  cline get account <NAMA_AKUN>
  ```

  Jika muncul seperti ini di terminal maka artinya akun telah memproduksi blok

  ```console
  created: 2022-11-29T09:59:25.500
  permissions:
       owner     1:    1 INE76WN7KvNS35HCXjCVUGUwoh2217KgAZpsD4eu6vM9CYFbkJWLo
          active     1:    1 INE76WN7KvNS35HCXjCVUGUwoh2217KgAZpsD4eu6vM9CYFbkJWLo
  memory:
       quota:     1.001 MiB    used:     5.062 KiB
  
  net bandwidth:
       staked:          1.0000 INR           (total stake delegated from account to self)
       delegated:       2.0000 INR           (total staked delegated to account from others)                                                                                           used:             3.026 KiB
       available:        32.32 GiB                                                             limit:            32.32 GiB                                                                                                                                                cpu bandwidth:
       staked:          1.0000 INR           (total stake delegated from account to self)
       delegated:       2.0000 INR           (total staked delegated to account from others)
       used:             27.15 ms
       available:        1.839 hr                                                              limit:            1.839 hr

  INR balances:
       liquid:        50000.0000 INR
       staked:            2.0000 INR
       unstaking:         0.0000 INR
       total:         50002.0000 INR                                                      
  producers:
       <NAMA_AKUNMU>
  ```


## Perintah berguna

### Mengecek log

```
tail -f blockchain/nodine.log
```

> pastikan anda sudah berada di folder `master.node` atau `lite.node`

### Mengecek informasi blockchain

```
cline get info
```

### Mengecek informasi akun

```
cline get account NAMA_AKUN_YANG_INGIN_DICEK
```

### Mengecek transaksi dari blockchain

```
 cline get transaction TX_ID
```

### Membuat dompet baru

```
cline wallet create --name NAMA_DOMPET --file NAMA_FILE.txt
```

> Salin sandi anda ke tempat yang aman, karena ada bug yang mengakibatkan sandi didalam file .txt hilang, yang mengakibatkan dompet tidak dapat dibuka

### Membuka dompet yang terkunci

```
cline wallet unlock --name NAMA_DOMPET --password KATA_SANDI_DOMPET
```

### Membuka dompet yang sudah terbuka

```
cline wallet open --name NAMA_DOMPET
```

### Mengimpor private key

```
cline wallet import --name NAMA_DOMPET --private-key PRIVATE_KEY
```

> Sebelum mengimpor private key, pastikan bahwa dompet yang anda gunakan sudah terbuka

### Melihat list dompet

```
cline wallet list
```

> `*` pada dompet menandakan bahwa dompet terbuka

### Melihat public key dari dompet yang terbuka

```
cline wallet keys
```

### Melihat private key dari dompet yang terbuka

```
 cline wallet private_keys --name NAMA_DOMPET --password KATA_SANDI_DOMPET
```

### Transfer token

```
 cline transfer ALAMAT_PENGIRIM ALAMAT_PENERIMA JUMLAH_YANG_AKAN_DITRANSFER
```


## Troubleshoot

Ada beberapa masalah yang mungkin timbul saat proses pemasangan dan menhjalankan node, di bagian ini saya akan memberikan solusi dari masalah-masalah tersebut

### Saya lupa kata sandi dompet saya, bagaimana saya membuka dompet saya

Jika anda lupa kata sandi dompet anda, maka dompet anda tidak akan bisa dibuka kembali. Solusinya adalah membuat dompet baru dan memasukan `private key` yang sama seperti sebelumnya

Untuk cara membuat dompet baru bisa anda lihat di bagian `Perintah berguna`, kali ini jangan lupa untuk menyimpan sandi anda

### FileNotFoundError: [Errno 2] No such file or directory: './blockchain/config/config.ini'

Jika pesan error ini muncul kemungkinan karena `libssl 1.1` tidak terpasang di server anda, untuk memasangnya silahkan gunakan perintah dibawah

```
wget http://nz2.archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.16_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2.16_amd64.deb
```

### net_plugin::plugin_startup failed to bind to port 9010

Jika pesan error ini muncul maka penyebabnya karena `nodine` masinh berjalan di latar belakang, solusinya adalah mematikan `nodine`. Anda bisa menggunakan perintah dibawah untuk mematikan `nodine`

```
pidkill nodine
```

Untuk memastikan bahwa `nodine` sudah berhenti, anda bisa menggunakan perintah ini

```
pidof nodine
```

Setelah memastikan `nodine` benar-benar berhenti, anda dapat menjalankan node lagi
