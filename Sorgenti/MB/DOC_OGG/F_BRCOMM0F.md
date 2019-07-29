## Contenuto
Informazioni di quantità, date e classificazioni delle commesse.

## Codice Oggetto (in TA/*CNTT)
'CM'                               £FUNT1

## Chiave primaria
Codice commessa          (CM)      £FUNK1

## Altri condizionamenti facoltativi in ricerca
Tipo commessa            (TA/BSA)  £FUNP1

## Ulteriore chiave primaria
N.A.

## Tabella guida
Le impostaziooni che condizionano questo archivio sono contenute nel settore di tabelle BSA (Tipo commessa).

## Autorizzazioni
La classe di autorizzazione è BRCM01.

La funzione di autorizzazione è il tipo commessa (tabella BSA) : 

## Note strutturate (Tabella NSC)
Il contenitore si assume dalla tabella BSA (tipo commessa). Se non inserito si assume CM.
Chiave 1 - Codice Commessa
Chiave 2 - N.A.
Chiave 3 - N.A.

## Parametri (Tabella C£E)
La categoria si assume dalla tabella BSA (tipo commessa).

## Flussi (Tabella B£H)
Per ogni tipo di flusso x (I : Creazione, C : Copia, A : Azioni eseguibili, ecc..) viene associato il flusso x-CMyyy, dove yyy è il tipo commessa; se assente viene associato il flusso x-CM.

## Costruzione automatica campi (tabella B£C)
 La struttura della matrice risultante quando è stata inserito in tabella BSA il campo "Domande cost. codice" (elemento di tabella B£F)  è la seguente : 
>         Descrizione                    Riga £SC Da  A
         Codice  Commessa                   1    01  10
         Descrizione Commessa               2    01  35
         Commessa Riferimento               2    36  45
         Codice Magazzino                   2    46  48
         Priorità                           2    49  50
         Descrizione Aggiuntiva             2    51  85
         Codice Responsabile                3    01  15
         Cod.Compet.Gestione                3    16  31
         Ente                               3    32  48


## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
In tabella BSA si può inserire il suffisso del programma di aggiustamento  BRCM01D_x.

## /COPY
Interfaccia commessa (£ICM) : 
 :  : DEC T(MB) P(QILEGEN) K(£ICM)

Inizializzazione commessa (£BRY) : 
 :  : DEC T(MB) P(QILEGEN) K(£BRY)

Calcolo date commessa (£BRK) : 
 :  : DEC T(MB) P(QILEGEN) K(£BRK)

Calcolo quantità commessa (£BRQ) : 
 :  : DEC T(MB) P(QILEGEN) K(£BRQ)

## Gruppi flag
I gruppi flag sono presenti nel tipo commessa Tab. BSA.

## Workflow e popup
N.A.

## Servizio di Update
- [BRCOMM0F Anagrafica commesse - Servizio Update](Sorgenti/MB/DOC_OGG/P_BRCOMM0F)

## Note particolari

## CONTENUTO DEI CAMPI

 :  : FLD M$LIVE **Livello**
In inserimento si assume il livello di nascita dalla tabella BSA.
Se non codificato, si assume il livello 2.

 :  : FLD M$STAT **Stato**
In inserimento si deriva il primo stato valido del livello determinato.
In variazione viene controllato che lo stato sia compatibile con lo stato precedente dell'archivio.

 :  : FLD M$COMM **Codice commessa**
Si assume il numeratore (tabella CRN, sottosettore CM) definito nella tabella BSA (tipo commessa).

 :  : FLD M$NACM **Natura commessa**
Si assume il valore impostato nel tipo commessa.

 :  : FLD M$PRIO h_Priorità
Si assume il valore impostato nel tipo commessa.

 :  : FLD M$TIRF h_Tipo oggetto riferimento
Si assume il valore impostato nel tipo commessa, nel campo tipo oggetto intestatario.

 :  : FLD M$PAOG h_Parametro oggetto riferimento
Si assume il valore impostato nel tipo commessa, nel campo tipo oggetto intestatario.

 :  : FLD M$CDOG h_Codice oggetto riferimento
E'l'oggetto tipizzato da tipo e parametro omonimi.

 :  : FLD M$TIRE h_Tipo oggetto responsabile
Si assume il valore impostato nel tipo commessa, nel campo omonimo.

 :  : FLD M$PARE h_Parametro oggetto responsabile
Si assume il valore impostato nel tipo commessa, nel campo omonimo.

 :  : FLD M$CDRE h_Codice oggetto responsabile
E'l'oggetto tipizzato da tipo e parametro omonimi.

 :  : FLD M$TICG h_Tipo oggetto competenza gestione
Si assume il valore impostato nel tipo commessa, nel campo omonimo.

 :  : FLD M$PACG h_Parametro oggetto competenza gestione
Si assume il valore impostato nel tipo commessa, nel campo omonimo.

 :  : FLD M$CDCG h_Codice oggetto competenza gestione
E'l'oggetto tipizzato da tipo e parametro omonimi.

 :  : FLD M$TIEN h_Tipo Ente
Si assume il valore impostato nel tipo commessa, nel campo omonimo.

 :  : FLD M$COEN h_Codice ente
E'l'ente tipizzato dal tipo ente.

 :  : FLD M$DT01 **Data 1**
Il suo significato è assunto dall'elemento XYY della tabella C£J CM, dove X è il secondo flag dell'archivio è il progressivo data (01, 02, ...).
 :  : FLD M$DT02.M$DT01 **Data 2**
 :  : FLD M$DT03.M$DT01 **Data 3**
 :  : FLD M$DT04.M$DT01 **Data 4**
 :  : FLD M$DT05.M$DT01 **Data 5**
 :  : FLD M$DT06.M$DT01 **Data 6**
 :  : FLD M$DT07.M$DT01 **Data 7**
 :  : FLD M$DT08.M$DT01 **Data 8**
 :  : FLD M$DT09.M$DT01 **Data 9**
 :  : FLD M$DT10.M$DT01 **Data 10**

 :  : FLD M$QI01 **Qtà/Importo 1**
Campo numerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella BSA.
 :  : FLD M$QI02.M$QI01 **Qtà/Importo 2**
 :  : FLD M$QI03.M$QI01 **Qtà/Importo 2**
 :  : FLD M$QI04.M$QI01 **Qtà/Importo 3**
 :  : FLD M$QI05.M$QI01 **Qtà/Importo 4**
 :  : FLD M$QI06.M$QI01 **Qtà/Importo 5**
 :  : FLD M$QI07.M$QI01 **Qtà/Importo 6**
 :  : FLD M$QI08.M$QI01 **Qtà/Importo 7**
 :  : FLD M$QI09.M$QI01 **Qtà/Importo 8**
 :  : FLD M$QI10.M$QI01 **Qtà/Importo 9**

 :  : FLD M$COD1 **Codice 1**
Campo alfanumerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella BRA.
 :  : FLD M$COD2.M$COD1 **Codice 2**
 :  : FLD M$COD3.M$COD1 **Codice 3**
 :  : FLD M$COD4.M$COD1 **Codice 4**
 :  : FLD M$COD5.M$COD1 **Codice 5**
