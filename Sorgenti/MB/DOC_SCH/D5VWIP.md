# Scheda Valorizzazione WIP

## CONSIDERAZIONI GENERALI
Il wip calcolato in questa scheda si può considerare un WIP standard per quanto riguarda i costi ed effettivo per quanto riguarda le quantità. E' calcolato nel modo seguente.
Vengono letti TUTTI gli ordini di produzione attivi e per quelli chiusi viene controllata (tramite £G20) l'ultima data di movimentazione magazzino e attività.
Per ogni ordine (è prevista una exit per l'eventuale omissione di alcune tipologie di ordine) viene letto il ciclo e recuperate TUTTE le attività di avanzamento fase (ovviamente alla data), vengono
considerate anche le quantità di scarto, e recuperati TUTTI i movimenti di versamento (VP interni e VE esterni) magazzino.
Viene calcolato il residuo alla data di ogni singola fase con lo schema come segue : 

  Quantità In Ordine :  1000
>.                 prodotti  Buoni     Scarti    Esistenza
.       Fase 1                950         50            0
.       Fase 2                950                     450
.       Fase 3                500        100          150
.       Fase 4                250                       0
.       Fase 5                250                       0

  Versato a Magazzino 250


La valorizzazione del WIP quindi sarà
 * 450 alla fase 2
 * 150 alla fase 3

Trovate  le quantità ci resta la valorizzazione, che a questo punto dovrà essere fatta utilizzando un costo precedentemente memorizzato.
Qui ci sono 2 opzioni :  un costo articolo alla fase o un costo "ordine di produzione" alla fase.
La seconda scelta è preferibile in quanto si ha la certezza di valorizzare tutte le fasi,nel primo caso si può incorrere in costi mancanti nel caso di fasi "extraciclo" standard.
E' prevista anche qui una exit per sistemare i valori

Ricapitolando per ottenere un buon risultato è necessario avere una dichiarazione di avanzamento produzione puntuale sia come attività produttive (P5ATTI0F) che di versamenti di magazz. (GMMOVI0F)

Da notare che è previsto il caso in cui la cronologia delle dichiarazioni (o della effettiva effettuazione della stessa) di avanzamento. Il programma gestisce con il calcolo sopra spiegato, anche delle giacenze (di wip) negative rendendo la somma della giacenza wip dell'ordine corretta, anche se esteticamente non bello.

## PREREQUISITI
 * Gestione della tabella D5X
 * Creazione contesto nella tabella D5S con elemento TAD5X
 * Creazione Sottosetotre £3 della tabella D5O , e l'elemento WIP (vedere da standard)
 * Sottosettore igi£3 e relativi elementi
 * Costo alla fase di articolo o ordine di produzione

## Formato principale

![D5BASE_21](http://localhost:3000/immagini/MBDOC_SCH-D5VWIP/D5BASE_21.png)