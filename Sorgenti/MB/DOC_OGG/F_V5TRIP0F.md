## Contenuto
Informazioni di un viaggio.

## Codice Oggetto (in TA/*CNTT)
'VG'                               £FUNT1

## Chiave primaria
Codice viaggio      (VG)      £FUNK1

## Altri condizionamenti facoltativi in ricerca
Tipo viaggio             (TA/V5T)  £FUNP1

## Ulteriore chiave primaria
N.A.

## Tabella guida
Le impostazioni che condizionano questo archivio sono contenute nel settore di tabelle V5T) : 
 :  : DEC T(ST) K(V5T)

## Autorizzazioni
La classe di autorizzazione è V5TR01, la funzione è V5TR01G per il formato guida, V5TR01L per la lista.

## Note strutturate (Tabella NSC)
Il contenitore si assume dalla tabella V5T (tipo viaggio). Se non inserito si assume VG.
Chiave 1 - Codice Viaggio
Chiave 2 - N.A.
Chiave 3 - N.A.

## Parametri (Tabella C£E)
La categoria si assume dalla tabella V5T (tipo viaggio). Se non impostata non si gestiscono i parametri.

## Flussi (Tabella B£H)
Per ogni tipo di flusso x (I : Creazione, C : Copia, A : Azioni eseguibili, ecc..) viene associato il flusso x-VGyyy, dove yyy è il tipo viaggio; se assente viene associato il flusso x-VG.

## Costruzione automatica campi (tabella B£C)
N.A.

## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
In tab. V5T è possibile indicare un programma di controllo specifico.

## /COPY
Inizializzatore viaggio (£V6A) : 
 :  : DEC T(MB) P(QILEGEN) K(£V6A)

## Gruppi flag
Il gruppo flag viene assunto dalla tabella V5T (tipo viaggio).

## Workflow e popup
N.A.

## Note particolari
N.A.

## CONTENUTO DEI CAMPI

 :  : FLD V$CDVG **Codice viaggio**
Si assume il numeratore definito in tabella V5T (tipo viaggio), (tabella CRN, sottosettore VG).

 :  : FLD V$LIVE **Livello**
In inserimento si assume il livello di nascita dalla tabella V5T.
Se non codificato, si assume il livello 2.

 :  : FLD V$STAT **Stato**
In inserimento si deriva il primo stato valido del livello determinato.
In variazione viene controllato che lo stato sia compatibile con lo stato precedente dell'archivio.

 :  : FLD V$PER1 **Tappa 1**
Nel tipo viaggio (Tab. V5T) può essere definito un elemento di C£I nel campo "Percorsi", che definisce le cinque tappe di un percorso.

 :  : FLD V$PER2.V$PER1 **Tappa 2**
 :  : FLD V$PER3.V$PER1 **Tappa 3**
 :  : FLD V$PER4.V$PER1 **Tappa 4**
 :  : FLD V$PER5.V$PER1 **Tappa 5**

 :  : FLD V$DT01 **Data 1**
Si possono trattare fino a 10 date definite nel sottosettore 'VG' della tabella C£J. I significati sono dati dagli elementi 'Xyy' dove X è il secondo flag dell'archivio e yy va da 01 a 10. L'elemento 'X  ' dà il significato al titolo del gruppo date. Se il secondo flag non è impostato non si gestiscono le date interne.
 :  : FLD V$DT02.V$DT01 **Data 2**
 :  : FLD V$DT03.V$DT01 **Data 2**
 :  : FLD V$DT04.V$DT01 **Data 2**
 :  : FLD V$DT05.V$DT01 **Data 2**
 :  : FLD V$DT06.V$DT01 **Data 2**
 :  : FLD V$DT07.V$DT01 **Data 2**
 :  : FLD V$DT08.V$DT01 **Data 2**
 :  : FLD V$DT09.V$DT01 **Data 2**
 :  : FLD V$DT10.V$DT01 **Data 2**

 :  : FLD V$QI01 **Quantità 1**
Si possono trattare fino a 10 numeri (Qtà/Valori) definiti nel sottosettore 'VG' della tabella C£H. I significati sono dati dagli elementi 'Xyy' dove X è il primo flag dell'archivio e yy va da 01 a 10.
L'elemento 'X  ' dà il significato al titolo del gruppo valori. Se il primo flag non è impostato non si gestiscono i numeri interni.
 :  : FLD V$QI02.V$QI01 **Quantità 2**
 :  : FLD V$QI03.V$QI01 **Quantità 3**
 :  : FLD V$QI04.V$QI01 **Quantità 4**
 :  : FLD V$QI05.V$QI01 **Quantità 5**
 :  : FLD V$QI06.V$QI01 **Quantità 6**
 :  : FLD V$QI07.V$QI01 **Quantità 7**
 :  : FLD V$QI08.V$QI01 **Quantità 8**
 :  : FLD V$QI09.V$QI01 **Quantità 9**
 :  : FLD V$QI10.V$QI01 **Quantità 10**

 :  : FLD V$COD1 **Codice 1**
Campo alfanumerico tipizzato dall'elemento di parametri impliciti (C£I) imserito in tabella V5T.
 :  : FLD V$COD2.V$COD1 **Codice 2**
 :  : FLD V$COD3.V$COD1 **Codice 3**
 :  : FLD V$COD4.V$COD1 **Codice 4**
 :  : FLD V$COD5.V$COD1 **Codice 5**

 :  : FLD V$NUM1 **Numero 1**
Campo numerico tipizzato dall'elemento di parametri impliciti (C£I) imserito in tabella V5T.
 :  : FLD V$NUM2.V$NUM1 **Numero 2**
 :  : FLD V$NUM3.V$NUM1 **Numero 3**
 :  : FLD V$NUM4.V$NUM1 **Numero 4**
 :  : FLD V$NUM5.V$NUM1 **Numero 5**
