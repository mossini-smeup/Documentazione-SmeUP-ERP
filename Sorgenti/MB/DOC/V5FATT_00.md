# Passi del ciclo attivo
Per il ciclo attivo i passi riguardanti la fatturazione sono : 

- Previsione di vendita
- Ordine di vendita
- Bolla
- Fattura
- Fatturazione

Non è necessario partire per forza da una previsione di vendita.

# Criterio di ordinamento
Quando inserisco un documento  (utilizzando quindi un tipo documento della **TA V5D**), tra le altre informazioni viene scritto il _7_criterio di ordinamento** (d'ora in poi **CORD**) che è una serie di informazioni ordinate e relative al documento stesso.

Chi gestisce il CORD è il programma **V5DO01O**. Tale programma costruisce il cord in base a un campo della tabella **V5A**+SS (tipo documento) ovvero il **T$V5AG** (Criterio ordine doc.).
Nel programma è prevista quindi la possibilità di utilizzare personalizzazioni per la gestione dei raggruppamenti :  è sufficiente infatti utilizzare  uno dei valori presenti in tabella V5A (che in realtà è un oggetto di tipo V2 V5COD) tra quelli a disposizione.

# Stampa fatture
La fatturazione come fase gestionale consta di fatto nello stampare le fatture a partire dalle bolle, che naturalmente avranno già un loro "cord" impostato dal modello di documento.
In fase di stampa fattura, sulla bolla (che generalmente ha già un suo numero e data bolla) viene scritto : 

- il numero e la data fattura (**T§NFAT**,**T§DFAT**)
- il criterio di ordinamento   (**T§CORD**)

Il numero della fattura è gestito dal numeratore fatture, che è definito in TAV5A+SS e che punta a sua volta alla tabella **CRNV5**.
La data fattura è quella indicata nella stampa stessa (di default è la data odierna).
Il **CORD** viene aggiornato con data fattura, numero fattura e  modello documento (da tabella V5A+SS), più eventuali altri criteri dettati dal programma **V5DO01O_x**.
Il criterio di ordinamento in cui vengono raggruppate le fatture è anzitutto quello del cliente cui sono intestate. Sull'anagrafica dell'ente, è possibile però specificare se per esso voglio un'unica fattura data da tutte le bolle a lui intestate per quel periodo. Per fare ciò è sufficiente compilare il campo (di BRENTI0F) **E§FL03** (solitamente impostato a blank). L'informazione di cui sopra verrà riportata anche sul campo **T§FDTA** dell'archivio documenti (V5TDOC0F).

# Contabilizzazione
La contabilizzazione delle fatture può essere effettuata tramite il richiamo del pgm V5FA05A. Questo richiamato senza parametri emetterà una finestra di richiesta parametri per definire le modalità di esecuzione della stessa.

Richiamando il medesimo programma con un solo parametro sarà invece possibile eseguire la contabilizzazione in modo cieco.
Passando nel parametro il valore C verrà effettuata la contabilizzazione di fatture e note clienti, mentre passando F, verrà effettuata la contabilizzazione di fatture/note di addebito fornitori (qual'ora previsti).

