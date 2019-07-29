## Contenuto
Dati della matricola di un oggetto.

## Codice Oggetto (in TA/*CNTT)
'MT'                          £FUNT1

## Chiave primaria
Tipo matricola      (TA/BRU)  £FUNP1
Codice matricola              £FUNK1

## Ulteriore chiave primaria
N.A.

## Altri condizionamenti facoltativi in ricerca
N.A.

## Tabella guida
Le impostazioni che condizionano questo archivio sono contenute nel settore di tabelle BRU (Tipo matricola) : 
 :  : DEC T(ST) K(BRU)

e nel settore di tabelle BRW (categoria matricole) : 
 :  : DEC T(ST) K(BRW)

## Autorizzazioni
La classe di autorizzazione è BRMT01G per la gestione delle matricole nel programma di Guida e Lista, indipendentemente dal Tipo Matricola.
La Classe BRMT01 è impostabile per Tipo Matricola ed è usata nel programma di dettaglio

## Note strutturate (Tabella NSC)
Il contenitore si aasume dalla tabella BRW (categoria matricola). Se non inserito si assume MT.
Chiave 1 - Tipo matricola
Chiave 2 - Numero matricola
Chiave 3 - N.A.

## Parametri (Tabella C£E)
La categoria si assume dalla tabella BRW.

## Flussi (Tabella B£H)
Per ogni tipo di flusso x (I : Creazione, C : Copia, A : Azioni eseguibili, ecc..) viene associato il flusso x-MTyyy, dove yyy è il tipo matricola; se assente viene associato il flusso x-MT.

## Costruzione automatica campi (tabella B£C)
 La struttura della matrice risultante quando è stata inserito in tabella BRU il campo "Strutt. costruzione" (elemento di tabella B£F)  è la seguente : 
>         Descrizione                    Riga £SC Da  A
         Codice Matricola                   1    01  15


## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
N.A.

## /COPY
Interfaccia matricola (£IMT) : 
 :  : DEC T(MB) P(QILEGEN) K(£IMT)

Inizializzazione matricola (£BRM) : 
 :  : DEC T(MB) P(QILEGEN) K(£BRM)

## Gruppi flag
Il gruppo flag si assume dalla tabella BRW.

## Workflow e popup
N.A.

## Servizio di Update
- [BRMATR0F Matricole - Servizio Update](Sorgenti/MB/DOC_OGG/P_BRMATR0F)

## Note particolari

## CONTENUTO DEI CAMPI
 :  : FLD F§TPCD_**Tipo codice**
Viene ripreso dal campo di tabella BRU.

 :  : FLD F§PACD_**Parametro codice**
Viene ripreso dal campo di tabella BRU.

 :  : FLD F§CODC_**Codice collegato**
E'un oggetto tipizzato dal tipo e parametro codice.

 :  : FLD F§SSGR **Sottosettore categoria**
Viene ripreso dal campo di tabella BRU.

 :  : FLD F§GRUP_**Categoria**
Viene proposto, in inserimento, il campo di tabella BRU.

 :  : FLD F§LIVE **Livello**
In inserimento si assume il livello di nascita dalla tabella BRU.
Se non codificato, si assume il livello 2.

 :  : FLD F§STAT **Stato**
In inserimento si deriva il primo stato valido del livello determinato.
In variazione viene controllato che lo stato sia compatibile con lo stato precedente dell'archivio.

 :  : FLD F§TIE1 **Tipo rag.sociale (1)**
Viene ripreso dal campo "Enti gestiti" di tabella BRW.
 :  : FLD F§TIE2.F§TIE1 **Tipo rag.sociale (2o 2**

 :  : FLD F§COE1 **Cod.Rag.sociale (1)**
E' un ente tipizzato dal tipo rag.sociale 1.
 :  : FLD F§COE2.F§COE1 **Cod.Rag.sociaie**

 :  : FLD F§TDO1 **Tipo docuemnto (1)**
Viene ripreso dal campo "Documenti gestiti" di tabella BRW.
 :  : FLD F§TDO2.F§TDO1 **Tipo documento (2)**
 :  : FLD F§TDO3.F§TDO1 **Tipo documento (3)**

 :  : FLD F§NDO1 **Numero documento (1)**
E' un documento tipizzato dal tipo documento 1.
 :  : FLD F§NDO2.F§NDO1 **Numero documento 2**
 :  : FLD F§NDO3.F§NDO1 **Numero documento 3**

 :  : FLD D§COD1 **Codice 1**
Campo alfanumerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella BRW.
 :  : FLD F§COD2.F§COD1 **Codice 2**
 :  : FLD F§COD3.F§COD1 **Codice 3**
 :  : FLD F§COD4.F§COD1 **Codice 4**
 :  : FLD F§COD5.F§COD1 **Codice 5**

 :  : FLD F§NUM1 **Numero 1**
Campo numerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella BRW.
 :  : FLD F§NUM2.F§NUM1 **Numero 2**
 :  : FLD F§NUM3.F§NUM1 **Numero 3**
 :  : FLD F§NUM4.F§NUM1 **Numero 4**
 :  : FLD F§NUM5.F§NUM1 **Numero 5**

 :  : FLD F§DT01 **Data 1**
Il suo significato è assunto dall'elemento XYY della tabella C£J MT, dove X è il Flag 1 dell'archivio e YY è il progressivo data (01, 02, ...).
 :  : FLD F§DT02.F§DT01 **Data 2**
 :  : FLD F§DT03.F§DT01 **Data 3**
 :  : FLD F§DT04.F§DT01 **Data 4**
 :  : FLD F§DT05.F§DT01 **Data 5**
