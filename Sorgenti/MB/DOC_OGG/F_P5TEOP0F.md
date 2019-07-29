## Contenuto
Informazioni di quantità, date e classificazioni degli ordini di produzione.

## Codice Oggetto (in TA/*CNTT)
 'OR'                               £FUNT1

## Chiave primaria
N.ro ordine              (OR)      £FUNK1

## Altri condizionamenti facoltativi in ricerca
Tipo ordine              (TA/P5T)  £FUNP1

## Ulteriore chiave primaria
N.A.

## Tabella guida
Le impostazioni che condizionano questo archivio sono contenute nel settore di tabelle P5T (Tipo ordine di produzione) : 
 :  : DEC T(ST) K(P5T)

## Autorizzazioni
La classe di autorizzazione è P5OR01.

La funzione di autorizzazione è il programma in cui si esegue il controllo : 
 * P5OR01G   -    Formato guida
 * P5OR01L   -    Lista

## Note strutturate (Tabella NSC)
Il contenitore si assume dalla tabella P5T (tipo ordine). Se non inserito si assume OR.
 Chiave 1 OR Ord. produzione
 Chiave 2 N.A.
 Chiave 3 N.A.

## Parametri (Tabella C£E)
La categoria si assume dalla tabella P5T (tipo ordine).

## Flussi (Tabella B£H)
Per ogni tipo di flusso x (I : Creazione, C : Copia, A : Azioni eseguibili, ecc..) viene associato il flusso x-ORyyy, dove yyy è il tipo ordine; se assente viene associato il flusso x-OR.

## Costruzione automatica campi (tabella B£C)
N.A.

## Presenza monitor - visualizzatore
In tabella P51 si deve impostare il flag "Visualiz.su Ord.Prod.". In tal caso la forma di presentazione viene assunta da quella impostata in tabella P5T, se assente, da quella in tabella P51.

## Programmi di controllo
In tabella P5T si può impostari il suffisso di un programma di controlli specifico, e quello di un programma lanciato all'atto dell'inizializzazione dell'ordine di produzione.

## /COPY
Interfaccia ordine di produzione IFORP : 
 :  : DEC T(MB) P(QILEGEN) K(£IFORP)

Inizializzazione ordine di produzione P5Y : 
 :  : DEC T(MB) P(QILEGEN) K(£P5Y)

Integrazione ordini di produzione P5I : 
 :  : DEC T(MB) P(QILEGEN) K(£P5I)

Sintesi valori di un ordine di produzione P5O : 
 :  : DEC T(MB) P(QILEGEN) K(£P5O)

Calcolo quantità :  specifiche P5Q
 :  : DEC T(MB) P(QILEGEN) K(£P5Q)

Reperimento tabelle collegate ad un elemento di P5T : 
 :  : DEC T(MB) P(QILEGEN) K(£P5T)

Controllo campi di un ordine di produzione P5Z : 
 :  : DEC T(MB) P(QILEGEN) K(£P5Z)

Calcolo date P5A : 
 :  : DEC T(MB) P(QILEGEN) K(£P5A)

## Gruppi flag
Il gruppo flag è assunto dalla tabella P5T (tipo ordine).

## Workflow e popup
N.A.

## Note particolari

## CONTENUTO DEI CAMPI

 :  : FLD K§NORD**Numero ordine**
Si utilizza il muneratore (di tabellla CRN, sottosettore P5), impostato in tabella P5T.

 :  : FLD K§DTOR**Data ordine**
Si può impostare, in tabella P5T, che venga proposta la data odierna.

 :  : FLD K§LIVE**Livello**
In inserimento si assume il livello di nascita dalla tabella P5T, e si deriva il primo stato valido di questo livello. Se non codificato, si assume il livello 2.

 :  : FLD K§STAT**Stato**
In variazione viene controllato che lo stato sia compatibile con lo stato precedente dell'archivio.

 :  : FLD K§USTA**Ultimo stato ante chiusura**
Ultimo stato prima della chiusura. Viene impostato quanto ordine passa a livello >=8

 :  : FLD K§ARTI**Codice Articolo**
Si può impostare, in tabella P5T, che non venga richiesto l'articolo, in modo da descrivere ordini di servizi.
Sempre in tabella P5T, si possono impostare gli stati minimo e massimo validi per l'articolo.

 :  : FLD K§COMM**Commessa**
Si può impostare, in tabella P5T, che la commessa sia obbligatoria.

 :  : FLD K§CLPR**Classe programmazione**
Viene ripresa dal campo omonimo dell'articolo.

 :  : FLD K§TDOC**Tipo documento**
Viene ripreso dal tipo documento assunto di tabella P5T.

 :  : FLD K§NDOC**Numero documento**
Documento tipizzato dal tipo documento di questo archivio.

 :  : FLD K§TIEN**Tipo ente**
Viene ripreso dal tipo ente assunto di tabella P5T.

 :  : FLD K§NDOC**Codice ente**
Ente tipizzato dal tipo ente di questo archivio.

 :  : FLD K§TIRF**Tipo oggetto di riferimento**
Viene ripreso dal campo omonimo di tabella P5T.

 :  : FLD K§PARF**Parametro oggetto di riferimento**
Viene ripreso dal campo omonimo di tabella P5T.

 :  : FLD K§OGRF**Riferimento**
Oggetto tipizzato dal tipo e parametro riferimento di questo archivio.

 :  : FLD K§TIMT**Tipo impegno matriali**
Viene ripreso dal campo omonimo di tabella P5T.

 :  : FLD K§MCDI**Modo costuzione impegno matriali**
Viene ripreso dal campo omonimo di tabella P5I (tipo impegno materiali).

 :  : FLD K§TODI**Tipo oggetto distinta variazione**
Viene ripreso dal campo omonimo di tabella P5I (tipo impegno materiali).

 :  : FLD K§PADI**Parametro oggetto distinta variazione**
Viene ripreso dal campo omonimo di tabella P5I (tipo impegno materiali).

 :  : FLD K§OJDI**Oggetto distimta variazione**
Oggetto tipizzato dal tipo e parametro distinta variazione di questo archivio.

 :  : FLD K§TIRS**Tipo impegno risorse**
Viene ripreso dal campo omonimo di tabella P5T.

 :  : FLD K§MCCI**Modo costuzione impegno risorsei**
Viene ripreso dal campo omonimo di tabella P5S (tipo impegno risorse).

 :  : FLD K§TOCI**Tipo oggetto ciclo variazione**
Viene ripreso dal campo omonimo di tabella P5I (tipo impegno risorse).

 :  : FLD K§PADI**Parametro oggetto ciclo variazione**
Viene ripreso dal campo omonimo di tabella P5S (tipo impegno risorse).

 :  : FLD K§OJCI**Oggetto ciclo variazione**
Oggetto tipizzato dal tipo e parametro ciclo variazione di questo archivio.

 :  : FLD K§PRIO**Priorità**
Viene proposto dal campo omonimo di tabella P5T.

 :  : FLD K§PRIC**Priorità calcolata**
Campo libero NON aggiornato dall'applicazione.

 :  : FLD K§TMAT**Tipo matricola**
Viene proposto dal "tipo matricola assunta" di tabella P5T.

 :  : FLD K§NMAT**Numero matricola**
Matricola tipizzata dal tipo matricola.

 :  : FLD K§CAMO**Caus.mag.vers.forz.**
Se presente è la causale utilizzata per i versamenti sull'articolo dell'ordine di produzione

 :  : FLD K§TCVS**Tipo sviluppo quantità**
Viene proposto dal campo omonimo di tabella P5T.

 :  : FLD K§NMAT**Codice sviluppo quantità**
Elemento di sviluppo quantità tipizzato dal tipo sviluppo quantità.

 :  : FLD K§UNMS**Unità di misura**
Viene ripresa dal campo omonimo dell'articolo.

 :  : FLD K§QT01 **Quantità 1**
Campo numerico tipizzato dall'elemento dal secondo flag  (Tipo quantità).
 :  : FLD K§QT02.K§QT01 **Quantità 2**
 :  : FLD K§QT03.K§QT01 **Quantità 3**
 :  : FLD K§QT04.K§QT01 **Quantità 4**
 :  : FLD K§QT05.K§QT01 **Quantità 5**

 :  : FLD K§LDTF**Tempo approvvigionamento fisso**
Viene ripreso dal valore corrispndente dell'articolo.

 :  : FLD K§LDTV**Tempo approvvigionamento variablile**
Viene ripreso dal valore corrispndente dell'articolo.

 :  : FLD K§LDTR**Tempo approvvigionamento rettifica**
Viene ripreso dal valore corrispndente dell'articolo.

 :  : FLD K§TSCH**Tipo schedulazione**
Viene proposto dal campo omonimo di tabella P5T.
E' riservato per sviluppi futuri.

 :  : FLD K§TRIS**Tipo risorsa**
Viene proposto dal "tipo risorsaa assunta" di tabella P5T.

 :  : FLD K§RISO**Codice risorsa**
Risorsa tipizzata dal tipo risorsa.

