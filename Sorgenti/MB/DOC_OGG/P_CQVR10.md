## Formato di lancio
![CQ_EART_02](http://localhost:3000/immagini/MBDOC_OGG-P_CQVR10/CQ_EART_02.png)
## Immissione dati ente / articolo
L'immissione dati Ente/Articolo viene utilizzata nella fase iniziale del rapporto tra l'azienda e il fornitore oppure nei casi di registrazione di prodotti nuovi, per definire uno skill di identificazione.
I dati che vengono inseriti nel modulo, sono in genere il frutto di indagini conoscitive che vengono condotte dall'azienda tramite schede, spedite al fornitore, o verifiche  ispettive, allo scopo di capire le principali caratteristiche legate alla capacità e alle qualità del fornitore.
Nella fase preliminare di raccolta dati (ma anche nel seguito), viene quindi impiegato il modulo degli Audit come supporto per la gestione della modulistica relativa alla valutazione iniziale del fornitore (cfr documentazione AUDIT per la spiegazione completa sul modulo degli Audit).

Il programma mediante questo modulo consente la raccolta/archiviazione e la relativa valutazione indicizzata dei dati risultanti dalle ispezioni dirette (visita in loco) o indirette (schede spedite) sul fornitore.

## Attribuzione classe di abilitazione
Questo si effettua lanciando il programma con il solo codice del fornitore senza specificare nessun codice di articolo (la classe di abilitazione è una caratteristica generale del fornitore).

Collegandosi con la Tabella che gestisce le classi di abilitazione, si sceglie o si crea il livello adatto per quel fornitore (la Tabella CQV indica i limiti delle classi funzionali accettabili nelle condizioni di fornitura normale ed in Free Pass).

È da notare che il programma permette di specificare tramite la tabella delle classi di abilitazione, le classi funzionali ammesse nelle due diverse situazioni :  normale ed in free pass. La struttura non è comunque rigida :  se l'utente lo desidera (e possiede validi motivi per farlo) può forzare l'abilitazione di un fornitore alla fornitura di prodotti di classe funzionale non ammessa.

### Formato inserimento classe di abilitazione
![CQ_EART_03](http://localhost:3000/immagini/MBDOC_OGG-P_CQVR10/CQ_EART_03.png)
_2_Nota 1; l'informazione sulla classe di abilitazione del fornitore è impiegata per l'impostazione del piano di controllo del prodotto acquistato.
Il programma quando definisce i parametri per i PdC e i Livelli da assegnare dei lotti confronta la classe funzionale dell'articolo con il  livello di abilitazione assegnato al fornitore e decide il piano sulla base delle tabelle impostate.

_2_Nota 2; è possibile fissare un livello di abilitazione per il "fornitore generico", in modo che rimane stabilito un valore di default nel caso in cui per uno specifico fornitore non venga definita l'AB. Operativamente ciò viene effettuato lanciando il programma inserendo " **" al posto del codice fornitore.

Il fatto di poter specificare una caratteristica generale (ciò come vedremo nel seguito vale anche per gli indici di qualità di un determinato fornitore per il quale si può assumere la valutazione generica, modificando solo le voci che si discostano da tale profilo), è dal punto di vista operativo per l'azienda, particolarmente utile.
Si pensi infatti ad un'azienda che gestisce svariati fornitori, da ciascuno dei quali acquista un certo numero di articoli a diversi livelli di modifica, e che vuole impostare un piano di Vendor Rating ad ogni livello, come minimo dovrebbe assumere degli addetti che si occupino esclusivamente di immettere i dati sui fornitori ed aggiornarli, con notevole dispendio di denaro e risorse rispetto ai benefici risultanti.
Il Q9000 gestendo questo sistema di profili generali, sfoltisce in modo drastico il lavoro :  l'Ente della qualità a cui è affidato il compito di gestire il Vendor Rating non deve far altro che adattare al caso specifico lo skill creato per il livello generale.

### Formato inserimento dati ente / articolo
![CQ_EART_04](http://localhost:3000/immagini/MBDOC_OGG-P_CQVR10/CQ_EART_04.png)
Successivamente si può passare all'inserimento dei dati Fornitore / Articolo / Fase di lavorazione + Esponente di modifica con tutte le necessarie documentazioni sulle specifiche e sulle condizioni di fornitura, dichiarando in questo modo l'"omologazione" del fornitore.
Il programma permette l'inserimento nell'archivio delle informazioni sul Free Pass, sulla prima fornitura, sulla forzatura,  sulla classe di  abilitazione, etc. Naturalmente l'inserimento in archivio dei dati relativi ad un fornitore avviene anche in modo automatico al momento dell'ingresso del lotto in base a dei valori di default. Quando entra un lotto per cui non esiste la combinazione Fo / Ar / Fase+EM, il programma cerca in archivio se esiste la documentazione relativa al fornitore; se esiste crea in automatico il record segnalando che il fornitore non era omologato e quindi assegnandogli un Piano di Campionamento opportuno. Il flusso operativo seguito dal programma è schematizzabile in questo modo : 

![CQ_EART_05](http://localhost:3000/immagini/MBDOC_OGG-P_CQVR10/CQ_EART_05.png)
 * Il programma informa anzitutto sulla abilitazione o meno alla fornitura dell'articolo in oggetto da parte del fornitore, confrontando la classe dell'articolo con quella associata al livello di abilitazione.
 * Avverte se il fornitore è abilitato o meno alla fornitura in Free Pass di un certo prodotto nel caso in cui si imposti la condizione di fornitura in Free Pass (in base alla tabella CQQ della classe funzionale del prodotto viene fissato il piano di campionamento adeguato).
 * Il programma gestisce le prime forniture condizionando il livello di controlli assegnati ad un certo fornitore :  le tabelle dei campionamenti forniscono il Piano ed il Livello di Campionamento previsti per la prima fornitura di un dato prodotto appartenente ad una determinata classe funzionale. Naturalmente ciò comporta che per un dato fornitore si potranno avere trattamenti diversi per la prima fornitura di ciascuno degli articoli da lui forniti. È possibile stabilire l'arco di tempo in cui è valido il trattamento di prima fornitura indicando la data di termine e il numero di forniture che si decide di far rientrare in questa categoria.
 * Inserendo una X nel campo "FREE PASS", il programma stabilisce la condizione di entrata libera dei lotti di quell'articolo che rientrano nel lasso di tempo incluso nella data specificata o nel numero di consegne valide per quel trattamento.
 * Inserendo un 1 nel campo "FORZATURA OMOLOGAZIONE", il programma stabilisce la condizione di forzatura (per la consegna di prodotti da parte di un fornitore non abilitato) di entrata dei lotti di quell'articolo che rientrano nel lasso di tempo incluso nella data specificata o nel numero di consegne valide per quel trattamento.  Serve ad esempio quando un fornitore è abilitato a CF=3 ma fornisce un articolo di CL=2; allora per questo articolo potrà fargli assumere se lo desidera una abilitazione forzata (con conseguente PdC). Allo stesso modo per il Free Pass. Se viene data la forzatura allora il PdC assunto è quello per fornitore omologato. Se viene data la consegna in 1° fornitura allora il PdC è della 1° fornitura nella tabella CQQ. Se il fornitore non è abilitato allora viene assegnato il PdC per fornitore non omologato di CQQ.
 * Il campo "Legame FO/AR-Ciclo Coll." consente di personalizzare il ciclo di collaudo standard mediante la selezione o la modifica delle fasi in esso presenti.
Vediamo in dettaglio tramite i seguenti Flow Chart come il programma gestisce l'assegnazione dei Piani di Campionamento  e dei Free Pass per un dato ordine di acquisto, appoggiandosi al modulo precedente.

![CQ_EART_06](http://localhost:3000/immagini/MBDOC_OGG-P_CQVR10/CQ_EART_06.png)
![CQ_EART_07](http://localhost:3000/immagini/MBDOC_OGG-P_CQVR10/CQ_EART_07.png)
![CQ_EART_08](http://localhost:3000/immagini/MBDOC_OGG-P_CQVR10/CQ_EART_08.png)
![CQ_EART_09](http://localhost:3000/immagini/MBDOC_OGG-P_CQVR10/CQ_EART_09.png)
![CQ_EART_10](http://localhost:3000/immagini/MBDOC_OGG-P_CQVR10/CQ_EART_10.png)
_2_Nota; se nel modulo di gestione dei dati si impongono consegne in Free Pass a un fornitore che non ne è abilitato, e non si opera una forzatura, quando si cerca di utilizzare il modulo di "Dichiarazione di Collaudo" per quel fornitore, il programma, eseguendo una serie di verifiche a diversi livelli (fornitore, fornitore-articolo,fornitore-articolo-esponente di modifica), avverte dell'incompatibilità riscontrata e impedisce di eseguire operazioni senza aver impostato una forzatura.

Esistono messaggi di controllo che avvisano riguardo alle condizioni di abilitazione e alla forzatura sull'abilitazione : 
 * Durante l'emissione dell'ordine a fornitore se nella scheda è attivo il flag relativo alla stampa degli accordi presi (campo "stampa accordi fornit.")  col fornitore, questi accordi verranno stampati sull'ordine a fornitore. Verranno stampate tutte le note, clausole e commenti che sono stati inseriti nelle Note Strutturate;  saranno incluse le righe che non presentano nelle colonne di controllo il flag "I".
 * Durante l'emissione dell'ordine a fornitore se nella scheda è attivo il flag di stampa della griglia di collaudo (campo "stampa griglia Coll."), assieme all'ordine fornitore, sarà stampata anche la griglia di collaudo personalizzata al fornitore in questione (se esiste il legame fornitore-ciclo, oppure la griglia di collaudo standard se non esiste il legame).Saranno stampate solamente quelle fasi del ciclo che sono state rilasciate e che sono legate al livello di modifica dell'ordine attivo.
 * Tramite l'opzione "legame FO/AR Ciclo Coll." il programma permette di personalizzare il ciclo di collaudo, attivando o disattivando le fasi previste per l'articolo nel ciclo standard.
 * Nei cicli di collaudo possono essere stampate solo le fasi con lo stato "Rilasciato" di tabella CQ2. Tutte le fasi presenti non ancora rilasciate vengono saltate e sulla stampa comparirà il N° della fase e la scritta "Non Rilasciata".
 * La stampa del ciclo di collaudo deve essere sempre effettuata al livello di modifica del lotto in questione o mediante scelta del livello da maschera iniziale.Tutte le fasi con livello di modifica minori o uguali alla scelta andranno a ricoprire le omologhe
 * Se una fase del ciclo non è rilasciata, viene stampata la fase precedente come livello di modifica e viene evidenziata con il commento :  "Fase Non Rilasciata" per il livello assunto.

![CQ_EART_11](http://localhost:3000/immagini/MBDOC_OGG-P_CQVR10/CQ_EART_11.png)
![CQ_EART_12](http://localhost:3000/immagini/MBDOC_OGG-P_CQVR10/CQ_EART_12.png)
![CQ_EART_13](http://localhost:3000/immagini/MBDOC_OGG-P_CQVR10/CQ_EART_13.png)
![CQ_EART_14](http://localhost:3000/immagini/MBDOC_OGG-P_CQVR10/CQ_EART_14.png)
### manutenzione dati ente / articolo
Lo stesso programma può essere utilizzato in fase di revisione quando nasce l'esigenza di aggiornare lo skill relativo ad un fornitore.
È possibile modificare : 
 * la classe di abilitazione :  ciò può essere necessario se dagli accertamenti fatti mediante Audit, risulta un miglioramento o un peggioramento del livello di qualità;
 * le condizioni di Free Pass o di forzatura che possono essere richieste;
 * i prezzi degli articoli in aumento o in diminuzione con le relative indicazioni sulle percentuali di sconto attribuite ed eventuali note corrispondenti alle stesse variazioni;
 * gli indici statici della qualità;

altre generiche informazioni che possono riguardare il rapporto fornitore/articolo.
