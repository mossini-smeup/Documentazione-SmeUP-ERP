# MESSAGGI INVIATI

Per attivare l'invio di un messaggio da ambiente AS400 con il modulo Mail.up è necessario : 
- definire la  **Tabella ED1 Personalizzazione ED**;
- codificare l'indirizzo dell'Ente Ricevente nella  **Tabella EDI Indirizzi**;
- codificare il metodo di comunicazione tra Ente Ricevente ed Emittente, da  cui dipende la trasformazione del messaggio inviato nella **Tabella EDC Metodi di comunicazione**;
- codificare il tipo di messaggio da inviare nella  **Tabella EDT Messaggi inviati**.
> T(Nota di codifica)
L'indirizzo dell'Ente Ricevente,  definito  sul  codice  del  messaggio, può essere fisso o ricavabile dinamicamente, da parametri o da programma utente. In ogni caso dovrà essere un elemento della tabella EDI.

-attivare,  sul gruppo di informazione da inviare,  il  programma  EDAP_XX   (selezionabile  da un elenco di programmi standar); XX è il  suffisso che identifica il programma,  diverso  a  seconda del tipo di informazioni da trasmettere.
Dovendo ad esempio inviare un  Documento è possibile attivare il programma creando un'azione (che contiene il pgm suddetto), eseguibile singolarmente o da flusso.
Quando l'_7_Emittente invia un gruppo di informazioni (es. un documento)  ad un _7_Ricevente a tutti gli effetti provoca i seguenti eventi : 
1 - alimentazione dell'archivio dei _7_Messaggi inviati (EDSEND0F)
2 - trasformazione  del messaggio nella struttura di dati prevista dal Ricevente.
Per  la  gestione  dei  messaggi trasmessi è disponibile sul menu del modulo MAIL.up  (ED00)  il sottomenu ED02 Messaggi trasmessi, che consente le attività di : 
- Simulazione delle funzioni (di creazione/gestione archivio EDSEND0F)
- Esecuzione flusso EDI (trasmissione messaggio con pgm EDAP_XX)
- Interrogazione dei Messaggi trasmessi
- Stampa dei Messaggi trasmessi
In particolare nell'Interrogazione dei Messaggi  è  possibile utilizzare dei campi chiave del Messaggio, ed è possibile interrogare il contenuto del messaggio.
I campi chiave sono definiti sul codice del messaggio tramite un  griglia di controllo (Tabella B£G).
Il contenuto del messaggio è visualizzabile o come campi  di  un archivio, o come elemento di tabella, o altro a seconda del tipo tracciato definito  sul codice del messaggio.

# MESSAGGI RICEVUTI

Per attivare il  ricevimento di un messaggio in ambiente AS400 con il modulo Mail.up è necessario : 
- codificare il tipo di messaggio da ricevere nella tabella  EDR  (Messaggi ricevuti);
- attivare il programma EDES_XX  ( selezionabile  da un elenco di programmi standard ),  diverso  a  seconda del tipo di informazioni da ricevere.Il  programma viene attivato tramite una funzione di navigazione sui messaggi;

Per effettuare quindi il ricevimento di un messaggio e la sua trasformazione nella struttura desiderata è necessario che si siano verificati i seguenti eventi : 
- alimentazione dell'archivio dei Messaggi ricevuti (EDRECI0F); il record riportato deve assolutamente contenere il codice del messaggio (elemento di tabella EDR);
- applicazione del messaggio ricevuto tramite funzione di navigazione dei messaggi (ED05 Funzioni di Set and Play).

La  trasformazione  del messaggio  dipende dal metodo di controllo/applicazione definito sul codice del messaggio ricevuto.
Tale metodo corrisponde al suffisso del programma EDES_XX.
In molti casi (soprattutto nel trasferimento di documenti tra aziende diverse) è necessario definire, in un'apposita struttura, le corrispondenze tra i dati trasmessi e i dati ricevuti per la loro corretta conversione.
La struttura utilizzata è quella degli ALIAS. Pertanto nel codice del messaggio ricevuto è necessario definire un contesto (**Tabella C£K**).

Per  la  gestione  dei  messaggi trasmessi è disponibile sul menu del modulo MAIL.up  (ED00)  il sottomenu ED03 Messaggi ricevuti , che consente le attività di : 
- Simulazione delle funzioni (di creazione/gestione archivio EDRECI0F)
- Interrogazione dei Messaggi ricevuti
- Stampa dei Messaggi ricevuti

In particolare nell'Interrogazione dei Messaggi  è  possibile utilizzare dei campi chiave del Messaggio, ed è possibile interrogare il contenuto del messaggio.
I campi chiave sono definiti sul codice del messaggio tramite un  griglia di controllo (Tabella B£G).
Il contenuto del messaggio è visualizzabile o come campi  di  un archivio, o come elemento di tabella, o altro a seconda del tipo tracciato definito  sul codice del messaggio.


# INDIRIZZI E METODI DI COMUNICAZIONE

Quando codifico un indirizzo Ricevente (indirizzo di destinazione del messaggio  che trasmetto) definisco anche il metodo di Comunicazione con tale _7_Ente, ovvero le modalità con cui andrò a trasformare il messaggio che trasmetto.

Anche il metodo di comunicazione deve essere a sua volta  codificato nella tabella **EDM** e può assumere i seguenti comportamenti : 

- **Metodo *PRT /FILE DI STAMPA**
  Con questo metodo il messaggio trasmesso viene trasformato in un File di stampa, nel parametro del metodo si deve definire la coda  di  stampa su cui emetterlo. Il File  di  stampa  coincide  con il tracciato del messaggio sull'archivio EDSEND0f.
- **Metodo *FLR /CARTELLA AS400**
  Con  questo metodo il  messaggio  trasmesso viene trasformato in un Documento  (Es.  File  di  testo  su AS400) contenuto in una cartella AS400. In questo caso nel parametro del metodo definisco il nome della cartella. Il Documento scritto coincide con il  tracciato del messaggio sull'archivio EDSEND0f.
- **Metodo *DIR /DIRETTO**
  Questo è il metodo utilizzato per  trasferire messaggi tra società diverse con librerie diverse, ma che utilizzano entrambe il modulo Mail.up di Smeup e sullo stesso AS400.
Con questo metodo il messaggio trasmesso viene trasformato automaticamente in un messaggio ricevuto  (archivio EDRECI0F), nella libreria definita sul parametro del metodo.
In questo caso è assolutamente  indispensabile che il codice del messaggio trasmesso e il codice del messaggio ricevuto siano uguali.
- **Metodo *RMT /SISTEMA REMOTO**
  Questo è il metodo utilizzato  per  trasferire messaggi da un ambiente con sistema  operativo  AS400  ad  un ambiente con sistema operativo diverso o comunque non collegato all'Ente Emittente.
  Con questo metodo il messaggio trasmesso viene trasformato in una struttura di dati esterna.
  E'  quindi  necessario  fornire nei parametri del metodo il Nome dell'Host (Sistema  remoto  che  riceverà  i  dati trasmessi), il nome del file e il percorso.
  Ad esempio se voglio trasfomare il mio messaggio in un  documento  Word il nome dell'Host è l'indirizzo IP della macchina, il nome del file è il nome del  documento  Word  e il percorso è la Directory e le eventuali cartelle sul Server/PC ricevente.


