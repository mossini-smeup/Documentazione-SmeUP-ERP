### Lista degli attributi
 - £JaxT1 (Tipo=" ")
 - £JaxP1 (Parametro=" ")
 - £JaxK1 (Codice=" ")
 - £JaxD1 (Testo=" "). Se assente e si tratta di un oggetto viene assegnata la decodifica dell'oggetto
 - £JaxOP (Exec="F(;;) 1(;;) P()"). Facoltativa. Nella forma standard dell'oggetto J1FUN.
 - £JaxNM (Nome=" "). Pprefisso per le variabili associate a tale nodo
 - £JaxLF (Leaf="Yes/No"). Se presente "Yes" in un albero ad espansione dinamica non appare il simolo di espansione (carattere +)
 - £JAXEN Chiusura. '/>' se non ci sono sottolivelli, '>' per aprire un nuovo livello
 - £JAXFL (Fld=" "). Lista dei campi con separatore come per le righe di una matrice
     ATTENZIONE :  Per poter utilizzare la £JAXFL è necessario definire la lista dei campi della griglia tramite l'istruzione £JAXSWK e
                           successivamente £JAX_AGRI come per la matrice.


### Funzioni
 - £JAX_ADDO Aggiunge un nodo all'albero
 - £JAX_CLOO Chiude il livello precedente

### Esempio di compilazione
Riportiamo il codice RPG per ottenere l'alebro che segue : 
> L(LET) C(A)
A
. B :  Pippo
. C
D

EVAL  £JaxK1='A'
EVAL  £JaxEN='>'
£JAX_ADDO
EVAL  £JaxK1='B'
EVAL  £JaxD1='Pippo'
EVAL  £JaxEN='/>'
£JAX_ADDO
EVAL  £JaxK1='C'
EVAL  £JaxEN='/>'
£JAX_ADDO
£JAX_CLOO
EVAL  £JaxK1='D'
EVAL  £JaxEN='/>'
£JAX_ADDO

