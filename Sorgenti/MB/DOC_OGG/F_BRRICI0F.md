## Contenuto
Codici, dati quantitativi e descrittivi che caratterizzano le operazioni di un ciclo di lavoro.

## Codice Oggetto (in TA/*CNTT)
Nessuno.

## Chiave primaria
N.A.

## Ulteriore chiave primaria
R§TCIC - R§CODI - R§CICL - R§SQCI - R§CVAD

## Altri condizionamenti facoltativi in ricerca
N.A.

## Tabella guida
Le impostazioni che condizionano questo archivio sono contenute nel settore di tabelle BRT (Tipo ciclo) : 
 :  : DEC T(ST) K(BRT)

## Autorizzazioni
La classe di autorizzazione è 'BRCI15' con funzione uguale al tipo ciclo (TA/BRL).

## Note strutturate (Tabella NSC)
Il contenitore note associato è definito in un elemento di un'azione B£J in un sottosettore fissato in una B£H apposita. Le chiavi da impostare nel contenitore note devono essere congruenti con quanto inserito nella B£J in questione.
Vedi come riferimento il documento relativo alle funzioni di una fase e risorse produttive secondarie : 
- [Funzioni di una fase e Risorse prod.secondarie](Sorgenti/MB/DOC/BRRIPS)

## Parametri (Tabella C£E)
La categoria parametri associata è definita in un elemento di un'azione B£J in un sottosettore fissato in una B£H apposita. Le chiavi da impostare nella categoria parametri devono essere congruenti con quanto inserito nella B£J in questione.
Vedi come riferimento il documento relativo alle funzioni di una fase e risorse produttive secondarie : 
- [Funzioni di una fase e Risorse prod.secondarie](Sorgenti/MB/DOC/BRRIPS)

## Flussi (Tabella B£H)
I flussi collegati NON sono utilizzati come esecuzione di funzioni all'atto dell'inserimento, variazione e annullamento, ma come collezione di azioni eseguibili dal dettaglio della manutenzione cicli.
Essi sono definiti in elementi così codificati :  A-F2xxx dove xxx è il tipo ciclo, se assente si risale a A-F2.
Vedi come riferimento il documento relativo alle funzioni di una fase e risorse produttive secondarie : 
- [Funzioni di una fase e Risorse prod.secondarie](Sorgenti/MB/DOC/BRRIPS)

## Costruzione automatica campi (tabella B£C)
N.A.

## Presenza monitor - visualizzatore
N.A.

## Programmi di controllo
Si può impostare, in tabella BRT, il suffisso x di un programma BRCI15D_x, lanciato dal dettaglio del ciclo, che permette di eseguire controlli specifici.

## /COPY
Scansione cicli £CIR : 
 :  : DEC T(MB) P(QILEGEN) K(£CIR)

Cicli di lavoro - Gestione Tempi £BRT : 
 :  : DEC T(MB) P(QILEGEN) K(£BRT)

Funzioni su oggetti/sviluppi di una fase £BRG : 
 :  : DEC T(MB) P(QILEGEN) K(£BRG)

Funzioni Risorse produttive secondarie £BRJ : 
 :  : DEC T(MB) P(QILEGEN) K(£BRJ)

Sviluppi righe ciclo :  Note/param./Ris.sec. £BRR : 
 :  : DEC T(MB) P(QILEGEN) K(£BRR)

## Gruppi flag
N.A.

## Workflow e popup
N.A.

## Note particolari

## CONTENUTO DEI CAMPI

 :  : FLD R§STAT **Stato**
Se lo stato è impostato, si controlla che esista in tabella e, in variazione, che sia compatibile con lo stato precedente dell'archivio.

 :  : FLD R§CODI **Codice**
E' l'oggetto tipizzato dai campi "Significato codice" (tipo) e "Parametro codice" (parametro).
di tabella BRT.

 :  : FLD R§RISO **Codice risorsa**
E' l'oggetto tipizzato dai campi "Tipo rsiorsa" e "Parametro risorsa" di tabella BRT.
