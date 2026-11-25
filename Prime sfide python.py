#Sfida 1
nome = ("Giosue") 
eta = (14)
saluto = ("Ciao" + " " + nome)
print (saluto)

#Sfida 2
resto = 25 % 4
if resto is 1:
    print ("il resto è 1!")
else:
    print("il resto è diverso")

#Sfida 3
zaino = []
zaino.append ("Astuccio")
zaino.append ("Computer")
zaino.append ("Quaderno")

posizione = ["Poizione"] * 4

inventario = zaino + posizione
print (inventario [1])

for x in inventario:
    print (x)