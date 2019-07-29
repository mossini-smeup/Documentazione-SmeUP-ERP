## OBIETTIVO

Qui di seguito vengono evidenziate una serie di casistiche particolari da prendere in considerazione prima di procedere con l'estrazione dei dati.

**NOTA BENE** :  qualora le soluzioni predisposte dallo standard non siano applicabili al contesto dall'azienda è importante notare che si potranno sempre implementare logiche alternative attraverso il programma di exit previsto per l'estrazione.

## NATURA DEGLI ASSOGGETTAMENTI

Per tutti gli assoggettamenti con aliquota zero, intra e reverse charge, è necessario che venga indicata la corrispondente natura.
Questa informazione va indicata nei parametri della tabella IVA (Classe parametri IVA) attraverso la gestione parametri o prevedendo che tale gestione venga richiamata in automatico con un flusso di post-inserimento/modifica della tabella IVA alla conferma di un elemento di tabella.
Attraverso il programma C5UTX62 è possibile far si che venga calcolata una proposta, ma tale proposta non è sufficiente a coprire tutti i casi. Per tale motivo è necessario che le varie casistiche vengano controllate puntualmente.
Qui di seguito una sintesi delle varie casistiche.

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

## ASSOGGETTAMENTI IVA (Tabella IVA)
Per gli assoggettamenti acquisti intra differenziare tra merci e servizi (campo T$IVA6)

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
* Comune
* Indirizzo
* Nazione
* Estensione £57 per escludere determinati soggetti

