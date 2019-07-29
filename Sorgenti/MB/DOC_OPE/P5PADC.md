# Generalità
La gestione della produzione a disponibilità chiamata (PDC) è la particolare modalità operativa che, senza la codifica di ordini, permette la gestione della produzione legata dinamicamente a una domanda in continua evoluzione e alla natura fisica dello stato della produzione stessa (quantità del materiale nelle varie ubicazioni) e degli eventi che si verificano (spostamenti tra ubicazioni, sia per alimentazione di un centro verso un'ubicazione a monte di esso, sia per effetto di una lavorazione, da un'ubicazione a monte ad una a valle).

# Informazioni necessarie
Per iniziare la gestione della PDC devono essere definite delle impostazioni di carattere generale e delle informazioni a livello articolo.
Nelle impostazioni a carattere generale si comprendono le politiche di riordino, le fonti presenti e future, i gruppi fonte associati a questa gestione, i parametri risorse necessari per gestire il ciclo logistico e le impostazioni generali della PDC.
Nelle impostazioni a livello articolo si comprendono i parametri di pianificazione e il ciclo logistico.

## Definizione fonti e gruppi fonte per PDC
Dovrà essere costruita una fonte futura con fabbisogno giornaliero e, di conseguenza, deve essere definito un gruppo fonti da utilizzare nel calcolo del fabbisogno giornaliero.
Questo gruppo fonti deve essere costituito da una fonte esistente di movimenti post MRP (fonte utente) e da una fonte futura degli ordini pianificati per PDC, come da esempio : 

![P5_02_01](http://localhost:3000/immagini/MBDOC_OPE-P5PADC/P5_02_01.png)
![P5_02_02](http://localhost:3000/immagini/MBDOC_OPE-P5PADC/P5_02_02.png)
Utilizzando il gruppo fonti che raggruppa le due fonti prima definite (nell'esempio il gruppo fonti si chiama ADC) si costruisce la fonte di domanda PDC, come da esempio seguente : 

![P5_02_03](http://localhost:3000/immagini/MBDOC_OPE-P5PADC/P5_02_03.png)
La fonte futura di domanda PDC dovrà essere inserita nel gruppo fonti per la domanda PDC che viene poi richiamata a livello di impostazioni generali PDC (P52) : 

![p5_02_14](http://localhost:3000/immagini/MBDOC_OPE-P5PADC/p5_02_14.png)
Deve inoltre essere definita anche la fonte esistente di disponibilità dei componenti montati nei contenitori nel WIP PDC (area WC) : 

![P5_02_04](http://localhost:3000/immagini/MBDOC_OPE-P5PADC/P5_02_04.png)
# Definizione politica di riordino per PDC
Nella tabella >M5A deve essere definita la politica di riordino PDC, che sarà associata, nei parametri di pianificazione, agli articoli da gestire a PDC : 

![P5_02_05](http://localhost:3000/immagini/MBDOC_OPE-P5PADC/P5_02_05.png)
>N.B. :  La fonte di pianificazione è quella usata dai programmi di schedulazione PDC che, leggendo i suggerimenti MRP, predispongono i contenitori pianificati da lanciare.

## Definizione parametri risorsa
Deve essere definita una categoria parametri di risorsa (se già esiste si possono aggiungere nuovi parametri), in cui un parametro rappresenta l'ubicazione pre-macchina e un altro rappresenta l'ubicazione post-macchina.
Nell'esempio seguente abbiamo : 

![P5_02_09](http://localhost:3000/immagini/MBDOC_OPE-P5PADC/P5_02_09.png)
I nomi dei parametri generati per descrivere le ubicazioni pre e post macchina devono essere riportati nelle impostazioni generali della PDC (pertanto, una volta generati e battezzati, non possono più cambiare nome salvo riallineamento dell'intera parametrizzazione PDC).

## Attribuzione parametri risorsa
Devono essere definiti dei gruppi risorsa a cui associare i parametri risorsa : 

![P5_02_06](http://localhost:3000/immagini/MBDOC_OPE-P5PADC/P5_02_06.png)
Tutte le risorse presenti nel ciclo di lavorazione candidate a diventare anche punti di controllo della definizione del ciclo logistico dovranno essere associate a uno di questi gruppi risorse (vedi esempio seguente).

![P5_02_10](http://localhost:3000/immagini/MBDOC_OPE-P5PADC/P5_02_10.png)
## Impostazioni generali
Per completare le informazioni legate alle impostazioni generali si definiscono i parametri guida della gestione PDC compresi nella tabella di personalizzazione >P52.

![p5_02_08](http://localhost:3000/immagini/MBDOC_OPE-P5PADC/p5_02_08.png)
## Definizione parametri di pianificazione per articolo
Nei parametri di pianificazione degli articoli da gestire a PDC deve essere inserita come politica di riordino la politica PDC definita in precedenza ed assegnata una quantità di lotto multiplo : 

![P5_02_13](http://localhost:3000/immagini/MBDOC_OPE-P5PADC/P5_02_13.png)
## Costruzione ciclo logistico
Per attivare la gestione del ciclo logistico si parte dal formato di sintesi produzione a disponibilità chiamata, selezionando in sequenza >FUNZIONI SU RISORSE (3) e >STRUTTURA LOGISTICA (3).
Si presenta il formato seguente : 

![P5_02_19](http://localhost:3000/immagini/MBDOC_OPE-P5PADC/P5_02_19.png)
Se siamo in fase di costruzione del ciclo logistico (cioè non c'è nessuna ubicazione pre o post macchina), si presentano solo le macchine che eseguono operazioni del ciclo di produzione.
Inserendo l'opzione 2  in corrispondenza della risorsa interessata, si aprirà la lista dei parametri di risorsa in cui inserire le ubicazione pre o post macchina (perché si possa aprire la gestione dei parametri per risorsa deve essere stato associato l'opportuno gruppo risorsa alla macchina).

![P5_02_11](http://localhost:3000/immagini/MBDOC_OPE-P5PADC/P5_02_11.png)
# Pianificazione Schedulazione PDC
La pianificazione e schedulazione delle attività PDC parte dalla elaborazione MRP, in coda all'elaborazione MRP vengono lanciati in successione : 
 * **la rifasatura degli impegni risorse**, che allinea gli impegni risorse dei materiali PDC con quanto richiesto dai contenitori PDC in corso di esecuzione e dai contenitori PDC pianificati dall'MRP. Gli impegni risorse vengono calcolati in base ai tempi di esecuzione per macchina specificati nei cicli di produzione e ordinati in base alla  data prevista.
 * **la schedulazione delle macchine**, applicando le regole di priorità e di abbinamento previste per le macchine interessate alla schedulazione o per le macchine appartenenti al gruppo risorse predefinito.

## Reports di analisi
Per verificare l'esito della schedulazione sono previsti due report principali : 
 * Stampa del GANTT della schedulazione
 * Analisi / stampa impegni risorse

### Stampa GANTT schedulazione
Questa stampa evidenzia la schedulazione dei contenitori (in corso o pianificati) presentando l'impegno sulle varie risorse in forma grafica.
Il formato di selezione per la stampa è il seguente e, oltre alle selezioni, nella videata deve essere stabilito anche lo scenario su cui operare (F20).

![P5_02_25](http://localhost:3000/immagini/MBDOC_OPE-P5PADC/P5_02_25.png)
Un esempio di output : 

![P5_02_15](http://localhost:3000/immagini/MBDOC_OPE-P5PADC/P5_02_15.png)
### Analisi / stampa impegni risorse
Questo report permette di visualizzare, ordinato per data di inizio schedulata, le attività (contenitori) che devono essere eseguite su una certa macchina.
Il formato di selezione è il seguente : 

![P5_02_17](http://localhost:3000/immagini/MBDOC_OPE-P5PADC/P5_02_17.png)
Devono essere impostati scenario, parzializzazioni, ordinamento e schema informazioni; si ottiene un report come il seguente, che può essere usato anche come worklist per la risorsa : 

![P5_02_16](http://localhost:3000/immagini/MBDOC_OPE-P5PADC/P5_02_16.png)
# Esecuzione PDC
L'esecuzione della PDC è sostanzialmente il tracciamento dello spostamento dei contenitori all'interno dell'officina sui vari centri di lavoro che eseguono il ciclo di produzione.

>N.B. :  Vengono tracciati solo punti cardine inseriti nel ciclo logistico attraverso l'attribuzione di ubicazioni pre post macchina.
Tutte le attività possono essere eseguite e monitorate attraverso il controllo della Sintesi della Produzione a Disponibilità Chiamata.

## Sintesi Produzione a Disponibilità Chiamata
Dal formato principale, inserito il codice materiale, si possono selezionare : 
1. **Funzioni Articolo**    -->    viene presentata la finestra delle funzioni per articolo (la gestione è spiegata nel documento di gestione anagrafico articolo).

![P5_02_22](http://localhost:3000/immagini/MBDOC_OPE-P5PADC/P5_02_22.png)
2. **Sintesi Magazzino/Articolo**    -->    viene presentata l'interrogazione sintesi magazzino articolo (la gestione è spiegata nel documento di gestione materiali).

![P5_02_12](http://localhost:3000/immagini/MBDOC_OPE-P5PADC/P5_02_12.png)
3. **Funzioni su risorse**
Le funzioni su risorse sono quelle utilizzate principalmente per la gestione delle attività dell'avanzamento PDC.


Le funzioni sono : 
1. **Impostazioni** (si possono vedere e gestire i parametri generali PDC);

![P5_02_08](http://localhost:3000/immagini/MBDOC_OPE-P5PADC/P5_02_08.png)
2. **Presentazione domanda**    -->    viene lanciata l'analisi disponibilità per l'articolo in input usando il gruppo fonte della domanda definito nelle impostazioni (nell'esempio PDC);


3. **Struttura logistica**    -->    presenta la videata per la gestione del ciclo logistico : 

![P5_02_19](http://localhost:3000/immagini/MBDOC_OPE-P5PADC/P5_02_19.png)
4. **Situazione attuale**    -->    presenta, sulla struttura del ciclo logistico, lo status dei contenitori presenti nelle varie ubicazioni : 

![P5_02_20](http://localhost:3000/immagini/MBDOC_OPE-P5PADC/P5_02_20.png)
5. **Prospetto esecutivo**    -->    per l'articolo in input presenta tutti i contenitori in corso nelle varie ubicazioni del ciclo logistico e tutti i contenitori pianificati in partenza all'inizio del ciclo.

>N.B. :  I contenitori pianificati hanno prefisso contenitore pianificato come stabilito nelle impostazioni generali (nell'esempio X) e numerazione progressiva.

![P5_02_21](http://localhost:3000/immagini/MBDOC_OPE-P5PADC/P5_02_21.png)
Su ogni contenitore sono possibili le seguenti azioni : 
 * Accorpamento contenitore (si sommano le quantità di uno o più contenitori in uno solo);
 * Annullamento contenitori, per cancellare il contenitore;
 * Blocco contenitori, per bloccare l'avanzamento del contenitore;
 * Creazione contenitore (viene creato un contenitore effettivo partendo da un contenitore pianificato; l'azione scarica il materiale componente utilizzando la causale di prelievo presa dalle impostazioni generali);
 * Gestione note, per inserire o visualizzare note libere per contenitore;
 * Riempimento contenitore, per dichiarare la quantità prodotta dalla macchina;
 * Annullamento dichiarazioni, per stornare una dichiarazione precedente
 * Riempimento + Scarti, per dichiarare la quantità prodotta e quella scartata dalla macchina;
 * Sblocco contenitori, precedentemente bloccati;
 * Spostamenti + Scarti, per spostare da una ubicazione macchina all'ubicazione successiva e dichiarare contemporaneamente gli scarti;
 * Spostamenti, per spostare da una ubicazione macchina all'ubicazione successiva;
 * Stampa CDI PDC, per stampare l'etichetta del contenitore;
 * Suddivisione contenitore, per suddividere il contenitore in altri di quantità inferiore;
 * Versamento a magazzino, per versare il contenitore a magazzino;
 * Versamento a scarto.

6. **Impegni risorse in corso**    -->    per l'articolo in input visualizza gli impegni risorse derivati dai contenitori in corso di produzione.

![P5_02_16](http://localhost:3000/immagini/MBDOC_OPE-P5PADC/P5_02_16.png)
## Attività con Radio/Frequenza
La quasi totalità delle azioni eseguibili sui contenitori dal prospetto esecutivo sono anche possibili via Radio / Frequenza.
Di seguito sono elencate le attività possibili : 

![P5_02_23](http://localhost:3000/immagini/MBDOC_OPE-P5PADC/P5_02_23.png)
![P5_02_24](http://localhost:3000/immagini/MBDOC_OPE-P5PADC/P5_02_24.png)