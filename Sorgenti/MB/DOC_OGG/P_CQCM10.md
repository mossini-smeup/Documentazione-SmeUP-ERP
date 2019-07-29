# Obiettivo
Assegnare per ogni articolo la metodologia di controllo delle caratteristiche, in funzione del loro grado di importanza.
Indicare per ogni fase del ciclo di controllo la tipologia dello strumento di misura da utilizzare.

# Generalità
Il programma dei cicli di collaudo prevede : 
 * _2_PER IL CICLO DI COLLAUDO ACCETTAZIONE
l'abbinamento delle caratteristiche dimensionali e/o degli attributi di un articolo al piano di campionamento ed al livello di L.Q.A. in funzione della CLASSE FUNZIONALE e della CLASSE DI IMPORTANZA della caratteristica in esame.
 * _2_PER IL CONTROLLO DA ESEGUIRE NELLA FASE DI LAVORAZIONE
l'abbinamento alle caratteristiche dimensionali e/o degli attributi dell'articolo per la fase di lavorazione in esame della frequenza dei controlli da eseguire in funzione della CAPABILITY precedentemente eseguita sulla macchina che esegue la fase in esame.
 * _2_LEGAME CON IL CICLO DI LAVORAZIONE ASSEGNATO
Ogni fase del ciclo di collaudo, sarà legata alla fase corrispondente del ciclo di lavoro con un legame tipo :  molti a uno.

Ad ogni fase, sarà indicato : 
 ** il tipo di controllo da eseguire,
 ** la tipologia dello strumento di controllo,
 ** i valori di riferimento, quali ad esempio : 
 ** piano di campionamento,
 ** il livello di qualità L.Q.A.,
 ** la frequenza dei controlli,
 ** etc.

## Azioni
Quando il ciclo viene ripreso nelle fasi di controllo, in funzione del fornitore (abilitazione alla classe funzionale) e/o del Work-Center (Capability della macchina) sarà rispettivamente variato in automatico il P.d.C. e/o la frequenza dei controlli da eseguire.
Il programma prevede, in caso di emissione di una RM-AM (richiesta di modifica) registrata ed approvata dalla Direzione Tecnica di segnalare una possibile variazione delle caratteristiche a ciclo. controllare che la classe di precisione della tipologia di strumento assegnata alla fase sia compatibile con la tolleranza riportata a disegno.

### Codice del difetto abbinato
Ad ogni fase del ciclo di collaudo viene assegnato il codice del probabile difetto, che potrà essere riscontrato in fase di collaudo per quella fase del ciclo, e la gravità del difetto assegnata. Il codice del difetto è tabellato, ed assieme ad esso viene proposto l'indice di gravità che potrà essere variato durante l'inserimento della fase del ciclo a seconda della gravità effettiva che il difetto può assumere per il pezzo in controllo.
Questi valori saranno proposti automaticamente qualora, in fase di collaudo accettazione, alla fase del ciclo di collaudo dovessero rilevarsi dei pezzi difettosi.

## Formato guida
![CQ_CCOL_04](http://localhost:3000/immagini/MBDOC_OGG-P_CQCM10/CQ_CCOL_04.png)
Particolarità : 
 * _2_fase lavorazione, nel caso di un articolo di acquisto o di un prodotto finito relativamente ai quali non ci sono fasi di lavoro si può superare questo controllo immettendo la fase di lavoro jolly (**)
 * _2_esponente di modifica, il programma correla il livello di modifica della fase del ciclo al livello di modifica del disegno, per cui si può immettere  un ciclo di collaudo ad un livello 'x' di modifica solo se è già stato emesso per l'articolo in questione un disegno tecnico a livello di modifica 'x'. Se è attivo il mudulo DOCU e sono gestiti i disegni tecnici. il programma si collega con questo modulo per fare in modo che ci sia la corrispondenza tra esponenti di modifica del ciclo di collaudo e del disegno tecnico.

## Formato lista
![CQ_CCOL_05](http://localhost:3000/immagini/MBDOC_OGG-P_CQCM10/CQ_CCOL_05.png)
## Formato dettaglio
![CQ_CCOL_06](http://localhost:3000/immagini/MBDOC_OGG-P_CQCM10/CQ_CCOL_06.png)
 * _2_esponente di modifica inferiore, segnala il livello di modifica inferiore del disegno tecnico per cui vale il  ciclo di collaudo in esame
 * _2_esponente di modifica superiore, segnala il livello di modifica superiore del disegno tecnico per cui vale il  ciclo di collaudo in esame, nel caso sia lasciato blank il ciclo di collaudo vale per tutti i disegni aventi livello di modifica maggiore o uguale al livello di modifica inferiore.
 * _2_obbligatorietà, è un campo tabellato CQ4 che descrive la obbigatorietà del controllo, il controllo può essere obbligatorio / non  obbligatorio, la registrazione obbligatoria / non obbligatoria;
 * _2_codice descrizione,  è un campo tabellato CQ*CD che descrive la fase del collaudo (controllo ammmaccature, coppia, arrotondatura dente);
 * _2_tipo di misura, è un campo tabellato CQT che identifica la natura del controllo (ad esempio "dimensione tolleranza assoluta"), il tipo di valori nominali da indicare (vedi tabella CQK Rilievi di misurazione) (ad esempio, valore nominale, tolleranza +, tolleranza -) ed i valori di riepilogo della misurazione (ad esempio media, valore massimo, devianza,..)
 * _2_classe di importanza, è un campo tabellato CQI che identifica la criticità della caratteristica controllata ed il range di LQA accettabili;
 * _2_strumento di controllo, il programma si collega con l'anagrafica strumenti e permette di effettuare la selezione. Dato lo stretto legame tra strumento ed unità di misura, scelto lo strumento il programma riporta automaticamente l'unità di misura. Viene data comunque la possibilità di modificare l'unità di misura dato che esistono strumenti di lavoro che operano su più unità di misura;
 * _2_procedura di controllo, è un campo tabellato CQM che identifica la procedura o istruzione di controllo per l'attività in esame;
 * _2_codice difetto, è un campo tabellato CQD dove viene data la possibilità di proporre un difetto per la caratteristica dell'articolo che si sta collaudando;
 * _2_piano / livello campionamento, in automatico il programma presenta la selezione piano/livello= **/** che è la modalità di campionamento "libero" in quanto viene assegnato il campionamento calcolato per il lotto, oppure può essere selezionato (CQP (Pdc) e CQ*SE (tipo Pdc)) un piano di campionamento, che possiamo definire "fisso", specifico della tripletta articolo/fase di lavorazione/ciclo di collaudo. È lasciata questa possibilità perché  per certi particolari tipi di prove che sono distruttive o che richiedono strumenti sofisticati, quindi particolarmente costose, va imposto un  campionamento indipendentemente dal lotto.
 * _2_unità di misura, è un campo tabellato CQM,  viene immessa dal programma una volta scelto lo strumento, viene data comunque la possibilità di modificare l'unità di misura dato che esistono strumenti di lavoro che operano su più unità di misura. Il programma esegue però un controllo di corrispondenza tra strumento e misura;
 * _2_tipo di controllo, è un campo tabellato CQ0 che identifica il tipo di controllo, può essere effettuato dall'operatore durante il ciclo di produzione (autocontrollo) oppure potrebbe essere un controllo in accettazione di merce in ingresso, oppure un controllo in una fase di lavorazione interna, etc.. In funzione del tipo di controllo viene stampata un certo tipo di griglia :  benestare di collaudo, autocontrollo operatore, griglia a fornitore;
 * _2_livello di qualità accettabile (L.Q.A.), è un indice che definisce la percentuale di non conformi accettabili in un lotto. L' L.Q.A. come prescritto dalla norma  UNI 4842-75 dovrebbe essere specificato nel contratto. Questo valore viene messo direttamente dal programma in funzione della classe di importanza scelta dal collaudatore.
 * _2_Codice Attrezzatura,
 * _2_Fase Rilavorazione, fase di lavorazione del ciclo a cui il lotto deve essere sottoposto nel caso in cui siano ravvisate delle non conformità  tali da causarne la non accettazione in collaudo.

### Funzioni aggiuntive
Possono essere lanciate dalle selezioni in basso del formato dettaglio : 
![CQ_CCOL_07](http://localhost:3000/immagini/MBDOC_OGG-P_CQCM10/CQ_CCOL_07.png)
_1_Dati di controllo
![CQ_CCOL_08](http://localhost:3000/immagini/MBDOC_OGG-P_CQCM10/CQ_CCOL_08.png)
_1_Dati aggiuntivi
![CQ_CCOL_09](http://localhost:3000/immagini/MBDOC_OGG-P_CQCM10/CQ_CCOL_09.png)
_1_Tempi e costi
![CQ_CCOL_10](http://localhost:3000/immagini/MBDOC_OGG-P_CQCM10/CQ_CCOL_10.png)