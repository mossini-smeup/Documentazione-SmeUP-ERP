## Contenuto
Definizione dei legami tra due oggetti.

## Codice Oggetto (in TA/*CNTT)
Nessuno.

## Chiave primaria
N.A.

## Ulteriore chiave primaria
D§TIPD - D§ASSI - D§USR1 - D§COMP - D§USR2

## Altri condizionamenti facoltativi in ricerca
N.A.

## Tabella guida
Le impostazioni che condizionano questo archivio sono contenute nel settore di tabelle BRL (Tipo distinta).
 :  : DEC T(ST) K(BRL)

## Autorizzazioni
Per la guida la classe di autorizzazione è 	BRDI01G.
Per la lista la classe di autorizzazione è 	BRDI01L.

## Note strutturate (Tabella NSC)
Il contenitore si assume dalla tabella BRL. Se non inserito si assume DIB.
Le tre chiavi delle note sono : 
Chiave 1 - Assieme
Chiave 2 - Componente
Chiave 3 - Posizioni 1  :  4 sequenza 1 - Posizioni 12  :  15 sequenza 2.

## Parametri (Tabella C£E)
N.A.

## Flussi (Tabella B£H)
N.A.

## Costruzione automatica campi (tabella B£C)
N.A.

## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
In tabella BRL si possono impostare i suffissi : 
- del programma di controllo in manutenzione distinta
- del programma di "postgestione" eseguito dopo aver aggiornato l'archivio.

## /COPY
Scansione distinta (£DIB) : 
 :  : DEC T(MB) P(QILEGEN) K(£DIB)

Gestione quantità distinta (£BRD) : 
 :  : DEC T(MB) P(QILEGEN) K(£BRD)

## Gruppi flag
N.A.

## Workflow e popup
N.A.

## Note particolari

### Impostazioni fisse
Sono fissati i seguenti tipi distinta : 
 * ART  -    Se distinta unica per articolo (da tabella BR1)
 * TAB  -    Struttura legami tabelle.

## CONTENUTO DEI CAMPI

 :  : FLD D§STAT **Stato**
In inserimento si assume lo stato impostato in tabella BRL.
In variazione, se impostato, viene controllato che lo stato sia compatibile con lo stato precedente dell'archivio.

