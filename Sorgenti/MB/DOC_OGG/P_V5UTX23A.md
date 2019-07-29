
# Obiettivo
Trovare nei sorgenti personalizzati le specifiche da adeguare a seguito delle modifiche avvenute per la sostituzione del campo R§TIOG con il campo R§TPOG.

# Note sulle stringhe di ricerca

***R§TIOG** :  è il campo eliminato che va sostituito con il campo R§TPOG. Se il campo R§TIOG conteneva un elemento della tabella B£G il nuovo campo deve contenere un oggetto OG.
NOTA BENE 1 :  è fondamentale che dove il campo R§TPOG verrà riempito venga sempre riempito  con un oggetto che non abbia valorizzato un parametro falcolativo (es. AR non dovrà mai essere ARxxx). Per aiutare in questo è possibile richiamare il pgm B£B£G2 passando il tipo oggetto. Es.
C                   CALL      'B£B£G2'
C                   PARM                    R§TPOG           12
NOTA BENE 2 :  il campo R§TIOG esiste anche sul file GARDAT0F, ma quanto è utilizzato per tale archivio non va fatta alcuna modifica.

***TIOG** :  ricerca generica del campo, nel caso in cui campo R§TIOG sia stato ridenominato. Valgono tutte le considerazioni del punto precedente.

***£V5PTO** :  valgono le medesime considerazioni del campo R§TIOG, solo che questo viene sostituito con il campo £V5PTT

***£V5PDE** :  è stato eliminato. Conteneva la descrizione dell'ente contenuto nei campi £V5PTC e £V5PEN. Dove viene valorizzato basta asteriscare, mentre dove veniva letto sarà necessario eseguire la £DEC basandosi sui campi £V5PTC e £V5PEN.

***£G03TO** :  valgono le medesime considerazioni del campo R§TIOG, solo che questo viene sostituito con il campo £G03TP

***V5RDOC*** :  sono tutti i logici che in chiave contenevano il campo R§TIOG che ora è stato sostituito con il campo R§TPOG. Vanno perciò verificati gli eventuali adeguamenti rispetto all'utilizzo di tali logici.

***G9AS100F** :  file di work del controllo bolle fatture G9. In questo archivio il campo M$TIOG è stato sostituito con il campo M$TPOG. Le considerazioni sono sempre le stesse dei campi R§TIOG ed R§TPOG.

***G9AS101F** :  come sopra ma per i campi T$TIOG e T$TPOG.

***V5AS100F** :  come sopra per i campi M$TIOG e M$TPOG.

***V5AS101F** :  come sopra per i campi T$TIOG e T$TPOG.

***£V6CTO** :  valgono le medesime considerazioni del campo R§TIOG, solo che questo viene sostituito con il campo £V6CTP

***WWTIOG** :  anche per questo campo, usato sui file V5AT15* valgono le medesime considerazioni con il campo WWTPOG fatte per i campi R§TIOG e R§TPOG.

