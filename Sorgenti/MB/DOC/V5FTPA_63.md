# Checklist di installazione

Questa sezione della documentazione ha come scopo quello di fornire una serie di controlli da fare in fase di installazione della Fatturazione Elettronica per verificarne il funzionamento.

## Controlli di competenza dell'infrastruttura

- **Capire se configurare uno Smart Kit Sme.UP o non Sme.UP.**
Per farlo chiedere al consulente applicativo se il cliente utilizza Sme.UP ERP per il ciclo attivo o per la contabilità. Se sì va configurato uno Smart Kit Sme.UP (con codice ambiente valorizzato), altrimenti va configurato uno Smart Kit NON Sme.UP (con codice ambiente vuoto).
- **Controllare il nome coda impostato nel file di configurazione**
Se il cliente è in Condominio, oppure se si attivano più Smart Kit per diversi sistemi informativi sullo stesso IBM i assicurarsi di impostare un nome coda "parlante" di 6 caratteri, in modo da garantirne l'univocità (altrimenti gli Smart Kit si consumano a vicenda i dati scritti sulla coda).
__Comunicare il nome della coda del provider al consulente applicativo.__
- **Pagina di debug del provider**
http://indirizzo-ip-macchina:8080/smeup-provider-fe/debug
- **Probe**
-- __test connettività__
http://indirizzo-smartkit:8080:8080/smeup-provider-fe/ProbesService/connectivity
-- __test interazione con Sme.UP ERP, valido ovviamente solo per situazioni con SmeUP su as400__
http://indirizzo-smartkit:8080/smeup-provider-fe/ProbesService/appserver
-- __test raggiungibilità dei folder di rete configurati__
http://indirizzo-smartkit:8080/smeup-provider-fe/ProbesService/folders



## Controlli di competenza del consulente applicativo
### Prima dell'avvio dello Smart Kit

- **Capire se il consulente di infrastruttura debba configurare uno Smart Kit Sme.UP o non Sme.UP.
-- Se il ciclo attivo è gestito con i **documenti V5** di Sme.UP ERP va configurato uno **Smart Kit Sme.UP, comunicando quindi al consulente di infrastruttura oltre a utente e pqssword anche il codice ambiente.
-- Se il cliente ha la **contabilità di Sme.UP ERP, ma il ciclo attivo non è gestito con i documenti V5** di Sme.UP ERP, va configurato uno **Smart Kit Sme.UP** aggiungendo nello **script SCP_CLO** dell'utente dello Smart Kit l'attivazione del plugin necessario per le funzioni non Smeup utilizzate per l'invio fatture tramite il pacchetto NON Smeup.
-- Se il cliente **non utilizza Sme.UP ERP** va configurato uno **Smart Kit NON Sme.UP**(con codice ambiente vuoto).
- **Utente di accesso Smart Kit** :  assicurarsi che l'utente abbia accesso e autorizzazioni sull'ambiente a cui si collega lo Smart Kit.
__Per Smart Kit Sme.UP__ :  verificarlo collegandosi con Loocup all'ambiente corretto usando l'utente dello Smart Kit
- **Ambiente di accesso Smart Kit** :  assicurarsi che l'ambiente a cui si collega lo Smart Kit abbia in linea gli aggiornamenti per la FE.
- **Impostare il nome dello Smart Kit nella tabella V50** (impostare il parametro allo stesso modo in ambiente di produzione e in ambiente di test)
__Concordare il nome della coda del provider al consulente applicativo.__
Se il cliente è in Condominio, oppure se si attivano più Smart Kit per diversi sistemi informativi sullo stesso IBM i assicurarsi di impostare un nome coda "parlante" di 6 caratteri, in modo da garantirne l'univocità (altrimenti gli Smart Kit si consumano a vicenda i dati scritti sulla coda).
**N.B. : ** E' necessario che lo Smart Kit venga avviato dopo aver compilato il campo**"SmeUP Provider Ft El" della tabella V50 e riavviato successivamente a modifiche del campo stesso

### Dopo l'avvio dello Smart Kit

- **Controllo collegamento Smart Kit** :  da Loocup, dal Menù "Cruscotto invio Fatture" aprire la scheda Provider, controllare i dati della dashboard e verificare che scegliendo la voce LOA38 dall'albero del menù si veda l'albero Network con la voce "61 - Interfaccia intermediari SDI" .
- In loocup dal Menù "Cruscotto invio Fatture" scegliere il tab "Controlli di sistema" e verificare che non siano indicati errori.
**N.B. : ** E' necessario che lo Smart Kit venga avviato dopo aver compilato il campo**"SmeUP Provider Ft El" della tabella V50 e riavviato successivamente a modifiche del campo stesso
- **Controllo impostazione data attivazione FE** :  indicare la data di attivazione della FE nella categoria parametri £CA dell'azienda. (Impostazione necessaria solo prima del 01/01/19)
- Controllo estensione £51 su cliente :  controllare di aver impostato sul cliente a cui si vuole inviare la fattura elettronica il codice univoco di identificazione o la pec. (Impostazione obbligatoria solo prima del 01/01/19)
- **In installazioni Multiazienda** controllare che i file EDSEND0F e EDRECI0F NON siano in comune, e che le tabelle e i parametri siano correttamente configurati in tutte le aziende.



## Invio fatture tramite pacchetto NON Smeup in ambienti con Contabilità Sme.UP
Impostarte nello script SCP_CLO dell'utente di collegamento dello Smart Kit l'attivazione del plugin aggiungendo sotto la sezione ** :  : C.SEZ Cod="Server"** le seguenti righe : 
_  :  : C.SER Cod="031" Txt="Abletech Connector Server" Add="localhost" Protocol="JAVA"                Param="class=Smeup.smeui.uicommon.uiexternalservices.java.ix_abletetch.IXWebserviceJavaExternalService" LoadOnStartup="1" 

Nel caso non sia già presente la sezione ** :  : C.SEZ Cod="Server"** aggiungerla prima delle righe sopra indicate.

## Criterio di completamento dell'installazione
Il criterio di completamento dell'installazione è dato dal successo della richiesta dell'Aooid.
Può essere eseguito ogni volta che vengono fatte delle modifiche per testarne la correttezza.
**Per lanciarlo occorre cliccare sull'apposito bottone all'interno della scheda "Controlli di
sistema"
