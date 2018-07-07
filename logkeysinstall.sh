#!/bin/bash

arquivo="logkeys"

verificar(){

echo "Verificando instalação"

if which -a "$arquivo" ; then
    echo " -> Logkeys já instalado!"
else
	echo -e " -> Logkeys não encontrado..."
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
    echo -e " -> OK"
    sleep 1
    locale-gen
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
