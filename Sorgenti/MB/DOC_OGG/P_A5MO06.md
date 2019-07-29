## Obiettivo
Attraverso questa funzione è possibile eseguire la contabilizzazione degli ammortamenti.

## Formato guida
La schermata del formato guida si presenta nel seguente modo : 

![A5OPCO_007](http://localhost:3000/immagini/MBDOC_OGG-P_A5MO06/A5OPCO_007.png)
Vediamo in dettaglio le voci che compaiono al suo interno : 

- Periodo/Esercizio :  indicare l'esercizio per cui si vogliano contabilizzare gli ammortamenti
- Linea ammortamento :  indicare la linea di cui si vogliono contabilizzare gli importi
- Data registrazione :  indicare la data a cui effettuare la scrittura contabile degli ammortamenti
- Data limite movimenti iniziale/finale :  indicare gli estremi di date entro cui recuperare i movimenti di ammortamento. Se, ad esempio, stiamo effettuando la contabilizzazione annuale degli ammortamenti inseriremo data iniziale 01/01/XX e data finale 31/12/XX mentre se stiamo effettuando la contabilizzazione dei soli ammortamenti di giugno metteremo 01/06/XX - 30/06/XX
- Solo simulazione :  compilare il campo nel caso in cui si voglia ottenere solo una stampa di simulazione
- Singolo cespite :  nel caso in cui si vogliano contabilizzare gli ammortamenti di un solo cespite indicarne il codice in questo campo
- Totalizza per conto :  se compilato i saldi verranno totalizzati per conto contabile
- Dettaglio registrazione :  permette di ottenere una scrittura dettagliata per cespite oppure generare una scrittura unica
- Tipo registrazione :  nel caso in cui si voglia forzare un tipo registrazione diverso rispetto a quanto impostato nei parametri di contabilizzazione inserirlo in questo campo.
- Scelta registrazioni :  indicare le tipologie di ammortamento che si voglia contabilzzare. Si consiglia di flaggare tutte le tipologie di ammortamento in modo da non escludere alcun movimento
- Parzializzazioni :  permette di accedere alle parzializzazioni per contabilizzare solo gli ammortamenti di alcuni cespiti


Nel caso in cui all'interno della tabella A51 non sia stato compilato il campo 'Ammessa contabilizzazione batch', confermando con F06 sarà possibile visualizzare la registrazione generata e confermarla con F18 : 
![A5OPCO_008](http://localhost:3000/immagini/MBDOC_OGG-P_A5MO06/A5OPCO_008.png)Se, invece, il campo è stato compilato la contabilizzazione verrà sottomessa in batch e verrà prodotta una stampa della scrittura generata.
