# OBIETTIVO
Questo fornisce una gestione completa e Sme.UP oriented, dei lavori di un utente.

# Dettaglio

Viene presentato l'elenco dei lavori raggruppato per "gruppo".
Il gruppo corrisponde a vari job dell'as400 "correlati" tra loro.
Questo perchè le connessioni sui device loocup, web o mobile, comportano l'impiego di più job as400 che qui vengono appunti raggruppati in base alla connessione di cui sono serventi.
In questo pannello vengono inoltre mostrati JOB che sono normalmente sono più "nascosti",
ad esempio i QZRCSRVS e QZHQSSRV.

Per ogni lavoro abbiamo le seguenti informazioni di colonna : 
* Nome lavoro :  nome del job as400
* Utente      :  utente del job as400
* Numero      :  numero del job as400
* Stato       :  stato del job as400
* Gruppo      :  è numero di job attraverso cui viene identificato una particolare connessione.

# Significato particolare di alcuni JOB
## QZRCSRVS
I JOB QZRCSRVS sono quelli che gestiscono le Program Call fatte dal client.
Quindi sono i JOB in cui bisogna mettersi in debug per debuggare le chiamate fatte al JAJAC0.
## QZHQSSRV
I JOB QZHQSSRV gestiscono altre chiamate fatte dal client.
Questi JOB non eseguono programmi Sme.UP, quindi non c'è l'esigenza di mettersi in debug su questi.
Sono inseriti in questo elenco per due motivi :  per poterli chiudere facilmente nel caso si vogliano
chiudere tutti i JOB di un certo utente e perché nel JOBLOG contengono l'IP del client da cui
ci si sta collegando.
Questo JOB (per motivi tecnici) risulta sempre inserito in un gruppo separato. Normalmente
"appartiene" al gruppo immediatamente precedente.

# Opzioni di riga

Su tutte le righe possono essere eseguite le seguenti azioni : 
* 02 = Modifica lavoro (corrispondente al comando CHGJOB)
* 03 = Congela lavoro (corrispondente al comando HLDJOB)
* 04 = Fine lavoro (corrispondente al comando ENDJOB)
* 44 = Fine lavoro cieco (corrispondente al comando ENDJOB, ma senza richiesta interattiva)
* 05 = Gestione lavoro (corrispondente al comando WRKJOB)
* 06 = Rilascio lavoro (corrispondente al comando RLSJOB)
* SS = Avvio diagnosi su un lavoro (corrispondente al comando STRSRVJOB)
* ES = Fine lavoro di manutenzione (corrispondente al comando ENDSRVJOB)
* SD = Avvio debug (corrispondente al comando STRDBG)
* ED = Fine modo debug (corrispondente al comando ENDDBG)
* SJ = Avvio diagnosi + Avvio debug
* EJ = Fine diagnosi + Fine modo debug
* RL = Chiude tutto :  Fine diagnosi + riacquisizione risorse + riacquisizione actgrp

# Tasti funzione

F14=Cambia utente, mi permette di cambiare l'utente di cui sto analizzando i job
F15=Cambia filtri, mi permetti di cambiare il filtro applicato ai job che vengono visualizzati :  di default si vedono solo i lavori attivi ed i coda, con 1 posso vedere solo gli attivi, con 2 posso vederli tutti.

