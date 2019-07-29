# Documentazione su server Wiki
## Introduzione
E' possibile pubblicare su server Wiki tutta la documentazione Sme.UP a livello di collana, book o singolo documento.

## Generazione e pubblicazione di documenti
La generazione e pubblicazione di un documento/book/collana crea uno o più file in formato WIki e li porta su un server JSPWiki.
Per maggiori informazioni su JSPWiki
[http://JSPWIKI.ORG](http://JSPWIKI.ORG)
### La generazione
La fase di generazione dei file Wiki prepara i file in formato Wiki.
Tali file vengono posizionati nella cartella **LoocUP_DOC** sul Desktop utente All'interno di questa cartella ne viene creata una ulteriore il cui nome dipende dalla lingua di generazione :  se si genera documentazione in italiano si chiamerà WIKIIT, in inglese WIKIEN, e così via.
A fronte della generazione di documenti in formato Wiki, in tale cartella saranno presenti file con estensione .S02 che conterranno i parametri di pubblicazione e file .S06 che contengono il documento Wiki vero e proprio.
La generazione è soggetta ad una variabile che indica dove reperire le immagini linkate in essa, tale variabile è SME.IMG.WEB.
### La pubblicazione
I file generati come descritto al punto precedente, qualora vengano impostati i parametri necessari, possono essere, contestualmente alla fase di generazione sottoposti ad una ulteriore fase che li pubblica direttamente attraverso un server JSPWiki.
La parametrizzazione del setup che permette la pubblicazione diretta tramite il server JSPWiki è rappresentata nell'immagine seguente
![B£DOCU_29](http://localhost:3000/immagini/B£DOCU_16/BXDOCU_29.png)Se viene impostato Sì nel parametro **Pubblica**, il file verrà spostato sul server Wiki e versionato.
### Parametri per la pubblicazione
La pubblicazione è soggetta ad una serie di variabili che indicano il server di pubblicazione, l'utente e la password di collegamento, il percorso di pubblicazione. Più in dettaglio

- Variabile WIK.SYS :  nome del server Wiki
- Variabile WIK.USR :  utente di collegamento
- Variabile WIK.PWD :  passowrd dell'utente di collegamento
- Variabile WIK.PER :  percorso di pubblicazione

### Generazione e pubblicazione automatica
La richiesta di generazione, anche con l'opzione della pubblicazione, può essere inserita anche in una sequenza di generazione (flusso).

Abbiamo quindi le seguenti possibilità di generare/pubblicare documenti : 

- Manuale di un singolo documento
- Automatica di un singolo documento
- Manuale di un book di una applicazione
- Automatica di un book di una applicazione
- Manuale di tutti i book delle applicazioni (collana)
- Automatica di tutti i book delle applicazioni (collana)


La generazione automatica presuppone un'architettura in cui Loocup è installato su un server, è attivo e l'AS400 è a conoscenza di questo server Loocup.

_3_NOTA :  La generazione automatica scandisce la lista delle applicazione, poi verifica l'esistenza dei  vari tipi di membri di documentazione (operativa, applicativa, tecnica, di sviluppo) e procede alla generazione/pubblicazione. Non vi è nessun controllo sulla validità del contenuto.  La scelta del metodo è a totale discrezione del responsabile dei manuali, anche se di default l'opzione usata è la prima illustrata.

## Consultazione del sito Wiki
Il sito Wiki è consultabile attraverso un normale browser all'indirizzo
[http://wikidoc.smeup.com](http://wikidoc.smeup.com)
![B£DOCU_30](http://localhost:3000/immagini/B£DOCU_16/BXDOCU_30.png)Nella sezione di sinistra è possibile selezionare la lingua (di default è italiano).
E' inoltre possibile entrare in navigazione attreverso la lista delle applicazioni o i tipi di manuale previsti (Applicativo, Operativo, Sviluppo, Tecnico, Visione)

## Autorizzazione ai documenti
Allo stato attuale non è gestito nessun tipo di autorizzazione in lettura, non è invece prevista la possibilità di modificare il contenuto dal sito Wiki.

## Note tecniche
