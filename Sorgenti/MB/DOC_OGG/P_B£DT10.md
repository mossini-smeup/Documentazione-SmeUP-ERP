# NOTE GENERALI SULLE TABELLE
Al fine di garantire la massima flessibilità delle applicazioni al mutare delle condizioni in cui l'azienda si trova ad operare, si è cercato di esprimere in forma tabellare alcune variabili che condizionano il sistema informativo. Le tabelle individuate da un nome e da una sigla di identificazione sono contenute in ARCHIVI
TABELLE a loro volta divisi in SETTORI.
Avremo un settore per ogni tabella.
Il riferimento alla tabella avverà sempre tramite il codice del settore.
Ogni settore è costituito da una DEFINIZIONE e da  eventulali
SUB-SETTORI ed ognuno di questi da un numero a  piacere di
ELEMENTI. Questi elementi rappresentano il codice della tabella ed il significato del contenuto dipende dal settore di appartenenza.
Una struttura così concepita si pone in particolare l'obbiettivo di permettere all'utente di aggiungere all'archivio propri SETTORI in modo libero, descrivendone il contenuto e le caratteristiche.
La gestione delle tabelle si appoggia su : 
## ARCHIVI DI DEFINIZIONE SETTORI
Gli archivi di definizione possono stare in una libreria comune a diversi sistemi informativi poichè è normale che lo stesso settore non abbia due definizioni diverse sulla stessa macchina.
Abbiamo in particolare : 
TABDS   = Descrizione settori
TABDC   = Dettagli campi
## ARCHIVI TABELLE
Possono esistere più archivi che contengono le tabelle. Essi devono tutti iniziare con "TABEL" ed essere seguiti da un  carattere che li contraddistingue. Tale carattere sarà nel seguito sufficiente ad individuare completamente l'archivio interessato.
Abbiamo in particolare : 
TABEL P = Tabelle generali di personalizzazione
TABEL I = Tabelle di interrogazione
TABEL 0 = Tabelle base
+-------+             +-------+ ! TABDS !    <---->    :  TABDC  : 
+-------+             +-------+ ! ! !
TABELy  <----* ! *----> TABELx
!            v          !
!          TABEL0       !
!            !          !
Set.01      Set.47     Set.11
Set.AX      Set.CC
Set.88
Un settore può essere definito come esistente in un solo archivio tabelle.
Il programma lo leggerà cioè nel solo archivio specificato a livello definizione settore
# DEFINIZIONE SETTORI E SUBSETTORI - FORMATO GUIDA
## SETTORE
Campo obbligatorio a codifica libera
- se presente sull'archivio si passa alla modifica
- se assente sull'archivio si passa all'inserimento
## SUBSETTORE
Campo non obbligatorio. Se non specificato si assume la modifica del subsettore bianco.
La ricerca viene eseguita nei sub-settori del settore scelto.
## COPIA
Vengono ripresi i dati di intestazione settore e i campi con i loro attributi
# DEFINIZIONE SETTORI E SUBSETTORI - FORMATO GUIDA
## DESCRIZIONE
L'inserimento della descrizione è relativo all'oggetto che si stà definendo, settore o subsettore.
## PROGRAMMA DI RICERCA SPECIFICO
Si indica un programma (scritto dall'utente) qualora si voglia attivare una particolare ricerca sui campi legati alle tabelle.
(Ad esempio la possibilità di presentare solo una sottoparte degli elementi).
NB.  Tale programma viene attivato quando nel campo di ricerca viene immesso il prefisso "+". I caratteri seguenti "+"  potrebbero essere utilizzati come condizionamento imposto dall'utente.
Valore di default
Se non viene indicato alcun programma viene assunto il programma di esempio e di prototipo "B£AR21".
Tale programma  esegue i seguenti passi : 
a)   presenta i tipi oggetto associati alla definizione tabella
b)   per il tipo oggetto scelto presenta i valori possibili
c)   per il valore scelto presenta gli elementi che lo contengono
In tale caso il condizionamento di ricerca ha la struttura : 
C.aaaaaa.b
Dove : 
C.        = Costante di identificazione aaaaaa    = campo assunto per la ricerca dei valori ammessi
.         = Costante di identificazione
b         = bianco  per presentare solo i valori utilizzati = A       per presentare tutti i valori  ammessi
Richiamo diretto
E' possibile richiamare tale ricerca specifica anche da normale programma di ricerca tabelle mediante il comando F04
## CONDIZIONAMENTO RICERCA / AUTORIZZAZIONE ALL'UTILIZZO
Quando nel campo precedente è indicato un programma specifico, questo campo serve per condizionare la modalità operativa con cui si vuole presentare all'utente il formato di ricerca. Le autorizzazioni sono demandate a tale programma. Per il programma di default si veda sopra il significato del condizionamento
Caso particolare
Quando si usa il programma standard di ricerca (campo precedente bianco) questo campo può assumere il significato particolare di indicare le eventuali caratteristiche di autorizzazione all'utilizzo degli elementi della tabella stessa.
Ciò vale se tale campo contiene una struttura del tipo : 
xx-nnn dove : 
xx   =    Funzione della classe di protezione "STATI"
-    =    Valore fisso utilizzato per riconoscere la particolare natura del campo
nnn  =    Posizione iniziale del campo utilizzato come indicazione di stato dell'elemento di tabella.
In tale modo un elemento non autorizzato è a tutti gli effetti come un elemento mancante (fanno eccezione quei programmi dove per valutazioni di prestazioni viene letto direttamente il record dal file (es. stampe ecc.)
Esempio
La tabella GAR contiene un campo controllato dalla tabella B£WRA (Tale campo inizia in posizione 72). Se si vogliono attivare le autorizzazioni si dovrà procedere nel modo seguente : 
a)   Inserire il valore RA-072 sulla definizione della tabella
b)   Definire le autorizzazioni per la classe "STATI" e per la funzione "RA" per tutti gli utenti o per un utente
specifico.
## FUNZIONE PER AUTORIZZAZIONE ALLA GESTIONE
E' il valore assegnato alla "FUNZIONE" per le autorizzazioni alla tabella.
Valgono le seguenti condizioni particolari : 
-    Se il campo non è bianco si assume questo come valore. In tal modo possiamo dare un unico codice "FUNZIONE" ad un insieme di tabelle che vogliamo considerare come gruppo.
-    Se il campo è bianco si assume come "FUNZIONE" il nome del settore.
-    Se indicato il nome settore seguito dai caratteri "**" si intende usare come nome funzione il nome dello specifico sottosettore in manutenzione.
-    Se indicato il nome settore seguito dal carattere "-" significa che le autorizzazioni sono definite a livello di elemento. Il codice elemento sarà concatenato al nome del settore e avremo :  xxx-yyyyyy. Dove xxx è il settore e yyyyyy è l'elemento.
NB.  L'autorizzazione si applica fino ad un massimo di 6 caratteri.
Le autorizzazioni possono essere definite anche a livello di sottosettore. Posso ad esempio vincolare uno ed un solo sottosettore. Se il sottosettore è protetto assume tale protezione, diversamente usa quelle standard del settore.
NB.  Sulle autorizzazioni valgono le normali regole di risalita.
## CARTELLA PER HELP
Definisce un nome di sottocartella interna alla cartella SMEHLP dove la tabella viene descritta.
## APPLICAZIONE SPECIFICA
Permette di indicare la sigla specifica dell'applicazione cui laa tabella appartiene. Normalmente le tabelle di una applicazione "&&" sono tutte caratterizzate dall'avere come prefisso "&&" stesso ma questo campo permette di generalizzare l'appartenenza.
## ARCHIVIO DI APPARTENENZA
Un carattere che identifica l'archivio tabelle cui appartiene il settore inteso come insieme dei suoi elementi.
Si veda quanto detto nell'introduzione circa la separazione delle tabelle in più archivi fisici.
## PROGRAMMA DI CONTROLLO
Previsto per tabelle particolarmente complesse che meritino una gestione con un programma specifico. Tale programma dovrà esistere al momento della codifica del settore.
## TABELLA DI PERSONALIZZAZIONE
Indica che tale tabella è costituita da un solo elemento
"*              ".
Il programma di gestione, se richiesto un settore con tale caratteristica, evita la richiesta del codice elemento e passa direttamente alla gestione.
NB.  Il carattere "L" inserito in questo campo definisce la tabella come di sola definizione. Ciò significa che non verrà costruito il formato video. Tale tipo di tabella potrà essere utilizzata da parte dell'utente per definire un tracciato record a piacere e da questo creare la DS di definizione.
## GESTIONE SETTORE E GESTIONE ELEMENTO
I campi presenti servono a lasciare traccia di una azione di immissione o variazione sul settore o sugli elementi.
Sono presenti tali campi in funzione dell'importanza che il contenuto delle tabelle rivestono per l'applicazione al fine di conoscerne eventuali manomissioni. I campi sono di sola emissione.
Nota tecnica
I dati di gestione settore/elemento sono aggiornati dai programmi B£DT10, B£DT20 (manut. settore)/ B£AM30 (manut. elementi).
## DESCRIZIONE SETTORI DI TABELLA
In basso a sinistra sullo schermo,  riga 24, è presente un campo di immissione di due caratteri alfabetici relativo alla descrizione dei settori di tabella. Digitando i caratteri GC (Gesione commenti) si accede al programma per la gestione delle Note libere in modalità Inserimento, digitando IC (Interrogazione Commenti) l'accesso al programma avviene in modalità Esame.
NB.  Per ulteriori chiarimenti sulla funzione di accesso alle note si veda la documentazione relativa alla funzione NOTE STRUTTURATE.
# PROGRAMMI DI UTILITY
## PROGRAMMA DI CONTROLLO FORMALE GESTIONE
Il programma deve eseguire controlli/completamenti su un elemento della tabella che si sta manutenendo. Deve essere denominato B£TXXX (dove XXX è il settore di tabella). Il suo funzionamento è spiegato nel dettaglio all'interno del prototipo presente nel file SMESRC.
 :  : INI **Visualizzazione sorgente prototipo B£TXXX**
 :  : CMD CALL B£VED0 PARM('B£TXXX' '' '' '' '0')
 :  : FIN
## PROGRAMMA GESTIONE AREA UTENTE TTUSER
Il programma permette di definire l'utilizzo del "campo libero utente" (=TTUSER) per gestire le aggiunte di informazioni personali sulle tabelle standard.
Deve essere denominato B£TXXX_U (dove XXX è il settore di tabella).
Il suo funzionamento è spiegato nel dettaglio all'interno del prototipo presente nel file SMESRC.
 :  : INI **Visualizzazione sorgente prototipo B£TXXX_U**
 :  : CMD CALL B£VED0 PARM('B£TXXX_U' '' '' '' '0')
 :  : FIN

