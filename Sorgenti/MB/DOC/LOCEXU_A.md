La matrice di aggiornamento (EXU) è un componente di LOOC.up strettamente legato alla matrice (EXB).
Non è un componente provvisto di grafica e ha come compito principale quello di gestire lo scambio di informazioni tra una matrice in modalità NON readonly (che può quindi essere usata per inserire, modificare, cancellare records) e l'AS.
La matrice di aggiornamento tiene traccia delle modifiche eseguite in modo da poterle annullare / confermare.

# Interazione client-server :  passaggi fondamentali
Consideriamo per semplicità un'operazione su una singola riga di matrice.
Tale riga (costituita da più campi) può rappresentare molte cose, come : 

- un record di file di dati, di Sme.up o meno
- un singolo campo (ad esempio in modalità codice, valore, descrizione)
- un elemento di tabella
- una riga di script
- un pezzo di documentazione attiva
- ...


L'operazione di inserimento/modifica/cancellazione avviene in 3 passi

- Passaggio in XML degli estremi dell'operazione dal client (la matrice EXU) al servizio AS.
- Esecuzione dell'operazione da parte del servizio (controlli, eventuale scrittura).
- Risposta in XML dal servizio al client, aggiornamento visualizzazione.


# Considerazioni
## Controlli di consistenza
Non sempre è possibile garantire che i dati visualizzati prima di un aggiornamento siano consistenti con quelli effettivamente salvati su AS.
Questo si ottiene di solito imponendo un lock al momento della visualizzazione, ma non sempre è possibile / auspicabile farlo (ad esempio perchè una matrice potrebbe rappresentare molti record e non si può bloccarli tutti).
In assenza di lock e quando è importante che i dati siano sempre aggiornati al momento dell'esecuzione di un'operazione di inserimento/modifica/cancellazione il servizio può garantire la consistenza del/dei record in modifica comparando i valori che il client crede di aggiornare con quelli effettivamente salvati su AS, segnalando errore e imponendo il refresh della matrice.

## Messaggi di errore
Se a seguito dei controlli effettuati dal servizio si rilevano errori, il servizio può segnalare al client (e questo all'utente) tali errori "accendendo" la visualizzazione di errore su uno o più campi della matrice e passando uno o più messaggi di errore (generici o di campi). Di questi messaggi, a cui è associata una gravità, verrà visualizzato il più grave.

## Ricerche specifiche
Normalmente le ricerche sui campi modificabili sono le stesse che in tutto Looc.up; è, tuttavia, possibile implementare e attivare ricerche particolari che tengano conto del contesto in cui vengono eseguite; si può, ad esempio, sostituire le ricerche normali con programmi personali che presentino dei dati tenendo conto dei valori degli altri campi del record che si sta aggiornando.

## Casi particolari
Normalmente non è possibile eccedere la lunghezza definita sul campo di aggiornamento.
Se il campo è una voce (oggetto VO) dinamico (parametro deriato da altro campo) la lunghezza del campo in imputazione non verrà controllata.
Il controllo in questo caso deve essere eseguito nel servizio di update.
