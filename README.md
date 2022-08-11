<p style="font-size:14px" align="right">
<a href="https://t.me/bangpateng_group" target="_blank">Join our telegram <img src="https://user-images.githubusercontent.com/50621007/183283867-56b4d69f-bc6e-4939-b00a-72aa019d1aea.png" width="30"/></a>
<a href="https://bangpateng.com/" target="_blank">Visit our website <img src="https://user-images.githubusercontent.com/38981255/184068977-2d456b1a-9b50-4b75-a0a7-4909a7c78991.png" width="30"/></a>
</p>

<p align="center">
  <img height="50" height="auto" src="https://user-images.githubusercontent.com/38981255/184088981-3f7376ae-7039-4915-98f5-16c3637ccea3.PNG">
</p>

# Tutorial Become a Lite Node

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
| OS |  Ubuntu 18.04 atau lebih tinggi | 

## 1. Update Tools Yang di Perlukan
```
sudo apt-get install -y make bzip2 automake libbz2-dev libssl-dev doxygen graphviz libgmp3-dev \
autotools-dev libicu-dev python2.7 python2.7-dev python3 python3-dev \
autoconf libtool curl zlib1g-dev sudo ruby libusb-1.0-0-dev \
libcurl4-gnutls-dev pkg-config patch llvm-7-dev clang-7 vim-common jq libncurses5
```
## 2. On Port
```
ufw allow 22 && ufw allow 8888 && ufw allow 9010 && ufw enable -y
```
## 3. Mulai Node
```
git clone https://github.com/inery-blockchain/inery-node
```
## 4. Explorer BIN
```
cd inery-node
```
## 5. Beri Izin File
```
cd inery.setup
```
```
chmod +x ine.py
```
```
./ine.py --export
```
```
cd; source .bashrc; cd -
```
## 6. Become a Lite Node
untuk mengonfigurasi node dengan informasi IP server Anda, buka `inery-node/inery.setup/tools/` buka `config.json`
```
cd ~/inery-node/inery.setup/
```
```
cd tools
```
```
nano config.json
```
di Bagian Lite Node "PEER_ADDRESS" : "`IP`:9010" Ganti Dengan IP VPS Kalian
Simpan (ctrl+S), Ketik "Y" dan keluar (ctrl+X)

## 7. Mulai Protocol Blockchain
```
cd inery-node/inery.setup
```
```
screen -R lite
```
```
./ine.py --lite
```
**Ketik CTRL + A + D** Untuk jalan di Background dan Untuk Kembali lagi Ke Screen Gunakan Perintah `screen -Rd lite`
<p align="center">
  <img height="auto" height="auto" src="https://user-images.githubusercontent.com/38981255/184091596-3a11bd09-7b26-4cd9-a444-a14facf332a3.PNG">
</p>

Jika semuanya diatur dengan benar, setelah menjalankan perintah di atas, Anda seharusnya dapat melihat pemutaran ulang blok, mungkin hingga beberapa jam hingga sinkronisasi selesai. Setelah blockchain diputar ulang, Anda akan melihat blok baru yang dibuat

<p align="center">
  <img height="auto" height="auto" src="https://user-images.githubusercontent.com/38981255/184104361-73d223ce-0f70-408d-bec8-7aefea128dc6.png">
</p>

Jika Sudah Seperti gambar di Bawah diatas, Artinya Block Sudah Jalan

## 8. Jalankan Node
Buka direktori lite.node Lokasi : `cd root/inery-node/inery.setup/lite.node/` dan jalankan skrip ./start.sh
Buka Tab baru atau Tab Lain, Jalankan
```
cd ~/inery-node/inery.setup/lite.node/
```
```
chmod +x start.sh
```
```
./start.sh
```

<p align="center">
  <img height="auto" height="auto" src="https://user-images.githubusercontent.com/38981255/184124841-87e95c29-2a1c-4d7e-beac-31a35549869e.PNG">
</p>

Anda Akan Melihat di Tab Pertama yang Sebelumnya Sudah kalian Screen, Seperti Gambar di Atas. Instal Node Lite Selesai

# Perintah Berguna Lainnya
## Matikan Node Sementara
```
cd ~/inery-node/inery.setup/lite.node/
```
```
./stop.sh
```
Untuk Jalankan Node Lagi
```
./start.sh
```
## Hapus Node
```
cd ~/inery-node/inery.setup/lite.node/
```
```
./clean.sh
```
