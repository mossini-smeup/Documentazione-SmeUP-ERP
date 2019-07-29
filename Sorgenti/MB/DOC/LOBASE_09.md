# SETUP GRAFICO DI FUNZIONE (CAMPO SG)

L'opzione SG() all'interno della sintassi di funzione consente di specificare una serie di setup specifici per l'esecuzione della funzione all'interno del client grafico Looc.Up.
o nei parametri.

# Utilizzo

La sezione SG è suddivisa in sottosezioni che identificano specifiche famiglie funzionali.

##  Gestione funzioni ad esecuzione lenta

L'esecuzione di una funzione all'interno di Looc.Up può in alcuni casi richiedere tempi lunghi o comunque non compatibili con i tempi attesi dall'utente del client grafico. Il caso tipico è quello di funzioni di interrogazione che richiedono l'elaborazione di molti dati per poter produrre un risultato finale.
Attraverso l'utilizzo del setup grafico è possibile mostrare un messaggio di warning prima che una funzione venga eseguita in modo che l'utente finale venga informato della pesantezza della funzione che sta richiedendo e possa decidere di abbandonare la richiesta nel caso ritenga di non dover aspettare la risposta.

Attraverso l'utilizzo del campo SG è quindi possibile : 

- Visualizzare un messaggio prima che la funzione venga eseguita. Per default il messaggio segnala la richiesta di esecuzione di una funzione lenta ma il messaggio emesso può essere personalizzato a piacere inmodo da segnalare anche situazioni diverse. A seguito della visualizzazione del messaggio l'utente può decidere per l'esecuzione dello stesso o può decidere di abbandonare la richiesta per non dover attendere la fine esecuzione.
- Attivare un meccanismo di cache che consenta la memorizzazione della richiesta in fase di esecuzione. L'utente può decidere di eseguire la funzione potenzialmente lenta salvando il risultato della funzione in una cache temporanea. La cache potrà poi essere riutilizzata in una esecuzione futura per evitare di dover rieseguire la funzione lenta per avere gli stessi risultati. L'opportunità o meno di utilizzare questo meccanismo di cache sarà valutata dal fornitore del servizio in base alla natura del servizio stesso.

I parametri disponibili nella sezione SG sono i seguenti : 

- **SlowF** :  se Yes viene visualizzato un messaggio di avviso di funzione lenta prima dell'esecuzione della funzione stessa. Se No o vuoto non viene visualizzato nulla.
- **Msg** :  se è attiva la visualizzazione del messaggio, consente di specificare il messaggio da visualizzare. Se non definito viene mostrato un messaggio di default che segnala la richiesta di esecuzione di una funzione lenta.
- **Cache** :  se Yes, alla prima esecuzione della funzione viene offerta all'utente la possibilità di salvare in cache il risultato della funzione stessa. Nelle esecuzioni successive viene proposta all'utente la possibilità di eseguire la funzione riutilizzando il risultato precedentemente salvato in cache.

## Esempio di utilizzo

Un esempio di utilizzo del campo SG è rappresentato nella seguente funzione di esempio : 

F(EXB;B£SER_02;COM.MAT) **SG(SlowF(Yes) Msg(La funzione richiesta può richiedere tempi di esecuzione molto lunghi.) Cache(Yes))






