# GESTIONE CONDIZIONI CAMPI DI UN ARCHIVIO
## FORMATI VIDEO
## OBIETTIVO
Permettere la gestione di una serie di vincoli e regole relativamente al contenuto dei campi di un archivio.
Attraverso tali regole deve risultare possibile validare la correttezza di un insieme di informazioni prima che vengano sritte su un record (ad esempio i campi di un articolo del MAPICS)
## IMPOSTAZIONE
Se pensiamo ad una IMPLICAZIONE, abbiamo i due momenti : 
.    SE        ....
.    ALLORA    ....

Ad esempio potremo dire :  SE il campo unità di misura contiene KG, ALLORA il tipo parte deve essere maggiore di 3, oppure SE il campo CLASSE contiene un valore questo deve essere definito nella tabella CLS, ecc.

## TABELLE COLLEGATE
C£F  Tabella archivi descritti alle manutenzioni di massa
C£M  Tabella di definizione campi
C£C  Tabella condizioni sui campi

## SOTTOFUNZIONI
Condizioni in funzione del contenuto di un campo

Se si sceglie tale funzione è obbligatorio indicare uno dei campi specificati nella tabella C£M. Si presenta un formato che permette di indicare la CONDIZIONE da verificare quando il campo ha un determinato contenuto.

Ad esempio potremo indicare per il campo UNITA' DI MISURA
>KG                  PESO      Condizioni di peso
MT                  LUNG      Condizioni di lunghezza
Ecc.


### Vincoli attivi per una condizione
Impostata una condizione viene presentata una lista che permette di specificare un elenco di campi il cui contenuto deve essere controllato. Posso quindi indicare che per la condizione PESO, il campo 003 (Tipo parte) deve essere compreso fra 3 e 9, e il campo REPARTO è obbligatorio.

### Gestione del dettaglio
Il formato di dettaglio permette una manutenzione controllata e con decodifica degli stessi dati presenti nella lista.

## CONDIZIONI SPECIALI
### Condizioni iniziali
La condizione ****** se presente viene verificata come all'inizio e definisce le obbligatorietà,

### Condizioni finali
