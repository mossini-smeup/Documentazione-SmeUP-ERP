## Costruzione Ciclo Ordine di Produzione

Costruisce il ciclo effettiva di un ordine di produzione attraverso i movimenti di versamento di magazzino dell'ordine e le dichiarazioni di attività sulle sue fasi del suo ciclo.
Il tipo ciclo può essere intestata all'ordine di produzione o al lotto.
Poichè a standard Smeup l'ordine di produzione corrisponde al lotto, la modalità di costruzione non cambia.
L'unica differenza è che nel primo caso il ciclo ha come codice l'ordine di produzione, mentre nel secondo caso ha come codice il lotto.
I tempi di ciasune fase sono la media sul totale versato, di tutti le dichiarazioni sulla fase stessa.

>La costruzione del ciclo d'ordine segue la seguente logica : 
 * Calcolo il totale versato attraveso i movimenti di magazzino
 ** Verifica tutti i versamenti di prodotti dichiarati buoni interni _9_(Movimenti VP che hanno l'ordine in S§NR01)
 ** Verifica tutti i versamenti finali di prodotti dichiarati buoni esterni _9_(Movimenti VE che hanno l'ordine in S§NR02 e S§FLG1<>'3')
 * Informazioni ciclo dell'ordine
 ** Legge il ciclo dell'ordine per determinare alcune informazione che non esistono  sulle attiivtà oppure  non sono attendibili.
 * costtruzione ciclo
 ** Verifica tutte le attività dichirate di produzione_9_(Attività VP che hanno l'ordine in W§NDOC  W§FLG1<>" ").
 ** Per le lavorazioni esterne calcola l'eventuale costo in valuta corrente del ciclo (W§TE09)  dal valore presente  sull'attività (W§VAL1)
 ** per ciascuna fase totalizza i suoi tempi in funzione del suo significato.  Dal flag del tipo tempo.
 ** determina il ciclo medio dividendo i tempi di ciacuna fase per il totale versato
 * Ciascuna fase può essere spezzata in più fasi in funzione del periodo in cui è stata dichiarata.
  Il periodo può essere l'anno o il mese. Con questa suddivisione è possibile costificare una   stessa fase con aliquote  diverse in funzione del periodo di dichiarazione.

