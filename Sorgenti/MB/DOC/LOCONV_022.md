### Titolo
E' la costante o la variabile definita titolo della finestra.

**Assunzioni sulle finestre**, E' considerata intestazione tutta la prima riga e i soli campi della seconda riga che iniziano prima della ventesima colonna.

**Assunzioni sui formati**, E' considerata intestazione tutta la prima riga e i soli campi della seconda riga che iniziano nelle colonne fra la nona e la settanta.

**Eslusioni e Inclusioni**, Sono esclusi dall'intestazione i seguenti campi : 
   £RAS*
   *PDS*
   £G00AZ
   £G00DV
   £G00ES
   La costante <--
Sono inclusi nell'intestazione i seguenti campi : 
   W$TIT* (fino alla terza riga)

### Comandi
Sono i tasti funzionale CFxx e CAxx.
**Funzionamento**, Durante la conversione viene ricercata la loro descrizione nel video attraverso le costanti Fx= o Fxx=, se non trovata ne verrà assegnata una di default. Tutte le costanti rimanenti contenti Fx= o Fxx= sono trasformate in "CommandText" anche in assenza della sua definizione sul video. Nei Subfile, sarà cura del client grafico unire i comand del piede al formato in emissione.

### Descrizioni di default
    F01=Help
    F02=Funzione
    F03=Fine
    F04=Decodifica
    F12=Ritorno
    F22=Informazioni programma

### Costanti
**Esclusioni**,    Eseguite subito : 
     /
     >
     <
     >> (Solo se persente dopo la ventiduesima)
Eseguite dopo l'attribuzione dei componenti
     <>
     <--

### Messaggio
E' la variabile utilizzata per l'emissione delle segnalazioni nella barra di stato
**Assunzione sui formati**, Il campo deve trovarsi dopo la ventiduesima riga.

**Eslusioni e Inclusioni**, Sono inclusi i soli campi alfabetici con i seguenti nomi : 
     W$M130
     W2MES1
     W$MES*
Sono esclusi i campi : 
     W$MESE
     W$MESG

### Intestazione di colonna
Sono derivate dalle due righe precedenti alla prima riga del subfile.
**Esclusioni di riga**
E' esclusa la prima riga
E' esclusa la seconda riga a meno che non sia una window
Sono escluse le righe che iniziano dalla ventunesima
Non sono fatti controlli di esclusione riga sui programmi : 
     C5MH01L
     B£G08G
Sono escluse le righe che contengono i campi : 
     £AUA*
o le costanti contenenti i caratteri : 
     =
o i campi di input solo se non sono protetti
o la seconda riga se non possiede campi nelle prime 10 posizioni

### Ricerca dell'intestazione
Se non viene identificata un'intestazione ne viene desunta una utilizzanto la sequente risalita : 
     Forzata dall'utente
     Dall'oggetto
     Dal dizionario

Sono esclusi gli articoli di congiunzione sia minuscoli che maiuscoli : 
     di
     da
     con
     su
     per
     fra
     tra
e se presenti più righe di le parole sono distribuite su entrambe.

### Opzioni
E' il campo si selezione della funzione desiderata.
**Assunzioni**, Assunto progressivo vuoto

**Inclusioni**, Sono considerati Opzioni i seguenti campi : 
     W$OPZ*
     W$MODA
     S$OPZ* (solo se si tratta di una lista)
     W$SBEM (solo se è riferita al programma CQBC10GV o CQBC50GV)

### Lista opzioni
E' l'elenco delle opzioni disponibili, sono legati all'opzione tramite il progressivo.
**Assunzioni**, Assunto progressivo vuoto

**Inclusioni**, Sono considerate liste di opzini i seguenti campi : 
     £AUAS*
     UI£OPZ
     W$AUS*
Sono considerate liste di opzioni le costanti col carattere :  = con almeno uno dei due caratteri seguenti diversi da spazio.

### Lista Pannelli di formato
E' la lista dei pannelli disponibili (legati al pannello tramite il progressivo) Si presenta in evidenza quello associato al numero del pannello attivo (vedi dopo)
**Inclusioni**, Sono considerate liste di pannelli i seguenti campi :  WX£FMT

**Esempio**, Vedere la gestione nel programma BRAR02D_$C e relativo video Il campo contiene una lista del tipo 1=aaa 2=bbb ecc

### Pannello di formato attivo
E' il campo di selezione del pannello desiderato all'interno della lista formati
**Inclusioni**, Sono considerati Pannelli i seguenti campi :  WX$FMT

**Esempio**, Vedere la gestione nel programma BRAR02D_$C e relativo video Il campo contiene un numero che viene descritto nella lista
