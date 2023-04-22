
# brute force simples para checar o tipo de arquivo cifrado


import os
import sys

def main():
    if len(sys.argv) != 2:
        print('''Uso: scrypt.py [arquivo]''')
    else:
        file = sys.argv[1]
        for i in range(257):
            os.system(f'./caesar -{i} {file} > out.out')
            os.system(f"echo 'key: {i}' && file out.out") 
main()
