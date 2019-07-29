# M51 - Pianificazione materiali
## OBIETTIVO
Definisce i parametri generali relativi alla pianificazione materiali
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Elemento
È un elemento fisso.
 :  : FLD T$M51A __Tipo / Parametro codice di rottura__
Il tipo ed il parametro dell'oggetto di rottura definiscono il codice che, insieme con l'articolo e il magazzino, individua l'elemento unitario di pianificazione.
Può essere uno dei seguenti oggetti : 
-    commessa
-    configurazione
-    esponente di modifica
-    ente (tipo e parametro)
Sarà poi, una caratteristica di ogni singolo articolo (definita nella sua politica), il fatto che ad esso si aggiunga il codice di rottura, con la possibilità di definire un comportamento a rottura a livello aziendale.
**NB** :  nel caso di pianificazione a rottura di ente, saranno trasferiti nel codice di rottura solo i codici enti delle fonti, con tipo ente uguale al parametro di rottura definito in questa tabella.
 :  : FLD T$M51B.T$M51A
 :  : FLD T$M51W __Intestazione oggetto di rottura__
È significativo se impostato l'oggetto di rottura. Se impostato, questa intestazione sostituisce la descrizione naturale dell'oggetto di rottura, ovunque essa appaia.
 :  : FLD T$M515 __Tempo rettifica lavorazione__
Normalmente, nella datazione degli impegni (sia pianificati che rilasciati) si tiene conto del tempo di rettifica, presente nel legame di distinta base (che sostituisce totalmente gli altri tempi di approvvigionamento), solo se gli impegni sono di produzione interna. Nel caso siano impegni di lavorazione, esso viene trascurato, per avere la stessa data su tutti gli impegni e impostare un'unica spedizione, indipendentemente dal tempo inserito nel legame.
Se, invece, si imposta questo carattere, il tempo di rettifica viene trattato anche negli impegni di lavorazione. Un esempio è il caso in cui l'emissione dell'ordine (per motivi di programmazione interna del terzista) deve essere molto anticipata rispetto all'invio dei materiali.
 :  : FLD T$M51C __Attivazione Scenari__
Se impostato, possono essere presenti diversi ambienti di pianificazione contemporaneamente (su diversi scenari) :  in questo caso, prima di ogni funzione della pianificazione viene richiesto lo scenario.
Gli scenari sono impostati nella tabella M5B (in cui è fissato l'oggetto di riferimento della pianificazione). Deve sempre essere presente lo scenario master '**'. In un ambiente monoscenario viene assunto in modo automatico. In un ambiente multiscenario, nell'applicazione dei suggerimenti viene forzata la gestione monoscenario, in modo che l'applicazione avvenga unicamente dallo scenario master. In questo modo si evita il pericolo di applicare più volte
gli stessi suggerimenti, da scenari diversi.
 :  : FLD T$M513 __Tempo fittizi__
Se impostato, il tempo di approvvigiamento dei codici fittizi (o resi tali nel legame) si aggiunge a quello dell'assieme (o quello di rettifica del legame) per datare gli impegni pianificati.
Viene assunto unicamente il tempo di approvvigionamento fisso di produzione.
Se presenti più fittizi in cascata, i tempi vengono sommati.
**NB** :  questa azione viene eseguita unicamente nella datazione degli impegni pianificati. Per ottenere lo stesso risultato nella datazione degli impegni rilasciati bisogna impostare il flag in tabella P51.
 :  : FLD T$M51D __GG lavorativi in produzione, acquisti e c/lavoraz.__
Se questo campo è diverso da blank, per ognuno dei tre possibili ordini pianificati, i tempi di approvvigionamento vengono considerati giorni lavorativi; altrimenti giorni di calendario.
La risorsa assunta (tipo e codice) da cui acquisire il calendario, è quella impostata nella tabella del magazzino dell'ordine che si sta pianificando.
 :  : FLD T$M51E.T$M51D
 :  : FLD T$M51F.T$M51D
 :  : FLD T$M51K __GG lavorativi in transito__
Indica il calendario da utilizzare per i tempi di transito tra i vari plant.
I valori possibili sono : 
- ' '  Verrà utilizzato il calendario solare
- '1'  Verrà utilizzato il calendario del plant di partenza
- '2'  Verrà utilizzato il calendario del plant di arrivo
- '3'  Verrà utilizzato il calendario dell'ente interno associato al plant di partenza
- '4'  Verrà utilizzato il calendario dell'ente interno associato al plant di arrivo.
Nel caso dei valori 3 e 4, se non è specificato nella tabella MAG l'ente interno, verrà utilizzato il calendario del plant di partenza/arrivo (corrispondenti alle scelte 1 e 2)
 :  : FLD T$M51G __Politica assunta produzione__
È un elemento della tabella M5A. Va obbligatoriamente impostato :  è la politica di pianificazione che assume un articolo di tipo parte con radice minore o uguale a '2', se non è stato definito nessun valore specifico, a nessun livello, nei dati di pianificazione.
 :  : FLD T$M519 __Tipo risorsa per calendario per ente__
È un elemento della tabella TRG :  se impostato deve puntare ad un tipo oggetto ente (CN). In tal caso, sia nella datazione degli ordini e impegni pianificati, sia di quelli rilasciati, si userà il calendario dell'ente.
 :  : FLD T$M51H __Politica assunta acquisti__
È un elemento della tabella M5A :  va obbligatoriamente impostato.
È la politica di pianificazione che assume un articolo di tipo parte con radice maggiore a '2', se non è stato definito nessun valore specifico, a nessun livello, nei dati di pianificazione.
Va ricordato che, a livello generale, se non specificato in dettaglio nei parametri di pianificazione, il sistema non pianifica ordini di lavorazione esterna.
 :  : FLD T$M51X __Appuntamenti__
È un valore V2/SI/NO. È significativo in caso di pianificazione logistica (codice di rottura 'ente') e se scelto di considerare il calendario per ente.
Se impostato, viene garantita la congruenza (entrambe devono essere lavorative, ciascuna per il proprio ente) tra la data di consegna dell'ordine pianificato e la data dell'impegno che esso soddisfa, in modo che si possa eseguire la spedizione tra i due enti.
 :  : FLD T$M51I __Ammessi aumenti.__
Attualmente questa possibilità non è  implementata.
 :  : FLD T$M510 __Modo risalita.__
Si imposta il modo in cui viene eseguita la risalita nel reperimento dei parametri di pianificazione (politiche, tempi e lotti).
Sono ammessi i seguenti valori : 
- ' '  Vengono assunti tutti i valori dal primo record presente
- 'P'  Vengono assunte le politiche dal primo record che contiene una poltica; vengono assunti i tempi e i lotti dal primo record che contiene un tempo o un lotto.
- 'T'  Vengono assunti i tempi dal primo record che contiene un tempo; vengono assunte le politiche e i lotti dal primo record che contiene una politica o un lotto.
- 'L'  Vengono assunti i lotti dal primo record che contiene un lotto; vengono assunte le politiche e i tempi dal primo record che contiene una politica o un tempo.
- 'S'  Vengono assunte le politiche, i tempi e i lotti, rispettivamente dal primo record che contiene una politica, un tempo e un lotto.
 :  : FLD T$M51L __Ricalcolo livello minimo.__
È un elemento della V2/ESDIS. Se impostato, prima della pianificazione globale, viene eseguito il ricalcolo del livello minimo, con il tipo esplosione qui specificato :  nel caso di distinta configurata può essere il caso di eseguire un'esplosione di produzione.
Se la distinta ha dei criteri di validità impostati, è conveniente fare una esplosione di tipo 2,
ossia scalare, per essere sicuri di percorrere tutte le possibilità.
Per quanto riguarda la validità dei legami per data invece, il programma di calcolo LLC è
impostato per scandagliare tutte le date possibili.
 :  : FLD T$M51M __Tipo distinta__
È un elemento della tabella BRL :  (se assente viene assunto 'ART') :  è il tipo distinta il cui livello minimo è la sequenza di scansione della pianificazione.
L'eventuale ricalcolo del livello minimo viene eseguito su questo tipo distinta.
Il tempo di approvvigionamento cumulato (per avanzare la scorta minima) viene reperito da questo tipo distinta.
 :  : FLD T$M51N __Periodicità__
È un elemento della tabella A£Q :  è il valore assunto per le politiche con raggruppamento per periodicità, se non specificato a livello di politica (tabella M5A).
 :  : FLD T$M51O __Spostamento a giorno lavorativo__
Indica come "aggiustare" la data di partenza, nel calcolo delle date tramite i giorni di approvvigionamento, se essa non è lavorativa (ed è stato richiesto il calcolo per giorni lavorativi).
Se vale ' ' la data  viene spostata all'ultimo giorno lavorativo precedente.
Se vale '1' la data  viene spostata al primo giorno lavorativo successivo.
Se vale '2' la data  viene spostata : 
- al primo giorno lavorativo successivo nella funzione "AVANTI"
- all'ultimo giorno lavorativo precedente nelle funzioni "INDIET" o "RETTIF"
Quest'ultima modalità è particolarmente utile in presenza di ATP che si traduce in MRP, per evitare
sporadiche incongruenze (ad esempio a cavallo di giorni di chiusura). L'MRP infatti lavora al più
tardi, mentre l'ATP al più presto.
La funzione sopracitata è relativa alla routine £M5T  (calcolo date da tempi di approvvigionamento.
 :  : FLD T$M51J __Modalità pianificazione multimagazziono__
È un elemento della V2/M5TPM. È significativo se l'applicazione è multimagazzino. Riferirsi all'aiuto specifico per le possibilità offerte.
 :  : FLD T$M51P __Fonte assunta per punto di riordino__
È un elemento della tabella M5E :  è la fonte che viene assunta nella scrittura dell'impegno del punto di riordino, negli articoli gestiti in questo modo. Deve avere, come origine fonte, 'PR'.
Ricordiamo che un articolo, per essere pianificato a punto di riordino, deve possedere TUTTE le seguenti caratteristiche : 
- avere una politica con "modo di pianificazione" a punto di riordini
- avere valorizzati i campi "Punto di Riordino" e "Lotto Economico" nei dati "Magazzino/Articolo"
Deve inoltre essere presente la presente fonte di punto di riordino, correttamente tipizzata.
Se almeno una delle precdenti condizioni non si verifica, l'articolo viene pianificato comunque a fabbisogno.
È necessario ricordare che non si deve specificare, nel gruppo fonti, una fonte a punto di riordino, o addirittura, per gli articoli gestiti a punto di riordino, impostare un gruppo fonti apposito che la contenga.
Il comportamento del sistema è il seguente :  se la politica è a punto di riordino, viene letto dai valori di articolo/magazzino il punto di riordino stesso, ed aggiunto esplicitamente un elemento di impegno che ha, come fonte M5E, il codice impostato al valore qui definito.
Se una fonte a punto di riordino è impostata in un gruppo fonti di una politica a fabbisogno, essa ha l'effetto di una scorta minima (impegno ad oggi).
Se è impostata in una politica a punto di riordino, non ha nessun effetto, essendo esclusi dal calcolo gli impegni, ad eccezione del punto di riordino aggiunto esplicitamente, come esposto in precedenza.
 :  : FLD T$M518 __Trattamento scaduti__
È un valore V2/M5ANT :  stabilisce i casi in cui non viene applicata la lottizzazione alla quantiità di un ordine pianificato.
Fare riferimento all'aiuto di questo valore per dettagli sulle modalità esecutive.
Nel record del consiglio viene segnalato se è scaduto :  è possibile dare solo segnalazione (continuando a lottizzare).
 :  : FLD T$M51Q __Pianificazione a codice di rottura__
Viene assunto se lasciato in bianco il flag a livello di singola politica.
Se impostato, tutti gli articoli saranno pianificati separatamente, per il codice di rottura definito in precedenza in questa stessa tabella; in questo modo si evita di specificare questa informazione su tutte le politiche.
Può essere utile, ad esempio, per una azienda che pianifica tutti i codici a commessa ed imposta una commessa fittizia, che raccoglie i codici non assegnati alle commesse operative.
Un altro caso è quello in cui si pianificano per configurazione solo gli articoli che la contengono; in questo modo tutti i codici sono pianificati per configurazione. Un caso particolare è quello dei codici con configurazione a blanks. Così facendo si evita di duplicare le politiche per separare i codici pianificati a rottura da quelli pianificati globalmente.
Questo non vale nel caso in cui la configurazione fa rottura solo per alcuni codici :  l'informazione va riportata separando le politiche.
 :  : FLD T$M51R __Scorta dopo tempo di approvvigionamento__
Può assumere i valori : 
- '1'  Spostamento dopo tempo approvvigionamento del livello, della politica master.
- '2'  Spostamento dopo tempo approvvigionamento cumulato :  in questo caso si assume, per determinarlo, il tipo distinta impostato in precedenza in questa tabella.
Se impostato, le fonti di scorta non vengono poste alla data di pianificazione, ma spostate in avanti del tempo di approvvigionamento selezionato.
Il fatto di trattare giorni lavorativi o di calendario dipende dal tipo di politica master (PR/AQ/LV) e da quanto impostato nella presente tabella (vedi 'giorni lavorativi in produzione / acquisti / lavorazione').
Questo spostamento viene eseguito esclusivamente sulle fonti che hanno come origine la scorta; le giacenze negative vengono comunque trattate come fabbisogni ad oggi.
!!! ATTENZIONE !!!
Questa opzione viene trascurata se abilitato il DRP. In questo caso bisogna ricorrere alla scorta
datata.
 :  : FLD T$M51S __Fonte per eccedenza presente__
È un elemento della tabella M5E :  viene assunto se non impostato a livello di politica specifica (tabella M5A).
Riferirsi ad essa per la documentazione di questo parametro.
 :  : FLD T$M516 __Trattamento scarti__
È un valore V2/DBSCA :  definisce la modalità del trattamento degli scarti nell'esplosione della distinta base, all'atto della generazione degli impegni pianificati.
 :  : FLD T$M51T __Fonte per eccedenza futura__
È un elemento della tabella M5E :  viene assunto se non impostato a livello di politica specifica (tabella M5A).
Riferirsi ad essa per la documentazione di questo parametro.
 :  : FLD T$M517 __Arrotondamento da unutà di misura__
Èun valore V2/SI/NO :  se impostato, nella generazione degi impegni pianificati, la quantità dei componenti verrà arrotondata secondo quanto definito nella tabella della sua unità di misura.
 :  : FLD T$M51U __Tipo e parametro di pianificazione per riferimento__
Si imposta il tipo e il parametro dell'oggetto di riferimento a cui si possono intestare i parametri di pianificazione (politiche/tempi/lotti), che sostituiranno, se la politica lo prevede, i parametri definiti a livello di articolo.
Si può scegliere tra : 
- E :  Ente (in questo caso biosgna impostare anche, nel parametro, il tipo dell'ente, da tabella BRE).
- C :  Commessa.
- F :  Configurazione (in questo caso, se si imposta un carattere x nel parametro, verrà lanciato il programma M5M5A0_Fx, che permette di usare solo una parte di configurazione (eventualmente modificata) nell'assegnazione del parametri di pianificazione).
 :  : FLD T$M51Z.T$M51U
 :  : FLD T$M51V __Suffisso pgm. di aggiustamento__
Il primo carattere è relativo all'aggiustamento in fase di pianificazione :  viene assunto se non impostato a livello di politica specifica (tabella M5A). Riferirsi ad essa per la documentazione di questo parametro.
Il secondo carattere è relativo all'aggiustamento sulle fonti rilasciate. Se impostato, è il suffisso x del programma 'M5M5R0I_x', che viene lanciato prima della scrittura dei consigli, con in linea il record di consigli e la DS dell'analisi disponibilità (£M5DDS). In questo modo è possibile inserire nel record dei consigli informazioni specifiche che potranno essere utili nella consultazione della pianificazione.
Attenzione :  questo aggiustamento NON ha effetto sulla pianificazione, in quanto le informazioni ritornate dall'analisi disponibilità hanno due sbocchi : 
- la memorizzazione in schiere per l'esecuzione dell'MRP
- la scrittura in M5CONS
Il presente aggiustamento si effettua soltanto sulla scrittura del record, per scopi unicamente
documentativi nella successiva consultazione.
Questo secondo carattere è inoltre utilizzato come suffisso del programma di aggiustamento 'M5M5R0J_x' che permette, durante la scansione di disponibilità per la pianificazione, di scartare o di datare in modo personale le fonti attuali negative.
Ricordiamo che normalmente esse vengono datate alla data di lancio della pianifcazione o, se di origine scorta, a questa data avanzata del tempo di approvvigionamneto (se impostata la correizone in questa tabella).
Lo stesso carattere è utlizzato anche per il programma di aggiustamento 'M5M5R0Y_x' che permette di modificare (o di escludere, azzerando la quantità fonte) un record ritornato dall'analisi disponibilità eseguita durante il caricamento dei dati di input della pianificazione.
 :  : FLD T$M51Y.T$M51V
 :  : FLD T$M511 __Richieste fisse__
Se impostate, fissano e rendono immodificabili le impostazioni del lancio della pianificazione.
Nel primo carattere si può impostare : 
1    -    Pianificazione totale.
2    -    Pianificazione parziale.
Nel secondo carattere si può impostare : 
1    -    Singolo articolo.
2    -    Singola commessa.
3    -    Set di articoli.
_9_Esempio :  si può decidere che la pianificazione avverrà sempre per commessa singola, impostando rispettivamente i codici '2' e '3'.
Se sono impostati valori incongruenti, tali da produrre un errore bloccante, bisogna variare questa tabella :  non sono modificabili, nemmeno se errati, nel formato del lancio della pianificazione.
Infatti la loro presenza sta a significare l'intenzione di limitare le possibilità di esecuzione della pianificazione.
 :  : FLD T$M512.T$M511
 :  : FLD T$M514 __Log pianificazione__
Se impostato, all'atto della pianificazione di ogni codice, viene registrato un elemento nell'archivio di log, con chiave 'MRP', articolo/magazzino e data e ora della registrazione.
Questa memorizzazione può essere utile, per determinare quanto è stato movimentato dopo l'esecuzione dell'ultima pianificazione.
Essa viene attivata soltanto se si sta pianificando lo scenario '**'.
 :  : FLD T$M51$ __Aggiustamento M5A__
Programma di aggiustamento dati di pianificazione.
Se impostato, la routine £M5A richiamerà al termine della sua esecuzione il programma M5M5A0_x che potrà modificare i valori restituiti nella DS £M5ADS
 :  : FLD T1M51A __Data scansione__
Normalmente la data di scansione della distinta base, per la determinazione degli impegni pianificati è : 
per gli ordini di produzione la data di suggerimento
per gli ordini di lavorazione la data di fine pianficata
Con questa impostazione è possibile modificare questo comportamento.
Se si imposta 1, la data di scansione viene forzata alla data di lancio dell'MRP, se inferiore ad essa.
Se si imposta 2, ed è presente il programma di exit M5M5W0_U (di cui si fornisce un prototipo), è possibile in esso impostare una data di scansione in modo personale. Questo programma riceve l'intero consiglio, in modo da permettere comportamenti specifici.
NB :  l'opzione 2 NON comprende l'opzione 1. Se lo si desidera, bisogna implementarla nell'exit, che riceve anche la data di lancio della pianificazione.
!!! ATTENZIONE !!! se nell'ordine pianificato è valorizzato il campo esponente di modifica (in qualsiasi modo esso sia stato ottenuto, per gestione a rottura di EM oppure con una exit), esso viene passato alla scansione distinta, e viene assunta la sua data di inizio validità come data di scansione, indipendentemente da ogni altra impostazione.
 :  : FLD T1M51B __No imp.p.rio__
Se si imposta questo campo, non verranno generati impegni pianificati per articoli gestiti a punto di riordino.
Questi impegni non verrebbero comunque utilizzati dalla pianificazione, in quanto l'unica fonte negativa è il punto di riordino stesso, indipendentemente da quanto impostato nel gruppo fonti.
NOTA TECNICA
In realtà gli impegni pianificati vengono scritti, e successivamente, quando viene pianificato l'articolo a cui appartengono, li si cancella. Il motivo di questo comportamento è la velocità :  non si determina, per ogni impegno pianificato che si sta scrivendo, se è a punto di riordino, ma lo si fa quando si sta pianificando il suo articolo (cosa che si farebbe indipendentemente dalla scelta di cancellazione).
 :  : FLD T1M51C
Suffisso del programma di aggiustamento chiamato dal servizio M5SER_11 per personalizzare la
matrice di navigazione dell'MRP (es :  M5SER_X1A se T1M51C=A);
 :  : FLD T1M51D
Se impostato non è permesso il rilascio dallo scenario base (**).
Ricordo che il flag di scenario di rilascio di tabella M5B, NON vale per lo scenario base, che quindi è normalmette rilasciabile.
La presente impostazione è significativa in una modalità di pianificazione "disaccoppiata" :  la pianificazione opera sulle scenario ** e, quando ha raggiunto un risultato accettabile, copia i dati su un altro scenario, definito di rilascio.
Con la presente impostazione lo scenario base risulta "protetto" da rilasci imprevisti.
 :  : FLD T1M51E
Se impostato, e se è attiva l'applicazione automatica dei suggerimenti, viene controllato il verificarsi di un selfie tardivo, segnalato nelle statistiche di una sessione di MRP.
NB :  viene segnalata la presenza di uno o più selfie tardivi, non i singoli casi.
Questo caso si verifica quando il selfie modifica un ordine di produzione o di conto lavoro che ha un impegno già trattato.
Deve essere presente una distinta documento, e l'articolo dell'impegno trascurato deve avere un LLC minore di quello dell'assieme, oppure uguale ma con codice più basso.
In entrambi i casi l'articolo dell'impegno è già stato trattato e quindi la sua modifica,
contesuale alla modifica dell'ordine dovuta al selfie, avviene in modo tardivo, risultando in tal modo ininfluente.
Naturalmente verrà considerata al successivo MRP.

