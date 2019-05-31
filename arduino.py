import serial 

ser = serial.Serial('COM6', 9600)

lista=[]

for i  in range(10):
    lista.append(ser.readline())
    print (lista[i])



print('-'*50)


#print (lista)
print('Tamanho da lista',len(lista))
