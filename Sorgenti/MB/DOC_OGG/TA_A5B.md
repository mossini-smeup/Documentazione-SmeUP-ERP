# A5B - Causali cespiti
 :  : DEC T(ST) K(A5B)
## OBIETTIVO
Descrive le causali con cui si eseguono i movimenti sui cespiti
## SOTTOSETTORE
Da non impostare.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Codice**
Indica il codice della causale
 :  : FLD T$5,01
È un valore V2 A5TOT :  definisce il totalizzatore interessato dai movimenti con questa causale
 :  : FLD T$5,02.T$5,01
 :  : FLD T$5,03.T$5,01
 :  : FLD T$5,04.T$5,01
 :  : FLD T$5,05.T$5,01
 :  : FLD T$5,06.T$5,01
 :  : FLD T$5,07.T$5,01
 :  : FLD T$5,08.T$5,01
 :  : FLD T$5,09.T$5,01
 :  : FLD T$5,10.T$5,01
 :  : FLD T$5,11.T$5,01
 :  : FLD T$5,12.T$5,01
 :  : FLD T$5,13.T$5,01
 :  : FLD T$5,14.T$5,01
 :  : FLD T$5,15.T$5,01
 :  : FLD T$5,16.T$5,01
 :  : FLD T$6,01
È un valore V2 SEGNO :  definisce se il valore del movimento si somma o si sottrae dal totalizzatore corrispondente
 :  : FLD T$6,02.T$6,01
 :  : FLD T$6,03.T$6,01
 :  : FLD T$6,04.T$6,01
 :  : FLD T$6,05.T$6,01
 :  : FLD T$6,06.T$6,01
 :  : FLD T$6,07.T$6,01
 :  : FLD T$6,08.T$6,01
 :  : FLD T$6,09.T$6,01
 :  : FLD T$6,10.T$6,01
 :  : FLD T$6,11.T$6,01
 :  : FLD T$6,12.T$6,01
 :  : FLD T$6,13.T$6,01
 :  : FLD T$6,14.T$6,01
 :  : FLD T$6,15.T$6,01
 :  : FLD T$6,16.T$6,01
 :  : FLD T$A5BA **Tipo movimento**
È un valore V2 A5TMO :  definisce la tipologia a cui apppartiene il movimento e che viene utilizzata dall'applicazione.
 :  : FLD T$A5BB **Inizializzazione movimento**
È un elemento della tabella A5W :  definisce il 'corredo' dei movimenti con questa causale :  livello di nascita, gruppi flag, categoria parametri, parametri impliciti, contenitore note.
 :  : FLD T$A5BC **Causali collegate**
È un elemento della tabella A5G :  quando si esegue un movimento con questa causale, verranno eseguiti in automatico tanti movimenti quante sono le causali impostate nella tabella A5G :  va impostato in movimenti di vendita/alienazione, nei quali, oltre al movimento manuale, vanno eseguiti movimenti di plus/minusvalenza, capitale/fondo alienato o venduto, ecc...
 :  : FLD T$A5BD **Suffisso pgm aggiustamento**
Se presente, viene eseguito il programma di aggiustamento A5A5B0_xxx.
Da utilizzare per indrodurre comportamenti standard.
