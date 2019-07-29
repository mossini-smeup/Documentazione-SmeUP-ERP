# Obiettivo
Permettere la gestione completa dei dati contenuti nella F.M.E.A.

Nel caso in cui si effettui l' annullamento, a scalare verranno annullati i dati logicamente legati alla testata,
ovvero : 
 * Righe del documento (Componenti)
 * Difetti
 * Effetti del Difetto
 * Cause del Difetto

## Modalità operative
Il programma si comporta differentemente in funzione della modalità di ingresso : 
 * _2_Gestione FMEA, permette la modifica o la cancellazione dei dati della FMEA
 * _2_Revisione FMEA, permette di selezionare una richiesta di FMEA per richiedere delle azioni correttive necessarie per la riduzione delle priorità (FMECA)

## Formato guida
![CQ_FMEA_14](http://localhost:3000/immagini/MBDOC_OGG-P_CQFM20/CQ_FMEA_14.png)
## Formato selezione difetto per inserimento azioni correttive
![CQ_FMEA_15](http://localhost:3000/immagini/MBDOC_OGG-P_CQFM20/CQ_FMEA_15.png)
Il progettista sceglierà la causa con priorità di rischio maggiore, ed a questa collegherà una serie di informazioni e di operazioni da farsi. Data una causa il programma mette a disposizione una serie di campi in cui specificare : 
 * sperimentazioni eseguite, l'utente può interrogare le richieste di intervento per cercare se è già stato gestito in azienda una problematica che possa colleagarsi con quanto stà analizzando;
 * rapporti di prova, il progettista può richiedere di effettuare determinati rapporti di prova;
 * misure previste, ci si collega alla tabella  CQ*MP da cui possono venire selezionate ed aggiunte le misure previste allo scopo di abbassare l'indice di priorità di rischio;
 * obiettivo, il progettista può specificare l'obbiettivo che ci si prefigge di raggiungere con l'attuazione di quelle misure;
 * azione correttiva, il progettista si può collegare con il modulo di immissione delle richieste di intervento per effettuare la richiesta di azione correttiva dove specificherà l'ente designato, la problematica ecc..;
 * ente designato, per la gestione di questa causa;
 * stato dell'intervento, che all'inizio sarà da evadere;
 * data evasione proposta.

L'ente designato per la gestione dell'azione correttiva può interrogare la FMEA che ha originato la richiesta e prendere le successive decisioni.

In seguito, l'ente designato per la gestione della FMECA può a sua volta interrogare il campo "AZIONE CORRETTIVA"   per vedere se l'azione è stata evasa ed in caso affermativo valutare quanto effettuato e quindi completare la gestione dei campi : 
 * soluzione adottata;
 * procedura adottata;
 * esito soluzione adottata;
 * tipo intervento.

## Formato immissione azione correttiva
![CQ_FMEA_16](http://localhost:3000/immagini/MBDOC_OGG-P_CQFM20/CQ_FMEA_16.png)
La terza fase consiste nella ridefinizione degli indici di priorità di rischio sulla base delle azioni effettuate : 

## Formato valutazione rischi
![CQ_FMEA_17](http://localhost:3000/immagini/MBDOC_OGG-P_CQFM20/CQ_FMEA_17.png)
alla causa viene associato con questa azione un nuovo documento (evidenziato figura seguente) su cui saranno riportati i nuovi valori degli indici ed in cui se necessario il progettista potrà rientrare ed associare una nuova richiesta di azione correttiva

## Hystory FMECA
![CQ_FMEA_18](http://localhost:3000/immagini/MBDOC_OGG-P_CQFM20/CQ_FMEA_18.png)
Il progettista a questo punto torna a rianalizzare gli istogrammi delle cause, sceglie quella con indice di priorità maggiore  ripetendo iterativamente questo processo (continous analisys) fino a che, per effetto delle misure previste o azioni correttive intraprese ed evase, tutte le priorità di rischio non siano al di sotto del livello minimo voluto.

Da notare che è stata intitolata FMECA la parte di gestione per ribadire il concetto di Continous-Analisys. Esiste però anche la FMECA in cui si intende Failure Mode Effect Criticability in cui viene analizzata la criticità degli effetti di guasto. Questa criticità è compresa nella dichiarazione della criticità del componente.
