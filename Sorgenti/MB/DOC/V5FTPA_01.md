# La fatturazione elettronica

## Il processo
Il processo di fatturazione elettronica verso la Pubblica Amministrazione e i Privati prevede i seguenti passaggi.
 * Generazione XML conforme a specifiche. SmeUP generà un XML per ogni singola fattura (non è prevista la possibilità di gestire lotti di fatture)
 * Firma del file (obbligatoria solo per PA) :  la firma può essere in  formato CAdES-BES (CMS Advanced Electronic Signatures) oppure in formato XAdES-BES (XML Advanced Electronic Signatures). Il software utilizzato per apporre la firma deve essere in grado di valorizzare il parametro "signing time", che riporta la data e l'ora, ed anche la "time zone" e che assume il significato di riferimento temporale. Non è invece necessaria l' apposizione della marca temporale. In base al formato di firma adottato, l'estensione del file assume il valore ".xml.p7m" (per la firma CAdES-BES) oppure ".xml" (per la firma XAdES-BES).
 * Invio a Sdi. Le possibili modalità di trasmissione sono : 
 ** Invio manuale tramite il sito web http://www.fatturapa.gov.it/ ;
 ** Invio tramite web-services (SDICoop) ;
 ** Invio tramite Posta Elettronica Certificata (PEC) ;
 ** Invio tramite FTP (SDIFTP) ;
 ** Invio tramite Porta di dominio (SPCoop) .
Sme.UP Erp consente l'invio tramite web-services grazie all'integrazione con la soluzione di firma digitale, invio e conservazione sostitutiva di Abletech, nostro partner già accreditato presso il Sistema di Interscambio.
Le altre modalità di invio non sono direttamente interfacciate, ma possono essere gestite a partire dal file xml generato da Sme.UP Erp, provvedendo autonomamente in modo manuale alla firma elettronica, all'invio al SdI e alla conservazione sostitutiva.
Il SdI prende in carico il file ed entro 5 giorni ne esegue un controllo formale verificando anche che la fattura non sia stata precedentemente già inviata. Se il file supera i controlli la fattura risulta emessa e il file viene inoltrato al destinatario della fattura, in base al codice univoco di identificazione dell'ufficio se si tratta di una PA, del codice intermediario o della pec nel caso di fattura B2B. Se il fiel non risulta conforme viene inviato un esito di Scarto e la fattura risulta NON emessa.
Nel caso in cui il Sdi abbia dato esito positivo provvederà a recapitare il file XML al destinatario. Nel caso in cui il canale ricevente non sia immediatamente raggiungibile il Sdi continuerà a contattarlo per 10 giorni. Se passati i 10 giorni il Sdi non riuscirà a contattare il canale invierà al cedente un messaggio di _Mancata consegna_ e il cedente dovrà preoccuparsi di inviare al cessionario una mail di notifica della mancata consegna. Contemporaneamente il Sdi depositerà il file XML nell'Area riservata del cessionario.
Una volta ricevuta la conferma dellìemissione della fattura, inoltre, il cedente dovrà preoccuparsi della sua conservazione elettronica.

## Precisazione
Dal 1 gennaio 2017 è in vigore il tracciato 1.2 della fatturazione elettronica, che consente di  emettere sia fatture elettroniche verso la PA che fatture elettroniche B2B e di inviarle tramite il Sistema di Interscambio gestito da Sogei (società del Ministero dell'Economia e delle Finanze).
 :  : NPG

## Timeline

### 06/06/2014  :  Fatturazione elettronica verso le Pubbliche amministrazioni centrali

**Presidenza del Consiglio dei Ministri e Ministeri** **(comprese anche tutte le unità organizzative locali afferenti ai Ministeri** **es. Arma dei Carabinieri, Vigili del Fuoco, Polizia di Stato)
**Istituti di Istruzione Statale di ogni ordine e grado**
**Agenzie fiscali**
**Agenzia del Demanio**
**Agenzia delle Dogane e dei Monopoli**
**Agenzia delle Entrate**
**Enti nazionali di previdenza e assistenza sociale**

### 31/03/2015  :  Fatturazione elettronica verso tutte le Pubbliche amministrazioni

### 01/01/2017  :  Inizio fase sperimentale fatturazione elettronica B2B

### 01/07/2018  :  Fatturazione elettronica B2B obbligatoria per gli operatori del settore dei subappalti pubblici e della filiera dei carburanti con eliminazione della scheda carburante.

### 01/01/2019  :  Fatturazione elettronica B2B obbligatoria per tutte le aziende e professionisti sia nei rapporti B2B che nei rapporti B2C.


## Reperire il Codice Univoco Ufficio di ciascuna PA
Qualora il Codice Univoco Ufficio non sia stato comunicato al fornitore dalla PA destinataria, sul sito http://www.indicepa.gov.it/documentale/ricerca.php , nella sezione informazioni _Servizi di Fatturazione Elettronica_  di ciascun ente è possibile reperire il Codice Univoco Ufficio e la data di avvio del servizio di fatt razione elettronica.
Eseguendo la ricerca per Codice Fiscale cliccare su _CERCA UFFICIO DESTINATARIO DELLE FATTURE_.
Eseguendo le altre tipologia di ricerca dall'elenco delle amministrazioni trovate cliccare sulla sezione delle informazioni _Servizi di Fatturazione Elettronica_ identificabile da una icona con il simbolo dell'Euro.
Unicamente nel caso in cui il fornitore, non avendo ricevuto la comunicazione del codice ufficio destinatario da parte dell'amministrazione e, pur avendo riscontrato la presenza dell'amministrazione in IPA non sia in grado di individuare in modo univoco, sulla base dei dati contrattuali in proprio possesso, l'Ufficio destinatario della fattura, è consentito l'utilizzo di un Ufficio di fatturazione elettronica "Centrale" denominato "Uff_eFatturaPA".
Nel caso in cui il fornitore, non avendo ricevuto alcuna comunicazione da parte dell'amministrazione, abbia rilevato l'assenza in IPA dell'amministrazione stessa, il codice ufficio da inserire in fattura può assumere il valore di default "999999".
Nel caso in cui sia possibile identificare univocamente un Ufficio di fatturazione elettronica, sulla base dei dati fiscali di destinazione della fattura in essa contenuti, il SdI respinge la fattura inviando al mittente una "notifica di scarto", segnalando il codice ufficio identificato.

 :  : NPG
