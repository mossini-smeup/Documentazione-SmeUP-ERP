## Flussi di creazione e gestione Piano
L'MPS è una tipica applicazione batch per l'elaborazione di masse di dati, quindi gran parte delle funzioni MPS sono batch che in genere creano, modificano o cancellano viste in base a parametri di elaborazione e ad altri dati contenuti negli archivi che alimentano l'MPS oppure in altre viste piano.

### Funzioni ingresso da altre applicazioni
In questo gruppo sono comprese tutte le funzioni che creano viste piano partendo da applicazioni esterne all'MPS.

* **Da calendario**
Dato un tipo risorsa per la quale il calendario è definito, permette di scrivere, su delle viste piano inserite nei parametri di elaborazione, dei valori scelti tra le seguenti possibilità : 
 ** capacità in ore
 ** numero giorni lavorativi
 ** capacità in quantità
 ** coefficiente di capacità orario medio
 ** numero giorni effettivi
 ** numero di risorse
 * **Da calendario partendo da vista**
Permette di scrivere su delle viste piano inserite nei parametri di elaborazione e, a fronte delle risorse presenti nella vista piano di riferimento, dei valori scelti tra le seguenti possibilità : 
 ** capacità in ore
 ** numero giorni lavorativi
 ** capacità in quantità
 ** coefficiente di capacità orario medio
 * **Da flussi di cassa**
Scrive sulla vista piano inserita nei parametri di elaborazione i dati letti dall'applicazione dei flussi di cassa a fronte dello scenario in input.
 * **Da carico risorse interne**
Per il range di risorse definito nei parametri di elaborazione carica la vista inserita con i dati letti nel file degli impegni risorse.
 * **Da ordini produzione rilasciati**
Per gli ordini di produzione compresi nel range delle parzializzazioni, scrive nella vista in input il valore prescelto tra quelli disponibili nel periodo del piano corrispondente alla data scelta.
 * **Da documenti ciclo esterno**
Per i documenti del ciclo esterno (ordini acquisti / vendite, bolle entrata / uscita, ecc...) compresi nel range delle parzializzazioni scrive nelle viste in input (fino a 3) il valore prescelto tra quelli
disponibili nel periodi del piano corrispondenti alla data scelta.
 * **Da fatture ciclo esterno**
Per fatture attive o passive aventi uno dei valori del flag di fatturazione indicato in input (fino a 5 valori) ed escludendo i modelli documento o i tipi riga indicati (fino a 8), scrive nella vista piano in input, il valore prescelto nella valuta richiesta.
 * **Da previsioni**
Scrive sulla vista piano in input i dati compresi nelle parzializzazioni e letti nel file delle previsioni, per il tipo previsione prescelto.
 * **Da altro Piano/Vista**
Definendo piano e vista di origine, vista di destinazione e metodo di ripresa dati.
 * **Da analisi disponibilità**
La ripresa dati legge la disponibilità di un articolo data da un gruppo fonti.
Gli articoli su cui fare la disponibilità possono essere : 
 ** quelli presenti in una vista piano di riferimento
 ** da anagrafico materiali
 * **Da consigli MRP**
Può leggere da fonti esistenti o future e può scrivere fino a 3 viste MPS : 
 ** considerando la data fonte
 ** considerando la data suggerimento
 ** usando come valore la disponibilità proiettata
 * **Da movimenti di magazzino**
Selezionando il valore da riprendere per le causali di movimentazione in input (fino a 4) e per il range di date definito.
 * **Da piani diversi in base a data e metodo di ripresa**
Permette di scrivere prelevando le informazioni da più piani e viste piano.
Le informazioni vengono selezionate fino a una data limite, a partire da una data limite o nell'intervallo compreso tra 2 date.
La selezione dei piani e il trattamento delle date sono definiti nei metodi di ripresa : 
 ** da se stesso
 ** da piano specifico
 ** da ultimo piano con prefisso
 ** da tipo piano in base alla data

## Funzioni su piano
In questo gruppo sono comprese tutte le funzioni che agiscono su piani interi.
 * **Cancellazione piano/vista piano**
Cancella l'intero piano o la vista in input
 * **Definizione piano**
Crea un nuovo piano (costruisce la tabella MPP, prepara i record fissi del piano, cioè i record dove definire le date inizio / fine di ogni periodo e i numeri relativi) secondo i metodi definiti nei parametri di elaborazione.
 * **Stampa piano/viste batch**
Lancia in batch la stampa del piano secondo i parametri di stampa memorizzati nella memorizzazione multipla.
 * **Cancellazione piani precedenti**
Fissato il numero di piani da tenere in linea, elimina (eventualmente storicizzando e riorganizzando il file) tutti i piani precedenti.
 * **Cancellazione piano con limiti**
Data la memorizzazione dei criteri di cancellazione che possono essere impostati con la funzione di "Eliminazione Selettiva Dati Piano", con questa funzione si possono lanciare le cancellazioni in un flusso batch.
 * **Esecuzione flusso azioni batch**
Dato un gruppo di azioni batch definite in un sottosettore della tabella B£J e un elemento della tabella B£H che identifica il flusso (il gruppo di azioni da lanciare in sequenza), questa funzione lancia il flusso suddetto.

## Funzioni su viste piano
In questo gruppo sono comprese tutte le funzioni di modifica o ottenimento di una nuova vista, partendo da altre viste interne al piano in elaborazione : 
 * **Operazioni su due viste**
Permette di eseguire delle operazioni aritmetiche o logiche su 2 viste riportando il risultato su una terza.
 * **Totalizzazione di una vista**
Partendo da una vista avente 2 entità (codice 1 / codice 2), somma i valori a livello del codice 1 o del codice 2 e riporta il risultato della somma su una seconda vista (es. :  da una vista di quantità vendute per cliente / articolo, totalizza le quantità a livello cliente).
* **Creazione sintesi**
Crea una vista partendo da un'altra vista di maggior dettaglio e sommarizzando i valori per classificazioni degli oggetti presenti nella vista di partenza (es. :  partendo da una vista di totale venduto per articolo, si crea una vista di totale venduto per classe materiale).
I concetti e le funzioni di sintesi degli oggetti sono spiegati nello specifico documento (cfr. Sintesi degli oggetti).
- [Sintesi degli oggetti](Sorgenti/MB/DOC/C£SINT)

 * **Valorizzazione di una vista**
Dato un tipo costo / livello costo, valorizza le quantità degli articoli presenti nella vista di partenza e le memorizza nella vista di destinazione.
 * **Adeguamento dettaglio al totale**
È la funzione inversa a quella di creazione sintesi :  partendo da una vista di sintesi, crea una vista di dettaglio utilizzando una terza vista come indicatore per la distribuzione delle quantità (es. :  dalla vista dei volumi previsti per classe materiale, crea la vista dei volumi previsti per articolo utilizzando come confronto le vendite per articolo).
 * **Attribuzione parametri a una vista**
Crea una vista di destinazione intestata a un parametro selezionato in una categoria parametri associata a uno dei due codici della vista di partenza.
 * **Copertura in periodi di una vista rispetto all'origine**
Riporta sulla vista di destinazione i valori di copertura di una vista rispetto ad un'altra di confronto.
Tutte le 3 viste devono avere la stessa definizione (stesso codice 1 e stesso codice 2).
 * **Esplosione distinta**
Crea o aggiorna una nuova vista esplodendo quella di origine secondo una distinta base.
Metodo di esplosione, tipo distinta e applicazione dell'anticipo del lead time sono impostati nei parametri di elaborazione.
 * **Esplosione distinta con nettificazione**
E' simile alla funzione precedente, con in più la possibilità di nettificare le quantità esplose verso una vista di impegni e un gruppo fonti e anche di scrivere il risultato sulla vista di destinazione e nei consigli MRP (M5CONS0F) in uno scenario di consigli definito nei parametri di elaborazione.
 * **Esplosione ciclo**
Esplode una vista secondo un ciclo di produzione, memorizzando il risultato in una vista di destinazione. Il tipo ciclo, il tipo esplosione, la componente di carico da utilizzare e l'unità di misura sono definite nei parametri di elaborazione.
 * **Nettificazione giacenza**
Ottiene una vista di destinazione nettificando la vista origine con le quantità giacenti in un magazzino.
L'area giacenza e il tipo giacenza vengono definiti nei parametri di elaborazione.
 * **Nettificazione gruppo fonti**
E' come la funzione precedente, con la differenza che utilizza un gruppo fonti e che il netting può essere immediato o tempificato.
Tutte le 3 viste devono avere la stessa definizione (stesso codice 1 e stesso codice 2).
 * **Emissione suggerimenti**
Partendo dalla vista in input, questa funzione crea suggerimenti di pianificazione (M5CONS0F) nello scenario definito nei parametri di elaborazione.
 * **Esplosione risorse**
 * **Carico risorse a capacità finita**
Data una vista di capacità risorse e delle viste di carico risorse (a capacità infinita), segnala i superamenti di capacità in ore su opportune viste di segnalazione e crea delle nuove viste di carico (ore e quantità) livellate secondo la capacità risorse della vista iniziale.
 * **Elaborazione MRP**
 * **Applicazione regola a una vista**
Data una vista, le applica una regola selezionata tra quelle appartenenti a una categoria compatibile con la vista in input.
Le regole sono programmi specifici che, attraverso parametri di comportamento definiti nella tabella delle regole, possono elaborare i dati in input per ottenere dei risultati.
Per fare un esempio attinente alla gestione MPS, una regola potrebbe essere la segnalazione di quantità che superano dei valori predefiniti o ritrovabili da un'altra parte definita all'interno della regola (es. :  segnalazione di quando le nuove quantità ordinate superano o sono inferiori alla tolleranza di variazioni ammessa per un cliente).
