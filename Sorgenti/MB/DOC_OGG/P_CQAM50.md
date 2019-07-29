# Obiettivo
Raccogliere in un archivio i dati di non conformità relativi ai lotti : 
 * acquistati;
 * in C.to lavoro;
 * di produzione;
 * resi da clienti;

in modo da : 
 * produrre per ogni lotto un documento riepilogativo delle non conformità rilevate;
 * assegnare ad ogni non conformità, un difetto, una causa del difetto, ed un parametro di merito legato all'importanza del difetto rilevato;
 * identificare, l'articolo, l'ente responsabile della non conformità;
 * evidenziare il danno economico associato alla non conformità.

## Formato guida
![CQ_NCNF_03](http://localhost:3000/immagini/MBDOC_OGG-P_CQAM50/CQ_NCNF_03.png)
 * _2_il numero documento
è un codice che in presenza del lotto è automaticamente riportato (la sua utilità in questo caso è superflua); nel caso in cui non è specificato il lotto il numero del documento permette di identificare in modo inequivocabile la registrazione della non conformità

 * _2_il codice lotto
è un'informazione che lega il seguito delle fasi operative a quello specifico lotto; questo serve chiaramente quando esiste un lotto a cui la non conformità che si vuole dichiarare, appartiene.Può accadere invece che ciò su cui è stata riscontrata la non conformità non appartenga specificatamente ad un lotto; è giustamente lasciata la libertà di annullare il campo del codice lotto e inserire solo il nome/codice del documento di registrazione;

Dato un documento viene presentata la lista di tutte le non conformità riscontrate sul lotto, oppure per quel documento, documentate fino a quel momento : 
![CQ_NCNF_04](http://localhost:3000/immagini/MBDOC_OGG-P_CQAM50/CQ_NCNF_04.png)
 * Qualsiasi non conformità riscontrata su quel documento viene proposta con una serie di informazioni di riepilogo sul lotto stesso (il modulo è in collegamento con l'anagrafica dei lotti) e sulle caratteristiche delle non conformità (tipo, fase di lavorazione e collaudo, se esistono). Questo tipo di legame tra il lotto e le non conformità rilevate è di fondamentale importanza per il soddisfacimento della norma che richiede una chiara documentazione sui prodotti, macchine, lotti coinvolti dalle difettosità riscontrate.
 * E' possibile entrare in variazione nelle singole sezioni del documento per aggiornare o modificare i dati raccolti.
 * Nel caso in cui si debba registrare una nuova non conformità relativa ad un lotto, è richiesto di specificare la fase di lavorazione e collaudo nella quale si è riscontrata la difettosità.
 * E' previsto inoltre che ad un lotto per cui non sia esplicitamente collegata una fase di collaudo o lavoro (vedi il caso di lotti di acquisto o di prodotti finiti ai quali non è imputabile una singola fase) inserire un codice Jolly (**) che permetta di identificare univocamente la non conformità.

## Formato di dettaglio
![CQ_NCNF_05](http://localhost:3000/immagini/MBDOC_OGG-P_CQAM50/CQ_NCNF_05.png)
Collegandosi con l'anagrafica dei lotti ed eventualmente con il modulo di dichiarazione dei collaudi  se si sta trattando di una difettosità riscontrata durante una prova di collaudo, il programma è in grado di recuperare le informazioni relative a : 
 * _3_articolo :  codice, descrizione, classe funzionale;
 * _3_planner;
 * _3_esponente di modifica dell'articolo;
 * _3_reparto;
 * _3_fase di lavorazione, (se esiste) a cui è collegata la non conformità rilevata. Tale specificazione viene riportata in automatico se si è in fase di dichiarazione di collaudo durante la registrazione dei controlli e si documenta la non conformità attraverso il campo di Osservazioni al Collaudo;
 * _3_fase di collaudo, come per la fase di lavorazione;
 * _3_ente rilevatore, se è stato immesso nella dichiarazione di collaudo;
 * _3_ente collaudatore, se è stato immesso nella dichiarazione di collaudo;
 * _3_importanza della caratteristica, che, se esiste un ciclo di collaudo, il programma acquisisce dalla fase corrispondente in cui è obbligatoriamente specificata;
 * _3_numero del lotto, a cui appartiene l'articolo;
 * _3_numero d'ordine; nel caso in cui sia specificato ad esempio il numero di ordine di produzione nei dati relativi ad un lotto, il codice viene qui riportato con il relativo numero di riga a cui si fa riferimento;
 * _3_numero della commessa, nel caso in cui il lotto faccia parte di una commessa;
 * _3_quantità, in fase di registrazione dei collaudi il programma riporta in automatico le quantità del lotto;
 * _3_ricorrenza del difetto; del difetto è possibile visitarne la "storia" tramite questo campo; ci si collega, aprendo le opportune finestre, con l'archivio dei difetti e si consulta la loro ricorrenza in riferimento all'articolo e per la combinazione articolo/ente (sul documento delle non conformità sono riportate in sintesi tali ricorrenze tramite due numeri separati da un tratto).

Viene richiesto di specificare : 
 * _3_codice del difetto, è un campo tabellato CQD che identifica il codice del difetto riscontrato;
 * _3_classe del difetto, è una specificazione che il programma legge dalla tabella CQD e riporta in automatico. A questa tabella è associato il valore del difetto e l'opzione legata all'obbligo di definire l'azione sulla prossima consegna;
 * _3_gravità, che il programma propone in automatico leggendolo dalla tabella CQD (è logico associare ad un difetto la relativa gravità) :  è comunque un parametro modificabile.
_2_Nota; ad ogni classe di difetto e per ogni livello di gravità viene assegnato un valore numerico di demerito come ad esempio da seguente prospetto : 
![CQ_NCNF_06](http://localhost:3000/immagini/MBDOC_OGG-P_CQAM50/CQ_NCNF_06.png)I demeriti sono parametri che vengo impiegati nella definizione degli indici di qualità che servono per il Controllo di Qualità. In genere infatti il Controllo Qualità deve esporre quando richiesto dalla Direzione e/o dalle Funzioni interessate i risultati delle verifiche effettuate : 
 - per tipo di prodotto (_1_Indice di Qualità Prodotto);
 - per l'intera produzione (_1_Indice di Qualità Aziendale);
 - per il fornitore (_1_Indice di Qualità del Fornitore);
 - per il parco fornitori (_1_Indice di Qualità delle Forniture).

A completamento di questo il Controllo Qualità deve essere in grado di fornire dati relativi a : 
 - la tipologia dei difetti rilevati;
 - il peso con cui hanno inciso sul risultato finale;
 - la ripartizione, per Funzione, dei demeriti rilevati con le rispettive causali;

 * causa del difetto, è un campo tabellato CQC che codifica la causa del difetto;
 * Caus.Acc, è un campo tabellato CQN che codifica l'accertamento della causa del difetto (è stato accertato, non è stato accertato che quella specificata sia la reale causa del difetto, ecc..)
 * tipo di non conformità, è un campo tabellato CQE che contiene informazioni legate alla costificazione della non conformità. In base al tipo il programma esegue una serie di calcolazioni su parametri impostati da tabella direttamente dall'utente  e produce in uscita come risultato il costo unitario della non conformità che compare nella finestra dei costi. Il tipo determina anche la forzatura nell'esito dei controlli.

Vediamo in dettaglio i campi che sono riportati in basso : 
![CQ_NCNF_07](http://localhost:3000/immagini/MBDOC_OGG-P_CQAM50/CQ_NCNF_07.png)
### Quantità
Tramite il campo Quantità l'operatore può registrare il riassunto delle quantita che ha rilevato distinguendole nelle differenti classi (scarti, accettati in deroga...)
![CQ_NCNF_08](http://localhost:3000/immagini/MBDOC_OGG-P_CQAM50/CQ_NCNF_08.png)
Automaticamente viene controllata l'esattezza dei dati introdotti ed è proposto un riepilogo sull'intero lotto.

### Costi
Il campo dei Costi permette di specificare il costo complessivo che ha comportato la non conformità distinto secondo le voci proposte : 
![CQ_NCNF_09](http://localhost:3000/immagini/MBDOC_OGG-P_CQAM50/CQ_NCNF_09.png)
E' messo in evidenza il costo unitario; quest'ultimo è ricavato in base al tipo di non conformità (costo primo, costo industriale...contenuti nell'archivio dei prezzi) e all'articolo.
Tale costo viene moltiplicato per il numero di pezzi che sono risultati non conformi ed il risultato sommato per le voci di costo specificate nella tabella soprariportata.
Questa finestra permette quindi di quantificare il costo della non conformità tenendo conto dell'entità del difetto, del valore del prodotto a quella fase della lavorazione e di tutte le spese sostenute per affrontare la non conformità in termini di tempo, addebiti/accrediti del fornitore.

### Dati per addebito/accredito
Una finestra molto importante dal punto di vista della conformità del programma alla norma è la seguente : 
![CQ_NCNF_10](http://localhost:3000/immagini/MBDOC_OGG-P_CQAM50/CQ_NCNF_10.png)
Le prime due voci evidenziate portano di Default il codice dell'articolo e del lotto; tramite l'interrogazione (/) è possibile collegarsi con la distinta base del prodotto, scandire tutti i sui componenti  ed individuare il responsabile della non conformità.

Se, ad esempio, accade che durante il collaudo finale venga riscontrato un difetto imputabile ad un particolare interno, tramite la connessione con la distinta del prodotto è possibile riportare in questo campo il codice dell'articolo e del lotto responsabile.
Qualora l'azienda fosse dotata di un sistema di rintracciabilità, si potrebbe risalire al lotto (se è di acquisto si può risalire al fornitore originario e quindi addebitargli la responsabilità ed i costi) che ha causato il difetto.

C'è da sottolineare che in questo caso il programma non permette di specificare che lo scarto riguarda solo il particolare e non il complessivo (la registrazione dello scarto è associata al codice dell'articolo complessivo e quindi non è possibile registrare che sono stati scartati 10 componenti e non 10 complessivi) ciò è un problema quando si va a costificare l'entità dello scarto :  in genere infatti non si scarta l'intero prodotto ma si sostituisce semplicemente il componente; questa informazione non è specificabile dal programma.

Sempre se il fornitore ha una gestione di rintracciablità è possibile identificare tutti quei prodotti che sono coinvolti dalla non conformità riscontrata.

Esempio
Per la realizzazione di 1000 caldaie viene impiegato un articolo prelevato dal magazzino in lotti differenti tra cui il lotto N°100. Il cliente che acquista la caldaia, riscontra una difettosità. Il Q9000 supporta la fase di registrazione della non conformità :  tramite il modulo riportato precedentemente si visualizza la distinta base e si risale al codice del pezzo difettoso; da qui poi se esiste la gestione di rintracciabilità è possibile risalire al lotto 100 a cui apparteneva l'articolo responsabile quindi individuare tutte le caldaie coinvolte dalla difettosità. E'comunque importante ribadire che la competenza della rintracciabilità non può far parte di un pacchetto di qualità.

Riprendiamo la spiegazione della finestra relativa agli addebiti/accrediti : 
 * _3_Costo Non Conf.; è un campo numerico in cui in automatico viene riportato il totale che è stato calcolato come spiegato in precedenza in base alla numerosità ed al costo unitario. C'è la possibilità di modificare tale valore se l'ente competente lo ritiene inadeguato.
 * _3_ente di addebito/accredito; è un campo tabellato CN*TT con cui si identifica l'ente di addebito  della non conformità in termini di spesa.
 * _3_tipo di addebito/accredito; è un campo tabellato CQ*AD che permette di identificare il tipo di addebito (se da addebitare, accreditare o altro).
 * _3_stato Add./Acc.; è un campo tabellato CQX che riporta lo stato in cui si trova  l'addebito/accredito :  la registrazione dello stato è obbligatoria e non si procede  fino a quando non è stato compilato il campo e quelli ad esso logicamente legati. Se ad esempio si conferma lo stato di accordo dell'addebito/accredito è obbligatorio inserire la cifra totale.

Qualsiasi altra informazione legata all'addebito/accredito che si desidera allegare, può essere inserita tramite il consueto sistema di gestione delle note libere.

### Azioni sulle non conformità
La finestra che si apre descrive le azioni che si decide di associare al tipo di difetto per quella causa specifica. Se supponiamo che un difetto si presenti frequentemente sotto quella
causa l'ente responsabile (generalmente la Direzione Tecnica) ha la possibilità di descrivere una serie di operazioni correttive che permettono all'operatore di attivare opportune azioni di intervento per eliminare il problema.
Questa informazione rimane legata in modo indissolubile all'articolo per quel difetto sotto quella causa cosicchè quando il problema si ripropone all'operatore compaiono automaticamente i tipi di intervento che può eseguire.
![CQ_NCNF_11](http://localhost:3000/immagini/MBDOC_OGG-P_CQAM50/CQ_NCNF_11.png)
Per l'immissione delle azioni si utilizza il comando funzione F15 : 
![CQ_NCNF_12](http://localhost:3000/immagini/MBDOC_OGG-P_CQAM50/CQ_NCNF_12.png)I campi da gestire sono : 
 * sequenza è un campo numerico che scandisce la priorità di esecuzione delle attività, decisa dall'ente responsabile.
 * azione è il campo che descrive l'azione correttiva intrapresa

Il comando funzione F10 offre in più l'opportunità di vedere elencate (e naturalmente anche di consultarle) le azioni correttive che sono state adottate per quella non conformità, su quel dato articolo, sotto quella specifica causa e per quella fase di lavoro. Una volta che si è introdotta tramite la finestra degli interventi l'azione correttiva (vedere seguito) e si è terminata la sessione di lavoro, automaticamente viene registrato in questo campo. E' da sottolineare il fatto che la  finestra mostra l'insieme di tutte le azioni intraprese e non solo per quella
sessione di lavoro. E' una opzione comoda quando si desidera consultare velocemente lo stato dell'intervento per vedere se è stato evaso o meno.

### Esclusione dalla statistica
E' possibile decidere di escludere la registrazione della non conformità dal calcolo statistico che il programma effettua per la determinazione dei piani di campionamento (livelli di qualità) che
piani di campionamento). Ciò può risultare importante quando si è in presenza di situazioni speciali o anomale per cui si ritiene di non doverne tenere conto nel conteggio complessivo delle difettosità che riguardano un articolo. Il programma quindi, in questo caso dimostra di non essere di ostacolo alla pratica operativa che presenta quasi sempre gradi di libertà imprevedibili :  l'aspetto fondamentale di un software efficiente, al servizio dell'azienda, è rappresentato dall'assenza di vincoli immodificabili.

### Esclusione dal Vendor Rating
E' possibile, anche in questo caso, decidere di escludere, per un qualsiasi motivo, la dichiarazione della non conformità dal calcolo del Vendor Rating (Vedere la sezione specifica per i particolari sull'argomento).

### Stampa osservazioni sui collaudi
E' un campo di segnalazione della stampa di questo modulo (si rimanda alla sezione dedicata alla stampa).

### Intervento
Su questo campo si apre una finestra che, operativamente, è di fondamentale importanza : 
![CQ_NCNF_13](http://localhost:3000/immagini/MBDOC_OGG-P_CQAM50/CQ_NCNF_13.png)
Direttamente da questo modulo, l'operatore che riscontra la non conformità (che può essere il collaudatore, oppure se la difettosità avviene durante una fase di autocontrollo, l'addetto abilitato) attiva, quando lo ritiene necessario un'azione di intervento.
