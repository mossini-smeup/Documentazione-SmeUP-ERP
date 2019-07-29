# TABEL00F  Tabelle
## Contenuto
Informazioni relative alle tabelle :  oggetti di impostazione delle applicazioni, con attributi variabili.
Legenda
xxx :  settore della tabella
yy :   subsettore della tabella

## Codice Oggetto (in TA/*CNTT)
'TA'                               £FUNT1
xxxyy                              £FUNP1

## Chiave primaria
Elemento                           £FUNK1

## Altri condizionamenti facoltativi in ricerca
N.A.


## Ulteriore chiave primaria
N.A.

## Tabella guida
N.A.

## Autorizzazioni
Autorizzazioni gestione tabelle,  Classe = RITSM, Funzione = settore.

## Note strutturate (Tabella NSC)
Il contenitore è B£E
Chiave 1  :  Settore
Chiave 2  :  Subsettore
Chiave 3  :  Elemento

## Parametri (Tabella C£E)
Si assume la categoria xxx (settore di tabella), se presente.
Chiave 1  :  Settore
Chiave 1  :  Settore

## Flussi (Tabella B£H)
Per ogni tipo di flusso f (I : Creazione, C : Copia, A : Azioni eseguibili, ecc..) viene associato il flusso f-TAxxxyy, se presente; se assente viene associato il flusso f-TAxxx; se assente non viene associato alcun flusso.

## Costruzione automatica campi (tabella B£C)
N.A.

## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
Se presente, viene eseguito in controllo, il programma specifico  B£Txxx.
Il campo libero utente (TTUSER) viene controllato con il programma specifico B£Txxx_U (se presente).

## /COPY
Interfaccia tabelle (£RITES) : 
 :  : DEC T(MB) P(QILEGEN) K(£RITES)

## Gruppi flag
N.A.

## Workflow e popup
N.A.

## Note particolari
Normalmente il file tabelle è il TABEL00F. Quando si vogliano applicazioni multiambiente con una parte di tabelle specifiche per ambiente ed altre comuni si utlilizza una opzione multifile simile a quella prevista per i parametri :  avremo un file (es. TABEL00F) specifico ed un file (es. TABELG0F) comune. Nella definizione tabella si specifica il file di appartenenza.

I seguenti file sono riservati : 
- Il file TABELA0F è riservato alle azioni dei menù Smeup (settori MEA).
- Il file TABELV0F è riservato ai valori fissi Smeup ("V1").

## CONTENUTO DEI CAMPI
