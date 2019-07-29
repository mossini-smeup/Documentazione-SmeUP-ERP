# Introduzione
Le funzioni sono operazioni che possono essere specificate direttamente nel codice e che vengono precedute sempre dal carattere %.
> T( Esempio)
.    C                   IF        %SUBST(AAA030 : 2 : 1)='='

In questo caso non c'è più bisogno di utilizzare una variabile di appoggio.

# Su stringhe
 * **%LEN**,ritorna la lunghezza di una variabile
 * **%REPLACE(str_sostituente,str_originale,parti_da,quanti_caratteri)**, Sostituisce una stringa all'interno di un'altra, permettendo di specificare da che posizione partire e quanti caratteri sostituire.
 * **%SCAN(str_ricerca  :  str_origine  :  a_partire_da)**, scansione stringa Es. :  EVAL POSIZ=%SCAN('PP' : 'PIPPO')       POSIZ avrà valore 3
 * **%SUBST(stringa : inizio : lunghezza)**, estrae una sottostringa e può essere utilizzata anche per modificare delle variabili Es.  EVAL %SUBST(VAR : 3 : 4)='****'       Se inizialmente VAR conteneva ABCDEFGHIL, ora EVAL conterrà AB****GHIL
 * **%TRIM(stringa)**, elimina eventuali spazi presenti all'inizio e alla fine della stringa
 * **%TRIML(stringa)**,  elimina eventuali spazi presenti all'inizio della stringa
 * **%TRIMR(stringa)**,  elimina eventuali spazi presenti alla fine della stringa

# Numeriche
 * **%ABS**, ritorna il valore assoluto
 * **%CHAR**,  trasforma un numerico in stringa
 * **%INT**, ritorna la parte intera arrotondata all'inferiore
 * **%INTH**, come %INT, ma con arrotondamento al valore più vicino

Le seguenti funzioni si applicano alla divisione tra due numeri interi : 
 * **%DIV**, ritorna la parte intera del risultato
 * **%REM**, ritorna il resto (intero)

# Su lunghezza campi e schiere
 * **%ELEM**, ritorna il numero di elementi di una schiera ed è utile per evitare errori di indice schiera, senza definire 'tappi'.
>.     C                   CLEAR                 $X
.     C                   DO        *HIVAL
.     C                   ADD       1           $X
.     C                   IF        $X>%ELEM(SCK)
.     C                   LEAVE
.     C                   ENDIF
.     C                   ....
.     C                   ENDDO


 * **%SIZE**, ritorna la lungezza (in byte) di un campo o di una costante
 * **%DECPOS**, ritorna il numero di decimali (in byte)
 * **%XFOOT**, somma il contenuto di una schiera

# Su archivi
 * **%EQUAL**, è vera se il posizionamento ha trovato un record con la chiave specificata.

>.     C     KYTRA2        SETLL     C5TRANR
.     C                   IF        %EQUAL
.     C     KYTRA2        CHAIN     C5TRANR
.     C                   ENDIF


 * **%FOUND**, è vera se è stato trovato un record

>.     C     KYTRA2        CHAIN     C5TRANR
.     C                   IF        %FOUND
.     C                   MOVEL     W5REC         £C52RE                                  .
.     C                   ENDIF


 * **%EOF** (End Of File), è vera se si è arrivati alla fine del file

>.     C     KYMOAN        READE     C5MOANR
.     C                   IF        %EOF
.     C                   MOVEL     'FINE'        £C52MS                                         .
.     C                   ENDIF


Per usare queste funzioni negate, la sintassi è : 

>.     C                   IF        NOT(%EOF)
.     C                   IF        NOT(%FOUND)


 * **%OPEN**, permette di controllare se un file è aperto o meno, rendendo inutile l'utilizzo di una variabile per il controllo di una apertura condizionale del file

>.     C                   IF        %OPEN(nomefile)
.     C                   IF        NOT %OPEN(nomefile)

