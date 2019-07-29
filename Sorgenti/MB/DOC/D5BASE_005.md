# Struttura di Delt.up
![D5BASE_01](http://localhost:3000/immagini/D5BASE_005/D5BASE_01.png)
# Analisi degli obiettivi del Controllo di gestione
L'obiettivo di Delt.UP è monitorare i processi aziendali per rilevare scostamenti rispetto ad un obiettivo predefinito.

## Definizione struttura in Delt.UP
Innanzi tutto è necessario chiarire la struttura : 
 * Definire tutte le entità interne che devono essere monitorate
 ** Azienda / Sede / Unità produttiva
 ** Centri di responsabilità
 ** Centri di Costo
 ** Reparti
 ** Risorse
 ** Prodotti chiave tecnica
 * Definire tutte le entità esterne che devono essere monitorate
 ** Aree geografiche / commerciali
 ** Settori merceologici
 ** Clienti
 ** Brand
 ** Fornitori
 ** Prodotti chiave commerciale.
 * Definire i dati da analizzare : 
 ** Budget
 ** Esercizi contabili / Periodi

## Alimentare Delt.UP
Nel controllo di gestione ho tutta una serie di elementi che mi permettono di alimentare Delt.UP, questi prendono il nome di "sistemi conferenti".
Ad esempio in Contabilità Analitica i tipici elementi caratterizzanti sono : 
 * Centro di Costo
 * Voce di spesa

Abbiamo a disposizione 3 Nature e 3 Destinazioni quali entità di analisi.

Sme.UP definisce queste sei entità come oggetti (Tipo, Parametro, Cod. Oggetto).

### Verificare struttura dei sistemi conferenti
I programmi conferenti controllano che gli oggetti definiti in input siano congruenti con quelli in output, esistono in Smeup casi di omonimia degli oggetti (es. il Cliente è sia l'oggetto CL che CN/CLI, la Voce di spesa può essere sia VS che TAV5D, ecc...) si suggerisce quindi di utilizzare le denominazioni consigliate : 


|  Nam="Tabella Oggetti consigliati" |
| 
| .COL LunAut="1" A="C" |
| ---|----|
| 
| .COL LunAut="1" A="C" |
| 
| .COL LunAut="1" A="C" |
|  _2_Natura o destinazione | _2_Oggetti consigliati | _2_Oggetti utilizzati ma sconsigliati |
|  Voce di Spesa | VS | TAD5V |
|  Centro di Costo | CC | TAD5C |
|  Cliente | CNCLI | CL |
|  Fornitore | CNFOR | FO |
|  Commessa | CM |
|  Articolo | AR | |
|  Conto Contabile | CO | TAC5B |
| 


Il codice oggetto deve essere coerente con il parametro, per fare questa verifica : 
 * Verificare la struttura della contabilità analitica se c'è Sme.UP
 ** Confrontare le B£G inserite, rispetto ai vari oggetti.
 *** D5C
 *** AR
 *** D5V
 *** Etc.
 * Se l'analitica non è Sme.UP si devono creare delle EXIT specifiche per alimentare il database scrivendo un programma, utilizzando in modo adeguato la /COPY D5A (Routine che si occupa di far confluire i dati nel nostro modello).
 * Nel caso in cui il sistema conferente non sia la Contabilità Analitica ma un altro tema del gestionale (esempio i documenti), la ripresa di tale dato è definita direttamente nel programma di ripresa (Vedi D5APV51 per i V5). Porre attenzione al caso in cui i centri di costo sono definiti come parametro = "CC" ed il nostro contesto è un TAD5C dovremo scrivere un programma di aggiustamento (D5APV51_x) che ne cambia il contesto.
 * E' estremamente consigliato definire i contesti "Consigliati" (visti nello schema precedente) al fine di non utilizzare continuamente programmi di aggiustamento.

# Definire i Modelli di Delt.UP
## Definizione dei contesti (tabella D5S)
La tabella D5S è quella che mi permette questa definizione, l'elemento da utilizzare nella D5S è obbligatoriamente un oggetto di Sme.up per cui il sistema lo controlla nella tabella *CN/TT  dove l'elemento deve esistere, oppure devo crearmi un UFO (Oggetto definito dall'Utente)
![D5BASE_02](http://localhost:3000/immagini/D5BASE_005/D5BASE_02.png)Da notare che nella tabella viene definito il sottosettore da utilizzare per le definizioni dei temi (Tab. D5O).

### Creazione oggetto UFO
 :  : DEC T(MB) P(DOC) K(OG__D) L(1)

* Risulterà fondamentale capire quando è il caso di fare un UFO o usare delle chiavi aggiuntive in Delt.UP

![D5BASE_03](http://localhost:3000/immagini/D5BASE_005/D5BASE_03.png)![D5BASE_04](http://localhost:3000/immagini/D5BASE_005/D5BASE_04.png)
## Definizione dei valori (Tabella IGI_xx)
In questa tabella si assegna un significato ad ognuno dei 99 campi generici (solo quelli necessari) avendo le seguenti possibilità : 
 * Valori
 * Formule
 * Totali

Questa tabella prevede due riclassifiche per ogni valore (che devono essere presenti nella stessa tabella), e l'assegnazione della natura (solo per la gestione dei costi).
Il sottosettore di questa tabella sarà l'elemento che utilizzeremo nella definizione della tabella D5O.
![D5BASE_05](http://localhost:3000/immagini/D5BASE_005/D5BASE_05.png)
Nel campo "controllo" digitando una "_2_F" si può permettere, da parte dell'utente, la modifica del valore, anche dopo il popolamento automatico dell'elemento.

## Definizione del tema (tabella D5O_xx)
Il sottosettore della D5O dipende dal contesto (esempio "CC" = Centri di Costo).
![D5BASE_06](http://localhost:3000/immagini/D5BASE_005/D5BASE_06.png)
Associamo la tabella IGI al tema nel campo "S/S indici(se STD)".
I 3 oggetti saranno i valori che vedremo nel D5COSO (D$COD1, D$COD2, D$COD3).

In alternativa alla IGI, per definire i valori del tema si può utilizzare, al posto del "S/S indici(se STD)", il campo "Suf. Pgm. Spec. D5CO_XX" dove ci sono degli schemi standard.

## Struttura delle chiavi dei contesti (D5COSO)
![D5BASE_07](http://localhost:3000/immagini/D5BASE_005/D5BASE_07.png)
 * _2_D$TIPA è il contesto
 * _2_D$COD è il codice del contesto
 ** Se il contesto è il centro di costo il D$CODI è il Codice del centro di costo.
 * _2_D$TROT è il tema che contiene la definizione delle tre chiavi aggiuntive (D$COD1, D$COD2, D$COD3), del significato dei 99 campi valore di definizione del costo e della periodicità (D$DTVA, Anno, Periodo, Data) riferimento alla tabella PER.

# Popolamento dei modelli.
I dati posso essere caricati con vari metodi : 
 * Inserimento manuale
 * Alimentazione da sistemi conferenti
 ** alimentazione da sistemi Smeup
 ** alimentazione da altri sistemi

## Inserimento manuale
Decido di non passare tramite sistemi conferenti, posso procedere a inserire, anche parzialmente, il dato manualmente, o magari gestisco a mano le sole correzioni a dati provenienti dai sistemi conferenti.
E' sempre un flag della tabelle IGI che permette tale opzione, che vale per tutti i Temi a cui è associata quella tabella IGI stessa.

## Alimentazione da Sistemi conferenti
### Tabella B£H - Gruppi di Azioni
Con questa tabella si definirà il flusso di alimentazione
![D5BASE_08](http://localhost:3000/immagini/D5BASE_005/D5BASE_08.png)attraverso la definizione dei passi di alimentazione, Tabella B£J_xx, che prevede due modalità diverse di definizione in base al sistema origine che può essere Sme.UP o altro sistema.

## Alimentazione da Sistemi conferenti Sme.UP
### Tabella B£J_xx - Gruppi di azioni
In questa tabella si definiranno i passi e, oltre alle azioni del programma D5* si dovrà porre attenzione ai campi "Sottosettore Fonte" e "Codice Fonte".
![D5BASE_09](http://localhost:3000/immagini/D5BASE_005/D5BASE_09.png)![D5BASE_10](http://localhost:3000/immagini/D5BASE_005/D5BASE_10.png)![D5BASE_11](http://localhost:3000/immagini/D5BASE_005/D5BASE_11.png)
### Tabella D5R_xx - Ripresa da sistemi conferenti
Tabella che definirà le fonti di alimentazione del D5COSO dei sistemi conferenti.
![D5BASE_12](http://localhost:3000/immagini/D5BASE_005/D5BASE_12.png)In questa tabella andremo a definire : 
 * il prefisso di tutti i passi che andiamo a codificare nella tabella D5E_xx (vedi "MH")
 * Il contesto e il tema di destinazione (solo quando i passi della D5E vanno tutti ad alimentare lo steso contesto), se lo impostiamo qui ci leghiamo a quel tema/contesto senza poterci svincolare nemmeno nei programmi di aggiustamento.
 * Il segno transazione serve solo nella contabilità e nel magazzino : 
 ** Nella contabilità se metto : 
 *** _2_D = Dare Positivo Avere Negativo
 *** _2_A = Dare Negativo Avere Positivo
 *** _2_Blanks = Tutto positivo
 ** Nel magazzino se metto : 
 *** _2_E = Entrate Positive Uscite Negative
 *** _2_U = Entrate Negative Uscite Positive
 *** _2_Blanks = Tutto positivo

### Tabella D5E_xx - Passi di ripresa
La numerazione dei passi è usualmente definita con un prefisso impostato nella D5R + un progressivo, genericamente numerico, (comunque non ci sono vincoli).
Il sistema esegue al massimo 10 passi per ogni D5R, per cui è in grado di alimentare al massimo una schiera di 10 valori (schiera della DS-esterna _2_D5MOVI).
![D5BASE_13](http://localhost:3000/immagini/D5BASE_005/D5BASE_13.png)
 * Il contesto e il tema, se definiti nella D5R, possono essere "**".
 * Metodo det. Origine : 
 ** _2_*VAL, è riferito a uno dei 10 valori della DS D5MOVI (D£CN01...D£CN10), questo in relazione al valore caricato dal programma di alimentazione (_2_D5APMHE per contabilità analitica).
 ** _2_*QTA, fa riferimento al campo _2_D£QTMO della DS _2_D5MOVI (verificare sempre cosa fa il programma di alimentazione). In questo caso non serve il parametro in quanto c'è una sola quantità.
 * Metodo di destinazione
 ** _2_1             Numero indice diretto. Andrà diretto nel valore, specificato nel parametro, del _2_D5COSO, che corrisponde al campo _2_D$C0xx dove xx è il parametro, senza alcun controllo, anche se non definito nella tabella IGI.
 ** _2_2   *IND      Indice di un sottosettore, stessa logica del precedente ma viene controllata l'esistenza sulla tabella IGI e nella fase di compilazione mi chiede il sottosettore della relativa tabella IGI. Questo elemento si vedrà sicuramente quando interrogo il costo perché è un campo definito.
 ** _2_3   *VDS      Indice VDS da param. Oggetto. E' un parametro legato alla voce di spesa, ed andrà sul _2_D5COSO in base all'indice definito nel parametro stesso. Nei primi 3 caratteri ci va l'elemento della C£E, dalla 4 in poi il codice del parametro. Il codice che passa è quello della voce di spesa, per cui prenderà il parametro della voce di spesa e alimenterà il campo relativo del _2_D5COSO senza controllo di esistenza se il parametro non è associato alla tabella IGI di competenza. Meno Flessibile dell'opzione _2_*PA2, in quanto questo è riferito tassativamente alla voce di spesa.
 ** _2_4   *OAV      Attributo oggetto, ha la stessa funzionalità del _2_*VDS, solo che viene risolto da un OAV. Prerequisito che l'OAV ritorni un indice della tabella IGI riferita al tema in questione. Il limite dell' _2_*OAV è che l'oggetto dell'OAV deve essere una delle 4 chiavi del _2_D5COSO.
 ** _2_5   *PAR      Parametro oggetto contesto. Limitato ..... vedi *PA2
 ** _2_6   *PA2      Parametro oggetto. E' un parametro di uno dei 10 oggetti passati dalla DS _2_D5MOVI, che potrebbe non essere una chiave del _2_D5COSO, vedi esempio dell'assegnazione di un parametro al conto contabile (entità non in chiave nel _2_D5COSO genericamente), per determinare l'assegnazione del valore nel report per Centro di Costo. Parametro dalla C£E.
 ** _2_7   *CAT      Indice da categ.dell'oggetto, dipendente dalla tabella D5U, al posto di assegnare la destinazione tramite parametro direttamente collegato alla tabella IGI, lo si definisce tramite la categoria (sulla tabella D5U è evidenziato sottosettore tabella IGI con relativo indice).
 ** _2_8   *CA2      Indice da param.categoria ogg. Uguale a *CAT (in fase di sviuppo).
 ** _2_9   *CAO      Indice usando algoritmo D5M. Usa l'indice associato all'oggetto ritornato dall'OAV definito nella tabella D5M. Quindi posso dire, per esempio, che tutti i conti contabili con quell'attributo (campo o parametro), vanno a finire nell'indice assegnato a quel attributo e non direttamente sul conto. Un esempio :  associare un indice alle categorie contabili permette di far convogliare i valori di tutti i conti appartenenti a quella categoria su quell'indice.
 ** _2_10   *D5MOVI   Indice presente in D5MOVI. Questo modello serve quando si devono ribaltare dei costi e si vuole che vadano a finire nello stesso indice da cui sono partiti. Se vogliamo far convergere i valori su un altro indice devo gestire un programma di aggiustamento. Per i ribaltamenti si può vedere il programma _2_D5AP05B. Rispetto a questo programma, nel parametro di destinazione devo inserire il _2_valore 02, che è il valore corrispondente a dove è stato messo l'indice, sempre che non ci sia stato un programma di aggiustamento prima.
 * Il flag di conserva relazione mi permette di tenere la traccia del dettaglio dei dati origine (_2_D5RECO).
 * Il flag di pre-cancellazione serve per evitare di fare un'azione di cancellazione nel flusso. E' il caso di attivare questo flag solo nel primo passo delle D5E altrimenti puliamo i dati ad ogni passo.
Significativo segnalare che se si vuole pulire l'origine del dato ribaltato è sufficiente utilizzare un secondo passo della D5E che destina il "Valore 02" della _2_D5MOVI su contesto tema origine (tale valore infatti non è nient'altro che un valore di segno opposto a quello ribaltato).

Vedi seguente esempio : 
![D5BASE_14](http://localhost:3000/immagini/D5BASE_005/D5BASE_14.png)![D5BASE_15](http://localhost:3000/immagini/D5BASE_005/D5BASE_15.png)
# Alimentazione da altri Sistemi conferenti (no Sme.UP)
In questo caso abbiamo la necessità di creare dei programmi utente che utilizzino in modo opportuno la /COPY D5A.
Nella tabella B£J metterò il nome del mio programma utente.

# Algoritmi di validazione e/o caricamento - Tabella D5M_xx
La tabella D5M, in supporto alla tabella D5E, permette di risolvere i contesti/temi di _2_destinazione qualora ciò non sia possibile mediante la D5E.
![D5BASE_16](http://localhost:3000/immagini/D5BASE_005/D5BASE_16.png)
Il prerequisito è che l'elemento di tabella sia così codificato : 
 * _2_aaaaaaaaa n bytes - Elemento della tabella D5E (max 9 bytes)
 * _2_  1 byte - Underscore fisso
 * _2_XXYYY  5 bytes max - Contesto di arrivo

Il significato del metodo è il seguente : 
 * _2_1   *IND      Indice. Permette di utilizzare un indice di distribuzione definito nella tabella D5I.
 * _2_2   *INDOAV   Indice di un attributo. Stessa cosa di _2_*IND, ma l'oggetto contenuto nell'indice (Tabella D5I) e ritornato da un OAV di uno degli oggetti origine. Esempio :  se ho in input i dati contabili, se voglio riportarmi il collaboratore (e io non ho questo dato) devo risolvere questo codice dal codice fornitore.
 * _2_3   *INDDIN   Indice dinamico da OAV. Stessa cosa di _2_*IND, ma l'indice (Tabella D5I) e ritornato da un OAV dell'oggetto origine.
 * _2_4   *OAV      Attributo di un oggetto. Questo non restituisce l'oggetto destinatario del valore. Non innesca un indice di distribuzione del costo, ma porta l'intero valore sull'entità rappresentata dall'attributo, mettendola nell'indice rappresentato dalla D5E relativa.
 * _2_5   *PAR      Parametro di un oggetto. Questo non restituisce l'oggetto destinatario del valore. Non innesca un indice di distribuzione del costo, ma porta l'intero valore sull'entità rappresentata dall'attributo, mettendola nell'indice rappresentato dalla D5E relativa, usando un parametro di uno degli oggetti origine anziché un attributo come prima.
 * _2_6   *ASS      Valore assunto. Definisce qual è l'oggetto destinatario, come valore assoluto. Esempio :  se vogliamo destinare i valori secchi su un'azienda se non viene passata, è chiaro che si può usare quando il codice di destinazione è unico.

# Indici di distribuzione - Tabella D5I
La tabella degli indici di distribuzione ritorna sempre le percentuali di distribuzione di un valore origine sugli oggetti destinatari (ad esempio centro di costo che destina il suo valore, in percentuale, su altri centri di costo).
Si potrà definire la matrice di distribuzione con dei valori o con delle percentuali. Il prerequisito, quando si utilizzano i valori, è che nel campo "_2_C=calcola la %" si deve impostare il valore "_2_C".

Il _2_tipo oggetto 1 or 2 sono gli oggetti in cui si possono inserire le percentuali o valori, mentre il "_2_Tipo ogg. Risultato" è l'oggetto destinatario dei valori.
I due tipi oggetto origine rappresentano le due chiavi dei parametri.
![D5BASE_17](http://localhost:3000/immagini/D5BASE_005/D5BASE_17.png)
Il metodo o Programma può essere : 
 * _2_1   *PARA     Da parametro. Parametro della coppia oggetti origine.
 * _2_2   *PGM      Da pgm utente. Scrivere un programma utente (vedere programma esempio D5SRC/SMESRC D5D5I_1)
 * _2_3   *OAV      Da OAV oggetto. Il valore non è definito in un parametro ma è tornato da un OAV.
 * _2_4   *COSO     Da D5COSO (sviluppo). In fase di sviluppo.

# Scrittura dati su D5COSO - Impostazione /COPY D5A
Si può testare la D5A con il consueto programma di test.
![D5BASE_18](http://localhost:3000/immagini/D5BASE_005/D5BASE_18.png)![D5BASE_19](http://localhost:3000/immagini/D5BASE_005/D5BASE_19.png)![D5BASE_20](http://localhost:3000/immagini/D5BASE_005/D5BASE_20.png)