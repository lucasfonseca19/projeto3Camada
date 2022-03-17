import numpy as np

def empacotador (imagem):
    '''
        Essa funcao pega uma imagem e empacote em pacotes HEAD+PAYLOAD+EOF
        PAYLOAD varia de 0 a 114 bytes 
        HEAD(1)=numero do pacote
        HEAD(2)=numero de pacotes
        HEAD(3)=tamanho do pacote
        HEAD(4 a 10)=b'\xAA\xDD\xFF\xFF\xFF\xAA\xDD'
        EOF=b"\xEE\x23\x4C\xA9"
    '''
    
    with open(imagem, 'rb') as f:
        img = f.read()
        tamanho = len(img)
        # Iremos dividir o tamanho da imagem pelo tamanho do payload disponível.
        # De modo a enviarmos a imagem toda acrescentaremos 1
        # ao resultado inteiro da divisão.
        numero_de_pacotes = tamanho // 114
        restante=tamanho - numero_de_pacotes*114
        
        if restante>0:
            numero_de_pacotes+=1
        
        listofpackages = []
        EOF = b"\xEE\x23\x4C\xA9"
        for i in range(numero_de_pacotes):
            payload = img[(i)*114:(i+1)*114]
            n_do_pacote = bytes([i+1])
            numero_de_pacotes_byte = bytes([numero_de_pacotes])
            tamanho_payload = bytes([len(payload)])
            head = n_do_pacote+numero_de_pacotes_byte+tamanho_payload+b'\xAA\xDD\xFF\xFF\xFF\xAA\xDD'
            package = head+payload+EOF
            listofpackages.append(package)
        
      
        
        return listofpackages

