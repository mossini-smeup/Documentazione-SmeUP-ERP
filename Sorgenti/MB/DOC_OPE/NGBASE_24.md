# Gestione Distinta Base

## Gestione Distinta Base

## Premessa

Una distinta base è l'elenco di tutti i componenti necessari per realizzare un prodotto.
Considerando come esempio una bicicletta, i suoi **figli** nella distinta base sono il telaio, la sella, il manubrio e le ruote. A sua volta il componente telaio potrebbe essere composto da un tubo di alluminio, ad un livello ancora inferiore. Esiste quindi un legame, detto legame **padre-figlio**, che collega insieme ogni articolo con il suo componente. I prodotti finiti non hanno mai padri, i componenti di acquisto non hanno mai figli, e gli oggetti prodotti o assemblati dall'azienda hanno sempre figli.
In Negoziando andremo a gestire le Distinte Base utilizzate dal Conto Lavorazione

## Funzioni DIsponibili

In Negoziando sono disponibili le seguenti funzioni per la Gestione e le Analisi delle Distinte Base, dal _Menu>Principale>Gestione Distinta Base_ : 

 * Gestione Distinta Base
 * Duplicazione Distinta Base
 * Sostituzione di Massa Componenti Distinta Base
 * Inserimento di Massa Componenti Distinta Base
 * Generazione Articoli e Distinta Base per Varianti
 * Aggiornamento Distinta Base con Varianti
 * Riallineamento Distinta Base
 * Generazione Movimenti di Magazzino da Articoli di Produzione
 * Esplosione/Implosione Distinta Base
 * Analisi Scheda Costo Distinta Base
 * Aggiornamento Costi Distinta Base

## Gestione Distinta Base

La funzione permette di definire gli Articoli che compongono la Distinta Base.
Prima di cominciare a popolare la Distinta Base bisogna inserire in anagrafica sia il prodotto finito (Bicicletta), che tutti i vari componenti (Ruota, Sellino, etc..)

- [Gestione Anagrafica Articoli](Sorgenti/MB/DOC_OPE/NGBASE_25)

Dal _Menu>Principale>Gestione Distinta Base>Gestione Distinta Base_ viene richiesto inizialmente di indicare l'articolo per il quale definire la distinta, che, nel nostro caso, sarà la bicicletta
(Questa stessa funzione può essere richiamata anche direttamente dalla Gestione Anagrafica Articoli)
Dopo aver confermato apparirà una schermata con i soliti tasti funzionali di Negoziando. Premere F6 Inserisci per aggiungere tutti i componenti che formano l'articolo inserito prima. Verrà richiesto di indicare : 

 * Sequenza. Sarà l'ordine in base al quale verranno elencati a video i vari componenti. Deve essere univoca nell'ambito della distinta
 * Articolo. Codice Articolo del Componente
 * Coefficiente di Impiego. La Quantità che verrà utilizzata per arrivare al prodotto finito
 * Data Inizio/Fine Validità
 * Costo Unitario
 * Valuta Costo
 * Unità di Misura
 * % Sfrido. Rappresenta la percentuale di scarto della lavorazione del materiale

## Duplicazione Distinta Base

Dal _Menu>Principale>Gestione Distinta Base>Duplicazione Distinta Base_ è possibile Copiare la Distinta Base di un Articolo, attribuendola ad un altro. Nella maschera principale verrà richiesto di indicare : 

 * Articolo di Riferimento. L'Articolo con la Distinta Base che si intende Duplicare
 * Articolo per Generazione Distinta. L'Articolo al quale verrà attribuità la Distinta duplicata

Confermare e attendere la notifica di avvenuta duplicazione

## Sostituzione di Massa Componenti Distinta Base

Con la funzione in oggetto è possibile sostituire in una volta sola un Componente contenuto in più Distinte Base. Dal _Menu>Principale>Gestione Distinta Base>Sostituzione di Massa Componenti Distinta Base indicare il Componente da Sostituire e premere Invio
A questo punto il sistema visualizzerà l'elenco di tutte le DB che contengono quel Componente. Sarà possibile : 

 * F2 Selezionare Tutto
 * F3 Deselezionare Tutto
 * F9 Selezionare un Record

Dopo aver confermato la scelta, apparirà la Richiesta del Nuovo Componente che andrà a Sostituire il precedente. Dopo aver premuto Invio, apparirà una Notifica che riporta quali DB verranno aggiornate col Nuovo Componente. Confermare per Continuare, altrimenti premere Esc.

## Inserimento di Massa Componenti Distinta Base

Dal _Menu>Principale>Gestione Distinta Base>Inserimento di Massa Componenti Distinta Base_ è possibile aggiungere dei Componenti alla Distinta
Viene richiesto di indicare il Codice Articolo del Padre, che non deve essere a sua volta un componente di una DB.
Premere F9 per Selezionare l'Articolo al quale si vogliono aggiungere dei Componenti e confermare con F6

## Generazione Articoli e Distinta Base per Varianti

In caso di Articoli Taglia/Colore è possibile, con la funzione in oggetto, generare in automatico dei Nuovi Articoli. Se volessimo creare delle Biciclette per Uomo/Donna/Bambino e di colori differenti, come prima cosa dovremmo entrare in Anagrafica Articoli (vedi manuale) e aggiungere taglie e colori.
Nel nostro caso all'articolo Bici aggiungeremo la taglia Baby, ad esempio, e i colori rosa e blu.
A questo punto dal _Menu>Principale>Gestione Distinta Base>Generazione Articoli e Distinta Base per Varianti  viene richiesto l'Articolo Taglia/Colore per il quale effettuare la generazione dei Nuovi Articoli e delle loro Distinte.
E' possibile procedere all'elaborazione di più articoli contemporaneamente utilizzando i Filtri della schermata di Selezione iniziale. Dopo la selezione del Filtro iniziale vengono elencati gli Articoli da generare.
Nel Pannello superiore viene riportato il numero degli Articoli da Generare,di quelli Esclusi dall'Utente e di quelli Esclusi per Anomalie
Per la determinazione del Nuovi Codici Articolo da generare il programma utilizza i valori definiti nella Configurazione di Negoziando (vedi annotazioni successive)
Premere F7 o F8 per Includere/Escludere dalla generazione dei nuovi articoli le combinazioni di Colore/Taglia interessate.
(F7Includi/Escludi Riga - F8 Includi/Escludi Gruppo)
Premere F5 per Visualizzare i componenti della Distinta Base dell'Articolo selezionato inizialmente
Premere F6 per procedere alla generazione dei Nuovi Articoli.
La funzione di generazione potrà essere riutilizzata nel caso venga modificata la combinazione Colore/Taglia
La Colonna Articolo da Generare rappresenta il Codice degli Articoli Nuovi

## Aggiornamento Distinta Base con Varianti

Questa funzione può essere utilizzata per effettuare modifiche alla composizione delle Singole Distinte Base dopo aver effettuato la Generazione Articoli per Varianti. E' naturalmente possibile utilizzare la funzione di Gestione Anagrafica Articoli per effettuare le stesse modifiche.
Dal _Menu>Principale>Gestione Distinta Base>Aggiornamento Distinta Base con Varianti_ viene richiesto inizialmente l'articolo per il quale si intende modificare la Distinta Base
Confermando la selezione viene preparata una griglia (in alto a destra l'elenco degli Articoli generati dalla funzione specifica, a sinistra i Componenti di ciascuna distinta) da utilizzare per l'aggiornamento delle Quantità
E' possibile inserire nella Distinta una nuova combinazione Sequenza/Componente con il tasto F6
Verrà richiesto di indicare un Codice Sequenza e un Articolo. A conferma avvenuta l'Articolo verrà inserito nella griglia.
E' anche possibile modificare le Quantità della Singola Cella con un doppio clic. Il Tasto F7 Aggiorna Costo permette di Modificare il Costo Unitario del Singolo Componente.
Al termine dell'indicazione delle Quantità (e degli eventuali nuovi componenti) premere F9 per procedere all'aggiornamento delle singole Distinte Base.

## Riallineamento Distinta Base

Questa funzione serve a riallineare le singole Distinte Base degli Articoli creati con l'apposita funzione di Generazione Articoli per Variante alla Distinta Base dell'Articolo principale (nel caso, ad esempio, sia stato aggiunto un componente alla Distinta Base principale o siano state effettuate modifiche alle singole Distinte Base degli articoli esplosi).
Dal _Menu>Principale>Gestione Distinta Base>Riallineamento Distinta Base_ viene richiesto inizialmente di selezionare l'Articolo da elaborare
Vengono successivamente indicati gli articoli che compongono la Distinta Base con i vari coefficienti di impiego. In rosso verranno evidenziate le righe che presentano differenze, che saranno visibili sotto la Colonna Descrizione Anomalia.
Premendo F6 Dettaglio Sequenze è possibile visualizzare nel Dettaglio le differenze tra le composizioni delle varie Distinte Base.
Premendo F7 Riallinea Sequenza si può procedere al riallineamento di un singolo componente.
Premendo F8 Riallinea Distinta Base si può procedere al riallineamento di tutti i componenti.

## Generazione Movimenti di Magazzino da Articoli di Produzione

Questa funzione permette di generare Movimenti di Magazzino sull'Articolo principale a partire dai Movimenti di Carico degli articoli di Produzione
Qui entra in gioco il Conto Lavorazione (VEDI CAPITOLO GESTIONE CONTO LAVORAZIONE)
Gli Articoli di Produzione (Es. Ruote, Sella, etc) vengono inviati ad un Terzista che dovrà assemblare gli Articoli Figli (es. Bici Blu Bambino). Quando gli Articoli Figli rientreranno dal Conto Lavorazione e verranno caricati in Magazzino, saranno tutti riassociati all'Articolo Padre, quindi alla Bici, nel nostro esempio (questo significa che quando verrà venduta una Bicicletta Blu da Bambino, a Magazzino verrà movimentato l'Articolo BICI nella Variante Blu/Bambino)
_Dal Menu>Principale>Gestione Distinta Base>Generazione Movimenti di Magazzino da Articoli di Produzione viene richiesto inizialmente di indicare il Codice Fornitore, ovvero il Terzista che sta assemblando il Prodotto. Confermare e successivamente verranno elencati tutti i Movimenti di Magazzino relativi agli articoli di Produzione ancora da elaborare
Premendo F5 Visualizza Dettaglio è possibile vedere in Dettaglio il Movimento selezionato.
Col Tasto F8 Da Elaborare/Tutti si possono Visualizzare anche tutti i Carichi già Elaborati
Premere F6 Genera Movimenti per Caricare la Merce a Magazzino
Viene richiesta inizialmente conferma e, al termine dell'elaborazione, viene data segnalazione del nuovo movimento di Magazzino generato.

La procedura di generazione dei Movimenti genera 2 movimenti di Magazzino : 

 * Uno per lo Scarico degli Articoli di Produzione (ex :  E.BICI.BLU.BIMBO)
 * Uno per il Carico dell'Articolo principale (ex :  EDB_BICI - Colore BLU - Taglia BIMBO)

**Per la generazione di tali movimenti di Magazzino è necessario definire nella Configurazione di Negoziando il Tipo Documento e le Causali da utilizzare (vedi annotazioni successive)

## Esplosione/Implosione Distinta Base

La funzione permette di analizzare le composizioni delle Distinte Base valutando eventualmente la disponibilità degli Articoli necessari alla Produzione dell'Articolo Finito
_Dal Menu>Principale>Gestione Distinta Base>Esplosione/Implosione Distinta Base_. All'attivazione della funzione vengono richiesti : 

 * Codice Articolo
 * Tipo Richiesta che potrà essere : 
 ** Esplosione Singolo Livello. Viene visualizzata la Composizione dell'Articolo Padre. Se viene impostato il Campo Quantità Richiesta, il Sistema calcolerà quanti Pezzi mi occorrono per creare Tot. Articoli
 ** Esplosione a Scalare. Se anche un Componente ha a sua volta una Distinta Base, vedrò anche tutta la sua Composizione
 ** Implosione a Scalare. E' il processo inverso, quindi indicherò il Codice Articolo di un Componente
 ** Implosione Singolo Livello
 * Disponibilità. Indicare SI se si intende avere informazioni riguardo la Disponibilità degli articoli. In questo caso, dopo aver dato Conferma, verrà richiesto di indicare (facoltativamente) la Quantità Richiesta di riferimento

Vengono sempre visualizzati : 
Livello/Articolo/Descrizione/Coefficiente di Impiego/Unità di Misura/ Quantità Totale.
La **Quantità Fattibile** viene visualizzata solo se indicato Si alla richiesta iniziale sulla Disponibilità
La **Quantità Totale Richiesta** e le **Quantità Mancanti** vengono visualizzate solo se è stato indicato un valore nella richiesta iniziale della Quantità Richiesta e sono condizionate a tale
valore.
Se si stanno analizzando le Disponibilità, il programma visualizza nella schermata iniziale le Quantità relative alla Disponibilità (Giacenza - Impegnato) e vengono messi a disposizione i tasti
funzionali F8 e F9 per visualizzare i valori specifici della Giacenza o dell'Impegnato.
E' sempre disponibile il tasto funzionale F5 per stampare l'elenco visualizzato.

## Analisi Scheda Costo Distinta Base

Questa funzione permette di analizzare i Costi complessivi di articoli che hanno una Distinta Base.
All'attivazione della funzione dal _Menu>Principale>Gestione Distinta Base>Analisi Scheda Costo Distinta Base vengono richiesti : 

 * Codice Negozio (per la determinazione del Prezzo di Vendita)
 * Codice Articolo
 * Tipo Richiesta che potrà essere : 
 ** Esplosione a Scalare
 ** Esplosione Singolo Livello
 * Valuta da utilizzare per la visualizzazione degli Importi

 * Informazioni per la Valorizzazione. E' possibile decidere come Valorizzare il Costo della Distinta Base, secondo un Valore Primario e, volendo, uno Secondario ed è possibile scegliere  tra
 ** Costo Standard
 ** Costo Medio
 ** Costo Medio Ponderato
 ** Listino di Vendita
 ** Listino d'Acquisto

Se viene indicato un Listino, verrà poi richiesto il Codice e il Tipo Prezzi : 
 * Normale
 * Promozionale
 * Entrambi

L'elenco degli articoli è ordinato (e raggruppato) in base alle impostazioni definite nella Configurazione di Negoziando (vedi annotazioni successive).
Per la determinazione del Costo Unitario viene utilizzato (se presente) il valore indicato nella Gestione della Distinta Base, in caso contrario il Costo viene determinato sulla base delle informazioni di selezione iniziale (Pannello Valorizzazione).
Premere F7 per stampare la Scheda Costo.
N.B. Nella Stampa della Scheda verrà eventualmente stampata (se disponibile) anche l'Immagine del Prodotto.

Una volta indicati i valori richiesta viene visualizzata la Scheda Costi dell'articolo selezionato.

## Configurazione di Negoziando

Per utilizzare le funzioni di gestione della Distinta Base occorre impostare la Configurazione di Negoziando dal _Menu>Utilità>Configurazione>Gestione Configurazione Applicativa>Gestione Articoli>Pannello Distinte Base

Verranno richiesti : 

 * Gestione Distinta Base. Indicare SI
 * Consenti Qta Componenti a Zero. Valore che riguarda più che altro il settore Alimentare

Tra le Informazioni per Generazione Articoli e Distinte Base per Varianti indicare : 

 * Prefisso per Nuovi Articoli da Generare
 * Usa Codice Articolo Origine da Posizione
 * Numero Caratteri Articolo Origine da Utilizzare
 * Tipo Esplosione per Varianti
 ** Esplicita. I nuovi codici conterranno Colore/Taglia
 ** Progressivo. I nuovi Codici saranno seguiti da 001,002,003 etc..
 * Carattere di Separazione tra Articolo/Colore/Taglia. Esempio :  nel caso di Generazione Articoli a partire da EDB_GIACCA Colori BLU/NER Taglie 41/42, se utilizzassimo il Punto come Carattere di Separazione, avremmo questi nuovi codici : 
E.GIACCA.BLU.41 - E.GIACCA.BLU.42 - E.GIACCA.BLU.43 etc
 * Generazione Codici a Barre Automatici SI/NO
 * Codice Marchio per Generazione Automatica. Dalla Tabella MARC - Marchi
 * Codice Stato da Attribuire ai Nuovi Articoli. Dalla Tabella SART - Stato Articolo

Tra le Informazioni per la Generazione Movimenti di Magazzino : 

 * Tipo Documento di Magazzino. Dalla Tabella TDMA
 * Causale per Scarico Articoli di Produzione. Tabella CAMA - Causali di Magazzino
 * Causale per Carico Articoli gestiti a Taglia/Colore. Tabella CAMA - Causali di Magazzino

 * Tipo Ordinamento per Stampa Scheda Costo. E' possibile scegliere tra diversi Valori


