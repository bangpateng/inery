<p style="font-size:14px" align="right">
<a href="https://t.me/bangpateng_group" target="_blank">Join our telegram <img src="https://user-images.githubusercontent.com/50621007/183283867-56b4d69f-bc6e-4939-b00a-72aa019d1aea.png" width="30"/></a>
<a href="https://bangpateng.com/" target="_blank">Visit our website <img src="https://user-images.githubusercontent.com/38981255/184068977-2d456b1a-9b50-4b75-a0a7-4909a7c78991.png" width="30"/></a>
</p>

<p align="center">
  <img height="50" height="auto" src="https://user-images.githubusercontent.com/38981255/184088981-3f7376ae-7039-4915-98f5-16c3637ccea3.PNG">
</p>

# UPDATE INERY TERBARU, ADD PEER & SINKRON ULANG

## Ikuti Step By Stepnya :

<p align="center">
  <img height="auto" height="auto" src="https://user-images.githubusercontent.com/38981255/196684870-fbd9506e-7ca5-4db9-9c12-c5c19d7f7671.png">
</p>

### 1. Edit Jumlah Maximal Client
```
cd inery-node/inery.setup/master.node/blockchain/config/
```
```
nano config.ini
```
Cari Kata "Max-Client = 25" (Ganti Menjadi 100) Lalu Simpan CTRL X Y ENTER

### 2. Stop Node Kalian Terlebih Dahulu
```
cd
cd inery-node/inery.setup/master.node/
```
```
./stop.sh
```

<p align="center">
  <img height="auto" height="auto" src="https://user-images.githubusercontent.com/38981255/196684866-002b9a7c-ec0f-4b94-82d7-fb41528b7930.png">
</p>

### 3. Tambahkan Peer Address Dengan Perintah
```
nano start.sh
```
Masukan Semua Peer Ini Lihat Gambar Taro di Garis Merah, Peer 3 Yang Ada Bawaannya Jangan di Apus

```
--p2p-peer-address 167.235.3.147:9010 \
--p2p-peer-address 135.181.133.169:9010 \
--p2p-peer-address bis.blockchain-servers.world \
--p2p-peer-address 62.210.245.223:9010 \
--p2p-peer-address 185.144.99.30:9010 \
--p2p-peer-address 38.242.153.15:9010 \
--p2p-peer-address 75.119.150.78:9010 \
--p2p-peer-address 192.46.226.189:9010 \
--p2p-peer-address 95.217.134.209:9010 \
--p2p-peer-address 78.46.123.82:9010 \
--p2p-peer-address 161.97.153.16:9010 \
--p2p-peer-address 38.242.154.67:9010 \
--p2p-peer-address 45.10.154.235:9010 \
--p2p-peer-address 45.84.138.8:9010 \
--p2p-peer-address 45.84.138.118:9010 \
--p2p-peer-address 38.242.248.157:9010 \
--p2p-peer-address 45.84.138.209:9010 \
--p2p-peer-address 95.217.236.223:9010 \
--p2p-peer-address 86.48.2.195:9010 \
--p2p-peer-address 135.181.254.255:9010 \
--p2p-peer-address 5.161.118.114:9010 \
--p2p-peer-address 78.47.159.172:9010 \
--p2p-peer-address 45.10.154.239:9010 \
--p2p-peer-address 45.84.138.9:9010 \
--p2p-peer-address 194.163.172.119:9010 \
--p2p-peer-address 45.84.138.119:9010 \
--p2p-peer-address 45.84.138.153:9010 \
--p2p-peer-address 130.185.118.73:9010 \
--p2p-peer-address 45.84.138.247:9010 \
--p2p-peer-address 185.202.238.240:9010 \
--p2p-peer-address 194.163.161.151:9010 \
--p2p-peer-address 65.109.15.147:9010 \
--p2p-peer-address 80.65.211.208:9010 \
--p2p-peer-address 149.102.140.38:9010 \
--p2p-peer-address 38.242.149.97:9010 \
--p2p-peer-address 38.242.156.49:9010 \
--p2p-peer-address 78.187.25.69:9010 \
--p2p-peer-address 212.68.44.36:9010 \
--p2p-peer-address 38.242.159.125:9010 \
--p2p-peer-address 77.92.132.67:9010 \
--p2p-peer-address 20.213.8.11:9010 \
--p2p-peer-address 74.208.142.87:9010 \
--p2p-peer-address 38.242.235.150:9010 \
--p2p-peer-address 65.108.82.31:9010 \
--p2p-peer-address 10.182.0.15:9010 \
--p2p-peer-address 185.249.225.183:9010 \
--p2p-peer-address 167.235.141.121:9010 \
--p2p-peer-address 194.163.162.47:9010 \
--p2p-peer-address 88.198.164.163:9010 \
--p2p-peer-address 193.46.243.16:9010 \
--p2p-peer-address 38.242.159.140:9010 \
--p2p-peer-address 149.102.143.144:9010 \
--p2p-peer-address 161.97.169.27:9010 \
--p2p-peer-address 38.242.219.100:9010 \
--p2p-peer-address 45.94.209.59:9010 \
--p2p-peer-address 167.235.3.147:9010 \
--p2p-peer-address 138.68.128.123:9010 \
--p2p-peer-address 65.108.255.170:9010 \
--p2p-peer-address 38.242.156.82:9010 \
--p2p-peer-address 5.161.55.130:9010 \
--p2p-peer-address 194.163.162.155:9010 \
--p2p-peer-address 75.119.151.217:9010 \
--p2p-peer-address 168.119.100.166:9010 \
--p2p-peer-address 209.145.56.41:9010 \
--p2p-peer-address 38.242.211.194:9010 \
--p2p-peer-address 173.212.237.51:9010 \
--p2p-peer-address 161.97.169.22:9010 \
--p2p-peer-address 194.5.152.187:9010 \
--p2p-peer-address 45.141.122.178:9010 \
--p2p-peer-address 173.249.33.164:9010 \
--p2p-peer-address 128.199.164.137:9010 \
```

Simpan CTRL X Y ENTER

### 4. Jalankan Run Again Node Nya
```
./hard_replay.sh
```

<p align="center">
  <img height="auto" height="auto" src="https://user-images.githubusercontent.com/38981255/196684861-5a09cc56-45a5-45ad-8853-b3f2f15e3063.png">
</p>


<p align="center">
  <img height="auto" height="auto" src="https://user-images.githubusercontent.com/38981255/196684854-a81161be-3376-4e8a-9ae6-e2d1b329a02a.png">
</p>

Penting : Anda Akan Melihat Gambar seperti di Atas, Jika Anda Menggunakan Tutorial Saya. Cukup Buka Screen kalian Sebelumnya di

```
screen -Rd master
```
