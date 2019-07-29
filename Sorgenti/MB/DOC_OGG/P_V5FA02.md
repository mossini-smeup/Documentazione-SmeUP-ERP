# Generalità
La funzione di stampa interattiva fatture permette di agire sui documenti del ciclo attivo al fine di ottenere fatture o note di credito.

Questa funzione, fatto salvo l'obiettivo finale di creare delle fatture, è un vero e proprio cruscotto di manutenzione con cui si possono eventualmente modificare i documenti in attesa di essere fatturati, ad esempio modificando dei prezzi o rendendo non fatturabili alcune righe oppure anche raggruppando in una fattura unica più documenti o separando documenti che il sistema avrebbe raggruppato.

# Formato richiesta
Il formato di richiesta è il seguente : 

![V5_21_01](http://localhost:3000/immagini/MBDOC_OGG-P_V5FA02/V5_21_01.png)
Scegliere se si vuole generare Fatture e/o Note di credito.

Il tipo azione permette di scegliere cosa fare sui documenti.

Per agire su un unico ente di fatturazione compilare il campo apposito, altrimenti agire su tutti o documenti fatturabili, oppure su una lista filtrata dalle parzializzazioni.

La data fattura viene preimpostata dal sistema ad oggi, ma può essere variata manualmente.

La scelta permette di decidere se lavorare sugli enti con fatturazione periodica, oppure sugli altri o su tutti.

# Impostazione fatturazione periodica
Gli enti che richiedono una fatturazione periodica devono avere impostato il tipo di periodicità richiesta; per fare questo bisogna impostare opportunamente i parametri di fatturazione nelle informazioni aggiuntive :  usare il tipo informazione £08 (Parametri Fatturazione) e impostare il tipo di fatturazione periodica voluto : 

![V5_21_02](http://localhost:3000/immagini/MBDOC_OGG-P_V5FA02/V5_21_02.png)
_2_Nota bene; i tipi di fatturazione  periodica sono caricati nella tabella BR*_CF.

Quando si vogliono gestire documenti con fatturazione periodica inserire il valore 1 (Fatture a data fissa) nel campo "Scelta" e nel campo di input Gruppo selezionare il gruppo su cui lavorare, il sistema filtra solo le fatture degli enti di quel gruppo.

# Gestione lista fatture
Fatte le opportune selezioni con F6 si ottiene la lista dei documenti fatturabili : 

![V5_21_03](http://localhost:3000/immagini/MBDOC_OGG-P_V5FA02/V5_21_03.png)
I documenti in attesa fattura che, secondo le regole definite, possono essere raggruppati, vengono unificati e presentati nella lista, dove ciascuna riga presentata corrisponde ad una fattura.
Se il tipo azione impostato è "Prestampa" il progressivo fattura è un numero di comodo, altrimenti è il numero fattura.

Sulla prima colonna di sinistra vengono indicati con "S" i documenti selezionati per la stampa, l'ultima colonna di destra indica il numero di documenti che vengono raggruppati nella fattura.

Sulle fatture presentate nella lista sono possibili le seguenti opzioni : 

![V5_21_04](http://localhost:3000/immagini/MBDOC_OGG-P_V5FA02/V5_21_04.png)
L'utilizzo è intuitivo, una menzione particolare meritano : 

## Stampa
L'opzione "S" permette di selezionare un documento per la stampa, tutti i documenti selezionati presentano una "S" nel campo S (di sinistra). Per deselezionare una fattura selezionata in precedenza usare l'opzione "N".
il tasto F20 lancia la stampa delle fatture selezionate con "S".

## Modifica righe
Può essere necessario modificare un prezzo od uno sconto in una riga.
L'opzione RI presenta la lista delle righe del documento, per entrare in modifica su una riga usare la solita opzione "02" di modifica.
Se la fattura è costituita di più documenti vengono presentate in sequenza le righe di ciascun documento a partire dal primo; F12 per passare al documento successivo.

## Testata bolle
Se si vogliono aggiornare delle condizioni di fatturazione (es. la modalità di pagamento) è necessario modificare la testata della bolla.
L'opzione BO è come l'opzione 02 di modifica, se la fattura è costituita da più documenti viene presentata prima la lista dei documenti, e si entra nella testata del documento selezionato.

## Raggruppamento documenti
I documenti che corrispondono ai criteri di raggruppamento vengono già raggruppati, se si vuole fare un raggruppamento ulteriore, come forzatura della regola inserita nel sistema, allora si selezionano con "RG" i documenti da raggruppare. Quando sono selezionati per i raggruppamenti i documenti vengono sottolineati.
Per deselezionare un documento selezionato in precedenza usare l'opzione "ER".
Il tasto F18 esegue il raggruppamento dei documenti selezionati con "RG".

## Divisione bolle
Se si vogliono creare delle fatture singole da documenti che il sistema prevede di raggruppare si usa l'opzione DI.
Viene presentata la lista dei documenti che concorrono alla composizione della fattura e si selezionano quelli da togliere.

## Gestione flag fatturazione di riga
Se si vuole intervenire su una riga singola di un documento, ad esempio per renderla non fatturabile, allora si deve intervenire sul "Flag" di fatturazione della riga stessa usando l'opzione FR :  viene presentato l'elenco delle righe della bolla con quantità prezzo e importo, a fine lista viene mostrata una situazione riassuntiva delle righe e relativi flag di fatturazione : 

![V5_21_05](http://localhost:3000/immagini/MBDOC_OGG-P_V5FA02/V5_21_05.png)
l'opzione opportuna permette di visualizzare la riga, di forzare la non fatturazione oppure di gestire direttamente il valore del flag di fatturazione con uno dei significati seguenti : 

![V5_21_06](http://localhost:3000/immagini/MBDOC_OGG-P_V5FA02/V5_21_06.png)
# Azioni su interi documenti
Quando dalla stampa fatture si vuole escludere (temporaneamente) un documento allora si deve intervenire sul documento stesso utilizzando la funzione apposita (cfr. P_V5DO21I Azioni su documenti fatturabili).
