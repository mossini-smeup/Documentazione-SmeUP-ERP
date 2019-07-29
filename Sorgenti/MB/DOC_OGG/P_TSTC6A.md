# OBIETTIVO

 Eseguire funzioni di analisi degli incassi/pagamenti

# PREREQUISITI
Controllare in modo preciso la corrispondenza tra causali tipi movimento utilizzati negli incassi/pagamenti, verificando che ci sia corrispondenza fra descrizioni e tipi movimento. Se è necessario intervenire sulle causali è  poi possibile utilizzare il pgm C5UT49A per adeguare i dati esistenti.
* Confrontare parole descrizioni con relativi tipi movimento
** Per tutte le causali legate a C5D con tipo movimento 05 / 06 vanno attribuite causali con tipo movimento 05 o 17
** Per tutte le causali di perdita su crediti vanno attribuiti tipi movimento 08
** Per tutte le causali di insoluto/protesto vanno attribuiti tipi movimento 04 / 09
** Per tutte le causali di abbuono/sopravvenienze vanno attributi tipi movimento 06
** Per tutte le causali di sconto finanziario vanno attributi tipi movimento 11

Altro prerequisito è che i movimenti di insoluto/protesto/richiamo abbiano l'indicazione della rata di effetto indicata nel campo S5IDPA. Anomalie relative a questa indicazione vengono segnalate nei messaggi della C6A e possono essere eventualmente corrette dall'utility C5UT53A (in assenza di questo collegamento i gg calcolati sull'insoluto e sugli effetti insoluti non verrebbero calcolati in modo preciso).

# FUNZIONE DATI DI SCANSIONE
## OBIETTIVO
Questa funzione permette di scandire dei movimenti di incasso/pagamento in un periodo.

## NOTE AGGIUNTIVE SULL'ELABORAZIONE
* L'ordine di scansione è il seguente : 
** La scansione parte dai dovuti movimentati nel periodo
** Per ognuno di questi verranno ritornati gli eventuali (se ve ne sono dunque) movimenti a saldo della partita (flag 11 = "-")
** A termine di tale scansione in presenza di un residuo verrà ritornato il movimento di dovuto con valorizzato il campo £C6AIN con l'importo che risulta da saldare a tale data.
* La scansione ritornerà quindi o i movimenti di regolamento (flag 11 = "-")  o i movimenti di dovuto che non risultano saldati alla data registrazione finale. Per quest'ultimi verrà valorizzato il campo £C6AIN con l'importo che risulta ancora da saldare a tale data. A questa regola vanno fatte però due eccezioni : 
** In presenza di rate di dovuto di anticipo o di esito effetti, questi dovuti al di là del residuo verranno ritornate dalla scansione una prima volta, con il campo £C6AIN=0 al solo scopo di permettere nel caso venisse eseguita la £C6A con funzione blank, di poter registrare l'evidenza di tali movimenti sugli importi di regolamento (entrambi i dovuti infatti vi influiscono, con segno positivo o negativo).
** Altre note particolari sono le seguenti : 
*** Un anticipo registrato con data precedente al periodo di analisi che è divenuto poi il regolamento di un movimento di dovuto registrato nel periodo in analisi verrà evidenziato come un dovuto pre-esistente saldato da se stesso.
*** Un movimento di regolamento registrato nel periodo che salda un movimento di dovuto registrato oltre il periodo in analisi verrà evidenziato come un dovuto da anticipo.
* Gli effetti che all'inizio del periodo di analisi risultano ancora da maturare verranno, ritornati come incassi maturati nel periodo (se la data di maturazione vi rientra). NOTA BENE :  per tale elaborazione la data di rischio viene sempre considerata la data successiva alla scadenza dell'effetto, quindi vengono considerati tutti gli effetti che hanno data scadenza maggiore o uguale alla data registrazione iniziale indicata.

## INPUT
* Azienda
* Codice Singolo Cliente/Fornitore o Lista di Clienti/Fornitori che saranno oggetto della scansione
* Tipo scansione
* Per data registrazione :  vengono analizzati tutti i movimenti registrati nel periodo considerando inoltre tutti le scadenze aperte o ancora da maturare prima dell'inizio del periodo (ho quindi una corrispondenza precisa con i movimenti del mastrino, apertura compresa.
* Per data documento :  vengono analizzati tutti i movimenti che fanno riferimenti ad una data documento compresa fra le date. Per tali movimenti vengono considerati gli incassi sino alla data indicata come data registrazione limite (assume data odierna). Questo criterio permette di controllare la situazione creditoria/debitoria dei documenti emessi in un certo periodo.
* Data Registrazione Iniziale/Finale (la finale se non indicata assume la data odierna)
* Data Documento Iniziale/Finale (controllata solo se tipo scansione per documento).

## OUTPUT
* Scaduto Precedente :  evidenzia il fatto che viene ritornato un movimento registrato nel periodo precedente alla data registrazione limite iniziale. Può assumere i valori : 
** "1" se si tratta di un dovuto che era da saldare
** "2" se si tratta di un effetto che doveva ancora maturare
* Importo da saldare :  se il movimento è di dovuto viene evidenziato l'importo ancora da saldare su di esso. E' da tenere conto che tale importo per un movimento di dovuto può essere a zero solo quando su movimenti di esito/anticipo si vuole evidenziare l'evidenza di un movimento che influisce sui regolamenti.
* DS della rata. NOTA BENE :  tale ds può subire delle variazioni rispetto a quanto effettivamente previsto nell'archivio, sulla base di quanto risulta dall'elaborazione. Esempi di questi interventi sono gli importi della scadenza ed il flag di dovuto/regolato che può essere invertito a causa del collegamento fra dovuti/regolamenti inclusi/esclusi dal periodo in esame.

# FUNZIONE DATI DI UN RATA

## OBIETTIVO
A partire da una scadenza e da alcuni parametri di riferimento permette di elaborare tale scadenza dal punto di vista dell'analisi degli incassi/pagamenti.

## NOTE SU CALCOLO DEI GIORNI
* Metodo di determinazione della data inizio dei giorni previsti/consuntivi : 
** La data a partire dalla quale inizia il calcolo può essere data o dalla data documento di riferimento della partita o dalla data inizio pagamento indicata sulla registrazione intestataria della partita (cioè quella partita che in testata ha indicato soggetto, n° e data documento della partita)
* Metodo di determinazione della data saldo prevista : 
** Se si tratta di un movimento di regolamento (fl11='-'), la data saldo prevista è data dalla data di scadenza indicata sul movimenti che quella rata va a saldare (cioè la rata indicata nel campo S5IDPA)
** Se si tratta di un movimento di insoluto/protesto/richiamo, la data saldo prevista è data dalla data di scadenza indicata sull'effetto all'origine del movimento (cioè la rata indicata nel campo S5IDPA. Qual'ora questo riferimento mancasse si può eseguire il C5UT53A per crearlo/ripristinarlo)
** Se si tratta di un qualsiasi altro movimento di dovuto, in attesa di essere saldato, la data di saldo prevista è data dalla scadenza indicata sul movimento stesso
* Metodo di determinazione della data saldo consuntiva : 
** Se si tratta di un effetto (fl24<>'') la data di saldo consuntiva è data dalla data scadenza indicata sull'effetto (tendendo conto che in caso di cumulo viene ripresa la data scadenza indicata sulla rata master, cioè quella indicata nel campo S5NROR)
** Per tutti gli altri casi, se è indicata una data valuta viene ripresa quella, viceversa, viene ripresa la data registrazione.
* Metodo di determinazione dei gg di ritardo : 
** Se il movimento è stato regolato, viene calcolata la differenza fra la data saldo prevista e la data saldo effettiva.
** Se i movimenti non sono stati regolati, viene calcolata la differenza fra la data saldo prevista e la data registrazione finale di riferimento. NOTA BENE :  per questa casistica i gg consuntivi non verranno calcolati (non essendoci il saldo), ma verranno comunque calcolati i gg di ritardo.
* Per alcune situazioni, i giorni vengono forzati a zero : 
** Qual'ora la differenza dei giorni fra le date fosse negativa (es. regolamento in anticipo)
** Se il regolamento corrisponde ad un effetto esitato (insoluto/protesto/esito)
** Sulle forme di chiusura di una partita, che non corrispondono ad un incasso (pagamenti, a costo/ricavo, pareggi, ad altro). NOTA BENE :  sui pareggi si fa questo assunto :  se anche dietro al pareggio ci fosse un anticipo il fatto che l'anticipo non sia collegato direttamente alla fattura dovrebbe implicare che l'anticipo (come dovrebbe indicare il termine) è stato inserito prima della fattura e quindi in anticipo rispetto alla fattura e quindi senza giorni di ritardo.
** Sui dovuti ancora da saldare che non hanno segno dare

## NOTE AGGIUNTIVE SULL'ELABORAZIONE
* Il rischio viene sempre calcolato forzando come data rischio la data successiva alla data registrazione limite (in modo che tutto quello che scade nel periodo sia considerato maturato). Se voglio quindi quadrare il risultato con lo scadenzario, nella data rischio dell'interrogazione dello scadenzario devo appunto forzare il giorno successivo alla data situazione (es. data situazione scadenzario 31/12/nn, data rischio 01/01/nn+1)

## INPUT
* Rata :  Identificativo della rata da analizzare
* DS Rata :  Se valorizzato invece che essere utilizzata la rata del campo precedente viene utilizzato il record passato in input nella DS C5RATE
* Data Registrazione Iniziale/Finale (la finale se non indicata assume la data odierna)
* Calcola da Incassare :  se passato non vengono elaborate solo i movimenti di incassato, ma anche i movimenti ancora da incassare. Questo flag dovrebbe essere valorizzato solo qual'ora, la scadenza non derivi dalla funzione di scansione (in questo caso la scansione valorizza già i modo opportuno tale informazione).
* Forza Data Limite Inizio come Scadenza Contrattuale Minima :  Se passata per il calcolo del ritardo invece il  calcolo dei gg non viene fatto rispetto alla date reali ma rispetto alla data limite iniziale se le date reali sono precedenti ad essa.

## OUTPUT

* Data Inizio Dilazione :  come data di riferimento viene ripresa o la data del documento o se indicata la data inizio pagamento della testata della registrazione del documento
* Data Scadenza Contrattuale :  per le rate da incassare è la data scadenza della rata stessa, mentre per le rate di incassato è la data di scadenza della rata saldata. Se questa non viene reperita, non verrà calcolato il ritardo.
* Data di Incasso Effettivo :  data presa in considerazione per l'incasso. Questa viene determinata nel seguente modo : 
** Per gli effetti (esclusi gli assegni) è la data di scadenza. Nel caso in cui una rata sia cumulata viene presa in considerazione la data di scadenza della master.
** Per tutto il resto se è indicata una data di valuta, viene presa in considerazione questa, altrimenti viene presa la data di registrazione.
* GG di Incasso Contrattuale :  Differenza fra "Data Scadenza Contrattuale"-"Data Inizio Dilazione"
* GG di Incasso Consuntivi :  Differenza fra "Data Incasso Effettivo"-"Data Scadenza Contrattuale"
* GG di Ritardo :  Differenza fra i due precedenti calcoli, applicato solo se la i gg consuntivi sono maggiori dei gg contrattuali e solo se la scadenza è positiva (a meno che ci sia la forzatura specifica)
* Effetto :  viene valorizzato ad 1 se è un effetto, con 2 indica che è un effetto ma che non è una rata master
* Origine
**  Id :  identificativo della rata di dovuto all'origine del credito/debito maturato
** Tipo movimento :  tipo movimento della rata di dovuto all'origine del credito/debito maturato
** Causale :  causale della rata di dovuto all'origine del credito/debito maturato
** Registrazione :  nr registrazione contabile della rata all'origine del credito/debito maturato

* **Importo Dovuto** :  importo corrispondente ai crediti/debiti maturati nel periodo in analisi e nel caso in cui l'elaborazione sia effettuata secondo il criterio della data registrazione, anche agli importi da saldare/maturare pre-esistenti all'inizio del periodo.
** **Dovuto da Documento** :  è un di cui dell'importo dovuto, in cui vengono evidenziati i crediti/debiti maturati nel periodo che sono stati originati dall'emissione di un documento
** **Dovuto da Esito** :  è un di cui dell'importo dovuto, in cui vengono evidenziati i crediti/debiti maturati nel periodo per effetto dell'esito di un effetto (Insoluto/Protesto/Richiamo)
** **Dovuto da Anticipo** :  è un di cui dell'importo dovuto, in cui vengono evidenziati i crediti/debiti maturati nel periodo per effetto di corrispettivi effettuati in anticipo
** **Dovuto da Altro** :  è un di cui dell'importo dovuto, vi rientrano tutti i crediti/debiti maturati che non rientrano nelle precedenti casistiche.
* **Importo da Saldare** :  evidenzia la quota parte dei dovuti maturati nel periodo in esame che non sono ancora stati saldati (nell'analisi per data registrazione, questo importo corrisponde al saldo finale dello scadenzario)
** **Importo Scaduto** :  è un di cui dell'importo da saldare, in cui vengono evidenziati gli importi non saldati che sono scaduti
** **Importo a Scadere** :  è un di cui dell'importo da saldare, in cui vengono evidenziati gli importi non saldati che sono ancora a scadere
** **Importo a Debito** :  è un di cui dell'importo da saldare, in cui vengono evidenziati gli importi non saldati che rappresentano dei debiti (tali importi non vengono inclusi nei due precedenti numeri)
* **Importo Regolato** :  evidenzia la quota parte dei dovuti maturati nel periodo in esame che corrisponde agli incassi/pagamenti effettuati nel periodo
** **Importo Incassato** :  è un di cui dell'importo regolato, in cui vengono evidenziati gli incassi (entrata di denaro)
** **Importo Esitato** :  è un di cui dell'importo regolato, in cui vengono evidenziati gli importi che sono stati esitati (effetti insoluti/protestata/richiamati)
** **N° Contatore Esiti** :  è un contatore del n° di esiti maturati nel periodo
** **Importo Pagato** :  è un di cui dell'importo regolato, in cui vengono evidenziati i pagamenti (uscita di denaro)
* **Importo a Costo/Ricavo** :  evidenzia la quota parte dei dovuti maturati il cui saldo si è tradotto in un costo/ricavo aggiuntivo (perdite, abbuoni, oscillazioni ecc.)
** **Abbuoni/Oscillazioni** :  è un di cui dell'importo a costo/ricavo, in cui vengono evidenziati gli importi generati da abbuoni o oscillazioni cambio.
** **Sconti** :  è un di cui dell'importo a costo/ricavo, in cui vengono evidenziati gli importi generati da sconti
** **Perdite** :  è un di cui dell'importo a costo/ricavo, in cui vengono evidenziati gli importi generati da perdite
* **Importo a Pareggio** :  evidenzia la quota parte dei dovuti maturati il cui saldo si è tradotto con un movimento di pareggio con un'altra posta di segno opposto.
* **Importo a Rischio** :  evidenzia la quota parte dei dovuti maturati il cui saldo si è tradotto in un effetto la cui maturazione avverrà in un periodo successivo a quello in esame. NOTA BENE : 
** **Quadratura** :  ha il solo fine di evidenziare il fatto che l'operazione aritmetica Importo Dovuto - Importo da Saldare - Importo Regolato - Importo a Costo/Ricavo - Importo a Pareggio - Importo a Rischio è pari a Zero.
* **Regolato in Ritardo** :  è un di cui dell'importo Regolato in cui vengono evidenziati i regolamenti che sono avvenuti in ritardo, rispetto alla scadenza prevista

# FUNZIONE DSO

Il DSO è un indice che misura i crediti in vendite ancora da incassare. Esistono alcuni metodi alternativi per determinarlo. In questo caso è stato utilizzando il metodo "a gambero" o "count-back" con anno commerciale. Attraverso esso il numero dei gg viene determinato sottraendo a ritroso, il fatturato dall'esposizione. Per l'ultimo mese determinato (salvo vi sia corrispodenza perfetta) il numero dei gg viene calcolato in questo modo :  30/fatturato del mese*importo scalato dall'esposizione.
