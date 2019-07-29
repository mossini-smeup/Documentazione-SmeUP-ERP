# Oggetti Esterni a Sme.Up.
Attraverso il nuovo oggetto V5 è possibile integrare in Sme.Up  oggetti esterni letti attraverso web service.

* L'oggetto va descritto nello script SCP_WSI
* Il web service va descritto nel costruttore A38

Una volta completato il setup delloggetto avremo disponibile in Sme.UP
* Ricerca delloggetto
* Decodifica delloggetto
* Attributi I/ delloggetto

## Script configurazione web service
L'oggetto va descritto nello script SCP_SET con nome LOA38_xx descritto in sezioni.
 :  : PAR L(N03) T(Estratto delle sezioni)
SEZ Sezione
A38.CLSSEZ
SUB Sub Sezione
A38.SUBMET Metodo
A38.SUBVAR Variabili


## Script configurazione oggetto esterno
L'oggetto va descritto nello script SCP_WSI il nome deve iniziare per V5_
Qui vengono descvritte le seguenti informazioni : 

* metodo di autentificazione
* metodo di accesso per la ricerca
* metodo di accesso per la verifica
* attributi interni
* percorsi jason per reuperare : 

 :  : PAR L(N03) T(Estratto delle sezioni)
FUN.LIS metodo di ricerca
COD codice
DEB  Descrizione estesa
 DEC Descrizione

 FUN.DEC metodo di ricerca
 OAV attibuto dove : 
       G/10 Codice
       G/12 Descrizione
       G/40 Descrizione estesa
       I/.. Altri valori

