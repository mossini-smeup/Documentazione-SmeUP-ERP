# OBIETTIVO
Ottenere informazioni sulle varie componenti di un servizio
# PREREQUISITI
D/COPY QILEGEN,£J03DS
C/COPY QILEGEN,£J03

# PARAMETRI

## PARAMETRI DI INPUT

## Funzioni (£J03FU)

### Funzione DAT
La funzione **DAT** restituisce i dati identificativi del servizio come Descrizione, utente di creazione/aggiornamento, ecc. .A questa funzione è associato il metodo SER.

### Funzione ESE
La funzione **ESE** esegue il servizio indicato nel campo £J03SE, con il metodo specificato nel campo £J03FM.
A questa funzione sono associati i metodi : 
 :  : PAR
**POS** = Posizionamento
**LET** = Lettura


### Funzione FMT
La funzione **FMT** si occupa di definire la formattazione della stringa che le viene passata nel campo £J03DI
A questa funzione sono associati i metodi : 
 :  : PAR
**D_S** = Formattazione con passaggio da riga in formato £UIBDS ad             un formato di stringa semplice.

**S_D** = Formattazione con passaggio da formato di stringa semplice            ad una riga in formato £UIBDS


### Funzione PRO
La funzione **PRO** si occupa di estrarre le chiamate di tutti i prototipi del servizio indicato nel campo £J03SE
A questa funzione sono associati i metodi : 
 :  : PAR
**POS** = Posizionamento sul primo prototipo del servizio.

**LET** = Lettura prototipi del servizio.

**RIC** = Restituisce l'elenco di tutti prototipi relativi al              servizio indicato.


### Funzione FEM
La funzione **FEM** si occupa di estrarre le funzioni/metodi del del servizio indicato nel campo £J03SE
A questa funzione sono associati i metodi : 
 :  : PAR
**POS** = Posizionamento sulla prima funzione/metodo del servizio.

**LET** = Lettura funzioni/metodi del servizio.

**RIC** = Restituisce l'elenco di tutti le funzioni/metodi relative al              servizio indicato.

### Funzione SEZ
La funzione **SEZ** si occupa di estrarre le sezioni del configuratore relative al  servizio indicato nel campo £J03SE
A questa funzione sono associati i metodi : 
 :  : PAR
**POS** = Posizionamento sulla prima sezione del servizio.

**LET** = Lettura sezioni del servizio.

**RIC** = Restituisce l'elenco di tutti le sezioni relative al              servizio indicato.

### Funzione ATT
La funzione **ATT** si occupa di estrarre gli attributi  del servizio indicato nel campo £J03SE
A questa funzione sono associati i metodi : 
 :  : PAR
**POS** = Posizionamento sul primo attributo del servizio.

**LET** = Lettura attributi del servizio.

**RIC** = Restituisce l'elenco di tutti gli attributi relativi al              servizio indicato.

### Funzione ATT_CFG
La funzione **ATT_CFG** si occupa di estrarre gli attributi per il cofiguratore del servizio indicato nel campo £J03SE
A questa funzione sono associati i metodi : 
 :  : PAR
**POS** = Posizionamento sul primo attributo del servizio.

**LET** = Lettura attributi del servizio.

### Funzione ATT_G30
La funzione **ATT_CFG** si occupa di estrarre gli attributi per la /copy G30 del servizio indicato nel campo £J03SE
A questa funzione sono associati i metodi : 
 :  : PAR
**POS** = Posizionamento sul primo attributo del servizio.

**LET** = Lettura attributi del servizio.


### Funzione VAL
La funzione **VAL** si occupa di restituire i valori di un singolo attributo di un servizio indicato nel campo £J03AT
A questa funzione sono associati i metodi : 
 :  : PAR
**POS** = Posizionamento sulla prima attributo del servizio e             restituzione del valore

**LET** = Lettura attributi e relativa estrazione dei valori

**RIC** = Restituisce l'elenco di tutti i valori  relative all             atributo indicato.

