# Descrizione gestione KIT


## Introduzione
Questo modulo permette di gestire le problematiche del KIT, in particolare nella fase  del ciclo attivo e del magazzino.
Sarà possibile gestire dei codici KIT sui documenti, e fare in modo che sia i prezzi che la disponibilità possano essere attribuiti al padre o a i figli in base a come è configurato il tipo riga utilizzato.

Non si tratta di KIT commerciale quando il KIT ha un proprio codice, assemblato in fase produttiva, e il cliente vede solo il codice KIT, sia come prezzo che come quantità.
In questo caso conviene gestire una riga di vendita normale, e gestire l'assemblaggio con un ordine di produzione.

La struttura di un kit a livello anagrafico, può essere descritta in una distinta base.
Può essere usata una distinta specifica oppure la distinta articolo (ART).  Un kit non può per definizione contenere 2 legami con lo stesso articolo.

In fase di inserimento di una riga di documento, se utilizzata un tipo riga _kit_,  vengono generate delle righe dei componenti che possono partire sia dalla distinta base del kit che dalla distinta base di memorizzazione (legata alla riga del documento), qualora questa sia stata creata con l'apposita funzione.

Nel documento, in presenza di un kit, saranno presenti le righe in questo modo : 
 :  : PAR F(01)
0010 - riga Kit padre                   FL10 = 3
0020 - riga Kit figlia  1 collegata   FL10 = 4  NRRI=0010
0030 - riga Kit figlia  2 collegata   FL10 = 4  NRRI=0010
0040 - riga Kit figlia  3 collegata   FL10 = 4  NRRI=0010


In base al flag 11 e flag 29 della riga (come vedremo più avanti), si potranno configurare varie modalità di Kit, sia per il calcolo del prezzo che per il calcolo della disponibilità.

Il modulo gestisce il KIT sul documento. Per la gestione logistica si riallaccia alla gestione classica, con la possibilità di gestire anche le richieste di movimentazione in base al flag di disponibilità della riga.


## Disegno impianto tabellare

**Struttura logica delle righe kit dal punto di vista tabellare : **

>
    V5B (tipo Riga)
      |
      +---------> Par di Cto Lavoro (V5L)
                      |
                      +----------> Tipo impegno (P5I)
                      |             - Tipo distinta origine (BRL)
                      |             - Tipo Distinta memorizzazione (BRL)
                      |
                      +----------> Tipo Kit (V5K)
                      |             - Tipo aggr. capo
                      |             - Calc. prezzo padre
                      |             - Tipo aggr. riga
                      |             - Calc. prezzo figlio
                      |             - SS tipo riga figlio
                      |             - Tipo riga figlio (V5B)
                      |             - Suff. pgm controllo
                      |             - Tp Riga RIM x rilev. disponib.
                      |             - Tp Riga RIM x NO rilev dispon.



La V5L va compilata sulla riga padre kit. A queste si fa riferimento per la creazione delle RIIM ecc.

Molti dei comportamenti e delle funzioni dei kit, sono governati dai flussi delle righe doc., opportunamente configurati; in questo modo c'è la possibilità che il kit venga gestito "automaticamente", creato, modificato, cancellato, valorizzato.
A livello di programma di data entry vengono controllate delle regole di coerenza relative alle righe che hanno a che fare con i Kit (quelle con Flag 10 di riga impostato a 3 o a 4) : 
1)  che un kit non contenga due componenti uguali;
2)  che la riga di riferimento KIT sia compilata (o non sia compilata) quando serve.

Si rimanda al capitolo successivo di documentazione per come configurare al meglio le tabelle per gestire i KIT.


## Casistiche gestite

Proviamo ad elencare alcune delle casistiche di Kit gestibili, e la loro configurazione. Descriviamo le casistiche sulle quantità e sui prezzi. In realtà si possono creare poi tutti gli incroci possibili.
In base poi a come vengono prodotti i documenti verso i clienti, si possono differenziare gestioni KIT solo interne (di prezzo e/o di quantità), solo esterne o entrambe.
Ad esempio il cliente vede solo il codice KIT e il suo prezzo, ma internamente gestisco a magazzino i suoi componenti, e anche il prezzo è derivato dalla somma dei suoi componenti.
Tutte le casistiche non toccano i flag di fatturazione, che per casi particolari potrebbero essere usati come ulteriore variabile.
I conti contabili nativamente vengono presi dalle righe che sono valorizzate.

Per maggior chiarezza ci appoggiamo ad un esempio in cui il Kit è così composto : 

Codice KIT = Art. KIT, composto da : 
* Art. A X 1
* Art. B X 2
ordine di 100 KIT.


### Quantità Caso 1
Il codice Kit è fittizio come disponibilità e magazzino, gestita sui componenti.
- Riga padre  FL11=C
- Riga figlio FL11=N  (riga che crea il movimento di magazzino - mappare causale)

Esempio :  a magazzino vengono impegnati e poi movimentati 100 art.A e 200 art. B, ma nessun codice KIT.


### Quantità Caso 2
Il codice Kit è reale come disponibilità e magazzino, i suoi componenti no.
- Riga padre  FL11=B  (riga che crea il movimento di magazzino - mappare causale)
- Riga figlio FL11=O

Esempio :  a magazzino vengono impegnati e poi movimentati 100 art. KIT, ma nessun codice art. A e B

### Prezzo Caso A
Il codice Kit ha un prezzo suo (recuperato da listino o imputato), componenti non significativi.
- Riga padre  FL29=blanks
- Riga figlio FL29=4

### Prezzo Caso B
Il codice Kit ha un prezzo derivato dal calcolo dei prezzi dei suoi componenti.
Sulla riga KIT padre vi è fisicamente il prezzo pari a 0, e nelle righe componenti è scritto il prezzo unitario (manuale o derivato da listino).
- Riga padre  FL29=3
- Riga figlio FL29=4

Ad esempio se A ha prezzo unitario 2 e B ha prezzo 1, il codice Kit ricalcola unb prezzo unitario pari a 4, dato da (100 * 2 + 200 * 1)/100.


### Prezzo Caso C
Il codice Kit non è significativo per il prezzo, che è esposto e calcolato per ogni componente.
- Riga padre  FL29=4
- Riga figlio FL29=blank


### Prezzo Caso D
Sia la riga del KIT, che i componenti partecipano ognuno con il suo prezzo all'importo del doc.
Ad esempio quando ogni componente ha il suo prezzo unitario, e il KIT ha il prezzo del montaggio.
- Riga padre  FL29=blanks
- Riga figlio FL29=blanks


## Fase di spedizione V5AT15
In fase di flusso spedizione da ordine, viene presentata sempre la riga padre seguita dalle righe figlie, a prescindere dagli ordinamenti. L'imputazione della quantità è possibile sempre e solo sulla riga padre (a prescindere dai flag) e viene poi spalmata in proporzione sulle righe collegate. Anche i filtri sono validi e attivi solo sulla riga padre.


## Spiegazione tecnica gestione distinta KIT
Essendo la DB del documento la struttura preposta a memorizzare il coeff. d'impiego del legame capo-componente del Kit questa verra' generata in automatico al verificarsi di qualsiasi condizione che, variando la struttura del kit in questo documento, rende necessaria una struttura di tale tipo.
Se per esempio viene variata la quantita' di un componente di un kit per il quale non e' stata prevista la creazione della DB documento nel flusso di immissione, la funzione di AGGRIG della  V5FUKIT provvedera' a crearla in automatico per potervi scrivere dentro il nuovo rapporto tra quantità capo e quantità componente (non essendo piu' valido quello della DB "standard").

**NB**
Le strade percorribili sono 2 : 
1) Non genero la DB del documento ma genero le righe partendo dalla DB del kit. La modifica della qta sul capo scatena una rifasatura che parte SEMPRE dalla DB del documento la cui creazione, in questo caso, viene lanciata automaticamente.
2) Genero la DB del documento (passo di flusso in immissione riga capo), la DB di riga doc. permette di tenere traccia di modifiche ai coeff. d'impiego del kit per quello specifico caso e quindi, al variare della qta del capo, rifasare correttamente i componenti.

**ATTENZIONE**

- In entrambi i casi il legame tra la riga del documento e il componente del kit viene fatta confrontando il cd componente, se ci fossero due legami con lo stesso cd articolo la routine di scansione troverebbe sempre solo il primo, motivo per cui in fase di immissione di una riga componente di kit viene controllato che, in presenza di altre righe componenti, il componente non sia gia' presente.

- Se viene effettuata una modifica/aggiunta/cancellazione di una riga componente di un kit questo scatena AUTOMATICAMENTE (sempre all'interno delle funzioni del V5FUKIT) la creazione della DB di documento essendo questo l'unico metodo per poter gestire i cambiamenti nel kit.


## Note generali
Se viene installato il modulo dei KIT, bisogna fare attenzione ad alcune cose : 
 - bisogna nei pgm sempre utilizzare le routine specifiche per il calcolo dei prezzi (£V5V, £V5F), per evitare di calcolare valori sbagliati.
 - bisogna fare attenzione nei report e negli Sql di capire se includere o meno le righe dei KIT, perchè in particolare sulle quantità si rischia nei totali di cosiderarli 2 volte.
 - nelle stampe dei documenti analizzare e decidere in base alle esigenze specifiche come visualizzare i KIT verso il cliente.


## Impostazioni per l'installazione

### Tabelle interessate

 :  : DEC T(ST) K(V5L) I(Gestione Tabella)
Gestisce sia i dati della gestione del conto lavoro e della gestione Kit. In ottica KIT va compilato il del tipo impegno, per reperire i parametri di memorizzazione delle distinta, e il campo tipo Kit, con l'elemento della V5K da utilizzare.

 :  : DEC T(ST) K(V5K) I(Gestione Tabella)
Definisce le tipologie di kit trattati a livello aziendale. Vengono mappati a questo livello i flag specifici delle righe di Kit, in modo da creare più modelli di comportamento in base a come sono compilati.
I flag della V5K sovrascrivono per i valori specifici i flag della riga.
- [V5K - Tipi Kit](Sorgenti/MB/DOC_OGG/TA_V5K)

### Programmi specifici
 :  : DEC T(OJ) P(*PGM) K(V5FUKIT)
E' il motore della gestione dei KIT.
Va utilizzato nei flussi riga documento, chiamato in molti funzioni e metodi. Si può attivare dalla tabella V5K, il relativo programma di aggiustamento, per indurre comportamenti specifici. Si chiama VV5FUKIT_x, e viene chiamato con gli stessi metodi del V5FUKIT.

 :  : DEC T(OJ) P(*PGM) K(V5FUKIT1)
Visualizza un Kit partendo dalla riga padre. Si può agganciare a flussi o popup, ed è nativa dalla gestione righe, F14 opzione 16.

### Configurazione consigliata
Gestione KIT a livello di ordine, con spedizione collegata. Nell'esempio che segue, la disponibilità è della riga padre e il prezzo è derivato da figli. Per creare comportamenti differenti, basta agire sulle tabelle V5K in particolare e V5B per diversificare i tipi riga.
>1. Creare 2 gruppi flag (B£Y) per l'ordine : 
  - riga padre (ad.es Fl10=3 FL11=B FL29=3)
  - riga figli (ad.es Fl10=4 FL11=O FL29=4)

2. Creare 2 gruppi flag (B£Y) per la bolla : 
  - riga padre (ad.es Fl10=3 FL11=B FL29=3)
  - riga figli (ad.es Fl10=4 FL11=O FL29=4)

3. Creare BRL con tipo distinta (ad es. OAK) con assieme riga ordine e comp. articolo

4. Creare P5I per indicare distinta origine e memorizzata (ad es. KIT)
   - Tipo impegno           KIT
   - Tipo origine           PE
   - Tipo distinta orig.    ART
   - Tipo distinta memor.   OAK
   - Modo costr.imp.mat.    D1
   - Tipo espl.distinta     1

5. Creare V5K per indicare i comportamenti specifici. (ad. es. K01)
   - Elemento               K01
   - Tipo aggr. capo        B
   - Tipo aggr. riga        O
   - SS tipo riga figlio    OA
   - Tipo riga figlio       071   (bisogna prima creare la riga)
   - Suff. pgm controllo    A
   - Calc. prezzo padre     3
   - Calc. prezzo figlio    4

6. Creare un tipo riga (V5BOA) dell'ordine per riga KIT padre : 
   - Codice tipo riga       061
   - Gest.prezzo O/N        N
   - Gest.q.tà   O/N        O
   - Gruppo flag riga       RK1
   - Tipo riga destinaz.    061    (anche questa deve essere una riga KIT padre)
   - Param. Cto Lavoro      K01

7. Creare un tipo riga (V5BOA) dell'ordine per riga KIT figlio : 
   - Codice tipo riga       071
   - Gest.prezzo O/N        N
   - Gest.q.tà   O/N        O
   - Tipo riga destinaz.    071    (anche questa deve essere una riga KIT figlio)
   - Gruppo flag riga       RK2

8. Analogamente creare un tipo riga (V5BDA) della bolla per riga KIT padre, con i seguenti campi specifici : 
   - Codice tipo riga       061
   - Gruppo flag riga       RK3
   - Param. Cto Lavoro      K01

9. Analogamente creare un tipo riga (V5BDA) della bolla per riga KIT figlio, con i seguenti campi specifici : 
   - Codice tipo riga       071
   - Gruppo flag riga       RK4

10. Importante configurare al meglio i flussi delle righe documento. Questa è la configurazione consigliata, delle B£H - B£JDR
Riga Ordine : 
-    **I-DROA  Creazione**
--      C.B£J Descrizione                      Programma    Funz/metodo
--      IOA30 Aggiungi Padre KIT               V5FUKIT      AGGPAD
--      IOA35 Crea DB documento KIT            P5FUDDC      CRE CIE
--      IOA40 Crea dettaglio KIT               V5FUKIT      COSFIG
--      IOA45 Aggiungi Comp.KIT                V5FUKIT      AGGFIG
-   **P-DROA  Pre Eliminazione**
--      C.B£J Descrizione                      Programma    Funz/metodo
--      POA10 Cancella Padre KIT               V5FUKIT      CANPAD
--      POA15 Cancella Comp. KIT               V5FUKIT      CANFIG
-   **M-DROA  Post Modifica**
--      C.B£J Descrizione                      Programma    Funz/metodo
--      MOA30 Modifica padre KIT               V5FUKIT      MODPAD
--      MOA40 Modifica comp. KIT               V5FUKIT      MODFIG
Riga Bolla  : 
-    **P-DRDA  Pre Eliminazione**
--      C.B£J Descrizione                      Programma    Funz/metodo
--      PDA10 Cancella Padre KIT               V5FUKIT      CANPAD
-    **M-DRDA  Post Modifica**
--      C.B£J Descrizione                      Programma    Funz/metodo
--      MDA30 Modifica padre KIT               V5FUKIT      MODPAD
--      MDA40 Modifica comp. KIT               V5FUKIT      MODFIG


