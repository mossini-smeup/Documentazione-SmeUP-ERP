 :  : TIT Bigino per la comprensione della codifica di distinta e ciclo in Sme.UP
# Obiettivo di questo documento : 
Obiettivo di questo documento è quello di rappresentare il "bigino" delle strutture fondamentali di Sme.UP, ossia distinta materiali (detta anche distinta base) e ciclo di produzione, necessarie per gestire la produzione . Con "gestire la produzione" si intende l'insieme di tutti quei processi che permettono ad una azienda di comprare dai fornitori, trasformare, immagazzinare  e spedire materiali ai clienti.
In altre parole il lettore di questo documento dovrebbe comprendere quali sono le strutture portanti, gli architrave, del modello di dati e processi che permettono al software gestionale Sme.UP di essere un'applicazione valida per la gestione della produzione. Un risultato atteso è anche quello di mettere chiarezza sui termini usati e sui concetti che sottintendono.

## Codificare gli articoli : 
Innanzi tutto bisogna capire perchè un oggetto si codifica come articolo. Si codifica come articolo un oggetto quando si necessita gestirlo a magazzino, oppure comprarlo più di una volta, oppure venderlo più di una volta, oppure perchè si desidera distinguerlo da un altro oggetto, anch'esso codificato.
La codifica è come il codice fiscale di una persona :  di Paolo Rossi ce ne possono essere tanti ma uno solo è quello con quel codice fiscale.
Quindi codifichiamo gli articoli per distinguerli e poi per ritrovarli in mezzo ai loro simili. A volte mettiamo l'etichetta col loro codice alle scatole che li contengono perchè è l'unico modo per riconoscerli.

Quindi il codice è importante :  in passato si usavano molto i codici parlanti perchè permettevano una facile identificazione, in quanto nel codice si "leggevano" le caratteristiche. Per esempio una vite con passso 10 e lunghezza 30 avrebbe potuto essere codificata come V10X30. Ovviamente se poi bisognava indicare anche il materiale (inox, ottone, etc) ed il tipo di testa (std, quadra, a croce) il codice si complicava troppo. Con prodotti complessi, ad esempio nel campo tessile, si arrivava anche a 30 campi per codificare un articolo. E questo provocava difficolta di digitazione e possibilità di errori.

In Sme.UP possiamo caratterizzare gli articoli con una serie di campi predisposti ad una caratterizzazione utente, ossia definibili alla bisogna, che permettono di descrivere tutte le caratteristiche identificative degli articoli. Questi campi sono definibili come Parametri dell'articolo. In questi parametri andiamo a caratterizzare l'articolo.
Ovviamente articoli profondamente diversi, ad esempio una vite ed un tessuto, una molla ed un cuscinetto, necessitano parametri diversi quali lunghezza e passo, oppure tipo tessuto e colore.

Quindi quando si codifica  un articolo, per prima cosa si indica il "tipo articolo" (tabella BRA) che rappresenta l'aggancio al gruppo di parametri che permettono la caratterizzazione dell' articolo. Questi parametri sono poi visti dappertutto come attributi dell'articolo e permettono quindi di aggiungere la colonna con il valore della caratteristica in una matrice e poi usarla per raggruppare, filtrare, etc.

Altre classificazioni importanti dell'articolo sono :  il tipo parte, che permette di agganciare almeno la politica di pianificazione di default quando mancano i parametri di pianificazione, la classe materiale (importante per differenziare le ricariche del calcolo costi)  e la classe programmazione (importante per indirizzare ai parametri di pianificazione).

NOTA :  il tipo parte "0" identifica gli articoli che non esistono fisicamente, ma che rappresentano un assieme di tipo logico, ossia un raggruppamento di altri articoli.
![AAV_01_001](http://localhost:3000/immagini/MBDOC_VIS-AABIG/AAV_01_001.png)

## Trasformare il materiale : 
Trasformare il materiale significa modificarlo. I due modi principali per modificare un articolo sono : 
 - tramite lavorazione di un pezzo di materiale (forare, verniciare, tagliare, etc) :   si otttiene un articolo diverso
 - tramite composizione (montaggio, incollaggio, saldatura) di due o più articoli si ottiene un altro articolo.
Ovviamente è possibile anche avere trasformazioni composite, ossia che lavorano dei pezzi nel mentre che li compongono, ma ci piace scomporre questa tipologia composita nelle due principali perchè permette di comprendere il ruolo di due strutture principali :  il "ciclo di lavoro" e la "distinta dei materiali".
Il ciclo di lavoro, d'ora in poi chiamato ciclo, è la struttura che descrive la sequenza ordinata delle fasi di lavorazione.
La distinta dei materiali, d'ora in poi chiamata distinta, è invece la struttura che descrive i materiali necessari (detti componenti) per comporre (montare, etc) un assieme.

Per capire queste strutture proviamo a descrivere come si applicherebbero alla costruzione di una scopa, dove si suppone di costruire prima il manico e poi di accoppiarlo alla saggina per ottenere la scopa.

Ad esempio , il ciclo dell'articolo "manico di scopa" è : 

|  Nam="Ciclo" |
| 
| .COL Txt="Fase" LunAut="1" |
| ---|----|
| 
| .COL Txt="Descrizione fase" LunAut="1" |
| 
| .COL Txt="Centro di lavoro" LunAut="1" |
| 0010 | Tagliare a misura | C01 |
| 0020 | Smussare un estremo | C05 |
| 0030 | Carteggiare  | C10 |
| 0040 | Vernicaire di Rosso | F01 |
| 


e la distinta dell'articolo "manico di scopa" è : 


|  Nam="Distinta" |
| 
| .COL Txt="seq" LunAut="1" |
| ---|----|
| 
| .COL Txt="assieme" LunAut="1" |
| 
| .COL Txt="componente" LunAut="1" |
| 
| .COL Txt="qty" LunAut="1" |
| 
| .COL Txt="operazione impiego" LunAut="1" |
|   | manico di scopa | bastone | 1 | 0010 |
|   | manico di scopa | vernice | 15 | 0040 |
| 


 Ad esempio, la distinta dell' articolo "scopa"  è   : 


|  Nam="Distinta" |
| 
| .COL Txt="seq" LunAut="1" |
| ---|----|
| 
| .COL Txt="assieme" LunAut="1" |
| 
| .COL Txt="componente" LunAut="1" |
| 
| .COL Txt="qty" LunAut="1" |
| 
| .COL Txt="operazione impiego" LunAut="1" |
|   | scopa | manico di scopa | 1 | 0020 |
|   | scopa | filo di saggina | 300 | 0010 |
|  1 | scopa  | filo di ferro | 20 | 0010 |
|  2 | scopa | filo di ferro | 10 | 0020 |
| 


ed il ciclo dell'articolo "scopa" è  : 

|  Nam="Ciclo" |
| 
| .COL Txt="Fase" LunAut="1" |
| ---|----|
| 
| .COL Txt="Descrizione fase" LunAut="1" |
| 
| .COL Txt="Centro di lavoro" LunAut="1" |
| 0010 | Raggruppare saggina legandola | G01 |
| 0020 | Accoppiare manico e legare | G01 |
| 


L'esempio della costruzione della scopa è molto significativo anche se potrebbe sembrare banale.
Osserviamo due o tre indicazioni chiave :  nei legami di distinta abbiamo descritto anche la operazione di impiego. Questo è utile per specificare meglio dove (e quando) il componente sarà utilizzato. Infatti se si nota che sul ciclo è indicato anche il centro di lavoro dove si effettua la operazione, si può dedurre che legando il componente alla operazione, si potrà indicare all'operatore che alimenta la linea dove portare i materiali.

Quindi, quando abbiamo dovuto descrivere il legame tra la scopa ed il filo di ferro, ci siamo accorti che il filo di ferro veniva utilizzato sia per "raggruppare la saggina legandola", che è la fase 0010 del ciclo di "scopa" e sia nella fase 0020 "accoppiare manico e legare". Pertanto abbiamo indicato due legami di distinta per l'articolo "scopa" e per poterli distinguere abbiamo inserito un valore nel campo "seq" (sequenza di distinta, per la precisione dovremmo dire che ci sono due campi sequenza utilizzabili..), dove ogni legame indica la quantità di componente necessaria per l'operazione specifica.

Inoltre, notiamo che per descrivere il fatto che "prima si costruisce il manico e poi si accoppia alla saggina" , abbiamo ipotizzato due livelli di distinta, ossia un legame per descrivere che dal legno si passa al manico, e poi un'altro per descrivere che dal manico si passa alla scopa.

Ovviamente questo approccio è utile, anzi fondamentale, se la fabbricazione della scopa si disaccoppia in "fabbricazione dei manici" e poi "montaggio della scopa". Per esempio se lo stessso tipo di manico (lunghezza, diametro, colore) è utilizzato per essere montato in scope con tipi saggina diversi (vegetale, nylon, altro..) ecco che diventa conveniente costruire in un colpo solo 1000 manici e poi assiemarli come scopa finita solo per le quantità necessarie a coprire gli ordini clienti specifici (150 scope con nylon, 270 scope con saggina vegetale)

Ben diversa sarebbe stata la descrizione della costruzione della scopa se questa avvenisse tutta insieme per una scopa finita. Svolgiamo questo esempio : 

Distinta dell' articolo "scopa"  diventa   : 


|  Nam="Distinta" |
| 
| .COL Txt="seq" LunAut="1" |
| ---|----|
| 
| .COL Txt="assieme" LunAut="1" |
| 
| .COL Txt="componente" LunAut="1" |
| 
| .COL Txt="qty" LunAut="1" |
| 
| .COL Txt="operazione impiego" LunAut="1" |
|   | scopa | bastone | 1 | 0010 |
|   | scopa | vernice | 15 | 0040 |
|   | scopa | filo di saggina | 300 | 0010 |
|  1 | scopa  | filo di ferro | 20 | 0050 |
|  2 | scopa | filo di ferro | 10 | 0060 |
| 


Ed il ciclo diventa


|  Nam="Ciclo" |
| 
| .COL Txt="Fase" LunAut="1" |
| ---|----|
| 
| .COL Txt="Descrizione fase" LunAut="1" |
| 
| .COL Txt="Centro di lavoro" LunAut="1" |
|  0010 | Tagliare a misura | C01 |
|  0020 | Smussare un estremo | C05 |
|  0030 | Carteggiare | C10 |
|  0040 | Verniciare di rosso | F01 |
|  0050 | Raggruppare saggina legandola | G01 |
|  0060 | Accoppiare a manico e legare | G01 |
| 


Un'altra modalità di fabbricazione della scopa potrebbe essere quella del carrello di lavoro che passa da un centro di lavoro all'altro, contenendo fin dalla creazione del carrello stesso tutti i componenti necessari per la fabbricazione della scopa. In questo caso, tutti i componenti sono necessari pre svolgere la prima fase del ciclo che diventa "riempimento carrello".
In distinta non bisogna più specificare l'operazione di impiego, così facendo tutti i componenti vengono legati alla prima fase, 0005 Riempire Carrello.


|  Nam="Ciclo" |
| 
| .COL Txt="Fase" LunAut="1" |
| ---|----|
| 
| .COL Txt="Descrizione fase" LunAut="1" |
| 
| .COL Txt="Centro di lavoro" LunAut="1" |
|  0005 | Riempire il carrello | H01 |
|  0010 | Tagliare a misura | C01 |
|  0020 | Smussare un estremo | C05 |
|  0030 | Carteggiare | C10 |
|  0040 | Verniciare di rosso | F01 |
|  0050 | Raggruppare saggina legandola | G01 |
|  0060 | Accoppiare a manico e legare | G01 |
| 


Ma non siamo ancora contenti del nostro processo di costruzione della scopa, vogliamo perfezionarlo :  abbiamo capito che è conveniente verniciare il manico solo quando si ha l'ordine cliente, perchè il colore è una variabile che lasciamo scegliere al cliente. Allora a magazzino mettiamo il manico carteggiato, e nel ciclo di "scopa" inseriamo come prima fase la verniciatura.

Distinte e ciclo diventano : 

il ciclo dell'articolo "manico di scopa" è : 


|  Nam="Ciclo" |
| 
| .COL Txt="Fase" LunAut="1" |
| ---|----|
| 
| .COL Txt="Descrizione fase" LunAut="1" |
| 
| .COL Txt="Centro di lavoro" LunAut="1" |
| 0010 | Tagliare a misura | C01 |
| 0020 | Smussare un estremo | C05 |
| 0030 | Carteggiare  | C10 |
| 


invece la distinta dell'articolo "manico di scopa" è : 


|  Nam="Distinta" |
| 
| .COL Txt="seq" LunAut="1" |
| ---|----|
| 
| .COL Txt="assieme" LunAut="1" |
| 
| .COL Txt="componente" LunAut="1" |
| 
| .COL Txt="qty" LunAut="1" |
| 
| .COL Txt="operazione impiego" LunAut="1" |
|   | Manico di scopa | bastone | 1 | 0010 |
|  


Ad esempio, la distinta dell' articolo "scopa"  è   : 


|  Nam="Distinta" |
| 
| .COL Txt="seq" LunAut="1" |
| ---|----|
| 
| .COL Txt="assieme" LunAut="1" |
| 
| .COL Txt="componente" LunAut="1" |
| 
| .COL Txt="qty" LunAut="1" |
| 
| .COL Txt="operazione impiego" LunAut="1" |
|   | scopa | manico di scopa | 1 | 0020 |
|   | scopa | vernice | 15 | 0005 |
|   | scopa | filo di saggina | 300 | 0010 |
|  1 | scopa  | filo di ferro | 20 | 0010 |
|  2 | scopa | filo di ferro | 10 | 0020 |
| 



ed il ciclo dell'articolo "scopa" è  : 


|  Nam="Ciclo" |
| 
| .COL Txt="Fase" LunAut="1" |
| ---|----|
| 
| .COL Txt="Descrizione fase" LunAut="1" |
| 
| .COL Txt="Centro di lavoro" LunAut="1" |
| 0005 | Verniciare di rosso | F01 |
| 0010 | Raggruppare saggina legandola | G01 |
| 0020 | Accoppiare a manico e legare  | G01 |
| 



### La distinta base : 
Possiamo quindi elencare a cosa serve la distinta base e quali sono le informazioni fondamentali.
 * Ogni legame di distinta rappresenta la relazione tra un articolo ed un componente.
 * Per rappresentare un grappolo di componenti, ossia una trasformazione che coinvolge più livelli di distinta, bisogna scrivere N legami, uno per ogni livello e per ogni componente
 * Operazione di impiego :  rappresenta la fase del ciclo dove si consumerà il componente
 * Nel legame di distinta si può riportare il "tempo di rettifica", detto anche leadtime adjustment, che rappresenta l'anticipo di giorni rispetto alla data di completamento trasformazione, per calcolare la data di necessità del componente. (vedi capitolo "pianificare")
 * Avere i livelli di distinta è utile nei seguenti casi : 
 ** Se ci sono vincoli di lotto minimo o multiplo diversi tra un assieme ed un componente (es. Manici almeno 1000, scope alla bisogna)
 ** Se si riutilizzano i semilavorati al livello in assiemi diversi (es :  lo stesso manico in scope diverse)
 ** Se si vuole immagazzinare una parte della trasformazione (es. manico di scopa)
 ** Se si vuole descrivere un KIT di materiali, ossia un assieme fittizio (detto anche phantom, fantasma) che non rappresenta un montaggio fisico ma solamente logico.

### Il ciclo di lavoro : 
Il ciclo è utile per  : 
 * Tenere in sequenza temporale le fasi di trasformazione (ne beneficia la schedulazione)
 * Calcolare i costi ed i carichi delle trasformazioni interne

Nel ciclo ci sono queste informazioni fondamentali : 
 * Tempi e valori della fase
 * Centro di lavoro su cui avviene la fase
 * Operazione di riferimento :  questa è una operazione predefinita, ossia è un template usando il quale si aiuta la compilazione delle fasi del ciclo. Praticamente rappresenta la classificazione della sequenza (es. la fase 0057 di un ciclo , se ha come operazione di riferimento " A010 Tornitura" permette al volo di capire che tipo di operazione sia...)

### Il tempo di trasformazione : 
In Sme.UP, per tempo di trasformazione si intende il tempo necessario per "completare" un livello di distinta. Infatti si chiama anche leadtime di livello.
Se un articolo è un assieme di semilavorati i quali hanno ulteriori componenti (grappolo di trasformazioni) , allora si può parlare anche di leadtime cumulato, che rappresenta la distanza più alta tra l'inizio di trasformazione di un componente elementare e il momento di fine trasformazione dell'assieme.
NOTA IMPORTANTE :  il leadtime NON è la somma dei tempi di lavoro riportati sulle singole fasi del ciclo, in quanto il tempo necessario è più determinato dalle code di attesa ai centri di lavoro piuttosto che dal tempo netto di lavorazione (quasi sempre vero).
Il tempo di trasformazione è utile per datare il consumo dei componenti in distinta e quindi indica la data a cui si vuole ricevere il materiale.
Ci sono tre modi per indicare questa data : 
 - All'inizio della trasformazione, e questo viene fatto utilizzando il leadtime di livello
 - In una delle operazioni del ciclo
 - N giorni prima della fine della trasformazione
Nei casi 2 e 3 si utilizza il "tempo di rettifica" scritto sul legame di distinta per indicare gli N giorni di anticipo.
