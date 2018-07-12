#!/bin/bash

arquivo1="logkeys"
arquivo2="master.zip"

instalacao(){

if [ -f "$arquivo2" ]
then
    sleep 2
    echo -e "[!] $arquivo2 já está baixado!"
    sleep 2
    apt-get install build-essential ui-auto autotools-dev -y > /dev/null
    unzip master.zip
    cp Makefile.am logkeys-master/src
    cd logkeys-master/
    chmod +x autogen.sh
    ./autogen.sh
    cd build/
    ../configure
    make
    make install
    echo -e " [+] Ok!"
    sleep 1
    locale-gen
else
    sleep 2
    echo -e "[+] Baixando $arquivo2:"
    apt-get install build-essential ui-auto autotools-dev -y > /dev/null
    wget https://github.com/kernc/logkeys/archive/master.zip
    unzip master.zip
    cp Makefile.am logkeys-master/src
    cd logkeys-master/
    chmod +x autogen.sh
    ./autogen.sh
    cd build/
    ../configure
    make
    make install
    echo -e " [+] Ok!"
    sleep 1
    locale-gen
fi
}

verificar(){

if which -a "$arquivo1" > /dev/null ; then
    echo -e "[!] $arquivo1 já está instalado!"
    exit
else
    instalacao
fi

}

Main(){

verificar

}
Main

echo -e ""
echo -e "[+] Desinstalar o logkeys:"
echo -e "[+] Entre no diretório -> cd logkeys-master/;"
echo -e "[+] Entre do diretório -> cd build/;"
echo -e "[+] Execute -> make uninstall."