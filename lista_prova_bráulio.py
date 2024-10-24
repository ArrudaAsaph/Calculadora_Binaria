from random import randint

# Gera um número binário aleatório de 16 bits
binario = [randint(0, 1) for _ in range(16)]


def complemento_de_dois(binario):
    if binario[0] == 1:  # Verifica se o número é negativo
        # Inverte os bits
        complemento = [1 if bit == 0 else 0 for bit in binario]
        # Adiciona 1 ao número invertido
        for i in range(len(complemento) - 1, -1, -1):
            if complemento[i] == 0:
                complemento[i] = 1
                break
            else:
                complemento[i] = 0
        
        # Converte o complemento de dois para decimal
        decimal = 0
        for i, bit in enumerate(complemento):
            decimal += bit * (2 ** (len(complemento) - 1 - i))
        
        return -decimal
    else:
        # Se o número for positivo, retorna o próprio número em decimal
        return binario_para_decimal(binario)

def binario_para_decimal(binario):
    decimal = 0
    for bit in binario:
        decimal = (decimal << 1) | bit
    return decimal

def main():
    complemento = complemento_de_dois(binario)
    complemento1 = complemento
    format_algarismo = binario
    
# PONTO FIXO
    aleatorio1 = randint(0,3)
    if(aleatorio1==0):
        x = 10
        y = 1
        z = 0
        padrão = "s iiiiiiiii . ffffff"
        decimal1 = (binario[x]*2**-1)+(binario[x+1]*2**-2)+(binario[x+2]*2**-3)+(binario[x+3]*2**-4)+(binario[x+4]*2**-5)+(binario[x+5]*2**-6)   
        inteiro = (binario[y]*2**8)+ (binario[y+1]*2**7)+(binario[y+2]*2**6)+(binario[y+3]*2**5)+(binario[y+4]*2**4)+(binario[y+5]*2**3)+(binario[y+6]*2**2)+(binario[y+7]*2**1)+(binario[y+8]*2**0)   
        if(binario[z]==0):
                sinal = "+"
        
        else:
                sinal = "-"
    

    elif(aleatorio1==1):
        x = 10
        y = 0
        z = 9
        padrão = "iiiiiiiii s fffffff"
        inteiro = (binario[y]*2**8)+ (binario[y+1]*2**7)+(binario[y+2]*2**6)+(binario[y+3]*2**5)+(binario[y+4]*2**4)+(binario[y+5]*2**3)+(binario[y+6]*2**2)+(binario[y+7]*2**1)+(binario[y+8]*2**0)   
        decimal1 = (binario[x]*2**-1)+(binario[x+1]*2**-2)+(binario[x+2]*2**-3)+(binario[x+3]*2**-4)+(binario[x+4]*2**-5)+(binario[x+5]*2**-6)   
        if(binario[z]==0):
            sinal = "+"
        else:
            sinal = "-"
     

    elif(aleatorio1==2):
        x = 0
        y = 7
        z = 6
        padrão = "ffffff s iiiiiiii"
        inteiro = (binario[y]*2**8)+ (binario[y+1]*2**7)+(binario[y+2]*2**6)+(binario[y+3]*2**5)+(binario[y+4]*2**4)+(binario[y+5]*2**3)+(binario[y+6]*2**2)+(binario[y+7]*2**1)+(binario[y+8]*2**0)   
        decimal1 = (binario[x]*2**-1)+(binario[x+1]*2**-2)+(binario[x+2]*2**-3)+(binario[x+3]*2**-4)+(binario[x+4]*2**-5)+(binario[x+5]*2**-6)   
        if(binario[z]==0):
            sinal = "+"
        else:
            sinal = "-"
    

    elif(aleatorio1==3):
        x = 9
        y = 0
        z = 15
        padrão = "iiiiiiii . ffffff s"
        inteiro = (binario[y]*2**8)+ (binario[y+1]*2**7)+(binario[y+2]*2**6)+(binario[y+3]*2**5)+(binario[y+4]*2**4)+(binario[y+5]*2**3)+(binario[y+6]*2**2)+(binario[y+7]*2**1)+(binario[y+8]*2**0)   
        decimal1 = (binario[x]*2**-1)+(binario[x+1]*2**-2)+(binario[x+2]*2**-3)+(binario[x+3]*2**-4)+(binario[x+4]*2**-5)+(binario[x+5]*2**-6)   
        if(binario[z]==0):
            sinal = "+"
        else:
            sinal = "-"
       

    elif(aleatorio1==4):
        x = 0
        y = 6 
        z = 15 
        padrão = "ffffff . iiiiiiii s"
        inteiro = (binario[y]*2**8)+ (binario[y+1]*2**7)+(binario[y+2]*2**6)+(binario[y+3]*2**5)+(binario[y+4]*2**4)+(binario[y+5]*2**3)+(binario[y+6]*2**2)+(binario[y+7]*2**1)+(binario[y+8]*2**0)   
        decimal1 = (binario[x]*2**-1)+(binario[x+1]*2**-2)+(binario[x+2]*2**-3)+(binario[x+3]*2**-4)+(binario[x+4]*2**-5)+(binario[x+5]*2**-6)   
        if(binario[z]==0):
            sinal = "+"
        else:
            sinal="-"
       
            

    ponto_fixo = sinal + str(inteiro+decimal1)
    print(padrão)
    print(ponto_fixo)
            

    # print(padrão)          
    # print(sinal,inteiro+decimal1,sep="")
    # print(*binario,sep="")
    # print(binario[1],binario[2],binario[3],binario[4],binario[5],binario[6],binario[7],binario[8],sep="")

    conversão1 = ((int(format_algarismo[0]))*2**15)+((int(format_algarismo[1]))*2**14)+((int(format_algarismo[2]))*2**13)+((int(format_algarismo[3]))*2**12)+((int(format_algarismo[4]))*2**11)+((int(format_algarismo[5]))*2**10)+((int(format_algarismo[6]))*2**9)+((int(format_algarismo[7]))*2**8)+((int(format_algarismo[8]))*2**7)+((int(format_algarismo[9]))*2**6)+((int(format_algarismo[10]))*2**5)+((int(format_algarismo[11]))*2**4)+((int(format_algarismo[12]))*2**3)+((int(format_algarismo[13]))*2**2)+((int(format_algarismo[14]))*2**1)+((int(format_algarismo[15]))*2**0)


    if (binario[0]==0):
        conversão2 = ((int(format_algarismo[1]))*2**14)+((int(format_algarismo[2]))*2**13)+((int(format_algarismo[3]))*2**12)+((int(format_algarismo[4]))*2**11)+((int(format_algarismo[5]))*2**10)+((int(format_algarismo[6]))*2**9)+((int(format_algarismo[7]))*2**8)+((int(format_algarismo[8]))*2**7)+((int(format_algarismo[9]))*2**6)+((int(format_algarismo[10]))*2**5)+((int(format_algarismo[11]))*2**4)+((int(format_algarismo[12]))*2**3)+((int(format_algarismo[13]))*2**2)+((int(format_algarismo[14]))*2**1)+((int(format_algarismo[15]))*2**0)
        
        sinal1 = "+" 

    else:
        conversão2 = ((int(format_algarismo[1]))*2**14)+((int(format_algarismo[2]))*2**13)+((int(format_algarismo[3]))*2**12)+((int(format_algarismo[4]))*2**11)+((int(format_algarismo[5]))*2**10)+((int(format_algarismo[6]))*2**9)+((int(format_algarismo[7]))*2**8)+((int(format_algarismo[8]))*2**7)+((int(format_algarismo[9]))*2**6)+((int(format_algarismo[10]))*2**5)+((int(format_algarismo[11]))*2**4)+((int(format_algarismo[12]))*2**3)+((int(format_algarismo[13]))*2**2)+((int(format_algarismo[14]))*2**1)+((int(format_algarismo[15]))*2**0)
        sinal1 = "-"

    

    # print("O número binário gerado é:", *binario, sep="")
    # print("O complemento de dois em decimal é:", complemento1)
    # print(conversão1)
    aleatorio = randint(1,4)
    if (aleatorio==0):
        print("    Binario     |   Natural   |   Complemento de Dois    |   Sinal Magnitude   |   Ponto Fixo    |   Ponto Flutuante   ")
        print("                |             |                          |                     |{}|                     ".format(padrão))
        print(*binario, "|   Natural   |   Complemento de Dois    |   Sinal Magnitude   |   Ponto Fixo    |   Ponto Flutuante   ",sep="")
    elif(aleatorio==1):
        print("    Binario     |   Natural   |   Complemento de Dois    |   Sinal Magnitude   |   Ponto Fixo    |   Ponto Flutuante   ")
        print("                |             |                          |                     |{}|                     ".format(padrão))
        print("    Binario     |","    ",conversão1,"    "     ,"|   Complemento de Dois    |   Sinal Magnitude   |   Ponto Fixo    |   Ponto Flutuante   ",sep="")
    elif(aleatorio==2):
        print("    Binario     |   Natural   |   Complemento de Dois    |   Sinal Magnitude   |   Ponto Fixo    |   Ponto Flutuante   ")
        print("                |             |                          |                     |{}|                     ".format(padrão))
        print("    Binario     |   Natural   |","           ", complemento1 ,"         ",     "|   Sinal Magnitude   |   Ponto Fixo    |   Ponto Flutuante   ",sep="")
    elif(aleatorio==3):
        print("    Binario     |   Natural   |   Complemento de Dois    |   Sinal Magnitude   |   Ponto Fixo    |   Ponto Flutuante   ")
        print("                |             |                          |                     |{}|                     ".format(padrão))
        print("    Binario     |   Natural   |   Complemento de Dois    |","         ",sinal1,conversão2,"        ","|   Ponto Fixo    |   Ponto Flutuante   ",sep="")
    elif(aleatorio==4):
        print("    Binario     |   Natural   |   Complemento de Dois    |   Sinal Magnitude   |   Ponto Fixo    |   Ponto Flutuante   ")
        print("                |             |                          |                     |{}|                     ".format(padrão))
        print("    Binario     |   Natural   |   Complemento de Dois    |   Sinal Magnitude   |","   ",   ponto_fixo    ,"   ","|   Ponto Flutuante   ",sep="")
    a= input()
    print("    Binario     |   Natural   |   Complemento de Dois    |   Sinal Magnitude   |   Ponto Fixo    |   Ponto Flutuante   ")
    print("                |             |                          |                     |                 |                     ")  
    print(*binario, "|","    ",conversão1,"    "     ,"|","           ", complemento1 ,"         ",     "|","         ",sinal1,conversão2,"        ","|","   ",   sinal,inteiro+decimal1    ,"   ","|   Ponto Flutuante   ",sep="")

if __name__ == "__main__":
    main()




