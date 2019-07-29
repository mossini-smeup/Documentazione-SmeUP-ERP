# Alcuni esempi di utilizzo
Mostriamo ora degli esempi di interrogazione.

## Analizzare le variazioni trimestrali di fatturato in una regione
Primo per selezionare i dati da analizzare applichiamo un filtro per "Dati geografici" / "Codice regione" e assegnamo (AND) il codice 03 = Lombardia

![V5STAT_012](http://localhost:3000/immagini/MBDOC_OPE-V5STAT_09/V5STAT_012.png)
Dopo aver impostato il filtro, è possibile interrogare la scheda per "Andamento nel tempo" > "Importo netto".

Una volta entrati è possibile scegliere il tipo di valore della vista che si vuole visualizzare, in questo caso l' "Importo netto" e quindi impostare il resto delle condizioni di interrogazione in questo modo : 
 * come parametro verticale :  anno
 * come parametro orizzontale :  trimeste

![V5STAT_029](http://localhost:3000/immagini/MBDOC_OPE-V5STAT_09/V5STAT_029.png)
Selezionando come "Valore" l'"Aumento - percentuale su precedente - Importo netto" otteniamo le variazioni percentuali : 
![V5STAT_030](http://localhost:3000/immagini/MBDOC_OPE-V5STAT_09/V5STAT_030.png)
## Interrogare il fatturato in lobardia di aprile 2009 per cliente
Impostiamo il filtro con periodo = 200904 e regione = 03 (Lombardia) : 

![V5STAT_031](http://localhost:3000/immagini/MBDOC_OPE-V5STAT_09/V5STAT_031.png)
Utlizziamo l'Analisi di Pareto" e selezioniamo con asse l'"ente intestatario" e come valore l'"Importo netto", in questo modo si ottiene un  report del fatturato ordinato per cliente in ordine discendente : 

![V5STAT_032](http://localhost:3000/immagini/MBDOC_OPE-V5STAT_09/V5STAT_032.png)
## Visualizzare i margini per provincia / classe contabile articolo
Per analizzare il margine l'interrogazione più appropriata è :  "Analisi tabellare" per "Articolo/Ente".
Si impostino i seguenti parametri
 * Valore :  margine
 * Verticale :  cliente - provincia
 * Orizzontale :  articolo - classe contabile

![V5STAT_033](http://localhost:3000/immagini/MBDOC_OPE-V5STAT_09/V5STAT_033.png)
### Controllare la registrazione cui appartiene la riga con il massimo importo negativo nel 2009
Impostiamo il filtro per esercizio di competenza = 2009.

Usiamo l'"Analisi di pareto" con asse = "numero documento" e come valore = "Importo netto". A questo punto non resta che ordinare in modo crescente la colonna del valore, così da avere gli importi negativi in alto alla matrice : 

![V5STAT_034](http://localhost:3000/immagini/MBDOC_OPE-V5STAT_09/V5STAT_034.png)
Per vedere il dettaglio di questo importo negativo, è necessario fare un doppio click sulla riga relativa : 
![V5STAT_035](http://localhost:3000/immagini/MBDOC_OPE-V5STAT_09/V5STAT_035.png)
In questo modo, è possibile, come da immagine, vedere il dettaglio delle righe riferite ai documenti che compongono questo fatturato negativo.
