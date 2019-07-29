## Obiettivo
L'obiettivo della schermata della lista scadenze è quello di visualizzare e modificare le scadenze relative ad una registrazione contabile.

## Formato lista
All'interno del formato lista viene presentato l'elenco delle scadenze associate alla registrazione contabile.

![C5D010_018](http://localhost:3000/immagini/MBDOC_OGG-P_C5RR01L/C5D010_018.png)
In prima battuta le scadenze vengono generate analizzando il codice pagamento presente in testata; è, in ogni caso, possibile modificare date, importi e tipologie di pagamento a proprio piacimento avendo l'accortezza di rispettare la corrispondenza tra importo indicato all'interno della registrazione contabile e somma degli importi delle singole rate.
All'interno del formato lista per ogni rata sono riportate le seguenti informazioni : 
 * Data scadenza
 * Numero e data documento
 * Importo rata
 * Segno rata
 * Tipo pagamento
 * Specifica dell'eventuale blocco presente sul pagamento
Nella parte alta della scheda è possibile visualizzare alcune informazioni relative alla registrazione contabile come il numero e la data registrazione, l'ente intestatario, l'importo della registrazione, le informazioni relative al documento e al protocollo.

### Opzioni
Per le rate visualizzate nel formato lista sono disponibili le seguenti opzioni : 
 * 02 Modifica. Permette di accedere al formato dettaglio e modificare la rata
 * 03 Copia. Permette di accedere al formato dettaglio e copiare la rata
 * 04 Cancellazione. Permette di accedere al formato dettaglio e cancellare la rata
 * 05 Interrogazione. Permette di accedere al formato dettaglio e visualizzare la rata
 * RS Recupero residuo. Nel caso in cui si chiuda una parte della scadenza è possibile utilizzare questa opzione per ottenere la creazione di due rate distinte :  una rata corrispondente alla parte pagata che non sarà più modificabile e una rata corrispondenmte alla parte ancora da saldare che sarà possibile gestire con le solite opzioni.
 * NO Gestione note. Permette di accedere alla gestione note delle rate.
 * VB Visualizza protezione rate. Nel caso in cui le rate non siano modificabili attraverso questa opzione è possibile visualizzare il motivo del blocco.
 * VP Visualizza protezione righe. Nel caso in cui le righe non siano modificabili attraverso questa opzione è possibile visualizzare il motivo del blocco.

### Tasti funzionali
All'interno del formato lista sono disponibili i seguenti tasti funzionali : 
 * F05 :  Rivisualizzazione. Aggiorna la schermata.
 * F06 :  Aggiorna. Conferma la schermata con le eventuali modifiche apportate.
 * F07 :  Immissione. Permette di immettere una nuova scadenza visualizzandone il formato dettaglio
 * F19 :  Valuta conto. Permette di visualizzare gli importi delle rate nella valuta del conto.
 * F21 :  Rigenera rate. Permette di ricreare le rate leggendo il codice pagamento presente in testata; quindi nel caso in cui vengano apportate modifiche alle scadenze, selezionando questo tasto e confermando l'azione si avrà l'annullamento delle modifiche apportate.

## Formato dettaglio
Il dettaglio di una rata contabile si presenta nel seguente modo : 
![C5D010_019](http://localhost:3000/immagini/MBDOC_OGG-P_C5RR01L/C5D010_019.png)Al suo interno è possibile visualizzare le seguenti informazioni : 
 * Segno rata
 * Tipo pagamento
 * Data scadenza
 * Blocco impostato
 * Importo rata in valuta
 * Importo rata in euro
 * Importo in pagamento :  questo campo viene compilato nel caso in cui una scadenza o parte di essa venga inclusa in una distinta non ancora contabilizzata.
 * Forzature eventualmente presenti :  attraverso questo campo viene messo in evidenza il fatto che la rata sia o meno una rata di abbuono.
 * Importo pagato in valuta :  evidenzia la parte saldata della scadenza.
 * Importo pagato in euro
 * Divisa e cambio di riferimento
 * Banca aziendale di presentazione del pagamento con relativo rapporto bancario :  la compilazione di questi campi è importante nel caso in cui per lo specifico pagamento abbia rilevanza la banca aziendale come ad esempio un pagamento a fornitore con Ri.Ba.
 * Data e numero documento
 * Dati relativi alla pratica in cui la scadenza è inclusa
 * Informazioni relative al responsabile del credito
 * Informazioni relative alla banca dell'ente su cui viene appoggiato il pagamento :  la compilazione di questi campi è importante nel caso in cui per lo specifico pagamento abbia rilevanza la banca dell'ente come ad esempio un pagamento a fornitore con bonifico o un pagamento di un cliente con Ri.Ba.
 * Informazioni relative all'eventuale cessione del credito
