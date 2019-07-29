
# Updater lato client
Il processo di aggiornamento di Loocup viene gestito dal software __SmeupGO__ tramite l'interfacciamento a un apposito servizio __"Sme.UP Upgrade Service"__ e al dialogo con __Sme.UP provider__.

 - Il ruolo di Sme.UP provider è quello di fornire l'informazione su aggiornamenti e inviare i nuovi file di diverse versioni di Loocup.
 - Il servizio deve essere installato sul computer locale e deve essere eseguito con l'account di sistema locale.
   Il suo ruolo e fare da tramite tra SmeupGO e il provider, eseguendo buona parte delle operazioni di update.

![LOSMEG_001](http://localhost:3000/immagini/LOSMEG_03/LOSMEG_001.png)
# Scenari tipici
Sme.UP pubblica gli aggiornamenti delle varie versioni di Loocup tramite un provider accessibile all'indirizzo  __http://update.smeup.com.__

La configurazione tipica per un'azienda consiste nell'avere uno Sme.UP Provider interno all'azienda con i PC opportunamente configurati come client.
![LOSMEG_016](http://localhost:3000/immagini/LOSMEG_03/LOSMEG_016.png)L'aggiornamento di tale provider con i rilasci ufficiali, può essere eseguito manualmente o tramite uno script schedulato che esegua SmeupGO con il parametro --OUP :  (per maggiori dettagli fare riferimento alla sezione "Aggiornamenti speciali").

Nel caso serva un'organizzazione più complessa (as esempio con multisede), può essere utilizzata una struttura in cui vi sia uno Sme.UP Provider "Master",  che faccia da riferimento per uno o più Sme.UP Provider "Slave".
![LOSMEG_017](http://localhost:3000/immagini/LOSMEG_03/LOSMEG_017.png)In questa configurazione si riduce il carico che avrebbe un unico provider, eventualmente sfruttando una rete locale riducendo i requisiti di banda verso l'esterno.
Anche in questo caso, gli aggiornamenti dei provider Slave possono essere schedulati o essere eseguiti manualmente.

# Logica di funzionamento
La procedura di aggiornamento comprede delle fasi distinte : 
* verifica
* download
* installazione
### Verifica
Nella cartella di installazione di Loocup sono presenti due file che contengono le informazioni necessarie a capire lo stato dell'installazione : 
* **version.info**  :  che identifica la versione <VersionNumber> in uso di Loocup (es :  V4R1M150315)
* **update.info**  :  che identifica l'ultimo update eseguito
I dati di versione vengono inviati al provider per avere in risposta il file update.info relativo al pacchetto di upgrade di uno specifico Loocup installato.

Le informazioni di tale file vengono confrontati con quelli presenti nel file di installazione per capire se è disponibile un nuovo aggiornamento per la versione in uso.
### Download
Il nuovo pacchetto di aggiornamento viene richiesto al provider tramite il servizio di upgrade.
Se il pacchetto non è stato mai generato dal provider il sistema potrebbe rimanere per un certo tempo in attesa di una risposta dal provider, prima di eseguire il download.

![LOSMEG_002](http://localhost:3000/immagini/LOSMEG_03/LOSMEG_002.png)L'operazione di download da parte del servizio non necessita la chiusura eventuali istanze di Loocup e continua anche se SmeupGO dovesse essere chiuso.
Il file vengono salvati nella cartella : 
 :  : R03      %temp%\Loocup\<VersionNumber>
![LOSMEG_003](http://localhost:3000/immagini/LOSMEG_03/LOSMEG_003.png)Durante la fase di avvio, SmeupGo verifica sempre la presenza e lo stato di eventuali processi di aggiornamento di un'istanza di Loocup.
### Aggiornamento
Una volta terminato il download, a seconda della modalità di aggiornamento, può essere richiesto all'utente se continuare o fermare l'installazione oppure se eseguire l'upgrade al riavvio di SmeupGO.

![LOSMEG_004](http://localhost:3000/immagini/LOSMEG_03/LOSMEG_004.png)Nel primo caso i file di aggiornamento vengono spostati in una directory temporanea
 :  : R03      %temp%\SmeAgg\<VersionNumber>
Se si sceglie di rimandare l'aggiornamento al riavvio, i file di aggiornamento vengono copiati in
 :  : R03      <cartella di installazione di loocup>\SmeupGo\UPD
All'avvio di SmeupGO tali file vengono poi spostati nella directory temporanea, per poi procedere all'installazione.

In questa fase, nelle schermate di dialogo è possibile vedere le informazioni dell'ultimo upgrade eseguito rispetto a quello in esecuzione in questo momento.

![LOSMEG_007](http://localhost:3000/immagini/LOSMEG_03/LOSMEG_007.png)
Durante l'installazione vera e propria viene eseguito un check di consistenza dei file scaricati e, a seconda di quanto contenuto nei parametri di configurazione, può essere eseguito un backup della cartella di installazione di Loocup.

![LOSMEG_005](http://localhost:3000/immagini/LOSMEG_03/LOSMEG_005.png)Possono esistere però particolari tipi di aggiornamento in cui viene eseguito comunque un backup di sicurezza.
Se in configurazione è stato però previsto che non vengano mantenuti backup in archivio, il file verrà eliminato all'avvio dello SmeupGO.


## Configurazione degli aggiornamenti
I parametri relativi alle operazioni di aggiornamento sono modificabili attraverso la "Gestione configurazione" di SmeupGO e sono contenuti nei file : 

- **SmeAgg.xml**  :  in questo file è presente la configurazione vera e propria : 
-- __Url Server update__ :  indirizzo URL del provider SmeUP provider di riferimento per gli upgrade
   Questa configurazione può essere passato anche da riga di comando come parametro all'avvio di SmeupGO **--UPD**. Esempio: SmeupGO.exe --UPD:http://myprovider.mydomain.com
-- __Versione__ :  questa opzione determina la richiesta di una versione specifica di Loocup a prescindere da quanto specificato nel file version.info. Maggiori informazioni si trovano nella sezione "Aggiornamenti speciali"
-- __Numero massimo backup__ :  determina quanti backup devono essere mantenuti in archivio. Se è specificato il valore 0, non verrà eseguito alcun backup durante aggiornamenti di update.
- **smeupgo<VersionNumber>.xml**  :  (es :  smeupgoV4R1M150315.xml)
-- __Modalità di aggiornamento__ :  determina come e quando devono essere eseguiti gli aggiornamenti. I possibili valori sono indicati in tabella.



|  Nam="Mod_agg" |
| 
| .COL Txt="**Valore**" Lun="0" A="L" |
| ---|----|
| 
| .COL Txt="**Descrizione** " Lun="0" A="L" LunAut="1" |
| NO-UPGRADE|Il sistema non esegue alcun tipo di aggiornamento |
| MANUAL|Gli aggiornamenti sono attivi, ma il programma non effettua nessuna verifica di congruenza con il sito, per cui effettuare l'aggiornamento è a completa discrezione dell'utente |
| MANUAL-WITH-CHECK|Gli aggiornamenti sono attivi, ad ogni accesso di SmeupGo viene verificato se sul sito ci sono nuovi aggiornamenti. La segnalazione all'utente avviene tramite abilitazione/disabilitazione del pulsante "Aggiornamenti disponibili". |
| AUTOMATIC-WITH-CONFIRMATION|Gli aggiornamenti sono attivi, ad ogni accesso di SmeupGo viene verificato se sul sito ci sono nuovi aggiornamenti ed, in caso affermativo, viene chiesto all'utente se scaricare gli aggiornamenti e in seguito se eseguirne l'installazione. |
| AUTOMATIC|Gli aggiornamenti sono attivi, ad ogni accesso di SmeupGo viene verificato se sul sito ci sono nuovi aggiornamenti ed, in caso affermativo, questi vengono scaricati e installati al successivo avvio di SmeupGO. |
| 



## Aggiornamenti speciali
### Richiesta di una versione specifica
Nel file di configurazione SmeAgg.xml è possibile definire una versione specifica di upgrade che può essere diversa da quella presente nel file version.info. Può essere utile specificarla se devono essere eseguiti dei test che necessitano la richiesta al provider di una versione particolare di Loocup.
Quando si specifica una versione differente da quella installata è necessario forzare il download completo. Se non si compie questa operazione e sul provider il file update.info specifica un update, verrà scaricato l'update della versione indicata e si mescoleranno le installazioni. Avremo una versione con l'upgrade di un'altra, con una condizione di potenziale instabilità.
Se sul provider il file update.info conterrà nella seconda riga RELEASE, non sarà necessario forzare il download completo :  al primo riavvio del GO, la nuova versione verrà scaricata in toto.
**Se nell'update folder dello SmeUP Provider è presente il file force_version.info verrà data la precedenza alla versione indicata in questo file in quanto si tratta di un cambio di versione!
_7_Attenzione! Il file SmeAgg presente in %appdata%/SmeupGo è comune a tutti i Loocup presenti sul pc in uso!
Per differenziare il comportamento di una specifica installazione di Loocup, il file di configurazione deve essere copiato in locale nella sua directory di installazione. I file in locale hanno la precedenza su quelli nella cartella di default di configurazione (%appdata%\loocup).
La "gestione configurazione" di SmeupGO permette la modifica del file effettivamente utilizzato, ma non tutti gli utenti potrebbero avere i diritti di scrittura nella cartella locale di installazione di loocup.
### Forzare un download completo
Nelle funzioni avanzate dell'interfaccia di SmeupGO è possibile forzare il download completo di tutti i file di Loocup in uso e non solo i file relativi all'ultimo aggiornamento disponibile.
Questa opzione può essere utile se si pensa di avere un'installazione non pulita del software :  alla fine del processo la cartella su PC risulterà uguale a quella utilizzata dal provider come sorgente dei file di aggiornamento.
Il download completo è utile anche nel caso in cui si sia indicato nello SmeAgg una versione diversa da quella installata. Il download completo, in questo caso, provocherà un cambio di versione.
_7_Attenzione! Andranno persi tutti i file "personalizzati" presenti nella cartella di installazione e non in %appdata%\loocup!
### Modalità silente
E' possibile eseguire un aggiornamento silenziando ogni richiesta o messaggio di errore ed evitando che lo SmeupGO si riavvii una volta eseguito l'aggiornamento.
Per avere questo tipo di operatività lo SmeupGo deve essere eseguito specificando il parametro **--OUPD** con l'indirizzo URL del provider SmeUP provider di riferimento per gli upgrade.
Esempio: SmeupGO.exe --OUPD:http://myprovider.mydomain.com
_7_Attenzione! Essendo silenziati i messaggi di errore, devono essere analizzati i log per verificare se l'operazione ha avuto successo!


## Il cambio di versione
Il cambio di versione richiede solitamente che la nuova release venga testata da alcuni utenti chiave, prima di essere distribuita a tutti.
Vediamo come operare.
La prima operazione da compiere è quella di installare la nuova versione (con il relativo upgrade) nella cartella PROVIDER_UPDATE_FOLDER, sottocartella versione, esempio : 
* PROVIDER_UPDATE_FOLDER = d : \updatefolder
* sottocartella versione = d : \updatefolder\V5R1M161106

### Cambio di versione per uno o più client
Per semplificare il cambio di versione per i client di test, si consiglia, si consiglia di modificare il file update.info (nella cartella di installazione della nuova release), di inserire nella seconda riga **RELEASE**  e di cancellare tutte le righe seguenti.
Modificare poi sui client di test la versione a cui punta il Go (funzioni avanzate, Sistema, Gestione configurazione, Versione) e qui inserire ad esempio V5R1M161106.
Chiudere il Go e riaprirlo :  verrà scaricata e installata la nuova versione. E' possibile che sia necessario fare più di un tentativo nel caso in cui il tempo di creazione del pacchetto di aggiornamento o il tempo di scaricamento sia eccessivo.

Se non si è modificato il file update.info e in questo c'è scritto UPDATE, è obbligatorio forzare un download completo, altrimenti il go, scaricherà l'aggiornamento della nuova release e lo installerà sulla vecchia con potenziali errori

### Cambio di versione per tutti i client
Dopo aver installato la nuova versione sarà sufficiente creare in PROVIDER_UPDATE_FOLDER, un file di testo con nome  **force_version.info**, e scrivere nella prima riga il codice della nuova release (es. V5R1M161106).

Tutti i client, quando effettureanno un aggiornamento verranno forzati ad usare questa versione.



## Note
* Le operazioni di aggiornamento coinvolgono vari programmi (SmeupGo, SmeAgg, Unzip e servizio di aggiornamento); nella barra di stato di SmeupGO viene indicata la versione di ognuna di essi. Questa è un'informazione importante nel caso debbano essere fatte delle segnalazioni.
![LOSMEG_006](http://localhost:3000/immagini/LOSMEG_03/LOSMEG_006.png)* Il processo di upgrade, aggiorna una sola installazione di Loocup. Se sono installate più istanze di Loocup verrà eseguito l'upgrade all'avvio del relativo SmeupGO.
** Caso limite :  se vengono eseguiti contemporaneamente più SmeupGO, ognuno considererà il processo di upgrade come se fosse relativo a se stesso. L'aggiornamento effettivo riguarderà lo SmeupGO a cui verrà confermato per primo l'esecuzione dell'installazione dell'upgrade e che ha la stessa versione del pacchetto scaricato.















