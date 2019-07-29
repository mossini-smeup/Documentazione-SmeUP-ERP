## Obiettivo
Attraverso questa funzione è possibile analizzare la situazione dei rapporti bancari ad una certa data ovvero visualizzarne il valore del fido, il saldo a una data indicata e il residuo.

## Formato guida
Il formato guida si presenta nel seguente modo : 

![C5D030_006](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOXC0/C5D030_006.png)
All'interno del formato guida è prima di tutto necessario selezionare l'azienda d'interesse e la modalità di esecuzione della funzione :  le modalità disponibili sono Interrogazione e Stampa che restituiscono lo stesso risultato ripsettivamente in formato video e in spool di stampa.
I campi 'Pertinenza' e 'Condizione' devono essere compilati in funzione della tipologia di registrazioni che si vogliono considerare per il calcolo della situazione dei rapporti. In particolare nel campo Pertinenza è necessario indicare se considerare solo registrazioni gestionali, solo contabili o entrambe mentre nel campo Condizione è possibile indicare se considerare solo registrazioni attive, solo simulate o entrambe.
La 'Data situazione' rappresenta la data a cui si vuole visualizzare il saldo e il residuo per ogni rapporto bancario.
Indicando un tipo rapporto nel campo specifico è possibile visualizzare solo i rapporti bancari di una certa tipologia :  ad esempio è possibile visualizzare solo i rapporti di conto corrente o di anticipo fatture.
Il campo 'Codice banca' viene compilato nel caso in cui si vogliano visualizzare solamente i rapporti di una specifica banca.

Confermando il formato guida è possibile accedere al formato lista.

### Impostazioni
Digitando il tasto F17 o selezionando il relativo bottone è possibile accedere alle Impostazioni che riportano i seguenti campi : 
 * Ometto dettaglio :  attraverso questo campo è possibile visualizzare o meno il dettaglio per rapporto bancario. Omettendo il dettaglio, quindi, verranno resituite solamente le informazioni a livello di banca e non a livello di rapporto bancario.
 * Ordinamento :  permette di definire l'ordinamento di visualizzazione dei record; le scelte disponibili sono per tipo rapporto/banca oppure per banca/tipo rapporto.
 * Tipi rapporti :  consente di visualizzare i soli rapporti di portafoglio, tutti i rapporti esclusi quelli di portafoglio oppure l'elenco completo dei rapporti bancari.
 * Solo valorizzati :  permette di visualizzare solamente i rapporti per cui si abbia un residuo non nullo.
 * Separazione simulati :  attraverso questo campo è possibile vedere i saldi suddivisi tra registrazioni simuate e registrazioni definitive :  sarà, quindi, possibile visualizzare l'utilizzo imputabile a registrazioni simulate, l'utilizzo per registrazioni defnitive e l'utilizzo totale.
 * Data situazione :  questo campo permette di definire quale data considerare come data situazione; in particolare è possibile scegliere di considerare sempre la data valuta oppure di considerare la data scadenza per i rapporti di portafoglio e la data operazione per quelli non di portafoglio.
 * Separazione Dare/Avere :  consente di visualizzare l'utilizzo di un rapporto suddiviso in dare e avere; in particolare è possibile avere la separazione tra dare e avere solo sul totale generale riportato in fondo alla schermata, sul totale di ogni banca oppure per ogni rapporto bancario.


## Formato lista
All'interno del formato lista è possibile visualizzare per ogni rapporto bancario (oppure per ogni banca se si è deciso di omettere il dettaglio) il valore del fido impostato nell'anagrafica del rapporto bancario, l'utilizzo alla data situazione e il valore residuo : 

![C5D030_007](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOXC0/C5D030_007.png)
La data delle registrazioni che compongono i valori visualizzati è definibile all'interno delle impostazioni :  in particolare è possibile considerare sempre la data valuta oppure la data scadenza per i rapporti di portafoglio e la data data operazione per gli altri.
In fondo alla schermata è riportato anche il totale per azienda.

### Opzioni
Per ognuna delle righe riportate nel formato lista sono disponibili alcune opzioni : 

 - CS :  Situazione castelletto. Permette di accedere al dettaglio del castelletto sui rapporti di SBF e quindi consente di visualizzare le diverse rate che compongono l'utilizzo e la loro scadenza (che quindi determinerà l'evoluzione dell'utilizzo del rapporto nel futuro). Nelle due immagini seguenti è riportato un esempio di analisi di dettaglio del castelletto su un rapporto SBF : 


![C5D030_008](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOXC0/C5D030_008.png)![C5D030_009](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOXC0/C5D030_009.png)

 - MC :  Estratto conto. Consente di visualizzare l'estratto conto del rapporto selezionato, ovvero l'insieme delle registrazioni effettuatre sul conto contabile associato al rapporto ordinato per Data Operazione. La data finale delle registrazioni restituite corrisponde con la Data Situazione impostata nel formato guida, quindi se ad esempio viene impostata come data situazione 31/12/XXXX verranno visualizzati tutti i movimenti con data operazione minore o uguale a 31/12/XXXX.


![C5D030_010](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOXC0/C5D030_010.png)

 - MV :  Proiezione in valuta. Consente di visualizzare il mastrino del conto contabile associato al rapporto selezionato ordinato per Data Valuta. La data finale delle registrazioni restituite corrisponde con la Data Situazione impostata nel formato guida, quindi se ad esempio viene impostata come data situazione 31/12/XXXX verranno visualizzati tutti i movimenti con data valuta minore o uguale a 31/12/XXXX.


![C5D030_011](http://localhost:3000/immagini/MBDOC_OGG-P_C5NOXC0/C5D030_011.png)
 - 22 :  Gestione Parametri. Consente di visualizzare e modificare i parametri relativi al rapporto bancario
 - 32 :  Gestione condizioni. Consente di visualizzare e modificare le condizioni bancarie relative al rapporto bancario


### Tasti funzionali

- F04 Stampa :  permette di stampare o creare un PDF dell'interrogazione
- F09 Capo :  permette di posizionarsi sulla prima riga dell'interrogazione
- F10 Fine :  permette di posizionarsi sull'ultima riga dell'interrogazione
- F11 Parametri di esecuzione. Permette di impostare i parametri per l'esecuzione della funzione; in particolare è possibile definire se eseguire il lavoro in modalità interattiva oppure batch.
- F17 Impostazioni. Permette di accedere alla schermata delle impostazioni

