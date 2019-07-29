# Compatibilità
La release minima di sistema operativo con cui è compatibile Sme.UP ERP è la V6R1.
È quindi importante prestare attenzione a non utilizzare istruzioni di release successive, in quanto potrebbero essere accettate dal Seu, ma non dal compilatore.

# Esempi di programmi
Il file QSRCGEN nella libreria SMEDEV contiene degli esempi di sorgenti di programmi, che possono essere utilizzati come prototipi.
Di seguito **alcuni** dei sorgenti disponibili : 


| MIN_RPG | include le /copy minime per un programma Sme.up |
| ---|----|
| FMT2_RPG | programma minimale con utilizzo di n file video |
| FUN | prototipo di programma "funizzato" (avente un'interfaccia standard con cui essere richiamato) |
| 


# La stesura del codice
## Definizioni
In testa si trova l'elenco delle modifiche, contrassegnate come specifiche **V***, interpretate nella scheda Modello Dinamico di Looc.up.
Per informazioni sul Modello Dinamico, fare riferimento all'apposito paragrafo del documento sotto riportato : 
- [Lavorare con i programmi](Sorgenti/MB/DOC/A£BASE_SD)

Si trovano poi una serie di specifiche : 
>H/COPY QILEGEN,£INIZH

per l'inclusione delle specifiche di compilazione contenute nella /copy **£INIZH**.

>I/COPY QILEGEN,£TABB£1DS

La /copy **£TABB£1DS** definisce le 2 DS : 
 * B£1$DS  :  utilizzata per salvare i riferimenti degli applicativi a cui puntano gli oggetti (es. cliente, fornitore, articolo) e dell'ambiente.
 * B£2$DS  :  utilizzata per salvare campi eterogenei (es. azienda, divisa, magazzino).

>I/COPY QILEGEN,£PDS

La /copy **£PDS** definisce la mappatura dell'area dati LDA (Local Data Area) con campi contenti dati di sistema e dati caricati dalla /copy £INZSR.
La /copy **£INZSR** si occupa di inizializzare il programma, valorizza la LDA ed esegue la routine **£INIZI** (eseguita solo la prima volta, nel caso il programma termini con RT)
Al di sotto della specifica relativa alla £PDS posso definire delle variabili includendole nella LDA (metodo utilizzato per il passaggio di parametri in chiamate batch di altri programmi).

**È preferibile che la definizione delle variabili avvenga sempre in testa al sorgente come specifiche D, e non a destra in specifiche C.
>DSTR198           S            198


A volte però risulta ancora necessario utilizzare la dichiarazione in specifiche C, come nel caso in cui ci sia bisogno di dichiarare delle variabili all'interno di /COPY di specifiche C.
>C* Dichiarazione variabili locali
C     'A'           IFEQ      'B'
C                   MOVEL     *BLANKS       £MDVNA            1
C                   MOVEL     *BLANKS       £MDVAP            8
C                   ENDIF

Per la definizione delle DS utilizzare in modo esteso l'istruzione **LIKE** per la definizione dinamica a partire dai campi dei file di dati.

## Costanti
È necessario che le costanti non siano definite come stringhe fisse all'interno di specifiche C od O, ma tramite valorizzazione di schiere a livello di programma, altrimenti non ne viene gestita la traduzione in fase di precompilazione. Lo stesso vale per le costanti utilizzate nei file di stampa.

## ILE RPG
Si suggerisce l'utilizzo di **specifiche CX** e di **EVAL** invece di MOVEL, in modo da rendere più facile un eventuale passaggio al FREE, per ora non in programma.
Inoltre si consiglia di usare istruzioni che supportano il formato libero (DO, FOR) ed evitare di utilizzare l'istruzione GOTO.
Attenzione agli indicatori :  se un indicatore non viene impostato come acceso o spento, per RPG ha valore acceso, mentre per l'ILE ha valore spento.

## Utilizzo di /COPY nidificate (come ad esempio £JAX_C)
In Sme.up alcune /COPY sono nidificate.
Ad esempio, la /COPY £JAX_C contiene al suo interno il richiamo della £JAX_C1 e della £JAX_C2.
In alcuni casi sembra esserci l'esigenza di "scorporare" alcune /COPY nidificate (cioè richiamare singolarmente le diverse /COPY contenute all'interno).
Questo comportamento è fortemente sconsigliato, in quanto l'eventuale aggiunta di ulteriori richiami nella /COPY "contenitore" non viene recepito nei programmi in cui tale COPY è stata scorporata.
Seguendo l'esempio iniziale, l'eventuale aggiunta nella £JAX_C del richiamo alla /COPY £JAX_C3, non verrebbe recepita nei pgm in cui sono state inserite singolarmente la £JAX_C1 e la £JAX_C2.

### SQLRPGLE
Il precompilatore SQL non gestisce le /COPY nidificate. Quindi se un membro è di tipo SQLRPGLE e non RPGLE, sembra necessario scorporare le /COPY nidificate per poter compilare correttamente.
In realtà è sufficiente sostituire la direttiva /COPY con /INCLUDE (che ha in pratica lo stesso comportamento di /COPY tranne per il fatto che con  questa il precompilatore SQL è in grado di gestire la nidificazione).
E' sufficiente inserire /INCLUDE solo per la COPY "contenitore", quindi tornando all'esempio iniziale, è sufficiente scrivere /INCLUDE QILEGEN,£JAX_C invece di /COPY QILEGEN,£JAX_C;
non è necessario modificare il contenuto della /COPY £JAX_C.

### NON-inclusione una /COPY inclusa in un'altra
In alcuni casi non si vogliono inserire tutte le COPY richiamate dalla /COPY contenitore.
Un esempio ricorrente è quello della £JAX_C. Essa richiama anche la £JAX_C9 che contiene la ENTRY PLIST.
In alcuni programmi con una propria ENTRY PLIST (tipicamente non servizi) in cui si ha l'esigenza di inserire ad esmpio la £JAX_C1, non si può inserire anche la £JAX_C9 che contiene una nuova ENTRY PLIST.
In questo caso, invece di inserire manualmente tutte le altre /COPY, è possibile richiamare la £JAX_C facendo in modo che la £JAX_C9 non venga inserita.
Per fare questo è possibile utilizzare alcune direttive di compilazione. Nel caso specifico, basta scrivere /DEFINE JAX_C9_INCLUDED /COPY QILEGEN,£JAX_C.
In questo modo vengono incluse tutte le /COPY contenute nella £JAX_C tranne la £JAX_C9.

## Performance
In fase di sviluppo si raccomanda di prestare attenzione alle performance, ad esempio relativamente al numero di accessi in lettura di un file di dati.
Se si usano le CL è meglio definirle come CLLE (il record è più lungo e le performance risultano migliori.

## Commenti
È raccomandato l'utilizzo dei commenti, al fine di aumentare la leggibilità del codice, in particolar modo nel caso di modifiche.
