 :  : HEA RESP(LS) STAT(00)

# OBIETTIVO
Il servizio si propone come strumento di comprensione dell'algoritmo di assegnazione delle quote percentuali riservate ad ogni colonna di una matrice nel momento della stampa.

# Comprensione del simulatore
## Script di origine
- Vedere nome e contenuto nella scheda stessa

## Funzione matrice di calcolo
01 = Lunghezza ripresa dall'XML come paramtro LUN di COLONNA
02 = Massima lunghezza dell'intestazione
03 = Massima lunghezza dei dati (senza intestazione)
04 = Massima lunghezza del totale (per colonne numeriche)
05 = Massimo fra 01 e 04
06 = Massimo fra 02 e 04
07 = Massimo fra 03 e 04 (Trascuro header essendo una sola riga accetto il ritorno a capo)
08 = Utilizzato nella strategia di riadeguamento delle colonne con testo lungo ae eccedo i car.max.
09 = Numero caratteri utilizzati per il calcolo percentuale (in base alla strategia scelta). Normalmente saranno le colonne 5/6/7/8 incrementate di 1/2/3 caratteri in base al numero complessivo di righe.
10 = % restituita al chiamante
11 = Caratteri ricalcolati a partire dalla percentuale
12 = Liberi considerando anche le intestazioni
13 = Liberi (se negativo sono mancanti) nei soli dati. Il negativo indica un ritorno a capo certo.

## Funzione e contenuto dei parametri
- Esterni = Possono essere ricevuti dal SCRIPT oppure dalla funzione "P(Car() Esp() Com())". Hanno un valore di
default.
- Calcolo = Coincidono con i totali della matrice dei risultati
- Strateie = Vedi paragrafo specifico
- Servizio = Altri parametri calcolati e di utilità

## Strategie
### Compatibili
1. Totale 05 inferiore al numero massimo di caratteri ammessi
1A. Se mancante a 100 supera    il limite di espansione lascio spazio in fondo a destra
1B. Se mancante a 100 inferiore al limite di espansione espando a 100
2. Totale 06 inferiore al numero massimo di caratteri ammessi
2A. Come sopra
2B. Come sopra
3. Totale 07 inferiore al numero massimo di caratteri ammessi
3A. Come sopra
3B. Come sopra
### Con adeguamento
Calcolo la colonna 08 (Adeguamento dei massimi). Estraggo tutte le colonne inferiori a 15 caratteri e riservo loro gli spazi necessari assumendo di non comprimerle. Distribuisco lo spazio residuo sulla percentuale restante in proporzione alla lunghezza massima dei dati.
4A. Se il totale 8 non supera il numero massimo del numero di espansione % ammessa procedo
4B. Negli altri casi taglio le colonne non ammesse
### Compressione
