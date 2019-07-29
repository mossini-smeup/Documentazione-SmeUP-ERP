## Contenuto
Informazioni anagrafiche di una ubicazione.

## Codice Oggetto (in TA/*CNTT)
 'UB'                               £FUNT1

## Chiave primaria
Codice Magazzino      (TA/MAG)      £FUNP1
Codice Ubicazione     (UB)          £FUNK1

## Ulteriore chiave primaria
N.A.

## Altri condizionamenti facoltativi in ricerca
N.A.

## Tabella guida
Le impostaziooni che condizionano questo archivio sono contenute nei settore di tabelle GMU (Tipo ubicazione) : 
 :  : DEC T(ST) K(GMU)
e GMG (Tipo gestione)
 :  : DEC T(ST) K(GMG)

## Autorizzazioni
La classe di autorizzazione è GMUB01.
La funzione di autorizzazione è il magazzino.

## Note strutturate (Tabella NSC)
Il contenitore è fisso UBI : 
Chiave 1 - Codice Magazzino
Chiave 2 - Codice Ubicazione
Chiave 3 - N.A

## Parametri (Tabella C£E)
La categoria si assume dalla tabella GMU.

## Flussi (Tabella B£H)
Per ogni tipo di flusso x (I : Creazione, C : Copia, A : Azioni eseguibili, ecc..) viene associato il flusso x-UB.

## Costruzione automatica campi (tabella B£C)
La struttura della matrice risultante quando è attivata la funzione di costruzione campo (definita nel tipo  ubicazione) è la seguente : 
>Descrizione                    Riga £SC Da  A
Codice Ubicazione                  1    01  12
Descrizione Ubicazione             2    01  30
Tipo gestione                      3    01  03
Unità movimentazione               4    04  06


## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
Si può inserire in tabella GMU il suffisso x del programma di aggiustamento GMUB01_x, eseguito durante la gestione dell'anagrafica ubicazioni.

## /COPY
Interfaccia ubicazioni (£IFUBI) : 
 :  : DEC T(MB) P(QILEGEN) K(£IFUBI)

Funzioni per ubicazioni (£GMU) : 
 :  : DEC T(MB) P(QILEGEN) K(£GMU)

## Gruppi flag
I gruppi flag sono impostati in tabella GMU.

## Workflow e popup
N.A.

## Note particolari

## CONTENUTO DEI CAMPI

 :  : FLD U§LIVE **Livello**
In inserimento si assume il livello di nascita dalla tabella GMU.
Se non codificato, si assume il livello 2.

 :  : FLD U§STUB **Stato**
In inserimento si deriva il primo stato valido del livello determinato.
In variazione viene controllato che lo stato sia compatibile con lo stato precedente dell'archivio.

 :  : FLD U§COAP **Codice appartenenza**
E' tipizzato di campi di tipo e parametro inseriti in tabella GMU.

 :  : FLD U§IDOJ **Identificativo**
E' riservato per sviluppi futuri.

 :  : FLD U§ALTE **Altezza**
In inserimento è proposto il campo omonimo di tabella GMU.

 :  : FLD U§LUNG **Lunghezza**
In inserimento è proposto il campo omonimo di tabella GMU.

 :  : FLD U§LARG **Larghezza**
In inserimento è proposto il campo omonimo di tabella GMU.

 :  : FLD U§PMAX **Peso**
In inserimento è proposto il campo omonimo di tabella GMU.

 :  : FLD U§COD1 **Codice 1**
Campo alfanumerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella GMU.
 :  : FLD U§COD2.U§COD1 **Codice 2**
 :  : FLD U§COD3.U§COD1 **Codice 3**
 :  : FLD U§COD4.U§COD1 **Codice 4**
 :  : FLD U§COD5.U§COD1 **Codice 5**

 :  : FLD A§NUM1 **Numero 1**
Campo numerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella GMU.
 :  : FLD U§NUM2.U§NUM1 **Numero 2**
 :  : FLD U§NUM3.U§NUM1 **Numero 3**
 :  : FLD U§NUM4.U§NUM1 **Numero 4**
 :  : FLD U§NUM5.U§NUM1 **Numero 5**

 :  : FLD U§DT01 **Data 1**
Il suo significato è assunto dall'elemento XYY della tabella C£J UB, dove X è il campo "Tipo date implicite" di tabella GMU e YY è il progressivo data (01, 02, ...).
 :  : FLD U§DT02.U§DT01 **Data 2**
 :  : FLD U§DT03.U§DT01 **Data 3**
 :  : FLD U§DT04.U§DT01 **Data 4**
 :  : FLD U§DT05.U§DT01 **Data 5**
