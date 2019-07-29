# Scopo
 * Fornire agli acquisti una visione immediata dello stato di abilitazione del fornitore per l'articolo in oggetto;
 * Calare l'abilitazione fino al livello di modifica controllato;
 * Offrire un supporto immediato per la modifica degli indici statici;
 * Fornire al Collaudo e Controllo Qualità lo stato di abilitazione del fornitore;
 * Gestire le prime forniture, le forzature e i Free Pass;
 * Gestire gli accordi presi coi fornitori, i cicli personalizzati e la stampa diretta della griglia di collaudo con l'ordine di fornitura;
 * Gestire il centro di lavoro interno come fosse un fornitore.

# Definizioni
 * Classe di Abilitazione (Fornitore); il concetto di classe di abilitazione è strettamente legato a quello di classe funzionale dei prodotti. I prodotti sono classificati e raggruppati in base alla loro importanza in "classi funzionali". Un fornitore, in funzione del livello tecnologico acquisito, della sua esperienza, dell'affidabilità dimostrata, viene abilitato alla fornitura di prodotti appartenenti ad una determinata classe funzionale, assegnandolo ad una "classe di abilitazione".
Sostanzialmente, quindi, la classe di abilitazione specifica quali classi funzionali di prodotto un fornitore è in grado di fornire.
 * Classe Funzionale (Prodotto); i prodotti sono classificati e raggruppati a seconda che siano componenti di sicurezza, critici, importanti, normali, ecc.. in "classi funzionali".

# Tabelle utilizzate dal modulo : 
### CQQ - CLASSE FUNZIONALE DEL PRODOTTO
Controllare le classi funzionali dei prodotti ripresi dal DATABASE aziendale mediante il programma definito nella tabella di personalizzazione CQ1. Ad ogni articolo deve essere assegnata la classe funzionale, che rappresenta l'importanza dell'articolo riferita all'utilizzo dello stesso. (es. Un articolo di sicurezza avrà classe funzionale "Critica" etc.).
In questa tabella deve obbligatoriamente essere presente l'elemento '**' generico.
 :  : DEC T(ST) K(CQQ)

### CQV - CLASSE DI ABILITAZIONE DELL'ENTE FORNITORE
Controllare le classi di abilitazione alla fornitura di un articolo di una certa CLASSE-FUNZIONALE riprese dal DATABASE aziendale mediante il programma definito nella tabella di personalizzazione CQ1.
 :  : DEC T(ST) K(CQV)

### CQ1 - TABELLA DI PERSONALIZZAZIONE 1
Questa tabella, contiene alcune scelte di personalizzazione dell'applicazione. Con tali scelte si può condizionare il modo di esecuzione dei programmi.
 :  : DEC T(ST) K(CQ1)

### DIP - PERSONALE ANAGRAFICA-DIPENDENTI
Codifica le matricole dei dipendenti.
  :  : DEC T(ST) K(DIP)

### *CNTT CODICI OGGETTI APPLICATIVI
Descrive il tipo di enti che richiedono, gestiscono, evadono,ecc.. l'Audit.
  :  : DEC T(ST) K(*CNTT)

# Processo di avviamento ed utilizzo
## Attività iniziale
 * Inserimento tabelle
 * Classificazione tipologie
 * Inserimento dati identificazione fornitori
 * Definizione indici valutazione fornitore
 * Inserimento dati prima fornitura

## Attività periodica
 * Registrazione nuovi prodotti
 * Modifiche alle classi di abilitazioni impostate
 * Modifiche alle condizioni di fornitura impostate
