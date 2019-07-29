## Contenuto
Solleciti a fronte di una rata.

## Codice Oggetto (in TA/*CNTT)
 'C3'                               £FUNT1

## Chiave primaria
ID ID sollecito                     £FUNK1

## Altri condizionamenti facoltativi in ricerca
N.A.

## Ulteriore chiave primaria
N.A.

## Tabella guida
Le impostazioni che condizionano questo archivio sono contenute nel tipo sollecito : 
 :  : DEC T(ST) K(C5X)
Altre impostazioni generali sono contenute in tabella Impostazioni Base Pagamenti e Incassi : 
 :  : DEC T(ST) K(C53)

## Autorizzazioni
N.A.

## Note strutturate (Tabella NSC)
Il contenitoìre si assume da tabella C51 : 
 Chiave 1 'C3'
 Chiave 2  ' '
 Chiave 3 ID Sollecito

## Parametri (Tabella C£E)
N.A.

## Flussi (Tabella B£H)
Si attivano se è impostato il flag in tabella C51.
Sono per x-C3 (I C....).

## Costruzione automatica campi (tabella B£C)
N.A.

## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
In tabella C5E è possibile impostare una exit di inizializzazione : 
 :  : DEC T(CS) P(T/C5D) K(T$C5EH) R(1)

## /COPY
Interfaccia rate (£IC3) : 
 :  : DEC T(MB) P(QILEGEN) K(£IRR)

Gestione solleciti (£C5S) : 
 :  : DEC T(MB) P(QILEGEN) K(£C5S)

ESTRAZIONE SOLLleciti (£C5H) : 
 :  : DEC T(MB) P(QILEGEN) K(£C5H)

## Gruppi flag
N.A.

## Workflow e popup
N.A.

## Note particolari

## CONTENUTO DEI CAMPI

 :  : FLD L5LIVE**Livello**
In inserimento si assume il livello di nascita della riga in tabella C5X.
Se assente, si assume il livello 2.

 :  : FLD L5STAT**Stato**
Il suo subsettore  è C3.
In inserimento si assume il primo stato valido del livello.
In variazione viene controllato che lo stato sia compatibile con lo stato precedente dell'archivio.

 :  : FLD L5IDOJ**ID Sollecito**
Viene assunto il numeratore  OG.C3 di tabella CRNC5.

 :  : FLD S5DT01 **Data 1**
E' a dispisioznie e non è tipizzata.
 :  : FLD L5DT02.L5DT01 **Data 2**
 :  : FLD L5DT03.L5DT01 **Data 3**
 :  : FLD L5DT04.L5DT01 **Data 4**
 :  : FLD L5DT05.L5DT01 **Data 5**

 :  : FLD L5AAD1 **Codice 1**
Liberi
 :  : FLD L5AA02.L5AA01 **Codice 2**
 :  : FLD L5AA03.L5AA01 **Codice 3**
 :  : FLD L5AA04.L5AA01 **Codice 4**
 :  : FLD L5AA05.L5AA01 **Codice 5**

 :  : FLD L5NU01 **Numero 1**
Liberi
 :  : FLD L5NU02.L5NU01 **Numero 2**
 :  : FLD L5NU03.L5NU01 **Numero 3**
 :  : FLD L5NU04.L5NU01 **Numero 4**
 :  : FLD L5NU05.L5NU01 **Numero 5**

