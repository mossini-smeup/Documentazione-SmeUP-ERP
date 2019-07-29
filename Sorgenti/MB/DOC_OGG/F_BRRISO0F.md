## Contenuto
Dati descrittivi e classificazioni risorse/centri di lavoro.

## Codice Oggetto (in TA/*CNTT)
 'RI'                                  	£FUNT1
Tipo risorsa                  (TA/BRR)  	£FUNP1

## Chiave primaria
Codice risorsa              (RI)   	£FUNK1

## Altri condizionamenti facoltativi in ricerca

## Ulteriore chiave primaria
N.A.

## Tabelle guida
Le impostazioni che condizionano questo archivio sono contenute nel settore di tabelle BRR (Tipo risorsa) : 
 :  : DEC T(ST) K(BRL)
e nel settore di tabella BRM (Gruppo risorsa) : 
 :  : DEC T(ST) K(BRM)

## Autorizzazioni
La classe di autorizzazione è 'D' funzione 'BRRI01G'.

## Note strutturate (Tabella NSC)
Il contenitore si assume dalla tabella BRM (gruppo risorsa). Se non inserito si assume 'RIS'.
Chiave 1 - Elemento della BRR
Chiave 2 - Codice risorsa (Tipo 'RI' e parametro elemento BRR)
Chiave 3 - N.A.

## Parametri (Tabella C£E)
La categoria parametri si assume dalla tabella BRM.

## Flussi (Tabella B£H)
Per ogni tipo di flusso x (I : Creazione, C : Copia, A :  Azioni eseguibili, ecc..) viene associato il flusso x-RIyyy, dove yyy è il gruppo risorsa; se assente viene associato il flusso x-RI.

## Costruzione automatica campi (tabella B£C)
N.A.

## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
N.A.

## /COPY
Interfaccia risorse £IRI : 
 :  : DEC T(MB) P(QILEGEN) K(£IRI)
In alcuni programmi è ancora utilizzata la precedente interfaccia £IFRIS.

## Gruppi flag
N.A.

## Workflow e popup
N.A.

## Note particolari

## CONTENUTO DEI CAMPI

 :  : FLD C§STAT **Stato**
In inserimento si assume il primo stato valido del settore (B£W RI).
In variazione, se impostato, viene controllato che lo stato sia compatibile con lo stato precedente dell'archivio.
