# Sme.App V 2.00  (marzo 2013)
Sme.App è un esempio di applicazione mobile che  : 
* contribuisce a rafforzare il Brand Sme.UP dando la percezione concreta di essere al passo con l'innovazione tecnologica;
* fornisce una dashboard con informazioni relative all'andamento aziendale.
Le informazioni di riferimento sono ricavate da : 
-  moduli applicativi Sme.UP
- **"Impresa Virtuale"** (applicazione web con cui i clienti avranno accesso a documenti, informazioni commerciali ed amministrative).

I destinatari dell'applicazione sono responsabili funzionali delle aree vendita, amministrativa, finanziaria, controllo di gestione.

Sme.App è scaricabile dall'Apple Store.
Sme.App, è disponibile per i dispositivi IOS iphone e ipad.
L'applicazione si presenta in lingua italiana o inglese in funzione della lingua del device.

**Seguono due screeshot di esempio**

![001](http://localhost:3000/immagini/MOBASE_V2/001.png)
![002](http://localhost:3000/immagini/MOBASE_V2/002.png)
**Una volta scaricata l'applicazione ci si presenta questa videata : **

![003](http://localhost:3000/immagini/MOBASE_V2/003.png)
L'ambiente demo **"demo version"** è accessibile senza specificare nessuna credenziale.
Chiunque scarichi l'app potrà accedere all' ambiente demo, al suo interno troverà un documento di aiuto che descrive la dinamica dell'applicazione.

Per i tutti i collaboratori interni sarà possibile accedere, tramite login, ai dati reali del proprio ambiente gestionale con queste credenziali : 
Server   :  app.smeup.it
Username  :  piegagli
Password  :  xxxxxxxxxxx
Environment  :  Paderno

Lo username e la password sono riferiti all'utenza di SRVAMM di Erbusco su cui risiede il nostro sistema gestionale.
L'Environment rappresenta la propria sede di appartenenza :  Paderno, Erbusco....
Fatta la login, si deve digitare una parte della ragione sociale del cliente desiderato, quindi premere il tasto "save" in alto a destra.
Selezionato il cliente si accede al menù, al suo interno si trova un documento di aiuto che descrive la dinamica dell'applicazione.
Questa applicazione utilizza le funzionalità di "impresa virtuale" già disponibile via web

Trattandosi di dati reali si raccomanda la massima discrezione.

Per i nostri clienti che già accedono ai propri dati via web (impresa virtuale) è possibile accedere, tramite login, ai dati reali (soli i propri) del nostro ambiente gestionale con queste credenziali di esempio : 
Server   :  app.smeup.it
Username  :  000013
Password  :  xxxxxxxxxxx
Environment  :  Clienti
Lo username e la password sono già in possesso dei nostri clienti, coloro che ne avessero bisogno la possono richiedere al commerciale che segue il cliente.

abbiamo due colleghi di riferimento : 
Applicazione mobile :  Andrea Marino
Impresa virtuale Web  :  Claudio Minelli


## Cosa dobbiamo sapere per rispondere ai nostri clienti : 

Siamo ora in grado di utilizzare l' applicazione e di farla apprezzare. Possiamo utilizzare le due modalità descritte, disponibili 24 per 7, esclusivamente in modalità "on line". I dati che esponiamo sono forniti dalle nostre "FUN". Quello che  siamo in grado di ottenere attraverso Looc.up, tendenzialmente lo potremo esporre sulla nostra app.
Per rendere disponibili i dati dell'ambiente di demo abbiamo sfruttato le pontenzialità dei costruttori (LOA15) con la generazione di dati casuali su oggetti reali mascherati a tempo di esecuzione.
DI seguito un esempio di come abbiamo lavorato per produrre l'analisi dello scaduto : 


## scaduto

* anzianità scaduto
* F(EXB;LOA15_SE;LIS.PAR) 1(;;PR.04.01) 2(;;04) P(PAR2(1)) INPUT()

![004](http://localhost:3000/immagini/MOBASE_V2/004.png)
* dimensioni dello scaduto
* F(TRE;LOA15_SE;LIS.DIM) 1(;;PR.04.01) 2(;;) INPUT()
![005](http://localhost:3000/immagini/MOBASE_V2/005.png)
* scaduto per agente
* F(EXB;LOA15_SE;LIS.PAR) 1(;;PR.04.01) 2(;;03) P(ParRic(1)) INPUT(WHR(BTCD04 = '020'))
![006](http://localhost:3000/immagini/MOBASE_V2/006.png)
## NOTA BENE
Alla domanda del cliente che chiede l'utilizzo della app. con i dati del proprio gestionale dobbiamo rispondere che è necessario fare nascere un progetto.

## Il progetto prevede almeno le seguenti attività : 

* analisi dei dati da presentare nell'applicazione;
* selezione delle funzioni Sme.UP e definizione delle implementazioni;
* definizione della sequenza di navigazione;
* definizione dell'infrastruttura;
* realizzazione dell'applicazione in ambiente Looc.up;
* configurazione del server;
* test e collaudo;
* rilascio;


Queste attività sono le medesime che abbiamo sviluppato al nostro interno per quanto detto in precedenza.


