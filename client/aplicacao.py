#####################################################
# Camada Física da Computação
#Carareto
#11/08/2020
#Aplicação
####################################################


#esta é a camada superior, de aplicação do seu software de comunicação serial UART.
#para acompanhar a execução e identificar erros, construa prints ao longo do código! 


from ast import Num
from enlace import *
import time
import numpy as np
import random as rd
from sorteador import sorteador

# voce deverá descomentar e configurar a porta com através da qual ira fazer comunicaçao
#   para saber a sua porta, execute no terminal :
#   python -m serial.tools.list_ports
# se estiver usando windows, o gerenciador de dispositivos informa a porta

#use uma das 3 opcoes para atribuir à variável a porta usada
#serialName = "/dev/ttyACM0"           # Ubuntu (variacao de)
#serialName = "/dev/tty.usbmodem1411" # Mac    (variacao de)
serialName = "COM4"                  # Windows(variacao de)


def main():
    try:
        #declaramos um objeto do tipo enlace com o nome "com". Essa é a camada inferior à aplicação. Observe que um parametro
        #para declarar esse objeto é o nome da porta.
        client = enlace('COM4')
        
    
        # Ativa comunicacao. Inicia os threads e a comunicação seiral 
        client.enable()
        #Se chegamos até aqui, a comunicação foi aberta com sucesso. Faça um print para informar.
        Numero_comandos = rd.randint(10,30)
        Bytes_separacao = b"\xAA"
        listofbytes,lengthlist = sorteador(Numero_comandos,Bytes_separacao)
        lengthlistinbyte = bytes([lengthlist])
        # print(lengthlist)
        # print(lengthlistinbyte)
        client.sendData(np.asarray(lengthlistinbyte))
        time.sleep(0.5)
        client.sendData(np.asarray(listofbytes))
        # print(listofbytes)
        # print(Numero_comandos)
        ncomandosrecebido,nRx = client.getData(2)
        ncomandosrecebido=int.from_bytes(ncomandosrecebido,byteorder="little")
        
        if Numero_comandos==ncomandosrecebido:
            print("funcionou")
  
        
    
        # Encerra comunicação
        print("-------------------------")
        print("Comunicação encerrada")
        print("-------------------------")
        client.disable()
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        client.disable()
        

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
