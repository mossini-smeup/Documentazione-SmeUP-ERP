# La scheda RETELE

## Premesse

- Il file RETEL0F contiene le chiamate passate per il server CUBE05 (server di Swyx).
- Viene aggiornato tramite il pulsante **Aggiorna Telefonate** presente sulla scheda


## Scheda RETELE
La scheda RETELE è composta da alcune sottoschede : 

- **Analisi Telefonate** che permette di filtrare il contenuto del file RETEL0F per Data, Ente mittente e destinatario, per numero mittente e destinatario. E' la sottoscheda fondamentale
- **Analisi numeri sul RETELE0F** che visualizza l'intero contenuto del file RETEL0F (il caricamento sarebbe da ottimizzare con la paginazione)
- **Analisi numeri sul BRESCO0F** che analizza il contenuto dei numeri telefonici del BRESCO0F (ha ancora ragione di esistere? - era solo per test)


### Il pulsante Aggiorna Telefonate
Richiama il programma RETEL_01 che legge dal file SWYX delle telefonate e scrive il file RETELE0F. Nel momento dell'importazione si occupa anche di decodificare il numero in questione in questo modo : 

- cerca sulla tabella BR*IN (tabella dei numeri interni) per controllare se è un numero di interno; nel caso retituisce anche CNCOL + il  codice collaboratore a cui il numero risulta associato.
- se la radice del numero in questione è uguale alla radice telefonica aziendale (parametro AWI della categoria £CA legato all'azienda) allora estrae le cifre presenti dopo questa radice ed esegue le stesse operazioni sopra dette
- cerca sulla tabella V§*PS per controllare se è un numero speciale (112, 113, 118 etc...)
- se non è niente di tutto ciò allora utilizza la G85 per decodificare il numero in questione e, oltre a farsi restituire la descrizione del numero, recupera anche il tipo+parametro e il codice ente intestatario del numero. __La G85 che effettua queste operazioni è ancora lenta (nonostante l'aggiunta del logico BRESCO4L con chiave numero telefonico); sarebbe utile controllare le performance della stessa per capire come poter velocizzare la decodifica del numero di telefono.


### Il pulsante Aggiorna Riferimenti
Richiama il programma RETEL_01 che scorre il file RETELE0F per decodificare i numeri telefonici non ancora decodificati.
Questa procedura va lanciata per allineare il file, __attenzione però che potrebbe durare parecchio tempo

### Il servizio LOSER_26
Il servizio LOSER_26 viene richiamato quando si riceve una telefonata sul proprio PC; anche qui è stata aggiunta la routine di decodifica del numero in modo che la decodifica compaia sulla finestra.

## Problemi riscontrati
Oltre alla lentezza riscontrata nella decodifica dei numeri durante l'importazione dei dati, sono stati riscontrati errori sul file di partenza (quello che scrive SWYX sul server CUBE05).

- manca il numero telefonico del mittente o del destinatario
- il numero mittente è solo +39
- il numero mittente è +39005
- il numero mittente è +1005
- il numero mittente è "sip : 991@172.16.3.133" o "sip : 997@172.16.3.133" o "sip : 999@172.16.3.133"; cosa significa?
- il numero mittente è "sip : 396898563098@psi"; cosa significa?
- il numero mittente è "conference"; cosa significa?
- il numero destinatario è "---" o "-" o "--"; cosa significa?
- il numero mittente è "-conference-"; cosa significa?


## Punti Aperti

- Il programma B£G85G presente adesso in P_SVI utilizza solo il campo numero telefono (sottostringa di S§DESE dalla posizione 41 per 17 caratteri) ed è quindi in grado di decodificare solamente i numeri fissi. Il concetto dovrà essere esteso anche per gli altri tipi indirizzo.
- dato il limite descritto sopra, i programmi RETEL_01 e LOSER_26 decodificano per ora solo i numeri fissi (quelli cioè presenti nella sottostringa S§DESE dalla posizione 41 per 17 caratteri)



**In P_SVI è presente anche il B£OA_IN a cui sono stati aggiunti alcuni OAV (restituzione del prefisso internazionale e nazionale, restituzione del numero senza prefisso internazionale).

