# C5E - Tipo rata
 :  : DEC T(ST) K(C5A)
## OBIETTIVO
Definire i diversi tipi di rata della gestione dei pagamenti, con particolare riguardo alla separazione tra pagamenti contabili ed extra contabili.
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC **Descrizione**
Descrive il tipo di rata
 :  : FLD T$C5EA **Rata Extra contabile**
È un elemento V2/SI/NO :  se impostato, significa che la rata è generata da movimenti extracontabili, per cui non interesserà lo scadenzario contabile, ma eventuali altre gestioni (flussi di cassa, ...). Esso viene riportato nelle rate di dovuto all'atto della loro generazione.
 :  : FLD T$C5EB **Livello di nascita**
È un elemento TA/B£W00. È il livello assunto in inizializzazione della rata. In assenza viene assunto il livello '2'.
 :  : FLD T$C5EC **Gruppo flag**
È un elemento TA/B£Y. Definisce il gruppo di flag che viene assunto all'atto dell'inizializzazione della rata di dovuto.
 :  : FLD T$C5ED **Parametri interni**
È un elemento TA/C£I. Caratterizza i campi liberi (5 alfannumerici e 5 numerici) presenti nell'archivio delle rate che sono a disposizione dell'utente.
 :  : FLD T$C5EE **Parametri espliciti**
È un elemento TA/C£E. Definsce la categoria parametri per aggiungere informazioni alle rate.
 :  : FLD T$C5EF **Responsabile del credito**
Derivato da un attributo, definisce il valore che assume il campo "responsabile del credito" della rata contabile. È utilizzato inoltre durante il processo di inizializzazione del record (£C5C).
_7_Origine
Definisce l'oggetto origine da cui viene derivato l'attributo. Può assumere i seguenti valori : 
'1'  (CN) dall'ente a cui si riferisce la rata.
'2'  (E4) dalla testata della registrazione contabile a cui la rata appartiene.
'3'  (E5) dalla riga di registrazione a cui la rata appartiene.
NOTA BENE :  se l'oggetto indicato non è un "TAAGE", tale oggetto va indicato nel campo specifico della tabella C53 (Tipo Oggetto Responsabile).
 :  : FLD T$C5EG **Attributo**
Definisce il codice dell'attributo da utilizzare nel reperimento del valore, in funzione del campo "origine".
NOTA BENE :  se l'oggetto indicato non è un "TAAGE", tale oggetto va indicato nel campo specifico della tabella C53 (Tipo Oggetto Responsabile).
 :  : FLD T$C5EH **Exit inizializz. RR**
È il suffisso del programma di aggiustamento dell'inizializzatore/driver delle rate contabili, che innesca il richiamo del programma **C5C5C0_x** (x è il suffisso).
Tale programma viene richiamato dall'api £C5C ad ogni esecuzione in inizializzazione nuovi record o all'aggiornamento per scrittura, aggiornamento e cancellazione.
Il prototipo del programma è costituito dal sorgente C5C5C0_X.
