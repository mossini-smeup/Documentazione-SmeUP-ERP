# OBIETTIVO
Costruisce i popup di esplorazione.

# FUNZIONI
Le funzioni sono sempre eseguite con i motodi : 
- POS posizionamento e lettura
- LET lettura
Viene tornato il messaggio 'CONT' o 'FINE'

# FUNZIONI
## MOD
Esplorazione interna per modulo.
Si imposta il modulo, e, se è un modulo naturato, anche il tipo/par/codice oggetto da cui deriva la natura (ad esempio, per il modulo V5DOCU, si imposta il tipo documento :  TA/V5D/xxx (dove xxx è il tipo documento).

## OGI
Esplorazione interna per oggetto.
Si imposta il tipo/parametro e codice dell'oggetto.

## OGE
Esplorazione esterna per oggetto
Si imposta il tipo/parametro e codice dell'oggetto.
Questa funzione comprende l'esplorazione esterna di tutti gli oggetti (anche i moduli).
Vengono ritornate alternativamente, le applicazioni e le esplorazioni di quella applicazione.

## OGA
Esplorazione esterna per oggetto / applicazione
Si imposta il tipo/parametro e codice dell'oggetto.
E'simile alla funzione OGE, ma vengono tornati soli i nodi delle applicazioni.

## OGM
Esplorazione esterna per oggetto /applicazione
Si imposta il tipo/parametro e codice dell'oggetto, e l'applicazione
E'simile alla funzione OGE, ma vengono tornati soli i nodi delle funzioni sottostanti all'applicazione impostata.

## PAS
Si imposta il tipo/parametro e codice dell'oggetto.
Vengono tornate le funzioni di GO dell'oggetto impostato.

