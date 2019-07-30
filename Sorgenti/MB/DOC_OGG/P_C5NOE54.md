## Obiettivo

Attraverso questa funzione è possibile analizzare e lanciare l'esecuzione delle scritture di differenze cambio per conti di contabilità generale .

## Formato guida

Il formato guida si presenta nel seguente modo : 

![C5D010_037](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOE54/C5D010_037.png)
All'interno del formato guida è necessario specificare i seguenti campi : 

 - Codice della lista di conti per cui si voglia eseguire la funzione. Nel caso in cui il campo venga lasciato bianco il sistema analizzerà l'elenco completo dei conti contabili.Per dettagli sull'utilizzo delle liste oggetti si veda : 

- [Liste oggetti](Sorgenti/MB/DOC_OPE/B£_LIS)

 - Funzione e Metodo. Per l'esecuzione delle scritture di oscillazione cambio è necessario impostare questi campi rispettivamente con M e K.
- Modalità. In questo campo è necessario indicare il tipo azione da eseguire. Le modalità disponibili per l'esecuzione di questa funzione sono : 
 -- 1 - Stampa :  permette di stampare un prospetto delle registrazioni eseguite automaticamente.
 -- 2 - Interrogazione :  permette di visualizzare le differenze cambio rilevate.
 -- 3 - Esecuzione :  permette di lanciare la funzione vera e propria.
 - Pertinenza. In questo campo è necessario indicare se considerare le sole registrazioni fiscali, le sole gestionali o entrambe.
 - Condizione. In questo campo è necessario indicare se considerar le sole registrazioni attive, le sole simulate o entrambe. Per maggiori dettagli sulla definizione e utilizzo della pertinenza e condizione nelle registrazioni contabili si veda il seguente : 

 :  : DEC T(MB) P(DOC_VOC) K(GLO_C5) I(Glossario Contabilità) L(1)

 - Esercizio. In questo campo è necessario indicare l'esercizio contabile per il quale si voglia eseguire la funzione.
 - Data Situazione. In questo campo è possibile impostare una particolare data a cui analizzare la situazione dei mastrini. Se non impostata il sistema analizza la situazione al 31 Dicembre dell'esercizio impostato nel campo sopra.


### Impostazioni
Digitando il tasto F17 o selezionando il relativo bottone è possibile accedere alle Impostazioni che riportano i seguenti campi : 
![C5D010_038](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOE54/C5D010_038.png)
- Tipo Calcolo. E' possibile richiedere un calcolo dettagliato per partita oppure sul saldo complessivo del conto. Il calcolo per partita è eseguibile solo per i conti su cui è attiva la Gestione a Documenti (si veda tabella C5B).
- Tipo Cambio di riferimento. Può essere compilato con : 
-- E - Cambi fissi verso l'Euro
-- 1 - Cambio effettivo
-- 2 - Cambio budget
-- 3 - Cambio Simulazione
-- 4 - Cambio Standard
-- 5 - Cambio di confronto
- Solo Totale? E' un campo Sì/No :  se compilato con Sì permette di visualizzare solo i totali per valuta
- Differenza minima rilevabile. Indica l'importo al di sotto del quale non viene rilevata la differenza cambio.
- Ometti sintesi cambi. Permette di visualizzare o meno la sintesi dei cambi applicati alla fine del prospetto.

Dati registrazione. Nei dati a seguire sono riporati i parametri per l'esecuzione della registrazione come la data e il tipo registrazione e conti di rilevazione di oscillazioni attive e passive.

- Autostorno.
- Data
- Tipo Registrazione
- Conto Differenze Attive
- Conto Differenze Passive


All'interno delle impostazioni sono disponibili le memorizzazioni video attraverso cui e' possibile salvare una specifica configurazione delle impostazioni : 

![C5C010_072](http://localhost:3000/immagini/MBDOC_OPE-C5C010_01/C5C010_072.png)
Le memorizzazioni salvate saranno poi richiamabili direttamente dal formato guida attraverso l'utilizzo dei caratteri di ricerca all'interno dello specifico campo : 

![C5C010_073](http://localhost:3000/immagini/MBDOC_OPE-C5C010_01/C5C010_073.png)
Per maggiori dettagli sull'utilizzo delle memorizzazioni video si veda il seguente : 

- [Gestione Dati Scelte Video](Sorgenti/MB/DOC_OGG/P_B£MDV0)

 :  : I.INC.MBR Lib(SMEDEV) Fil(DOC_OPE) Mem(C5BASE_01) Tag(Parzializazioni)

### Tasti funzionali

 * F06 :  Conferma. Permette di confermare ed eseguire la funzione
 * F11 :  Parametri esecuzione. Permette di impostare i parametri per l'esecuzione della funzione; in particolare è possibile definire se eseguire il lavoro in modalità interattiva oppure batch, come eseguire la stampa, ecc.
 * F13 :  Parzializzazioni. Permette di definire dei filtri per l'estrazione dei dati
 * F17 :  Impostazioni. Permette di accedere alla schermata delle impostazioni.

### Memorizzazioni

Le memorizzazioni consentono di salvare le parametrizzazioni definite all'interno della videata. Per maggiori dettagli sulla loro creazione e gestione si veda il seguente : 

- [Gestione Dati Scelte Video](Sorgenti/MB/DOC_OGG/P_B£MDV0)


## Formato lista
Lanciando la funzione con modalità Interrogazione è possibile visualizzare l'elenco delle oscillazioni rilevate. Il formato di questo elenco varia in funzione delle impostazioni definite e della struttura dei conti : 

![C5D010_039](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOE54/C5D010_039.png)
In questo caso è riportato l'esempio di conti gestiti a partita e l'interrogazione è stata effettuata impostando il tipo calcolo per partite.
Pe ogni partita in valuta sono riportati seguenti dati : 

- Data e Numero Documento
- Valuta della partita
- Importo in Valuta
- Cambio riportato nella registrazione
- Importo in Euro calcolato con il cambio precedente
- Cambio Attuale
- Importo in euro con il cambio attuale
- Differenza tra importo in euro al cambio storico e al cambio attuale (Valore della registrazione di oscillazione cambio)


Lanciando la funzione con modalità 3 - Esecuzione verrà scritta la registrazione di oscillazione cambio che sarà parametrizzata in funzione dei dati inseriti nelle impostazioni.
In particolare se viene indicato un Tipo Calcolo per partita il sistema procederà scrivendo una riga per ogni partita rilevata all'interno dell'oscillazione cambi e all'interno della riga verranno riportati i riferimenti della partita stessa; se invece il Tipo calcolo è impostato a Saldo verrà scritta una sola riga per conto contabile.

### Tasti funzionali

 * F01 :  Permette di ricercare una stringa all'interno della videata
 * F05 :  Esegue l'aggiornamento della videata
 * F04 :  Permette di eseguire una stampa della lista visualizzata in PDF o in spool di stampa
 * F09 :  Permette di posizionarsi sulla prima pagina del mastrino
 * F10 :  Permette di posizionarsi sull'ultima pagina del mastrino
 * F13 :  Parzializzazioni. Permette di definire dei filtri per l'estrazione dei dati
 * F17 :  Impostazioni. Permette di accedere alla schermata delle impostazioni.


