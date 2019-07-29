# MOCIM     -  MODALITÀ COSTRUZIONE IMPEGNI MATERIALI
Definisce le varie modalità con cui possono essere costruiti gli impegni materiali di un documento (ordine di
produzione/riga di lavorazione).
Va tenuto presente che, qualora la costruzione preveda la presenza (anche opzionale) della distinta del documento, se
non è impostato in tabella degli impegni il tipo distinta di memorizzazione (che è appunto il tipo distinta in cui si
memorizza l'eventuale distinta specifica del docuemnto), la scansione termina con un messaggio d'errore.

## VALORI POSSIBILI

### DB DISTINTA OGGETTO
Viene trattata unicamente la distinta dell'articolo intestatario del documento, del tipo impostato in tabella
P5I nel campo 'tipo distinta origine'.

### D1 DISTINTA DOCUMENTO / DISTINTA OGGETTO
Se presente, viene trattata la distinta del documento, intestata al n.documento, del tipo impostato in tabella P5I nel
campo 'tipo distinta memorizzata', se assente viene assunta la distinta oggetto.

### D2 DISTINTA DOCUMENTO
E'come il caso precedente, senza la risalita alla distinta oggetto.

### D3 STESSO OGGETTO + DISTINTA DOCUMENTO/STESSO OGGETTO + DISTINTA OGGETTO
E'come il caso D1, con l'aggiunta, in entrambi i casi, dell'assieme come primo componente, con quantità di legame 1.

### OJ STESSO OGGETTO
E'un legame dell'assieme con se stesso, con quantità di legame 1.
Serve nel caso di ordini di rilavorazione/riparazione.

### F1 OGGETTO FISSO DA TABELLA V54
E'un legame dell'assieme con un oggetto impostato in tabella V54 : 
serve per la gestione del conto trasformazione.

### L1 DISTINTA DOCUMENTO/DISTINTA LAVORAZIONE OGGETTO
Serve nel caso di conto lavorazioen di fase. Se assente la distinta del documento viene assunta la distinta di
lavorazione dell'oggetto, vale a dire i materiali alla fase dell'oggetto.

### L2 DISTINTA DOCUM./DIST.LAVORAZ.DOCUM/DIST.LAVOR.OGGETTO
Se assente la distinta del documento, viene esaminata la distinta di lavorazione del documento, vale a dire i
materiali alla fase del documento origine (ordine di produzione) :  quest'ultima poi si può ridirezionare sulla distinta
dell'oggetto in funzione della modalità di scansione dell'ordine di produzione origine.

### UT LIBERA UTENTE
La scansione viene ridirezionata al programma definito come aggiustamento nella tabella del tipo impegno (P5I) in cui
viene inserita questa modalità di costruzione.
