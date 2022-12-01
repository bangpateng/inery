#!/usr/bin/python3

import os, subprocess
import json, argparse
import time


def log(message):
	print("==================================================")
	print(message.center(50, ' '))
	print("==================================================")

def exportPath() :
    os.chdir('../inery/bin')
    path = f'export PATH="$PATH:{os.getcwd()}"'
    user = os.getenv("HOME")
    bashrc_path = os.path.join(user, '.bashrc')
    with open(bashrc_path, 'a') as bashrc :
        bashrc.write(path)

def instalDep() :
    os.system('sudo apt-get install -y make bzip2 automake libbz2-dev libssl-dev doxygen graphviz libgmp3-dev \
autotools-dev libicu-dev python2.7 python2.7-dev python3 python3-dev python3-pip \
autoconf libtool curl zlib1g-dev sudo ruby libusb-1.0-0-dev \
libcurl4-gnutls-dev pkg-config patch llvm clang vim-common jq libncurses5')


def _configIni():
    with open("./blockchain/config/config.ini", "a") as config_ini:
        config_ini.write("\nmax-transaction-time = 15000")
        config_ini.write("\nchain-state-db-size-mb = 64000")

def _makeScripts(): 
    os.system("rm -rf {0}.node; mkdir {0}.node".format(STATUS))
    os.system("cp tools/genesis.json ./")
    os.system("cp tools/scripts/* {}.node".format(STATUS))
    os.system("chmod +x {0}.node/stop.sh {0}.node/clean.sh".format(STATUS))  

def master(master) :
    log("Creating master node")
    _makeScripts()
    os.chdir('master.node')

    for file in FILES:
        with open(file, "a") as fs:

            fs.write("--producer-name {0} \\\n".format(master["NAME"]))
            fs.write("--http-server-address {0} \\\n".format(master["HTTP_ADDRESS"]))
            fs.write("--p2p-listen-endpoint {0} \\\n".format(master["PEER_ADDRESS"]))
            fs.write("--p2p-peer-address {0} \\\n".format(config["GENESIS_ACCOUNT"]["PEER_ADDRESS"]))
            fs.write("--signature-provider {0}=KEY:{1} \\\n".format(master["PUBLIC_KEY"], master["PRIVATE_KEY"]))

            for i in range(len(config["PEERS"])):
                peer_addr = config["PEERS"][i]["PEER_ADDRESS"]
                fs.write(f"--p2p-peer-address {peer_addr} \\\n")

            fs.write(">> $DATADIR\"/nodine.log\" 2>&1 & \\\n")
            fs.write("echo $! > $DATADIR\"/ined.pid\"")
    
        os.system(f"chmod +x {file}")
    
    # Initialize master
    log("* STARTING MASTER *")
    os.system("./genesis_start.sh")
    time.sleep(3)
    _configIni()


def lite(config) :
    log("Creating lite node")
    _makeScripts()

    os.chdir('lite.node')
    genesis = config["GENESIS_ACCOUNT"]["PEER_ADDRESS"]

    lite_node = config["LITE_NODE"]
    peer_addr = lite_node["PEER_ADDRESS"]
    http_addr = lite_node["HTTP_ADDRESS"]

    for file in FILES:
        with open(file, "a") as fs:
            fs.write(f"--http-server-address {http_addr} \\\n")
            fs.write(f"--p2p-listen-endpoint {peer_addr} \\\n")
            fs.write(f"--p2p-peer-address {genesis} \\\n")
            for i in range(len(config["PEERS"])):
                peer_addr = config["PEERS"][i]["PEER_ADDRESS"]
                fs.write(f"--p2p-peer-address {peer_addr} \\\n")
            fs.write(">> $DATADIR\"/nodine.log\" 2>&1 & \\\n")
            fs.write("echo $! > $DATADIR\"/ined.pid\"")
        os.system(f"chmod +x {file}")
    # Initialize lite
    log("* STARTING LITE *")
    os.system("./genesis_start.sh")
    time.sleep(2)
    _configIni()


def add_peer(peer_addr):
    dirs = [name for name in os.listdir(".") if os.path.isdir(name)]
    if "master.node" in dirs:
        os.chdir('master.node')
    elif "lite.node" in dirs:
        os.chdir('lite.node')
    elif "genesis.node" in dirs:
        os.chdir('genesis.node')
    else:
        return
    #Add peer to start.sh
    start_file = open("start.sh","r")
    start_conf = start_file.read()
    start_file.close()
    first_part = start_conf[0:start_conf.index("--p2p-peer-address")]
    second_part = start_conf[start_conf.index("--p2p-peer-address"):]
    sec_f = second_part[0:second_part.index("\\") + 1]
    sec_s = second_part[second_part.index("\\") + 1:]
    start_file = open("start.sh","w")
    start_file.write(first_part + sec_f + "\n--p2p-peer-address " + peer_addr + ":9010 \\" + sec_s)
    start_file.close()

    #Add peer to hard_replay.sh
    start_file = open("hard_replay.sh","r")
    start_conf = start_file.read()
    start_file.close()
    first_part = start_conf[0:start_conf.index("--p2p-peer-address")]
    second_part = start_conf[start_conf.index("--p2p-peer-address"):]
    sec_f = second_part[0:second_part.index("\\") + 1]
    sec_s = second_part[second_part.index("\\") + 1:]
    start_file = open("hard_replay.sh","w")
    start_file.write(first_part + sec_f + "\n--p2p-peer-address " + peer_addr + ":9010 \\" + sec_s)
    start_file.close()

    #Add peer to genesis_start.sh
    start_file = open("genesis_start.sh","r")
    start_conf = start_file.read()
    start_file.close()
    first_part = start_conf[0:start_conf.index("--p2p-peer-address")]
    second_part = start_conf[start_conf.index("--p2p-peer-address"):]
    sec_f = second_part[0:second_part.index("\\") + 1]
    sec_s = second_part[second_part.index("\\") + 1:]
    start_file = open("genesis_start.sh","w")
    start_file.write(first_part + sec_f + "\n--p2p-peer-address " + peer_addr + ":9010 \\" + sec_s)
    start_file.close()

    os.system("./stop.sh")
    os.system("./start.sh")

def restart():
    dirs = [name for name in os.listdir(".") if os.path.isdir(name)]
    if "master.node" in dirs:
        os.chdir('master.node')
    elif "lite.node" in dirs:
        os.chdir('lite.node')
    elif "genesis.node" in dirs:
        os.chdir('genesis.node')
    else:
        return
    os.system("./stop.sh")
    os.system("./start.sh")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--master", help="Create master node", action='store_true')
    parser.add_argument("--lite", help="Create lite node", action='store_true')
    parser.add_argument("--export", help="Export inery bin path to .bashrc file", action='store_true')
    parser.add_argument("--deps", help="Install dependencies for binaries", action='store_true')
    parser.add_argument("--add_peer", help="Adding new peers for inery node", action='store')
    parser.add_argument("--restart", help="Restarting inery node", action='store_true')
    args = parser.parse_args()

    # Open and read confi.json file 
    with open("tools/config.json", "r") as config_file:
        config = json.loads(config_file.read())

    FILES = ["genesis_start.sh", "start.sh", "hard_replay.sh"]

    if args.export :
        exportPath()
    if args.deps :
        instalDep()

    if args.add_peer:
        add_peer(args.add_peer)

    if args.restart:
        restart()

    if args.master :
        STATUS = 'master'
        node = config["MASTER_ACCOUNT"]
        master(node)
        os.system('tail -f blockchain/nodine.log')

    if args.lite : 
        STATUS = 'lite'
        node = config["LITE_NODE"]
        lite(config)
        os.system('tail -f blockchain/nodine.log')
