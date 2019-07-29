#  Prerequisiti funzionamento Smeup Provider e troubleshooting
Scopo di questo documento è di riassumere le impostazioni a cui prestare attenzione in fase di configurazione e di fornire spunti per la risoluzione dei problemi più comuni.


 * Per tutto il periodo di funzionamento l'IBMi deve essere acceso e raggiungibile dal provider e i sottosistemi necessari al funzionamento devono essere attivi (sono gli stessi di LoocUp).
 * Non devono esserci salvataggi in corso.
 * Le porte di comunicazione verso l'IBMi devono essere aperte (sono le stesse di LoocUp).
 * Il provider deve collegarsi all'IBMi con un utente dedicato.
 * L'utente di collegamento all'IBMi DEVE avere il file di configurazione SCP_CLO correttamente configurato (copiarlo da SMEUPR_ES).
 * Porre attenzione alla variabile PROVIDER_PATHS :  contiene i percorsi delle cartelle a cui il provider può accedere.
 ** Si consiglia di usare solamente percorsi espliciti. Le variabili vengono risolte nell'ambiente dell'utente WebUp connesso e questo complica l'individuazione di eventuali problemi.
 ** Per testare la raggiungibilità dei path definiti in PROVIDER_PATHS, con la Roma V1, si può utilizzare la pagina di debug.
 ** PROVIDER_PATHS. Serve per : 
 *** autorizzare il provider al reperimento delle risorse remote.
 *** autorizzare il provider al reperimento delle immagini a WebUp.
 *** autorizzare il provider al reperimento degli upgrade.
 * Se il provider è installato come servizio, DEVE utilizzare un utente di dominio dedicato. Utenti locali NON vanno usati.
 * Rispetto a Loocup, SmeupProvider, utilizza SEMPRE una porta server e opzionalmente una porta http. Devono essere univoche. Di default sono la 9990 e la 9090.
 * Se sullo stesso server sono installati due o più provider, le porte server e http devono essere univoche. Es Provider1 9991 e 9091, Provider2 9992 e 9092.
 * Il provider va spento prima che si spenga l'IBMi e riavviato solo quando l'IBMi è pronto (vedi prerequisiti da 1 a 3).
 * Valutare spegnimenti e riavvii in funzione del carico di lavoro :  si consiglia un riavvio a settimana (se l'IBMi ha spegnimenti più frequenti rispettare la cadenza di questi ultimi).
 * Se l'IBMi non si spegne mai o il carico di lavoro è molto elevato, schedulare riavvii con maggiore frequenza (max uno al giorno).
 * Se il provider, installato come servizio, non riesce a raggiungere cartelle di rete, disabilitare il servizio e schedulare avvii e spegnimenti con i file **start_server.cmd** e **stop_server.cmd** (cartella LOOCUP_SCP).
 * Prima di avviare il provider come servizio, utilizzare il file ServiceTest.bat. E' nella cartella di installazione e utilizza (come default) la configurazione serviceNT\conf\wrapper.conf.

## la pagina di debug
Con la versione Roma Revisione 1, è stata migliorata la pagina di debug.
Sono state separate le informazioni disponibili nel provider da quelle che richiednono una connessione al server applicativo iSeries.
E' possibile ricaricare la connessione di default (serve la password dell'utente iSeries del provider)
E' possibile testare la raggiungibilità dei percorsi
Migliorata la pagina di debug :  è possibile ricaricare la sessione master, migliorata la fruibilità
della pagina richiamando i servizi sul server applicativo e il test della coda server tramite
apposito pulsante, introdotto il test dei path definiti nella variabile PROVIDER_PATHS

## Risorse remote - Immagini in WebUp
L'utilizzo delle risorse remote e delle immagini in WebUp prevedono
Lato SmeupProvider
 * PROVIDER_PATHS con inseriti i path delle risorse che si vogliono condividere con gli utenti
 * I path devono essere raggiungibili dal server su cui si trova SmeupProvider
 * L'utente di Windows che utilizza lo SmeupProvider deve poter accedere in lettura e scrittura ai path indicati. Utilizzare le autorizzazioni di Windows se si vuole togliere il permesso di scrittura.
Lato SmeUp
 * Attenzione agli oggetti nella K09 :  **devono essere di tipo J8 e J9**, altrimenti il client (Loocup) li considererà locali o raggiungibili tramite la rete windows e non sarà in grado di gestirli.

NOTA :  con sistemi operativi Windows server 2008 abbiamo riscontrato limiti nel funzionamento del provider come servizio :  in questo tipo di installazione non riesce ad accedere a file in rete o a mappare unità di rete tramite il servizio interno JA_00_15 NET.AUT .

