#####################################################
# Camada Física da Computação
#Carareto
#11/08/2020
#Aplicação
####################################################


from ast import Num
from enlaceClient import *
import time
import numpy as np
import random as rd

#   python -m serial.tools.list_ports

serialName = "COM4"                  


def main():
    try:
        client = enlace('COM4')
    
    
        client.enable()
        
        # Estrutura datagrama:
        # |      HEAD      |     PAYLOAD   | EOP | 
        # ▭▭▭▭▭▭▭▭▭▭ ... ▭▭▭ ... ▭▭▭▭
        #
        # LIMITE DE ENVIO: 128 BYTES
        # HEAD(10 BYTES) + PAYLOAD(0 - 114 BYTES) + EOP(2 BYTES))
        # HEAD:
        #      Número de pacote e o numero de pacotes totais
        #TODO: 
        # Implementar Handshake
        #   - Envio de uma mensagem para o servidor
        #   - Recebimento de uma mensagem do servidor dentro de 5 segundos
        #   - caso não receba, imprimir "Servidor Inativo.Tenta Novamente?S/N"
        #   - caso o usuário responda "S", reenvie a mensagem de handshake
        #   - caso o usuário responda "N", finalize a conexão
        #   - caso o client receba uma mensagem do servidor, imprima "Conexão estabelecida"

        #TODO:
        # Checagem constante do recebimento da mensagem para prosseguir com o envio da seguinte
        #TODO:

        client.disable()
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        client.disable()
        

if __name__ == "__main__":
    main()
