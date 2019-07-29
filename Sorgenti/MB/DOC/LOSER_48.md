# Attivazione
L'attivazione avviene tramite l'oav dell'oggetto (OG)  ed in particolare : 
Attraverso l'attributo J/032 - Tipo gestione grafica
 :  : DEC T(OA) P(OG) K(J/032)
 :  : PAR L(TAB)
Valore|Descrizione|
1|Completa (Guida, Dettaglio, Inserimento)
2|Dettaglio (Guida e Dettaglio)
3|Guida


## Guida
Il guida si attiva se l'oggetto possiede l'attributo J/032 impostato.
Nel B£G99D, se attiva la gestione e si è in Looc.UP, viene eseguita la scheda LOSER_48 con sottoscheda G99D ricevendo l'oggetto.
La scheda viene aperta in modalità dialog, vengono completate le informazioni necessarie e sull'evento di UPDATE viene esguita la funzione LOSER_48 ESE.G99 che rimanda alla £G99 la risoluzione della funzione da richiamare.
Se l'oggetto possiede l'attributo J/032 impostato a 1, allora il guida richiederà anche i campi necessari ad eseguire l'inizializzaione dell'oggetto durante la fase di inserimento.
Il guida non esegue nessun controllo di obbligatorietà o consistenza del record demandandoli al controller. Il messaggio che viene utilizzato durante l'inserimento è il BAS0079.
Se attivo l'inserimento grafico vengono verificate assenza di errori sui campi video, sempre basandosi sul controller.

## Dettaglio
Il dettaglio si attiva se l'oggetto possiede l'attributo J/032 minore di 3 e nella descrizione la scheda da richiamare.
Nel B£GES0, se attiva la gestione e si è in Looc.UP, viene richiamata la funzione LOSER_48 ANA.RIC che esegue il  controller verifica la fattibilità dell'azione richiesta ed esegue la scheda LOSER_48 con sottoscheda G99STD.
Questa scheda esegue la parte comune a tutti gli oggetti ed esegue la funzione passatagli dal B£GES0.
La scheda viene recuperata dall'attributo J/032 e associata la relativa sottoscheda per azione richiesta.
Nel caso in cui il controller interrompa l'azione intrapresa, l'azione verrà reindirizzata su di una scheda che esplicita il motivo dell'annulamento dell'azione

### Inserimento grafico
Deve recuperare le informazioni del guida e passarle al dettaglio

### Note
Nella funzione LOSER_48 ANA.RIC e ESE.G99 dovranno essere presenti tutte quelle attivita da eseguire prima e dopo la gestione del dettaglio.
* VIncolo oggetto
* Flussi
