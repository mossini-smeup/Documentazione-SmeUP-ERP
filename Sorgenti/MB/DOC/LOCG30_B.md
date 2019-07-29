# Scopo di questo documento
Illustrare come creare questionari.
Verranno forniti i concetti di base,  poi analizzati i vari tipi di questionari ed inifine l'utilizzo delle configurazioni.

# Nomenclatura
 * _2_Configuratore :  insieme di domande, suddivise in una o più sezioni
 * _2_Configurazione :  insieme di risposte ottenute dalla compilazione di un configuratore
 * _2_Sezioni :  suddivisione logica di un questionario in più parti. Ogni sezione contiene una o più domande.
 * _2_Script di configurazione :  membri del file SCP_CFG che contengono la struttura del questionario
 * _2_Domanda configurata (a risposta) singola :  tipo di domanda in cui su un'unica riga posso immettere più valori
 * _2_Domanda configurata (a risposta) multipla :  tipo di domanda in cui l'utente può immettere una matrice di valori.

# Aspetti Grafici

a) E' stata migliorata la gestione delle icone, che vengono cambiate in base alle caratteristiche del campo quindi : 

![03COMG3001](http://localhost:3000/immagini/LOCG30_B/03COMG3001.png)
b) La finestra viene dimensionata in base al contenuto
c) Le finestre non vengono sovrapposte una all'altra ma vengono posizionate in modo che si vedano tutte (leggermente scalate)


# Estensioni del richiamo come funzione
Esempio
La funzione F(G30;JA_00_01;GES.EDT) 1(J5;;) con i parametri P(SCP(EDT_BRE) FORJ5(P)) visualizza il contenuto dello script EDT_BRE in SCP_CFG sotto forma di G30 in questo modo
![03COMG3004](http://localhost:3000/immagini/LOCG30_B/03COMG3004.png)![LOCG30_006](http://localhost:3000/immagini/LOCG30_B/LOCG30_006.png)
Restituisce le scelte effettuate sotto forma di J5 con il formato indicato nel parametro FORJ5(P).
Questo parametro e' di tipo V2 FORJ5 e puo' assumere i seguenti valori : 

- A Doppio apice
- P Parentesi
- F Fisso/Posizionale

Nel caso specificato sopra il ritorno delle risposte e' : 
![LOCG30_007](http://localhost:3000/immagini/LOCG30_B/LOCG30_007.png)
- GRA :  configuratore di componenti grafici
- ESE :  esempi
- LST :  configuratori di listener (ascoltatori di eventi)
- SER :  configuratori di servizi

Verra' quindi visualizzato un questionario con le domande scritte all'interno dello script per
la configurazione richiesta.
Ad esempio : 
![LOCG30_008](http://localhost:3000/immagini/LOCG30_B/LOCG30_008.png)Premendo F4, compare il questionario per la configurazione del componente EXD 'Scheda'
![LOCG30_009](http://localhost:3000/immagini/LOCG30_B/LOCG30_009.png)
# Albero editor di scheda
Il vecchio albero che si apriva dall'editor di scheda
![03COMG3007](http://localhost:3000/immagini/LOCG30_B/03COMG3007.png)e' stato sostituito dal nuovo
![LOCG30_010](http://localhost:3000/immagini/LOCG30_B/LOCG30_010.png)
# Tipi di questionari
I questionari sono oggetti di tipo RE.
Comme illustrato nel documento introduttivo, si dividono in base all'orgine della struttura del questionario e a seconda della destinazione delle risposte fornite.

Analizziamo le varie tipologie.

## Questionari T-
 * **Utilizzo** :   manutenzione tabelle SmeUp.
 * **Costruzione** :  dedotte dalla struttura del tipo di tabella.
 * **Struttura** :  un'unica sezione
 * **Formato risposte** :  posizionale, scritte nel file delle tabelle di SmeUp (normalmente il Tabel00f)
 * **File Configurazioni** :  TABEL00F
 * **Forma presentazione** :  unica sezione.
 * **Navigazione** : 
 * **Regole** :  definite da programma (per gestire i range dei valori)

## Questionari Q-
 * **Utilizzo** :   creazione configuratorei generici, dal configuratore di prodotto ad un questionario per raccogliere le preferenze degli utenti.
 * **Costruzione** :  utilizzando le tabelle SmeUp CFQ, CFS, CFD, CFV, CFC oppure appositi script.
 * **Struttura** :  composta da sezioni, con possibilità di includere questionari o di ripetere sezioni o gruppi di sezioni.
 * **Formato risposte** :  vari formati di XML.
 * **File Configurazioni** :  CFVARI0F, B£MEDE0F
 * **Forma presentazione** :  albero di navigazione con sezione corrente.
 * **Navigazione** :  Dalla prima sezione all'ultima.
 * **Regole** :  definite liberamente dal creatore del questionario, oppure tramite programmi appositi.

## Questionari L-
Questionari definiti all'interno del file SCP_CFG
 * **Utilizzo** :   creazione configuratori  di servizio (configuratore di configuratori, wizard vari)
 * **Costruzione** :  tramite Wizard in Loocup
 * **Formato risposte** :  vari formati di XML.
 * **File Configurazioni** :   B£MEDE0F
 * **Forma presentazione** :  pannello con n pannelli, ognuno con una sezione
 * **Navigazione** :  Libera
 * **Regole** :  non definite

## Questionari U-
Questionari ottenuti dall'unione di una o più sezioni di script oppure da impostazioni grafiche.
 * **Utilizzo** :   raggruppare configurazioni eterogenee
 * **Costruzione** :  da codice :  viene indicato lo script e quali sezioni utilizzare, oppure viene solo indicato il codice del questionario e quali sono le risposte da salvare.
 * **Formato risposte** :  vari formati di XML.
 * **File Configurazioni** :   B£MEDE0F
 * **Forma presentazione** :  pannello contenente da 1 a n pannelli, ognuno con una sezione
 * **Navigazione** :  Libera
 * **Regole** :  non definite

## Questionari S-
Questionari definiti all'interno del file SCP_CFG
 * **Utilizzo** :   creazione configuratori  di setup di moduli SmeUp
 * **Costruzione** :  tramite Wizard in Loocup
 * **Formato risposte** :  vari formati di XML.
 * **File Configurazioni** :   B£MEDE0F
 * **Forma presentazione** :  pannello con n pannelli, ognuno con una sezione
 * **Navigazione** :  Libera
 * **Regole** :  non definite

# Costruzione di un questionario
La costruzione di un questionario si differenzia in base al tipo.

## Costruzione di un questionario di tipo Q-

Per la costruzione della struttura di un questionario di tipo Q- si rimanda alla documentazione del modulo CF, in particolare alla documentazione delle tabelle
 * _2_CFQ :  questionari
 * _2_CFS :  sezionidi questionario
 * _2_CFD : domande di sezione
 * _2_CFV :  valori di domanda
 * _2_CFC :  configurazioni.

Per la costruzione delle regole del questionario utilizzare la scheda CFBASE, sottoscheda Regole.

Per il reference delle regole fare riferimento al manuale tecnico dell'applicazione CF :  My Loocup, Appllicazioni

## Questionari L-, U- da script e S-
I questionari in oggetto sono definiti  come membri del file SCP_CFG.
Un unico script può contenere un solo questionario oppure da 1 a n questionari.
Ad esempio il membro GRA_EMU contiene un unico questionario, mentre EDT_SCH ne contiene varie decine.
Gli script multi questionario hanno una parte di indice che raggruppa i questionari in base all'utilizzo :  ad esempio tutti i tag G.SET.XXX si troveranno sotto il gruppo G.SET, a sua volta membro del gruppo G.
Per accedere ad un determinato questionario si può utilizzare la sintassi CF S->NOME_SCRIPT/>SEZIONE, dove >NOME_SCRIPT/>SEZIONE deve avere una lunghezza minore uguale ai 10 caratteri.

### Struttura script
Gli script che definiscono i questionari hanno una sintassi leggermente diversa da quella degli script delle schede in quanto alcuni tag si sviluppano su più righe, inoltre il significato di una riga potrebbe dipendere da quelle precedenti.
Questa condizione si verifica solo quando voglia definire domande configurate, a risposta singola oppure multipla.

Gli script sono composti dalle seguenti parti : 
 * _2_Sezione Header
 ** _3_KEY :  contiene le chiavi di salvataggio, da utilizzare quando si salva una configurazione
 ** _3_POP :  le voci di popup da aggiungere al G30
 ** _3_BOT :  quali pulsanti tra salva/salva con nome/ elimina sono attivi
 * _2_SEZ :  da questo tag, fino al tag RIG sono indicati i questionari da cui è composto lo script. Per ogni riga viene indicato il formato delle risposte.
 * _2_RIG :  da questo taga fino al tag LIS sono indicate le sezioni e le domande che compongono i vari questionari.
 * _2_LIS :  contiene i possibili valori che una risposta può assumere.

Analizziamo i vari tag.
**Tag RIG**
Il tag specifica l'inizio della definizione di sezioni e domande.

Una sezione è identificabile dal fatto che il primo carattere non è un ".".
Avremo pertanto che tutto quanto si trova tra due righe che non iniziano con il carattere "." costituisce il corpo di una sezione.

Nota molto importante va posta a quelle riche che iniziano con il carattere " : " :  queste righe identificano una subsezione.

Avremo pertanto che se una sezione contiene delle subsezioni, questa presenterà le sue domande divise in n gruppi distinti.
Si presenterà pertanto come un questionario composto da n sezioni.

**Sintassi righe di sezione**
Le righe di sezione NON iniziano con il "."
Le righe di sezione possono avere codice e descrizione :  il primo spazio suddivide questi due elementi.

**Sintassi righe di subsezione**
Le righe di subsezione iniziano con il carattere " : "
Le righe di subsezione possono avere codice e descrizione :  il primo spazio suddivide questi due elementi.

**Sintassi righe di domanda**
Le righe di domanda iniziano con il carattere ".". La sintassi è guidata da apposito wizard.
Se ad una riga di domanda seguono due o più righe che iniziano per ".." questo significa che è una domanda configurata a risposta singola.
Se ad una riga di domanda che inizia con ".." seguono due o più righe che iniziano con "..." significa che è una domanda configurata a risposta multipla.

**Tag KEY**
Il tag KEY è opzionale :  il servizio che costruisce l'XML del questionario potrebbe costruirne uno diverso da quello definito nello script.
Posso avere da 0 a 3 tag Key.

**Tag POP**

**Tag LIS**
Se ad esempio una domanda chiederà la posizione, e i valori possibili sono alto basso oppure centro, andrò ad assegnare alla domanda come tipo risposta **.VPos.Vert** e poi andrò a creare le seguenti righe nella sezione LIS : 
Pos.Vert
.A            Alto
.C            Centro
.B            Basso
Il codice occupa 16 caratteri, compreso il punto iniziale. La descrizione si troverà  dal 17esimo carattere.
Anche per la definizione delle liste di valori c'è un apposito wizard.

## ESEMPI
**Questionario Mono Sezione - ESE_001**
 :  : RIG
S1 prima sezione
.A Articolo                             AR                      015
.B Cliente                              CNCLI                   015
.C Libera                               **                      100
.D Con valori                           .VPos.Vert              001
 :  : LIS
Pos.Vert
.A              Alto
.C              Centro
.B              Basso
 :  : DEC D(Apri G30 Mono Sezione) X(F(G30;CFSER_02;STR.LET) 1(RE;L-;ESE_01))
 -- F(G30;CFSER_02;STR.LET) 1(RE;L-;ESE_01) --

**Questionario Multi sezione**
 :  : RIG
S1 prima sezione
.A Tipo                                 OG                      002
.B Parametro                            OG[A]                   010
.C codice                               [A][B]                  015
S2 seconda sezione
.E Articolo                             AR                      015
.F Cliente                              CNCLI                   015
.G Libera                               **                      100
.H Con valori                           .VPos.Vert              001
 :  : LIS
Pos.Vert
.A              Alto
.C              Centro
.B              Basso

 :  : DEC D(Apri G30 multi sezione) X(F(G30;CFSER_02;STR.LET) 1(RE;L-;ESE_02))

**Questionario Multi Questionario**
 :  : SEZ
S
.A             Quest. 1                      "
.B             Quest. 2                      (
 :  : RIG
A
 : S1A prima subsezione
.A Articolo                             AR                      015
.B Cliente                              CNCLI                   015
 : S1B seconda subsezione
.C Libera                               **                      100
.D Con valori                           .VPos.Vert              001
B seconda sezione
.E Centro di lavoro                     RICDL                   015
.F Data                                 D8*YYMD                 015
.G Libera                               **                      100
.H Con valori                           .VPos.Vert              001
 :  : LIS
Pos.Vert
.A              Alto
.C              Centro
.B              Basso

 :  : DEC D(Apri G30 sezione A) X(A(CFCF01X;GES;01) 1(CF;S-ESE_03/A;))
 :  : DEC D(Apri G30 sezione B) X(A(CFCF01X;GES;01) 1(CF;S-ESE_03/B;))

Utilizzo S-
modifica di una configurazione
A(CFCF01X;GES;02) 1(CF;S-B£EQRY/A;0000202291)

Utilizzo come SP

Utilizzo nei wizard

Utilizzo nei setup di componente (Emulatore, Scheda e componenti interni alla scheda)

Utilizzo configurazione Listener.
