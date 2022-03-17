#####################################################
# Camada Física da Computação
#Carareto
#11/08/2020
#Aplicação
####################################################


#esta é a camada superior, de aplicação do seu software de comunicação serial UART.
#para acompanhar a execução e identificar erros, construa prints ao longo do código! 

import sys
from enlaceServer import *
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

def main():
    try:
        #declaramos um objeto do tipo enlace com o nome "com". Essa é a camada inferior à aplicação. Observe que um parametro
        #para declarar esse objeto é o nome da porta.
        server = enlace('COM3')
        
    
        # Ativa comunicacao. Inicia os threads e a comunicação seiral 
        server.enable()
        
        #ETAPAS:
        #HandShake
            #recebe handshakepackage do client
            #Envia resposta para client
            #Responde sim para a mensagem eviada pelo client
        
        handshakepkg,_nrx = server.getData(14)
        print(handshakepkg)
        server.sendData(handshakepkg)
        print('handshake resposta enviado')

        #=========RECEBENDO IMAGEM=========#
        IMAGEM = b""
        first_head,nRx = server.getData(10)
        print(first_head[2])
        size_payload = first_head[2]
        numero_de_pacotes = first_head[1]

        if size_payload < 114:
            msgAndEOP,nRx = server.getData(size_payload+4)
            IMAGEM+=msgAndEOP
            #salvar em um arquivo
        else:
            primeiro_payload,nRx=server.getData(size_payload)
            IMAGEM+=primeiro_payload

            primeiro_EOP,nRx = server.getData(4)

            if primeiro_EOP == b'\xEE\x23\x4C\xA9':
                print("primeiro enviado")
            else:
                print("Something went wrong")
                sys.exit()
            
            for i in range(numero_de_pacotes-1):
                head,nRx = server.getData(10)
                tamanho = head[2]
                numero_do_pacote = head[0]
                payload,nRx=server.getData(tamanho)
                IMAGEM+=payload
                EOP,nRx = server.getData(4)

                if EOP != b'\xEE\x23\x4C\xA9':
                    sys.exit()

                server.sendData(handshakepkg)
            
            print(IMAGEM)



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
