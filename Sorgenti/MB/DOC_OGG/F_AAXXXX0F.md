## Contenuto
Info sul contenuto del file.

Se è un oggetto ci sono tre possibilità

parametro obbligatorio
## Codice Oggetto (in TA/*CNTT)
 'XX'                               £FUNT1
 'YY'                               £FUNP1
## Chiave primaria
 ZZZZ                               £FUNK1
## Altri condizionamenti facoltativi in ricerca
N.A.

parametro facoltativo
## Codice Oggetto (in TA/*CNTT)
 'XX'                               £FUNT1
## Chiave primaria
 ZZZZ                               £FUNK1
## Altri condizionamenti facoltativi in ricerca
 'YY'                               £FUNP1

parametro non ammesso
## Codice Oggetto (in TA/*CNTT)
 'XX'                               £FUNT1
## Chiave primaria
 ZZZZ                               £FUNK1
## Altri condizionamenti facoltativi in ricerca
N.A.

## Ulteriore chiave primaria
Se non è un oggetto descrivere la chiave primaria
Se è un oggetto e ha l'IDOJ mettere la chiave primaria vera ad esempio C£LIST, S5IRIS

## Tabella guida
Le impostazioni che condizionano questo archivio sono contenute nel settore di tabelle xxx / yyyy)
 :  : DEC T(ST) K(xxx)

## Autorizzazioni
Classi autorizzazione per gestione e campi particolari.

## Note strutturate (Tabella NSC)
Da dove assumere il contenitore e con quale chiave.
Se ammesse presentare sempre le tre chiavi (se assente mettere N.A.)
 Chiave 1 xxxy
 Chiave 2 yyyy
 Chiave 3 N.A.

## Parametri (Tabella C£E)
Da dove assumere la categoria e con quale chiave.

## Flussi (Tabella B£H)
Definire quali flussi sono ammessi e regole di recupero del flusso (es. DO - DOOVE)

## Costruzione automatica campi (tabella B£C)
Se prevista. Descrivere anche la matrice risultante

## Presenza monitor - visualizzatore
Se presente indicare come viene recuperato e se ci sono tab. di condizionamento (es. BR1)

## Programmi di controllo
Indicare  se c'è la possibilità di lanciare programmi di controllo personali.

## /COPY
Elenco /copy e chiamate a doc. gestione es.  :  : DEC T(MB) P(QILEGEN) K(£WFB)
Inserire le copy di interrfaccia, inizializzazione, ecc..

## Gruppi flag
Da dove vengono presi i gruppi flag e se ci sono regolre di risalita (es. flag V5RDOC da V5B con risalita a V5D)

## Workflow e popup
Se l'oggetto è sottoposto a WF o se è attivabile la gestione popup B£G99

## Note particolari
Es. se sono previste impostazioni fisse (cfr. Tipo distinta = ART)

## CONTENUTO DEI CAMPI
_2_Nota In corrispondenza del campo appropriato inserire i riferimenti (es. la tabella degli stati,  valori assunti, ecc..). Inserire in questa sezione TUTTE le informazioni utili che si possono riferire ad un campo specifico, ad esempio il Livello e lo Stato.

_3_Esempi di compilazione

 :  : FLD CODCAMPO1**Livello**
a cosa è riferito (es. TA B£W_00)

 :  : FLD CODCAMPO1**Stato**
a cosa è riferito (es. TA B£W_xx) con xx in BRA

 :  : FLD CODCAMPO1**Descrizione campo**
Nota descrittiva del campo (da scrivere solo per campi particolari quando, il significato dei campi con oggettizzazione dinamica viene ritornato dal programma che decodifica la sintassi di definizione del campo stesso (cfr documentazione dell'oggetto "CS" - campo di un file)

 :  : FLD CODCAMPO2.CODCAMPO1**Descrizione campo 2**
quando il campo 2 ha le stesse caratteristiche del campo 1

 :  : FLD A§BARC Barcode
La costruzione e il controllo di questo campo sono guidati dal campo "Codice EAN" impostato in
tabella BRA.
 :  : DEC T(CS) P(T/BRA) K(T$BRAZ) R(1)
*** NOTA l'opzione R(1) sul tag  :  : DEC riporta in questo doc. la documentazione dell'oggetto (da usare
quando si cita un campo di tabella di cui si vuole includere la documentazione)
