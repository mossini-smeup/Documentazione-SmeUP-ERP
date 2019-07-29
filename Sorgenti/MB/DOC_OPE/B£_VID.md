#Generalità
Tutti i formati video usati nelle applicazioni Sme.up hanno un layout con caratteristiche standard : 

- struttura del formato (testata, corpo, piede);
- tipologie di formato (guida, lista, dettaglio, stampe, parametri stampa, )
- sequenza di presentazione


# Struttura di un formato video
Normalmente un formato video è costituito da : 

- **testata** (la parte in alto);
- **corpo** (la parte centrale);
- **piede** (la parte in basso).


![B£BASE_059](http://localhost:3000/immagini/MBDOC_OPE-B£_VID/BXBASE_059.png)
**1. Testata**
È costituita dalle prime due righe in alto della videata, contiene una serie di informazioni standard : 

- >PRIMA RIGA      -->   Nome azienda, Carattere speciale> ">" , Nome funzione, Nome sistema, Nome programma (questo nome deve essere citato nelle comunicazioni tecniche verso l'ente di supporto Sme.up ed è il riferimento per accedere alla documentazione)

- > SECONDA RIGA      -->   Data, Posizionamento (vedi di seguito), Tipo formato, Nome stazione di lavoro, Utente (il codice utente viene utilizzato come chiave per la memorizzazione dei dati di impostazione/selezione, inseriti a video)


**2. Corpo**
È la parte centrale della videata e contiene i dati caratteristici della funzione e del tipo formato.

**3. Piede**
Sono le ultime tre righe in basso della schermata e contengono : 

- ELENCO COMANDI    -->    due caratteri >">>" a destra significano che con il comando >F24 è possibile visualizzare in forma completa ed estesa tutti i comandi ammessi;
- MESSAGGI    -->    appare la forma ridotta del primo messaggio di errore. Mediante il comando >F22 è possibile accedere a tutti i messaggi e per ognuno alla sua forma estesa.


# Tipologie di formato
I formati video possono essere classificati nelle seguenti tipologie : 

- guida
- gestione
- selezione
- dettaglio
- parzializzazioni
- impostazioni di stampa
- parametri esecuzione
- messaggi


## Formato guida
Guida alle funzioni (immissione, modifica, copia, cancellazione, ecc...) abilitate per l'oggetto.
Nel formato guida si può definire l'opzione di scelta della funzione da eseguire e passare direttamente al formato di dettaglio per la gestione (in questo caso si devono anche inserire i dati relativi all'oggetto cui applicare l'azione).


![B£BASE_060](http://localhost:3000/immagini/MBDOC_OPE-B£_VID/BXBASE_060.png)
## Lista di gestione
Su questa videata viene mostrata la lista degli oggetti sui quali è possibile eseguire una delle attività alle quali l'utente è abilitato.
E' possibile selezionare più oggetti per la stessa o per diverse attività :  il sistema proporrà la videata di dettaglio per ciascun record selezionato.
La lista può essere ridotta solo ai record di interesse utilizzando le parzializzazioni; se già attive, viene evidenziato il corrispondente comando funzione in reverse image.


![B£BASE_061](http://localhost:3000/immagini/MBDOC_OPE-B£_VID/BXBASE_061.png)
## Lista di selezione
È del tutto simile alla lista di gestione, ma sono attive solo le funzioni di scelta ed eventualmente di visualizzazione del dettaglio.

## Dettaglio
È la videata attraverso la quale si esegue l'attività richiesta :  vengono evidenziati (per immissione, modifica o visualizzazione, in base all'opzione scelta) i campi di dettaglio del record selezionato, permettendo l'accesso alle ulteriori funzioni, mediante gli appositi campi di input o comandi.
In particolare possono essere attivate le seguenti funzionalità standard : 

- **memorizzazioni multiple**    -->   la presenza di una carattere >>>** in alto a destra, indica la possibilità di memorizzare e quindi riprendere alcune videate ripetitive;
- **funzioni per oggetto**    -->     premendo >F10**, se abilitato, si accede alla funzione "%", tipica dell'oggetto, mediante la quale si possono richiamare tutte le funzioni ad esso associate;
- **note strutturate**     -->    se presente il campo >__** in basso a destra, è possibile passare alla gestione delle note strutturate.


![B£BASE_059](http://localhost:3000/immagini/MBDOC_OPE-B£_VID/BXBASE_059.png)
## Parzializzazioni
Con questa schermata si limitano / ricercano i record da presentare nella lista.
Se presente l'ordinamento, si definisce anche il modo con cui i record selezionati saranno ordinati.
Per ragioni di performance, scegliendo ordinamenti diversi da quello di default, vengono prestese anche le opportune parzializzazioni (es. :  nella videata di parzializzazione dei centri di lavoro, se si vuole ordinare per centro di costo, deve essere impostata una parzializzazione per centro di costo).
Se presente lo schema, si possono scegliere i campi da visualizzare in lista.
Se presente la scansione, la ricerca dei record da presentare può essere fatta anche per caratteri contenuti nel codice (es. :  inserendo *AUT* nella scansione descrizione, vengono presentati tutti i centri di lavoro che hanno le 3 lettere >AUT all'interno dela descrizione).
Alcune gestioni richiedono l'utilizzo di parzializzazioni superiori a quelle consentite da una unica videata di selezione :  in questi casi con >F13__ si passa alle __"Altre parzializzazioni".
Tutte le parzializzazioni impostate possono essere identificate con un codice identificativo e memorizzate.
- [Gestione Dati Scelte Video](Sorgenti/MB/DOC_OGG/P_B£MDV0)

![B£BASE_062](http://localhost:3000/immagini/MBDOC_OPE-B£_VID/BXBASE_062.png)
## Impostazione di una stampa
L'impostazione di una stampa inizia abitualmente con la richiesta del tipo di output (carta, video o trasferimento a personal computer).
Normalmente un formato di stampa è un insieme di diverse impostazioni : 

- Ordinamento
- Parzializzazioni
- Schema
- Scelta valori
- Periodicità

Ciascuna di queste impostazioni può essere memorizzata singolarmente per essere riutilizzata in diversi tipi di stampe.
Anche l'insieme delle impostazioni di una stampa può essere memorizzato.
- [Gestione Dati Scelte Video](Sorgenti/MB/DOC_OGG/P_B£MDV0)

![B£BASE_063](http://localhost:3000/immagini/MBDOC_OPE-B£_VID/BXBASE_063.png)
Si rimanda al documento _2_"STAMPE" per ulteriori dettagli.

## Richiesta parametri di esecuzione
Normalmente le elaborazioni di funzioni che trattano masse di dati vengono eseguite in modo batch (tipico esempio sono le stampe di rapporti) e permettono di intervenire manualmente per cambiare i parametri di elaborazione preimpostati in fase di programmazione.
Queste modifiche possono essere fatte attarverso la schermata standard di gestione dei parametri di esecuzione, a cui si accede mediante il comando funzione >F11.

![B£BASE_064](http://localhost:3000/immagini/MBDOC_OPE-B£_VID/BXBASE_064.png)
## Messaggi
Nelle operazioni di modifica il sistema esegue contemporaneamente i controlli sui dati di input e può emettere dei messaggi di errore, il primo dei quali viene visualizzato in alta intensità sul piede della schermata. I messaggi possono essere visualizzati o gestiti (aggiungendo informazioni particolari) mediante il comando funzione >F22.

# Sequenza delle videate
Le funzioni di gestione degli archivi partono normalmente da un formato guida e permettono di arrivare direttamente al dettaglio, oppure a partire da un formato di lista.
Le parzializzazioni possono essere impostate sia dal formato guida che dal formato lista.

# Altri standard
Nella definizione delle videate sono state utilizzate alcune convenzioni : 

- **Opzione**    -->    è un campo (normalmente di due caratteri) in cui l'utente può inserire l'opzione desiderata fra quelle esposte (in quanto autorizzate). Inserendo il carattere >"/" nel campo opzione, è possibile accedere al dettaglio delle autorizzazioni e, se abilitati, a modificarle.

- **.. >>**    -->    indica che, inserendo un carattere nel campo, è possibile accedere ad un ulteriore formato video.

- **Posizionamento**    -->    se presente all'inizio della seconda riga, permette di visualizzare la lista sottostante a partire dal valore inserito. I caratteri utilizzati nel posizionamento dipendono dall'ordinamento scelto e normalmente corrispondono a quelli del codice oggetto o della sua descrizione.

- **>**    -->    (su prima riga dopo il nome dell'azienda o può essere visualizzato in reverse image nel formato dettaglio) se presente, premendo >F22 vengono visualizzate le tabelle utilizzate dal programma.
Tale funzione è attiva se scelta in impostazione della tabella >B£2.

- **Memorizzazioni**    -->    se presente un campo di immissione sottolineato e costituito da uno o 8 caratteri a destra, normalmente sulla terza riga in alto.

