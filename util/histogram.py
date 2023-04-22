import sys

def histogram(s):
    d = dict()
    v = s.split(' ')
    for c in v:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1

    return d

def print_hist(h):
    for c in h:
        print (c, h[c])

def bin_to_ascii(string_b):
    string_ascii = ''
    for c in string_b:  
        string_ascii += f'{c}' + ' '
    return string_ascii

def main():
    file = sys.argv[1]                       # atribui à variavel file o arquivo passado como parâmetro

    string_b = ''

    with open(file, 'rb') as f:
        string_b = f.read()                  # lê o arquivo

    string_ascii = bin_to_ascii(string_b)    # converte a string de binario para ascii

    h = histogram(string_ascii)              # faz o histograma da string

    #print_hist(h)                            #printa o histograma
    print_hist(dict(sorted(h.items(), key=lambda x:x[1], reverse=True)))                            #printa o histograma ordenado



main()
