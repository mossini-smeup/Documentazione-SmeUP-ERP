# Generalità
Sia in emulazione 5250 che in loocup è disponibile il cruscotto di verifica di Looc.UP
In emulazione questo coincide con il richiamo al UP SME, mentre in loocup alla combinazione di CTRL+F9, dalla scheda utente e dal relativo capitolo.

# Struttura
Il cruscotto e suddiviso nei seguenti argomenti : 
* Coda lavoro
* Libreria
* Sottosistema
* Impostazioni
* Host server
* SmeNS
* Ambienti
* Utente

## Coda lavoro
Vengono verificate l'esistenza delle code B£QQ99 e B£QJ01 e della loro associazione ad un sottosistema attivo

## Libreria
Viene verificata l'esistenza della libreria SMEUPUIDQ e alla sua autorizzazione.

## Sottosistemi
Viene verificata l'attivazione dei seguenti sottosistemi : 
* QSYSWRK  System subsystem
* QBATCHUI Looc.UP batch subsystem
* QBATCH   Batch subsystem
* QINTER   Interactive subsystem

## Impostazioni
Le impostazioni risiedono nella tabella UI1 da cui viene verificata la coda di lavoro.
La stessa deve esistere e associata ad un sottosistema attivo con una definizione di lavori *NOMAX.

## Host Server
Vengono verificati che i seguenti demoni siano attivi : 
* QZDASRVSD Database
* QZHQSRVD  Data queue
* QZSCSRVSD General
* QZRCSRVSD Remote comand
* QZSOSGND  Signon

## SmeNS
Viene verificata l'attivazione dei log e l'esistenza del percorso di salvataggio

## Ambienti
Vengono evidenziati i soli ambienti incompatibili con la JOBD associata al profilo utente.

## Utente
Viene verificato che l'utente sia presente nella tabella B£U, sia abilitato e non abbia anomalie nell'elenco librerie iniziale.
