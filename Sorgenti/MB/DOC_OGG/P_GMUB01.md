# GESTIONE UBICAZIONI

## Generalità
Quando si vuole gestire una giacenza anche da punto di vista fisico nasce l'esigenza di creare le ubicazioni.
Ad esempio :  per gestire un magazzino materiali con scaffalature, ogni scaffale potrebbe essere una ubicazione;  per identificare fisicamente la giacenza dei componenti elettronici presenti vicino alle macchine inseritici nel reparto montaggio si potrebbero identificare le ubicazione dei componenti a piede di macchina.

Di seguito viene esposta le gestione ubicazioni di Sme.up, che si attiva a partire dal seguente formato guida : 

![GMUBIC_01](http://localhost:3000/immagini/MBDOC_OGG-P_GMUB01/GMUBIC_01.png)
le opzioni utilizzabili sono quelle standard, come è standard la sequenza delle videate usate nella gestione.

Il formato di dettaglio è il seguente : 

![GMUBIC_02](http://localhost:3000/immagini/MBDOC_OGG-P_GMUB01/GMUBIC_02.png)
## Campi significativi : 
I campi significativi di questa gestione sono : 

### Ubicazione di riferimento
Si può utilizzare questo campo per far "risalire" l'ubicazione in gestione a quella di riferimento da cui eredita le caratteristiche :  in pratica per gestire in un colpo solo le caratteristiche di un gruppo di ubicazioni tutte uguali si crea la capostipite, a cui si associano tutte le caratteristiche, per tutte le altre si creano codice / descrizione e si indica la capostipite come ubicazione di riferimento, quando si vogliono variare delle caratteristiche su tutte le ubicazioni basta variarle sulla capostipite.

### Tipo ubicazione
identifica la tipologia fisica dell'ubicazione, il tipo ubicazione viene gestito nella tabella GMU, dove si possono specificare dimensioni (lunghezza, larghezza, altezza) dell'ubicazione e peso massimo sopportabile.
Una informazione importante da notare, associata al tipo ubicazione è l'indicazione dei metodi di accesso alla giacenza che sono per ubicazione (usato del motore inferenziale di scelta ubicazione di versamento), per articolo (usato dal motore inferenziale di scelta ubicazione di prelievo), questi metodi di accesso possono essere usati se i motori inferenziali sono basati sul tipo ubicazione.

### Tipo gestione
classifica l'ubicazione dal punto di vista gestionale, il tipo gestione è riferito alla tabella GMG, tra le informazioni presenti la più rilevante è l'indicazione dei metodi di accesso alla giacenza che sono per ubicazione (usato del motore inferenziale di scelta ubicazione di versamento), per articolo (usato dal motore inferenziale di scelta ubicazione di prelievo), questi metodi di accesso possono essere usati se i motori inferenziali sono basati sul tipo gestione ubicazione.

Le altre informazioni :  famiglia contenitori, gestione multi item, gestione multi lotto, blocco ubicazione, ubicazione occupata, sono informazioni che potrebbero essere rilevanti nelle regole di scelta ubicazioni usate dai motori inferenziali

## Particolarità
Nella gestione ubicazione è possibile verificare se questa è occupata (esiste giacenza di materiali nella ubicazione) :  l'interrogazione mostra una lista di ubicazioni, con gli articoli / quantità contenuti.
L'ordinamento della lista ed i valori che vengono presentati è condizionato da un file logico di GMQUAN0F che è definito nella tabella GMF :  inserendo nel campo "Metodo accesso giacenza ubicazione" della tabella GMU un elemento della tabella GMF si usa il logico di GMQUAN associato.
