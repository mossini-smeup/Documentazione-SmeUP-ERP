# Caricamento dei documenti di ciclo attivo
## Stampa
L'operazione di stampa fattura assegna il numero di fattura al documento.
![ARCHIV](http://localhost:3000/immagini/ODIAED_03/ARCHIV.png)Durante tale operazione è possibile scegliere il formato di stampa.
 T(Le scelte possibili sono : )
- Spool di stampa (vecchio formato stampa su stampante ad aghi)
- Pdf
- Entrambi

E' stata lasciata la possibilità di stampare sul vecchio formato per la stampa delle fatture proforma e nel caso si voglia ristampare una fattura precedentemente stampata su quel supporto.
E' possibile inoltre decidere se procedere all'archiviazione del pdf oppure no.
Entrando nel programma in fase di stampa e ristampa l'archiviazione viene proposta di default.
In caso di prestampa viene generato solo lo spool di stampa e non avviene nessuna archiviazione.
In caso si stia ristampando una fattura già conservata questa non verrà riarchiviata anche se impostato il flag di archiviazione.
### Generazione documento
Viene generato da Smeup il PDF del documento da archiviare e posizionato in una cartella condivisa dell'AS
Il nome del pdf è composto nel modo seguente : 
Codiceazienda_AnnoFattura_CodiceRegistro_NumeroFattura.pdf
### Richiesta di archiviazione del documento generato ( Upload del file )
Tramite la coda di comunciazione con Loocup Server Smeup richiede l'archiviazione del PDF passando le chiavi di archiviazione, opzionalmente richiedendone anche la firma digitale se prevista.
Il documento trasferito viene marcato sul gestionale come "archiviato".
Contestualmente al trasferimento i documenti, se richiesto dalla necessità di avere "fatturazione elettronica" sono firmati digitalmente e su ognuno di essi viene applicato un riferimento temporale che sta ad indicare l'istante di archiviazione.
### Esito dell'upload
L'archiviazione del documenti in EDOK restituisce, se andata a buon fine, l'ID di salvataggio del file all'interno di EDOK. tale ID viene registrato nel documento Smeup.
### ID di salvataggio del documento
 T(Questa informazione indica in modo univoco il documento all'interno di EDOK ed è costituita da due parti : )
- Nome del contenitore di salvataggio (Es :  FA01 Fatture Attive Azienda 01. Oppure per lo storico FS012004 Fatture Storiche Azienda 01 Anno 2004)
- Numerico identificativo del documento nel contenitore

L'archiviazione dello storico è prevista attraverso una procedura che rigenera i PDF dei documenti interessati e ne richiede l'archiviazione tramite Loocup Server

# Consultazione
Grazie all'informazione relativa all'ID di salvataggio del documento in EDOK è possibile "puntarlo" e recuperarlo in qualunque scheda richiedendo a Loocup server (sempre tramite le code dati che questo mette a disposizione) l'estrazione di una copia del documento e il percorso per visualizzarla. percorso fornito sotto forma di XML consono ad essere visualizzato in una sezione HTM di una scheda.
Ad esempio le fatture archiviate e/o conservate sono consultabili tramite loocup attraverso la scheda della fattura.
![doccons](http://localhost:3000/immagini/ODIAED_03/doccons.png)Tale scheda è richiamabile indicando il codice registro, l'anno e il numero della fattura.
E' inoltre possibile accedere alla scheda della fattura dal partitario del cliente e da azioni bolle e fatture, tramite l'azione XV "Visualizzazione scheda fattura".
![lisfatt](http://localhost:3000/immagini/ODIAED_03/lisfatt.png)In maniera analoga a quanto fatto nella scheda della fattura è possibile, da una scheda, accedere alla lista dei contenitori dei documenti presenti in EDOK e all'elenco dei documenti presenti in un contenitore con tutti i suoi campi.
![volcont](http://localhost:3000/immagini/ODIAED_03/volcont.png)
# Conservazione sostitutiva
Per sommi capi ora spieghiamo cos'è la Conservazione Sostitutiva e come viene realizzata da Loocup, lasciando l'approfondimento dell'argomento a documentazione specifica.
La conservazione sostitutiva è una procedura che permette di eliminare la necessità di registrare cartaceamente alcuni dei documenti aziendali. Prendendo ad esempio le fatture del ciclo attivo, tramite la Conservazione sostitutiva, si può ovviare alla stampa cartacea e all'archiviazione in faldoni fisici delle stesse.
La conservazione sostitutiva prevede il salvataggio dei PDF dei tipi di documento interessati a tale procedura su un supporto informatico sottoponendo i pdf relativi ai documenti in oggetto ad una procedura di firma digitale e marcatura temporale.
La firma digitale viene applicata da Loocup, che si avvale del software di firma della EDOK, ai files ed al contenitore dei documenti sottoposto a Conservazione sostitutiva prendendo la chiave di cifratura dalla smartcard rilasciata da enti preposti che deve essere stata inserita nel lettore collegato al PC che esegue l'operazione. Allo stesso modo la Marca Temporale viene applicata dal software di firma, integrato in Loocup, scaricandola in tempo reale dal sito dell'InfoCamere o da ente omologo. Tale marca temporale deve essere applicata non oltre il quindicesimo giorno dall'emissione della prima fattura del contenitore in via di conservazione
Una volta eseguita l'elaborazione il tutto viene portato, in un formato stabilito per legge e realizzato dal software di conservazione, in una cartella precedentemente definita ed a ciò adibita con le necessarie autorizzazioni e backup previsti.
I documenti conservati tramite Loocup verranno quindi spostati in un nuovo contenitore che verrà indicato a Smeup per permettere la modifica della chiave di reperimento del documento. Tale nuovo contenitore avrà un nome "parlante" costituito da : 

- Tipo Documento (2 caratteri, es. :  FA)
- Codice azienda (2 caratteri, es :  01)
- Anno dell'operazione (2 caratteri, es. :  09)
- Settimana dell'operazione (2 caratteri, es. :  25)
- Progressivo indicante il numero di operazioni di conservazione eseguito nella settimana in corso (1 carattere, es. :  3)

quindi i risultato del nome del nuovo contenitore conservato sarà :  FA0109253 e tale rimarra per sempre. I documenti contenuti, così come i corrispettivi documenti gestionali dovranno essere resi totalmente immodificabili tramite il cambio del loro stato in Smeup.
Il contenitore di documenti di cui si era richiesta la conservazione viene svuotato ed è pronto a raccogliere le nuove fatture da archiviare.
La procedura di conservazione, a seconda della quantità di documenti presenti nel contenitore può impiegare diversi minuti (si può arrivare ad una media di due secondi a documento).

Tutti i documenti conservati saranno ancora interrogabili tramite Loocup alla stregua di quelli solo archiviati.

## Prerequisiti
 T(I requisiti necessari per la conservazione sono di due tipi : )
- Requisiti strutturali
-- Installazione e configurazione del Doc-Filing Manager con sorgente dati di nome "Gnutti"
-- Installazione e configurazione del lettore smart card
- Requisiti contingenti
-- Aver inserito la smart card nel lettore collegato al pc
-- Abilitazione del pc al collegamento internet


## L'operatività
Per procedere alla procedura di conservazione occorre portarsi nella scheda di interfaccia per l'archiviazione sostitutiva (scheda ODIAED) : 
![volcont](http://localhost:3000/immagini/ODIAED_03/volcont.png)
La conservazione prevede di selezionare in tale scheda il contenitore che si vuole sottoporre a conservazione (quindi il contenitore FA01) e premere il bottone "Conserva Documenti".
La procedura procede preventivamente ad una fase di controllo dei documenti che si stanno per conservare, bloccando la conservazione in caso di errori.
 T(I controlli implementati sono : )
- Controllo presenza di eventuale buchi di protocollo nelle fatture del contenitore FA01
- Controllo stato fattura nel gestionale (la fattura deve essere contabilizzata per essere conservata).
- Controllo che la fattura non sia già stata conservata in precedenza
- Controllo che i PDF archiviati non siano corrotti


E' presente anche una funzione di controllo, tramite il bottone "Controllo conserva"  che effettua gli stessi controlli descritti in precedenza senza però procedere alla conservazione in caso tutti i controlli diano esito positivo.
Il risultato degli errori vengono evidenziati nella sezione inferiore della scheda. Se non presente nessun errore la sezione risulterà vuota.
E' importante notare che la presenza di errori blocca tutto il processo di conservazione. Anche un solo documento non corretto impedisce la conservazione di tutti quelli presenti nel contenitore.

La fase di conservazione vera e propria viene richiesta al software EDOK che effettua tutta la procedura prevista e restituisce i dati di conferma del successo dell'operazione

Al termine dell'operazione, se è avvenuta con successo, apparirà nella sezione in basso "Conserva documenti" la tabella con i risultati della conservazione.
![volcons7](http://localhost:3000/immagini/ODIAED_03/volcons7.png)
Ricaricando la scheda si noterà la presenza nella lista "Contenitori" del nuovo contenitore creato dalla conservazione, contenente i documenti appena conservati, mentre il contenitore di archiviazione FA01 sarà vuoto.
