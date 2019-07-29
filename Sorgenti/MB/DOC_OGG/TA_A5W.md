# A5W - Inizializzazione cespite
 :  : DEC T(ST) K(A5W)
## OBIETTIVO
Definisce il corredo di informazioni degli oggetti dell'applicazione (cespiti, movimenti).
Codificando un elemento di questa tabella, ed assegnandolo alla opportuna classe (categoria fiscale, causale cespiti), tutti gli oggetti della classe ne ereditano i campi.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Codice**
Indica il codice dell'inizializzazione
 :  : FLD T$A5WA **Livello di nascita**
Si imposta il livello di nascita dell'oggetto, in assenza si assume '2'
 :  : FLD T$A5WB **Gruppo flag**
È il gruppo flag assegnato all'oggetto all'atto della sua creazione.
 :  : FLD T$A5WC **Categoria parametri**
È la categoria di parametri assegnabili all'oggetto
 :  : FLD T$A5WD **Parametri impliciti**
Riguarda i parametri impliciti (5 alfanumerici e 5 numerici) che si possono assegnare all'oggetto
 :  : FLD T$A5WE **Contenitore note**
È il contenitore delle note che si possono scrivere per l'oggetto
 :  : FLD T$A5WF **Suffisso programma di aggiustamento**
È il suffisso x del programma di aggiustamento eseguito all'atto dell'inserimento, della modifica e dell'aggiornamento dell'oggetto
Per l'oggetto cespite il programma è A5A5A0_x
Per l'oggetto movimento il programma è A5A5B0_x
