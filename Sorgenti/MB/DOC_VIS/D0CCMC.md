# Visione Costi Multicontesto
## Panoramica Costi Multicontesto
Con la versione V3R2 in alternativa, o anche in coesistenza con il modulo D0BASE è possibile attivare il nuovo modulo D0CCMC per il calcolo del costo riferito non solo all'oggetto articolo ma anche ad altri oggetti SmeUP chiamati, con la terminologia tipica di questa applicazione "contesti".

Ci si propone di realizzare il calcolo del costo per i seguenti contesti : 
* Articoli (AR)
* Righe documento (DR)
* Ordini di produzione (OR)
* Lotti (LO) (consuntivo in fase di sviluppo)
* Commesse (CM) (consuntivo in fase di analisi)

Sono previsti : 
* Calcolo costo standard
* Calcolo costo medio (per articolo)
* Calcolo costo preventivo
* Calcolo costo consuntivo (vedi contesti)

## Funzionalità fornite : 
* **Documentazione del calcolo** :  possibilità di memorizzare la "documentazione" del calcolo cioè tutti gli elementi, le regole, i valori che hanno determinato il calcolo. La documentazione può essere interrogata attraverso una scheda specifica. La documentazione può essere anche stampata.
* **Gestione degli errori** :  gli errori intercettati durante il calcolo dei costi vengono registrati in un archivio da cui sono interrogabili, ad ogni errore è associato un codice ed un grado di severità. Si possono identificare e risolvere con priorità gli errori che impattano il numero maggiore di oggetti (es. nel calcolo costi articoli l'errore su un componente impatta tutta la catena in implosione della distinta base, quindi la soluzione di un singolo errore può sistemare N. articoli). Possono essere definiti come errori anche differenze, nel costo calcolato, superiori ad una certa percentuale del valore calcolato nell'elaborazione precedente. Gli errori sono codificati nella tabella D0E dove all'errore viene anche associato un grado di severità (es. errore di warning o vincolante)
* **Politiche di calcolo costi proprie**, indipendenti dalle politiche di pianificazione materiali, con possibilità di risalita per default. Sono possibili anche politiche miste :  il calcolo costi tiene in considerazione il mix dovuto alla percentuale di utlilizzo di ciascuna politica
* **Distribuzione costi di materiale**, su diversi elementi di costo in base ad un attributo dell'articolo, così è possibile, ad esempio, identificare nel costo del prodotto le quote di costo dovute alla componente alluminio o ottone distinte da quelle relative alle minuterie metalliche di acquisto
* **Impostazioni di calcolo sotto autorizzazione** :  l'utente finale che si occupa di lanciare le elaborazioni, se non autorizzato, non è in condizione di cambiare le impostazioni predefinite
* Utilizzo nel calcolo del costo medio di "**Costi forzati**" per articoli che non sono movimentati a magazzino e per i quali non viene registrata la giacenza. Costi standard anche per movimenti quali rettifiche inventariali o smontaggi diversi da quelli associati a documenti del ciclo esterno o di produzione
* **Tipi costo di conto / lavoro**, distinti tra C/L Pieno e C/L di fase
* **Possibilità di definire il tipo costo dei "semilavorati" distinto dal tipo costo di calcolo,  la sua utilità appare evidente considerando ad esempio il costo di un oridne di produzione :  il contesto dell'ordine (OR) non può essere uguale al contesto dei suoi componenti che abbiano politica di produzione (AR) e di conseguenza devono essere distinti i relativi tipi costo
* **Costo di fase anche per oggetto "Operazione" (OP)** :  nel calcolo normale del costo di una fase per il contesto articolo si usa l'oggetto "Fase" (FA) mentre per il contesto ordine di produzione si usa l'oggetto "Operazione di ordine" (OO), adesso c'è la possibilità di inpostare il costo per operazione
* Possibilità di memorizzazione del costo oggetto anche in presenza di **errori di warning**
* **Flussi di elaborazioni pre / post**, associati al calcolo costi di massa
* **Confronto tipi costo**, tra tipi costo diversi o tra periodi diversi dello stesso tipo costo con possibilità di evidenziare differenze superiori ad un valore o ad una percentuale data
* **Impostazione oggetto titolare del costo di lavorazione interna** :  centro di costo, risorsa del ciclo, risorsa del ciclo con risalita al centro di costo
* **Tool di customizzazione**, che verifica le tabelle di impostazione e la loro congruenza, il tool permette anche la creazione diretta di queste tabelle e la compilazione delle "MDV" di impostazione dei programmi di calcolo

## Calcolo costo standard
Nella sua sostanza il calcolo del costo standard richiama quanto già fornito dal modulo D0BASE a cui si rimanda per riferimenti. Nel modulo D0CCMC sono state ampliate le impostazioni del calcolo ed introdotti dei miglioramenti operativi.

### Impostazioni del calcolo
* tipo costo / tema dove memorizzare il costo articolo
* tipo costo / tema dove memorizzare il costo alla fase
* tipo di calcolo (tutti, solo mancanti, solo presenti)
* tipo costo per lettura aliquote orarie
* tipo costo per lettura conto lavoro pieno
* tipo costo per lettura conto lavoro di fase
* tipo costo per lettura acquisto
* struttura elementi di costo
* regole attribuzione ricariche
* regole definizione errori
* metodo di memorizzazione costi (solo senza errori, solo se con valore, tutti, nessuno, nessuno con cancellazione costi precedenti)
* metodo memorizzazione documentazione del calcolo
* flussi pre / post elaborazione
* filtro articoli da estrarre (parzializzazioni interne / esterne)
* aggiunta estrazione articoli in implosione o in esplosione

### Differenze rispetto alla versione base D0 (V2R2)
* **risalita al livello per il costo materiali**, se impostata in tabella D01, viene eseguita SOLO se il componente ha un costo totalmente di acquisto, se invece la politica del componente è mista il suo costo resta ai livelli inferiori
* **memorizzazione costi "corretti"**, se viene richiesta la memorizzazione dei costi solo se corretti "C" ed è impostata l'esplosione distinta in costo non viene memorizzato anche se l'errore è sul costo di uno dei componenti.
* **pre-cancellazione oggetti sottoposti al ricalcolo costi**, con la versione D0BASE veniva calcolato il costo di un articolo e, se corretto, tale costo veniva memorizzato, mentre se era in errore non veniva memorizzato, con il rischo di lasciare sull'archivio un costo precedentemente calcolato.
In questa versione, prima del calcolo vengono cancellati tutti i costi, quindi quelli che si ritrovano a fine elaborazione sono solo quelli corretti, compatibilmente con i parametri impostati nel calcolo
* **possibilità di memorizzare costi unitari o costi totali**, nel secondo caso tra i vari elementi di costo (tabella IGI) viene memeorizzato anche il campo quantità a cui il costo totale è riferito



## Calcolo costo medio
* opera nel contesto "articolo"
* determina la media ponderata delle componenti di costo aventi origini diverse :  produzione; acquisto; conto/lavoro
* considera i movimenti di magazzino relativi a : 
** ordini di produzione :   valorizzazione ciclo e distinta (effettivi/previsti per ordini chiusi/in corso); valorizzazione puntuale delle lavorazioni esterne
** bolle di acquisto
** bolle di conto lavoro :  valorizzazione distinta (effettiva/prevista per ordini chiusi/in corso); valorizzazione lavorazione esterna
* può considerare costi standard per rettifiche inventariali positive
* può considerare costi standard per articoli componenti provenienti da smontaggio
* può considerare costi standard per articoli non movimentati a magazzino
* può eseguire una media ponderata verso valore e quantità delle rimanenze del periodo precedente
* può utilizzare come periodo l'anno o il mese

### Costo medio annuale
Calcolato annualmente. Può essere lanciato in due modalità : 
* **con ponderazione verso il periodo precedente**, in questo caso si tratta di un vero costo medio ponderato che può essere utilizzato per valorizzare l'intero magazzino fiscale
* **senza ponderazione**, in questo caso è solo il costo medio ponderato del periodo e a fine anno può essere utilizzato per valorizzare la fascia lifo dell'anno

### Costo medio year to date
Simile al precedente con la differenza che viene calcolato mensilmente  e si incrementa mano mano che passano i mesi, i movimenti considerati sono quelli da inizio anno, anche in questo caso possiamo avere o meno la ponderazione con le rimanenze dell'anno precedente.

### Costo medio del periodo
Genericamente è mensile e considera solo i movimenti del periodo, eventualmente può essere ponderato con le rimanenze del periodo precedente.

## Set'n play tipo costo
Con questo modulo viene fornito uno strumento di set'n play del tipo costo, delle tabelle collegate e delle impostazioni di lancio elaborazioni (MDV formati video di lancio programmi).
Data una tipologia di calcolo (es. costo medio annuale) il programma controlla la presenza delle tabelle e delle MDV dei programmi, segnala  le incongruenze ed eventualmente crea/modifica le impostazioni mancanti.
