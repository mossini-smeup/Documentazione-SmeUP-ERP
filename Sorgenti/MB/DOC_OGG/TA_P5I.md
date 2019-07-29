# P5I - Tipo impegno materiali
 :  : DEC T(ST) K(P5I)
## OBIETTIVI
Descrivere le modalità di formazione e di scarico degli impegni di produzione (interni) e di lavorazione (esterni), sia che siano attivi o passivi.
## SOTTOSETTORI
Non gestiti
## CONTENUTO DEI CAMPI
 :  : FLD T$P5IA __Tipo origine__
È un elemento fisso V2/P5TOI.
Definisce l'oggetto a cui è assegnato l'impegno di risorse :  ordine di produzione, riga di ciclo esterno, ecc...
 :  : FLD T$P5IB __Tipo distinta origine__
È un elemento della tabella BRL. Definisce il tipo distinta che si usa nella scansione dei materiali di partenza.
È obbligatoriamente un tipo che ha come assiemi e componenti oggetti di tipo articolo.
**Attenzione** :  la mancanza di questo campo significa che non si desidera avere nessuna distinta origine. Non viene assunto nessun tipo di default.
 :  : FLD T$P5IC __Tipo distinta memorizzazione__
È un elemento della tabella BRL. Definisce il tipo distinta in cui si memorizza la distinta del documento.
È obbligatoriamente un tipo che ha come assiemi oggetti del tipo a cui si assegna l'impegno (ordini di produizione o righe di documento esterno) e componenti oggetti di tipo articolo.
**Attenzione** :  se non si imposta questo campo e il modo di costruzione degli impegni prevede la scansione della distinta del documento, la scansione stessa va subito a fine, con segnalazione di errore.
 :  : FLD T$P5ID __Tipo distinta variazione__
È un elemento della tabella BRL. Definisce il tipo distinta in cui sono presenti le variazioni da applicare alla distinta origine per ottenere gli impegni effettivi.
 :  : FLD T$P5IE __Modo costruzione impegni materiali__
È un elemento fisso V2/MOCIM.
Definisce il modo in cui si compongono gli impegni (ad esempio la sola distinta origine, quella del documento, e in assenza, la distinta origine, se e come tener conto della distinta di variazione.)
 :  : FLD T$P5IF __Causale di prelievo__
È un elemento della tabella GMC. Definisce la causale con cui vengono eseguiti i prelievi relativi ad impegni di questo tipo.
Il tipo movimento di questa causale deve essere lo stesso del tipo origine impostato in precedenza.
Se non impostata, nei prelievi viene assunta la causale definita nei parametri logistici di prelievo dell'articolo/magazzino.
La presenza di questo campo fa sì che, se l'impegno è esterno, il prelievo venga fatto automaticamente all'atto del collegamento dell'assieme (ad esempio lo scarico componenti presso il terzista, quando si riceve in azienda la riga dell'ordine di conto lavoro).
I movimenti effettuati con questa causale contribuiscono alla nettificazione degli impegni.
 :  : FLD T$P5IG __Tipo/Parametro distinta di variazione__
Definisce la natura dell'oggetto intestatario della distinta di variazione. Se impostato, l'oggetto di variazione è obbligatorio nella gestione degli ordini di produzione. Un possibile utilizzo è negli ordini di trasformazione.
 :  : FLD T$P5IH.T$P5IG
 :  : FLD T$P5IU __Suffisso pgm deviazione della scansione impegni__
È significativo nei seguenti due casi : 
- se impostato il modo di costruzione impegni materiali 'UT'. In questo caso viene lanciato il programma B£IDBID_x, dove x è questo suffisso, a cui è deviata totalmente la scansione della distinta del documento in esame.
- per impegni esterni, se impostato il tipo ciclo origine. Se impostato, viene lanciato il programma B£IDBID_x, dove x è questo suffisso, per ritornare le fasi ulteriori di impegno dell'assieme. Serve in caso di parallelismo delle operazioni.
 :  : FLD T$P5II __Causale di recupero__
È un elemento della tabella GMC. Se presente, i recuperi (scarichi degli impegni negativi) vengono eseguiti con questa causale come versamenti. In assenza vengono eseguiti come prelievi negativi con la causale di prelievo.
Il tipo movimento di questa causale deve essere lo stesso del tipo origine impostato in precedenza.
I movimenti effettuati con questa causale contribuiscono alla nettificazione degli impegni.
 :  : FLD T$P5IL __Tipo esplosione distinta__
Definisce il tipo di esplosione della distinta di origine. Se assente, viene assunto '3' (esplosione di produzione).
 :  : FLD T$P5I3
In questo campo si possono forzare i componenti (interni/esterni) che verranno ritornati dall'esplosione della distinta di origine.
Normalmente per impegni su ordine interno, viene scandita la distinta interna.  Per impegni su documento, invece, viene scandita la distinta esterna. Nel caso di impegni su documento ordine cliente, sarebbe opportuno che venisse scandita la distinta interna. Lo si fa impostando questo flag.
I valori ammessi sono : 
-    ' '   :  secondo il tipo impegno (ordine/documento);
-    'I'   :  componenti interni;
-    'E'   :  componenti esterni;
-    '*'   :  tutti i componenti;
 :  : FLD T$P5I1 __Trattamento movimenti neutri__
È un valore V2/SINO :  se impostato, nella nettificazione degli impegni vengono considerati anche i movimenti di magazzino neutri (che hanno in bianco l'azione sulla giacenza). Se la quantità è positiva è un prelievo, se negativa è un recupero.
 :  : FLD T$P5IM __Modalità scarico__
È un elemento fisso V2/MOSMA (modalità scarico per tipo impegno).
Definisce, se impostata, gli automatismi nello scarico degli impegni di questo tipo.
Se si imposta 'DO', viene eseguito lo scarico di tutti i materiali all'atto del versamento dell'assieme (ordine di produzione o riga di documento esterno), senza creazione degli impegni. Questa modalità può essere utile in una produzione 'leggera', con tempi brevi tra l'inserimento e l'esecuzione, in cui la presenza degli impegni nel sistema non ha significato applicativo.
_9_Esempio :  ricevimento di una bolla di lavorazione non preceduta dall'ordine. In questo caso gli impegni 'vivrebbero' soltanto dal momento dell'inserimento della bolla al suo collegamento a magazzino.
Quindi, un passo di flusso di inserimento/variazione degli ordini/documenti, che ha come scopo la creazione degli impegni, non produce nessun effetto per impegni di questo tipo .
Negli altri casi, la modalità di scarico per tipo impegno sostituisce la modalità di scarico componenti, definita nella tecnica di gestione dei campi dell'articolo/magazzino, secondo questa corrispondenza : 
-       IM :   -->  B (Scarico automatico di tutti i componenti);
-       IC :   -->  C (Scarico automatico di tutti i componenti su residuo);
-       ID :   -->  D (Scarico automatico di tutti i componenti alla fase);
In questo modo si può impostare tale comportamento a livello aziendale, o comunque in modo dipendente dal documento e non dall'articolo. Quindi può risultare superfluo sia specificarlo per tutte le tecniche di gestione, sia diversificare il comportamento per lo stesso articolo, a seconda del tipo impegno in cui si trova.
Questa corrispondenza ha l'effetto 'fisico' di scrivere sugli impegni, nel campo relativo, la modalità di scarico componenti. Di conseguenza, per le funzioni successive di trattamento degli impegni, è indifferente se la modalità di scarico proviene dalla tecnica di gestione oppure è derivata dal tipo impegno.
In particolare è opportuno impostare 'IM', vale a dire lo scarico automatico di tutti i componenti, nel caso di tipi impegno di conto lavoro, in cui normalmente si desidera lo scarico automatico di tutti i componenti indipendentemente dal loro comportamento nel caso di prelievo interno (definito dalla loro tecnica di gestione, oppure dalla modalità di scarico definita in questa tabella per gli impegni interni).
Se questo campo non è impostato, viene eseguito lo scarico automatico secondo quanto previsto dalle tecniche di gestione dei singoli componenti.
 :  : FLD T$P5IN __Causale di scarto__
Se impostata, è la causale proposta nelle dichiarazioni di scarto relative ad impegni di questo tipo. Il tipo movimento deve essere 'PS'.
Con questa casusale si dichiarano gli scarti dei componenti già prelevati.
I movimenti effettuati con questa causale non contribuiscono alla nettificazione degli impegni.
 :  : FLD T$P5IO __Rifasatura impegni__
I due caratteri definiscono la modalità di rifasatura degli impegni dopo la manutenzione o l'annullamento della distinta del documento.
Il primo carattere può assumere i valori : 
- Se impostato a 'A', gli impegni  vengono rifasati automaticamente.
- Se impostato un altro valore qualsiasi, gli impegni vengono rifasati previa richiesta di conferma.
- Se lasciato in bianco, non viene eseguita nessuna rifasatura.
Se impostato il secondo carattere, verranno rifasati anche gli impegni degli ordini di conto lavoro, collegati all'ordine di produzione in rifasatura.
 :  : FLD T$P5I2.T$P5IO
 :  : FLD T$P5IR __Aggiorna impegni origine__
È significativo per impegni esterni :  se impostato, all'atto del prelievo degli impegni (e se l'impegno ha un impegno origine) vengono scaricati anche questi impegni. In questo modo, un prelievo di conto lavoro di fase può contemporaneamente saldare l'impegno di produzione corrispondente.
 :  : FLD T$P5IP __Gruppo fonti__
Se impostato, nel prelievo pianificato verrà esposta la disponibilità riepilogata, costruita in base a questo gruppo fonti.
 :  : FLD T$P5IT __Gestione esponente modifica__
Se valorizzato, inserisce nell'impegno, all'atto della sua costruzione, l'esponente di modifica dell'articolo, secondo quanto impostato.
- Se impegno di produzione o impegno esterno con origine impegno di produzione : 
--     '1'  Data ordine;
--     '2'  Data inizio richiesta ordine;
--     '3'  Data fine richiesta ordine;
--     '4'  Data impegno;
- Se impegno esterno non collegato ad un ordine di produzione
-- '1'  Data documento;
-- '2'  Data consegna richiesta riga;
-- '3'  Data consegna confermata riga;
-- '4'  Data impegno.
 :  : FLD T$P5IQ __Tipo ciclo origine__
È significativo nel caso di scansione di lavorazione. Definisce il tipo ciclo assunto nella scansione dei materiali alla fase, per determinare la fase a cui assegnare l'assieme (fase precedente a quella dei materiali); se non impostato siglifica che non si desidera avere come componente l'assieme alla fase precedente.
 :  : FLD T$P5IX __Programma ripresa valori precedenti__
Se impostato, e se presente il flag corrispondente in tabella P51, nella rifasatura degli impegni materiali, in modalità non rigenerativa, viene eseguito il programma P5FASIM_x, dove x è il suffisso qui impostato. Questo programma riceve sia il record prima della rifasatura (se presente) sia
quello dopo. È così possibile trasferire le informazioni che si vogliono conservare, dal primo al secondo.
Questo richiamo viene eseguito prima del programma di aggiustamento, che è sempre l'ultima operazione prima della scrittura.
 :  : FLD T$P5IS __Causale di prelievo per fase__
Se impostato, definisce la causale con cui vengono eseguiti i prelievi relativi ad impegni di questo tipo, se intestati ad un oggetto/fase. In questo modo si può diversificare l'area e il tipo giacenza (normalmente le giacenze per articolo/fase sono parte del wip e non del magazzino).
Il tipo movimento di questa causale deve essere lo stesso del tipo origine impostato in precedenza.
Se assente, si assumerà la causale di prelievo precedentemente definita.
I movimenti effettuati con questa causale contribuiscono alla nettificazione degli impegni.
 :  : FLD T$P5IZ __Causale di prelievo per scarto__
Se impostato, definisce la causale con cui vengono eseguiti i prelievi collegati a scarti di assieme (effettuati sia in modo automatico che manuale).
Il tipo movimento di questa causale deve essere lo stesso del tipo origine impostato in precedenza.
Se assente, si assumerà la causale di prelievo precedentemente definita.
I movimenti effettuati con questa causale contribuiscono alla nettificazione degli impegni.
 :  : FLD T$P5IV __Tipo data scansione distinta__
È la data di validità che viene assunta nella scansione della distinta base per la costruzione degli impegni di questo tipo : 
-     Se impostato ' ', per gli impegni di produzione si assume la data inizio richiesta, per gli impegni esterni la data di consegna confermata.
-     Se impostato 'O', si assume la data odierna in entrambi i casi.
-     Se impostato 'D', si assume la data dal documento (nel caso di richiesta di acquisto viene utilizzata la data inserimento del record)
-     Se impostato 'E', si assume la data di inizio validità dell'esponente di modifica
-     Se impostato 'L', si assume per gli impegni di produzione la data fine richiesta, per gli impegni esterni la data di consegna confermata, rettificata (anticipando) dal Lead Time dell'assieme.
-     Se impostato 'P', viene lanciato il programma B£DATS_x (Da valore impostato in suffisso programma).
 :  : FLD T$P5I8 __Suffisso programma__
È il suffisso del programma B£DATS che viene lanciato se impostato P nel tipo data scansione distinta
 :  : FLD T$P5I5 __Trattamento scarti__
Definisce la modalità del trattamento degli scarti nella esplosione della distinta base.
 :  : FLD T$P5I6 __Arrotondamento da unità di misura__
Se impostato, la quantità dei componenti verrà arrotontata secondo quanto definito nella tabella della sua unità di misura.
 :  : FLD T$P5IW __Programma aggiustamento impegni__
I due campi del programma di aggiustamento definiscono il richiamo ad exit esterne.
Il primo campo è il suffusso x del programma P5FUIMT_x. Se presente, viene eseguito prima della scrittura dell'impegno, con la possibilità di modificare l'impegno stesso.
Se si imposta il secondo campo, il programma di aggiustamento viene lanciato anche con funzione 'CHG', prima dell'aggancio del record dell'impegno (eseguito per decidere se si deve scrivere un nuovo impegno od aumentarne uno esistente). Si ha quindi la possibilità di modificare dinamicamente il codice del componente. Se non si intende sfruttare questa possibilità, pur in presenza di programma di aggiustamento, si lascia in bianco questo campo, evitando cosi chiamate inutili ad un programma esterno.
 :  : FLD T$P5I4.T$P5IW
 :  : FLD T$P5I7 __Non perm.pre.NON PLN__
Se impostato, nella funzione di prelievo manuale componenti è inibito il tasto F08 di passaggio al prelievo di componenti non pianificati.
 :  : FLD T$P5IJ __Residuo per impegni__
Indica se la rifasatura degli impegni materiali deve essere eseguita al netto o al lordo dell'attesa (documenti non ancora collegati). I valori possibili sono : 
-      ' ' netto attesa.
-      '1' lordo attesa.
 :  : FLD T$P5IK __Pgm. Agg. Distinta Memorizzata__
È il suffisso del programma di aggiustamento che viene lanciato all'atto della scrittura della distinta memorizzata.
_9_Esempio :  P5FUDDC_X
 :  : FLD T$P5IY __Programma aggiustamento scarico impegni materiali.__
È il suffisso del programma di aggiustamento P5FUIMM_x (dove x è il suffisso indicato), che viene lanciato all'atto della scrittura dei movimenti di magazzino di scarico impegni materiali. Il prototipo di tale programma è P5FUIMM_X.
 :  : FLD T$P5I9 __No escl.mag.__
Se impostato questo campo, gli impegni di articoli esclusi da magazzino, avranno il flag 3 (escluso da analisi
coperture) impostato a '1'.
 :  : FLD T$P5I0 __No escl.pia.__
Se impostato questo campo, gli impegni di articoli esclusi da pianificazione, avranno il flag 3 (escluso da analisi
coperture) impostato a '1'.
 :  : FLD T1P5IA __No p.to rio.__
Se impostato questo campo, gli impegni di articoli gestiti a punto di riordino, avranno il flag 3 (escluso da analisi
coperture) impostato a '1'.
 :  : FLD T1P5IB __Fase as..__
Se impostato, negli impegni dell'ordine di produione con il componente uguale all'assieme, viene inserito nel campo
fase l'oggetto di riferimento impostato in testata dell'ordine di produzione.
L'assieme come impegno alla fase può essere utile in caso di rilavorazione :  un ordine di produizone
si interrompe, anche parzialmente, e si versa a magazzino, in un'area con tipo giacenza per fase,
il finito, per tenere traccia del livello di completamento della sua esecuzione. Un ulteriore
ordine di produzione, che dovrà portare a termine il ciclo, avrà, tra i suoi impegni, l'assieme alla
fase a cui si era interrotto. In questa accezione la fase svolge un ruolo di configurazione, mentre
non ha niente a che fare con il ciclo dell'ordine di completamento (potrebbe essere un ciclo ad hoc,
del tutto diverso da quello orginale dell'articolo).
 :  : FLD T1P5IC __/__
Se impostato, verrà forzato il plant dell'impegno nel gruppo fonti per l'analisi disponibilità, indipendenetemente dalla
lista plant memorizzata nel gruppo fonti stesso.





