# Avviamento Veloce Q9000 1

I passi per eseguire un avviamento minimalista del Q9000 sono quelli necessari alla messa in opera di un sistema di qualità che abbia copertura sui seguenti processi : 

# Processi Primari
 ** Creazione lotti di origine esterna :  acquisto, conto lavoro, resi cliente
 ** Classi funzionali dell'articolo e di abilitazione del fornitore
 ** Piani di campionamento :  particolare attenzione al free pass
 ** Movimentazione dei materiali conseguente al collaudo
 ** Collaudo lotti
 ** Registrazione non conformità
 ** Registrazione azioni correttiva, accettazioni in deroga, etc

# Processi Secondari
 ** Creazione lotti di produzione
 ** Cicli di collaudo
 ** Vendor rating
 ** Documentazione
 ** Strumenti di misura
 ** Manutenzione Impianti

## Primo punto fondamentale :  creazione del Lotto di qualità, oggetto fulcro del sistema

I lotti vengono creati con naturalezza in Smeup partendo dai punti dove ci sono le aggregazioni di materiale :  le entrate materiali e la generazione dell'ordine di produzione.

_7_NOTA :  il pgm che crea i lotti è il CQER11_S2 . S2 è il codice impostato sulla B£1 nel campo Lotti Tenete presente che la vecchia interfaccia (SM) non era sensibile al numeratore che era cablato, mentre S2 sente il numeratore che è agganciato al tipo lotto (tab CQL).

## Entrate materiale
Si agganciano al tipo riga delle bolle di entrata materiale tramite il campo "tipo lotto" che si vuole creare. Ovviamente i flag della riga debbono prevedere il collegamento alla qualità (flag 09 blank) , ed anche il modello della testata deve prevedere il collegamento (anche sul modello è presente il tipo lotto, per le risalite). La creazione del lotto viene lanciata dal collegamento della bolla, con l'azione V5do15x, metodo CO inserita alla fine del flusso V5G.

Tabelle fondamentali, in ordine di compilazione (prelevare da modello) Interfaccie in  B£1 :  Lotti/Rintra = S2, Non conformità = SM, Rich.Int. = SM
Tab CQ1, impostazioni Base :  (prelevare da modello)
![CQAVVI_01](http://localhost:3000/immagini/CQAVVI/CQAVVI_01.png)Tabella CQL :  tipo lotto, prelevare da smemod tipo AC e PR (aggiungere C/lavoro, resi Cliente, etc)
![CQAVVI_02](http://localhost:3000/immagini/CQAVVI/CQAVVI_02.png)
_7_Il tipo lotto è una informazione fulcro del sistema
Dal tipo lotto derivano 3 rami fondamentali : 
 - La micrologistica conseguente al collaudo, ovvero dove vanno i pezzi buoni, quelli di scarto, quelli non conformi, etc. La tab. CRP ci permette di movimentare opportunamente tra le aree di magazzino tipi lotti diversi (il materiale di produzione o i resi cliente vanno in aree diverse dall'entrata di acquisto!)
 - Il tipo ciclo di collaudo scelto per il lotto
 - Il tipo non conformità che viene proposto all'inserimento di un difetto
## Classe funzionale dell'articolo, tab CQQ
![CQAVVI_03](http://localhost:3000/immagini/CQAVVI/CQAVVI_03.png)La classe funzionale dell'articolo è determinante per definire i seguenti comportamenti : 
 - Se l'articolo deve creare un lotto (ad esempio, la cancelleria o gli starcci non creano il lotto)
 - Se il lotto nasce in Free Pass oppure deve essere collaudato
 - Qual'è il target di qualità per l'articolo (chiamato AQL dai Quality Engineers ) detto Average Quality Level. Vedere in wikipedia per approfondire :  in sintesi un AQL di 1 significa che si punta
ad avere al massimo 1 % di pezzi difettosi. Per dare un'idea dei valori di riferimento , nelle produzioni meccaniche di alta qualità, si punta ad avere un AQL di 0,01, ossia 1 pezzo difettoso su 10.000 ! Lo "zero difetti" non è contemplato.
 - Se l'articolo è da matricolare :  questa caratteristica attiva in smeup diverse obbligatorietà sui campi "Matricola".
 - con quale piano di campionamento trattare il lotto generato :  questo porta a definire la numerosità del campione statistico da analizzare per essere sicuri dell'AQL del lotto.

La classe funzionale dell'articolo (tabella CQQ) può essere attribuita ad ogni singolo articolo direttamente dalla gestione dell'articolo (è un campo di BRarti0f), oppure derivata dalla classe materiale (è un campo di tab CLS).

Per un avviamento veloce del Q9000, si suggerisce di definire una classe funzionale ** di default che non gestisca i lotti, e di definire un'altra classe CF-1 che movimenta a lotti da mettere come attributo sulle classi materiali che si vuole lottizzare

## Classe di abilitazione del fornitore, tab CQV
![CQAVVI_04](http://localhost:3000/immagini/CQAVVI/CQAVVI_04.png)I fornitori possono essere classificati con diverse gradazioni di "affidabilità qualitativa" tramite l'attribuzione in anagrafica Brenti0f della classe di abilitazione. Tale classe identifica le classi funzionali degli articoli per cui il fornitore è qualificato.
Per un avviamento veloce del Q9000, si suggerisce di attribuire a qualsiasi fornitore la classe AB-0 che deve essere autorizzata alla classe funzionale più critica. In questo modo tutti i fornitori sono autorizzati a fornire tutti gli articoli.

A questo punto  una entrata materiale riesce a creare un lotto , assegnargli un piano di campionamento in funzione di CQQ e CQV.
Il piano di campionamento può essere reso sensibile alla storia pregressa di quell'articolo/fornitore (ossia i lotti precedenti) se sulla classe funzionale sono stati attivate le regole di commutazione, e le stesse sono state inserite nella tabella CQR (prelevare esempi da smemod).
In questo caso il piano di campionamento può essere appesantito o alleggerito, fino al Free Pass.
## Attenzione al Free Pass
![CQAVVI_05](http://localhost:3000/immagini/CQAVVI/CQAVVI_05.png)Quando una coppia Articolo/Fornitore finisce in Free Pass, bisogna prevedere una modalità di audit per verificare ogni tanto che la coppia mantenga le caratteristiche di affidabilità che ci permettono di saltare il controllo. Per fare ciò bisogna sia impostare nella CQR un appesantimento del free pass al presentarsi di non conformità, sia nella CQQ prevedere una frequenza di audit.

## Micrologistica di magazzino
La tabella CRP prevede come elementi inseriti solamente i tipi lotto :  in questo modo ogni tipo lotto trova le sue movimentazioni previste.
Essenzialmente nella tabella CRP si possono dire le seguenti cose : 
 - in che area si carica il materiale da collaudare o il materiale in Free Pass (si scrivono le causali di magazzino che si sovrappongono a quelle impostate sul tipo riga della bolla di entrata materiali!
 - con che causali si muove il magazzino quando si registra l'esito di collaudo.
NOTA :  l'esito di collaudo permette di scomporre la quantità del lotto in cinque quantità separate, chiamate  : 
 * Qty Conforme
 * Qty Non Conforme
 * Qty Scarto
 * Qty Rilavorare
 * Qty Selezionare
Tali quantità possono essere movimentate alla fine del collaudo in modo differente, generando quindi la micrologistica di magazzino (i resi cliente finiscono in posto diverso dai non conformi di acquisto)
![CQAVVI_06](http://localhost:3000/immagini/CQAVVI/CQAVVI_06.png)## Collaudo Lotti
Per operare il collaudo lotti è necessario solo avere impostata la tabella CQB degli esiti di collaudo.
![CQAVVI_07](http://localhost:3000/immagini/CQAVVI/CQAVVI_07.png)La tabella CQB permette di attivare o disattivare i movimenti di magazzino che si attivano tramite CRP (è utile in quanto la rettifica di esito conseguente all'aver trovato il lotto difettoso dopo collaudo, che viene registrata con un esito specifico (PC) , non deve attivare la movimentazione di magazzino !) Inoltre tale tabella identifica se l'esito è da classificarsi tra i conformi o no, e se deve essere definita "declassante" rispetto all'esecuzione delle regole di commutazione.
Per un avviamento veloce del Q9000, prelevare la tabella dalla Smemod

## Dichiarazione difetti, Non conformità
Innanzi tutto bisogna aver definito i tipi di non conformità :  prelevare da Smemod  la tab. CQ§! Il tipo di non conformità deve essere collegato al tipo lotto.
Tramite il tipo non conformità è possibile registrare i difetti (uno per non conformità) ma anche l'effetto che tale non conformità deve avere sul pagamento fatture  :  infatti sarà possibile entro il
2011, avere la creazione automatica di note di accredito nei confronti del fornitore al momento della registrazione della non conformità.
Questo si definisce sul gruppo flag associato al tipo non conformità (tab CQ§)
![CQAVVI_08](http://localhost:3000/immagini/CQAVVI/CQAVVI_08.png)Anche lo sviluppo delle quantità e valori della non conformità è sul gruppo flag.
NOTA :  l'inserimento della non conformità su un lotto permette il cambio dell'esito di collaudo dello stesso (utile per attivare le regole di commutazione dei piani di campionamento)
## registrazione azione correttiva
Dalla non conformità, se opportunamente inserita tra le azioni utente (B£H A-NC) l'azione con pgm  NCDEVRI   e metodo INS si crea una o più richieste di intervento collegate alla non conformità.
## Creazione lotti di produzione
La creazione del lotto di tipo PR, legato al'ordine di produzione si effettua dal menu funzioni oggetto OR (B£H A-OR oppure I-OR) inserendo il pgm CQP5L01, metodo INS. Il tipo lotto da creare è riportato nella tabella P5T (tipo ordine di produzione)
## Cicli di collaudo
I cicli di collaudo sono sempre di difficile gestione per il fatto che essi possono/dovrebbero indicare due informazioni basilari : 
 - quale è la lista delle caratteristiche critiche dell'oggetto che debbono essere controllate
 - quali sono i valori di riferimento per quelle caratteristiche
Se ci limitassimo alla prima informazione che è di tipo qualitativo e non quantitativo, ossia che potrebbe accettare un esito del tipo "OK, conforme" oppure "NO, non conforme" allora l'ingegnerizzazione dei cicli di collaudo sarebbe semplice.
Infatti sfruttando la costruzione per OAV dei tipi ciclo (Tabella CRJ) potremmo definire un tipo ciclo per la classe materiale e far sì che tutti gli articoli di quella classe materiale risalgano a quel singolo ciclo. Quindi basterebbe scrivere un ciclo per classe materiale!
![CQAVVI_09](http://localhost:3000/immagini/CQAVVI/CQAVVI_09.png)Ovviamente le fasi di controllo di quel ciclo dovrebbereo far riferimento al disegno dell'articolo specifico dove si troverebbero le "quote" specifiche dell'articolo.
Se invece si vuole registrare di ogni singolo articolo le quote critiche numeriche, allora sul ciclo di collaudo debbono comparire i valori di riferimento specifici dell'articolo, e non
si possono utilizzare i cicli per famiglia!
Tra i due approcci ci sono di mezzo 6 mesi di lavoro per gli uomini della qualità!
In effetti si suggerisce un percorso di avvicinamento di questo tipo : 
 - riuscire a "vedere" i disegni (o le schede tecniche) degli articoli tramite la registrazione in un server aziendale (o nell'IFS). Sui disegni sono riportate normalmente le quote da controllare.
 - Scrivere cicli di famiglia collegati ad un OAV dell'articolo (classe materiale, tipo di articolo, etc) o della coppia art/fase di lavoro (es. Tipo di lavorazione, CDL, etc). Sul ciclo si riporta il tipo di documento da illuminare all'occorrenza.
In questo contesto si registrano esiti di tipo OK o NON OK.
![CQAVVI_10](http://localhost:3000/immagini/CQAVVI/CQAVVI_10.png)## Vendor rating
Copiare tutte le tabelle del modello (Smemod) in cui sono stati preparati anche troppi indici per clienti e fornitori
## Documentazione
Consiglio di gestire almeno il documento di tipo DISE, in modo da visualizzare i disegni.
Copiare da modello le tabelle B§D, B§P, B§T
