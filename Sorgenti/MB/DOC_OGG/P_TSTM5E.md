## Applicazione suggerimenti
Questa copy riceve il record del consiglio
 :  : DEC T(OJ) P(*FILE) K(M5CONS0F)
che ha il tipo suggerimento 'AE' o 'PN'.
L'MRP riempie, in questo record, il campo parametro suggerimento
 :  : DEC T(VO) P(F.M5CONS0F) K(H§PRSU)
Il programma della /copy esegue il programma contenuto nelle prime dieci posizioni del parametro suggerimento. Le posizioni successive sono riservate per ulteriori parametri specifici di ogni programma di lancio (ad esempio elementi di tabelle, ecc...)
I programmi forniti a standard sono i seguenti : 
 :  : DEC T(OJ) P(*PGM) K(M5PNP5_SM)
 :  : DEC T(OJ) P(*PGM) K(M5PNVR_SM)
 :  : DEC T(OJ) P(*PGM) K(M5PNP5_SM)
E' fornito inoltre uno scheletro per realizzare programmi specifici, ad esempio per interfacciarsi con applicazioni esterne.
 :  : DEC T(MB) P(M5SRC) K(XXM5D0)
In essi non ci si deve far carico di aggiornare il record del consiglio, ma solamente di modificare i campi opportuni (quantità di rilascio, ecc..) e ritornare nel messaggio l'informazione se l'applicazione è stata eseguita.
E' il programma della /copy
 :  : DEC T(OJ) P(*PGM) K(M5M5E0)
che aggiorna i campi generali del consiglio (stato, livello, quantità, ecc..) in base a quanto impostato nel programma di applicazione specifico.
L'aggiormanento fisico dell'archivio deve essere eseguito dal programma che ha lanciato la copy £M5E, con la DS del record che quest'ultima gli ha ritornato (sempre se l'applicazione è stata eseguita).








