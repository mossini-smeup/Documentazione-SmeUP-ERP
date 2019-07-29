# Caricamento dei documenti di ciclo attivo
## Generazione pdf
Per procedere all'archiviazione del documento è necessario generare il pdf relativo.
Il file pdf viene generato in una cartella condivisa (per esempio sull'ifs dell'as400) il cui percorso è specificato in un elemento della B§P richiamato nella tabella ODC che specifica il tipo documento del documentale da archiviare.
### Fatture di ciclo attivo
Per l'archiviazione delle fatture di ciclo attivo è stato stabilito che il nome sia composto nel modo seguente : 
Codiceazienda_AnnoFattura_CodiceRegistro_NumeroFattura.pdf
Il nome è così composto perchè da esso sono derivate le chiavi di archiviazione della tabella del documentale per tale documento. In caso si voglia archiviare un tipo documento diverso bisogna concordare le chiavi della tabella
di archiviazione per tale documento e costruire la struttura del nome.
### Richiesta di archiviazione del documento generato ( Upload del file )
Tramite la coda di comunciazione con Loocup Server, Smeup richiede l'archiviazione del PDF passando le chiavi di archiviazione. Il documento trasferito viene marcato sul gestionale come "archiviato".
Contestualmente al trasferimento i documenti, se richiesto dalla necessità di avere "fatturazione elettronica"  (tabella ODC), sono firmati digitalmente e su ognuno di essi viene applicato un riferimento temporale che sta ad indicare l'istante di archiviazione.
L'archiviazione viene effettuata tramite una chiamata al programma funizzat. Il programma gestisce in ingresso sia l'oggetto DO (documento V5) che l'oggetto FT (fattura contabilizzata). E' quindi richiamabile sia nella stampa fattura (come oggetto DO) che in un flusso post contabilizzazione (oggetto FT). Per i dettagli del richiamo della funzione si rimanda al capitolo "Installazione e Configurazione su Smeup".
### Esito dell'upload
L'archiviazione del documenti in COMPED restituisce, se andata a buon fine, l'ID di salvataggio del file all'interno di COMPED. Tale ID viene registrato nel documento Smeup (parametri £D1). E' Possibile attivare una stampa di log per controllare l'esito di ogni archiviazione.
### ID di salvataggio del documento
 T(Questa informazione indica in modo univoco il documento all'interno di COMPED ed è costituita da due parti : )
- Nome del volume di salvataggio (Es :  FA01 Fatture Attive Azienda 01).
- Numerico progressivo univoco del documento nel volume

# Consultazione
Grazie all'informazione relativa all'ID di salvataggio del documento in COMPED è possibile recuperare il documento stesso in qualunque scheda di Loocup richiedendo a Loocup server (sempre tramite le code dati che questo mette a disposizione) l'estrazione di una copia del documento e il percorso per visualizzarla.
Ad esempio le fatture archiviate e/o conservate sono consultabili tramite loocup attraverso la scheda della fattura.
![DOCCONS](http://localhost:3000/immagini/ODIACO_04/DOCCONS.png)Tale scheda è richiamabile indicando il codice registro, l'anno e il numero della fattura.
E' inoltre possibile accedere alla scheda della fattura dal partitario del cliente e da azioni bolle e fatture, tramite azioni apposite. Per l'impostazione delle azioni si rimanda al capitolo "Installazione e Configurazione su Smeup".
![LISFATT](http://localhost:3000/immagini/ODIACO_04/LISFATT.png)In maniera analoga a quanto fatto nella scheda della fattura è possibile, da una scheda, accedere alla lista dei volumi presenti in COMPED e all'elenco dei documenti presenti in un volume con tutti i suoi campi.
![VOLCONT](http://localhost:3000/immagini/ODIACO_04/VOLCONT.png)
# Conservazione sostitutiva
Per sommi capi ora spieghiamo cos'è la Conservazione Sostitutiva e come viene realizzata da Loocup, lasciando l'approfondimento dell'argomento a documentazione specifica.
La conservazione sostitutiva è una procedura che permette di eliminare la necessità di registrare cartaceamente alcuni dei documenti aziendali. Prendendo ad esempio le fatture del ciclo attivo, tramite la Conservazione sostitutiva, si può ovviare alla stampa cartacea e all'archiviazione in faldoni fisici delle stesse.
La conservazione sostitutiva predeve il salvataggio dei PDF dei tipi di documento interessati a tale procedura su un supporto informatico sottoponendo i pdf relativi ai documenti in oggetto ad una procedura di firma digitale e marcatura temporale.
La firma digitale viene applicata da Loocup, che si avvale del software Digital Sign della COMPED, ai files ed al volume sottoposto a Conservazione sostitutiva prendendo la chiave di cifratura dalla smartcard rilasciata da enti preposti che deve essere stata inserita nel lettore collegato al PC che esegue l'operazione. Allo stesso modo la Marca Temporale viene applicata dal software Digital Sign, integrato in Loocup, scaricandola in tempo reale dal sito dell'InfoCamere. Tale marca temporale deve essere applicata non oltre il quindicesimo giorno dall'emissione della prima fattura del volume in via di conservazione
Una volta eseguita l'elaborazione il tutto viene portato, in un formato stabilito per legge e realizzato da Digital Sign, in una cartella precedentemente definita ed a ciò adibita con le necessarie autorizzazioni e backup previsti.
I documenti conservati tramite Loocup verranno quindi spostati in un nuovo volume che verrà indicato a Smeup per permettere la modifica della chiave di reperimento del documento. Tale nuovo volume avrà un nome "parlante" costituito da : 

- Tipo Documento (2 caratteri, es. :  FA)
- Codice azienda (2 caratteri, es :  01)
- Anno dell'operazione (2 caratteri, es. :  09)
- Settimana dell'operazione (2 caratteri, es. :  25)
- Progressivo indicante il numero di operazioni di conservazione eseguito nella settimana in corso (1 carattere, es. :  3)

quindi i risultato del nome del nuovo volume conservato sarà :  FA0109253 e tale rimarrà per sempre. I documenti contenuti, così come i corrispettivi documenti gestionali dovranno essere resi totalmente immodificabili tramite il cambio del loro stato in Smeup.
Il volume di cui si era richeista la conservazione viene svuotato ed è pronto a raccogliere le nuove fatture da archiviare.
La procedura di conservazione, a seconda della quantità di documenti presenti nel volume può impiegare diversi minuti (si può arrivare ad una media di due secondi a documento).

Tutti i documenti conservati saranno ancora interrogabili tramite Loocup alla stregua di quelli solo archiviati.

## Prerequisiti
 T(I requisiti necessari per la conservazione sono di due tipi : )
- Requisiti strutturali
-- Installazione e configurazione del Doc-Filing Manager con definizione nome sorgente dati
-- Installazione e configurazione del lettore smart card
- Requisiti contingenti
-- Aver inserito la smart card nel lettore collegato al pc
-- Abilitazione del pc al collegamento internet


## L'operatività
Per procedere alla procedura di conservazione occorre portarsi nella scheda di interfaccia per l'archiviazione sostitutiva (scheda ODIACO) : 
![volcont](http://localhost:3000/immagini/ODIACO_04/volcont.png)
La conservazione prevede di selezionare in tale scheda il volume che si vuole sottoporre a conservazione (quindi il volume FA01) e premere il bottone "Conserva Volume".
La procedura procede preventivamente ad una fase di controllo dei documenti che si stanno per conservare, bloccando la conservazione in caso di errori.
 T(I controlli implementati sono : )
- Controllo presenza di eventuale buchi di protocollo nelle fatture del volume FA01
- Controllo stato fattura nel gestionale (la fattura deve essere contabilizzata per essere conservata).
- Controllo che la fattura non sia già stata conservata in precedenza
- Controllo protocollo ultimo documento conservato e protocollo primo documento in conservazione per evitare presenza di buchi di protocollo tra una conservazione e l'altra.


E' presente anche una funzione di controllo, tramite il bottone "Controllo conserva"  che effettua gli stessi controllo descritti in precedenza senza però procedere alla conservazione in caso tutti i controlli diano esito positivo.
Il risultato degli errori vengono evidenziati nella sezione inferiore della scheda. Se non presente nessun errore la sezione risulterà vuota.
E' importante notare che la presenza di errori blocca tutto il processo di conservazione. Anche un solo documento non corretto impedisce la conservazione di tutti quelli presenti nel volume.

Una volta che il volume è stato predisposto alla firma appare la finestra di interfaccia alla smart card. E' necessario cliccare il bottone "Aggiungi firma" che aggiunge la firma al volume oggetto della conservazione.

L'accesso alla smart card prevede l'inserimento del PIN della smart card stessa e successivo click su ok.
![volcons1](http://localhost:3000/immagini/ODIACO_04/volcons1.png)![volcons2](http://localhost:3000/immagini/ODIACO_04/volcons2.png)
La finestra seguente è quella che imprime il riferimento temporale alla chiusura del volume.
Occorre prestare attenzione al fatto che sia selezionata la voce "Imposta attributo signing Time" riportante l'istante dell'operazione in corso. In seguito cliccare sul bottone "Firma".
![volcons3](http://localhost:3000/immagini/ODIACO_04/volcons3.png)
Dopo pochi istanti si torna alla finestra di firma del file di chiusura e a questo punto va applicata la marca temporale, cliccando sul bottone "Marca temporale".
![volcons4](http://localhost:3000/immagini/ODIACO_04/volcons4.png)
La finestra seguente è quella che applica la marca temporale e che richiede il collegamento ad internet da parte del pc su cui si opera. Cliccare su "Applica timestamp"
![volcons5](http://localhost:3000/immagini/ODIACO_04/volcons5.png)
Terminata la procedura di download della marca temporale si torna alla finestra originaria e resta solo da cliccare su "Salva".
![volcons6](http://localhost:3000/immagini/ODIACO_04/volcons6.png)
Al termine dell'operazione, se è avvenuta con successo, apparirà nella sezione in basso "Conserva volume" la tabella con i risultati della conservazione.
![volcons7](http://localhost:3000/immagini/ODIACO_04/volcons7.png)
Ricaricando la scheda si noterà la presenza nella lista "Volumi" del nuovo volume creato dalla conservazione, contenente i documenti appena conservati, mentre il volume di archiviazione FA01 sarà vuoto.
