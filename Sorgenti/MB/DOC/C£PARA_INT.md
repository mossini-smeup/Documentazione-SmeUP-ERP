# Generalità
La gestione "Parametri per Oggetti" è stata creata per potere espandere liberamente le informazioni che si riferiscono ad almeno un oggetto (anche ad una coppia di oggetti).
Questa possibilità risponde all'esigenza applicativa di dover incrementare le informazioni di un oggetto, senza dover aumentare fisicamente l'archivio dove è definito l'oggetto.
Per esempio, definire il colore per gli articoli, o il grado di frigorie per le ubicazioni, diventa possibile senza dover modificare il tracciato dell'anagrafica articoli (per aggiungere il campo colore che non era previsto ) o dell'anagrafica ubicazioni ( per aggiungere il campo "frigorie").

Quindi ad ogni entità (oggetto o coppia di oggetti) è possibile associare uno o più parametri che lo caratterizzano permettendo di descrivere ancor meglio l'oggetto :  si viene così a creare una scheda tecnica legata all'oggetto in questione costituita di n caratteristiche aggiuntive.
Questa struttura si utilizza ad esempio per associare ad un articolo (o ad  un tipo di articoli) un gruppo di variabili non presenti a livello anagrafico perché tipiche del contesto applicativo in cui ci si trova.
Per l'inserimento e la manutenzione dei parametri sono previste apposite funzioni che possono essere chiamate autonomamente, oppure direttamente nei flussi di inserimento/modifica degli oggetti.
I parametri memorizzati possono poi essere interrogati in vari modi : 

- parametri per oggetto
- oggetti per parametro
- oggetti che rispondono a particolari valori dei parametri.


![C£_05_01](http://localhost:3000/immagini/C£PARA_INT/CX_05_01.png)
Figura 1 - Associazione Parametri ad oggetti

# Utilizzi
Potere associare dei parametri ad una entità può risultare particolarmente utile per caratterizzarla. Si può, per esempio, facilmente associare ad ogni oggetto dei valori (scheda tecnica) che risultano particolarmente utili ad un cliente.
La possibilità di associare ad un oggetto (o ad una coppia di oggetti) un numero praticamente infinito di parametri premette di soddisfare gran parte delle richieste del cliente senza la necessità di sviluppare personalizzazioni.
La disponibilità di funzioni di interrogazione e selezione di oggetti che soddisfano la presenza di valori specifici in determianti parametri agevola la gestione degli oggetti.
