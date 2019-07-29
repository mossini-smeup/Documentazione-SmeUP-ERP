# Implementazioni e installazione
## Archivi
  * **P5TEOP0F**
 ** E' stata introdotta la nuova quantità K§QT05. Rappresenta la quantità totale dei contenitori dell'ordine. Quantità pianificata e giacenza.
 ** E' stato introdotto il flag K§FL05. Identifica il tipo di ordine MFP
 * **GMCOLL0F**
 ** Ogni contenitore è legato ad un ordine di produzione.
 ** Sono state introdotte le quantità Z§QTAO e Z§QTAC. Rappresentano la quantità pianificata e riempita del contenitore.
 ** Sono stati introdotti i flag : 
 *** Z§FLG3 :  tipo contenitore MFP
 *** Z§FLG4 :  Saldo pianificato
 *** Z§FLG5 :  Contenitore pieno
 *** Z§FLG6 :  Contenitore scarti

## Tabelle
  * **P5M**; Nuova tabella che gestisce le diverse tipologie di avanzamento MFP
  * **P5H**; Nuova tabella che gestisce le diverse azioni di avanzamento MFP
  * **P51**; Aggiunto il numeratore MF
  * **P5T**; Aggiunto la tipologia di avanamento MFP
  * **GMF**; Gestita la nuova chiave collo in giacenza
  * **GMU**; Gestione campo tipo ubicazione MFP
  * **GM*SQ**; Aggiunta la chiave di giacenza collo

## Procedura di installazione
### Menù
Nel menù Y1 sono presenti le voci principali degli oggetti conivolti nel processo MFP

### OAV - Risorse RI
 * Creare OAV Ubicazione Ante
 ** Tipo oggetto base - RI
 ** Codice attributo - J/012
 ** Descrizione attr. - Ubicazione Ante
 ** Tipo attributo - UB
 ** Programma di calcolo - B£OA_RI
 * Creare OAV Ubicazione Post
 ** Tipo oggetto base - RI
 ** Codice attributo - J/013
 ** Descrizione attr. - Ubicazione Post
 ** Tipo attributo - UB
 ** Programma di calcolo - B£OA_RI

**Eseguire TSTOAV con funzione/metodo GES/01**
 :  : INI Eseguire TSTOAV con funzione/metodo GES/01
 :  : CMD CALL PGM(TSTOAV)
 :  : FIN

### Controllo tabelle
Inserire o modificare le definizioni delle seguenti tabelle
 * P5M, P5H, P51, P5T, GMF, GMU

**Gestione definizioni tabelle**
 :  : INI Gestione definizioni tabelle
 :  : CMD UP FTB
 :  : FIN

**Scandire le seguenti tabelle, controllandone la completezza**
**Creare numeratore MFP**
 :  : DEC T(ST) K(CRNP5)
 :  : INI Creare numeratore MFP
 :  : CMD CALL PGM(B£AR16) PARM('02' 'CRN' 'P5' '')
 :  : FIN
**Compilare il campo "Numeratore MFP"**
 :  : DEC T(ST) K(P51)
 :  : INI Compilare il campo "Numeratore MFP"
 :  : CMD CALL PGM(B£AR16) PARM('02' 'P51' '' '')
 :  : FIN
**Nuovo elemento "C=Collo"**
 :  : DEC T(ST) K(GM*SQ)
 :  : INI Nuovo elemento "C=Collo"
 :  : CMD CALL PGM(B£AR16) PARM('02' 'GM*' 'SQ' '')
 :  : FIN
**Creare aree :  WIP lavorazione, WIP C/lavoro terzista**
 :  : DEC T(ST) K(GMR)
 :  : INI Creare aree :  WIP lavorazione, WIP C/lavoro terzista
 :  : CMD CALL PGM(B£AR16) PARM('02' 'GMR' '' '')
 :  : FIN
**Creare tipi giacenza**
 :  : DEC T(ST) K(GMQ)
 * Tipi giacenza
 ** WIP lavorazione (Ubicazione, Fase, collo)
 ** WIP C/Lavoro Terzista (Terzista, Fase, Collo)
 :  : INI Creare tipi giacenza
 :  : CMD CALL PGM(B£AR16) PARM('02' 'GMQ' '' '')
 :  : FIN
**Creare forme di presentazione**
 :  : DEC T(ST) K(GMF)
 * Forme di presentazione magazzino
 ** WIP interno. Chiavi :  C/M/A/R/T/X/Y, e fissare area e tipo giacenza dove X è l'ubicazione e Y la fase
 ** WIP C/Lavoro Terzista. Chiavi :  C/M/A/R/T/X/Y, e fissare area e tipo giacenza dove X è il fornitore e Y la fase
 :  : INI Creare forme di presentazione
 :  : CMD CALL PGM(B£AR16) PARM('02' 'GMF' '' '')
 :  : FIN
**Creare causali scarico / carico delle nuove aree**
 :  : DEC T(ST) K(GMC)
 :  : INI Creare causali scarico / carico delle nuove aree
 :  : CMD CALL PGM(B£AR16) PARM('02' 'GMC' '' '')
 :  : FIN
**Nota**, nella causale di scarico del conto lavoro utilizzata nelle entrate MFP deve essere posto il programma di aggiustamento GMTR00X_£M.

**Creare casuale dichiarazione attività**
 :  : DEC T(ST) K(P5C)
 :  : INI Creare casuale dichiarazione attività
 :  : CMD CALL PGM(B£AR16) PARM('02' 'P5C' '' '')
 :  : FIN
**Creare numeratore contenitori MFP**
 :  : DEC T(ST) K(CRNGM)
 :  : INI Creare numeratore contenitori MFP
 :  : CMD CALL PGM(B£AR16) PARM('02' 'CRN' 'GM' '')
 :  : FIN
**Creare tipo contenitore MFP**
 :  : DEC T(ST) K(GMD)
 :  : INI Creare tipo contenitore MFP
 :  : CMD CALL PGM(B£AR16) PARM('02' 'GMD' '' '')
 :  : FIN
**Creare tipo ubicazione MFP**
 :  : DEC T(ST) K(GMU)
 :  : INI Creare tipo ubicazione MFP
 :  : CMD CALL PGM(B£AR16) PARM('02' 'GMU' '' '')
 :  : FIN
**Definire tipi MFP da utilizzare**
 :  : DEC T(ST) K(P5M)
 :  : INI Definire tipi MFP da utilizzare
 :  : CMD CALL PGM(B£AR16) PARM('02' 'P5M' '' '')
 :  : FIN
**Creare tipi ordine MFP**
 :  : DEC T(ST) K(P5T)
 :  : INI Creare tipi ordine MFP
 :  : CMD CALL PGM(B£AR16) PARM('02' 'P5T' '' '')
 :  : FIN
**Creare elemento "C07 = Tipo contenitore"**
 :  : DEC T(ST) K(B£N£P)
 :  : INI Creare elemento "C07 = Tipo contenitore"
 :  : CMD CALL PGM(B£AR16) PARM('02' 'B£N' '£P' '')
 :  : FIN
**Creare azioni MFP**
 :  : DEC T(ST) K(P5H)
 :  : INI Creare azioni MFP
 :  : CMD CALL PGM(B£AR16) PARM('02' 'P5H' '' '')
 :  : FIN
**Creare Azioni Radiofrequenza MFP**
 :  : DEC T(ST) K(B§J)
 :  : INI Creare Radiofrequenza MFP
 :  : CMD CALL PGM(B£AR16) PARM('02' 'B§J' '' '')
 :  : FIN

### Azioni manuali su ordine produzione
Negli ordini di produzione si devono aggiungere delle funzioni oggetto (F10) ad attivazione manuale (Tipo A-ORxxx) per l'analisi e il controllo degli ordinini MFP : 
 :  : DEC T(ST) K(B£JOR)
 :  : INI Creare le seguenti azioni sull'ordine
 :  : CMD CALL PGM(B£AR16) PARM('02' 'B£J' 'OR' '')
 :  : FIN

**Presentazione quadro MFP**
![P5PMFP_48](http://localhost:3000/immagini/P5PMFP_011/P5PMFP_48.png)
**Rifasa Quantità ordinata/contenitore**
![P5PMFP_49](http://localhost:3000/immagini/P5PMFP_011/P5PMFP_49.png)
**Gestione gruppi MFP**
![P5PMFP_50](http://localhost:3000/immagini/P5PMFP_011/P5PMFP_50.png)
### Tabelle conto lavoro
**Creare tipo impegno per scarico MFP esterno**
 :  : DEC T(ST) K(P5I)
 :  : INI Creare tipo impegno per scarico MFP esterno
 :  : CMD CALL PGM(B£AR16) PARM('02' 'P5I' '' '')
 :  : FIN
**Creare parametro conto lavoro MFP**
 :  : DEC T(ST) K(V5L)
 :  : INI Creare parametro conto lavoro MFP
 :  : CMD CALL PGM(B£AR16) PARM('02' 'V5L' '' '')
 :  : FIN
**Gestione tipi riga documenti**
 :  : DEC T(ST) K(V5BDP)
 *  Creare tipo riga uscita MFP
 * Creare tipo riga entrata MFP con parametro conto lavoro
 :  : INI Gestione tipi riga
 :  : CMD CALL PGM(B£AR16) PARM('02' 'V5B' 'DP' '')
 :  : FIN

## Azioni flussi conto lavoro
 Di seguito alcuni esempi di flussi utilizzabili per l'invio in conto lavoro ed il successivo rientro.

### Flusso CP501 - Invio in conto lavoro con Radio/Frequenza
![P5PMFP_24](http://localhost:3000/immagini/P5PMFP_011/P5PMFP_24.png)Questo flusso prevede che i contenitori da inviare in conto lavoro siano stati spostati nell'ubicazione ante del CDL terzista, attraverso il terminale R/F si crea la testata documento relativa al terzista, quindi si legge il bar-code dei vari contenitori, il sistema esegue i controlli previsti, quando si dichiara la fine delle letture il flusso propone la situazione riassuntiva che, se confermata, crea le righe del documento. Per completare il processo è previsto un successivo flusso da terminale con il quale si riprende il documento appena creato e si stampa il DDT.

**J0005    Crea testata (R/F)**
La funzione viene eseguita dal programma V5AT11E che è stato implementato in modo da uscire in formato R/F se attivo il flag opportuno : 
![P5PMFP_25](http://localhost:3000/immagini/P5PMFP_011/P5PMFP_25.png)
**J0010    Righe in file lavoro (R/F)**
Programma V5AT51A con le seguenti parametrizzazioni
![P5PMFP_26](http://localhost:3000/immagini/P5PMFP_011/P5PMFP_26.png)Il programma legge il codice contenitore, controlla che la sua giacenza sia congruente con la causale di scarico presente nel tipo riga e con l'ubicazione, inoltre controlla che il fornitore associato alla risorsa della fase successiva di lavoro sia lo stesso della testata.
Superati i controlli viene inserita una riga in un file di lavoro, con il comando funzione F8 è sempre possibile scorrere il contenuto di questo file.
Alla fine delle letture con F12 si procede al successivo passo di flusso.

**J0050    Crea righe V5 da file lavoro**
Programma V5AT51Z con le seguenti parametrizzazioni
![P5PMFP_27](http://localhost:3000/immagini/P5PMFP_011/P5PMFP_27.png)Il programma presenta le informazioni riassuntive di testata e permette di forzare alcuni dati, es. numero e peso colli, dopo la conferma trasferisce le righe dal file di lavoro al documento.

### Flusso CP502 - Stampa e collega bolla da documento esistente
![P5PMFP_28](http://localhost:3000/immagini/P5PMFP_011/P5PMFP_28.png)Questo flusso completa il processo di invio riprendendo il documento appena creato e stampando il DDT, è possibile inserire nel flusso un passo che, in automatico crea un ordine di conto lavoro speculare al DDT.

**K0005    Selezione documento esistente**
Programma V5AT11E con le seguenti parametrizzazioni : 
![P5PMFP_29](http://localhost:3000/immagini/P5PMFP_011/P5PMFP_29.png)
**K0010    Modifica testata**
Programma V5DO15X con le seguenti parametrizzazioni
![P5PMFP_30](http://localhost:3000/immagini/P5PMFP_011/P5PMFP_30.png)
**K0100    Stampa bolla**
Programma V5BOFA con le seguenti parametrizzazioni
![P5PMFP_31](http://localhost:3000/immagini/P5PMFP_011/P5PMFP_31.png)
**K0800    Crea ordine conto lavoro**
Programma V5AT52A con le seguenti parametrizzazioni
![P5PMFP_32](http://localhost:3000/immagini/P5PMFP_011/P5PMFP_32.png)Il programma crea un documento, copia della bolla con tipo documento, modello documento e tipo riga presi dai "Parametri aggiuntivi".

**K0900    Collegamento**
Programma V5DO15X con le seguenti parametrizzazioni
![P5PMFP_33](http://localhost:3000/immagini/P5PMFP_011/P5PMFP_33.png)
### Flusso CP505 - Invio in conto lavoro MFP
![P5PMFP_34](http://localhost:3000/immagini/P5PMFP_011/P5PMFP_34.png)Questo flusso riprende le funzionalità dei due flussi precedenti con la differenza che viene eseguito interamente a terminale (No R/F).

**I0005    Creazione testata**
Come azione J0005 senza il flag di radiofrequenza.

**I0010    Scrittura righe documento**
Programma V5MFP01 con le seguenti parametrizzazioni : 
![P5PMFP_35](http://localhost:3000/immagini/P5PMFP_011/P5PMFP_35.png)Il programma ha un comportamento analogo al PGM V5AT51A con la differenza che alla fine del processo vengono scritte direttamente le righe del documento V5.

**I0050    Modifica testata**
Come azione K0050

**I0100    Stampa bolla**
Come azione K0100

**I0800    Crea ordine conto lavoro**
Come azione K0800

**I0900    Collegamento**
Come azione K0900

### Flusso CP506 - Entrata merci da conto lavoro con Radio/Frequenza
![P5PMFP_36](http://localhost:3000/immagini/P5PMFP_011/P5PMFP_36.png)Questo flusso prevede di eseguire l'entrata merci attraverso la lettura del bar-code dei contenitori, a titolo di esempio sono stati inseriti due passi di flusso, che normalmente sono alternativi : 
 * __lettura di contenitori bar-code "estern" (non presenti nel file colli)__, si ipotizza di avere dei contenitori provenienti dal fornitore con etichette proprie, non fornite da noi,  in cui il codice contenitore comprende codice fornitore + codice articolo + progressivo, alla fine del processo il flusso crea un collo MFP a cui associa come alias il bar-code esterno
 * __lettura di contenitori bar-code MFP__, si ipotizza di avere di ritorno dal fornitore gli stessi contenitori usciti, in questo caso i colli sono di tipo MFP e sono sottoposti ai normali controlli MFP.

Per completare il processo è previsto un successivo flusso da terminale con il quale si riprende il documento appena creato e si conferma l'entrata merci.

**L0005    Crea testata (R/F)**
La funzione viene eseguita da programma V5AT11E con le seguenti parametrizzazioni
![P5PMFP_37](http://localhost:3000/immagini/P5PMFP_011/P5PMFP_37.png)
**L0010    Work righe colli MFP (Alias)**
Programma V5AT51B con le seguenti parametrizzazioni
![P5PMFP_38](http://localhost:3000/immagini/P5PMFP_011/P5PMFP_38.png)Il programma legge ed interpreta il bar-code contenitore esterno scrivendo una riga nel file di lavoro con i dati del contenitore più i dati presi dal "Parametri aggiuntivi" dell'azione

**L0011    Work righe colli MFP (MFP)**
Programma V5AT51C con le seguenti parametrizzazioni
![P5PMFP_39](http://localhost:3000/immagini/P5PMFP_011/P5PMFP_39.png)Come il precedente con in più il controllo di validità del contenitore MFP.

**L0100    Crea righe V5 da file work**
Come azione J0050

### Flusso CP507 - Completamento entrata merci da Radio Frequenza
![P5PMFP_40](http://localhost:3000/immagini/P5PMFP_011/P5PMFP_40.png)Questo flusso completa il processo di ricezione riprendendo il documento appena creato, completando le righe delle fasi esterne, ove manchino ed eseguendo infine la "distribuzione" delle quantità entrate con riferimento alle giacenze esterne c/o terzista, agli ordini di conto lavoro e agli ordini di produzione MFP.

**M0005   Selezione documento esistente**
Come azione K0005

**M0050   Modifica testata**
Come azione K0010

**M0070   Controllo operazione**
Programma V5MFP02Z con le seguenti parametrizzazioni
![P5PMFP_41](http://localhost:3000/immagini/P5PMFP_011/P5PMFP_41.png)Il programma, seleziona le righe del documento dello stesso tipo inserito nei "Parametri aggiuntivi" con fase bianca, ricerca ordini (stesso tipo documento, tipo riga dei parametri aggiuntivi) assegnati al fornitore del documento per lo stesso articolo e, se trova una sola fase la forza sulle righe documento in maniera "cieca", altrimenti presenta la lista delle righe da sistemare manualmente.
Questo passo di flusso può essere utile quando le entrate merci da radio/frequenza sono di tipo eterogeneo quindi possono entrare sia forniture normali che lavorazioni extraciclo che riparazioni, bisogna prevedere tipi riga diversi ed un programma di controllo operazione per ciascuno di questi tipi riga.

**M0090   Distribuzione righe documento**
Programma V5MFP02A con le seguenti parametrizzazioni
![P5PMFP_42](http://localhost:3000/immagini/P5PMFP_011/P5PMFP_42.png)Il programma può trattare nello stesso documento tipologie diverse di fornitura, per questo deve avere delle associazioni tra i tipi riga scritti in precedenza con il flusso R/F e i controlli e le righe che dovrà eseguire/generare nella fase di distribuzione, questi abbinamenti vengono impostati attraverso altri elementi di tabella B£J presenti in un proprio sottosettore; nei "Parametri aggiuntivi" di questo passo è indicato il sottosettore e gli elementi di B£J da utilizzare internamente all'elaborazione, vedi esempio seguente : 
![P5PMFP_43](http://localhost:3000/immagini/P5PMFP_011/P5PMFP_43.png)
**M0900   Collegamento documento**
Come azione K0900

### Flusso CP509 - Entrata merci MFP
![P5PMFP_44](http://localhost:3000/immagini/P5PMFP_011/P5PMFP_44.png)Questo flusso prevede l'esecuzione dell'entrata merci da terminale. I primi due passi del flusso sono quelli tipici dei flussi entrata merci da ordine, i due passi successivi sono quelli tipici MFP di controllo operazione e distribuzione con creazione contenitori MFP.

**N0005   Crea testata documento **
Programma V5AT11E con le seguenti parametrizzazioni
![P5PMFP_45](http://localhost:3000/immagini/P5PMFP_011/P5PMFP_45.png)
**N0010   Seleziona righe**
Programma V5AT15G con le seguenti parametrizzazioni
![P5PMFP_46](http://localhost:3000/immagini/P5PMFP_011/P5PMFP_46.png)da notare che, se i bar-code dei contenitori sono esterni, deve essere associato un programma di aggiustamento che chiede il codice bar-code per ogni riga inserita

**N0070   Controllo operazione**
Come azione M0070

**N0090   Distribuzione righe documento**
Come azione M0090

**N0900   Collegamento documento**
Come azione M0900

### Azioni impostazione
**Gestione azioni flussi entrata/uscita**
 :  : INI Gestione azioni flussi entrata/uscita
 :  : CMD CALL PGM(B£AR16) PARM('02' 'B£J' 'CP' '')
 :  : FIN
**Gestione gruppi azioni flussi**
 :  : INI Gestione gruppi azioni flussi
 :  : CMD CALL PGM(B£AR16) PARM('02' 'B£H' '' '')
 :  : FIN
**Gestione attività ciclo passivo**
 :  : INI Gestione attività ciclo passivo
 :  : CMD CALL PGM(B£AR16) PARM('02' 'V5G' 'CP' '')
 :  : FIN

### Programma aggiustamento GMTR00X_£M sulla causale di scarico della bolla di rientro
Nella gestione MFP sia le giacenze esterne che quelle interne sono per contenitore, mentre nelle righe documenti V5 esiste un solo campo collo, il programma di aggiustamento in questione reperisce il secondo collo (di scarico :  giacenza esterna) dal parametro implicito dove è stato inserito dal programma di "distribuzione" premettendo di eseguire il movimento di scarico giacenza corretto.
Quindi la causale di scarico del tipo riga entrata merci deve avere il programma di aggiustamento GMTR00X_£M
**Gestione causali movimentazione**
 :  : INI Gestione causali movimentazione
 :  : CMD CALL PGM(B£AR16) PARM('02' 'GMC' '' '')
 :  : FIN

### Parametri logistici da controllare
**Per creazione contenitori - Parametri logistici £P3 1P3 2P3**
 :  : INI Parametri logistici  xP3
 :  : CMD CALL PGM(C£CR01G) PARM('£P3')
 :  : CMD CALL PGM(C£CR01G) PARM('1P3')
 :  : CMD CALL PGM(C£CR01G) PARM('2P3')
 :  : FIN
**Per versamento magazzino - Parametri logistici £P2 1P2 2P2**
 :  : INI Parametri logistici  xP2
 :  : CMD CALL PGM(C£CR01G) PARM('£P2')
 :  : CMD CALL PGM(C£CR01G) PARM('1P2')
 :  : CMD CALL PGM(C£CR01G) PARM('2P2')
 :  : FIN
