## Obiettivo

Attraverso questa funzione è possibile stampare i modelli e generare il file da trasmettere poi all'agenzia delle dogane tramite sistema Intraweb.

## Formato guida

All'interno del formato guida sono disponibili le seguenti informazioni : 

 * Tipo elaborazione. Indica la tipologia di transazioni da elaborare; le opzioni disponibili sono : 
 ** X = Completa. Permette di estrarre sia gli acquisti che le cessioni.
 ** XM = Merci. Permette di estrarre i soli record relativi a merci (sezioni 1 e 2 dei modelli).
 ** XS = Servizi. Permette di estrarre i soli record relativi a prestazioni (sezioni 3 e 4 dei modelli).
 ** C = Cessioni. Permette l'estrazione dei soli record relativi a cessioni di beni e servizi (modello Intra1).
 ** A = Acquisti. Permette l'estrazione dei soli record relativi ad acquisti di beni e servizi (modello Intra2).
 ** CM = Cessioni - Merci. Permette di estrarre i soli record relativi a merci cedute (Intra 1 bis e ter).
 ** AM = Acquisti - Merci. Permette di estrarre i soli record relativi a merci acquistate (Intra 2 bis e ter).
 ** CS = Cessioni - Servizi. Permette di estrarre i soli record relativi a prestazioni effettuate (Intra 1 quater e quinquies).
 ** AS = Acquisti - Servizi. Permette di estrarre i soli record relativi a prestazioni ricevute (Intra 2 quater e quinquies).
 * Anno/Mese/Trimestre. Riporta il periodo di elaborazione.
 * Dati trimestre. Indica se vanno trasmessi tutti o solo i primi mesi del trimestre, in previsione del passaggio alla periodicità mensile.
 * Dkt.C./Dkt.A. Questi campi compaiono nel caso in cui si effettui la trasmissone definitiva o una ritrasmissione.
 ** Nel caso della trasmissione definitiva viene automaticamente calcolo il nuovo numero da attribuire.
 ** Nel caso di ritrasmissione viene proposto il n° più alto che viene trovato nel periodo. Se per uno stesso periodo sono state effettutate più trasmissioni è possibile rettificare manualmente il n° per indicare il modo preciso la trasmissione che si vuole rieseguire.
 * Tipo trasmissione. In questo campo è possibile scegliere con quale modalità eseguire la trasmissione : 
   1 = Definitiva
   2 = Ritrasmissione
   3 = Annullamento Definitiva
     = Provvisoria (default)
 * Dati Soggetto. Se questo campo viene selezionato verranno trasmessi i dati del 'Soggetto diverso da persona fisica' sul frontespizio dei modelli.
 * Causale. Questo campo serve per compilare i realtivi campi presenti sui frontespizi dei modelli.
 * Stampa log. Flaggando questo campo è possibile ottenere, oltre ai modelli, una stampa di controllo delle dichiarazioni.
 * Contatto. Attraverso questi tre campi è possibile filtrare la tipologia e il codice ente di cui estrarre le registrazioni intrastat.
 * Trasferimento. Consente di gestire i parametri con i quali il programma genererà il file Scambi.CEE, compreso l'eventuale cartella di destinazione.
 * ENTRATEL. Se la trasmissione avviene tramite l'entratel attivando questo campo il file verrà integrato delle specifiche necessarie per questo tipo di trasmissione.

All'interno della schermata è disponibile il campo delle memorizzazioni che consente di salvare una particolare compilazione della finestra. Per maggiori dettagli sull'utilizzo delle memorizzazioni video si veda il seguente : 

- [Gestione Dati Scelte Video](Sorgenti/MB/DOC_OGG/P_B£MDV0)

### Tasti Funzionali

 * F06 - Conferma. Permette di lanciare la funzione.
 * F11 - Parametri. Peremtte di impostare i parametri di lancio della funzione come l'interattività del lavoro o alcune specifiche di stampa.
