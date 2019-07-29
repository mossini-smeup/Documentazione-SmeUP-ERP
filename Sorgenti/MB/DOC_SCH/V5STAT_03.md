## Scheda Analisi di pareto

### Introduzione all'analisi di Pareto
Questa interrogazione permette di analizzare i dati del fatturato secondo il principio di Pareto.
Questo principio detto anche principio della scarsità dei fattori o chiamato "legge 80/20", è sintetizzabile nell'affermazione :  la maggior parte degli effetti è dovuta ad un numero ristretto di cause (considerando grandi numeri) e su questi fattori si deve concentrare l'attenzione. Naturalmente i valori 80% e 20% sono ottenuti mediante osservazioni empiriche e sono solo indicativi, ma è interessante notare come numerosi fenomeni abbiano una distribuzione statistica in linea con questi valori.
L'analisi di Pareto sta alla base della classificazione ABC che applicata al fatturato per cliente permette di classificare come classe A i clienti che concorrono alla formazione dell'80% del fatturato, come classe B i clienti che concorrono ad un altro 15% e come classe C il resto.

### Utilizzo della scheda
Per attivare l'analisi si devono scegliere : 
 * l'_2_asse :  si seleziona l'oggetto di riferimento del quale si vogliono rappresentare i valori (es. per cliente, per regione, per articolo, ecc....)
 * il _2_valore, che deve essere mostrato.

Facciamo un esempio :  partendo dalla sezione "Vendite Fatturato" si voglia analizzare il fatturato (importo netto) per regione.
Si sceglie nell'asse la regione e nel valore l'importo netto : 

![V5STAT_015](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_03/V5STAT_015.png)
### Presentazioni alternative
Nella sezione di destra della scheda possiamo avere diverse presentazioni dei dati relativi all'analisi di Pareto : 

 - _2_Base, è la visualizzazione di default (vedi figura precedente) in cui gli oggetti vengono presentati in ordine di valore decrescente
 - _2_Completa, rispetto alla visualizzazione base presenta anche altre informazioni (es. media, % sul totale, progessivo, % progressiva) inoltre viene rappresentato in forma grafica l'andamento dei valori

![V5STAT_016](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_03/V5STAT_016.png)
 - _2_Grafico, è la visualizzazione grafica del "base", sono previste diverse forme di presentazione, es. la rappresentazione a barre (default) e quella a torta

![V5STAT_021](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_03/V5STAT_021.png)
 - _2_Dettaglio, mostra la lista dei record dell'archivio statistiche che concorrono alla visualizzazione

![V5STAT_022](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_03/V5STAT_022.png)
### Pop-up
Il tasto destro del mouse su uno qualsiasi dei record attiva le funzioni di pop-up

![V5STAT_017](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_03/V5STAT_017.png)
- _2_Dettaglio, presenta i record di dettaglio che hanno originato il raggruppamento


- _2_Drill Down, aggiunge ai filtri anche il raggruppamento selezionato (in questo modo si può ritornare all'analisi per un altro asse es. articolo utilizzando tutti i fltri precedenti a cui si aggiunge quest'ultimo). Se poi il drill down viene eseguito anche su altri oggetti, gli ulteriori drill down vanno sempre in aggiunta rispetto ai filtri già impostati. Il filtro viene mantenuto finché non viene eseguito un roll up oppure non si interviene direttamente sui filtri con il bottone apposito (o con F13).
I filtri vengono mantenuti anche se ci si scollega / ricollega a Looc.Up.

![V5STAT_019](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_03/V5STAT_019.png)
- _2_Reset e Drill Down, questo invece cancella tutti i filtri già presenti e imposta come filtro solo l'elemento su cui si sta eseguendo l'azione, nell'esempio seguente è stato attivato un reset e drill down su un articolo, che ha cancellato tutti i filtri precedenti inserendo un filtro sull'articolo

![V5STAT_018](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_03/V5STAT_018.png)
- _2_Drill Down per oggetto, è significativo se nel file esistono altri campi dello stesso tipo di quello in esame (es. date, enti) cioè se viene seguito il click tasto destro su un raggruppamento ente (es. ente di fatturazione) questa azione permette di scegliere ed aggiungere al filtro un oggetto appartenente ad uno degli enti (responsabile, intestatario, di conferma, di fatturazione, di spedizione) presenti nel file usando come valore del filtro lo stesso cliccato (es. click sul valore 00180 di un'analisi di partenza in cui l'asse è per ente intestatario, permette di filtrare per il valore 00180 dell'ente di fatturazione)

![V5STAT_024](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_03/V5STAT_024.png)
- _2_Reset e Drill Down per Oggetto", come il precedente con la differenza che elimina tutti i filtri presenti prima.


- _2_Roll UP, permette di togliere i filtri impostati : 

![V5STAT_020](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_03/V5STAT_020.png)_2_Nota, gli stessi del filtri del drill/down possono essere visti/gestiti tramite il tasto funzionale F13
