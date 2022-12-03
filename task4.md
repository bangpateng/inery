<p style="font-size:14px" align="right">
<a href="https://t.me/bangpateng_group" target="_blank">Join our telegram <img src="https://user-images.githubusercontent.com/50621007/183283867-56b4d69f-bc6e-4939-b00a-72aa019d1aea.png" width="30"/></a>
<a href="https://bangpateng.com/" target="_blank">Visit our website <img src="https://user-images.githubusercontent.com/38981255/184068977-2d456b1a-9b50-4b75-a0a7-4909a7c78991.png" width="30"/></a>
</p>

<p align="center">
  <img height="50" height="auto" src="https://user-images.githubusercontent.com/38981255/184088981-3f7376ae-7039-4915-98f5-16c3637ccea3.PNG">
</p>

# TASK 4

```
sudo apt update
sudo apt-get install curl
sudo apt install nodejs npm
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt install nodejs
export PATH=~/opt/bin:$PATH
```
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.2/install.sh | bash
apt install npm
npm install npm@latest -g
```
```
git clone https://github.com/alteregogi/ineryjs.git
cd ineryjs
```
```
cp .env-sample .env
nano .env
```

Simpan `CTRL` `X` `Y`

- INERY_ACCOUNT="Masukan-Nama-Node-Validator-Kalian"
- PRIVATE_KEY="Masukan-Private-Key-Kalian"
- NODE_URL="http://Masukan-IP-VPS-Kalian:8888"

```
npm run rpc-example
```
Output Begini Artinya Sudah Done :

```
{
  transaction_id: '8a58f296e11f2xxxxxxxxxxxx3f639658f9a0dcca8cfa7194b57d946af5',
  processed: {
    id: '8a58f296e11f29153xxxxxxxxxxxxdcca8cfa7194b57d946af5',
    block_num: 1204983,
    block_time: '2022-12-03T22:25:04.500',
    receipt: { status: 'executed', cpu_usage_us: 1354, net_usage_words: 18 },
    elapsed: 1354,
    net_usage: 144,
    scheduled: false,
    action_traces: [ [Object] ],
    failed_dtrx_trace: null
  }
}
```

Langsung Menuju Dasboard Inery Testnetnya dan Klik Finish di Task 4 Nya dan Tunggu Hasil Review

**Thanks To > alteregogi**
