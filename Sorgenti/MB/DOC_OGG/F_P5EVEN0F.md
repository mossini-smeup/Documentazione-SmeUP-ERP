## Contenuto
Contiene tutti gli eventi, sia di produzione che relativi ad altre funzioni aziendali di cui si vuole tenere una registrazione.

## Codice Oggetto (in TA/*CNTT)
 'E3'                               £FUNT1
 N§TEVE 'Tipo evento'   £FUNP1

## Chiave primaria
N§NREV     Numero reg. evento    £FUNK1

## Altri condizionamenti facoltativi in ricerca
N.A.

## Tabella guida
Le impostazioni che condizionano questo archivio sono contenute nella tabella tipo evento P5D e nella tabella categoria evento P5F : 
 :  : DEC T(ST) K(P5D)
 :  : DEC T(ST) K(P5F)

## Autorizzazioni
La classe di autorizzazione è P5EV01 con funzione = Tipo evento (P5D).

## Note strutturate (Tabella NSC)
Il contenitore si assume dalla tabella P5D (parametri gestione produzione), il campo è T$P5DJ (Contenitore note).
Se non inserito si assume il contenitore dalla tabella P51 (parametri gestione produzione) :  il campo è T$P51M (Conten.note eventi). Se non inserito si assume EV.
 Chiave 1 TA - P5D
 Chiave 2 E3
 Chiave 3 N.A.

## Parametri (Tabella C£E)
La categoria parametri si assume dalla tabella P5F.

## Flussi (Tabella B£H)
Per ogni tipo di flusso x (I : Creazione, C : Copia, A : Azioni eseguibili, ecc..) viene associato il flusso x-E3yyy, dove yyy è il tipo evento; se assente viene associato il flusso x-E3.

## Costruzione automatica campi (tabella B£C)
N.A.

## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
N.A.

## /COPY
Interfaccia generalizzata Eventi IE3 : 
 :  : DEC T(MB) P(QILEGEN) K(£IE3)

Inizializzazione eventi  P5E : 
 :  : DEC T(MB) P(QILEGEN) K(£P5E)

## Gruppi flag
N.A.

## Workflow e popup
Non è prevista la gestione popup B£G99.

## Note particolari

## CONTENUTO DEI CAMPI
 :  : FLD N§NREV**Numero reg. evento**
Il numeratore si assume dalla tabella P51 (parametri gestione produzione).
 :  : FLD N§LIVE**Livello**
TA B£W_00
 :  : FLD N§STAT**        Stato evento**
TA B£W_xx con xx in P5D, se non inserito si assume EV.
 :  : FLD N§COD1**Codice Oggetto**
Campo alfanumerico tipizzato dall'elemento della griglia 1 (B£G) inserito in tabella P5F.
 :  : FLD N§COD2.N§COD1**Codice Oggetto2**
 :  : FLD N§COD3.N§COD1**Codice Oggetto2**
 :  : FLD N§COD4**Codice Oggetto4**
Campo alfanumerico tipizzato dall'elemento della griglia 2 (B£G) inserito in tabella P5F.
 :  : FLD N§COD5.N§COD4**Codice Oggetto5**
 :  : FLD N§COD6.N§COD4**Codice Oggetto6**
 :  : FLD N§ALF1**Campo alfanumerico**
Campo alfanumerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella P5F.
 :  : FLD N§ALF2.N§ALF1**Campo alfanumerico 2**
 :  : FLD N§ALF3.N§ALF1**Campo alfanumerico 3**
 :  : FLD N§ALF4.N§ALF1**Campo alfanumerico 4**
 :  : FLD N§ALF5.N§ALF1**Campo alfanumerico 5**
 :  : FLD N§NUM1**Campo numerico**
Campo alfanumerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella P5F.
 :  : FLD N§NUM2.N§NUM1**Campo numerico 2**
 :  : FLD N§NUM3.N§NUM1**Campo numerico 3**
 :  : FLD N§NUM4.N§NUM1**Campo numerico 4**
 :  : FLD N§NUM5.N§NUM1**Campo numerico 5**
