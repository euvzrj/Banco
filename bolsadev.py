def leiaInt(msg):
    while True:
        try: 
            n = int(input(msg))
        except (ValueError, TypeError):
            print("ERRO: Por favor instira um valor válido")
            continue
        else:
            return n  
        
num = leiaInt("A")
print(num)