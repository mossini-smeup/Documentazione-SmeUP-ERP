## Contenuto
Singola riga di una registrazione contabile.

## Codice Oggetto (in TA/*CNTT)
 'E5'                               £FUNT1
 'WK' Se è nel transito             £FUNP1

## Chiave primaria
Numero registrazione  (1-10)        £FUNK1
Numero riga           (11-15        £FUNK1

## Altri condizionamenti facoltativi in ricerca
N.A.

## Ulteriore chiave primaria
N.A.

## Tabella guida
Le impostazioni che condizionano questo archivio sono contenute in tabella Causale contabile : 
 :  : DEC T(ST) K(C5V)
Altre impostazioni generali sono contenute in tabella Impostazioni base Keep.Up : 
 :  : DEC T(ST) K(C51)
e nella tabella Tipo registrazione : 
 :  : DEC T(ST) K(C5D)

## Autorizzazioni
N.A.
Si autorizza l'intera registrazione (vedi testata).

## Note strutturate (Tabella NSC)
Il contenitore si assume da tabella C51 : 
 Chiave 1 'E5'
 Chiave 2 ' ' o 'WK' (se è nel transito)
 Chiave 3 Cod.regstrazione + Numero riga

## Parametri (Tabella C£E)
N.A.

## Flussi (Tabella B£H)
Si attivano se è impostato il flag in tabella C51.
La B£H è x-E5 (dove x vale I/V/A ...).

## Costruzione automatica campi (tabella B£C)
N.A.

## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
In tabella C5D è possibile impostare : 
una exit di inizializzazione righe
 :  : DEC T(CS) P(T/C5D) K(T$C5DT) R(1)
una exit di controllo
 :  : DEC T(CS) P(T/C5D) K(T$C5D5) R(1)

## /COPY
Interfaccia righe registrazioni (£IE5) : 
 :  : DEC T(MB) P(QILEGEN) K(£IE5)

Gestione righe registrazioni (£C5B) : 
 :  : DEC T(MB) P(QILEGEN) K(£C5B)

## Gruppi flag
Viene assunto il gruppo flag di riga di tabella C5D.

## Workflow e popup
N.A.

## Note particolari

## CONTENUTO DEI CAMPI

 :  : FLD R5LIVE**Livello**
In inserimento si assume il livello di nascita della riga in tabella C5D.
Se assente, si assume il livello 2.

 :  : FLD R5STAT**Stato**
Il suo subsettore  è E5.
In inserimento si assume il primo stato valido del livello.
In variazione viene controllato che lo stato sia compatibile con lo stato precedente dell'archivio.

 :  : FLD R5SOCI**Società Intercompany**
Informazione legata all'anagrafico (estensione £33).
Non modificabile.

 :  : FLD R5SOCO**Società Origine**
Usato solo in caso di gestione del consolidato e solo per l'AZIENDA AGGREGATO.

 :  : FLD R5RIGA**Riga registrazione**
Viene assunto il passo righe registrazioni contabili di tabella C51.
 :  : DEC T(CS) P(T/C5D) K(T$C51D) R(1)

 :  : FLD R5DT01 **Data 1**
Campo libero a disposizione.
 :  : FLD R5DT02.R5DT01 **Data 2**
 :  : FLD R5DT03.R5DT01 **Data 3**
 :  : FLD R5DT04.R5DT01 **Data 4**
 :  : FLD R5DT05.R5DT01 **Data 5**

 :  : FLD R5AAD1 **Codice 1**
Campo alfanumerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella C5D.
 :  : FLD R5AA02.R5AA01 **Codice 2**
 :  : FLD R5AA03.R5AA01 **Codice 2**
 :  : FLD R5AA04.R5AA01 **Codice 2**
 :  : FLD R5AA05.R5AA01 **Codice 2**

 :  : FLD R5NU01 **Numero 1**
Campo numerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella C5D.
 :  : FLD R5NU02.R5NU01 **Numero 2**
 :  : FLD R5NU03.R5NU01 **Numero 3**
 :  : FLD R5NU04.R5NU01 **Numero 4**
 :  : FLD R5NU05.R5NU01 **Numero 5**

