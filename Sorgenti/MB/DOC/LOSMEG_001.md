# Updater lato client
Il processo di aggiornamento di Loocup viene gestito dal software __SmeupGO__ tramite l'interfacciamento a un apposito servizio __"Sme.UP Upgrade Service"__ e al dialogo con __Sme.UP provider__.

 - Il ruolo di Sme.UP provider è quello di fornire l'informazione su aggiornamenti e inviare i nuovi file di diverse versioni di Loocup.
 - Il servizio deve essere installato sul computer locale e deve essere eseguito con l'account di sistema locale.
   Il suo ruolo e fare da tramite tra SmeupGO e il provider, eseguendo buona parte delle operazioni di update.

![LOSMEG_001](http://localhost:3000/immagini/LOSMEG_001/LOSMEG_001.png)
## Logica di funzionamento
La procudera di aggiornamento comprede delle fasi distinte : 
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

![LOSMEG_002](http://localhost:3000/immagini/LOSMEG_001/LOSMEG_002.png)L'operazione di download da parte del servizio non necessita la chiusura eventuali istanze di Loocup e continua anche se SmeupGO dovesse essere chiuso.
Il file vengono salvati nella cartella : 
 :  : R03      %temp%\Loocup\<VersionNumber>
![LOSMEG_003](http://localhost:3000/immagini/LOSMEG_001/LOSMEG_003.png)Durante la fase di avvio, SmeupGo verifica sempre la presenza e lo stato di eventuali processi di aggiornamento di un'istanza di Loocup.
### Aggiornamento
Una volta terminato il download, a seconda della modalità di aggiornamento, può essere richiesto all'utente se continuare o fermare l'installazione oppure se eseguire l'upgrade al riavvio di SmeupGO.

![LOSMEG_004](http://localhost:3000/immagini/LOSMEG_001/LOSMEG_004.png)Nel primo caso i file di aggiornamento vengono spostati in una directory temporanea
 :  : R03      %temp%\SmeAgg\<VersionNumber>
Se si sceglie di rimandare l'aggiornamento al riavvio, i file di aggiornamento vengono copiati in
 :  : R03      <cartella di installazione di loocup>\SmeupGo\UPD
All'avvio di SmeupGO tali file vengono poi spostati nella directory temporanea, per poi procedere all'installazione.

In questa fase, nelle schermate di dialogo è possibile vedere le informazioni dell'ultimo upgrade eseguito rispetto a quello in esecuzione in questo momento.

![LOSMEG_007](http://localhost:3000/immagini/LOSMEG_001/LOSMEG_007.png)
Durante l'installazione vera e propria viene eseguito un check di consistenza dei file scaricati e, a seconda di quanto contenuto nei parametri di configurazione, può essere eseguito un backup della cartella di installazione di Loocup.

![LOSMEG_005](http://localhost:3000/immagini/LOSMEG_001/LOSMEG_005.png)Possono esistere però particolari tipi di aggiornamento in cui viene eseguito comunque un backup di sicurezza.
Se in configurazione è stato però previsto che non vengano mantenuti backup in archivio, il file verrà eliminato all'avvio dello SmeupGO.


## Configurazione degli aggiornamenti
I parametri relativi alle operazioni di aggiornamento sono modificabili attraverso la "Gestione configurazione" di SmeupGO e sono contenuti nei file : 

- **SmeAgg.xml**  :  in questo file è presente la configurazione vera e propria : 
-- __Url Server update__ :  indirizzo URL del provider SmeUP provider di riferimento per gli upgrade
   Questa configurazione può essere passato anche da riga di comando come parametro all'avvio di SmeupGO **--UPD**. Esempio: SmeupGO.exe --UPD:http://myprovider.mydomain.com
-- __Versione__ :  questa opzione determina la richiesta di una versione specifica di Loocup a prescindere da quanto specificato nel file version.info. Maggiori informazioni si trovano nella sezione "Aggiornamenti speciali"
-- __Numero massimo backup__ :  determina quanti backup devono essere mantenuti in archivio. Se è specificato il valore 0, non verrà eseguito alcun backup durante aggiornamenti di update.
- **smeupgo<VersionNumber>.info**  :  (es :  smeupgoV4R1M150315.xml)
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
_7_Attenzione! Il file SmeAgg presente in %appdata%/SmeupGo è comune a tutti i Loocup presenti sul pc in uso!
Per differenziare il comportamento di una specifica installazione di Loocup, il file di configurazione deve essere copiato in locale nella sua directory di installazione. I file in locale hanno la precedenza su quelli nella cartella di default di configurazione (%appdata%\loocup). La "gestione configurazione" di SmeupGO permette la modifica del file effettivamente utilizzato.
### Forzare un download completo
Nelle funzioni avanzate dell'interfaccia di SmeupGO è possibile forzare il download completo di tutti i file di Loocup in uso e non solo i file relativi all'ultimo aggiornamento disponibile.
Questa opzione può essere utile se si pensa di avere un'installazione non pulita del software :  alla fine del processo la cartella su PC risulterà uguale a quella utilizzata dal provider come sorgente dei file di aggiornamento.
_7_Attenzione! Andranno persi tutti i file "personalizzati" presenti nella cartella di installazione e non in %appdata%\loocup!
### Modalità silente
E' possibile eseguire un aggiornamento silenziando ogni richiesta o messaggio di errore ed evitando che lo SmeupGO si riavvii una volta eseguito l'aggiornamento.
Per avere questo tipo di operatività lo SmeupGo deve essere eseguito specificando il parametro **--OUPD** con l'indirizzo URL del provider SmeUP provider di riferimento per gli upgrade.
Esempio: SmeupGO.exe --OUPD:http://myprovider.mydomain.com
_7_Attenzione! Essendo silenziati i messaggi di errore, devono essere analizzati i log per verificare se l'operazione ha avuto successo!


## Note
* Le operazioni di aggiornamento coinvolgono di software; nella barra di stato di SmeupGO viene indicata la versione di ognuna di essi. Questa è un'informazione importante nel caso debbano essere fatte delle segnalazioni.
![LOSMEG_006](http://localhost:3000/immagini/LOSMEG_001/LOSMEG_006.png)* Il processo di upgrade, aggiorna una sola installazione di Loocup. Se sono installate più istanze di Loocup verrà eseguito l'upgrade all'avvio del relativo SmeupGO.
** Caso limite :  se vengono eseguiti contemporaneamente più SmeupGO, ognuno considererà il processo di upgrade come se fosse relativo a se stesso. L'aggiornamento effettivo riguarderà lo SmeupGO a cui verrà confermato per primo l'esecuzione dell'installazione dell'upgrade e che ha la stessa versione del pacchetto scaricato.















