# EDC - Metodi di comunicazione
## OBIETTIVI
Definire il ricevitore inteso come supporto fisico (file, cartella,stampa, etc.)
## SOTTOSETTORI
Non gestiti
## INTRODUZIONE
L'elemento di tabella è il codice del metodo di comunicazione.
Una volta definito, viene successivamente associato al codice indirizzo (EDI) per permettere l'attribuzione univoca indirizzo/metodo.
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC Descrizione
 :  : FLD T$EDCA __Metodo__
*PRT      Stampare i messaggi.
*WRK      In ricevitore di lavoro.
*FLR      Cartella PCS.
*DIR      In ricevitore destinatario.
*RMT      Invio a sistema remoto.
*LOO      Richiesto da LOOC.up.
*PGM      Attraverso la chiamata di un programma esterno.

 :  : FLD T$EDCB __Parametro del metodo__
Nome file di stampa o nome libreria.
Nel caso di metodo *PGM il parametro contiene il nome della libreria/programma che verrà chiamato
durante la trasmissione del messaggio nell'esecuzione della £EDT. Il parametro libreria può contenere
*LIBL oppure il nome di una libreria specifica.
E' disponibile il prototipo del programma chiamato nel membro EDFUC0T_XX.
