
# OBIETTIVO
Gestire tutte le funzioni sui carrelli utente

# FUNZIONI/METODI
Premessa :  ad ogni FUN/MET del B£SER_25 corrispondono una FUN/MET della £G97; per la lista delle Funzioni/Metodi vedere la documentazione della £G97.
Qui sotto riportiamo una carrellata delle FUN/MET del B£SER_25 associandole alle FUN/MET della /Copy.

## Funzioni Generiche

- GET.TIP visualizza in matrice la lista dei tipi oggetti contenuti nei carrelli
- GET.OWN visualizza in matrice i carrelli di un dato tipo
- GET.FLR visualizza in matrice le cartelle omogenee
- GET.OGG visualizza in matrice gli oggetti all'interno di una cartella o di un carrello
- DED.ADE Drag&Drop :  aggiunge elemento al carrello; GEL.CRE della G97
- DED.MOV Drag&Drop :  spostamento di un elemento all'interno del carrello; prima GEL.DEL per cancellazione dell'elemento in questione e poi GEL.CRE per inserimento dell'elemento nel nuovo posto assegnato
- DED.DEE Drag&Drop :  elimina elemento dal carrello; GEL.DEL della G97


## Sul Carrello

- GES.CAR.CRE creazione del carrello; GCR.CRE della G97
- GES.CAR.DEL cancellazione del carrello :  GCR.DEL della G97
- GES.CAR.CRL svuotamento del carrello :  GCR.CLR della G97


## Sulle Cartelle

- GES.CRT.CRE creazione della cartella; GCT.CRE della G97
- GES.CRT.DEL cancellazione della cartella :  GCT.DEL della G97
- GES.CRT.CRL svuotamento della cartella :  GCT.CLR della G97


## Sul contenuto (elementi)
Le funzioni sono ancora quelle spiegate per il Drag&Drop cioè : 

- DED.ADE
- DED.MOV
- DED.DEE

