# Avviamento veloce delle prevsioni Holt Winters
## Introduzione
La struttura del processo che porta a costruire le previsioni e a renderle disponibili per l'MRP si basa su due step fonamentali : 
 * _2_Flusso di costruzione dello storico e della funzione Holt Winters
 * _2_Flusso pre MRP che aggiusta le previsioni con le forzature manuali, le nettifica dall'ordinato e prepara il forecast che entrerà nell'MRP.

## Prerequisiti
Ci sono n tabelle che debbono essere allineate prima di partire. Esse sono : 
* gli indici dell'articolo ed il tema/contesto su cui registrare nel D5COSO i risultati sintetici del calcolo (tra cui la classe previsiva)
* la tabella MP2 che contiene le indicazioni per assegnare le classi previsive
* la tabella C£I e B£NMP dove sono definiti i parametri interni delle viste risultato HW, utile per comprendere la stratificazione degli articoli in previsivi e non.

Per effettuare quanto sopra eseguire i seguenti comandi
Call D5FS01A per i contesti AR ed MP
UP FTB    MP2
UP FTB    C£I, B£NMP

Importante :  bisogna collegare i parametri impliciti alla vista risultato del calcolo Holt Winters tramite il campo "significato campi liberi" - vedi esempio seguente

![MP_001_45](http://localhost:3000/immagini/MPHW02/MP_001_45.png)

## Flusso HW10 - costruzione storico e Holt Winters
Riportiamo un esempio di flusso costruzione storico : 
![MPPIAN_049](http://localhost:3000/immagini/MPHW02/MPPIAN_049.png)Questo flusso va schedulato solo una volta ad inizio mese (*mthstr), costruisce un piano che ha come data di inizio oggi - 24 mesi, periodicità  di 36 mesi, ossia predispone le prime 24 colonne nel passato e dalla 25 alla 36 nel futuro.

### H010    Crea piano HW
Programma MPAP99 con le seguenti parametrizzazioni
![MPPIAN_050](http://localhost:3000/immagini/MPHW02/MPPIAN_050.png)
### H020    OC1 - Riprendi storico
Carica nella vista OC1 le quantità ordinate negli ultimi 24 mesi, programma MPAPV5C, con le seguenti parametrizzazioni
![MPPIAN_051](http://localhost:3000/immagini/MPHW02/MPPIAN_051.png)La parzializzazione ULT 24 si ottiene mettendo questo filtro sulla data richiesta : 
![MPPIAN_052](http://localhost:3000/immagini/MPHW02/MPPIAN_052.png)
### H030    OC3 - Correggi storico
Questa funzione permette di sostituire gli articoli obsoleti con gli articoli nuovi, scrive anche una vista di passaggio dove si trovano gli articoli sostituiti con le quantità negative ed i nuovi con le stesse quantità positive. Questo permette di controllare ciò che è entrato e ciò che è uscito. __Il legame tra entrante ed uscente (phase-in e phase-out) è descritto dalla distinta di tipo £CS! Questo tipo distinta è molto semplice, padre AR e componente AR, lega l'uscente (padre) con l'entrante (componente) . Se si utilizza la data di validità questa assume il significato di data di phase-in phase-out.

Se la data di validità è nel passato, tutto lo storico è convertito dall'articolo uscente in articolo entrante.

Se la data di validità è nel futuro, allora la conversione viene fatta sulle previsioni create, da quella data in poi.

Quindi, il passo di correzione/sostituzione potrebbe essere presente due volte nel flusso di costruzione delle previsioni :  come correzione dello storico, prima del calcolo holt winters, e dopo il calcolo come correzione delle prevsioni

Questo passo di flusso necessita dell'esistenza di uno script di nome MPAP53 che normalmente si trova in SMEDEV/SCP-SET, ed utilizza il pgm MPAP53A con la seguente parametrizzazione : 
![MPPIAN_053](http://localhost:3000/immagini/MPHW02/MPPIAN_053.png)
### H040    HW1 Sviluppa Holt Winters
Questo passo utilizza il pgm MPAP48, con le seguenti parametrizzazioni
![MPPIAN_054](http://localhost:3000/immagini/MPHW02/MPPIAN_054.png)
### H050    Cancella classi >=5
Questo passo utilizza il pgm MPGP02X, con le seguenti parametrizzazioni
![MPPIAN_055](http://localhost:3000/immagini/MPHW02/MPPIAN_055.png)Il programma esegue una cancellazione selettiva dalla vista piano di tutti gli articoli con classe previsiva > 5. __Questa cancellazione è FACOLTATIVA :  infatti, pur non essendo affidabili le previsioni degli articoli con classe maggiore di 5, esse rappresentano comunque un fabbisogno previsionale che permette di pianificare qualche copertura per quegli articoli. Se si cancellano queste previsioni si resta senza fabbisogni, a meno di inserire manualmente delle scorte minime per poter generare una copertura pianificata!

Per l'impostazione della cancellazione bisogna : 
 * avere l'OAV dell'articolo J/H01 = Classe previsiva
 * impostare nella tabella C£Z tra le sintesi articolo l'OAV J/H01
 * collegare ai raggruppamenti articolo (Tab. C£S) la tabella delle sintesi C£Z che contiene l'OAV J/H01
 * memorizzare nelle parzializzazioni del programma di eliminazione selettiva dati piano MPGP02G il filtro per classe previsiva > 5
 * utilizzare la memorizzzazione come parametro in questo passo di flusso
**Inserimento in tabella C£Z_AR della classe previsiva**
![MPPIAN_056](http://localhost:3000/immagini/MPHW02/MPPIAN_056.png)**Collegamento in tabella C£S del sottosettore tabella sintesi C£Z**
![MPPIAN_057](http://localhost:3000/immagini/MPHW02/MPPIAN_057.png)**Memorizzazione parzializzazioni HWPR>5**
![MPPIAN_058](http://localhost:3000/immagini/MPHW02/MPPIAN_058.png)![MPPIAN_059](http://localhost:3000/immagini/MPHW02/MPPIAN_059.png)![MPPIAN_060](http://localhost:3000/immagini/MPHW02/MPPIAN_060.png)
### H060    CREA PIANO FC
Questo passo utilizza il pgm MPAP99, con le seguenti parametrizzazioni : 
![MPPIAN_061](http://localhost:3000/immagini/MPHW02/MPPIAN_061.png)Il passo di creazione piano FC viene fatto in questo flusso, che gira solo una volta al mese, per poter riprendere la vista delle previsioni forzate, di modo che poi sarà gestita nel nuovo piano (di solito subisce continui aggiornamenti da parte del Demand Manager).

### H070    RIPRENDE FORZATURA
Questo passo utilizza il pgm MPAP02F, con le seguenti parametrizzazioni : 
![MPPIAN_062](http://localhost:3000/immagini/MPHW02/MPPIAN_062.png)**IMPORTANTE** :  la ripresa della forzatura deve riprendere ANCHE i record con i valori zero (sono gli articoli per cui si vogliono annullare le previsioni !). Per fare questo, BISOGNA impostare il flag "conserva zeri" !

## Flusso MP20 - Forecast  PRE MRP
Riportiamo un esempio di flusso pre MRP per la ripresa delle previsioni, questo flusso va inserito nei flussi pre-MRP (Gruppo azioni = MRP-A), con una azione come la seguente : 

![MPPIAN_064](http://localhost:3000/immagini/MPHW02/MPPIAN_064.png)
L'obiettivo del flusso è quello di recuperare dal piano HWxxx le previsioni, fonderle con le forzature e nettificarle con gli ordini in corso.

![MPPIAN_063](http://localhost:3000/immagini/MPHW02/MPPIAN_063.png)
### P010   Crea piano previsioni
Questo passo utilizza il pgm MPAP99, con le seguenti parametrizzazioni
![MPPIAN_065](http://localhost:3000/immagini/MPHW02/MPPIAN_065.png)Viene creato un piano che ha radice FC e comincia dal mese presente. (**Nota**, nella normalità il piano già esiste perchè è stato creato nella elaborazione mensile del flusso delle previsioni HW10.

### P020   Riprendi Previsioni        HW1
Questo passo utilizza il pgm MPAP02F, con le seguenti parametrizzazioni
![MPPIAN_066](http://localhost:3000/immagini/MPHW02/MPPIAN_066.png)Si riprende l'ultimo sviluppo Holt Winters (vista delle previsioni).

### P025   Confronta con forzatura    PRE
Questo passo utilizza il pgm MPAP03A, con le seguenti parametrizzazioni
![MPPIAN_067](http://localhost:3000/immagini/MPHW02/MPPIAN_067.png)A questo punto si confronta con le previsioni forzate, utilizzando l'operatore PRIOF che fa vincere anche i records con tutti zeri!

### P028   Eventuale pulizia records
Questo passo non è obbligatorio, qui è citato, anche ne non si vede nel flusso, come promemoria e potrebbe essere attivato quando si vogliano eliminare dalla vista delle previsioni determinati gruppi di articoli. Il passo utilizza il pgm MPGP02X per l'eliminazione selettiva dei dati piano con il filtro opportuno sul gruppo di articoli.

### P030   Riprendi ordinato          ORD
Questo passo utilizza il pgm MPAPV5C, con le seguenti parametrizzazioni
![MPPIAN_068](http://localhost:3000/immagini/MPHW02/MPPIAN_068.png)Si riprende l'ordinato, per data richiesta (per assicurare la coerenza con la costruzione delle previsioni che è sempre fatta per data richiesta...)

### P040   Determina delta previsioni DEL
Questo passo utilizza il pgm MPAP03A, con le seguenti parametrizzazioni
![MPPIAN_069](http://localhost:3000/immagini/MPHW02/MPPIAN_069.png)Si determina il delta, solo se positivo, tra la previsione e l'ordinato; il contenuto della vista DEL viene pescato da una fonte di tipo MP, con segno negativo, ed entra nel gruppo fonti dell'MRP insieme all'ordinato : 

![MPPIAN_070](http://localhost:3000/immagini/MPHW02/MPPIAN_070.png)
## Attivazione della scorta minima Holt Winters

Per attivare la lettura della scorta minima coerente con le previsioni generate da Holt Winters e con il livello di servizio desiderato per l'articolo, bisogna eseguire i seguenti passi : 
* attivare nell'anagrafica magazzino/articolo il campo "Calcolo scorta/lotti" con il valore   " £01" che significa  :    Scorta da previsioni
* definire una fonte disponibilità (M5E se presente o M5F se futura ) di origine SC o SD , opportunamente parametrizzata in modo che "legga" il valore calcolato da HW : 
 Par     Risalita scorta minima
            Sc.inserita risalita Sc.calcolata
 A         Sc.calcolata risalita Sc.inserita
 B         Sc.inserita
 C         Sc.calcolata
 D         Sc.calcolata se presente criterio

NOTA BENE :  con il parametro Blank , che è la condizione in cui si trova la vecchia fonte scorta minima, la scorta calcolata viene comunque risalita quando la scorta inserita è uguale a zero!
Questa condizione è pericolosa se non si vuole far entrare nella pianificazione la scorta calcolata per gli articoli trattati da Holt Winters, quindi si consiglia inizialmente di parametrizzare la vecchia fonte scorta minima  con il parametro = 'B'.

