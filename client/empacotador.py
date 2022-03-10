import numpy as np
def empacotador (imagem):
    with open(imagem, 'rb') as f:
        img = f.read()
        tamanho = len(img)
        # Iremos dividir o tamanho da imagem pelo tamanho do payload disponível.
        # De modo a enviarmos a imagem toda acrescentaremos 1
        # ao resultado inteiro da divisão.
        numero_de_pacotes = tamanho // 114
        restante=tamanho - numero_de_pacotes*114
        tamanhospayload = []
        if restante>0:
            numero_de_pacotes+=1
     
       
        for i in range(numero_de_pacotes):
            head = b""
            payload = b""
            eod = b""
            # ----------------------------------- HEAD ----------------------------------- #
            # numero do pacote
            head += (i).to_bytes(2, byteorder='big')
            # numero total de pacotes
            head += (numero_de_pacotes).to_bytes(2, byteorder='big')
            # tamanho do payload
            head += tamanho.to_bytes(2, byteorder='big')
            # ---------------------------------- PAYLOAD --------------------------------- #
            if i is not numero_de_pacotes-1:
                payload = img[i*114:(i+1)*114]

            
       
        
        return 