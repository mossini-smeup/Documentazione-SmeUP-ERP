## Contenuto
Dati generali di una registrazione contabile.

## Codice Oggetto (in TA/*CNTT)
 'E4'                               £FUNT1
 'WK' Se è nel transito             £FUNP1

## Chiave primaria
Numero registrazione                £FUNK1

## Altri condizionamenti facoltativi in ricerca
N.A.

## Ulteriore chiave primaria
N.A.

## Tabella guida
Le impostazioni che condizionano questo archivio sono contenute in tabella Tipo registrazione : 
 :  : DEC T(ST) K(C5D)
Altre impostazioni generali sono contenute in tabella Impostazioni base Keep.Up : 
 :  : DEC T(ST) K(C51)

## Autorizzazioni
Classe 'C5E401G' per autorizzare o disautorizzare in generale.
Funzioni  'C5D'
Classe'C5E401I' per autorizzare o disautorizzare per tipo registrazione (se autorizzato in generale).
Funzioni  'C5D'

## Note strutturate (Tabella NSC)
Il contenitore si assume dal valore impostato in tabella C51 : 
 Chiave 1 'E4'
 Chiave 2 ' ' o 'WK' (se sul transito)
 Chiave 3 Cod.registrazione

## Parametri (Tabella C£E)
La categoria parametri viene assunta dal campo parametri espiciti di tabella C5D.

## Flussi (Tabella B£H)
Si attivano se è impostato il flag in tabella C51.
La B£H è x-E4 (dove x vale I/V/A ....).
La testata è l'ultima scrittura di una registrazione, quindi i suoi flussi possono modificare anche
gli altri record (righe, rate, analitica) che sono già stati scritti.

## Costruzione automatica campi (tabella B£C)
N.A.

## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
In tabella C5D è possibile impostare : 
una exit di inizializzazione
 :  : DEC T(CS) P(T/C5D) K(T$C5D5) R(1)
una exit di controllo
 :  : DEC T(CS) P(T/C5D) K(T$C5DR) R(1)

Si possono scrivere anche le seguenti exit, di nome fisso (eseguite se è  presente l'oggetto) : 
C5E401E_X (Exit per differenze cambio)
 :  : DEC T(MB) P(C5SRC) K(C5E0101E_X) R(1)
C5E401E_Y (Exit per controllo divisione)
 :  : DEC T(MB) P(C5SRC) K(C5E0101E_X) R(1)

## /COPY
Interfaccia testate registrazioni (£IE4) : 
 :  : DEC T(MB) P(QILEGEN) K(£IE4)

Gestione testate registrazioni (£C5A) : 
 :  : DEC T(MB) P(QILEGEN) K(£C5A)

## Gruppi flag
Viene assunto il gruppo flag di testata di tabella C5D.

## Workflow e popup
N.A.

## Note particolari

## CONTENUTO DEI CAMPI

 :  : FLD T5LIVE**Livello**
In inserimento si assume il livello di nascita della testata in tabella C5D.
Se assente, si assume il livello 2.

 :  : FLD T5STAT**Stato**
Il suo subsettore  è E4.
In inserimento si assume il primo stato valido del livello.
In variazione viene controllato che lo stato sia compatibile con lo stato precedente dell'archivio.

 :  : FLD T5PROG**Progressivo registrazione**
Viene utilizzato il numeratore  OG.E4 della tabella CRNC5.

 :  : FLD T5DT01 **Data 1**
Campo libero a disposizione.
 :  : FLD T5DT02.T5DT01 **Data 2**
 :  : FLD T5DT03.T5DT01 **Data 3**
 :  : FLD T5DT04.T5DT01 **Data 4**
 :  : FLD T5DT05.T5DT01 **Data 5**

 :  : FLD T5AAD1 **Codice 1**
Campo alfanumerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella C5D.
 :  : FLD T5AAD2.T5AA01 **Codice 2**
 :  : FLD T5AAD3.T5AA01 **Codice 2**
 :  : FLD T5AAD4.T5AA01 **Codice 2**
 :  : FLD T5AAD5.T5AA01 **Codice 2**

 :  : FLD T5NU01 **Numero 1**
Campo numerico tipizzato dall'elemento di parametri impliciti (C£I) inserito in tabella C5D.
 :  : FLD T5NU02.T5NU01 **Numero 2**
 :  : FLD T5NU03.T5NU01 **Numero 3**
 :  : FLD T5NU04.T5NU01 **Numero 4**
 :  : FLD T5NU05.T5NU01 **Numero 5**

