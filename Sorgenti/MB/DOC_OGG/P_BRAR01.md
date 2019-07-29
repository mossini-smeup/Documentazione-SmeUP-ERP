# Generalità
Tutti i materiali che vengono usati in un'azienda e sono codificati vengono registrati nell'anagrafico articoli.

In Sme.up l'anagrafico articoli permette di gestire non solo articoli di produzione ma anche tutta una serie di codici materiali definiti ed utilizzati per le più svariate esigenze.

Ad esempio possono essere usati per gestire i materiali di produzione, gli utensili, i materiali di manutenzione, i contenitori, le attrezzature, gli strumenti di misura, o anche i servizi .
La diversificazione di questi oggetti è caratterizzata dal tipo articolo (tabella BRA).

## Tipi articoli
In Sme.up è possibile definire diversi tipi articoli ed associare a ciascun tipo caratteristiche e comportamenti differenti.
Ad esempio potremmo avere : 

- Prodotti Finiti
- Componenti
- Materia prima
- Utensili
- Materiali di manutenzione
- Imballi
- Articoli generici
- ......


## Gestione anagrafico articoli
Per attivare la gestione dell'anagrafico articoli si parte dal seguente formato guida : 

![BR_01_01](http://localhost:3000/immagini/MBDOC_OGG-P_BRAR01/BR_01_01.png)
Utilizzando le opzioni si accede al formato di dettaglio dove sono presentati tutti i campi propri dell'anagrafico articoli di Sme.up : 

![BR_01_02](http://localhost:3000/immagini/MBDOC_OGG-P_BRAR01/BR_01_02.png)
_3_Nota, un solo formato video non è sufficiente a contenere tutti i dati dell'anagrafico articoli,  sono previsti 2 formati successivi; il principale contiene i dati di più frequente utilizzo mentre l'altro è dedicato ai dati secondari : 

![BR_01_03](http://localhost:3000/immagini/MBDOC_OGG-P_BRAR01/BR_01_03.png)
### Descrizione dei campi principali

- _2_Tipo articolo, i vari tipi articoli sono presenti nella tabella BRA. Il tipo articolo definisce la caratterizzazione dell'articolo (es. se è richiesta la configurazione guidata; se in sede di inserimento si attiva un processo di costruzione guidata del codice; se ci sono dei campi di default tipo :  unità di misura, classe materiale; quale categoria parametri è prevista; ecc).
- _2_Stato, permette di indicare se si tratta di un articolo attivo o meno.
- _2_Tipo parte, classifica l'articolo. Da un punto di vista di pianificazione o di esplosione distinta di produzione gli articoli con tipo parte che inizia con 0 sono considerati "fittizi" :  questo significa che non vengono considerati e si passa direttamente ai loro figli di distinta. Dal punto di vista del calcolo dei costi questo campo permetterà di considerare l'articolo di produzione, di acquisto o di conto lavoro.
- _2_Iva, riferito alla tabella IVA, è l'assoggettamento IVA a cui normalmente è legato l'articolo.
- _2_Plant di appartenenza, riferito alla tabella MAG, è il plant responsabile della pianificazione dell'articolo (gestito solo nel caso di implementazione multiplant).
- _2_Unità di misura, unità di misura interna dell'articolo (in tabella UMS).
- _2_Disegno, solo descrittivo. Permette di indicare un disegno di riferimento.
- _2_Gruppo Distinta - Gruppo Ciclo, nel caso diversi articoli abbiano la stessa distinta, nella gestione distinta base si indica la distinta per un articolo (l'articolo di riferimento) e in tutti gli altri articoli che hanno la stessa distinta invece di creare anche per loro una distinta base si inserisce l'articolo di riferimento nel campo GRUPPO DISTINTA, in questo modo ereditano la distinta dell'articolo di riferimento.
Stessa logica si applica al _2_GRUPPO CICLO. Da evidenziare il fatto che per default se si specifica un articolo nel campo GRUPPO DISTINTA, questo vale anche per il GRUPPO CICLO (se quest'ultimo è lasciato vuoto). La tabella BRT (Tipo ciclo) permette di modificare questo comportamento.
- _2_Configurazione e Criteri di configurazione, si applicano agli articoli che fanno uso dei concetti di configurazione.
- _2_Catalogo di vendita, se un articolo ha una codifica interna (ad uso della produzione e della gestione interna all'azienda) ed una codifica esterna (ad uso commerciale) in questo campo è possibile indicare il codice esterno.
- _2_Peso e Volume, sono informazioni quantitative associate all'articolo.
- _2_Lotto standard, se compilato fa riferimento al lead time di produzione presente nei parametri di pianificazione.
- _2_Classe Materiali - Programmazione - Gestionale - Valore - Contabile - Fiscale  - Funzionale, permettono la classificazione dell'articolo secondo vari punti di vista aziendali.
- _2_Esclusione da magazzino, se impostato a SI, per l'articolo non vengono generati movimenti di magazzino e viene ignorato dall'MRP. Si applica a materiali codificati ma che non si vogliono gestire a magazzino (es. cancelleria).


### Regole di impostazione valori assunti per i campi
Esistono tre modi per riprendere automaticamente alcuni campi : 

- _2_Da memorizzazione immissione dati. La funzione può essere richiamata dall'utente in qualsiasi momento (immissione/modifica) e sostituisce tutti i valori presenti nei campi con quelli precedentemente memorizzati. In immissione vengono ripresi i valori assuntimemorizzati nell'elemento '*' di memorizzazione multipla. La memorizzazione è tipica dell'utente ma indipendente dal tipo articolo.
- _2_Da valori impostati in tabella BRA per il tipo articolo in gestione. La ripresa si esegue solo in fase di immissione e riporta i campi impostati in tabella. Tali campi si sovrappongono a quelli eventualmente ripresi da memorizzazione video.
- _2_Da domande di costruzione automatica se previsto per il tipo articolo. Se la funzione è attiva e l'utente ha risposto ad alcune domande, tutti i valori presenti nelle risposte vengono portati a video. Fra questi quindi anche quelli eventualmente già ripresi come assunti dalla tabella BRA.
Se la prima domanda per la costruzione del codice richiede come risposta il tipo articolo, deve essere impostata come domanda implicita, perchè il tipo articolo è memorizzato nella schiera di costruzione £SC (riga 2, colonna 1) e quindi può essere recuperato in modo automatico.
Quando viene fatta la prima domanda nella schiera £SC sono memorizzati il codice articolo (riga 1, colonna 1) e il tipo articolo (riga 2 , colonna 1).

