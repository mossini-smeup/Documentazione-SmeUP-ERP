## OBIETTIVO
Avere uno strumento di gestione della documentazione aziendale. Per documentazione aziendale intendiamo la documentazione tecnica, le schede tecniche, i cataloghi, i disegni, le
specifiche e qualsiasi altro tipo di documento che la realtà aziendale necessita. L'applicazione realizzata consente di effettuare tutte le operazioni di gestione della documentazione attraverso un
unico formato video che presenta una serie di opzioni disponibili all'utente, consentendo a diversi utenti di effettuare solo le operazioni per cui sono abilitati.

## Formato video guida
![CQDOCU_02](http://localhost:3000/immagini/MBDOC_OGG-P_CQQM10/CQDOCU_02.png)
Le opzioni disponibili sono : 
 * 01 Aggiunta :  per immettere un nuovo documento;
 * 02 Modifica :  per modificare, approvare, rilasciare e distribuire un documento;
 * 03 Copia :  per creare un nuovo documento con caratteristiche simili ad uno già creato;
 * 04 Annullamento :  per eliminare un documento;
 * 05 Interrogazione :  per visualizzare un documento.

## Tipo documento
Per poter accedere in modo corretto alle funzioni si deve precisare quale è il TIPO DOCUMENTO che si vuole gestire; il TIPO DOCUMENTO è codificato nella tabella CQ0 (si veda eventualmente la descrizione della tabella CQ0).
Il tipo documento suddetto può anche essere precisato prima ancora di entrare nell'applicazione e, in questo caso, deve essere passato all'applicazione come parametro (CALL CQQM10G
PARM('tipo docum.')). Con questa possibilità la gestione sarà personalizzata in funzione di quel tipo di documento senza però poter modificarne il tipo fino al termine dell'applicazione.


## Formato video dettaglio
![CQDOCU_03](http://localhost:3000/immagini/MBDOC_OGG-P_CQQM10/CQDOCU_03.png)
### Note particolari
L'opzione di modifica permette di effettuare una molteplicità di operazioni : 
 * modificare la parte relativa all'immissione
 * approvare il documento una volta immesso
 * rilasciare il documento una volta approvato
 * distribuire il documento

Tutte queste operazioni sono assoggettate alle autorizzazioni che ogni singolo utente può avere o non avere, le autorizzazioni possono essere gestite per la classe "documenti" e per la classe "azioni-doc" : 
 * la classe documenti permette di autorizzare per : 
 ** 01 Immissione;
 ** 02 Modifica;
 ** 03 Copia;
 ** 04 Cancellazione;
 ** 05 Visualizzazione
 * la classe azioni-doc permette di autorizzare per : 
 ** Emissione;
 ** Approvazione;
 ** Rilascio;
 ** Distribuzione

Gli utenti che non possono nè approvare nè rilasciare un documento non vedranno nella prima videata del DETTAGLIO il tasto funzionale F15 che permette di passare alla seconda videata che gestisce l'approvazione, il rilascio e la distribuzione.

## Immissione
Il Q9000 nella fase di immissione porta alla compilazione di un documento  identificato da : 
 * Numero documento :  assegnato in automatico;
 * Livello di modifica inferiore;
 * Oggetto di riferimento.

I campi presenti nel documento, in linea con quanto richiesto dalla norma, consentono di specificare : 
 * il centro di lavoro interessato a questo documento;
 * il numero della modifica;
 * il tipo di modifica :  una modifica può essere definitiva, limitata, provvisoria, prima emissione ecc..;
 * lo stato di evasione della modifica :  un documento può essere emesso, approvato e rilasciato;
 * l'ente emittente del documento;
 * la matricola del responsabile dell'emissione;
 * la data di emissione del documento;
 * la problematica, obbiettivo e soluzione proposta;
 * una azione sulla prossima emissione :  facendo riferimento all'esempio fin qui visto, sul documento DISE9500046 al livello di modifica superiore a B5 verrà riportato nel campo "note" quanto specificato nel campo "Azione prossima emissione" del documento al livello modifica B5;
 * documento di origine :  se una richiesta di modifica di un progetto avesse portato alla modifica dei disegni del progetto, il campo "Docum. Origine" avrebbe offerto la possibilità di collegarsi in interrogazione con tale richiesta di modifica di progetto
 * la distribuzione della documenutazione;

## Approvazione
Si attiva dal formato di dettaglio attraverso il comando funzione F15; per approvare un documento con il Q9000 si deve specificare l'ente di approvazione e in funzione delle procedure aziendali si può specificare : 
 * un numero di documento per il documento dell'approvazione;
 * un responsabile interno per l'approvazione;
 * la data dell'approvazione del documento.

![CQDOCU_07](http://localhost:3000/immagini/MBDOC_OGG-P_CQQM10/CQDOCU_07.png)
## Rilascio
Si attiva dal formato di dettaglio attraverso il comando funzione F15; per rilasciare un documento con il Q9000 si deve specificare l'ente del rilascio e in funzione delle procedure aziendali si può specificare : 
 * un numero di documenuto per il documento del rilascio;
 * un responsabile interno per il rilascio;
 * la data del rilascio del documenuto.

![CQDOCU_08](http://localhost:3000/immagini/MBDOC_OGG-P_CQQM10/CQDOCU_08.png)
Si noti come il Q9000 impedisca il rilascio del documenuto se prima quest'ultimo non è stato approvato.

## Distribuzione
Si attiva dal formato di dettaglio selezionando l'apposito campo "Distribuzione documento" : 

![B£_LISD_03](http://localhost:3000/immagini/MBDOC_OGG-P_CQQM10/BX_LISD_03.png)
Per la gestione successiva si rimanda alla documentazione operativa del PGM B£IRT2
