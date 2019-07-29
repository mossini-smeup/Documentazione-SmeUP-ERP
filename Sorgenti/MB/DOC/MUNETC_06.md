# WebService per invocazione servizi in As.UP

La piattaforma As.UP prevede la possibilità di invocare l'esecuzione di un servizio attraverso una richiesta inviata
ad uno specifico servizio WebService attivo su piattaforma web integrata (basata sull'application server Jetty).

Le modalità di accesso al servizio sono due.

## Accesso al WebService in modalità sessionless

In questa modalità, la richiesta WebService viene gestita come richiesta unitaria di esecuzione del servizio.
Alla ricezione della richiesta, viene creata una sessione di lavoro temporanea su As.UP e all'interno di
questa sessione vien eseguito il servizio richiesto. Al termine dell'esecuzione, l'eventuale risposta in
formato XML viene tornata al chiamante e la sessione di lavor temporanea viene chiusa.

Il formato della richiesta web è la seguente : 

**http://<server>:8282/SLWSService?user=<user>&fun=<fun>**

dove


- <**server** > : IP del server As.UP o nome host corrispondente
- <**user**> :  utente As.UP da utilizzare per l'esecuzione della funzione
- <**fun**> :  servizio richiesto, in formato funizzato secondo lo standard Looc.UP. In caso di richieste web di
tipo GET Eventuali spazi presenti nella stringa funzione vanno sostituiti con %20. La sostituzione non è
invece necessaria se l'invocazione al web service avviene in modalità POST.


La risposta è in formato XML.


Esempio di richiesta : 

http://muas01:8282/SLWSService?user=GIAGIU&fun=F(EXB;MUJ08_SE;EXE.CMD)%201(J1;CMD;WRKACTJOB)

produce un XML di risposta del tipo : 


><UiSmeup Testo=" - ">
  <Service Titolo1="" Titolo2="" Funzione="F(EXB;MUJ08_SE;EXE.CMD)" Servizio="MUJ08_SE" TSep="." DSep=","/>
    <Griglia>
      <Colonna Cod="COD000" Txt="creationInfo" Tip="" Lun="12" IO="O" Ogg="**" Dpy="" Fill="" Aut=""/>
      <Colonna Cod="COD001" Txt="currentLibrary" Tip="" Lun="10" IO="O" Ogg="**" Dpy="" Fill="" Aut=""/>
      <Colonna Cod="COD002" Txt="dateFormat" Tip="" Lun="10" IO="O" Ogg="**" Dpy="" Fill="" Aut=""/>
      <Colonna Cod="COD003" Txt="dateSeparator" Tip="" Lun="1" IO="O" Ogg="**" Dpy="" Fill="" Aut=""/>
      <Colonna Cod="COD004" Txt="jobID" Tip="" Lun="13" IO="O" Ogg="**" Dpy="" Fill="" Aut=""/>
      <Colonna Cod="COD005" Txt="jobName" Tip="" Lun="10" IO="O" Ogg="**" Dpy="" Fill="" Aut=""/>
      <Colonna Cod="COD006" Txt="jobNumber" Tip="" Lun="6" IO="O" Ogg="**" Dpy="" Fill="" Aut=""/>
      <Colonna Cod="COD007" Txt="jobStatus" Tip="" Lun="9" IO="O" Ogg="**" Dpy="" Fill="" Aut=""/>
      <Colonna Cod="COD008" Txt="jobType" Tip="" Lun="7" IO="O" Ogg="**" Dpy="" Fill="" Aut=""/>
      <Colonna Cod="COD009" Txt="jobUser" Tip="" Lun="10" IO="O" Ogg="**" Dpy="" Fill="" Aut=""/>
      <Colonna Cod="COD010" Txt="libraries" Tip="" Lun="9" IO="O" Ogg="**" Dpy="" Fill="" Aut=""/>
      <Colonna Cod="COD011" Txt="messages" Tip="" Lun="8" IO="O" Ogg="**" Dpy="" Fill="" Aut=""/>
      <Colonna Cod="COD012" Txt="switches" Tip="" Lun="8" IO="O" Ogg="**" Dpy="" Fill="" Aut=""/>
      <Colonna Cod="COD013" Txt="timeSeparator" Tip="" Lun="1" IO="O" Ogg="**" Dpy="" Fill="" Aut=""/>
     <Colonna Cod="COD014" Txt="variables" Tip="" Lun="9" IO="O" Ogg="**" Dpy="" Fill="" Aut=""/>
    </Griglia>
    <Righe>
      <Riga Fld="Mon Jan 11 1|QSYS |DMY |/|66a32fe3-2495|LO_E115520|114709|Run |Batch |FORDAR |[QTEMP, P|[] |00000000| : |[org.smeu|"/>
      <Riga Fld="Mon Jan 11 1|QSYS |DMY |/|1204b2a7-fadd|QAS114708 |114708|Active |Batch |FORDAR |[QTEMP, P|[114709]|00000000| : |[org.smeu|"/>
      <Riga Fld="Mon Jan 11 1|QSYS |DMY |/|2101cbbd-780c|QAS114710 |114710|Run |Batch |GIAGIU |[QTEMP, Q|[] |00000000| : |[] |"/>
    </Righe>
</UiSmeup>



## Accesso al WebService con mantenimento di sessione

In questa modalità, il WebService consente il mantenimento di una sessione e l'esecuzione all'interno di
questa sessione di più di una richiesta servizio.

In questa modalità, la richiesta al WebService prevede tre fasi distine


- Connessione e creazione di una sessione di comunicazione
- Richiesta di funzione (per n volte)
- Disconnessione


E' possibile aprire e tenere contemporaneamente aperte più sessioni di comunicazione. La singola
sessione sarà identificata dal suo codice univoco di sessione e si manterrà attiva fino
a quando non verrà esplicitamente chiusa con un comando di disconnessione.


### Fase 1 :  connessione e creazione sessione

In questa fase viene autenticato l'utente e creata una nuova sessione di comunicazione.
Il formato della richiesta web è la seguente : 

**http://<server>:8282/WSService?cmd=INI&sessionID=<session_id>&user=<user>**

dove : 


- Parametro cmd impostato a INI
- <**server** > : IP del server As.UP o nome host corrispondente
- <**session_id**> :  codice univoco di sessione (consigliato numerico a 6 cifre)
- <**user**> :  utente As.UP da utilizzare per l'esecuzione della funzione


A seguito di questa invocazione viene creata una sessione di comunicazione per l'utente USER identificata
dal codice di sessione univoco SESSION_ID.

Esempio : 

http://muas01:8282/WSService?cmd=INI&sessionID=123456&user=FORDAR

### Fase 2 :  richiesta di servizi

In questa fase (ripetuta più volte) viene utilizzata la sessine di di connessione identificata dal
codice sessione passato per l'esecuzione di richieste di servizio.

Il formato della richiesta è del tipo : 

**http://<server>:8282/WSService?cmd=FUN&sessionID=<session_id>&fun=<fun>**

dove : 


- Parametro cmd impostato a FUN
- <**server** > : IP del server As.UP o nome host corrispondente
- <**session_id**> :  codice univoco di sessione, lo stesso passato nella fase 1
- <**fun**> :  servizio da eseguire in formato funzione Looc.UP


Nel caso venga passato un codice sessione non corrispondente a nessuna sessione esistente
la richiesta ritorna un errore e il servizio non viene eseguito.

Esempio : 

http://muas01:8282/WSService?cmd=FUN&sessionID=123456&fun=F(EXB;MUJ08_SE;EXE.CMD)%201(J1;CMD;WRKACTJOB)

### Fase 3 :  chisura sessione di comunicazione

In questa fase viene chiusa la sessione di comunicazione identificata da uno specifico
codice sessione.
Il formato della richiesta web è la seguente : 

**http://<server>:8282/WSService?cmd=CLO&sessionID=<session_id>

dove : 


- Parametro cmd impostato a CLO
- <**server** > : IP del server As.UP o nome host corrispondente
- <**session_id**> :  codice della sessione di comunicazione da chiudere


Esempio : 

http://muas01:8282/WSService?cmd=CLO&sessionID=123456
