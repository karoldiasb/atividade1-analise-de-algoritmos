import time

tempo_i = time.time()
arquivo = open('dataset-1-c.csv','r')
read = arquivo.read()

def encontra(n, lista):
    i = 0
    for l in lista[2:10]:
        if (n == l):
            return "True\n" + str(i)
        i = i + 1
    return "False\n" +  str(-1)

lista = read.split("\n")
lista.remove('')
resp = encontra(lista[0], lista)
tempo_f = time.time()

s = tempo_f - tempo_i
#print(sub)

a = open('resposta-dataset-1-c.txt','w')

#print(str(texto))
a.writelines(str(resp))
a.writelines("\n"+str(s))

a.close()
arquivo.close()


