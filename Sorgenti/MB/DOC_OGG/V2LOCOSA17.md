

# Prerequisiti
Installazione e configurazione dello SMENS per il funzionamento della £G53.

# Configurazione invio e-mail

Lo scopo del costruttore LOA17 è la configurazione delle modalità di invio delle e-mail.
Le impostazioni vengono scritte in membri LOA17* del file SCP_SET .

Lo script è composto da sezioni (tag SEZ) e subsezioni (tag SUB).
L'identificazione e l'indirizzamento di un tipo mail è quindi data da un codice composto dal suffisso del membro (per 2 caratteri) più sezione e subsezione per tre caratteri ciascuno.
Quindi, ad esempio, X1.A01.001 indica un tipo mail definito nel membro LOA17_X1 sezione A01, subsezione 001.

## Invio della mail tramite il servizio B£SER_85
L'invio della mail avviene tramite il richiamo del B£SER_85 tramite una funzione A(EMU , una funzione A con entry del servizio invece che entry funizzata.
**Esempio di chiamata : **
A(EMU;B£SER_85;MAI.OGG) 1(;;X1.A01.001)  2(CN;CLI;&CO.Cod) INPUT(SJ(Report del &AM.DT) TX(-TEXT-/Smedoc/testo.html))


| Parametro | Valore |  Descrizione |
| ---|----|----|
| Metodo | MAI.OGG | Invio dell'e-mail ad un oggetto |
| Oggetto 1 | es. 1(;;X1.A01.001) | Tipo mail per la configurazione dell'invio |
| Oggetto 2 | es  2(CN;CLI;&CO.Cod) | Oggetto da cui reperire il destinatario (se non presente il destinatario deve essere impostato nello script del tipo mail oppure tramite attributo EM() nell'INPUT della chiamata |
| Attributi nell'INPUT della chiamata | EM() | Indirizzo del destinatario |
| | CC() | Indirizzo a cui inviare in copia conoscenza |
| | BC() | Indirizzo a cui inviare in copia conoscenza nascosta |
| | FR() | Indirizzo del mittente |
| | SJ() | Oggetto dell'e-mail |
| | TX() | Testo del corpo dell'e-mail L'attributo TX() può anche rimandare ad un file di testo o html su IFS con la stessa sintassi usata per la £G53 (es. :  TX(-TEXT-/Smedoc/testo.html) ) |
| | FL() | Cartella sull'IFS in cui reperire i file da allegare. Il percorso va scritto relativamente al Server IBM i (con / ) |
| | AT() | Nomi dei file da allegare separati da ';' . E' anche possibile specificare tutti i file che iniziano con un prefisso (ex XXX*) |
| | TF() | Estensione dei file da allegare. Accetta * per tutti i tipi di file |
| | CA(1) | Cancella l'allegato dopo aver inviato la mail |
| 


**N.B. :  Il funzionamento degli attributi impostati nell'INPUT dipende dalla presenza delle corrispondenti variabili &CO. nello script LOA17_* (come specificato in seguito)




## I tag utlizzati nello script LOA17_*

### MAI.TPM
E' il tag più importante. Contiene le informazioni relative al reperimento degli indirizzi e-mail del mittente e dei destinatari e configura la modalità di esecuzione dell'invio mail. Deve esserci un solo tag MAI.TPM per ogni subsezione.


| Attributo | Descrizione | Spiegazione | Sostituzione |
| ---|----|----|----|
| **Test** | Modalità test                 | **=' '  :  Non invia la mail e scrive una stampa di controllo; ='1'  : Invia la mail all'indirizzo di test specificato in TstM ; ='2'  : Invia effettivamente la mail | |
| **CFTo** | Funz. Aziendali / Mail  To    | Determina il reperimento dell'indirizzo a cui inviare la mail. Può contenere la funzione aziendale (V£F) su cui cercare tramite £G85 l'e-mail dell'oggetto ricevuto. E' anche possibile impostare una risalita separando le funzioni aziendali con ';' . E' inoltre possibile impostare come ultima risalita *FIRST in modo che restituisca l'e-mail associata alla prima funzione aziendale trovata. L'attributo accetta in alternativa l'impostazione di un indirizzo e-mail. | Qualora nello script sia impostato &CO.EM il valore viene recepito dall'attributo EM() ricevuto nell'INPUT della chiamata del B£SER_85 |
| **CFCc** | Funz. Aziendali / Mail  Cc    | Determina il reperimento dell'indirizzo a cui inviare la mail in copia conoscenza. Può contenere la funzione aziendale (V£F) su cui cercare tramite £G85 l'e-mail dell'oggetto ricevuto. E' anche possibile impostare una risalita separando le funzioni aziendali con ';' . E' inoltre possibile impostare come ultima risalita *FIRST in modo che restituisca l'e-mail associata alla prima funzione aziendale trovata. L'attributo accetta in alternativa l'impostazione di un indirizzo e-mail. | Qualora nello script sia impostato &CO.CC il valore viene recepito dall'attributo CC() ricevuto nell'INPUT della chiamata del B£SER_85 |
| **CFBc** | Funz. Aziendali / Mail  Bcc   | Determina il reperimento dell'indirizzo a cui inviare la mail in copia conoscenza nascosta. Può contenere la funzione aziendale (V£F) su cui cercare tramite £G85 l'e-mail dell'oggetto ricevuto. E' anche possibile impostare una risalita separando le funzioni aziendali con ';' . E' inoltre possibile impostare come ultima risalita *FIRST in modo che restituisca l'e-mail associata alla prima funzione aziendale trovata. L'attributo accetta in alternativa l'impostazione di un indirizzo e-mail. | Qualora nello script sia impostato &CO.BC il valore viene recepito dall'attributo BC() ricevuto nell'INPUT della chiamata del B£SER_85 |
| **OFro** | Ogg. Funz. Azi.  From         | Oggetto su sui effettare il reperimento dell'indirizzo e-mail del mittente in caso in From si imposti una funzione aziendale anziché direttamente un indirizzo e-mail | |
| **From** | Funz. Aziendali / Mail  From  | Determina il reperimento dell'indirizzo del mittente. Può contenere la funzione aziendale (V£F) su cui cercare tramite £G85 l'e-mail dell'oggetto ricevuto. E' anche possibile impostare una risalita separando le funzioni aziendali con ';' . E' inoltre possibile impostare come ultima risalita *FIRST in modo che restituisca l'e-mail associata alla prima funzione aziendale trovata. L'attributo accetta in alternativa l'impostazione di un indirizzo e-mail. | Qualora nello script sia impostato &CO.FR il valore viene recepito dall'attributo FR() ricevuto nell'INPUT della chiamata del B£SER_85 |
| **OTst** | Ogg. Funz. Azi.  segnalazioni | Oggetto su sui effettare il reperimento dell'indirizzo e-mail del mittente in caso in TstM si imposti una funzione aziendale anziché direttamente un indirizzo e-mail | |
| **TstM** | Funz. Az./ Mail  segnalazioni | Determina il reperimento dell'indirizzo a cui inviare notifica di anomalie e che viene utilizzato come destinatario nell'invio di test. Può contenere la funzione aziendale (V£F) su cui cercare tramite £G85 l'e-mail dell'oggetto ricevuto. E' anche possibile impostare una risalita separando le funzioni aziendali con ';' . E' inoltre possibile impostare come ultima risalita *FIRST in modo che restituisca l'e-mail associata alla prima funzione aziendale trovata. L'attributo accetta in alternativa l'impostazione di un indirizzo e-mail. **La segnalazione di anomailia si genera qualora non sia reperito il mittente, il destinatario o uno dei file da allegare | |
| 


### MAI.TXT
Contiene le informazioni relative all'oggetto e al testo dell'e-mail. Deve esserci un solo tag MAI.TPM per ogni subsezione.


| Attributo | Descrizione | Spiegazione | Sostituzione |
| ---|----|----|----|
| **Sbj**  | Oggetto della mail        | Testo che appare nell'oggetto della mail | Qualora nello script sia impostato &CO.SJ il valore viene recepito dall'attributo SJ() ricevuto nell'INPUT della chiamata del B£SER_85 |
| **Txt**  | Testo                     | Testo che appare nel corpo della mail  | Qualora nello script sia impostato &CO.TX il valore viene recepito dall'attributo TX() ricevuto nell'INPUT della chiamata del B£SER_85. L'attributo TX() può anche rimandare ad un file di testo o html su IFS con la stessa sintassi usata per la £G53 (es. :  TX(-TEXT-/Smedoc/testo.html) ) |
| **FldT** | Cartella su IFS           | Cartella sull'IFS in cui reperire il file di testo contenente il corpo della mail. Il percorso va scritto relativamente al Server IBM i (con  / ) | |
| **FilT** | File contenente il testo  | Nome del file di testo contenente il corpo della mail | |
| **ScpF** | File sorgente AS400       | File sul Server IBM il cui membro contiene il corpo della mail | |
| **ScpM** | Membro AS400 con il testo | Membro contenente il corpo della mail | |
| 


### MAI.ATT
Contiene le informazioni relative al reperimento degli allegati.  Possono esserci più tag MAI.TPM per ogni subsezione.


| Attributo | Descrizione | Spiegazione | Sostituzione |
| ---|----|----|----|
| **NFld** | Cartella su IFS            | Cartella sull'IFS in cui reperire i file da allegare. Il percorso va scritto relativamente al Server IBM i (con / ) | Qualora nello script sia impostato &CO.FL il valore viene recepito dall'attributo FL() ricevuto nell'INPUT della chiamata del B£SER_85 |
| **NFil** | Files da allegare (sep. ;) | Nomi dei file da allegare separati da ';' . E' anche possibile specificare tutti i file che iniziano con un prefisso (ex XXX*) | Qualora nello script sia impostato &CO.AT il valore viene recepito dall'attributo AT() ricevuto nell'INPUT della chiamata del B£SER_85 |
| **TFil** | Estensione file            | Estensione dei file da allegare. Accetta * per tutti i tipi di file | Qualora nello script sia impostato &CO.TF il valore viene recepito dall'attributo TF() ricevuto nell'INPUT della chiamata del B£SER_85 |
| **FCnd** | Condizioni di validazione  | Espressione di £G91 usata per condizionare il fatto che il file venga allegato. Ad esempio FCnd="&CO.Cod =01" comporta che i file vengano allegati solo se il codice dell'oggetto a cui si sta inviando la mail è 01. |
| **Des**  | Descrizione                | Campo descrittivo | |
| **MTst** | Modalità di test           | Simula il reperimento degli allegati anche se non esistono i file corrispondenti **(DA USARE SOLO IN CASO DI TEST!)** | |
| 


### MAI.CAR
Serve unicamente al caricamento dei dati necessari alla simulazione del corretto reperimento dei dati nalle scheda LOA17.
Non influisce in alcun modo sul funzionamento dell'invio delle mail e può venire omesso dallo script.


| Attributo | Descrizione | Spiegazione |
| ---|----|----|
| **Pgm** | Programma da eseguire |programma che si occupa di ritornare gli oggetti per i quali le istruzioni incluse nel loop dovranno essere eseguite. Come programma di esempio vedere il programma **LOA11_01** |
| **Mod** | Modalità              |passo funzione/metodo del programma stesso. |
| **Par** | Parametri             |posso passare un serie di parametri al programma specifico. |
| 

