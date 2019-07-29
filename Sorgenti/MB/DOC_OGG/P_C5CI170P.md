## OBIETTIVO

Qui di seguito vengono evidenziate una serie di casistiche particolari da prendere in considerazione prima di procedere con l'estrazione dei dati.

**NOTA BENE** :  qualora le soluzioni predisposte dallo standard non siano applicabili al contesto dall'azienda è importante notare che si potranno sempre implementare logiche alternative attraverso il programma di exit previsto per l'estrazione.

## NATURA DEGLI ASSOGGETTAMENTI

Per tutti gli assoggettamenti con aliquota zero, intra e reverse charge, è necessario che venga indicata la corrispondente natura.
Questa informazione va indicata nei parametri della tabella IVA (Classe parametri IVA) attraverso la gestione parametri o prevedendo che tale gestione venga richiamata in automatico con un flusso di post-inserimento/modifica della tabella IVA alla conferma di un elemento di tabella.
Attraverso il programma C5UTX62 è possibile far si che venga calcolata una proposta, ma tale proposta non è sufficiente a coprire tutti i casi. Per tale motivo è necessario che le varie casistiche vengano controllate puntualmente.
Qui di seguito una sintesi delle varie casistiche.
NOTA BENE :  il C5UTX62 compila solo gli assoggettamenti per cui non è stata già indicata la natura.

* **N1 Escluse**(Va sempre indicata manualmente)
** operazioni escluse dall'applicazione IVA per ex art. 15 (rif. Circolare 1/E/2017)

* **N2 Non soggette**(il C5UTX62 la attribuisce se aliquota zero e campo codice esenzione vuoto)
** Cessioni di beni non soggette
** Servizi fuori campo iva (art. 7-ter 633/1972 rif. Circolare 1/E/2017)
** Operazioni fuori campo iva (ex Art.74 DPR 633/72 rif. Circolare 87/E/2017)
** Fatture ricevute dai contribuenti minimi o forfettari o di vantaggio (rif. Circolare 1/E/2017 e rif. Circolare 87/E/2017)
** Prestazioni servizi extra-UE  (rif. Circolare 1/E/2017)

* **N3 Non imponibile**(il C5UTX62 la attribuisce se aliquota zero e campo codice esenzione NI)
** Esportazioni  (rif. Circolare 1/E/2017) comprese quelle nel regime del margine ((rif. Circolare 87/E/2017))

* **N4 Esente**(il C5UTX62 la attribuisce se aliquota zero e campo codice esenzione ES)
** Operazioni esenti (es. prestazione sanitaria secondo rif. Circolare 1/E/2017)

* **N5 Regime del margine / Iva non esposta in fattura**(Va sempre indicata manualmente)
** operazioni in regime dei beni usati (rif. Circolare 1/E/2017)
** operazioni relative all'editoria (rif. Circolare 1/E/2017)
** fatture emesse senza separata indicazione dell'imposta da parte di agenzie di viaggio e turismo (rif. Circolare 1/E/2017)

* **N6 Reverse charge**(il C5UTX62 la attribuisce se presente flag reverse charge o intra con aliquota <> da 0)
** Operazioni soggette a reverse charge (rif. Circolare 1/E/2017)
** Acquisti intracomunitari (unica eccezione per cui imponibile ed imposta sono diversi da zero) (rif. Circolare 1/E/2017)
** servizi ricevuti da prestatori UE ed Extra UE

* **N7 Iva assolta in un altro stato UE**(Va sempre indicata manualmente)
** Vendite a distanza
** Servizi di telecomunicazioni teleradiodiffusione ed elettronici

## NOTE DI DEBITO
E' necessario che le registrazioni corrispondenti a documenti di nota di debito vengano identificate rispetto alle normali fatture. Tale identificazione a standard è possibile tramite la tabella del tipo registrazione (campo T1C5DB).
Se erano stati predisposti dei tipi di registrazione specifici per queste operazioni basta integrare le C5D esistenti, viceversa sarà necessario codificare delle nuove tipologie e forzare poi tali tipologie sulle registrazioni pertinenti (stando attenti al fatto che il registro del tipo registrazione di origine e quello forzato non mutino).

## DOCUMENTI SEMPLIFICATI
Valgono le medesime considerazioni delle note di addebito, utilizzando il campo identificativo specifico.

## AUTOFATTURE
In merito alle autofatture al momento è necessario fare le seguenti considerazioni : 
* Esplicitamente è stato indicato dall'agenzia delle entrate che le autofatture che sono state emesse a seguito del mancato ricevimento di una fattura fornitore o di una sua irregolarità, vengano trasmesse nei dati delle fatture ricevute e non nei dati delle fatture emesse. In smeup questo tipo di operazioni non è individuabile rispetto ad altre e per tale motivo una situazione del genere andrà trattata manualmente.
* In linea generale non è chiarissimo se le altre tipologie di autofatture siano o meno da trasmettere. Smeup le prende in considerazione, se si valuta di non volerlo fare è possibile, come per qualsiasi altro soggetto, indicare nella corrispondente anagrafica che il soggetto intestatario delle autofatture sia da omettere dalla dall'estrazione (tramite l'estensione £55).
* Si apre infine una questione relativa alle autofattura generate a partire dall'integrazione di una fattura estero. Anche nel caso in cui le autofatture si valuta siano da trasmettere non è chiaro se questa ulteriore sottocasistica sia da trasmettere o meno fra le fatture emesse. Al momento smeup salvo l'eccezione della £55, le trasmette. Se si decidesse di non trasmetterle è necessario intervenire manualmente.
* Infine un ulteriore nota per il caso del punto precedente :  l'autofattura relativa all' integrazione di una fattura estera non dovrebbe essere invece trasmessa in quanto rientrante nel caso della natura N6 (Reverse Charge). Quando questi movimenti vengono strutturati in base alle funzioni previste da Sme.Up per reverse charge e generazione autofattura, la parte vendite non viene effettivamente trasmessa. Viceversa se io movimenti iva vendite vengono creati in differente modo sarà necessario operare manualmente.
* Per la stessa categoria del punto precedente va inoltre concordato se i movimenti relativi all'iva debito vadano trasmessi con soggetto intestatario il fornitore o l'azienda. Sarà necessario poi intervenire manualmente se i dati estratti non coincidono con la scelta.

## BOLLE DOGANALI
Per le bolle doganali, è previsto siano trasmesse con i dati del fornitore estero cui si riferisce l'operazione.
Solo per l'anno 2017, è però previsto, che nel caso in cui tali informazioni non siano reperibili, che il movimento possa essere trasmesso con id paese = OO ed id fiscale composto da una sequenza di undici "9".
Perchè questo avvenga in estrazione è necessario che tutti i soggetti usati per la registrazione delle bolle doganali sia individuabili attraverso un rapporto fiscale (tabella BRX) specifico, in cui sia stato impostato il campo "Dogana".

Se la situazione non è già questa, vanno reperiti i soggetti che corrispondono ad un dogana, se necessario codificare un nuovo elemento della BRX e poi attribuire tale elemento all'elenco dei codici reperiti.

## MOVIMENTI DI PURA IVA

Vengono tutti inclusi considerando queste casistiche : 
* Autofattura
* Rettifica registrazione documento
* Bolle doganali
Qualora si pongano differenti casistiche per cui possa risultare necessaria l'esclusione dalla trasmissione, tale esclusione andrà gestita manualmente.

## REGISTRAZIONE RIEPILOGATIVE DI FATTURE
Nel caso siano state effettuate delle registrazioni riepilogative di più fatture, sarà necessario cancellare il movimento creato in automatico dall'estrazione e reinserire manualmente i dati di ogni singola fattura di cui era composta la registrazione.

## ASSOGGETTAMENTI IVA (Tabella IVA)
Per gli assoggettamenti acquisti intra differenziare tra merci e servizi (campo T$IVA6)

## ESCLUSIONI
* Sono automaticamente esclusi tutti i movimenti che non finiscono nella stampa dei registri Iva (unica eccezione sono gli assoggettamenti fuori campo per le quali è possibile applicare un eccezione in fase di estrazione)
* A livello di assoggettamento è prevista l'esclusione manuale dello spesometro (suddivisa fra esclusione registrazioni clienti e registrazioni fornitori). Questa esclusione era già stata   utilizzata per il vecchio spesometro e quindi da ricontrollare per il nuovo spesometro.

## RAPPRESENTATE FISCALE
Se nella stampa fattura sono indicati i dati del rappresentate fiscale è necessario che nella trasmissione vengano indicati sia i dati del soggetto rappresentato che l'id paese ed il riferimento fiscale del rappresentante fiscale.

A standard è gestita solo questa situazione : 
* Un anagrafica cliente/fornitore italiano in cui come codice fiscale è stato indicato quello del rappresentate fiscale
* Su tale anagrafica deve essere aggiunta l'estensione £42 tramite cui verrà creato il legame con un anagrafica in cui verranno indicati i dati del soggetto rappresentato

Altre situazioni sarà necessario gestirle tramite exit.

## STABILE ORGANIZZAZIONE
Se nella stampa fattura è indicata la stabile organizzazione è necessario trasmettere sia i dati dell'impresa non residente che l'indirizzo della stabile organizzazione.

A standard è gestita solo questa situazione : 
* Un anagrafica cliente/fornitore con i dati della stabile organizzazione
* Su tale anagrafica deve essere aggiunta l'estensione £54 tramite cui verrà creato il legame con un anagrafica in cui verranno indicati i dati dell'impresa non residente

Altre situazioni sarà necessario gestirle tramite exit.

## ALTRE NOTE SU ANAGRAFICHE CLIENTI/FORNITORI
* Partita Iva Italiana, per enti italiani
* Partita Iva Estera, per enti esteri. La partita iva estera dovrà sempre iniziare con il codice nazione iso alpha 2 (sia intra che extra cee).
* Codice Fiscale, verrà preso in considerazione solo per enti italiani privi di partita iva.
* Comune
* Indirizzo
* Nazione
* Estensione £55 per escludere determinati soggetti

## IMPORTO DETRAIBILE E DEDUCIBILE
Questi importi presenti non vengono mai valorizzati. Si riferiscono a spese detraibili ed indeducibili, elementi che non sono al momento individuabili da smeup.
Vanno eventualmente mantenuti manualmente.

Tali dati è comunque importate notare sono facolativi (vedi Circolare 1/2017 dell'agenzia).

## FATTURE EMESSE IN COMUNI DELLA REPUBBLICA ITALIANA NON CONSIDERATI TERRITORIO DELLO STATO (LIVIGNO, CAMPIONE D'ITALIA)
In caso di soggetti passivi residenti nei comuni di Livigno e Campione d'Italia il programma di estrazione dello spesometro forzerà l'ID nazione con OO e compilerà il codice fiscale con il dato trovato sull'anagrafica del soggetto. Tale automatismo verrà attivato tramite il controllo del codice comune riportato sull'anagrafica del soggetto che dovrà essere E621 per Livigno e B513 per Campione d'Italia,
Sarà, quindi, necessario verificare che le anagrafiche di clienti e fornitori stabiliti in questi due comuni abbiano correttamente compilato il codice comune

## VARIAZIONE DI SOLA IMPOSTA
Per questa casistica, ovvero se nella riga iva è riportata solo l'imposta, senza indicazione dell'aliquota ed imponibile, viene settato il codice iva 99, come riportato nelle FAQ dell'agenzia delle entrate.

## ISOLE CANARIE (IC) e MELILLA (EA)
Per questa casistica, se idpaese è impostato a IC o EA, viene impostato come idpaese='OO' ed identificativo fiscale 99999999999, come riportato nelle FAQ dell'agenzia delle entrate.
