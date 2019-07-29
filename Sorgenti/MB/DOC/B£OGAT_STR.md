# Introduzione
SmeUp è un software gestionale ad oggetti applicativi e pertanto, in linea con gli standard comuni dell'object oriented, tutte le entità che operano al suo interno sono concepite come oggetti con i propri attributi e metodi e disposti secondo una logica di ereditarietà.


## Limiti dei linguaggi object oriented
La rapida evoluzione della tecnologia e di conseguenza anche dei linguaggi di programmazione ha portato a sviluppare linguaggi robusti come java e delphi e in parallelo l'illusione che con questi si potessero rappresentare in maniera ottimale le diverse sfaccettature del reale. A dire il vero questi linguaggi hanno dei limiti intrinseci che possono indurre chi li utilizza, in maniera spesso inconsapevole, a forzare il reale ai vincoli del linguaggio, la realtà allo strumento.

I limiti principali di questi linguaggi possono essere enucleati in questi due punti : 


- Ogni oggetto deve ereditare da un'unica classe padre, è vero che questo è stato un aggiustamento introdotto per evitare l'enorme confusione che veniva a crearsi con la multiereditarietà ed è vero che l'utilizzo di interfacce consente di superare in parte il problema, ma è pur vero che nella realtà ogni oggetto a seconda del contesto in cui viene utilizzato può essere concepito come erede di una classe piuttosto che di un'altra cioè esiste una sorta di polimorfismo trasversale alla cui rappresentazione java e come lui ogni altro linguaggio di programmazione risulta del tutto inadeguato. Un cliente ad esempio potrebbe in casi particolari anche essere un fornitore.

- Le definizioni delle classi in java sono fatte su files di testo di tipo *.java, pertanto ogni precisazione introdotta alla definizione in termini di attributi e di funzioni richiede sempre l'intervento sul codice, in termini aziendali di un programmatore che aggiunge codice, compila e riaggiusta l'ambiente. Le definizioni spesso dipendono da chi le dichiara, cioè essendo astrazioni eseguite da qualcuno in un qualche contesto possono essere soggette a diversi tipi di interpretazione. Il rendere le classi su un file di testo rende difficile la modificabilità delle stesse, un prodotto object oriented deve poter consentire all'utente la modificabilità delle proprie definizioni in maniera interattiva, le definizioni stesse delle classi devono poter essere oggetti manipolabili.


Questi limiti sono intrinseci nei linguaggi orientati ad oggetti attuali e il loro utilizzo deve sempre essere fatto con la consapevolezza dei medesimi.
Il fatto che SME.UP sia un prodotto slegato da tali linguaggi e che il concetto di oggetto non sia tradotto su un file di testo, ha consentito che esso potesse anche indirizzarsi nella gestione del polimorfismo trasversale e nella possibilità di oggettivare le stesse definizioni dei propri oggetti di lavoro.

# Oggetti in SME.UP
Ogni oggetto, per definizione, è identificato da un insieme di attributi e di funzioni dette metodi che lo caratterizzano e si innesta in una struttura ad albero secondo una logica di ereditarietà che discende da un oggetto padre. Padre di tutti gli oggetti è l'Oggetto in quanto oggetto, che è l'astrazione maggiore che si possa fare su un'entità.

## Oggetto applicativo o MetaOggetto
In Sme.Up l'oggetto base, il padre di tutti gli oggetti è l' 'Oggetto applicativo' (OG) o 'Metaoggetto' (ossia oggetto che, sta al di sopra degli oggetti, e ne descrive la struttura delle informazioni); esso identifica una generica entità all'interno del gestionale e costituisce l'astrazione maggiore che si può fare su tali entità.
OG ha attributi e metodi propri, eccone l'elenco


- attributi di OG : 
-- Lunghezza oggetto
-- File master
--- se oggetto persistente indica il nome dell'archivio fisico
-- Accesso Master
-- Oggetto con Numeri?
-- Script per query
-- Tipo oggetto base
-- Par. oggetto base
-- Oggetto sostituito con
--- se oggetto deprecato
-- Oggetto deviato su
--- se oggetto deviato sul altro oggetto
- funzioni di OG : 
-- Sintesi
-- Parametri
--- Categoria
-- Listini
--- Area
--- Capitolo
--- Sezione
-- Descrizioni in lingua
-- Legami
-- Regole
-- Esponenti di Modifica
-- Alias
--- Contesto


Questo pacchetto di funzioni e metodi per effetto dell'ereditarietà viene reso disponibile a tutti gli oggetti figli che possono valorizzarli con costanti specifiche. L'accesso a tali meta-informazioni verrà precisato nel paragrafo relativo alla routine £OAV.
## Attributi di un oggetto

Ogni entità applicativa in SmeUp è identificata da un pacchetto di attributi ereditati o specifici. Essi possono essere così classificati


- Attributi Interni (tipo 'I') :  sono gli attributi definiti sul file fisico associato all'oggetto;non sono presenti in oggetti non persistenti.
- Attributi Intrinseci (tipo 'J') :  attributi composti o 'calcolati' o 'intrinseci'.
- Parametri (tipo 'P') :  sono attributi definiti dall'applicazione ma non necessariamente gestiti dall'utente. Si impostano nella tabella B£N specificando il sottosettore e si classificano in categorie nella tabella C£E che vengono poi agganciate all'attributo primario dell'oggetto.
- Attributi Derivati (Tipo 'R') :  sono attributi di attributi ossia attributi di oggetti riferiti dall'oggetto corrente; vengono portati in primo piano ossia considerati come attributi primari dell'oggetto corrente attraverso programmi di tipo B£OA_DE_XX.
- Attributi Utente (Tipo 'U') :  sono attributi definibili liberamente dall'utente secondo le proprie esigenze vengono impostati su programmi creati specificatamente dall'utente.


Ogni attributo in realtà poi è un riferimento ad esso e quindi 'apre' la possibilità di indagine sull'oggetto da esso riferito.
Questa mappa diversificata di tipologie di attributi e la referenza di ogni attributo ad altri oggetti offre un'enorme libertà di azione nel definire le caratteristiche di un oggetto e di navigazione nella rete delle istanze.
L'intera gestione degli attributi di un oggetto è delegata alla /copy  £OAV; nel paragrafo 4 ne viene descritto  il funzionamento.

## Funzioni su un oggetto
La natura di un oggetto è anche descritta da un pacchetto di funzioni. In genere si distinguono in Funzioni generali (proprie dell'oggetto applicativo)  piuttosto che in Funzioni specifiche dell'oggetto (individuato da tipo oggetto, parametro e attributo primario), piuttosto che in Eventi (inserimento, copia, modifica) e in Azioni  associate ad eventi (ridefinibili e componibilitramite il concetto di flusso di azioni)
SmeUp attraverso i concetti di parametri e di azioni gestisce con estrema libertà la definizione di un oggetto disponendo di caratteristiche impostabili, cosa che in un normale linguaggio di programmazione ad oggetti è fattibile solo intervenendo a livello di codice.

## Ereditarietà
L'ereditarietà è un altro elemento essenziale di una architettura che si definisca 'ad oggetti'. Essa consiste nella propagazione degli attributi delle classi padre sulle figlie. In SmeUP esistono diversi strumenti per rendere l'ereditarietà. La figura sotto dà uno stralcio esemplificativo delle principali casistiche.

![BLV0002-01](http://localhost:3000/immagini/B£OGAT_STR/BLV0002-01.png)
### Ereditarietà di primo livello (Tipo Oggetto)
Il primo livello di ereditarietà si ottiene attraverso il Tipo Oggetto come si può vedere nello schema. La tabella che contiene i tipi oggetto è la *CN sottosettore TT.
Esempi di oggetti applicativi sono : 

- CN :  contatti
- AR :  articoli
- TA :  tabella
- D8 :  data

Menzione particolare merita l'oggetto OG che è l'oggetto definizione di classe. Le sue istanze infatti sono le definizioni dei diversi oggetti applicativi e con esso è possibile attuare le estensioni delle diverse classi.
### Ereditarietà di livello superiore al primo

I livelli successivi di ereditarietà si possono ottenere attraverso il tipo parametro, attraverso la definizione di un attributo primario oppure seguendo entrambe le strade.


- Ereditarietà attraverso il Tipo Parametro (TP)

Il tipo parametro è un campo di dieci caratteri in cui in base al tipo oggetto scelto è possibile impostare un elenco di valori con cui identificare l'oggetto erede. Attualmente il massimo numero di parametri in sequenza previsti è tre. Tali valori sono contenuti in tabelle e dunque estendibili.
I contatti hanno ad esempio un unico livello. Due ne ha l'oggetto tabella TA e tre l'oggetto PA pratica amministrativa.

- Ereditarietà attraverso l'Attributo Primario (AP)

E' un attributo impostabile attraverso la tabella tipo_nome_oggetto; ad esempio per l'oggetto AR articoli esiste la tabella BRA TIPI_ARTICOLI che definisce l'attributo primario per gli articoli. Si può combinare con un tipo parametro :  per i clienti che sono identificati con il tipo parametro CLI sull'oggetto CN, ad esempio, si possono specializzare attraverso l'attributo tipo cliente.


## Oggetti deprecati e Oggetti deviati
Lo sviluppo storico del prodotto ha portato ridefinire più volte il portafoglio degli oggetti disponibili;  si sono così creati oggetti deprecati perché sostituiti da altri o rinominati, nellatabella *CNTT compaiono ad esempio l'oggetto 'CL' Cliente o l'oggetto 'FO' Fornitore, rimpiazzatirispettivamente dalle specializzazioni 'CLI' e  'FOR' dell'oggetto CN ma utilizzati ancora ampiamente nei moduli più vecchi del prodotto come la qualità. (Ricordo che 'deprecato' non significa non utilizzato, ma semplicemente che se ne sconsiglia l'uso laddove possibile perché se ne prevede la rimozione).
La catalogazione di tutti gli oggetti deprecati è allo stato attuale delle cose 'difficoltosa'. Qua sotto elenchiamo i principali oggetti deprecati e i rispettivi rimpiazzamenti : 

- CL
-- CNCLI
- FO
-- CNFOR
- BA
-- CNBAN
- AG
-- TAAGE
- PG
-- OG*PGM
- PU
-- OG*USRPRF

Per Deviazione di oggetti si intende l'operazione di reindirizzamento di un oggetto su un altro oggetto per cui ad esempio quelli che per un'azienda sono i clienti per un'altra potrebbero esserei fornitori o gli agenti, oppure all'interno della stessa azienda gli agenti potrebbero anche figurare come clienti. La mappatura di queste deviazioni è tracciata nelle tabelle B£O nel caso di oggetti generici e B£I per la deviazione di oggetti tabella 'TA'.
La deprecazione e deviazione di un oggetto sono attributi generici dell'oggetto, pertanto sono attributi riferibili all'oggetto applicativo OG. Attualmente se si vuole sapere se un oggetto è stato rimpiazzato o agganciato ad un altro oggetto è sufficiente consultare i meta-attributi.

## Decodifica (£DEC)
Per verificare l'esistenza di un oggetto e ricavarne alcune caratteristiche descrittive, SmeUp  rende disponibile la routine di decodifica £DEC; essa è soprattutto usata per verificare l'esistenza di un oggetto e risolve al suo interno la deviazione e deprecazione di oggetti.

# Oggetti persistenti e Interfacce
Con il termine 'persistenza' di informazioni si intende identificare quel tipo di dati che persistono all'esecuzione di un processo perchè vengono archiviate in opportuni files fisici. Un oggetto si dice persistente quando possiede uno o più archivi fisici su cui salvare le proprie istanze. Non tutti gli oggetti di SmeUp sono persistenti, oggetti come il Numero (NM) o la Data (D8) non hanno necessità di persistere da sé su un archivio, lo hanno solo in qualità di  attributi di altri oggetti.

In genere ogni oggetto persistente ha un programma specifico di gestione (manager) che implementa i metodi di salvataggio, aggiornamento, creazione e visualizzazione e altre funzionalità strettamente collegate con la persistenza.

SmeUp possiede i propri programmi di gestione ma consente anche di agganciare programmi manager di applicazioni diverse da SmeUp. Questo è stato possibile introducendo la distinzione tra il livello di interfaccia e il programma di gestione.

![BLV0002-02](http://localhost:3000/immagini/B£OGAT_STR/BLV0002-02.png)
Per ogni oggetto viene creato un programma interfaccia, una /copy, che ha il compito di indirizzare le richieste anche su programmi gestionali diversi da quelli forniti da SmeUp. E' possibile così per un cliente che vuole passare a SmeUp conservare intere strutture del vecchio applicativo o evitare migrazioni di archivi.
L'elenco delle sezioni dell'applicativo che possono essere agganciate a sistemi diversi da SmeUp è fornito dalla tabella B£1.
Il programma interfaccia è una /copy formalmente viene denominato con '£IXX' dove XX è il codice dell'oggetto, talvolta anche '£IFXX'. Esso a sua volta chiama un programma che si innesta sull'applicativo specifico e denominato 'B£IXX_xx' dove xx è un abbreviativo dell'applicazione, nelcaso di SmeUp è 'SM'e valorizzato dalla B£1 in fase di inizializzazione. Questo programma adeguale informazioni in uscita all'applicativo gestionale e in ingresso a SmeUp.

# Gestione Attributi (£OAV)
Nella architettura ad oggetti ogni singolo elemento è definito da un pacchetto di caratteristiche proprie o ereditate che lo identificano dette attributi. L'intera gestione degli attributi di un oggetto in SmeUp è affidata alla routine £OAV che consente di creare, aggiornare, ricercare attributi e valori. Occorre innanzitutto precisare che attualmente tale routine non risolve deprecazione e deviazione di oggetti. Nel caso in cui ci si trovi in queste situazioni occorre quindi operare lo switch di oggetto prima di richiamarla.

Per questa routine sono disponibili due programmi interattivi. Il programma di test e quello attivabile tramite comando up oav.

![BLV0002-03](http://localhost:3000/immagini/B£OGAT_STR/BLV0002-03.png)Le informazioni descrittive degli attributi di un oggetto sono archiviate nel file B£SLOT0F che presenta in chiave due oggetti con relativi parametri. Questo consente anche di definire caratteristiche tipiche di un oggetto solo se questo ha una particolare relazione logica con un altro oggetto. In questo caso la ricerca dell'attributo nel file avviene prima considerando entrambi i parametri poi solo il primo, quindi solo il secondo e per finire non considerandone nessuno. Sul record viene anche salvato il programma che gestisce l'attributo

L'aggiornamento di massa del file avviene col metodo COS che imposta sul file il nome del programma di ricerca. Ciascun tipo di attributo ha uno specifico trattamento.


## Attributi Interni 'I' e intrinseci 'J'
I primi sono le informazioni che risiedono sul file e vengono decodificati con radice 'I'.
I secondi 'J' sono valori che possono essere direttamente ricavati dalle informazioni che risiedono sul file, ad esempio attributi calcolati, attributi secondari (cioè attributi di un oggetto di cui si ha codificata la chiave sull'oggetto corrente) che si vuole portare in primo piano, o attributi comunque ricavabili dalle sole informazioni che risiedono sul record. Entrambi vanno elencati in una schiera all'interno del programma 'B£OA_XX' con le relative descrizioni il tipo di oggetto ed eventualmente anche l'oggetto secondario.
Il metodo COS di caricamento del file degli slots legge tali schiere e immette i valori su file Nel valorizzare il dato sul programma di gestione dell'attributo, prima di scrivere il record, consulta la tabella B£X di deviazione programmi e nel caso l'attributo abbia un programma deviato lo scrive sullo slot. In questo modo nella fase di ricerca del valore, poiché la routine si appoggia unicamente sulle informazioni descrittive del file degli slots, lancia il programma salvato su file.
Come caso di studio il membro B£OA_CN che gestisce gli attributi interni e intrinseci dei contatti, si tenga conto che tutti i tipi di contatto vengono archiviati sull'unico file BRENTI0F non occorre quindi utilizzare programmi specifici per Clienti, Fornitori o Aziende per mapparne attributi.

## Attributi derivati 'R' (deprecato)
Col termine attributi derivati si intendono gli attributi secondari ossia relativi ad un oggetto puntato dall'oggetto corrente. Attualmente questo tipo di attributi vengono gestiti come attributii intrinseci di tipo 'J' e il loro utilizzo in modo separato è deprecato. Tuttavia l'evoluzione storica del prodotto ha portato a scrivere programmi di tipo B£OA_DE_XX per questi specifici attributi ed attualmente la routine £OAV chiama in automatico tali programmi.
Esempi sono il B£OA_DE_DR e il B£OA_DE_DO per la gestione testate e righe documento.

## Parametri 'P'
Sono definibili in maniera arbitraria dall'utente per qualsiasi oggetto. Si impostano sulla tabella B£N nello specifico sottosettore. Si raggruppano poi in categorie o classi di parametri nella tabella C£E, e il codice della categoria viene inserito nelle caratteristiche dell'attributoprimario dell'oggetto (per l'articolo il Tipo Articolo, per intendersi).
Le informazioni sono salvate sull'archivio parametri associati ad un oggetto ossia sul file fisicoC£CONR0F  letto tramite la /copy £C£E.

## Attributi Utente 'U'
Vengono definiti direttamente dall'utente col metodo GES della /copy OAV, va indicato il programmaspecifico da richiamare che viene salvato sul B£SLOT. La decodifica 'U' è indispensabile perché cablata nei programmi di gestione.

## Meta-attributi
Sono gli attributi ereditati dall'oggetto applicativo OG e valorizzati con costanti specifiche perl'oggetto erede. La loro visualizzazione è possibile tramite comando up fun, che verrà meglio esplicata al paragrafo successivo, impostando come oggetto OG e come tipo oggetto la specializzazione che si intende indagare. Con la funzione 7 Attributi si visualizzano tali informazioni.

# Gestione Funzioni (£FUN)
Ogni oggetto si caratterizza oltre che per gli attributi anche per il pacchetto di funzioni che possono essere applicate ai propri dati. Nel lessico dell'object oriented tali funzioni sono comunemente chiamate 'metodi' dell'oggetto e possono essere rese disponibili o meno agli oggetti eredi.
La gestione dei metodi in SmeUp è affidata alla routine £FUN; attualmente tale routine risolve deprecazione e deviazione di oggetti.

Il suo funzionamento può essere schematizzato come nella figura seguente : 

![BLV0002-04](http://localhost:3000/immagini/B£OGAT_STR/BLV0002-04.png)
L'elenco delle funzioni in SmeUp di ogni oggetto è visibile attraverso il comando up fun che apre una finestra di dialogo ripartita in tre sezioni : 

- Funzioni Generali (proprie  di ogni oggetto applicativo)
- Funzioni Interne (proprie dell'oggetto specifico)
- Funzioni Utente (definite liberamente dall'utente).

Tutte queste funzioni sono soggette ad autorizzazione. Al tema oggetti e autorizzazioni viene riservato un paragrafo a parte

![BLV0002-05](http://localhost:3000/immagini/B£OGAT_STR/BLV0002-05.png)
## Funzioni Generali
Sono le funzioni che si possono applicare ad un oggetto generico, sono funzionalità generiche di analisi dell'oggetto in quanto oggetto. Eccone l'elenco : 

### Funz. Generali oggetto : 
Si tratta delle funzioni derivate dall'oggetto in quanto erede dell'oggetto applicativo. Sono le funzioni della definizione della classe oggetto applicativo.

### Funz. Generali Tipo oggetto : 
Si tratta delle funzioni derivate dall'oggetto in quanto erede dell'oggetto tipo oggetto.
Visualizza in formato G18 l'elenco di tutte le funzioni sull'oggetto corrente anche quelle di LoocUp suddivise in funzioni interne, azioni utente e flussi oggetto.

Le funzioni interne sono quelle specifiche dell'oggetto; si veda il prossimo paragrafo per dettagli.

L'elenco delle azioni disponibili è il seguente : 

A-        Azioni eseguibili
I-        Creazione
C-        Copia
P-        Pre Eliminazione
D-        Post Eliminazione
F-        Pre Modifica
M-        Post Modifica
V-        Visualizza
K-        Collegamento
S-        Scollegamento
E-        Esecuzione
J-        2° collegamento (CoGe)
L-        2° scollegamento (CoGe)
O-        Riferim. origine post Delete
B-        Batch

Il primo, le 'A-XX' sono le azioni utente, Tutte le azioni vengono cercate prima per tipo oggetto + parametro e nel caso in cui non vengano trovate, le si cerca solo per tipo oggetto. Nel caso gli oggetti siano tabelle la ricerca viene fatta prima sul sottosettore se significativo.

Le azioni vengono definite nella tabella B£J nel sottosettore specifico dell'oggetto, occorre specificarne lo stato di attivazione per renderle visibili. I raggruppamenti sono invece definiti nella tabella B£H che viene interpellata dalla £FUN in fase di esecuzione o ricerca di funzioni. La procedura esplode l'elenco delle funzioni chiamate per azione se attive.  Nel caso incui non vengano trovate azioni o non si sia autorizzati l'elemento compare in rosso. In questo modo è possibile inserire una sequenza di funzioni sulle azioni significative dell'oggetto come la copia, l'inserimento o la modifica che vengono attivate in sequenza e nell'ordine fissato all'atto di esecuzione dell'azione.

4. Proprietà oggetto, visualizza il contenuto dell'istanza.
5. Immagini
7. Attributi :  elenca tutti gli attributi dell'oggetto
8. Numeri :  elenca gli attributi numerici

## Funzioni Interne
Sono le funzioni specifiche dell'oggetto caratterizzato da tipo oggetto/ parametro e attributo primario (se definito). Vengono elencate nel programma B£FUN0_XX che ne carica la schiera specificando il gruppo di autorizzazione e ne gestisce l'esecuzione.
La chiamata del numero attiva la funzione corrispondente sull'oggetto.

## Funzioni Utente
Si tratta delle azioni A-XX viste al punto 3 del paragrafo precedente. A differenza delle altre azioni che vengono eseguite in sequenza e in modo automatico al verificarsi dell'evento, queste compaiono anche nel menù dell'up fun e possono così essere chiamate singolarmente.

# Creazione di un nuovo oggetto
## Creazione Step by Step
- Definizione in tabella *CNTT                                            VO
  Nome, Significato, Lunghezza massima
- Definizione in programma B£DEC3 del parametro                               MB DOC_VOC
  Oggetto e obbligatorietà
- Implemento le funzioni base sull'oggetto (interfaccia)                 £VOC TSTVOC B£VOC0
  . Ricerca
  . Verifica
- Definisco l'oggetto in B£DEC0 (richiamando la funzione base)    £IVO
- Implemento la gestione degli attributi                                 B£OA_VO
  . Attributi I/J e scrittura in B£SLOT
- Definisco le funzioni di gestione                                       £A5A per cespiti
  . Definizione classe di autorizzazione alla gestione                   Come il pgm di gestione
- Definisco note strutturate                                              N/A
- Definisco parametri                                                     N/A
- Definisco stati                                                          N/A
- Definisco flussi in tabella B£H                                         I-VO M-VO ecc
  . Nel caso scrivo il programma B£FUN0_XX                               Sarebbe B£FUN0_VO
- Implemento la gestione degli attributi                                 Sarebbe B£OA_VO
- Decido se gestire tabella oggetti B§O
- Eventuale programma "inizializzatore"
  . Flusso di creazione (B£F) e assegnazione codice e dati
- Abilito la risposta come lista oggetti
  . Definizione funzione di scansione in B£DEC4
- Definizione funzioni in JAGES0
- Scheda dell'oggetto

# Oggetti e autorizzazioni

# Oggetti 'TA' :  tabelle
Gli oggetti di tipo TA meritano una trattazione a parte perché presentano alcune caratteristiche che li contraddistinguono in maniera significativa dagli altri oggetti.

# Inclusione OAV negli schemi
Gli OAV rappresentano informazioni associate agli oggetti, quindi risulta naturale poter presentare anche queste informazioni nelle liste che si possono ottenere in Sme.up, cioè includere gli OAV negli schemi informazione (cfr. B£BASE Schemi di visualizzazione stampa).

Per far ciò bisogna inserire degli elementi nella tabella INT (sottosettore specifico) corrispondente allo schema di stampa che si vuole ampliare.

## Convenzioni di codifica e descrizione
Il codice dell'elemento deve avere la convenzione di scrittura seguente : 

- da 001 a 100 per valori alfanumerici
- da 101 a 199 per valori numerici


La descrizione deve avere la struttura seguente : 

_1_&nnn*TT*PPP>CCC

dove : 

 - _1_ & ; fisso per indicare che si tratta di un valore derivato da un OAV
 - _1_nnn; numero dell'elemento della tabella INT che richiama l'oggetto di cui si vuole inserire nello schema l'OAV. (es. nella tabella degli schemi analisi disponibilità INT_AD se voglio aggiungere un OAV dell'ente sarà nnn = 010)
 - _1_*TT; è il tipo oggetto (es. se si parla di ente sarà *TT = *CN)
 - _1_*PPP; può essere : 
 -- _3_blank, quando l'oggetto non pretende il parametro oggetto (es. per gli articoli può essere sufficiente TT = AR se si vuole un OAV comune a tutti gli articoli);
 -- _3_*PPP, dove PPP è il parametro oggetto quando questo è predefinito (es. per una causale di movimentazione sarà *TT = *TA e *PPP = *GMC);
 -- _3_&nnn, dove il parametro oggetto viene preso da un altro campo della tabella INT (es. nella tabella schemi analisi disponibilità INT_AD se voglio aggiungere un OAV di un ente prendendo un OAV dipendente dal tipo ente dovrò scrivere *PPP = &09 per derivare il tipo ente dalla tabella INT_AD)
 - _1_>CCC; può essere : 
 -- _3_blank, nello schema sarà aggiunta la descrizione;
 -- _3_>>, nello schema sarà aggiunta la descrizione;
 -- _3_>CCC, in questo caso CCC è il codice dell'OAV (es. >U/001 aggiunge alo schema un OAV di tipo utente e che ha codice U/001)


Esempio : 
![BLV0002-06](http://localhost:3000/immagini/B£OGAT_STR/BLV0002-06.png)questo elemento della tabella INT_AD aggiunge agli schemi dell'analisi disponibilità l'OAV I/03 (indirizzo) di un ente il cui codice è nell'elemento 010 della tabella ed il cui tipo è nell'elemento 009 della tabella.

# Sviluppi Futuri
- Polimorfismo trasversale :  lo stesso oggetto potrebbe secondo il contesto apparire in forme trasversali diverse; ad esempio un agente potrebbe essere un cliente o un fornitore.
- Aumento delle dimensioni della stringa contenente il parametro
- Negli attributi dell'oggetto base OG aggiungere attributi :  deprecato, deviato con rispettivi oggetto sostitutivo o deviato
