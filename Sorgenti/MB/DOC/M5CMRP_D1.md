# Controlli se l'MRP non funziona

Se l'MRP noin funziona correttamente, vale a dire se non riesce a coprire, con ordini pianificati, tutte le coperture presenti, i motivi possono essere i seguenti.

## Errato livello minimo
In questo caso gli impegni pianificati sono stati costruiti dopo avcer trattato il loro articolo, e quindi non sono trattati dal motore dell'MRP.
Per verificare questo caso, si confronta il numero record origine del primo consiglio rilasciato presente nell'archivio e quello di un impegno pianificato. Se quest'ultimo è più alto, significa che è stato scritto dopo aver trattato l'articolo, e quindi ci sono problemi di livello minimo :  l'assieme dell'ordine a cui si riferiscono i consigli non ha livello minimo inferiore dell'articolo in esame.
Bisogna quindi esaminare il motivo per cui il livello minimo è errato :  Può errere un errore di conversione, oppure non è stata correttamente considerata la configurazoone, ....

## Errata definizione fonti
Un errore più subdolo si presenta quando, pur con il livello minimo corretto, gli impegni pianificati, che sono presenti nell'archivio consigli, non vengono coperti.
Si deve verificare se essi sono presenti nel gruppo fonti che costituisce la base di disponibilità per la pianificazione.
Essi sono presenti nell'archivio consigli, perchè sono stati scritti all'atto della pianificazione del loro assieme, ma, all'atto della pianificazione del loro articolo, se non sono presenti nel gruppo fonti, non vengono riportati nelle aree di memoria utilizzate per eseguire la pianificazione.

## Considerazione generale sul gruppo fonti
Gli ordini pianificati, a rigore, non è necessario siano presenti nel gruppo fonti della pianificazione, dato che all'inizio della pianificazione di ogni aritcolo, quando viene scandito il gruppo fonti, essi non sono ancora presenti.
Tuttavia, se li si include comunque, a prezzo di un rallerntamento insignificante, è possibile utilizzare lo stesso gruppo fonti anche al di fuori dell'MRP, ad esempio in una normale analisi disponibilità, per controllare il bilanciamento eseguito dall'MRP stesso.

## Errata definizone impegni raggruppati
Se si è impostato, nella fonte, di raggruppere gli impegni per data, si deve avere l'avvertenza, se l'articolo è gestito a rottura, di impostare nella fonte il flag di separazione per codice di rottura. In mancanza di questa impostazione, gli impegni vengono attribuiti all'oggetto di rottura (ad esempio configurazione) blanks, con il risultato di un'errata pianificazione.



