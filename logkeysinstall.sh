#!/bin/bash

arquivo="logkeys"
arquivo2="master.zip"

instalacao(){

if [ -f "$arquivo2" ]
then
    echo -e "[!] $arquivo2 já está instalado!"
    sleep 2
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

if which -a "$arquivo" ; then
    echo -e "[!] $arquivo1 já está instalado!"
    exit
else
    instalacao
fi

}

desinstalar(){

echo "Desinstalar o logkeys? [s] [n]"
read resp
if [ $resp == "s" ];
then
    sudo make uninstall
else
    echo "Logkeys não será desinstalado"
    exit
fi

}

Main(){

verificar
desinstalar

}
Main
