# INTRODUZIONE
Scopo della /copy g40 è la gestione di Liste di oggetti (oggetti 'LI') cioè la definizione di sottoinsiemi di elementi.

# FUNZIONI E METODI
Di seguito l'elenco dei metodi disponibili : 
 * DEC Decodifica
 * SCA Scansione Liste
 ** POS_INZ Posizionamento + Reinizializzazione
 ** POS Posizionamento
 ** LET Lettura
 * LISOG Lista Codici Elementi
 ** POS Posizionamento
 ** LET Lettura
 * LISOD Lista Codici+Descrizione Elementi
 ** POS Posizionamento
 ** LET Lettura
 * LISRE Lista Codici+Record
 ** POS Posizionamento
 ** LET Lettura
 * RIP Ripresa Elementi
 ** INZ Inizializzazione
 ** "   " Continua e se fine ricomincia
 * SCN Scansione elementi lista
 ** POS Posizionamento nella lista
 ** LET Lettura elementi
 * CTR Controllo
 ** INZ Inizializza
 ** OGG Oggetto passato
 * GES Gestione
 ** INT Interrogazione
 ** MOD Modifica
 ** WRI Scrittura
 ** DEL Cancellazione
 ** CLR Svuota
 ** ADD Aggiunta elemento
 ** RMV Rimozione elemento
 ** UPD Aggiornamento cieco
 ** ELI Eliminazione cieca
 * COM Funzione su commmenti
 ** LET Lettura
 ** UPD Aggiornamento
 * SCE Scelta da lista
 * SQL SQL (E)
 ** WHR Ritorno Stringa WHR Completa
 ** WHR_LI Ritorno Stringa WHR Specifica della lista
 ** WHR_CO Ritorno Stringa WHR di Sola Comparazione
 * FON Fonti
 ** DEC Decodifica / Controllo
 ** POS Posizionamento Fonti
 ** SCA Scansione Fonti
 ** OG_POS Posizionamento Codici
 ** OG_SCA Scansione Codici
 ** WHR_LI Ritorno Stringa WHR Specifica della lista
 ** WHR_LI Ritorno Stringa WHR Specifica della lista
 ** WHR_CO Ritorno Stringa WHR di Sola Comparazione
 ** ORD Ordinamento
 ** JOIN Ritorno Stringa di JOIN
 * TST Test di Performance
 ** SCA Scansione delle liste
 ** RIP Ripresa Elementi
 ** LISOG Lista Codici
 ** LISOD Lista Codici+Descrizione
 ** LISRE  Lista Codici+Record
 ** SCN Scansione Elementi

## DEC
Controlla/Decodifica una lista

## SCA
Ritorna l'elenco delle liste di una classe oggetto. La funzione POS_INZ si differenzia rispetto alla POS in quanto reinizializza le eventuali cache di memoria create per la determinazione dell'elenco delle liste.

## LISOG
Ritorna l'elenco dei codici della lista, nella DS £40KDS la quale a sua volta è ridefinita dalla schiera £40KK. Dopo la chiamata con funzione LET la suddetta DS va riempita con il parametro £40AE.

Se la scansione è SQL nella variabile £40AE è possibile passare una stringa WHR() che contenga un filtro aggiuntivo.

Il numero di elementi ritornati è indicato nella variabile £G40NE.

Se gli elementi della lista vanno oltre il n° massimo previsto dalla schiera sopracitata viene tornato nel campo messaggio il valore "CONT". Quando non ci sono altri elementi da caricare viene invece tornato il messaggio il valore " ".  Richiamando nuovamente in lettura la /COPY verrà ritornato il messaggio "FINE". Quindi con questa funzione i messaggi ritornati possono essere tre : 
 * CONT  Se ci sono altri elementi da caricare
 * "      "  Dopo quelli ritornati con la chiamata in oggetto non ci sono altri elementi da caricare
 * FINE E' il messaggio che viene tornato dopo una chiamata che ha tornato messaggio " ". In questa chiamata non viene tornato alcun elemento.

Per questa funzione e per tutte le funzioni LIS è inoltre prevista la possibilità di passare i seguenti parametri aggiuntivi nel campo £40AE nella forma attributo(valore) : 
* WHR :  where aggiuntiva fissa
* ORD :  order by aggiuntivo
* FROM :  from da applicare in sostituzione alla FROM determinabile a partire dall'oggetto
* FST :  stringa di filtro per codice/descrizione (si veda £G83 con comparatore SD). A differenza dei precedenti parametri viene applicata anche in caso di lista non sql.
* FSA :  stringa di filtro avanzata (si veda api £K41)

## LISOD
Ritorna l'elenco dei codici della lista e la loro descrizione, nella DS £40DDS la quale a sua volta è ridefinita dalle schiere £40DK e £40DD, che rispettivamente contengono codici e descrizioni. Dopo la chiamata con funzione LET la suddetta DS va riempita con il parametro £40AE.

Se la scansione è SQL nella variabile £40AE è possibile passare una stringa WHR() che contenga un filtro aggiuntivo.

Il numero di elementi ritornati è indicato nella variabile £G40NE.

Per liste con elementi che vanno oltre il numero massimo previsto dalle suddette schiere valgono le stesse regole descritte per la funzione LISOG.

## LISRE
Ritorna un elemento della lista alla volta seguito dall'intero record corrispondente nel file di origine della classe. Il record viene ritornato tramite il parametro £40AE.

Se la scansione è SQL nella variabile £40AE è possibile passare una stringa WHR() che contenga un filtro aggiuntivo.

In lettura viene tornato nel campo messaggio il valore "CONT" sin tanto che non si arriva alla conclusione degli elementi. Solo quando si arriva a tale limite viene tornato il valore "FINE". E' quindi da sottolineare che il valore "CONT" viene ritornato anche per l'ultimo elemento della lista, mentre "FINE" viene tornato solo alla chiamata successiva, la quale non torna alcun elemento valido.

## SCN
Ritorna un elemento della lista alla volta nel primo elemento della schiera £40A o nel parametro £40AE se la lista è estesa.

Sull'utilizzo del campo messaggi valgono le stesse considerazioni descritte per la funzione LISRE.

## RIP
(funzione superata dalla LISOG :  mantenuta per compatibilità in quanto utilizzata in alcuni programmi)
Ritorna nella schiera £40A 300 elementi alla volta della lista. Se la lista contiene altri elementi, viene tornato il messaggio CONT, altrimenti viene ritornato il messaggio è blank. Nel campo £G40NE vengono ritornati il numero di elementi caricato nella schiera.

E' da considerare che una chiamata con metodo blank con chiamata successiva a quella che ha tornato il messaggio vuoto comporta il ricaricamento della lista a partire dal primo elemento. Per questo motivo, per questa funzione a differenza delle altre forme di scansione non viene mai tornato il messaggio con valore "FINE". I messaggi possono essere solo due : 
 * CONT  Se ci sono altri elementi da caricare
 * "      "  Se non ci sono altri elementi da caricare

**INZ**
Forza l'inizio della ripresa della lista a partire dal primo elemento

**"  "**
Nel caso in cui la lista contenga più di 300 elementi con il metodo blank è possibile caricare gli elementi successivi.

## CTR

Dati in input una lista e nel campo £G40CD un codice della classe, permette di conoscere l'appartenenza (indicatore 35 spento) o meno (indicatore 35 acceso) di quell'elemento alla lista.

La funzione INZ serve solo per reinizializzare l'eventuale cache della composizione della lista.

## GES

Corrispondono alle funzioni di gestione della lista. A seconda della natura della lista (elenco puntuale, filtro per attributi, filtri Q3, carrello, fonte specifica) le modalità di gestione si differenzieranno.

## SCE

Permette di aprire in una finestra l'elenco degli elementi della classe, con la possibilità di potervi applicare una selezione multipla. Gli elementi selezionati vengono ritornati nella schiera £40A.

## SQL

Ritorna nel parametro £40AE la stringa di selezione sql corrispondente alla lista. Vi sono tre metodi per tre differenti tipologie di where.
> * WHR Ritorno della stringa where completa :  è la stringa di where da applicare al file di origine della classe oggetto per ottenere gli elementi della lista. Questa where tiene conto degli eventuali filtri impliciti della classe oggetto (es. per le registrazioni contabili viene automaticamente aggiunto il filtro sull'azienda se questa è stata fissata nella B£2)
 * WHR_LI Ritorno Stringa WHR Specifica della lista :  funziona come la precedente con la differenza che con questa funzione viene tornata solo la where specifica della lista non tenendo conto degli eventuali filtri impliciti della classe.
 * WHR_CO Ritorno Stringa WHR di Sola Comparazione :  ritorna il filtro da applicare ad un qualsiasi file che faccia riferimento alla classe dell'oggetto della lista, in modo che di tale file vengano presi in considerazione solo gli elementi inclusi nella lista.

A questa funzione nel parametro £40AE è possibile passare come parametri aggiuntivi, nel formato "xxx(valore)" i parametri aggiuntivi : 
* WHR :  stringa SQL di where aggiuntiva
* ORD :  stringa SQL di ordinamento
* FRO :  archivio da leggere in sostituzione a quello nativo

## FON

Sono funzioni di servizio dei pgm di fonte delle liste (sono utilizzate solo internamente alla G40).

Le fonti corrispondono all'oggetto Smeup V3L+TipoOggetto, e definiscono particolari forme di definizione di una lista. Il codice è costruito dalla desinenza del programma che gestisce la fonte (che hanno suffisso "B£G40F_") + '.' + funzione/metodo della fonte.

Un programma di fonte deve risolvere obbligatoriamente i metodi di scansione delle fonti stesse (POS/SCA), che  permettono appunto di identificare le fonti e le loro caratteristiche. Ad essa si dovrebbero almeno affiancare  uno o più, dei metodi necessari per la determinazione degli elementi della lista, costituiti da : 
* OG_POS/SCA => la fonte è grado di ritornare i singoli elementi della lista tramite le stesse variabili utilizzate per la funzione LIOSG
* WHR_LI => la fonte è grado di ritornare stringa SQL della WHERE da applicare al file di database nativo dell'oggetto

Le caratteristiche di una fonte (definite dalla DS £40FDS) sono le seguenti : 
* £40FDE     :  descrizione della fonte
* £40FRE     :  tipo tracciato di configurazione della fonte
* £40FLU     :  livello utente, è della classe d'autorizzazione USRLVL che l'utente deve possedere per una lista determinata dalla fonte in oggetto
* £40F_MSO   :  Gestione funzione di scansione per oggetto
* £40F_MWL   :  Gestione Ritorno where di lista
* £40F_MWC   :  Gestione Ritorno where di comparazione
* £40FNT     :  n° oggetti gestiti dalla fonte (n° elementi della schiera £40FTO riempiti)
* £40FTO     :  Schiera con i tipi oggetto gestiti dalla fonte. L'indicazione del solo tipo oggetto implica la considerazione di tutti i parametri collegati. Come codici speciali possono essere indicati :  "*ALL"  per indicare che la fonte è valida per qualsiasi oggetto e *DB per indicare che la fonte è valida per qualsiasi oggetto che corrisponde ad un file di database.

Altre funzioni che la fonte può aggiuntivamente svolgere
* WHR_CO => la fonte è grado di ritornare la condizione utilizzabile in una WHERE di un qualsiasi file corrispondente alla definizione degli elementi della lista (es. se voglio applicare una lista di date in una WHERE sul file dei movimenti di magazzino)

## TST
Permette di verificare funzionamento e performance delle funzioni di scansione delle liste. Ogni suo metodo corrisponde appunto ad una delle funzioni di scansione. Le informazioni calcolate vengono ritornate nella DS £40TDS (la quale va riempita dopo l'esecuzione con il parametro £40AE). Esse sono così strutturate : 

* £40TIN :  registrazione ora inizio
* £40TFI :  registrazione ora fine
* £40TMI :  tempo totale in millesimi di secondi
* £40TNE :  n° di chiamate eseguite

Nel campo £G40NE viene inoltre ritornato il numero totale di elementi della lista caricati dalla scansione.

# I PROGRAMMI DELLA G40

* B£G40G :  programma di servizio generale. Svolge le funzioni più datate della /COPY e ne smista l'esecuzione, sui pgm specifici aggiunti successivamente

* B£G40E :  è il pgm che si occupa di tutte le funzioni concernenti la definizione degli elementi della lista. Risolve le funzioni LISxx e SQL.

* B£G40D :  richiamato dal B£G40G, è solo un deviatore che ha la funzione di richiamare il pgm di interfaccia delle liste con svolgimento delle funzioni di gestione della lista.

* B£G40S :  richiamato dal B£G40G, è solo un deviatore che ha la funzione di richiamare il pgm di interfaccia delle liste con svolgimento delle funzioni di scansione delle liste.

* B£G40I :  richiamato dai pgm B£G40D e B£G40S, è il programma di interfaccia delle liste di una classe oggetto. ad esso affindata la risoluzione delle funzioni di decodifica, scansione e manutenzione delle liste.

* B£G40F :  è il pgm di interfaccia generali delle fonti, richiamato dai pgm B£G40E e I che si occupa di svolgere le chiamate con i pgm di fonte specifici (B£G40F_xx).

* B£G40W :  è versione 1 del pgm B£G40G che si occupa ancora di risolvere le funzioni legate alle liste esplicite e per filtri su attributi.

* B£G40R :  è il pgm che presenta la ricerca delle liste in ambiente 5250.

* B£G40T :  è il pgm di servizio che si occupa di svolgere le funzioni di test.

