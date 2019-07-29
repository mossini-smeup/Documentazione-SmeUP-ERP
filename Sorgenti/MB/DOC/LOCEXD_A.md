# Obiettivo
La scheda è un componente di Looc.up Web.UP la cui finalità primaria è la presentazione di insiemi di dati correlati.
In un'unica finestra vengono mostrate varie sezioni, ognuna delle quali rappresenta un insieme di dati tramite un componente di Looc.up :  in pratica in una sola schermata vengono raggruppate più chiamate a funzioni di Looc.up, riunendo nello stesso contesto alberi, matrici e altre forme di visualizzazione.

>N.B. :  Non tutti i componenti di LOOC.up sono utilizzabili all'interno di una scheda, come ad esempio l'emulazione 5250.
In questi casi è solo possibile aprire in una nuova finestra tali componenti. Lo stesso concetto si applica anche tra web e client, non tutti i componenti che si possono utilizzare in Web.UP sono visualizzabili in Looc.UP.

# Utilizzi
Nata come strumento per visualizzare i dati di un oggetto di Sme.up, quindi legata a un Tipo-Parametro, si è successivamente svincolata da questa limitazione.
In parallelo sono state aggiunte diverse funzionalità per quanto riguarda la dinamicità tra le varie sezioni che compongono una scheda :  è possibile operare delle scelte sui dati mostrati in una sezione per condizionare i dati mostrati in altre sezioni (selezionare un cliente da una lista per vederne gli ordini attivi, ad esempio).

È quindi possibile, ora, utilizzare la scheda per realizzare dei veri e propri "cruscotti" di controllo; accanto alle classiche schede cliente, articolo, ecc., si possono implementare schede più generali, come ad esempio : 
 * Scheda riepilogativa di tutti gli ordini di vendita attivi
 * Scheda delle statistiche degli agenti
 * Scheda degli indici di andamento dell'azienda
 * Schede di andamento della produzione

## Come accedere ad esempi di scheda

- Schede di oggetto :  dalla schermata iniziale di Looc.up premere F4 e inserire un oggetto (un articolo o un cliente); dando OK si accede alla scheda di tale oggetto.

![LOCEXD_024](http://localhost:3000/immagini/LOCEXD_A/LOCEXD_024.png)
# Associazione scheda oggetto
Una scheda è individuata dal nome del suo script, salvato in un membro di file AS/400.
Distinguiamo due categorie di schede, a seconda del nome dello script ad esse associato : 
 * Schede generiche
 * Schede di oggetto

## Schede generiche
Uno script di scheda può avere un nome qualsiasi; la scheda corrispondente può essere lanciata come una normale funzione di LOOC.up, quindi : 
 * Dalla barra dei menù di Looc.up, Servizi / Funzione libera
 * Dai menù di Looc.up (quindi elemento della TAMEA)
 * Da una voce dei Preferiti
 * Da un altro componente di Looc.up, come un albero o un'altra scheda

La funzione da chiamare è del tipo F(EXD;*SCO;) 1(...;...;...) 2(...;...;...) 3(...;...;...) 4(...;...;...) P(...), dove : 
 * EXD è il componente scheda
 * *SCO il servizio (programma JATRE_18C) che fornisce l'XML al componente in seguito all'interpretazione di uno script
 * negli Oggetti da 1 a 4 va specificato, secondo varie modalità, quale script elaborare
 * P è una stringa attraverso cui possono essere passati ulteriori parametri il cui valore condizionerà l'esecuzione dello script.
 *INPUT è un ulteriore stringa in cui gli si possono passare parametri aggiuntivi

## Schede associate ad un oggetto
Le schede il cui nome di script corrisponde a un Tipo-Parametro di Sme.up sono un sottocaso delle schede generiche :  sono associate agli oggetti di quel tipo e, in aggiunta alle modalità di lancio delle schede generiche, possono essere richiamate : 
 * Dall'F4 nella schermata iniziale di LOOC.up specificando un oggetto e dando OK;
 * Da qualunque punto in LOOC.up in cui un campo sia riconosciuto come oggetto, cliccando su "scheda oggetto" nelle azioni presentate con il clic del tasto destro su un oggetto.

Dato un oggetto, viene cercato uno script dal nome corrispondente al "Tipo-Parametro" dell'oggetto; se c'è non viene cercato uno script dal nome "Tipo"; se anche questo manca viene utilizzato lo script dell'oggetto OGOG, se definito, oppure uno script di default.

## Sottoschede
All'interno di ciascuna scheda è possibile definire sottoschede richiamabili dalla scheda di appartenenza o da altre schede. Per il richiamo di sottoschede si distinguono due casi : 
 * La sottoscheda appartiene alla scheda origine : 
In questo caso il caricamento avviene semplicemente con il comando
 :  : D.SCH Nam(NOME_SOTTOSCHEDA)

 * La sottoscheda appartiene ad una scheda diversa da quella di origine
In questo caso il caricamento avviene invece con il comando
 :  : D.FUN.STD F(EXD;*SCO;) 2(MB;SCP_SCH;NOME_SCHEDA) 4(;;NOME_SOTTOSCHEDA)

# Esecuzione di una scheda
Tipicamente una scheda di oggetto viene eseguita su una particolare istanza dell'oggetto a cui è associata, indicata nel parametro Oggetto 1 :  la struttura dei dati mostrati è comune (impostata nello script di scheda), cambiano i valori presentati.
Le schede generiche possono, invece, dipendere o meno da un oggetto particolare, ad esempio : 
Ulteriori oggetti o opzioni possono essere passati nel parametro P(...) e liberamente gestiti nello script di scheda.

## Esempi
Schede generiche : 
 * Un cruscotto di controllo che mostra tutti gli ordini attivi di un'azienda, richiamato con F(EXD;*SCO;) 2(MB;SCP_SCH;ORDINI)
 * La stessa scheda, filtrata sugli ordini dell'agente 00 :  F(EXD;*SCO;) 2(MB;SCP_SCH;ORDINI) P(AGE(00))
 * La stessa scheda, filtrata sugli ordini dell'agente 00 e del cliente 000001 :  F(EXD;*SCO;) 1(CN;CLI;000001) 2(MB;SCP_SCH;ORDINI) P(AGE(00)). In questo caso nella scheda sono disponibili per la visualizzazione anche gli OAV del cliente in esame.

Schede di oggetto : 
 * La scheda del cliente 000001, richiamata con F(EXD;*SCO;) 1(CN;CLI;000001)
 * La scheda dei dati di base dell'articolo A01, richiamata con F(EXD;*SCO;) 1(AR;;A01) 3(;;BAS)

# Perchè usare la scheda
## Modularità
Una scheda può essere composta da varie sezioni, ognuna delle quali viene rappresentata da uno o più componenti di Looc.up/Web.UP.
Anche la scheda è un componente di LOOC.up, quindi in una sezione è possibile visualizzare un'altra scheda.
Diventa quindi semplice costruire schede anche molto complesse mettendo insieme schede elementari, potenzialmente riutilizzabili in più contesti.

## Espandibilità
Le informazioni visualizzate all'interno di una sezione di scheda sono reperite dall'AS/400 mediante programmi AS (i **servizi**) che le convertono in formato XML da fornire in input ai componenti di Looc.up.
Sono forniti vari servizi standard da Sme.up per il reperimento di tali informazioni, sia generici (liste di oggetti, OAV, ...) che specifici per moduli (ad esempio, per il V5 la lista di documenti di un certo tipo intestati a un ente).
È molto semplice, qualora questi non bastassero, costruire servizi personalizzati con i quali arricchire i dati rappresentabili in una scheda.

## Configurabilità dell'output
Negli script di scheda è possibile fornire informazioni ai componenti di Looc.up relative alla modalità di visualizzazione dei dati nella scheda.
Si può, ad esempio, definire il tipo di grafico visualizzato in una sezione, oppure impostare quali colonne visualizzare in una matrice di valori, preimpostando ordinamenti, somme sui dati...

## Dinamicità
Una scheda può essere dinamica a vari livelli.
 - Le informazioni presentate sono caricate di volta in volta dall'AS, quindi possono variare in due richiami successivi. Ad esempio, se una scheda generica mostra tutti gli ordini di vendita attivi in un'azienda in due richiami successivi tale elenco può variare.
 - I dati mostrati nelle schede associate agli oggetti sono sempre variabili in base all'istanza dell'oggetto considerato :  in una scheda cliente, ad esempio, le informazioni mostrate per il cliente 001 e 002 (come i suoi attributi, o gli ordini ad esso intestati) cambiano.
 - La struttura di una scheda può dipendere da caratteristiche dell'oggetto su cui è eseguita oppure di altri parametri passati nella chiamata :  posso decidere, in una scheda cliente, di non mostrare l'elenco degli ordini di vendita attivi se il cliente che sto visualizzando è estero.
 - I dati visualizzati in una sezione di scheda, infine, possono dipendere da scelte operate dall'utente in altre sezioni della scheda. Per esempio, in una scheda posso mostrare un elenco di articoli in una sezione e, dopo averne selezionato uno, visualizzarne gli attributi in una seconda sezione della stessa scheda, dipendente dalla prima.
