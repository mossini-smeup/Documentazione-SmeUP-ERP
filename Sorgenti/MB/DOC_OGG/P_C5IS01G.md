## Obiettivo
Attraverso questa voce di menù è possibile inserire, interrogare o modificare singoli movimenti che andranno a generare gli elenchi riepilogativi degli scambi intracomunitari di beni e servizi, accedendo anche al formato lista dei movimenti già inseriti.

## Formato guida
Il formato guida si presenta nel seguente modo : 


![C5C090_001](http://localhost:3000/immagini/MBDOC_OGG-P_C5IS01G/C5C090_001.png)

Al suo interno è possibile visualizzare i seguenti campi : 
 * Opzione :  è possibile selezionare l'inserimento, la modifica, la cancellazione, ecc di record.
 * Numero di registrazione :  è possibile inserire il numero di registrazione contabile a cui il movimento intrastat è riferito. Selezionando uno dei classici caratteri di ricerca è possibile visualizzare l'elenco della registrazioni di prima nota e reperire al suo interno la registrazione desiderata.
 * Tipo inserimento :  questo campo compare solamente digitando l'opzione 01 e al suo interno è necessario indicare se si tratta di una rettifica oppure di una normale registrazione.

## Formato lista

Omettendo la compilazione dei campi riportati nel formato guida e dando invio è possibile accedere al formato lista che riporta l'elenco dei movimenti intrastat inseriti : 

![C5C090_002](http://localhost:3000/immagini/MBDOC_OGG-P_C5IS01G/C5C090_002.png)

Nella parte superiore dell'elenco sono riportate le opzioni disponibili per ogni singolo record e che compariranno anche digitando un '?' all'interno della casella posta all'inizio del record stesso : 


![C5C090_003](http://localhost:3000/immagini/MBDOC_OGG-P_C5IS01G/C5C090_003.png)
All'interno dell'elenco sono facilmente distinguibili i record relativi a note di credito (evidenziati dalla lettera N e colorati in rosso) e quelli di rettifica (distinti dalla lettera R e colorati in blu).
Per ognuno dei record della lista sono riportati : 
 * data registrazione, codice registro IVA e numero protocollo interno
 * tipo ente intestatario, partita iva, codice e ragione sociale
 * presenza di servizi o meno all'interno del record
 * Nomenclatura combinata/codice CPA della prestazione :  questo campo ha senso ovviamente solo nel caso in cui all'interno della registrazione contabile ci sia una sola nomenclatura combinata/un solo codice prestazione. Nel caso in cui ne fossero presenti più di uno sarà necessario entrare nel dettaglio del record per visualizzare tutti i codici riportati al suo interno.
 * Massa netta :  ha senso solo per i record contenenti solamente merci
 * Importo totale :  riporta l'importo totale registrato per il movimento intrastat.

Utilizzando l'opzione 02 o 05 è possibile accedere in modifica o in interrogazione del formato dettaglio.

### Impostazioni

Digitando il tasto F17 o selezionando il relativo pulsante è possibile accedere alla schermata delle impostazioni al cui interno è possibile selezionare lo schema 'Esteso con righe' che consente la visualizzazione del dettaglio di ogni record nel formato lista : 

![C5C090_004](http://localhost:3000/immagini/MBDOC_OGG-P_C5IS01G/C5C090_004.png)
### Parzializzazioni

Digitando il tasto F13 o selezionando il relativo pulsante è possibile accedere alla schermata delle parzializzazioni che consentono di filtrare i record visualizzati : 

![C5C090_005](http://localhost:3000/immagini/MBDOC_OGG-P_C5IS01G/C5C090_005.png)
All'interno delle parzializzazioni è sempre disponibile il campo delle memorizzazioni che consente di salvare una particolare parzializzazione; ad esempio è possibile salvare parzializzazioni che consentono di visualizzare solamente record relativi a cessioni o record di rettifica degli acquisti, ecc.
Per maggiori dettagli sull'utilizzo delle memorizzazioni video si veda il seguente : 

- [Gestione Dati Scelte Video](Sorgenti/MB/DOC_OGG/P_B£MDV0)


### Tasti funzionali

 * F13 - Parzializzazioni :  permette di accedere alla schermata delle parzializzazioni.
 * F17 - Impostazioni :  permette di accedere alla schermata delle impostazioni.

## Dettaglio registrazione Intra

Entrando nel dettaglio di ogni singola registrazione è possibile visualizzarne le informazioni associate così come il dettaglio dei record che verranno poi riportati all'interno dei riepilogativi intrastat : 

![C5C090_006](http://localhost:3000/immagini/MBDOC_OGG-P_C5IS01G/C5C090_006.png)
Le informazioni visualizzate all'interno del formato lista sono : 
(i campi in corsivo sono presenti solo nel caso in cui all'interno della registrazione sia presente almento un record relativo a merce mentre i campi sottolineati compaiono solo nel caso in cui all'interno della registrazione sia presente almeno una prestazione)
 * Numero Registrazione. Nel caso in cui il movimento abbia origine da una registrazione contabile è il numero della registrazione stessa mentre nel caso in cui il movimento abbia origine da un documento V5 in questo campo è riportato il riferimento interno del documento.
 * Data Registrazione. Nel caso in cui il movimento abbia origine da una registrazione contabile è la data della registrazione stessa mentre nel caso in cui il movimento abbia origine da un documento V5 in questo campo è riportata la data del documento interno.
 * Periodo Rifermento. Nel formato AnnoMese, è il periodo che viene derivato automaticamente dalla Data Registrazione. Per i movimenti di nota credito relativi a fatture appartenenti a periodi precedenti il dato va corretto manualmente. Quindi in caso di nota credito registrata a Marzo 2010 e relativa a fattura di Gennaio 2010 il sistema automaticamente identificherà la nota credito con periodo di riferimento 201003 che andrà corretto manualmente mettendo 201001.
 * Tipo Movimento. Viene posto automaticamente a 'C' o 'A' a seconda del registro IVA della registrazione o del tipo modello documento.
 * Tipo Documento. Assume il valore di 'Fattura' o di 'Nota' a seconda del segno IVA.
 * Tipo Comunicazione. In questo campo viene indicato se i dati relativi alla registrazione dovranno generare una comunicazione Completa, solo Fiscale, solo Statistica oppure se non sono da trasmettere. Questo campo di default viene impostato 'Completa'; solo in caso di documenti di conto lavoro viene forzato a 'Fiscale'.
 * Riferimento. Nel caso in cui la registrazione provenga dalla contabilità riporta il tipo e il numero di protocollo, nel caso in cui provenga da un documento riporta il tipo e il numero di documento.
 * Data Riferimento. Riporta la data del protocollo o del documento indicato nel Riferimento.
 * __Fattura/Del.__  In questi campi sono riportati il numero e la data protocollo del documento di acquisto/cessione delle prestazioni riportate nel formato dettaglio.
 * _ Natura Transazione._  Tabellato nella V§*IB, è un flag che, nel caso in cui la registrazione derivi dalla prima nota, è determinato dalla causale del movimento di origine (tabella C5V) mentre, nel caso in cui la registrazione abbia origine da un documento, viene impostato a 5 per documenti di conto lavoro e a 1 per gli altri documenti.
 * __Modalità Incasso.__  In questo flag è riportata la modalità di incasso della fattura relativa alla/e prestazione/i di servizio. Il campo è ripreso in automatico dalla prima scadenza della registrazione e impostato a B in caso di bonifico e a X negli altri casi.
 * Soggetto.  Individua la tipologia e il codice dell'ente con il quale si intrattiene il movimento di acquisto o cessione.
 * P.IVA del soggetto con cui si intrattiene lo scambio.
 * Valuta Nazionale soggetto. Indicazione del codice divisa nel caso in cui il soggetto appartenga ad un paese che non aderisce al sistema euro. Viene automaticamente ripreso leggendo l'anagrafica dell'ente.
 * Cambio.  Cambio riferito alla valuta sopra indicata. Viene automaticamente ripreso dal file dei cambi se gestito, in caso contrario viene ripreso l'ultimo cambio inserito.
 * _ Nazione provenienza._  Il campo è visualizzato solo nel caso di acquisti di beni; è tabellato nella V§N e rappresenta la nazione da cui proviene la merce.
 * __Nazione pagamento.__  Tabellata nella V§N, è la nazione in cui il corrispettivo entra nella disponibilità del beneficiario. Quindi in caso di bonifico a fornitore verrà ripresa la nazione della banca del fornitore mentre in caso di bonifico da cliente verrà ripresa la nazione della banca aziendale.
 * _ Nazione origine/destinazione._  Tabellata nella V§N, è la nazione dell'ente con cui si intrattiene lo scambio (sarà nazione origine in caso di ciclo passivo e nazione destinazione in caso di ciclo attivo).
 * _Provincia origine/destinazione._  Tabellata nella V§P, è la provincia dell'azienda dichiarante (sarà provincia origine in caso di ciclo attivo e provincia destinazione in caso di ciclo passivo).
 * _Condizioni consegna._  Tabellata nella V§*IE, è collegata alla modalità di consegna presente sul documento V5 (tabella CCO).
 * _Modalità trasporto/resa._  Tabellata nella V§*IC, è collegata alla modalità di spedizione presente sul documento V5 (tabella SPE).
 * Dettaglio dati : 
 ** Codice :  riporta la nomenclatura combinata/il codice CPA dei beni/prestazioni oggetto dello scambio. I due valori sono rispettivamente tabellati all'interno della BRN e della V§*IG.
 ** Descrizione :  riporta la descrizione della nomenclatura combinata/prestazione di servizio.
 ** Massa netta :  riporta il valore della massa netta nel caso in cui il record di dettaglio sia riferito a merce.
 ** Importo :  riporta l'importo relativo alla riga di dettaglio.
 ** Periodo :   riprende il concetto espresso per il campo analogo di cui sopra, consentendo tuttavia di differenziarlo per singola nomenclatura/CPA.
 ** T :  questo campo viene valorizzato a 1 per quei record che identificano prestazioni di servizio.
 ** E :  rappresenta la modalità di erogazione di una prestazione (I per istantanea R se a più riprese).
 * Importo registrazione :  viene qui riportato l'importo totale della registrazione contabile.
 * Totale :  riporta il totale della registrazione intrastat.
 * Differenza :  nel caso in cui vi sia una squadratura di importi tra contabilità e movimento intrastat, questa squadratura viene segnalata e valorizzata.

### Tasti funzionali

 * F05 - Rivisualizza. Permette di aggiornare la videata visualizzata.
 * F06 - Conferma. Conferma i dati visualizzati e ritorna al formato lista registrazioni intrastat.
 * F08 - Aggiunta. Permette di aggiungere nuove righe di dettaglio all'interno della registrazione. Selezionando questo tasto verrà richiesto se il record da inserire è relativo a una prestazione di servizio oppure a uno scambio di merce; una volta indicata questa informazione verrà presentato il formato dettaglio nel quale andranno compilate le informazioni necessarie.

### Opzioni

Su ciascuna delle righe di dettaglio sono disponibili le seguenti opzioni : 
 * 2 - Modifica :  entra in modifica del dettaglio della riga.
 * 4 - Cancella :  cancella la riga di dettaglio.
 * 5 - Visualizzazione :  entra in visualizzazione del dettaglio della riga.

## Formato dettaglio

Il contenuto del formato dettaglio varia al variare del contenuto della riga. In particolare per le merci saranno visualizzate le seguenti informazioni : 

![C5C090_007](http://localhost:3000/immagini/MBDOC_OGG-P_C5IS01G/C5C090_007.png)
 * Codice nomenclatura combinata. E' tabellato all'interno della BRN.
 * Importo U.d.C. Importo esposto in fattura (valore della merce).
 * Importo Valuta. Importo precedente convertito in divisa tramite il cambio espresso precedentemente.
 * Massa Netta. Peso netto della merce con nomenclatura indicata oggetto della movimentazione.
 * Massa udm suppl. Peso netto della merce espresso nell'unità di misura supplementare.
 * Importo Statistico. Sulla base dell'importo U.d.C. viene aggiunto un valore di trasporto e calcolato il valore statistico.
 * Importo Statistico in valuta. Importo precedente convertito in divisa tramite il cambio espresso precedentemente.
 * Periodo di riferimento. Riprende il concetto espresso per il campo analogo nel formato lista, consentendo tuttavia di differenziarlo per singola nomenclatura.

Per le prestazioni saranno invece visualizzate le seguenti informazioni : 

![C5C090_008](http://localhost:3000/immagini/MBDOC_OGG-P_C5IS01G/C5C090_008.png)
 * Codice prestazione. E' tabellato nella V§*IG
 * Importo U.d.C. Riporta l'importo della prestazione.
 * Importo valuta. Importo precedente convertito in divisa tramite il cambio espresso precedentemente.
 * Modalità erogazione. Riporta se l'erogazione del servizio è avvenuta a più riprese o in modo istantaneo. Di default il campo viene compilato 'A più riprese' solo nel caso in cui all'interno della registrazione contabile venga indicato un periodo di competenza.
 * Periodo di riferimento. Riprende il concetto espresso per il campo analogo nel formato lista, consentendo tuttavia di differenziarlo per singola prestazione.

Per confermare le informazioni visualizzate all'interno del formato dettaglio è necessario digitare il tasto F6; per uscire senza confermare è invece necessario digitare F12.
