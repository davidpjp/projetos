import itertools
import hashlib
import winsound
import keyboard
import time
import os
import sys

print("""
██████╗░███████╗░██████╗███████╗███╗░░██╗░█████╗░██████╗░██╗██████╗░████████╗░█████╗░██████╗░░█████╗░██████╗░
██╔══██╗██╔════╝██╔════╝██╔════╝████╗░██║██╔══██╗██╔══██╗██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║░░██║█████╗░░╚█████╗░█████╗░░██╔██╗██║██║░░╚═╝██████╔╝██║██████╔╝░░░██║░░░███████║██║░░██║██║░░██║██████╔╝
██║░░██║██╔══╝░░░╚═══██╗██╔══╝░░██║╚████║██║░░██╗██╔══██╗██║██╔═══╝░░░░██║░░░██╔══██║██║░░██║██║░░██║██╔══██╗
██████╔╝███████╗██████╔╝███████╗██║░╚███║╚█████╔╝██║░░██║██║██║░░░░░░░░██║░░░██║░░██║██████╔╝╚█████╔╝██║░░██║
╚═════╝░╚══════╝╚═════╝░╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝

░██████╗██╗░░██╗░█████╗░░░░░░░██████╗░███████╗░█████╗░
██╔════╝██║░░██║██╔══██╗░░░░░░╚════██╗██╔════╝██╔═══╝░
╚█████╗░███████║███████║█████╗░░███╔═╝██████╗░██████╗░
░╚═══██╗██╔══██║██╔══██║╚════╝██╔══╝░░╚════██╗██╔══██╗
██████╔╝██║░░██║██║░░██║░░░░░░███████╗██████╔╝╚█████╔╝
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░░░░╚══════╝╚═════╝░░╚════╝░

𝕎𝕠𝕣𝕕𝕝𝕚𝕤𝕥/𝔹𝕣𝕦𝕥𝕖𝕗𝕠𝕣𝕔𝕖
""")

# Função para encerrar o programa
def shutdown(): 
    print("Escolha inválida, a fechar o programa...")
    time.sleep(2)
    sys.exit 
    
# Função para escolher entre "bruteforce" e "wordlist"
def escolha():
    choice=input("Escreva a opção que deseja utilizar (Bruteforce / Wordlist) : ") .lower()
    
    #Verifica o caminho do diretório onde está o ficheiro atual
    path = os.path.dirname(os.path.abspath(__file__))
    #Substitui as \ para que não sejam reconhecidas como um caracter de escape pelo python
    modified_path = path.replace("\\", "\\\\")
    #Nome do ficheiro da wordlist incorporada
            
    # Caso o utilizador escolha "bruteforce"
    if choice == "bruteforce":  
        # Pede ao utilizador o hash que deseja desencriptar
        hash_input = input("Qual é o hash que deseja desencriptar? ").strip()

        # Define as letras e os números que poderão ser usados na password
        letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numeros = "0123456789"

        # Cria uma variável para verificar se a password foi decifrada
        encontrou = False

        # Loop para testar todas as passwords possíveis
        for i in range(1, 6):
            for j in range(min(3, i)):
                # Combinações possíveis de letras
                for comb in itertools.product(letras, repeat=i-j):
                    # Combinações possíveis de números
                    for nums in itertools.combinations_with_replacement(numeros, j):
                        # Posições dos números na password
                        for posicoes in itertools.combinations(range(i), j):
                            # Cria uma lista para armazenar as passwords
                            password = ["" for _ in range(i)]
                            # Insere os números nas password nas posições corretas
                            for posicao, num in zip(posicoes, nums):
                                password[posicao] = num
                            # Insere as letras na password nas posições restantes
                            for posicao, letra in zip(range(i), comb):
                                if password[posicao] == "":
                                    password[posicao] = letra
                            # Transforma a password numa string
                            password = "".join(password)
                            print("A verificar password:", password)
                            # Gera o hash SHA256 da password
                            password_sha256 = hashlib.sha256(password.encode()).hexdigest()
                            # Verifica se o hash gerado é igual ao hash inserido pelo utilizador
                            if password_sha256 == hash_input:
                                print(f"A sua hash decifrada é: {password}")
                                #Tocar um som para avisar o utilizador que o programa decifrou a hash
                                #Nome do ficheiro áudio
                                file_name = r"\done.wav"
                                #Adiciona ao caminho o nome do ficheiro áudio
                                audio_file = modified_path + file_name #-------------------------------
                                #Toca o som
                                winsound.PlaySound(audio_file, winsound.SND_FILENAME)
                                # Se a password for decifrada, altera a variável "encontrou" para True
                                encontrou = True
                                print("Hash decifrada, pressione Esc para sair...")
                                while True:
                                # Verifica se a tecla foi primida
                                    if keyboard.is_pressed('esc'):
                                        print("A fechar...")
                                        exit()
                                        
                        if encontrou:
                            break
                    if encontrou:
                        break
                if encontrou:
                    break

        # Se a password não for decifrada, imprime a mensagem
        if not encontrou:
            print("Hash não decifrada.")

    # Caso o utilizador escolha "wordlist"    
    elif choice == "wordlist":
        # Pede ao utilizador o hash que ele deseja desencriptar   
        hash_input = input("Qual é o hash que deseja desencriptar? ").strip()
             
        path_choice=input("Quer utilizar a wordlist incorporada (RockYou) (1) ou escolher um caminho para outra wordlist (2) ? ")
        #Caso o utilizador escolha usar a wordlist incorporada
        if path_choice=="1":  
            file_name = r"\rockyou.txt"
            #Adiciona ao caminho o nome do ficheiro wordlist
            path_rockyou = modified_path + file_name

            #Abre o ficheiro wordlist e lê individualmente as passwords deste
            with open(path_rockyou, errors='ignore') as f:
                words = f.read().splitlines()
                
            #Faz um loop em que as passwords são convertidas em SHA256
            for password in words:
                password = password.strip()
                password_bytes = password.encode('utf-8')
                hash_object = hashlib.sha256(password_bytes)
                hex_dig = hash_object.hexdigest()
                #Compara a password convertida da wordlist com a hash introduzida pelo utilizador
                if hex_dig == hash_input:
                    print(f"A sua hash decifrada é: {password}")
                    #Tocar um som para avisar o utilizador que o programa decifrou a hash
                    #Nome do ficheiro áudio
                    file_name = r"\done.wav"
                    #Adiciona ao caminho o nome do ficheiro áudio
                    audio_file = modified_path + file_name
                    #Toca o som
                    winsound.PlaySound(audio_file, winsound.SND_FILENAME)
                    print("Hash decifrada, pressione Esc para sair...")
                    while True:
                        # Verifica se a tecla foi primida
                        if keyboard.is_pressed('esc'):
                            print("A fechar...")
                            exit()
                else:
                    print(f"A verificar password: {password}")
                      
                                     
        #Caso o utilizador escolha usar a sua própria wordlist           
        elif path_choice=="2":
            path_custom=input("Insira aqui o caminho para a sua wordlist: ")
            #Substitui as \ para que não sejam reconhecidas como um caracter de escape pelo python
            modified_path = path_custom.replace("\\", "\\\\")
                
            #Abre o ficheiro wordlist e lê individualmente as passwords deste
            with open(modified_path, errors='ignore') as f:
                words = f.read().splitlines()
            #Faz um loop em que as passwords são convertidas em SHA256        
            for password in words:
                password = password.strip()
                password_bytes = password.encode('utf-8')
                hash_object = hashlib.sha256(password_bytes)
                hex_dig = hash_object.hexdigest()
                #Compara a password convertida da wordlist com a hash introduzida pelo utilizador
                if hex_dig == hash_input:
                    #Verifica o caminho do diretório onde está o ficheiro atual
                    path = os.path.dirname(os.path.abspath(__file__))
                    #Substitui as \ para que não sejam reconhecidas como um caracter de escape pelo python
                    modified_path = path.replace("\\", "\\\\")
                    
                    print(f"A sua hash decifrada é: {password}")
                    #Tocar um som para avisar o utilizador que o programa decifrou a hash
                    #Nome do ficheiro áudio
                    file_name = r"\done.wav"
                    #Adiciona ao caminho o nome do ficheiro áudio
                    audio_file = modified_path + file_name
                    #Toca o som
                    winsound.PlaySound(audio_file, winsound.SND_FILENAME)
                    print("Hash decifrada, pressione Esc para sair...")
                    while True:
                        # Verifica se a tecla foi primida
                        if keyboard.is_pressed('esc'):
                            print("A fechar...")
                            exit()
                else:
                    print(f"A verificar password: {password}")
        else:
            shutdown()       
   
    else:
        shutdown()       

#Chama a função escolha            
escolha()