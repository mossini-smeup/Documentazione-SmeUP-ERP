# AGE - Tabella Agenti
 :  : DEC T(ST) K(AGE)
## OBIETTIVO
Permettere la caratterizzazione dei diversi agenti.
## CONTENUTO DEI CAMPI
 :  : FLD T$AGEA **% Provvigione 1**
È usato come "parcheggio" per indicare la percentuale provvigionale fissa dell'agente. Non è utilizzato da nessun programma.
 :  : FLD T$AGEB **Tipo Liquidazione 1**
Indica il tipo di liquidazione previsto per l'agente a meno che non impostato diversamente sulla singola fattura. Può assumere i seguenti valori : 
 - P = Su pagato ------> la liquidazione avviene in rapporto ai pagamenti effettuati nel periodo;
 - S = Su saldato -----> la liquidazione avviene in rapporto ai documenti saldati nel periodo;
 - F = Su fatturato ---> la liquidazione avviene in rapporto ai documenti fatturati nel periodo.
 Se non è impostato verrà utilizzato il tipo liquidazione indicato nella tabella V58.
 :  : FLD T$AGEC **Tipo contatto**
È un elemento TA/BRE. Indica il tipo contatto del soggetto che identifica l'agente in anagrafica
 :  : FLD T$AGED **Piano Enasarco**
È un elemento TA/V6T. Indica il piano in base al quale devono essere calcolati gli importi relativi all'enasarco sul piano delle provvigioni
 :  : FLD T$AGEE **Piano F.I.R.R.**
È un elemento TA/V6U. Indica il piano in base al quale devono essere calcolati gli importi relativi al F.I.R.R. sul piano delle provvigioni
 :  : FLD T$AGEG **Piano I.S.C.**
È un elemento TA/V6V. Indica il piano in base al quale devono essere calcolati gli importi relativi all'I.S.C. sul piano delle provvigioni
 :  : FLD T$AGEF **Codice contatto**
È un elemento CN. Indica il codice del soggetto che identifica l'agente in anagrafica
 :  : FLD T$AGEK **Periodo liquidazione**
Definisce la periodicità di liquidazione dell'agente nel caso differisca rispetto al default indicato nella tabella V58. Può assumere i seguenti valori : 
 - M = Liquidazione mensile
 - T = Liquidazione trimestrale
 - A = Liquidazione Annuale
 :  : FLD T$AGEJ **Piano anticipi**
È un elemento TA/V6Z. Definisce il piano anticipi di riferimento dell'agente nel caso in cui questo sia differente rispetto al default definito nella tabella V58.
 :  : FLD T$AGEH **Data inizio rapporto**
È un elemento D8*YYMD. Definisce la data di inizio dei rapporti con l'agente. Essa viene presa in considerazione quando di devono calcolare i contributi.
 :  : FLD T$AGEI **Data fine rapporto**
È un elemento D8*YYMD. Definisce la data di fine dei rapporti con l'agente. Essa viene presa in considerazione quando si devono calcolare i contributi.
 :  : FLD T$AGEL **Tipo Provvigioni Fattura**
È un elemento TA/V5P. Definisce il tipo di provvigione da utilizzare per l'agente, quando deve essere ripresa una fattura e qualora questa sia differente rispetto al default definito nella tabella V58.
 :  : FLD T$AGEM **Tipo Provvigioni Nota**
È un elemento TA/V5P. Definisce il tipo di provvigione da utilizzare per l'agente, quando deve essere ripresa una nota d'accredito e qualora questa sia differente rispetto al default definito nella tabella V58.
 :  : FLD T$AGEN **Piano Provvigione**
Permette di definire il calcolo delle provvigioni in modo più articolato rispetto al solo utilizzo del campo tipo liquidazione. Se valorizzato il campo tipo liquidazione non verrà tenuto in considerazione.
 :  : FLD T$AGEQ **Sospensione da Liquidazione**
Se attivato l'agente viene escluso dalle elaborazioni di liquidazione.
 :  : FLD T$AGEO **Mesi Slittamento su Fatturato**
Sulle note di accredito e sulle fatture da liquidare con il criterio del fatturato,
verranno applicati i mesi di dilazione indicati in questo campo (es. se metto 3 una fattura di
gennaio verrà liquidata nel periodo corrispondente ad aprile).
 :  : FLD T$AGEP **Agente Enasarco**
Attraverso questo campo è possibile unificare le elaborazioni dei documenti proforma  di più agenti e del calcolo contributi, tipicamente quando più codici agente corrispondono ad un solo fornitore.
E' importante notare che : 
* Non sono gestiti collegamenti multilivello (es. un codice collegato ad un codice che è a sua volta collegato ad un altro codice, a->-b->c)
* Il codice di riferimento deve a sua volta aver indicato se stesso come Agente Enasarco
* E' inoltre importante che se viene modificato/aggiunto il campo, della tabella, sarà necessario riallineare il campo P§COD1 scritto sul file V5PROV.
