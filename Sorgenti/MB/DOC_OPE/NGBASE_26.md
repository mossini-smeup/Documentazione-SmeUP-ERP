# Analisi Variazioni Prezzi di Vendita

## Analisi Variazioni Prezzi di Vendita

## Introduzione

Nel caso in cui la sede apporti delle modifiche al Listino Vendita e cambi i prezzi di alcuni Prodotti, i Punti Vendita possono, tramite la funzione in oggetto, Generare e Stampare Elenchi e/o Etichette delle variazioni dei Prezzi di Vendita.

## Attivazione

Per attivare questa funzionalità selezionare _Principale>Anagrafiche di Base>Stampa Anagrafiche di Base>Analisi Variazioni Prezzi di Vendita.
All'attivazione della funzione viene presentato l'elenco delle Analisi Variazioni di Prezzo (in Ordine decrescente di Data e Ora) effettuate fino al momento della selezione della funzione.

Sono a disposizione i seguenti tasti funzionali : 

 * Invio Per Stampare l'Elenco delle Variazioni e/o le Etichette
 * F4 Cancella Elenco Variazioni
 * F5 Visualizza Variazioni Prezzo
 * F6 Crea Elenco Variazioni
 * F7 Crea Previsione Variazioni
 * F8 Crea Tabella Stampa Frontalini
 * F9 Schedulazione. Per la preparazione automatica degli Elenchi

## Creazione Elenco Variazioni

La funzione permette di generare l'elenco delle Variazioni Prezzi di Vendita intervenute sugli Articoli rispetto all'ultima data di Creazione dell'Elenco (dello stesso tipo, quindi con gli stessi Parametri di selezione).
Premere F6 Crea Elenco Variazioni ed indicare : 

 * Tipo Creazione. E' possibili scegliere tra
 ** Prezzi di Vendita Negozio. Per ottenere l'elenco dei nuovi Prezzi di Vendita indipendentemente dal Listino su cui sono intervenute le variazioni. bbligatorio specificare il Codice del Punto Vendita di riferimento
 ** Listino. Nel caso in cui si intenda ottenere l'Elenco delle Variazioni Prezzo di un Listino specifico.
 * Codice Listino. Specificare un Codice Listino se il Tipo Creazione sarà di Tipo Listino
 * Negozio.

Nel caso di selezione di **Prezzi di Vendita Negozio** il programma analizzerà i Prezzi di Vendita dei Listini definiti sull'Anagrafica del Magazzino nello stesso ordine in cui vengono analizzati per la
determinazione dei Prezzi di Vendita in Cassa e cioè : 

 * Listino Saldi
 * Listino Speciale 2
 * Listino Speciale 1
 * Listino di Vendita

Verrà utilizzato il primo prezzo trovato.

Premere Conferma e attendere che il Sistema elabori l'Elenco Variazioni. Una volta terminato, si chiuderà la finestra di Elaborazione e comparirà la riga dell'Analisi in alto nella finestra (verrà posizionata come prima riga).

## Creazione Previsione Elenco Variazioni

Questa funzione permette di generare una Previsione delle Variazioni Prezzi di Vendita
Non vengono cioè analizzati i prezzi in vigore, ma i prezzi che andranno in vigore alla data specificata (in base naturalmente alle informazioni già presenti nel DataBase).
Il confronto sui prezzi verrà effettuato rispetto all'ultima data di Creazione di un **Elenco non di Previsione dello stesso tipo.
Premere F7 Crea Previsione Variazioni e compilare gli stessi parametri della normale funzione di Creazione Elenco Variazioni con la sola aggiunta della Data di Previsione (obbligatoria)

## Visualizza Variazioni Prezzo

Il tasto F5 permette di visualizzare il Dettaglio (con la suddivisione per Colore e Taglia) delle Variazioni di Prezzo.
Vengono evidenziati Articolo/Colore/Taglia, Nuovo Prezzo e Vecchio Prezzo
Col tasto destro su una qualsiasi riga dell'analisi sarà anche possibile Stamparla o Esportarla in Excel

## Stampa Variazioni Prezzo

Questa funzione permette la Stampa dell'Elenco delle Variazioni Prezzo e/o la Stampa delle Etichette degli Articoli che hanno subito una variazione di Prezzo. Selezionare la riga dell'Analisi interessata e premere Invio. A questo punto si aprirà una finestra divisa in tre diversi Pannelli : 

**Selezioni di Stampa**

Vengono richieste informazioni generiche utilizzate sia per la Stampa dell'Elenco, che per la Stampa delle Etichette

 * Stampa Nuovi Prezzi SI/NO. Indicando NO a questa richiesta verranno esclusi gli Articoli per i quali è stato attribuito per la prima volta un Prezzo di Vendita.
 * Stampa Solo Articoli in Giacenza SI/NO
 * Codice Negozio per Verifica Giacenza. Questo dato è obbligatorio nel caso si sia impostato SI alla richiesta Stampa Solo Articoli in Giacenza o alla richiesta Stampa Etichette

**Informazioni per Stampa Elenco**

 * Stampa Elenco Differenze SI/NO
 * Template. E' possibile indicare eventualmente il nome di un Template precedentemente salvato con la funzione generica delle stampe di Negoziando
 * Altre selezioni (oltre Template) SI/NO

**Informazioni per Stampa Etichette Articoli in Giacenza**

Vengono proposte le normali informazioni richieste in tutti i punti di Negoziando in cui è possibile stampare le etichette articolo e cioè : 

 * Stampa Etichette SI/NO
 * Stampante da Utilizzare
 * Stampa Prezzi di Vendita SI/NO
 * Codice Listino
 * Codice Tipo Etichetta
 * Modalità di Utilizzo dell'Etichetta specificata
 * Destinatario Etichetta. Richiesta visibile solo nel caso in cui sia attiva questa gestione
E' da tenere presente che le etichette verranno stampate nella quantità relativa alla Giacenza per Articolo/Colore/Taglia.

## Schedulazione

Col tasto F9 è possibile schedulare in Negoziando Info Center la Creazione automatica dell'Elenco delle Variazioni Prezzo.
VEDI NEGOZIANDO INFOCENTER
Oltre alla Creazione dell'Elenco è possibile schedularne eventualmente anche la Stampa.

Prima di effettuare la schedulazione è necessario aver memorizzato almeno le Impostazioni per la Creazione dell'Elenco.
(Le Impostazioni andranno memorizzate anche per la Stampa, se si intende schedularla).
**Per memorizzare le Impostazioni di Creazione Elenco : **

 * Premere F6 Crea Elenco Variazioni
 * Definire i Valori di Selezione
 * Premere Tasto Destro sulla Barra del Titolo della Finestra di Creazione Elenco Variazioni Prezzo
 * Selezionare Gestione Impostazioni e poi Salva con Nome

**Per memorizzare le Impostazioni per la Stampa dell'Elenco : **

 * Premere Invio Stampa Variazioni Prezzo
 * Definire i Valori di Selezione
 * Premere Tasto Destro sulla Barra del Titolo della finestra
 * Selezionare Gestione Impostazioni e Salva con Nome
Nel caso di Schedulazione della Stampa che prevede la Stampa dell'Elenco occorrerà definire obbligatoriamente il nome del Template di stampa.

Dopo aver premuto il tasto di Schedulazione, compilare la richiesta iniziale con i Codici di Impostazione richiamabili col Tasto F1 posizionandosi sul campo giallo. La funzione prosegue con le normali
richieste delle Schedulazioni di Info Center.

## Tabella Stampa Frontalini

Con la Funzione in oggetto è possibile creare un Archivio per la Stampa dei Frontalini, richiamabile poi da Principale>Anagrafiche di Base>Stampa Anagrafiche di Base>Stampa Frontalini da Archivio
Premere il Tasto F8 Crea Tabella Stampa Frontalini dopo essersi posizionati sulla riga di interesse e al termine dell'Elaborazione apparirà un messaggio che riporta il Numero di Riferimento dell'Archivio appena generato.


