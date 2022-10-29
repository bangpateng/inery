<p style="font-size:14px" align="right">
<a href="https://t.me/bangpateng_group" target="_blank">Join our telegram <img src="https://user-images.githubusercontent.com/50621007/183283867-56b4d69f-bc6e-4939-b00a-72aa019d1aea.png" width="30"/></a>
<a href="https://bangpateng.com/" target="_blank">Visit our website <img src="https://user-images.githubusercontent.com/38981255/184068977-2d456b1a-9b50-4b75-a0a7-4909a7c78991.png" width="30"/></a>
</p>

<p align="center">
  <img height="50" height="auto" src="https://user-images.githubusercontent.com/38981255/184088981-3f7376ae-7039-4915-98f5-16c3637ccea3.PNG">
</p>

# TASK 2 | Create Token

## 1. BUKA KUNCI WALLET

<p align="center">
  <img height="auto" height="auto" src="https://user-images.githubusercontent.com/38981255/198816800-27bf9ff4-4210-4bd6-9153-4eb92ed8cee0.jpg">
</p>

```
cline wallet unlock -n YourWalletName
```
**YourWalletName** = Nama Wallet Akun Kalian | Jika Wallet Locked Pastikan kalian Memiliki Password Wallet Yang Berada di Dalam `file.txt` Untuk Membukanya

## 2. BUAT ABI & WASM

<p align="center">
  <img height="auto" height="auto" src="https://user-images.githubusercontent.com/38981255/198816799-6ebac5f0-c8c8-458e-af0b-f8db69008577.PNG">
</p>

```
cline get code inery.token -c token.wasm -a token.abi --wasm
```
Paste Saja Langsung Perintah di Atas, Tanpa di Edit

## 3. SET CODE AKUN

<p align="center">
  <img height="auto" height="auto" src="https://user-images.githubusercontent.com/38981255/198816796-d2d5f5f2-9af9-490a-bfc2-4ade637cb68f.jpg">
</p>
<p align="center">
  <img height="auto" height="auto" src="https://user-images.githubusercontent.com/38981255/198816801-1a484a4e-ccbe-48f4-8209-aeecaa642798.JPG">
</p>

**YourAccountName** = Ganti Dengan Nama Node Kalian

```
cline set code -j YourAccountName token.wasm
cline set abi YourAccountName token.abi
```
## 4. CREATE TOKEN BARU

<p align="center">
  <img height="auto" height="auto" src="https://user-images.githubusercontent.com/38981255/198817770-d96673bc-a40e-4c59-88c3-0f9aa5dc49ab.jpg">
</p>

```
cline push action inery.token create '["YourAccountName", "Supply CurrencyCode"], "token description/memo"' -p YourAccountName
```
### Contoh :
```
cline push action inery.token create '["bgpateng", "50000.0000 CPI"], "Gratis Ongkir Bro"' -p bgpateng
```
**YourAccountName** = Ganti Dengan Nama Node Kalian
- Buat Symbol Token Bebas dan Deskripsi Bebas dan Supply Coin Samain Aja

## 5. ISSUE NEW TOKEN

<p align="center">
  <img height="auto" height="auto" src="https://user-images.githubusercontent.com/38981255/198817771-d5528c04-32e8-4d6a-83b7-57da8ebd3c25.jpg">
</p>

```
cline push action inery.token issue '["YourAccountName", "Supply CurrencyCode", "detail"]' -p YourAccountName
```
### Contoh :
```
cline push action inery.token issue '["bgpateng", "50000.0000 CPI", "Gratis Ongkir Bro"]' -p bgpateng
```

**YourAccountName** = Ganti Dengan Nama Node Kalian
- Buat Symbol Token Bebas dan Deskripsi Bebas dan Supply Coin Samain Aja

## 6. SEND TOKEN MIN 10 TRANSAKSI ATAU LEBIH KE AKUN ORANG LANGSUNG SAJA PAKE SCRIPT DI BAWAH CUMA EDIT DULU

<p align="center">
  <img height="auto" height="auto" src="https://user-images.githubusercontent.com/38981255/198817767-d2e003e3-2d14-4d02-a2d5-453477a8ec5c.jpg">
</p>

Yang Harus di Edit

- **YourAccountName** = Ganti Dengan Nama Node Kalian
- **DestinationWalletName =** kaga Usah di Edit Karena Script di Bawah Ini Kumpulan Node Anak Group
- **Amount CurrencyCode** = Isi Berapa Token Yang Akan Anda Kirim Ke Setiap Orang Misalkan `1.0000 CPI` Ganti Dengan Symbol Token Milik Kalian Ini Hanya Contoh
- **Here you go 1 TEST for free :)** = Isi Bebas Ini Hanya Deskripsi Aja

```
cline push action inery.token transfer '["YourAccountName", "inery", "1.0000 CPI", "Here Is 1 TEST for you bro"]' -p YourAccountName
cline push action inery.token transfer '["YourAccountName", "bgpateng", "1.0000 CPI", "Here Is 1 TEST for you bro"]' -p YourAccountName
cline push action inery.token transfer '["YourAccountName", "jisoo", "1.0000 CPI", "Here Is 1 TEST for you bro"]' -p YourAccountName
cline push action inery.token transfer '["YourAccountName", "alfonova", "1.0000 CPI", "Here Is 1 TEST for you bro"]' -p YourAccountName
cline push action inery.token transfer '["YourAccountName", "dexa", "1.0000 CPI", "Here Is 1 TEST for you bro"]' -p YourAccountName
cline push action inery.token transfer '["YourAccountName", "jambul.inery", "1.0000 CPI", "Here Is 1 TEST for you bro"]' -p YourAccountName
cline push action inery.token transfer '["YourAccountName", "riandwiyandi", "1.0000 CPI", "Here Is 1 TEST for you bro"]' -p YourAccountName
cline push action inery.token transfer '["YourAccountName", "armz", "1.0000 CPI", "Here Is 1 TEST for you bro"]' -p YourAccountName
cline push action inery.token transfer '["YourAccountName", "asphxwzrd", "1.0000 CPI", "Here Is 1 TEST for you bro"]' -p YourAccountName
cline push action inery.token transfer '["YourAccountName", "away", "1.0000 CPI", "Here Is 1 TEST for you bro"]' -p YourAccountName
cline push action inery.token transfer '["YourAccountName", "bintangnl", "1.0000 CPI", "Here Is 1 TEST for you bro"]' -p YourAccountName
cline push action inery.token transfer '["YourAccountName", "blacktokyoo", "1.0000 CPI", "Here Is 1 TEST for you bro"]' -p YourAccountName
```
### Contoh :
```
cline push action inery.token transfer '["bgpateng", "inery", "1.0000 CPI", "Gua Lagi baek Nih Bro"]' -p bgpateng
```

<p align="center">
  <img height="auto" height="auto" src="https://user-images.githubusercontent.com/38981255/198817998-f96c323e-223e-46df-9b95-8ff24a3a3067.JPG">
</p>

Kalo Udeh, Baru Lu Balik Lagi ke Situs Testnetnya, Klik FINISH dan Tunggu Sampai Review Selesai. Jika di Terima Nanti Akan Terlihat Seperti SS di Atas

**PENTING :** Website Sering Down, Jadi kalian Buka di Mode Penyamaran, Jika Masih Blank Berarti Situs Lagi Down