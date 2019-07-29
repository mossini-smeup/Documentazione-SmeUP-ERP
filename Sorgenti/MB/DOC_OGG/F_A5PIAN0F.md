## Contenuto
Piano di ammortamento dei cespiti gestiti, definito a vari livelli di risatita.

## Codice Oggetto (in TA/*CNTT)
'A1'                               £FUNT1

## Chiave primaria
IDOJ del piano           (A5)      £FUNK1

## Altri condizionamenti facoltativi in ricerca
N.A.

## Ulteriore chiave primaria
Le chiavi dei logici 1L e 2L sono comunque primarie, essendo univoche (amche senza l'IDOJ finale).

## Tabella guida
L'oggetto che individua il livello di risalità è codificato in V2 - A5LRP : 
 :  : DEC T(MB) P(DOC_OGG) K(V2_A5LRP)  L(1)

### NOTE STRUTTURATE (Tabella NSC)
Come contenitore è assunto A1.

# Autorizzazioni
La classe di autorizzazione è A5PA01.

## Note strutturate (Tabella NSC)
Il contenitore è fisso A1.
Chiave 1 - IDOJ del movimento
Chiave 2 - N.A.
Chiave 3 - N.A.

### Parametri (Tabella C£E)
N.A.

### Flussi (Tabella B£H)
Per ogni tipo di flusso x (I : Creazione, C : Copia, A : Azioni eseguibili, ecc..) viene associato il flusso x-A1.

## Costruzione automatica campi
N.A.

## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
N.A.

## /COPY
Ritorno aliquote e quote di ammortamento (£A5C) : 
 :  : DEC T(MB) P(QILEGEN) K(£A5C)

## Gruppi flag
N.A.

## Workflow e popup
N.A.

## Note particolari

## CONTENUTO DEI CAMPI

 :  : FLD PALIVE **Livello** (TAbella B£W_00)
In inserimento si assume il livello 2.

 :  : FLD PASTAT **Stato**  (TAbella B£W_A1)
In inserimento si deriva il primo stato valido del livello determinato. In variazione viene controllato che lo stato sia compatibile con lo stato precedente dell'archivio.

 :  : FLD PAIDOJ **ID riga piano**
Si assume il numeratore OG.A1 (tabella CRN, sottosettore A5).

