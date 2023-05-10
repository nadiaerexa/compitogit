import json

f = open ("datisalvati.txt" , "r" , encoding= "utf-8")
datijson= f.read()
f.close()


dati= json.loads(datijson)

#stampacontrollo
print(dati["citta"])
print(dati["registrazioni"][2])
