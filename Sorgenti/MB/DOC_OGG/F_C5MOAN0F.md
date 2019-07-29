## Contenuto
Suddivisione dell'importo di una riga contabile.

## Codice Oggetto (in TA/*CNTT)
 'MH'                               £FUNT1
 'WK' Se è nel transito             £FUNP1

## Chiave primaria
ID Mov.Analitica                    £FUNK1

## Altri condizionamenti facoltativi in ricerca
N.A.

## Ulteriore chiave primaria
N.A.

## Tabella guida
Le impostazioni che condizionano questo archivio sono contenute in tabella Causale Analitica : 
 :  : DEC T(ST) K(C5L)
Altre impostazioni generali sono contenute in tabella Impostazioni Analitica : 
 :  : DEC T(ST) K(C52)

## Autorizzazioni
Si utilizza la classe 'C5MH01'.

## Note strutturate (Tabella NSC)
Il contenotre si assume da tabella C51 : 
 Chiave 1 'MH'
 Chiave 2 ' ' WK (se è nel transito)
 Chiave 3 IDOJ Analitica

## Parametri (Tabella C£E)
La categoria parametri viene assunta dal campo parametri espiciti di tabella C5L.

## Flussi (Tabella B£H)
Si attivano se è impostato il flag in tabella C51.
La B£H è x-MH (I C....).

## Costruzione automatica campi (tabella B£C)
N.A.

## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
In tabella C5L è possibile impostare una exit di inizializzazione : 
 :  : DEC T(CS) P(T/C5D) K(T$C5LI) R(1)

## /COPY
Interfaccia ANALITICA (£IMH) : 
 :  : DEC T(MB) P(QILEGEN) K(£IMH)

Gestione righe analitica (£C5D) : 
 :  : DEC T(MB) P(QILEGEN) K(£C5D)

## Gruppi flag
Viene assunto il gruppo flag di riga di tabella C5L.

## Workflow e popup
N.A.

## Note particolari

## CONTENUTO DEI CAMPI

 :  : FLD A5AZIE**Azienda**
Codice dell'azienda di riferimento.

 :  : FLD A5DIVI**Divisione**
Se attivata la gestione delle divisioni contiene il codice della divisione specifica. Viceversa contiene la divisione fissa memorizzata nei parametri azienda.

 :  : FLD A5ESER**Esercizio Contabile**
Esercizio contabile di riferimento.

 :  : FLD A5LIVE**Livello**
- Non utilizzato -

 :  : FLD A5STAT**Stato**
- Non utilizzato -

 :  : FLD A5SOCI**Società Intercompany**
Se valorizzato a livello di testata della registrazione contabile o di riga contabile, viene assunto anche a livello di riga di analitica.

 :  : FLD A5SOCO**Società Origine**
- Non utilizzato -

 :  : FLD A5IDOJ**ID Mov.Analitica**
Identificativo univoco della riga di analitica. Viene assunto dal numeratore OG.MH di tabella CRNC5.

 :  : FLD A5CAUS**Causale Analitica**
Viene valorizzata a partire dall'indicazione prevista a livello di tipo registrazione. E' importante per caratterizzare una serie di elementi dell'analitica, in particolare ad esempio se alcune dimensioni di analitica sono fissate a livello di testata e/o riga contabile.

 :  : FLD A5CAUC**Causale Contabile**
Viene ripresa in modo fisso la causale indicata sulla riga contabile.

 :  : FLD A5DESC**Descrizione**
Assume la descrizione della causale contabile, ma può poi essere modificata manualmente.

 :  : FLD A5NDOR**N° Documento**
Assume l'informazione indicata a livello di riga e/o testata contabile.

 :  : FLD A5TPCN**Tipo Contatto**
Assume l'informazione indicata a livello di riga e/o testata contabile (tipo ente intestatario della riga o della registrazione).

 :  : FLD A5SOGG**Soggetto**
Assume l'informazione indicata a livello di riga e/o testata contabile (codice ente intestatario della riga o della registrazione).

 :  : FLD A5TPRO**Tipo protocollo**
Assume l'informazione indicata a livello di testata contabile.

 :  : FLD A5NPRO**N° protocollo**
Assume l'informazione indicata a livello di testata contabile.

 :  : FLD A5RIGA**N° riga**
Numerazione delle righe di analitica collegate ad una riga di registrazione contabile.

 :  : FLD A5TPOR**Tipo Origine**
Oggetto origine, contiene tipicamente E5 per le righe collegate a righe contabili e TAC6B per le righe generate per la definizione di modelli.

 :  : FLD A5CDOR**Codice Oggetto Origine**
Codice oggetto origine, a seconda del tipo contiene il codice oggetto corrispondente (es. nel caso di E5, la riga di registrazione contabile).

 :  : FLD A5DREG**Data registrazione**
Assume l'informazione indicata a livello di testata contabile.

 :  : FLD A5DCOM**Data Competenza**
Assume l'informazione indicata a livello di testata contabile nella data registrazione (di fatto che costituisce un informazione ridondante rispetto alla data registrazione)

 :  : FLD A5DDOR**Data Documento**
Assume l'informazione indicata a livello di riga e/o testata contabile.

 :  : FLD A5DPRO**Data protocollo**
Assume l'informazione indicata a livello di testata contabile.

 :  : FLD A5DPRO**Data protocollo**
Assume l'informazione indicata a livello di testata contabile.

 :  : FLD A5TPN1 **Tipo Oggetto 1**
Contiene il tipo oggetto di una delle dimensioni che si vogliono gestire in analitica per il conto indicato sulla riga contabile.Viene determinato sulla base della struttura indicata nell'elemento della tabella C6B corrispondente al conto contabile.
 :  : FLD A5TPN2.A5TPN1 **Tipo Oggetto 2**
 :  : FLD A5TPN3.A5TPN1 **Tipo Oggetto 3**
 :  : FLD A5TPD1.A5TPN1 **Tipo Oggetto 4**
 :  : FLD A5TPD2.A5TPN1 **Tipo Oggetto 5**
 :  : FLD A5TPD3.A5TPN1 **Tipo Oggetto 6**

 :  : FLD A5CDN1 **Codice Oggetto 1**
Contiene il codice oggetto di una delle dimensioni che si vogliono gestire in analitica per il conto indicato sulla riga contabile.Viene determinato sulla base della struttura indicata nell'elemento della tabella C6B corrispondente al conto contabile.
 :  : FLD A5CDN1.A5TPN1 **Codice Oggetto 2**
 :  : FLD A5CDN3.A5TPN1 **Codice Oggetto 3**
 :  : FLD A5CDD1.A5TPN1 **Codice Oggetto 4**
 :  : FLD A5CDD2.A5TPN1 **Codice Oggetto 5**
 :  : FLD A5CDD3.A5TPN1 **Codice Oggetto 6**

 :  : FLD A5DAAV **Dare/Avere**
Assume l'informazione indicata a livello di riga contabile. Per indicare il segno opposto si può invertire l'importo della riga.

 :  : FLD A5VALU **Valuta**
Divisa assunta dalla riga contabile. NOTA BENE :  a livello di impostazione di base di può decidere che l'analitica sia sempre fissa nella valuta di conto, al di là della valuta della riga contabile.

 :  : FLD A5CAMB **Cambio**
Cambio assunto dalla riga contabile.

 :  : FLD A5IMPO **Importo in valuta di conto**
Importo in valuta di conto della riga di analitica.

 :  : FLD A5IMVA **Importo in valuta**
Importo in valuta della riga di analitica.

 :  : FLD A5CAME **Cambio valuta alternativa**
Se attiva la gestione della valuta alternativa (per la produzione di bilanci in valuta differente dalla valuta di conto), contiene il cambio della valuta alternativa (ricalcolo in modo cieco ad ogni inserimento/modifica della registrazione).

 :  : FLD A5IMVE **Importo in valuta alternativa**
Se attiva la gestione della valuta alternativa (per la produzione di bilanci in valuta differente dalla valuta di conto), contiene l'importo nella valuta alternativa (ricalcolo in modo cieco ad ogni inserimento/modifica della registrazione).

 :  : FLD A5UNMS **Unità di misura**
Se attiva la gestione quantità contiene la tabella di identificazione di tale quantità.

 :  : FLD A5QUAN **Quantità**
Se attiva la gestione quantità ne contiene il valore.

 :  : FLD A5DT01 **Data 1**
E' a disposizione e non è tipizzata.
 :  : FLD A5DT02.A5DT01 **Data 2**
 :  : FLD A5DT03.A5DT01 **Data 3**
 :  : FLD A5DT04.A5DT01 **Data 4**
 :  : FLD A5DT05.A5DT01 **Data 5**

 :  : FLD A5AA01 **Codice 1**
Campo alfanumerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella C5L.
 :  : FLD A5AA02.A5AA01 **Codice 2**
 :  : FLD A5AA03.A5AA01 **Codice 3**
 :  : FLD A5AA04.A5AA01 **Codice 4**
 :  : FLD A5AA05.A5AA01 **Codice 5**

 :  : FLD A5NU01 **Numero 1**
Campo numerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella C5L.
 :  : FLD A5NU02.A5NU01 **Numero 2**
 :  : FLD A5NU03.A5NU01 **Numero 3**
 :  : FLD A5NU04.A5NU01 **Numero 4**
 :  : FLD A5NU05.A5NU01 **Numero 5**

 :  : FLD A5FL01 **Pertinenza**
Identifica se la riga è contabile o extra contabile (con varie accezioni). L'informazione è derivata dalla testata.

 :  : FLD A5FL02 **Condizione**
Identifica se la riga è definitiva o provvisoria (con varie accezioni). L'informazione è derivata dalla testata.

 :  : FLD A5FL03 **Origine**
Identifica il tipo di origine del movimento (se manuale, da conversione, da sistemi conferenti ecc.). L'informazione è derivata dalla testata.

 :  : FLD A5FL04 **Stato registrazione**
Identifica lo stato della registraizone (normale, stornata, stornante).  L'informazione è derivata dalla testata.

 :  : FLD A5FL05**Intercompany**
Identifica il fatto che il movimento è relativo ad un'operazione intercompany. L'informazione è derivata dalla testata.

 :  : FLD A5FL12**Origine Mov. Analitica**
Identifica a differenza del flag 03 che riguarda la testata se il singolo movimento di analitica ha un origine particolare.

 :  : FLD A5DTIN**Data inserimento**
Data inserimento della riga di analitica.

 :  : FLD A5ORIN**Ora inserimento**
Ora inserimento della riga di analitica.

 :  : FLD A5USIN**Utente inserimento**
Utente inserimento della riga di analitica.

 :  : FLD A5DTAG**Data aggiornamento**
Data aggiornamento della riga di analitica.

 :  : FLD A5ORAG**Ora aggiornamento**
Ora aggiornamento della riga di analitica.

 :  : FLD A5USAG**Utente aggiornamento**
Utente aggiornamento della riga di analitica.
