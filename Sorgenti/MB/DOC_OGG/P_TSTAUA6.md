# CONTROLLO ACCESSI UTENTE APPLICAZIONE

# OBIETTIVO
Oltre alla normale protezione prevista a livello di sistema AS400 sugli oggetti (programmi e archivi), si prevede di impostare una tecnica di attribuzione autorizzazioni per utente/applicazione, a livello applicativo.

Ciò permetterà ad esempio di proteggere la singola informazione di un record oppure le condizioni di richiamo in immissione/modifica di una stessa transazione.

# SOLUZIONE
Realizzeremo un programma che data una classe di sicurezza, restituisca, in funzione dell'utente, 10 possibili condizioni di accesso, il cui significato e' in funzione della classe di sicurezza (ovvero dell'applicazione).

Se non sono definite condizioni per un utente, il programma legge le condizioni relative al gruppo di utenti, e in mancanza anche di queste si utilizzano le condizioni di DEFAULT definite per l'utente "**"

Ogni condizione avrà 10 possibili contenuti.

Possiamo immaginare di avere per ogni classe di sicurezza una tabella di 10 righe e 10 colonne.

Supponiamo di voler realizzare una protezione relativamente ai costi (che chiameremo "COSTI").
Possiamo separare le seguenti aree : 

- Calcolo
-- SI
-- NO
- Livello di autoriz. in interrogazione
-- Fino ai costi variabili
-- Fino al costo industriale
-- Fino al costo pieno
- Modifica costi
-- ** = tutti
-- AC = di acquisto
-- LE = solo lavorazioni esterne
- Ecc.


Dato un utente avremo : 
>UTENTE1         Sc      Opzioni
1. Calcolo      NO      SI NO
2. Interrog.    04      01 02 03 04
3. Modifica     **      AC LE

Nella scrittura del programma si potranno usare tutti i condizionamenti necessari.

# DETTAGLIO DI PROGRAMMAZIONE
# TABELLE
B£P  Classi di autorizzazione
Rispetto all'esempio di sopra, sarà qui descritto il codice "COSTI"

B£S  Significati per classe di protezione
elementi che descrivono le righe della
Si scompone in un sottosettore richiamato tramite la tabella B£P. Ogni sottosettore contiene fino a
matrice. Ogni elemento contiene i possibili valori della scelta.
NB.  Si faccia riferimento al documento tabelle per maggiori dettagli.

# PROGRAMMA DI GESTIONE
Devono funzionare : 
.    Ricerche (tranne su utente)
.    Ripresa da un collegato
.    Formato di scelta per : 
- utente in mancanza di classe
# PROGRAMMA CHIAMATO PER LETTURA SCELTE
- classe in mancanza di utente

## PROGRAMMA CHIAMANTE
Fornisce : 
"CLASSE DI PROTEZIONE"
Riceve : 
valori di 2 caratteri
## PROGRAMMA CHIAMATO
Riceve : 
"CLASSE DI PROTEZIONE"
Ricerca l'utente e il suo gruppo di appartenenza.
Cerca la prima definizione di autorizzazione valida fra : 
.    UTENTE/CLASSE
.    GRUPPO/CLASSE
.    "**"/CLASSE
.    "**"/"**"
Fornisce : 
valori di 2 caratteri
