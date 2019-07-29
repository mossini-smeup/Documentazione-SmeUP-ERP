## Contenuto
In questo file sono memorizzati le attività produttive e non produttive che implicano una registrazione di tempi e/o quantità nell'ambito delle attività aziendali.

## Codice Oggetto (in TA/*CNTT)
'E2'                               £FUNT1

## Chiave primaria
Numero registrazione               £FUNK1

## Altri condizionamenti facoltativi in ricerca
N.A.

## Ulteriore chiave primaria
N.A.

## Tabella guida
Le impostazioni che condizionano questo archivio sono contenute nel settore di tabelle P5C (causali attività produttive) : 
 :  : DEC T(ST) K(P5C)

## Autorizzazioni
N.A.

## Note strutturate (Tabella NSC)
Il contenitore si assume dalla tabella P51 (Contenitore note attività) : 
 Chiave 1 - Numero registrazione
 Chiave 2 - N.A.
 Chiave 3 - N.A.

## Parametri (Tabella C£E)
N.A.

## Flussi (Tabella B£H)
Per ogni tipo di flusso x (I : Creazione, C : Copia, A : Azioni eseguibili, ecc..) viene associato il flusso x-E2yyy, dove yyy è la causale del movimento :  se assente viene associato il flusso x_E2.
NB :  il flusso per causale non è attivo per le Azioni eseguibili.

## Costruzione automatica campi (tabella B£C)
N.A.

## Presenza monitor - visualizzatore
La forma di presentazione viene assunta da quella impostata in tabella P5C.

## Programmi di controllo
Se impostato il prelievo alla fase è possibile lanciare il PGM di controllo B£G35G3_x, con x impostato nel campo "Controllo giacenza" della tab. P5C.

## /COPY
Dichiarazione Attività Produzione G35 : 
 :  : DEC T(MB) P(QILEGEN) K(£G35)

Funzioni Attività Produzione P5N : 
 :  : DEC T(MB) P(QILEGEN) K(£P5N)

Consuntivazione attività di una fase P5F : 
 :  : DEC T(MB) P(QILEGEN) K(£P5F)

## Gruppi flag
Il gruppo flag viene assunto dalla tabella P5C.

## Workflow e popup
N.A.

## Note particolari

## CONTENUTO DEI CAMPI
 :  : FLD W§NURE**Numero Registrazione**
Si assume il numeratore definito nella tabella di personalizzazione P51.

 :  : FLD W§STAT**Stato**
Campo riservato a sviluppi futuri.

 :  : FLD W§LIVE**Livello**
Campo riservato a sviluppi futuri.

 :  : FLD W§COD1**Codice**
Campo alfanumerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella P5C.
 :  : FLD W§COD2.W§COD1**Codice 2**
 :  : FLD W§COD3.W§COD1**Codice 3**
 :  : FLD W§COD4.W§COD1**Codice 4**
 :  : FLD W§COD5.W§COD1**Codice 5**

 :  : FLD W§NUM1**Campo numerico**
Campo alfanumerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella P5C.
 :  : FLD W§NUM2.W§NUM1**Campo numerico 2**
 :  : FLD W§NUM3.W§NUM1**Campo numerico 3**
 :  : FLD W§NUM4.W§NUM1**Campo numerico 4**
 :  : FLD W§NUM5.W§NUM1**Campo numerico 5**
