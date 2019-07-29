# Scopo
 * Gestione Vendor Rating, Customer Satisfation, Work Center Rating, ecc...
 * Gestione dati Ente/Articolo tramite l'utilizzo combinato di indici statici e dinamici
 * Gli indici del Rating vengono calcolati sul periodo
 * Valutazione Globale Ente /Articolo


![CQ_VEND_01](http://localhost:3000/immagini/CQVEND_01/CQ_VEND_01.png)
# Definizioni
## Vendor Rating
Obiettivo è quello di valutare in forma  continuativa l'andamento dell'affidabilità dei Fornitori in termini di : 
 * conformità del prodotto
 * rispetto dei termini di consegna
 * osservanza dei termini contrattuali in fatto di valide certificazioni e disponibilità a collaborare per risolvere eventuali situazioni di criticità in essere.

Le informazioni sono da intendersi, quale integrazione e correttivo all'iniziale "Valutazione di Idoneità del Fornitore", come una raccolta continua di dati pesati, inerenti i vari rapporti esistenti tra Azienda e Fornitore, atti a fornire un'immagine sempre più precisa ed attuale sulla reale validità del Fornitore.

Le informazioni per la classificazione del fornitore sono : 
 * andamento della qualità delle forniture
 * andamento delle tempistiche di consegna
 * sensibilità all'aspetto qualitativo del prodotto
 * rispetto della certificazione del prodotto consegnato e dell'obbligo di conservazione documentazioni secondo le prassi stabilite.

La valutazione del fornitore viene quindi ottenuta dalla combinazione pesata di una serie di indici statici e dinamici.

## Customer Satisfation
Il calcolo dell'indice di soddisfazione del cliente viene ottenuto, allo stesso modo del "Vendor Rating" dalla combinazione degli indici dinamici e statici. (es. gli indici dinamici potranno calcolare il rispetto delle date di consegna...ecc..., gli indici statici saranno aggiornati funzione delle interviste sul cliente...ecc.)

## Indici statici
Sono indici che vengono assegnati direttamente dall'utente e sono il risultato di valutazioni attribuite dagli Enti responsabili ed inserite "manualmente nell'archivio;

## Indici dinamici
Sono indici che risultano da elaborazioni eseguite in automatico dal programma sulla base dei dati in archivio del tipo : 
 * andamento della qualità delle forniture,
 * andamento delle tempistiche di consegna,
 * sensibilità all'aspetto qualitativo del prodotto, rispetto della certificazione del prodotto consegnato e obbligo di conservazione dei documenti secondo le prassi stabilite,
 * ......

Per questo tipo di indici il programma apre i diversi archivi disponibili : 
 * Non Conformità
 * Audit
 * Lotti
 * Documentazione
 * Strumenti di misura
 * Fmea
 * Personale
 * Richieste di Intervento

## Indice Globale
è costituito da una combinazione di indici statici e dinamici inseriti in un'architettura la cui complessità è fissata dalla fantasia e dalla capacità di analisi dell'utente vedi figure seguenti

# Costruzione indice globale
![CQ_VEND_02](http://localhost:3000/immagini/CQVEND_01/CQ_VEND_02.png)
# Struttura generale indice
![CQ_VEND_03](http://localhost:3000/immagini/CQVEND_01/CQ_VEND_03.png)
# Calcolo indice globale (versione con utilizzo dell'archivio indici IGREPT0F)
![CQ_VEND_04](http://localhost:3000/immagini/CQVEND_01/CQ_VEND_04.png)
 * _2_Area, rappresenta un macro raggruppamento dei temi di interesse per le valutazioni  effettuate con indici dinamici, ad esempio Area Contabilità, Area Produzione, Area Vendite, Area Zonale, Area Assicurazione Qualità, Area Magazzini, ecc.. (tabella IGA)
 * _2_Tema, identifica con un codice un insieme di dati legati ad un argomento comune, ad esempio tema delle verifiche sugli audit, tema della gestione delle non conformità, tema della fmea, ecc.. (tabella IGT). È utilizzazto per indici dinamici.
 * _2_Livello di sintesi, specifica a quale preciso fattore fare riferimento per la ricerca dei dati relativi ad un indice dinamico, ad esempio articolo, articolo/fornitore, ecc.. (tabella IGS)

![IG_REPT_01](http://localhost:3000/immagini/CQVEND_01/IG_REPT_01.png)
# Tabelle utilizzate dal modulo
### CRM - RATING - INDICI DI RIFERIMENTO
Questa tabella contiene gli indici di riferimento globali del Q9000. Per ogni indice vengono assegnate le intestazioni ed i riferimenti per l'assegnazione agli oggetti dell'azienda (possono essere fornitori, Work-center, clienti, articoli, etc.).
 :  : DEC T(ST) K(CRM)

### CRL - RATING - CAMPI DI RIFERIMENTO
Questa tabella contiene tutti gli indici di riferimento del Q9000 che possono definirsi in tre categorie : 
 * indici statici (assegnati e gestiti manualmente dall'operatore)
 * indici dinamici (calcolati dal programma attraverso Routine dedicate)
 * indici intermedi (sono la combinazione lineare (produttoria) di alcuni degli indici precedenti.

Per ogni indice vengono assegnate le modalità di calcolo ed i riferimenti di merito.
 :  : DEC T(ST) K(CRL)

### CRI - VALUTAZIONI STATICHE
Questa tabella contiene le valutazioni assegnate agli indici statici di riferimento che possono essere definiti a piacere un funzione delle necessità aziendali.
Per questo scopo è possibile creare più sottosettori nella stessa tabella associati ciascuno ad un indice statico ed in riferimento al singolo sottosettore (e quindi al singolo indice) le valutazioni assegnabili.
 :  : DEC T(ST) K(CRI)

### CQY - TIPO GRIGLIA  CONTROLLI
Descrive il significato dei campi legati alla griglia. Collegare questi campi alle tabelle o ad archivi dati.
 :  : DEC T(ST) K(CQY)

# Processo di avviamento ed utilizzo
## Attività iniziale
 * Attivazione del modulo indici (riferimento FU/INDI)
 * Classificazione indici statici, dinamici e globali per il Rating
 * Classificazione periodi di analisi
 * Classificazione valutazioni per indici statici
 * Inserimento tabelle
 * Definizione indici statici, dinamici, globali nelle relative tabelle
 * Inserimento valutazioni statiche per i fornitori, work center, ecc...

## Attività periodica
 * Inserimento e/o modifica valutazioni statiche per i fornitori, work center, ecc...
 * Lancio del calcolo degli indici dinamici
 * Interrogazione Rating
 * Storicizzazione del Rating in un archivio di indici dinamici
 * Stampa Rating
 * Controllo valutazioni statiche/dinamiche
 * Aggiornamento indici

# Definizione dell'indice globale
L'indice globale di valutazione del fornitore, centro di lavoro, ecc.. è impostato tramite una tabella (Tabella CRM) che contiene i riferimenti a tabelle (CRL) le quali a loro volta  contengono dei sottoindici.
La tabella associata ad ogni sottoindice contiene, oltre ai pesi, gli indirizzamenti a tabelle di ordine inferiore o a tabelle di valutazione (CRI)  (per gli indici statici) o ancora, al percorso per il recupero dei valori in archivio (per gli indici dinamici).

## Creazione  indice di valutazione globale del fornitore (IVVG)
![CQ_VEND_08](http://localhost:3000/immagini/CQVEND_01/CQ_VEND_08.png)La tabella dell'indice richiede di indicare i codici del tipo di chiave a cui andrà a riferirsi l'indice; esempi di chiavi sono le triplette : 
 * FO/AR/FASE+EM
 * CL/AR/FASE+EM
 * RI/AR/FASE+EM

Oltre ai campi che definiscono la griglia delle chiavi (i codici :  fornitore/articolo/Fase+EM o altro elemento) adatte per quell'indice, è richiesto di specificare il riferimento alle tabelle dei sottoindici.

Scelta del riferimento per i sottoindici collegandosi con i sottosettori della tabella CRL
![CQ_VEND_09](http://localhost:3000/immagini/CQVEND_01/CQ_VEND_09.png)
Scegliendo uno dei sottosettori si accede ad una tabella di indici dinamici o statici tra i quali si sceglie quello desiderato (oppure naturalmente si può decidere di inserirne uno nuovo).

# Definizione dell'indice Statico
Gli indici statici associati sono definiti mediante una tabella (Tabella CRL) che specifica : 
 * peso attribuito in funzione dell'importanza dell'indice stesso;
 * riferimento alla tabella di valutazione (CRI-**)
 * il sottosettore degli indici collegati

![CQ_VEND_10](http://localhost:3000/immagini/CQVEND_01/CQ_VEND_10.png)
Il valore che il programma calcola per un indice statico è il risultato del prodotto tra il peso e la valutazione assegnata.

![CQ_VEND_11](http://localhost:3000/immagini/CQVEND_01/CQ_VEND_11.png)
# Definizione dell'indice Dinamico
Nel Q9000 l'indice dinamico è  individuato da 3 elementi : 
 * AREA DI PROVENIENZA
 * TEMA DELL'INDICE
 * LIVELLO DI SINTESI

I 3 riferimenti (Area, Tema, Livello), costituiscono le chiavi di accesso ad un archivio in cui sono mantenute le informazioni relative ad una determinata combinazione di codici Cod1/ Cod2/ Cod3/ Periodo.

Associato ad ogni tripletta di chiavi (Area, Tema, Livello), esiste un programma di calcolo che ha il compito di prelevare dai vari archivi disponibili le informazioni (Max 30 valori) richieste in corrispondenza dei fattori specificati.

Per ogni Area / Tema / Livello di Sintesi il programma è predisposto per rilevare un numero massimo di 30 valori. L'aspetto importante di questa gestione è la libertà che viene lasciata all'utente di decidere che tipo di informazioni far recuperare dagli archivi. Con opportune modifiche può inserire nuove caselle nella matrice del tema o modificare quelle esistenti.

Il limite di 30 valori è superato dalla possibilità di combinarli linearmente per definirne dei nuovi fino ad un massimo totale di 99 indici per ognuna delle possibili combinazioni Area / Tema / Livello di Sintesi. Gli elementi presenti nell'elenco con indice 31 e 32 sono un esempio di indici creati dalla combinazione dei primi 30 fattori.

Ogni volta che si lancia il calcolo di un indice globale a cui appartiene l'indice dinamico in oggetto, il programma aggiorna il record (o lo crea, se non esiste) nell'archivio, corrispondente alla combinazione di : 
 * Area
 * Tema
 * Livello Sintesi
 * Cod.1
 * Cod.2
 * Cod.3
 * Periodo

caricando i primi 30 valori del tema :  gli altri indici con codice superiore al 30 non sono archiviati, ma vengono calcolati al momento della consultazione.

Gli indici dinamici associati sono definiti mediante una tabella (Tabella CRL) che specifica : 
 * peso attribuito in funzione dell'importanza dell'indice stesso;
 * il tema dell'indice,
 * il livello di sintesi,
 * l'area di provenienza,
 * il sottosettore degli indici collegati

![CQ_VEND_12](http://localhost:3000/immagini/CQVEND_01/CQ_VEND_12.png)
 * la tripletta area/tema/livello di sintesi selezionata deve essere stata creata con la opzione "Gestione legami area/tema/livello" (cfr INDI) altrimenti si definisce un indice che non ha associato il programma di calcolo.
 * Progressivo griglia questo campo deve essere compilato solo se stiamo trattando un indice dinamico. È il riferimento alla griglia di controllo di un AUDIT eseguito presso un fornitore. In questo caso il programma preleverà il valore risultante dal punto della griglia assegnato e lo tratterà come indice dinamico.
 * Classe di Autorizzazione è un campo controllato dalla tabella 'B£P' (Classi di autorizzazione). Questo campo se diverso da 'blank' definisce dei livelli di controllo per l'accesso e la modifica di detto indice.
 * Set.Indici Collegati é un campo controllato dalla tabella 'CRL' (Campi di riferimento). Il settore Indici Collegati indica a quale raggruppamento di indici, l'indice in questione trae il suo valore. (è il GRUPPO o SOTTOGRUPPO della distinta base). Viene utilizzato solo se l'indice è di tipo 'INTERMEDIO' e cioè risultante dalla produttoria di altri indici che a loro volta possono essere : 
 ** statici
 ** dinamici
 ** intermedi
 * Num.indice in arch. Questo campo deve essere compilato solo se stiamo trattando un indice dinamico o un indice statico. Campo numerico da 0...a...99 che da il riferimento di prelievo (posizione dell'indice) del valore nell'archivio degli indici dinamici o negli indici statici.

# Deviazione degli indici sull'archivio D5COSO0F

Allo scopo di superare il nuemro massimo di 30 indici registrabili tramite l'utilizzo dell'archivio IGSTOR0F, si è attivata la gestione degli indici nell'archivio D5COSO0F, che è lo stesso archivio utilizzato per registrare fino a 100 numeri per griglie di oggetti.

Il passaggio dalla vecchia gestione IGSTOR alla nuova gestione D5COSO si ottiene valorizzando il campo  " Indici su D5 " nella tabella CQ1.

A questo punto l'impianto tabellare necessario per registare gli indici nel D5COSO e collegarli all'indice sintetico CRM si diversifica rispetto a quello descritto nella parte precedente di questo documento, con le seguenti Variazioni : 

* le tabelle CRM e CRLxx restano immutate.
* L'aggancio con gli indici statici resta immutato
* l'aggancio tra gli indici dinamici riferenziati nel sottosettore della CRLxx e le chiavi del D5COSO avviene nel seguente modo : 
**nella tabella CQ$ bisogna codificare un elemento che riporta tra i suoi attributi le stesse  Area-Tema-Sintesi riporatte nell'elemento della CRLxx
**nello stesso elemento della CQ$ sono indicati il contesto D5 (tabella D5S) ed il tema (D5Oxx) dove sono contenuti gli indici che dovranno essre scritti
**nello stesso elemento sono indicati il sottosettore xx della D5R e l'elemento della D5R che permetteranno la scrittura degli indici
**nell'elemento della D5RXX è indicato il flusso di azioni della tabella D5Exx che deve essere attivato
**Nei passi della D5Exx sono descritti i metodi di valorizzazione degli indici specifici del contesto/tema del D5COSO.

Ovviamente per una corretta compilazione di questi legami tra tabelle è raccomandata la lettura dell'help delle tabelle coinvolte : 

 :  : DEC T(ST) K(CQ$)
 :  : DEC T(ST) K(D5S)
 :  : DEC T(ST) K(D5O)
 :  : DEC T(ST) K(D5R)
 :  : DEC T(ST) K(D5E)

# Programmi di calcolo degli indici

Il programma che calcola gli indici contiene le logiche , più o meno parametriche, che attribuiscono valori agli eventi. Per uan comprensione di questi programmi fare riferimento al pgm CQVEN3_SM, che si appoggia sulla tabella IGVQQ



