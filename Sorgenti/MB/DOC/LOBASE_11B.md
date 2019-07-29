# EVA - VARIABILI (Lato SERVER)

## Obiettivo
Questo documento vuole definire un quadro chiaro sugli oggetti variabili lato Server di SmeUp/LoocUp e sulla loro gestione. Vuole rispondere alle seguenti domande :  come si crea, come si utilizza, come può essere visionata e quali operazioni si possono fare su una variabile.
Oltre che illustrare i vantaggi del loro utilizzo.

## Definizioni e Generalità
Occorre innanzi tutto precisare che le variabili Server sono oggetti di tipo V3EVA. Come tutte le istanze possono essere quindi visionate con i comandi UP FUN e UP OAV per conoscerne attributi, funzioni.

![LOBASE_11B](http://localhost:3000/immagini/MBDOC_OGG-V3_EVA/LOBASE_11B.png)
Esiste una categorizzazione delle variabili in base a chi le crea, alla visibilità o allo scopo e tale categorizzazione si traduce nel codice che identifica la variabile tramite un prefisso.

|  Nam="Categorie previste e rispettivi prefissi" R="0000000050" |
| 
| .COL Txt="Categoria" LunAut="1" A="L" |
| ---|----|
| 
| .COL Txt="Prefisso"  LunAut="1" A="L" |
|  Sistema B§V|_&_ |
|  Ambiente|_&_AM. |
|  Contesto|_&_CO. |
|  Istanza|_&_KI. |
|  Configurazione Upp|_&_KU. |
|  Data|_&_D8. |
|  Variabili lunghe|_&_G00. |
|  Oggetto|_&_OG. |
|  Parametri|_&_PA. |
|  Workflow|_&_AWF. |
|  Sistema |_&_SY. |
|  Collegamento |_&_CL. |
|  Collegamento ambiente test|_&_CLT. |
| 


E' possibile inoltre fare le seguenti affermazioni : 

- Fatta eccezione per le variabili di categoria Data e Variabili Lunghe, ogni variabile risiede in uno specifico contesto.
- Ad ogni variabile può essere assegnato un valore e il relativo oggetto di appartenenza.
- Una variabile può essere un alias di un'altra variabile o risolta attraverso il richiamo di un servizio.
- Ogni variabile inizia con _&_
- La variabile si intende chiusa quando incontra uno dei seguenti caratteri : 
--   Spazio
-- ; Punto e virgola
-- ( Parentesi aperta
-- ) Parentesi chiusa
-- " Doppio apice
-- ' Apice
-- \ Barra rovesciata
-- = Uguale
-- < Minore
-- > Maggiore
-- _ Sottolineatura
-- | Pipe

Consideriamo la prima delle affermazioni fatte qua sopra : 
Per ciascuna di queste categorizzazioni esiste un contesto associato...

### Contesti
Il contesto è un'aggregazione logica di variabili, che permettono la condivisione delle stesse.
 T(Un contesto possiede : )
- Nome
- Descrizione
- Attributi

 T(I contesti si distinguono in tre tipi distinti)
- Default
- Oggetto
- Libero

Il contesto**Default**possiede e condivide con tutti gli altri contesti le variabili di ambientee di sistema che possono avere solo questo contesto; è riservato e non possiede attributi.
Il contesto**Oggetto**gestisce l'univocità fra oggetto e contesto impedendo una replicazione di variabili per lo stesso oggetto, è un contesto che possiede solo l'attributo OG.
Il contesto**Libero**gestisce tutte le altre casistiche, possiede attributi liberi definiti dall'utente.

In fase di sostituzione del valore delle variabili la ricerca viene fatta nel contesto specificato quindi nel contesto di default.

I lavori all'interno del nostro JOB possono accedere ai vari contesti risalendo per scansione di attributi, se trovati più contesti la ricerca fallisce.
## Categorie
### _&_ Sistema B§V
Queste variabili sono definite tramite la tabella B§V e non posseggono un oggetto di riferimento.

### _&_AM. Ambiente
 T(Sono assunte direttamente dal programma e assumono i seguenti nomi)
- UT Utente (UP)
- AZ Azienda (CNAZI)
- DT Data sistema (D8*YYMD)
- DF Data sistema formattata (D8*DMYY)
- HR Ora sistema (I2D)


### _&_CO. Contesto
Sono definite dal contesto in cui si usano. Possono possedere un oggetto e avere un contenuto di 256 caratteri e un nome di 26 caratteri.

### _&_KI. Istanza
Sono variabili definite su un'istanza di un oggetto, non necessitano di essere dichiarate in quanto sono autoreferenziate.


|  Nam="Definizioni" R="00000000100" |
| 
| .COL Txt="Identificativo" A="L" |
| ---|----|
| 
| .COL Txt="Separatore" A="L" |
| 
| .COL Txt="Oggetto" A="L" |
| 
| .COL Txt="Separatore" A="L" |
| 
| .COL Txt="Istanza" A="L" |
| 
| .COL Txt="Separatore" A="L" |
| 
| .COL Txt="Attributo" LunAut="1" A="L" |
| 
| .COL Txt="Separatore" A="L" |
| 
| .COL Txt="Attributo" LunAut="1" A="L" |
|  _&_KI|.|TABRA|.|ART|%|I/01|%|I/02 |
|  Obbligatorio|Obbligatorio|Obbligatorio|Obbligatorio|Obbligatorio|Facoltativo|Facoltativo|Facoltativo|Facoltativo |
| 


### _&_KU. Configurazione Upp
Sono variabili definite sulla configurazione di una Upp, non necessitano di essere dichiarate in quanto sono autoreferenziate. Per la definizione della configurazione di un Upp si rimanda alla scheda dell'Upp (Oggetto SU).


|  Nam="Definizioni" R="00000000100" |
| 
| .COL Txt="Codice Upp" A="L" |
| ---|----|
| 
| .COL Txt="Separatore" A="L" |
| 
| .COL Txt="Codice Campo Configuratore" A="L" |
|  _&_KU|.|A£_000|%|D01 |
|  Obbligatorio|Obbligatorio|Obbligatorio |
|  |
| 


### _&_AWF. Workflow
 T(Sono istanziate dal contesto di Workflow e assumono i seguenti nomi)
- NWF Numero ordine
- TMS Tipo Oggetto master ordine
- PMS Parametro Oggetto master ordine
- OMS Oggetto master ordine
- OOW Oggetto owner ordine
- PRO Processo
- SCP Script utilizzato
- IMP Impegno (+ codice per definire la transazione)


### _&_SY.Sistema
Sono variabili utilizzate per ritornare valori del sistema operativo

|  Nam="Definizioni" R="00000000100" |
| 
| .COL Txt="Identificativo" A="L" |
| ---|----|
| 
| .COL Txt="Separatore" A="L" |
| 
| .COL Txt="Oggetto" A="L" |
| 
| .COL Txt="Separatore" A="L" |
| 
| .COL Txt="Oggetto" A="L" |
| 
| .COL Txt="Separatore" A="L" |
| 
| .COL Txt="Attributo" LunAut="1" A="L" |
| 
| .COL Txt="Separatore" A="L" |
| 
| .COL Txt="Attributo" LunAut="1" A="L" |
| 
| .COL Txt="Nota" A="L" |
|  _&_SY.LIB|;|<File>|;|<Membro>|%|I/01|%|I/02|Ritorna la libreria dell'oggetto specificato |
|  Obbligatorio|Obbligatorio|Obbligatorio|Facoltativo|Facoltativo|Facoltativo|Facoltativo|Facoltativo|Facoltativo |
| 


### _&_CL.Collegamento
Sono le variabili definite nello script di collegamento (SCP_CLO)

### _&_CLT.Collegamento ambiente di test
Sono le variabili definite nello script di collegamento (SCP_CLO).
Se in un ambiente normale coincidono con quelle di collegamento.
Se in un ambiente di test vengono restituite solo le variabili presenti negli script che terminano
con i caratterei '_T'

### _&_D8. Data variabile
Sono date calcolate dinamicamente al momento dell'utilizzo.
 T(Tipi di data)
- U Def.utente (Pgm B£DAT8S_U)
- O Da oggi +/- giorni/sett./mesi
- C Da periodo contabile
- Z Da segno zodiacale
- T Da tabella date particolari (B£4)
- S Settimana (Giorno/Anno scost.)

E' possibile definire il formato di output attraverso i seguenti valori

|  Nam="Formato emissione data" R="0000000070" |
| 
| .COL Txt="Codice" A="L" |
| ---|----|
| 
| .COL Txt="Formato"    LunAut="1"  A="L" |
| 
| .COL Txt="Esempio"  LunAut="1"  A="L" |
|  .Y|YYYY/MM/DD|2009/05/18 |
|  .y|YYYYMMDD|20090518 |
|  .D|DD/MM/YYYY|18/05/2009 |
|  .d|DDMMYYYY|18052009 |
| 

se non impostato viene assunto il valore **.D**.

### _&_G00. Variabile Lunga
Le variabili lunghe permettono di gestire fino a 30000 caratteri, il limite di tutte le altre variabili è di 256 caratteri. Essendo più lunga del campo previsto per le altre variabili (£G91TV) è possibile impostarla tramite la funzione.metodo VAR.G00 inserendo il valore nel campo £G91SI, ma non è possibile utilizzarla negli altri metodi della funzione VAR, pertanto è possibile utilizzarla solo come traduzioni di stringa con output nel campo £G91SO, ma per esempio non è disponibile la lettura del suo contenuto tramite la funzione.metodo VAR.LET.
Le variabili lunghe sono utilizzabili anche nelle funzioni CND, con il limite di 256 caratteri, il resto del contenuto della variabile lunga viene ignorato.
Avendo la funzione.metodo specifica VAR.G00 non è necessario definirla come _&_G00.nomevariabile, pertanto la variabile pippo, non cominciando per _&_G00, viene comunque automaticamente tradotta in _&_G00.pippo.
Non sono variabili di contesto, pertanto se si necessita di eventuali aggregazioni logiche si consiglia attribuire l'aggregazione ai nomi delle variabili, per esempio _&_G00.contesto.variabile1, _&_G00.contesto.variabile2 ecc..
La gestione di queste variabili avviene tramite la G00, pertanto i relativi dati sono memorizzati temporaneamente nel B£MEDE0F, cancellati poi alla chiusura del lavoro.

### _&_OG. Oggetto
 T(Sono istanziate solo su richiesta e possono assumere i seguenti nomi)
- FU Funzione
- ME Metodo
- CO Componente (J1GRA)
- PA Stringa del parametro
- Tx Tipo oggetto x (OG)
- Px Parametro oggetto x (_&_OG.Tx)
- Ex Tipo/Parametro oggetto x (OG)
- Kx Codice Oggetto x (_&_OG.Tx_&_OG.Px)
- Dx Sigificato Oggetto x

Assumiamo che il programma conosca tutte le variabili di una funzione nella forma F(programma;funzione;metodo) ecc.
Sono memorizzati fino a 6 oggetti quindi x assume i valori da 1 a 6.

### _&_PA. Parametri
Una funzione può contenere una stringa che chiamiamo "parametro". All'interno del parametro possono essere definite delle variabili nella forma "Variabile(Valore)". Nello SCRIPT potremo riferirci alla singola variabile chiamandola _&_PA.Variabile

# Gestione delle variabili
## Attributi, variabile e espressione
Data una variabile, a cui è assegnato un oggetto, è possibile attraverso il carattere % accedere agli attributi dell'oggetto.
Poichè l'attributo è a sua volta un oggetto, è ammessa la ricorsione continuando la successione di definizioni tramite il carattere %.

### Struttura di un'espressione
V%RA%RA%RA...%RA


|  Nam="Definizioni" R="00000000100" |
| 
| .COL Txt="Nome della Variabile" A="L" |
| ---|----|
| 
| .COL Txt="Separatore" A="L" |
| 
| .COL Txt="Tipo di risposta" A="L" |
| 
| .COL Txt="Attributo" LunAut="1" A="L" |
|  V|%|R|A |
|  Obbligatorio|Obbligatorio|Facoltativo|Obbligatorio se Tipo risorsa diverso da OV. |
| 

La definizione dell'attributo può continuare fino ad arrivare alla definizione richiesta.

 T(Tipi di risposta)
- OI. Intestazione
- OA. Valore è il default e può essere omesso
- EA. Elenco di tutti i valori
- OD. Significato
- ED. Elenco di tutti i significati
- OT. Tipo oggetto
- OP. Parametro oggetto
- OO. Tipo e parametro oggetto
- OV. Oggetto della variabile

All'elenco può essere attribuito un formato di ritorno, se non impostato assume una lista numerata.
 T(Formato elenco)
- 1  Separato da ;
-    Numerato x)


## Assegnazione variabile
Utilizzando operatore "Doppiouguale" è possibile assegnare un valore ad una variabile; naturalmente il formato della variabile deve rispettare quanto definito in precedenza

### Struttura libera
N d= O;V : S|A

 * _2_Nome della variabile N Obbligatorio
 * _2_Operatore Doppio uguale d= Facoltativo
 * _2_Oggetto in forma Tipo e parametro O Obbligatorio se definito Oggetto
 * _2_Separatore ; Obbligatorio
 * _2_Valore V Obbligatorio
 * _2_Separatore  :  Facoltativo
 * _2_Significato S Facoltativo
 * _2_Separatore (Pipe) "|" Facoltativo
 * _2_Alias A Facoltativo

### Struttura tramite tag "VAR"
 T(Attributi)
- Tip Oggetto
- Des Significato
- Ali Alias
- Name Nome
- Val Valore
- Pgm Funzione con cui risolviamo il valore

Se si utilizza un alias, da questo oltre al suo valore viene derivato anche l'oggetto a cui si riferisce e il suo significato.
Se si utilizza una funzione, questa restituisce solo il valore e non l'oggetto a cui si riferisce.

# Esempi

Assumiano di avere nell'oggetto 1 il cliente e di voler recuperare l'aggregazione di appartenenza della propria nazione; possiamo utilizzare i seguenti metodi.
 T(Metodi)
- & OG.K1%I/15%I/T$V§NB "Attraverso gli attributi della variabile"
- & CO.AG "Definendo come alias la variabile & OG.K1%I/15%I/T$V§NB"
- & CO.AG%I/T$ELEM "Utilizzo l'alias per accedere all'attributo dell'aggregazione"


- [Variabili (Lato SERVER](Sorgenti/MB/DOC_OGG/V3_EVA_ES)


# Test/Simulazione

Nella scheda V3EVA è possibile eseguire delle simulazioni e dei test sull'assegnazione e la valutazione di variabili
 :  : DEC T(MB) P(SCP_SCH) K(V3EVA)


 :  : TAG Id="ANA" Txt="Analisi dei contesti"
### Analisi dei contesti
In questa sottoscheda sono elencati tutti i contesti creati e le rispettive variabili

 :  : TAG Id="ASS" Txt="Assegnazione di una variabile a un contesto"
### Assegnazione di una variabile a un contesto
La sottoscheda permette di creare un contesto assegnando un gruppo di variabili, estratte da una qualunque FUN
**Contesto** - Inserire un contesto nuovo o esistente
**Funzione** - Inserire una funzione :  gli oggetti della funzione e tutti i paramentri e l'input verranno inseriti nel contesto


 :  : TAG Id="CRE" Txt="Creazione di una variabile"
### Creazione di una variabile
La sottoscheda permette di creare una variablile in un contesto, assegnando nome e valore
**Contesto** - Inserire un contesto esistente
**Variabile** - Inserire il nome della variabile
**Valore** - Inserire il valore da assegnare alla variabile


 :  : TAG Id="RISVAR" Txt="Risoluzione di una variabile"
### Risoluzione di una variabile
Dato un contesto, viene estratta un/a variabile del contesto
**Contesto** - Inserire un contesto esistente
**Variabile** - Inserire una variabile nella notazione & NOMEVARIABILE

 :  : TAG Id="VALEXP" Txt="Valutazione espressione"
### Valutazione di espressioni
Dato un contesto, viene valutata un'espressione (anche detta "stringa")
**Contesto** - Inserire un contesto esistente
**Espressione** - Inserire una variabile nella notazione & NOMEVARIABILE%ATTRIBUTO%ATTRIBUTO%ATTRIBUTO






