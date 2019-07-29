# ANAGRAFICA ARTICOLI
## ANAGRAFICA ARTICOLI
Negoziando mette e disposizione un'anagrafica articoli ricca di informazioni e personalizzabile con ulteriori campi. Dal punto di vista dell'interfaccia, l'anagrafica è strutturata in 3 parti. La prima è costituita da una serie numerosa di campi presenti di default per ogni configurazione di Negoziando, presentati in due schermate.
La seconda parte, opzionale, permette di compilare dati personalizzati. Potremo quindi fare in modo che il sistema richieda l'inserimento facoltativo o obbligatorio di qualsiasi tipo di dato venga considerato utile o pertinente al sistema.
La terza è costituita da una serie di informazioni aggiuntive riunite sotto un menu la cui composizione dipende parzialmente dalle impostazioni di Negoziando. Ad esempio, avremo il menu per l'inserimento delle varianti Taglia e Colore solo se l'impostazione di Negoziando ne prevede l'utilizzo.
L'anagrafica è popolabile con metodi di importazione massiva oppure con la compilazione di un singolo articolo per volta. Vediamo questa seconda possibilità in maniera da illustrare i campi disponibili. A parte il Codice articolo, la Descrizione e l'IVA, obbligatori, è possibile selezionare quali campi presentare nelle schermate e se la compilazione è obbligatoria o facoltativa. Come da convenzione di Negoziando, dove il fondo è di colore giallo il dato è selezionabile da tabelle che devono essere già compilate. La maggior parte sono riunite sotto un'unica voce di menu _Principale> Anagrafiche di Base>Gestione Tabelle_. Per i casi restanti indichiamo il differente percorso da seguire.
### Inserimento articoli
Dal Menu _Principale>Anagrafiche di Base>Gestione Anagrafica Articoli_ premiamo Invio anche senza effettuare selezioni. Ci troviamo nell'elenco articoli. Col tasto F6 Inserisci viene richiesto il codice del nuovo articolo che non deve essere già presente e che una volta inserito non sarà più modificabile. Confermiamo con Invio e accediamo alla scheda anagrafica vera e propria. L'articolo viene creato solo dopo aver confermato con Invio la scheda dei campi personalizzati o, in assenza di essa, la seconda scheda dei campi standard. Se l'impostazione lo prevede (Principale >Utilità>Configurazione>Gestione Configurazione Applicativa, 02 Articoli, scheda Articoli, Genera Codici a Barre automatici=SI), viene associato al nuovo articolo un codice a barre di tipo EAN 13. Per la gestione dei barcode vedi anche più avanti il paragrafo Campi aggiuntivi.
### Modifica articoli
Dal Menu _Principale>Anagrafiche di Base>Gestione Anagrafica Articoli_ premiamo Invio anche senza effettuare selezioni. Premiamo Invio sull'articolo da modificare e accediamo alla 1° pagina della scheda anagrafica standard. Le modifiche vengono salvate solo dopo aver confermato con Invio la scheda dei campi personalizzati o, in assenza di essa, la seconda scheda dei campi standard.
Vediamo ora il significato dei vari campi
### Campi standard
 1° scheda
* Descrizione :  la descrizione dell'articolo
 * Descrizione scontrino :  non utilizzata
 * 1°, 2°, 3° Classificazione :  tre categorie merceologiche dell'articolo. Le categorie sono gerarchiche, ovvero il valore della prima Classificazione determina un sottoinsieme selezionabile delle voci della 2° Classificazione che a sua volta permette di selezionare solo alcune voci della 3°. I valori delle classificazioni vanno inseriti preventivamente nella tabella Classi Merceologiche CLAM.
 * Marchio :  il Marchio dell'articolo. Il valore va selezionato tra quelli inseriti nella tabella Marchi MARC.
 * Codice Stagione :  la stagione dell'articolo. Il valore va selezionato tra quelli inseriti nella tabella Stagioni STAG
 * Aliquota IVA :  selezionato dalla tabella Aliquote Iva ALIV
 * Codice Fornitore :  Fornitore di default. Selezione da tabella Fornitori, _Principale> Anagrafiche di Base>Gestione Anagrafica Fornitori
 * Codice etichetta :  etichetta di default per stampa. Tabella Tipi Etichetta ETIC
 * U.M. Gestione Magazzino :  Unità di misura. Tabella Unità di misura UMIS
 * Valuta per Importi/Costi :  divisa di default dell'articolo. Tabella Valute VALU
 * Costo standard :  costo di default
 * U.M. Acq./F. Conv. :  U.M in acquisto. Tabella Unità di misura UMIS
 * Provvigione :  percentuale di provvigione spettante all'agente
 * Trasmetti anagrafica :  l'impostazione su NO fa in modo che l'anagrafica articolo non venga trasmessa automaticamente al database dei punti vendita ma solo nel momento in cui l'articolo diventi di pertinenza del negozio, Questo evita che i PV abbiano un'anagrafica inutilmente troppo corposa. La trasmissione avviene se l'articolo è inserito in ordini a fornitore o da cliente, o se viene generata una movimentazione di magazzino a qualsisasi titolo.
E' possibile modificare parzialmente questo comportamento impostando la trasmissione degli articoli appartenenti ad un singolo Marchio verso un singolo Magazzino, da Utilità > Trasmissioni > Trasmissioni Sede > Trasmissioni articoli per Marchio.
 * Descrizione estesa :  Descrizione aggiuntiva
 * Articolo non gestito a magazzino :  SI fa in modo che l'articolo non venga visualizzato in alcune statistiche. E' consigliabile utilizzare questa impostazione per articoli fittizi come acconti o buoni, oppure su articoli di valore commerciale baso o nullo (shopper).
2° scheda
 * Raggruppamento fiscale :  utilizzabile per la suddivisione in fasce prezzo. Impostando nella tabella Anagrafica Raggruppamenti CRGF un gruppo e nella tabella Fasce di Prezzo per Raggruppamenti FRGF una serie di fasce prezzo legate al gruppo di CRGF, selezionando il gruppo di CRGF l'articolo verrà indirizzato nella fascia di prezzo di appartenenza secondo i valori di FRGF.
 * Categoria Contabile Ricavi :  non utilizzato
 * Abilita C/Vendita :  abilita o meno l'articolo alla gestone in conto vendita ******
 * Gestione Matricole :  *******
 * Voce Doganale :  da tabella Voci Doganali VODO *******
 * Nazione Origine :  provenienza dell'articolo. Da tabella Nazioni NAZI
 * Catalogo :  da tabella Cataloghi Prodotti CATL ********
 * Gruppo articoli :  suddivisione in gruppi da tabella Gruppi Articoli GRAR ******
 * Gruppo gerarchico :  tabella Gruppi Gerarchici GRGE. Gruppo gerarchico non è una semplice tabella doppia entrata ma un albero multilivello di profondità virtualmente infinita. All'articolo può essere assegnato un valore preso da una delle "foglie" dell'albero, cioè un elemento che non abbia nessun altro elemento sotto di se
 * Codice Modello :  selezione di un modello di riferimento. Da  _Principale> Anagrafiche di Base>Gestione Anagrafica Modelli********
### Campi personalizzati
Come anticipato in apertura, Negoziando dà la possibilità di inserire in anagrafica informazioni che non siano già richieste dai campi standard. I campi vengono proposti in una scheda dedicata posta dopo le prime due schede dei campi standard. I dati inseribili possono essere facoltativi o obbligatori, con inserimento libero o selezionabili da un elenco a tendina. Rimandiamo al capitolo DATI PERSONALIZZATI per le istruzioni dettagliate.
### Campi aggiuntivi
In ultimo l'anagrafica propone una lista di voci presenti in base alla configurazione di Negoziando. Descriviamo la modalità di attivazione e il significato.
Le primi 4 voci sono relative alla gestione di Taglia Colore in relazione ai Codice a Barre. Se è abilitata la gestione di Taglia e Colore è possibile inserire un articolo ed esplodere successivamente le taglie e/o i colori con queste due funzioni. Supponendo di avere N taglie e M colori, questo comporta la generazione di NxM nuovi codici a barre, uno per ogni combinazione di Taglia e Colore possibili. Di conseguenza l'articolo inserito non rappresenta più una singola referenza ma NxM articoli differenziati per taglia e colore. In cassa quindi il codice a barre determina univocamente l'articolo con la taglia e il colore esatti. Con la funzione Codice a Barre è però possibile intervenire sui codici a barre degli articoli, sia in modalità Taglia e Colore che in quella unica.


 * 01 Taglie :  Utilità>Configurazione >Gestione Configurazione Applicativa, 02 Articoli, scheda Articoli :  Gestione Taglie=SI.
Si seleziona un codice dalla tabella Taglie TAGL oppure si compila il piano taglie dell'articolo. Viene generato un codice a barre diverso per ogni componente del piano taglie inserito

 * 02 Colore :  Utilità>Configurazione >Gestione Configurazione Applicativa, 02 Articoli, scheda Articoli :  Gestione Colore=SI
SI possono inserire le varianti colore con codice e descrizione. Viene generato un codice a barre diverso per ogni colore inserito.

 * 03 Dimensioni :  Utilità>Configurazione >Gestione Configurazione Applicativa, 02 Articoli, scheda Articoli :  Gestione Dimensioni=SI. Visualizzato solo se Gestione Taglie e Gestione Colori nella stessa scheda sono impostati a NO. ********

 * 04 Codice a Barre :  visualizza i codici a barre associati all'articolo. Se in Principale>Utilità> Configurazione>Gestione Configurazione Applicativa, 02 Articoli, scheda Articoli, Genera Codici a Barre automatici=SI, un codice EAN 13 viene generato automaticamente e abbinato all'articolo in fase di creazione. Se sono stati inseriti dei valori di Taglia e Colore, viene generato un codice a barre per ogni combinazione di taglia e colore. E' possibile modificare gli esistenti, se nella scheda di configurazione è impostato Modifica Codici a Barre=SI.
E' possibile anche inserirne di aggiuntivi col tasto F6. Viene richiesto : 
 ** Codifica barcode : 
 ** Quantità fissa :  1 barcode = 1 articolo;
 ** Peso Variabile - Indicazione del Prezzo :  il codice ha una parte fissa e una che viene compilata col prezzo di vendita.
 ** Peso Variabile - Indicazione del Peso :  il codice ha una parte fissa e una che viene compilata col peso.
Per l'utilizzo dei barcode a Peso Variabile vi rimando al paragrafo ARTICOLI A PESO VARIABILE
 ** Tipo Barcode :  scelta tra tipi differenti di codifica barcode. Selezionando EAN 13 viene effettuato un controllo sulla correttezza formale del codice
 ** Codice Barcode :  il valore del codice a barre
 ** Stagione :  per abbinare una stagione a questo barcode (non all'articolo che ha lo stesso parametro nei campi standard). Da tabella Stagioni STAG
 ** Classe Barcode  :  da tabella EANC
Il tasto F4 Elimina un codice a barre, a patto che non sia stato già utilizzato.

 * 05 Articoli esterni :  sezione in cui inserire il codice che il fornitore (o i fornitori) utilizza per l'articolo.
E' possibile inserire più codici differenti. Se attivata la gestione Taglia/Colore e l'articolo è stato già esploso in Taglia e Colore, è possibile inserire codici relativi all'articolo (cioè senza riferimenti a taglia e colore) oppure codici che fanno specificatamente riferimento a un singola combinazione di Taglia e Colore. Negli altri casi invece il codice inserito si riferisce direttamente all'articolo. I codici inseriti in questa sezione vengono utilizzati dal sistema nelle ricerche per barcode. Premendo F6 Inserisci viene richiesto : 
 ** Codice Taglia/Codice Colore :  visualizzati se attivata la gestione Taglia/Colore
** Fornitore :  il fornitore che utilizza il codice che si sta inserendo. Opzionale
** Codice :  Il codice utilizzato dal fornitore. Alfanumerico, fino a 50 caratteri. Il sistema utilizzerà questo codice per la ricerca.
** Codice Colore/Taglia Esterno :  i codici Colore e Taglia utilizzati dal fornitore esterno
** Codice Fornitore Esterno :  ************


 * 06 Codici statistici :  Serie di dati aggiuntivi legati a attributi di tipo statistico inseriti nella tabella Titoli Statistici STAT e Codici Statistici STAC. STAT va compilata con la tipologia di attributi che si intende dare agli articoli e STAC con i valori di ogni tipologia.
Ad esempio potremmo avere : 
     STAT =  1 Genere . . . . . . . . . .  STAC =  D Donna
                                                                      U Uomo
                   2 Target . . . . . . . . . . .               N Neonato
                                                                      R Ragazzo
                                                                      A Adulto
Il sistema propone quindi il campo GENERE che compilo con D o U e il campo TARGET dove posso inserisco N, R o A.
Le tipologie disponibili sono 10 contrassegnate dai numeri da 0 a 9, i valori non hanno limitazioni.

* 07 Parametri Alimentari :  Utilità>Configurazione >Gestione Configurazione Applicativa, 02 Articoli, scheda Articoli :  Gestione Alimentare=SI

 * 08 Listini d'Acquisto :  nel caso in cui l'articolo sia acquistato da fornitori differenti, è possibile inserire qui la lista. Premendo il tasto F6 viene proposta la maschera i cui inserire : 

 ** Fornitore :  un fornitore deve comparire solo una volta in questa lista *********Viene replicato il fornitore e costo standard?
 ** Costo Lordo :  il prezzo di listino al lordo sconti
 ** Valuta :  da tabella Valuta VALU
 ** % sconti :  3 sconti applicati in cascata
 ** Tabella sconti :  da tabella CSCO
 ** Applica sconti Fornitore :  ***************
 ** Esamina Struttura Sconti :  ***********
 ** Costi Colori/Taglie :  **********

 * 09 Listini di Vendita :  mostra l'elenco dei prezzi dell'articolo. L'articolo può essere inserito in listini diversi e all'interno dello stesso listino può comparire più volte con periodi di validità differenti. Con F6 si inserisce un nuovo prezzo : 
 ** Codice Listino :  da tabella Listini Vendita LIST
 ** Da data Validità/A data Validità :  il periodo entro il quale l'articolo assume questo prezzo all'interno del listino indicato. Se l'articolo è già stato inserito nello stesso listino in un periodo sovrapposto, anche parzialmente, il prezzo utilizzato nel sistema durante il periodo di sovrapposizione è quello del prezzo inserito per ultimo
 ** Prezzo Lordo :  al lordo degli sconti
 ** Valuta :  da tabella Valuta VALU
 ** % sconti :  3 sconti applicati in cascata
 ** Tabella sconti :  da tabella CSCO *******
 ** Tipo Prezzo :  Normale / Promozione ***********
 ** Prezzo Colori/Taglie :  **********
 ** Nr. Punti tessera fidelity :  **********
 ** Applica sconti Fidelity :  *************

 * 10 Parametri Dimensionali :  dati di peso netto, tara, volume, altezza, larghezza e profondità.

 * 11 Parametri generali Riassortimento :  permettono di stabilire i parametri di riassortimento dell'articolo. I parametri sono : 
 ** Scorta minima :  se la DISPONIBILITA' (non la semplice GIACENZA) è minore di questo parametro l'articolo è considerato sottoscorta e rientra nelle selezioni impostate dai criteri di Riassortimento. Vedi paragrafo dedicato per il calcolo della disponibilità e le politiche di riassortimento.
La Disponibilità è definita come : 
Giacenza + Ordinato + In Arrivo + Richiesta - Impegnato - Allocato
 ** Scorta Massima :  il livello al quale viene riportata la disponibilità dell'articolo dal riassortimento a meno di politiche di reintegro particolari
 ** Quantità per confezione :  il numero di pezzi contenuti nel package del fornitore
 ** Controllo analitico su ordini centralizzati :  SI tiene suddivisa la quantità di riassortimento per singolo magazzino, NO invece considera la somma delle quantità ordinate senza distinzione di magazzino. La prima ipotesi obbliga a ordinare sempre un numero di confezioni intere per ogni magazzino, la seconda permette invece di ordinare solo il numero di confezioni necessario al raggiungimento del totale ordine e poi ripartire il contenuto tra i vari magazzini.
Es :  Quantità per confezione=6
Mag 1 :  riassortimento di 2 pz.
Mag 2 :  riassortimento di 3 pz.
Con la prima ipotesi devo ordinare 1 conf. (6 x 2= 12pz.) per ogni magazzino, con la seconda solo 1 confezione (6 pz) e suddividerli tra i due negozi.
 ** Quantità minima Riassortimento :  la quantità minima che fa aprire un riassortimento
 ** Quantità minima Acquisto :  la quantità minima che fa aprire un ordine di acquisto
 ** Tempo approvvigionamento giorni :  non utilizzata
 ** Codice curva :  curva storica della vendita dell'articolo. Utilizzabile per predire le vendite future e quindi pianificare più correttamente il riassortimento.

 * 12 Parametri Riassortimento per Magazzino :  permette di stabilire quantità minima e massima di riassortimento diversi da quelle dei Parametri Generali, validi solo per singolo magazzino. All'inserimento con F6 infatti viene richiesto il magazzino, poi : 
 ** Scorta Minima, Scorta Massima :  sostituiscono i valori impostati nei Parametri Generali per il magazzino indicato
 ** Da riassortire :  se l'articolo sia da riassortire o meno
 ** Ordinabile a fornitore :  se l'articolo sia da ordinare o meno al fornitore.

 * 13 Relazioni


 * 14 Kit :  Utilità>Configurazione >Gestione Configurazione Applicativa, 02 Articoli, scheda Articoli :  Gestione Kit=SI vedi
- [Gestione Kit Articoli](Sorgenti/MB/DOC_OPE/NGBASE_23)

 * 15 Distinta Base :  Utilità>Configurazione >Gestione Configurazione Applicativa, 02 Articoli, scheda Distinta Base :  Gestione Distinte Base=SI vedi
- [Gestione Distinta Base](Sorgenti/MB/DOC_OPE/NGBASE_24)

 * 16 Oggetti Multimediali :  permette di associare all'articolo un contenuto multimediale come ad esempio un'immagine o un video. Nella tabella Oggetti Multimediali OGGM è possibile creare una regola per associare dinamicamente l'immagine all'articolo. Qui invece possiamo effettuare l'abbinamento di un contenuto mm premendo F11 e selezionandolo. Con Invio Seleziona invece vediamo l'oggetto.  (Vedi Oggetti multimediali per le regole)
