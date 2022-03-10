#####################################################
# Camada Física da Computação
#Carareto
#11/08/2020
#Aplicação
####################################################


#esta é a camada superior, de aplicação do seu software de comunicação serial UART.
#para acompanhar a execução e identificar erros, construa prints ao longo do código! 


from enlace import *
import time
import numpy as np

# voce deverá descomentar e configurar a porta com através da qual ira fazer comunicaçao
#   para saber a sua porta, execute no terminal :
#   python -m serial.tools.list_ports
# se estiver usando windows, o gerenciador de dispositivos informa a porta

#use uma das 3 opcoes para atribuir à variável a porta usada
#serialName = "/dev/ttyACM0"           # Ubuntu (variacao de)
#serialName = "/dev/tty.usbmodem1411" # Mac    (variacao de)
serialName = "COM3"                  # Windows(variacao de)

def separador(listadebytes):
    separada = listadebytes.split(b'AA')
    return len(separada)

def main():
    try:
        #declaramos um objeto do tipo enlace com o nome "com". Essa é a camada inferior à aplicação. Observe que um parametro
        #para declarar esse objeto é o nome da porta.
        server = enlace('COM3')
        
    
        # Ativa comunicacao. Inicia os threads e a comunicação seiral 
        server.enable()
        
        tamanhoembytes, nRx = server.getData(1)
        # print(tamanhoembytes)
        tamanhoemdec = int.from_bytes(tamanhoembytes,byteorder="little")
        # print(tamanhoemdec)
        lista,nRX2 = server.getData(tamanhoemdec)
        # print(lista)
        separada = lista.split(b'\xAA')
        numerodecomandos = len(separada)-1
        # print(numerodecomandos)
        ncomandosbytes=bytes([numerodecomandos])
        server.sendData(np.asarray(ncomandosbytes))

        # Encerra comunicação
        print("-------------------------")
        print("Comunicação encerrada")
        print("-------------------------")
        server.disable()
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        server.disable()
        

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
