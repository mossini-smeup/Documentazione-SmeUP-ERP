# Introduzione
Tramite questa scheda è possibile eseguire le azioni di gestione di un ente.
Le novità principali introdotte con la nuova gestione dell'anagrafica, oltre ad un'evidente ristrutturazione grafica, sono : 
* una gestione più fruibile dei dati
* l'accesso tramite diverse prospettive :  la prospettiva permette di avere diversi raggruppamenti di dati gestiti da  persone diverse in funzione dell'organizzazione aziendale (es. dati anagrafici e di pagamento gestiti dall'organizzazione commerciale, dati fiscali e bancari gestiti dalla Contabilità)
* una gestione più snella delle estensioni
* la gestione della data validità non più per campo ma per insiemi di dati, appartenenti da un gruppo, interessati ad una gestione storica per data.

# Struttura della scheda
I dati relativi ad un ente interessano un grande numero di aspetti diversi, per questo alla scheda è stata data una struttura che permetta di gestire tale complessità.

La scheda si presenta quindi suddivisa in tre macro sezioni.
![BRENTI_01](http://localhost:3000/immagini/MBDOC_SCH-CN_D/BRENTI_01.png)
* Nella prima macro-sezione in alto (bordo rosso) abbiamo i dati fondamentali che mi permettono di comprendere : 
** In che modalità di gestione sono entrato nella scheda (inserimento/modifica/copia ecc.).
** Il codice/descrizione dell'ente che sto gestendo.
** Con quale prospettiva sto interrogando i dati.
![BRENTI_02](http://localhost:3000/immagini/MBDOC_SCH-CN_D/BRENTI_02.png)
* Nella seconda, a sinistra (bordo giallo), avente titolo "ELENCO DATI", ho l'elenco dei raggruppamenti di dati che posso gestire. Se sono attive le prospettive, i raggruppamenti possono variare in funzione della prospettiva scelta.
![BRENTI_03](http://localhost:3000/immagini/MBDOC_SCH-CN_D/BRENTI_03.png)
* Nella terza sezione  (bordo verde), viene presentato il contenuto del  gruppo che è stato selezionato nell'ELENCO DATI.
![BRENTI_04](http://localhost:3000/immagini/MBDOC_SCH-CN_D/BRENTI_04.png)
# Comandi funzione
Nella manutezione dei dati entre sono presenti dei bottoni riconducibili ad uno specifico comando funzione : 
* **F06 - Conferma** : uno dei primi aspetti da considerare è che tutte le azioni che vengono effettuate all'apertura della scheda sono temporanee sin tanto che non vengono confermate dalla pressione del tasto funzione F06. Se la scheda viene chiusa in altro modo (es. abbandono), gli effetti di tutte le azioni effettuate andranno perse. Per evitare che questo accada, in caso di uscita, se sono state fatte delle azioni, viene richiesta la conferma dell'abbandono e della conseguente perdita delle modifiche applicate
* **F07 - Forzature** :  in funzione della parametrizzazione del rapporto fiscale (tab. BRX) è possibile determinare alcuni dei controlli applicabili ai dati fiscali  (partita iva nazionale, codice fiscale, partita iva estera) ad esempio è possibile controllare che non esista un  altro ente con la medesima partita iva. Se tali controlli impediscono di continuare si può utilizzare il tasto funzione F07 per forzare il proseguimento dell'attività.
![BRENTI_06](http://localhost:3000/immagini/MBDOC_SCH-CN_D/BRENTI_06.png)* **F18 - Gestione prospettive** :  permette di cambiare la prospettiva dei dati da gestire. Per il dettaglio relativo alla definizione delle prospettive si rimanda allo specifico capitolo della documentazione applicativa.
![BRENTI_18](http://localhost:3000/immagini/MBDOC_SCH-CN_D/BRENTI_18.png)
### Indicazione campo modificato in attesa di conferma
![BRENTI_26](http://localhost:3000/immagini/MBDOC_SCH-CN_D/BRENTI_26.png)
# Classificazione dati
I differenti raggruppamenti di dati attribuibili ad un ente possono riferirsi a tre categorie : 
* Dati di base
* Estensioni dell'anagrafica
* Dati Esterni

## Dati di Base
I dati di base sono i dati contenuti fisicamente nell'archivio anagrafico ed hanno essenzialmente due modalità di presentazione, differente a seconda che sia attiva la gestione per data o meno.

1) Se non è attiva la gestione per data, la sezione presentata è di questo tipo : 
![BRENTI_05](http://localhost:3000/immagini/MBDOC_SCH-CN_D/BRENTI_05.png)In questa sezione avrò una sola vista nella quale i dati sono direttamente modificabili.

2) Se invece la gestione per data è attiva la schermata si presenta in quest'altro modo : 
![BRENTI_10](http://localhost:3000/immagini/MBDOC_SCH-CN_D/BRENTI_10.png)Rispetto alla precedente versione le principali differenze sono : 
* Non ho una sola sezione, ma due sezioni sovrapposte (la prima con tutti i dati principali, la seconda con i soli dati gestiti per data validità).
* Nella prima vista vedo i dati validi alla data odierna e fra questi, __quelli con l'indicazione "/d"  non sono direttamente modificabili perché gestiti con data validità.
* Nella vista sottostante invece troverò l'elenco, per data, dei dati che è possibile modificare con data di validità.
![BRENTI_12](http://localhost:3000/immagini/MBDOC_SCH-CN_D/BRENTI_12.png)
## Estensioni dell'anagrafica
Le estensioni dell'anagrafica, sono informazioni aggiuntive rispetto ai dati di base in cui scopo è dedicato a particolari applicazioni (es. elenco riferimenti telefonici, modelli documento ammessi/esclusi, ....) Loro caratteristica è quella di poter essere gestite a loro volta oltre che per data, anche per dimensioni multiple (es. possono avere vari numeri di telefono/mail collegati allo stesso ente).

Per queste gestioni abbiamo differenti modalità : 
* **Estensione singola/semplice** :  non si discosta di molto dalla gestione dei dati di base, con l'aggiunta dell'azione di eliminazione che permette di cancellare l'estensione presentata.
![BRENTI_08](http://localhost:3000/immagini/MBDOC_SCH-CN_D/BRENTI_08.png)* **Estensione multipla** :  la schermata viene suddivisa in due sezioni, in quella superiore ho l'elenco di tutte le estensioni presenti, mentre nella sezione inferiore ho la possibilità di inserire/modificare/cancellare la singola estensione.
![BRENTI_13](http://localhost:3000/immagini/MBDOC_SCH-CN_D/BRENTI_13.png)* **Estensione con gestione per data validità** :  la gestione è simile a quella ad estensione multipla con in aggiunta le date di inizio e fine validità.
![BRENTI_14](http://localhost:3000/immagini/MBDOC_SCH-CN_D/BRENTI_14.png)
## Dati Aggiuntivi
Oltre alle estensioni, ad un ente possono essere aggiunte molte altre informazioni di natura eterogenea, le funzioni per la loro gestione vengono raggruppate in fondo all'elenco e generalmente indicate come "DATI AGGIUNTIVI". La sezione che verrà aperta sarà specifica della tipologia di informazioni aggiuntive selezionata.
![BRENTI_17](http://localhost:3000/immagini/MBDOC_SCH-CN_D/BRENTI_17.png)
# Setup
Qualora se ne possegga l'autorizzazione, sarà inoltre disponibile una voce "Funzioni Tecniche" : 
![BRENTI_25](http://localhost:3000/immagini/MBDOC_SCH-CN_D/BRENTI_25.png)
Le funzioni disponibili sono divise sotto due voci specifiche : 
* **Analisi differenze per data**
** Righe anagrafica :  permette di interrogare/analizzare le modifiche apportate ai dati di base
** Righe estensione :  come la precedente per le varie estensioni.
![BRENTI_19](http://localhost:3000/immagini/MBDOC_SCH-CN_D/BRENTI_19.png)* **Controllo Setup**
** Contatti in Gestione :  permette di interrogare/analizzare i contatti che sono in gestione in quella sessione (es. per un ente, gestito con nominativo, che è contemporaneamente un  fornitore ed un cliente vedrò 3 righe :  cliente, fornitore, nominativo) ho quindi una visione immediata di tutti gli enti su cui potrebbero avere effetto le modifiche in corso
** Scenari :  è l'elenco degli scenari previsti per il tipo contatto (se il tipo contatto ne prevede la gestione).
** Prospettive :  è l'elenco delle prospettive disponibili per il tipo contatto, dall'elenco posso passare alla modifica dello script.
** Def. Campi :  è l'elenco di tutti i campi dei dati anagrafici e di tutte le estensioni con tutte le relative caratteristiche.
** Campi :  è l'elenco di tutti i campi dei dati anagrafici e di tutte le estensioni con l'indicazione del puntatore utilizzato nelle schiere dei programmi dell'anagrafica.
** Campi Video :  è l'elenco di tutti i campi dei dati anagrafici e di tutte le estensioni previsti dalla prospettiva con tutte le relative caratteristiche.
** Controllo Errori :  permette di analizzare gli errori pendenti in quella precisa sessione (vedi figura successiva)
** Script Prospettive :  mi permette di analizzare lo script della prospettiva.
** Script Campi :  mi permette di analizzare lo script di definizione dei campi per il tipo contatto.
** Script Nominativo :  mi permette di analizzare lo script CN_£NO nel quale sono elencati i campi definiti a livello di nominativo.
** Intestazioni :  mi permette di visualizzare la tabella *CN IE dove sono stati definiti i macro gruppi dei dati dell'anagrafica.
![BRENTI_07](http://localhost:3000/immagini/MBDOC_SCH-CN_D/BRENTI_07.png)