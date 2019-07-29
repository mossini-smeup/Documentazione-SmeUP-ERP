# Utilizzo schedulatore cron per As.UP

## Cos'è lo schedulatore e come funziona

Lo schedulatore As.UP è una funzionalità che consente l'esecuzione temporizzata di specifici comandi e procedure. Lo
schedulatore As.UP si basa sull'integrazione tra tre elementi di sistema

***Lo schedulatore di sistema operativo (Chron nel caso di Linux)**

Consente la schedulazione dei singoli eventi

***Lo SmeupProvider**

Mette a disposizione il webservice che, invocato dallo schedulatore, consente di inviare al server As.UP il
comando da eseguire. Per la configurazione dello SmeupProvider e dell'accesso al WebService vedi la
documentazione specifica per questo prodotto.

***Il server As.UP**

E' il server che eseguirà fisicamente il comando schedulato

## 1) Prerequisiti su sistema Linux

Programmi di sistema necessari al funzionamento dello schedulatore : 

***Bash**
***Cron**
***Crontab**
***Curl**

Script As.UP (script bash di accesso Cron specifici per As.UP. Vanno installati nella cartella utente e autorizzati come eseguibili) : 

***listcron**
***addcron**
***removecron**
***call_ws**
***cronlog**

## 2) Comandi di gestione Cron

A seguire, la lista dei comandi Chron utili per la gestione manuale dei processi schedulati : 

### 2.1) Lista dei processi schedulati

Visualizza la lista dei processi schedulati (solo quelli As.UP)

Comando :  **./listcron**

per visualizzare tutti i processi : 

 Comando :  **crontab -l**

### 2.2) Visualizzazione log delle sottomissioni

Visualizza la lista dei processi sottomessi limitatamente alle funzioni As.UP

 Comando :  **./cronlog**


### 2.3) Gestione processi As.UP schedulati

Visualizza in un editor la lista dei processi schedulati e consente la gestione dei processi As.UP da inserire nel motore di schedulazione

 Comando :  **crontab -e**

I processi As.UP sono inseriti come righe con il seguente formato : 

**mm hh dd MM DD sh call_ws asupProvider port system user pwd env "cmd" id name "Description"**

dove : 

***mm** :  minuti (* per tutti i minuti)
***hh** :  ore (* per tutte le ore)
***dd** :  giorno del mese (numero 1-31, * per tutti)
***MM** :  mese (numero 1-12, * per tutti)
***DD** :  giorno della settimana (mon, tue, wed, thu, fri, sat, sun, * per tutti i giorni)
***asupProvider** :  indirizzo IP dell'As.UP provider che fornisce il webservice per esecuzione comandi (XMLStatelessService)
***port** :  porta di accesso al webservice (9090 per default)
***system** :  indirizzo server As.UP
***user** :  utente di sottomissione del comando su As.UP
***pwd** :  password per utente As.UP
***cmd** :  comando As.UP da eseguire (deve essere tra doppi apici)
***id** :  codice processo schedulato (codice 6 cifre univoco)
***name** :  nome del processo schedulato
***description** :  descrizione del processo schedulato (tra doppi apici)

Esempio : 

**00 * * 8 mon sh call_ws asuptest.smeup.com 9090 MUAS01 FORDAR FORDAR 001 "CALL MUAPI01" SCD001MUAPI01 "Test"

Esegue il comando "CALL MUAPI01" al minuto 00 (mm=00) di tutte le ore (hh=*) di tutti i giorni (dd=*) del mese di agosto (MM=8) che cadono di lunedi (DD=mon).
La richiesta comando viene inviata al web service (XMLStatelessService) attivo sullo SmeupProvider asuptest.smeup.com sulla porta 9090 e sarà indirizzata al
server As.Up contrassegnato dal codice MUAS01 con l'utente FORDAR.

Per uscire dall'editor e salvare gli oggetti schedulati premere CTRL+X e confermare il salvataggio del file con Y (o con N se non si vogliono salvare le modifiche)

Per disabilitare un processo di schedulazione è sufficiente commentare la riga relativa anteponendo un -

## 3) Comandi As.UP per la gestione dei processi schedulati

**TODO**


