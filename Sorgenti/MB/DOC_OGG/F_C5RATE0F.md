## Contenuto
Rata di pagamento (dovuto o pagato).

## Codice Oggetto (in TA/*CNTT)
 'RR'                               £FUNT1
 'WK' Se è nel transito             £FUNP1

## Chiave primaria
ID Rata                             £FUNK1

## Altri condizionamenti facoltativi in ricerca
N.A.

## Ulteriore chiave primaria
N.A.

## Tabella guida
Le impostazioni che condizionano questo archivio sono contenute in tabella Tipo Rata : 
 :  : DEC T(ST) K(C5E)
Altre impostazioni generali sono contenute in tabella Impostazioni Base Pagamenti e Incassi : 
 :  : DEC T(ST) K(C53)

## Autorizzazioni
La classe è 'C5RR01'.

## Note strutturate (Tabella NSC)
Il contenitore si imposta in tabella C51 : 
 Chiave 1 'RR'
 Chiave 2 ' ' WK (se è nel transito)
 Chiave 3 CIDOPJ

## Parametri (Tabella C£E)
La categoria parametri viene assunta dal campo parametri espiciti di tabella C5E.

## Flussi (Tabella B£H)
Si attivano se è impostato il flag in tabella C51.
La B£H è x-RR (I C....).

## Costruzione automatica campi (tabella B£C)
N.A.

## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
In tabella C5E è possibile impostare una exit di inizializzazione : 
 :  : DEC T(CS) P(T/C5D) K(T$C5EH) R(1)

## /COPY
Interfaccia rate (£IRR) : 
 :  : DEC T(MB) P(QILEGEN) K(£IRR)

Gestione rate (£C5C) : 
 :  : DEC T(MB) P(QILEGEN) K(£C5C)

## Gruppi flag
Viene assunto il gruppo flag di riga di tabella C5E.

## Workflow e popup
N.A.

## Note particolari

## CONTENUTO DEI CAMPI

 :  : FLD S5LIVE**Livello**
In inserimento si assume il livello di nascita della riga in tabella C5E.
Se assente, si assume il livello 2.

 :  : FLD S5STAT**Stato**
Il suo subsettore  è RR.
In inserimento si assume il primo stato valido del livello.
In variazione viene controllato che lo stato sia compatibile con lo stato precedente dell'archivio.

 :  : FLD S5IDOJ**ID Rata**
Viene assunto il numeratore  OG.RR  di tabella CRNC5.

 :  : FLD S5DT01 **Data 1**
E' a dispisioznie e non è tipizzata
 :  : FLD S5DT02.S5DT01 **Data 2**
 :  : FLD S5DT03.S5DT01 **Data 3**
 :  : FLD S5DT04.S5DT01 **Data 4**
 :  : FLD S5DT05.S5DT01 **Data 5**

 :  : FLD S5AAD1 **Codice 1**
Campo alfanumerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella C5E.
 :  : FLD S5AA02.S5AA01 **Codice 2**
 :  : FLD S5AA03.S5AA01 **Codice 3**
 :  : FLD S5AA04.S5AA01 **Codice 4**
 :  : FLD S5AA05.S5AA01 **Codice 5**

 :  : FLD S5NU01 **Numero 1**
Campo numerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella C5E.
 :  : FLD S5NU02.S5NU01 **Numero 2**
 :  : FLD S5NU03.S5NU01 **Numero 3**
 :  : FLD S5NU04.S5NU01 **Numero 4**
 :  : FLD S5NU05.S5NU01 **Numero 5**

