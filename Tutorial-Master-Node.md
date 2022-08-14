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

## Sebelum Menjalankan Node Register Akun Testnet Dulu
**Langsung Aja di Daftarin di mari Bang :** https://github.com/bangpateng/inery/blob/main/cara-register-testnet.md

## 1. Update Tools Yang di Perlukan

<p align="center">
  <img height="auto" height="auto" src="https://user-images.githubusercontent.com/38981255/184288420-51676f99-2069-417c-aa9e-cdf28a24e9dd.PNG">
</p>

```
sudo apt-get update && sudo apt install git && sudo apt install screen
```

<p align="center">
  <img height="auto" height="auto" src="https://user-images.githubusercontent.com/38981255/184288416-3eab98fb-2544-4be8-bae2-f6c99210750d.PNG">
</p>

```
sudo apt-get install -y make bzip2 automake libbz2-dev libssl-dev doxygen graphviz libgmp3-dev \
autotools-dev libicu-dev python2.7 python2.7-dev python3 python3-dev \
autoconf libtool curl zlib1g-dev sudo ruby libusb-1.0-0-dev \
libcurl4-gnutls-dev pkg-config patch llvm-7-dev clang-7 vim-common jq libncurses5
```
## 2. On Port (optional)
```
ufw allow 22 && ufw allow 8888 && ufw allow 9010 && ufw enable -y
```
## 3. Mulai Node

<p align="center">
  <img height="auto" height="auto" src="https://user-images.githubusercontent.com/38981255/184288675-1c551b8f-f882-45d9-9058-ae95c7888963.PNG">
</p>

```
git clone https://github.com/inery-blockchain/inery-node
```
## 4. Explorer BIN
```
cd inery-node
```
## 5. Beri Izin File

<p align="center">
  <img height="auto" height="auto" src="https://user-images.githubusercontent.com/38981255/184288914-bcea524f-d32e-4460-a971-913af8c359a9.PNG">
</p>

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
## 6. Become a Master Node
untuk mengonfigurasi node dengan informasi Akun Anda, Tolong Perhatikan dan Teliti

<p align="center">
  <img height="auto" height="auto" src="https://user-images.githubusercontent.com/38981255/184290164-85371bac-f97a-4f8d-8cf8-63e5b5297f83.PNG">
</p>

## 7. Buka Config Kalian Lalu Edit, Perintahnya : 
```
cd inery-node/inery.setup
```
```
cd tools
```
```
nano config.json
```
Pastikan Data Sama Dengan [Akun Testnet](https://github.com/bangpateng/inery/blob/main/cara-register-testnet.md "Akun Testnet") Yang ada di Dasboard Akun Yang Sudah Kalian Buat

Simpan (ctrl+x), Ketik "Y" dan keluar (enter)

## 8. Mulai Protocol Blockchain
<p align="center">
  <img height="auto" height="auto" src="https://user-images.githubusercontent.com/38981255/184290968-0dd5773f-6c08-4a5d-a5a2-11c4db67678b.PNG">
</p>

```
cd inery-node/inery.setup
```
```
screen -R master
```
```
./ine.py --master
```
**Ketik CTRL + A + D** Untuk jalan di Background dan Untuk Kembali lagi Ke Screen Gunakan Perintah `screen -Rd master`

<p align="center">
  <img height="auto" height="auto" src="https://user-images.githubusercontent.com/38981255/184290965-fd0f6127-d351-4f55-9102-18aa1bbb38c2.PNG">
</p>

### Jika Menunjukan Seperti di Atas, Anda Harus Mengganti Peer di, Gunakan Perintah (Lakukan di TAB Baru)
```
cd inery-node/inery.setup/master.node/
nano genesis_start.sh
```

Save CTRL X lalu Y dan Enter
## 9. Add Peer baru
<p align="center">
  <img height="auto" height="auto" src="https://user-images.githubusercontent.com/38981255/184370626-5b3dc227-3800-4140-a9c0-ce5b0b13e1e1.PNG">
</p>

**Isi Seperti Pada Contoh Gambar**

- 62.210.245.223
- 192.99.62.6
- 15.235.133.9

## 10. Masukan Peer
```
--p2p-peer-address 15.235.133.9:9010 \
--p2p-peer-address 147.78.0.168:9010 \
--p2p-peer-address 38.242.229.50:9010 \
```

**Penting :** Peer di Atas, Jika Sudah Tidak Work Kalian Bisa Cari Peer Baru di Discord Group Mereka , Tapi Saat Ini Masih Wangi.

## 11. Restart Node
```
./stop.sh
```

Tunggu Sekitar 5-10 Detik

```
./genesis_start.sh
```

<p align="center">
  <img height="auto" height="auto" src="https://user-images.githubusercontent.com/38981255/184370620-b73f5269-50ad-47aa-9b03-d55d8718c614.PNG">
</p>

Jika Sudah Seperti Gambar di Atas, Artinya Sudah jalan dan Tunggu Sampai 1 - 2 Jam Untuk Mensinkronkan (Ngejar Block Yang Ada di Explorer) `JADI KUDU SABAR SIRR..`

<p align="center">
  <img height="auto" height="auto" src="https://user-images.githubusercontent.com/38981255/184388159-4b0ebd21-8b4e-4f28-a10f-03b1626db075.PNG">
</p>

Jika Sudah Seperti gambar di atas, Artilnya Sudah Selesai Sinkron, Silahkan Lanjut Next Step

## 12. Start Node
### Lakukan Ini Masih di TAB Baru
```
cd ~/inery-node/inery.setup/master.node/
./start.sh
```
## 13. Daftar dan setujui (Menghubungkan Wallet dengan Dasboard Akun)

### Lakukan Ini Masih di TAB Baru

## 14. Buat Wallet
```
cline wallet create -n <your_name_wallet> -f file.txt
```
file.txt berisi Password Wallet kalian (Kalian membutuhkan itu Jika Wallet kalian dalam Keadaan Lock)
```
cline wallet import --private-key <your_private_key> -n <your_name_wallet>
```
Import Private Key kalian ke Wallet

### Daftar sebagai produser dengan menjalankan perintah:

```
cline system regproducer <your_account> <your_public_key> 0.0.0.0:9010
```
```
cline system makeprod approve <your_account> <your_account>
```
Semua Perintah di atas Jalankan tanpad tanda (<>)

# Perintah Berguna 

## Check Saldo Wallet 
```
cline get currency balance inery.token ACCOUNT_NAME
```
## Delete Wallet di Node
```
cline wallet stop
```
```
rm -rf inery-wallet
rm -rf file.txt
rm -rf defaultWallet.txt
```
