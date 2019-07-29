Questi sono i passi necessari al corretto funzionamento di SmePD : 

- Si installa il servente SmePD su un pc Windows che sia visibile da AS/400. L'installazione tipica potrebbe essere su server di rete e tipicamente avviene nel percorso c : \lpd-0.6.5 cui faremo riferimento con il termine di **cartella di installazione**. Tutte le stampanti locali o di rete che sono visibili da questo PC possono essere usate dal server SmePD come destinazione delle stampe PDF. Quindi un'unica installazione del servente SmePD può servire per il controllo di n stampanti.
- Si definiscono su AS/400 n code di stampa virtuali, una per ognuna delle stampanti su cui si richiede l'emissione di documenti PDF. Una coda di stampa virtuale è la definizione di un device che non fa riferimento ad una stampante fisica ma ad un server capace di gestire le stampe attraverso un protocollo di comunicazione SmePD.


# Reperimento del server SmePD
Il server SmePD è distribuito con gli aggiornamenti di Sme.UP.
E' possibile reperirilo tramite l'utility UP UT3. La cartella in cui estrarre tale componente è ininfluente (a differenza di SmeNS e SmeDG) in quanto poi l'installazione avverà successivamente su un server diverso.

# Installazione del server SmePD
L'installazione del server SmePD può essere fatta su un PC con sistema operativo Windows che sia accessibile da AS/400 attraverso la rete. SmePD è un server SmePD e quindi è bene installarlo su una macchina che sia sempre attiva e che non abbia altri servizi SmePD attivi (il servizio SmePD viene avviato sempre sulla porta 515, non è quindi possibile avere più servizi SmePD sulla stessa macchina).
La **prima installazione** del server SmePD prevede i seguenti punti : 

- Arresto del processo acrord32.exe da task manager
- Estrazione dell'archivio compresso SmePD nella cartella di destinazione sul disco locale del server SmePD scelto (es. c : \lpd-0.6.5).
- Installazione di Acrobat Reader e/o GhostScript. Ove possibile è preferibile installare la versione consigliata dal programma e disinstallare altre eventuali versioni, disabilitando gli aggiornamenti automatici. Verificare il corretto percorso di installazione di gsprint o di Acrobat Reader. Es :  nel file lpd_config.xml gsprint è impostato a c : \"program files"\ghostgum\gswiew\gsprint.exe ma nei sistemi operativi x64 potrebbe essere c : \"program files (x86)"\ghostgum\gswiew\gsprint.exe.
- Configurazione delle code di stampa nel file _2_lpd_config.xml contenuto nella cartella di destinazione scelta "./" (vedi paragrafi successivi).
- Configurazione del servizio nel file _2_wrapper.conf contenuto nella sottocartella "./serviceNT/conf".
- Controllare il corretto funzionamento di tutta la procedura di test visualizzando il file di log _2_lpd.log e _2_serviceNT/logs/wrapper.log.
- Avviare il test interattivo _2_serviceTest.bat per ogni coda di stampa configurata nel file config.xml. Il test deve essere avviato settando nel file di configurazione  _2_config.xml il nodo _2_< show_gui >true< /show_gui > per ogni coda.
- Avviare il servizio SmePD  _2_ServiceInstall.bat.
- Avviare lo script di test _2_testStampaLocale.bat per ogni coda di stampa configurata nel file _2_config.xml. E' consigliabile eseguire il test copiando lo script su un pc diverso da quello su cui è installato il servizio in modo da avere la certezza che non ci siano porte bloccate dal firewall di windows. Sul server e sul pc che eseguono il test deve essere installato il programma di sistema lpr. Per verificare se è installato aprire una cmd, digitare "lpr" e dare invio, se appare la spiegazione della sintassi significa che il servizio è installato. Se non è installato verrà data una risposta del tipo "Comando non riconosciuto". In questo caso fare riferimento alla documentazione del sistema operativo per la procedura d'installazione di LPR. Editare lo script testStampaLocale.bat inserendo il corretto ip del pc/server su cui sono configurate le stampanti, il nome della coda di stampa virtuale che si vuole testare, il percorso e il nome del file pdf da usare come test. La sintassi di LPR è la seguente :  **LPR -S indirizzo-ip-server-lpd -P nome-coda-lpr-da-testare percorso-file-pdf-di-test.pdf
- Controllare il corretto funzionamento di tutta la procedura di test visualizzando il file di log _2_lpd.log e _2_serviceNT/logs/wrapper.log
- Configurazione dei device di stampa virtuali su AS400 (vedi paragrafi successivi)
- Avviare il test di stampa su AS400 digitando da linea di comando _2_t g87 inserendo come funzione _2_CPY2SPLF, come percorso il percorso del documento da stampare (es. _2_SMEDOC/TEST.PDF) e come coda di output il nome scelto come device di stampa virtuale (es. _2_SMEPD)


Per l'**aggiornamento** del server SmePD i passi da seguire sono molto simili, avendo l'accortezza di creare un backup della vecchia installazione e di copiare i vecchi file di configurazione nella nuova installazione. Seguire i seguenti punti : 

- Arresto del processo acrord32.exe da task manager
- Arresto dell'eventuale servizio SmePD attivo sul server (seguire il percorso :  risorse del computer -> gestione -> servizi e applicazioni -> servizi)
- Ridenominazione della cartella con la vecchia installazione con il suffisso "_OLD" (es. c : \lpd-0.6.5_OLD)
- Estrazione del nuovo archivio compresso SmePD nella cartella di destinazione esistente in precedenza sul disco locale del server SmePd scelto (es. c : \lpd-0.6.5).
- Installazione di Acrobat Reader e/o GhostScript. Ove possibile è preferibile installare la versione consigliata dal programma e disinstallare altre eventuali versioni, disabilitando gli aggiornamenti automatici.
- Copia del file _2_lpd_config.xml contenuto nella vecchia installazione "./".
- Copia del file _2_wrapper.conf contenuto nella vecchia installazione, nella sottocartella "./serviceNT/conf"
- Avviare il test interattivo _2_serviceTest.bat per ogni coda di stampa configurata nel file _2_config.xml. Il test deve essere avviato settando nel file di configurazione  _2_config.xml il nodo _2_< show_gui >true< /show_gui > per ogni coda.
- Riattivare il servizio SmePD  (seguire il percorso :  risorse del computer -> gestione -> servizi e applicazioni -> servizi).
- Avviare lo script di test _2_testStampaLocale.bat per ogni coda di stampa configurata nel file _2_config.xml.
- Controllare il corretto funzionamento di tutta la procedura di test visualizzando il file di log _2_lpd.log e _2_serviceNT/logs/wrapper.log
- Configurazione dei device di stampa virtuali su AS400 (vedi paragrafi successivi)
- Avviare il test di stampa su AS400 digitando da linea di comando _2_t g87 inserendo come funzione _2_CPY2SPLF, come percorso il percorso del documento da stampare (es. _2_SMEDOC/TEST.PDF), come coda di output il nome scelto come device di stampa virtuale (es. _2_SMEPD) e il numero di copie (ovvero il numero di file stream che vado a creare sull'IFS il default è 1)



## Definizione delle code di stampa
Questa fase della installazione è necessaria per creare l'associazione tra code di stampa virtuali e stampanti fisiche.
La coda di stampa virtuale è identificata da un nome univoco che è l'unico identificativo con cui la coda viene riconosciuta dai client esterni.

La configurazione delle code di stampe si ottiene agendo sul file di configurazione _2_lpd_config.xml situato sul PC direttamente nella cartella di installazione del server.
All'interno dei file di configurazione vanno definiti : 

- un elemento **acrobat_settings** (e/o **ghost_settings**) che specifica il percorso del programma Acrobat Reader (e/o GhostScript) necessario per il corretto funzionamento del servizio.
- un elemento **spool** per ogni coda di stampa che dovrà essere gestita.

L'elemento **acrobat_settings** (o **ghost_settings**) viene definito come segue : 
>  <acrobat_settings>
      <executable>c : /"Program Files"/Adobe/"Acrobat 7.0"/Reader/AcroRd32.exe</executable>
      <tmp_dir>C : /temp/</tmp_dir>
  </acrobat_settings>
  <ghost_settings>
      <executable>C : /"Program Files"/Ghostgum/gsview/gsprint.exe</executable>
  </ghost_settings>


Alla coda di stampa andrà assegnato un nome nell'attributo _7_name . A questo punto va scelto il motore di stampa dichiarando il print_handler.
Il print_handler può essere di 4 tipi : 

- FILE copia lo stream ricevuto in un file
- PDFPRINTER :  interpreta lo stream ricevuto come un PDF e lo stampa sulla stampante definita tramite il driver interno (utilizzato in fase di test ma sconsigliato a regime)
- PRINTER :  interpreta lo stream ricevuto come un PDF e lo stampa sulla stampante definita tramite l'invocazione del programma Actobat Reader.
- GHOSTPRINTER :  interpreta lo stream ricevuto come un PDF e lo stampa sulla stampante definita tramite l'invocazione del programma GhostView.


Ora andrà collegata ad una stampante. Per fare ciò bisogna considerare quanto indicato nel print_handler.

Prendendo ad esempio di aver dichiarato GHOSTPRINTER come print_handler la stampante andrà definita nell'elemento _7_printer  contenuto in _7_GHOSTPRINTER_settings
>  < spool name="RAW" >
      < show_gui >false< /show_gui >
      < print_handler >GHOSTPRINTER< /print_handler >
        < paper_settings >
             < page_format >A4< /page_format >
             < page_orientation >V< /page_orientation >
                  <border>
                      <top_border>10</top_border>
                      <right_border>10</right_border>
                      <bottom_border>20</bottom_border>
                      <left_border>10</left_border>
                  </border>
        </paper_settings>
      < PRINTER_settings >
         < printer >\\nomeserver\nomecondivisionestampante< /printer >
      < /PRINTER_settings >
      < GHOSTPRINTER_settings >
         < printer >\\nomeserver\nomecondivisionestampante< /printer >
         <parameters>-dPDFFitPage</parameters>
      < /GHOSTPRINTER_settings >
      < FILE_settings >
           < out_dir >C : /temp/< /out_dir >
     < /FILE_settings >
 < /spool >


L'esempio riportato definisce una coda di stampa denominata RAW associata ad una stampante condivisa "\\nomeserver\nomecondivisionestampante" definita nel tag GHOSTPRINTER_settings.
Questo vuol dire che tutte le richieste di stampa che saranno indirizzate allo spool virtuale RAW saranno stampate su questa stampante condivisa.
Il gestore della coda di stampa definito è GHOSTPRINTER che usa GhostPrint (che deve essere installato a parte ed il cui percorso deve essere indicato nell'apposita sezione all'inizio del file di configurazione).
L'alternativa è PRINTER che usa l'Acrobat Reader indicato all'inizio del file di configurazione.
Tale gestore definisce il driver di trasformazione del PDF in PCL per la stampante.
Qualora si utilizzi il print_handler GHOSTPRINTER, è possibile definire esplicitamente l'orientamento della stampa da produrre. Se si definisce una coda con page_orientation H la coda stamperà sempre orizzontale, se la si definisce V stamperà sempre verticale. Se al contrario si omette la definizione dell'attributo page_orientation anche il gestore GHOSTPRINTER si comporterà come PRINTER ruotando automaticamente la stampa.
Quindi una coda GHOSTPRINTER che ruoti automaticamente la stampa dovrà essere definita nel seguente modo : 

>  < spool name="RAW" >
      < show_gui >false< /show_gui >
      < print_handler >GHOSTPRINTER< /print_handler >
        < paper_settings >
             < page_format >A4< /page_format >
                  <border>
                      <top_border>10</top_border>
                      <right_border>10</right_border>
                      <bottom_border>20</bottom_border>
                      <left_border>10</left_border>
                  </border>
        </paper_settings>
      < PRINTER_settings >
         < printer >\\nomeserver\nomecondivisionestampante< /printer >
      < /PRINTER_settings >
      < GHOSTPRINTER_settings >
         < printer >\\nomeserver\nomecondivisionestampante< /printer >
         <parameters>-dPDFFitPage</parameters>
      < /GHOSTPRINTER_settings >
      < FILE_settings >
           < out_dir >C : /temp/< /out_dir >
     < /FILE_settings >
 < /spool >


Inoltre, sempre in riferimento al caso del print_handler GHOSTPRINTER, verrà utilizzata la stampante definita nel tag GHOSTPRINTER_settings. In questo caso è anche possibile passare al motore ghostscript, attraverso l'elemento **parameters** dei parametri da lui interpretati e sul cui significato si rimanda alla documentazione GhostScript. Di default viene già gestito il parametro **-dPDFFitPage** che indica a ghostscript di adattare la pagina da stampare al foglio previsto.

All'interno di una istanza del server SmePD è possibile definire più code di stampa virtuali semplicemente replicando il blocco di configurazione precedente. Si ricorda comunque che il nome delle code di stampa è univoco.

Nel caso si utilizzi GhostPrint come motore di stampa è possibile vedere le stampanti disponibili lanciando lo script **lista_stampanti_ghostscript.bat**. Il risultato sarà, a seconda delle versioni, l'emissione nella finestra DOS o la creazione di un file lista.txt, con l'elendo delle stampanti utilizzabili da GhostPrint.

**ATTENZIONE** :  l'editing del file lpd_config.xml può essere effettuato con un qualunque editor di testo ma NON CON Notepad di Windows. In taluni casi infatti Notepad corrompe il file in fase di slavataggio inserendo alcuni byte che non lo rendono leggibile come xml. Inoltre è preferibile editare il file, trattandosi di file xml, con un editor che faccia anche una verifica sintattica in maniera che modificandolo lo si renda non xml-compliant.

## Installazione del server SmePD come servizio NT
E' possibile installare il server di stampa SmePD come servizio NT in modo tale che sia attivato automaticamente in fase di avvio della macchina.
Prima di procedere con l'installazione del servizio è necessario modificare il file  **wrapper.conf** presente nella cartella **serviceNT\conf\** sistemando le due voci : 

wrapper.ntservice.account=DOMINIO\utente
wrapper.ntservice.password=password

con un account di dominio che abbia accesso alle risorse di rete o comunque alle stampanti che si intendono usare (un utente Domain Admins se non ci sono controindicazioni).
Visto che nel file di configurazione andrà inserita la password e con tale password si avvierà il servizio, il successivo cambio della password dell'utente utilizzato bloccherebbe l'avvio del servizio e obbligherebbe alla disintallazione del servizio, alla modifica del file di configurazione e alla sua reinstallazione. Ciò potrebbe suggerire la creazione di un utente lpduser, con accesso alle risorse di rete ed alle stampanti, da usare a questo specifico scopo.

**Attenzione** :  la sintassi del file di configurazione di wrapper.conf prevede che il carattere **-** ad inizio riga trasformi l'intera riga in commento. Assicurarsi quindi che le righe di configurazione che eventualmente si sono modificate non siano commentate, altrimenti le modifiche nona avranno influenza sul server

Una volta sistemato il file di configurazione è possibile installare l'applicazione come servizio attraverso il richiamo dello script **ServiceInstall.bat**. Viceversa, nel caso sia necessaria la disintallazione del servizio è sufficiente il richiamo dello script **ServiceUnistall.bat**.  Nel caso invece non si desideri l'installazione del server SmePD come servizio NT è necessario l'avvio manuale del programma attraverso il comando **start.bat**. In questo caso il servente sarà attivo per tutto il tempo in cui il programma rimane attivo.

## Configurazione del device virtuale su AS/400
Una volta installato su un PC il servente SmePD è necessario configurare su AS/400 i device di stampa virtuali.
La regola è quella di definire un device virtuale per ognuna delle code di stampa definite nel server SmePD.

La procedura è la seguente : 

- Collegarsi al sistema AS400 con una utenza _2_QSECOFR
- Come prima cosa è indispensabile compilare correttamente la tabella hosts dell'AS400
 -- lanciare il comando _2_cfgtcp
 -- selezionare l'opzione 10 'Gestione voci di tabella host TCP/IP'  e creare l'associazione nome host -> indirizzo IP, usando l'opzione 1.
 -- Nel campo 'indirizzo internet' specificare l'indirizzo IP del personal computer dove è stato installato SmePD e, dopo aver confermato con invio, inserire nel campo 'nome' il nome host del personal, nel nostro caso '_2_PC_SMEPD', confermando sempre con invio.
- Di seguito è riportata la sequenza dei comandi per l'intera configurazione stampante, dove la coda di stampa del sistema OS400 verrà denominata '_2_SMEPD' con descrizione '_2_STAMPANTE PDF'. Il personal computer con installato SmePD verrà chiamato '_2_PC_SMEPD', la sua coda di stampa '_2_RAW' e il suo indirizzo IP '_2_192.168.1.xxx'.


### Comando di creazione OUTQ remota
CRTOUTQ OUTQ(_2_SMESYS/SMEPD) RMTSYS(*INTNETADR) RMTPRTQ('_2_RAW') CNNTYPE(*IP) DESTTYPE(*OTHER) TRANSFORM(*NO) INTNETADR('_2_192.168.1.xxx') TEXT('_2_STAMPANTE PDF')

Nota :  Sperimentalmente si è notato come l'indicazione diretta dell'IP invece del nome
simbolico generi una situazione più stabile. Si consiglia pertanto l'indicazione diretta dell'IP.
 :  : INI Creazione OUTQ remota
 :  : CMD CRTOUTQ OUTQ(SMESYS/SMEPD) RMTSYS(*INTNETADR)  RMTPRTQ(RAW) CNNTYPE(*IP) DESTTYPE(*OTHER) TRANSFORM(*NO) INTNETADR('192.168.1.xxx') TEXT('STAMPANTE PDF')
 :  : FIN

### Comando di avvio OUTQ remota
STRRMTWTR OUTQ(_2_SMEPD)
 :  : INI Avvio OUTQ remota
 :  : CMM STRRMTWTR OUTQ(SMEPD)
 :  : FIN




Il punto 3 va eseguito n volte, una per ognuna delle code di stampa definite sul server SmePD.

Se è necessario modificare la configurazione della coda una volta configurata bisogna procedere nel seguente modo (es. con OUTQ di nome _2_SMEPD) : 


- Fermare il programma di gestione della OUTQ con ENDWTR WTR(_2_SMEPD) OPTION(*IMMED)
- Modificare la configurazione con CHGOUTQ OUTQ(_2_SMEPD) ed accedere ai parametri con F4
- Confermare all'uscita e, se necessario, riavviare il programma con STRRMTWTR OUTQ(_2_SMEPD)



Una volta modificati i file di configurazione, è possibile testare il corretto funzionamento del servizio prima di installarlo tramite il programma **ServiceTest.bat** nella cartella di installazione del server.


Qualora si vogliano modificare le impostazioni, ovviamente con un utente AS400 con le autorizzazioni per farlo, del device stampante precedentemente configurato è necessario procedere come per qualunque altro device stampante AS400  : 

- visualizzare il programma che gestisce il device stampante del sistema OS400 verrà denominato, che come esempio chiameremo '_2_SMEPD'
WRKWTR WTR(*all) OUTQ(QUSRSYS/_2_SMEPD)
- interrompere tale programma
- rieseguire il comando _2_CHGOUTQ con i parametri corretti

