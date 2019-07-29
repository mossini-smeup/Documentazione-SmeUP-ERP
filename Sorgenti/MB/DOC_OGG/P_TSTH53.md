# OBIETTIVO

Tramite questa /COPY è possibile semplificare la scrittura dei file PDF che vengono prodotti tramite la £G53. In sostanza, viene scissa la definizione della struttura del PDF (Righe, Intestazioni, Riquadri ecc.) che viene delegata a degli script, dalla valorizzazione dei quali viene riempita la struttura stessa. Il programma deve perciò occuparsi solo di quest'ultima parte e dell'utilizzo

# PREREQUISITI

D/COPY QILEGEN,£H53D
C/COPY QILEGEN,£H53

# NOTE AGGIUNTIVE

Gli script di definizione si trovano nel file SCP_G53. Per una loro maggiore comprensione si rimanda alla scheda di test raggiungibile dal programma di TST tramite  l'apposito tasto.

Per effettuare dei test sulla funzioine è inoltre possibile attivare dall'elemento B£H53G della tabella PGM la stampa LOG per vedere in stampa il risultato dell'output della B£H53G.

# PARAMETRI

## FUNZIONI/METODI


- INZ      Inizializzazione
-- XML :  Prepara inizio XML (CDATA)
-- SCP :  Apre lo SCRIPT indicato
--- $H53_STRIN :  Nam="NOMESCRIPT"
-- PDF :  Prepara inizio XML ed apre script indicato (INZ.XML + INZ.SCP)
-- INV :  Formato .INV :  rispetto al metodo precedente l'immagine azienda non viene ricercata  nelle directory di loocup, ma sull'AS in '/SMEDOC/IMG/AZ/CodiceAzienda.jpg
-- AOP :  Apertura documento XML in formato Medusa
- NEW      Creazione
-- PAG :  Inizializza una nuova pagina (Header, etc.)
--- $H53_STRIN :  Nam="NOMEPAGINA"
-- RIG :  scrive una nuova riga
--- $H53_STRIN :  Nam="NOMERIGA" Txt="VALORI|DA|INSERIRE|NELLE|COLONNE"
-- BDY :  Crea un salto pagina
-- MOD :  Crea un Modello (solo AOP)
- CLO      Chiusura :  completa la scrittura del file .INV
-- PAG :  Chiude una pagina (Footer, etc.)
-- XML :  Prepara Setup e chiude XML
-- PDF :  Chiude pagina, prepara Setup e chiude XML (CLO.PAG + CLO.XML)
- SER      Funzioni di servizio (restituzione di un XML)
--  MEM     Visualizzazione completa
--  SCP     Script
- ASS      Funzioni di assegnazione
--  VAR     Variabili :  permettere di assegnare il valore di una variabile indicata nello script
--- $H53_STRIN :  Nam="NOMEVAR" Txt="VALOREVAR"
--  UIB     Variabili da £UIBDS :  permette di assegnare le variabili della £UIBDS. Nel campo di input dovrà essere appunto passata tale DS
--  STY     Stili :  permette di assegnare/sovrascrivere la configurazione di uno stile indicato nello script
--- $H53_STRIN :  Nam="NOMESTILE"
- AOP Estensione AOP
-- INV :  Invio file a Medusa


## PARAMETRI DI INPUT


- Numero pagina :  Numero della prima pagina del pdf _campo £H53NPA _
- Lunghezza Record  :  Lunghezza del record della riga del PDF _campo £H53RL _
- Presenza footer  :  Presenza del footer nella stampa del PDF  _campo £H53NF_
- Stringa di input :  Stringa di input del PDF _campo £H53_STRIN _


## PARAMETRI DI OUTPUT


- Stringa di output :  _Campo £H53_STROU_


## ESEMPIO DI CHIAMATA

- Inizializzazione
>     C                   CLEAR                   £H53_DS
     C                   EVAL      £H53_FUN='INZ'
     C                   EVAL      £H53_MET='PDF'
     C                   EVAL      £H53_AMB=XG18AM
     C                   EVAL      £H53_STRIN='Nam="NomeScriptSCP_G53"'
     C                   EXSR      H53_EMI
     C                   EXSR      £H53
2    C                   IF        £H53_STROU<>' '
      * [...] Istruzioni per scrivere £H53_STROU nell'IFS (es. tramite G80)
2E   C                   ENDIF
 :  : PAR : END
- Scrittura delle variabili di intestazione
>     C                   EVAL      £H53_FUN='ASS'
     C                   EVAL      £H53_MET='VAR'
     C                   EVAL      £H53_STRIN='Nam="Nomevariabile" '
     C                             +'Txt="ValoreVariabile"'
     C                   EXSR      £H53

- Scrittura di una nuova riga
>     C                   EVAL      £H53_FUN='NEW'
     C                   EVAL      £H53_MET='RIG'
     C                   EVAL      £H53_STRIN='Nam="NomeStile" '
     C                             +'Txt="TestoRiga"'
     C                   EXSR      £H53
2    C                   IF        £H53_STROU<>' '
      * [...] Istruzioni per scrivere £H53_STROU nell'IFS (es. tramite G80)
     C                   ENDIF

- Test Salto Pagina (solo se voglio modificare la pagina, altrimenti la nuova pagina  viene scritta automaticamente
>     C                   IF        £H53_MES='OVF'
     C                   ENDIF

- Chiusura
>     C                   EVAL      £H53_FUN='CLO'
     C                   EVAL      £H53_MET='   '
     C                   EXSR      £H53
2    C                   IF        £H53_STROU<>' '
      * [...] Istruzioni per scrivere £H53_STROU nell'IFS (es. tramite G80)
     C                   ENDIF

