import json
dati = {
  "meteo" : "pioggia leggera",
  "tempAttuale" : 16,
  "citta" : "dalmine",
  "registrazioni" : [19,21,23,20,18]

}
datijson = json.dumps(dati)

#confronto il formato di pu con json
print(dati)
print(datijson)

#salvo i dati su file
f = open ("datisalvati.txt" , "w" , encoding= "utf-8")
f.write(datijson)
f.close()



