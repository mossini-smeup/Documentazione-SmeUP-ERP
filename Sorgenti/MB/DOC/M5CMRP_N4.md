# Modo di sviluppo degli oggetti di rottura nell'MRP


##  Introduzione
L'oggetto di rottura è un codice che si accoda allo scenario, al plant e all'articolo per costutiure l'insieme degli oggetti su cui si esegue la pianificazione.

L'MRP di Smeup gestisce i seguenti oggetti di rottura : 
* Configurazione
* Commessa
* Ente
* Esponente di modifica
Tutti questi campi sono presenti nell'archivio della pianificazione
 :  : DEC T(OJ) P(*FILE) K(M5CONS0F)

Per attivare questa funzione è necessario inserire in tabella M51 uno dei precedenti oggetti.
Si deve quindi stabilire quali articoli sono gesatiti a rottura.
Ci sono due possibilità : 
* Si imposta un flag in tabella M51, che fa sì che tutti i codici siano gestiti a rottura.
* Si imposta un flag sulla politica master (M5A) degli articoli che si vogliono gestire a rottura. Questo campo è superfluo se è stato impostato il precedente.
 :  : DEC T(ST) K(M51)
 :  : DEC T(ST) K(M5A)

## Trattamento oggetto di rottura in dettaglio
Il caricamento delle fonti rilasciate
 :  : DEC T(OJ) P(*PGM) K(M5M5R0I)
lanciato per ogni articolo in ordine di livello minimo crescente
(per un'esposizione dettagliata della struttura dell'MRP riferirsi al documento)
 :  : DEC T(MB) P(DOC) K(T_M5_002) O(D) L(1)
scrive nel record dell'archivio tutti i possibili oggetti di rottura, ciascuno nel campo corrispondente, partendo da quanto ritorna la scansione della disponibilità (ad esempio la commessa viene copiata da £M5DCO in H§COMM).
Se l'articolo che si sta scandendo è gestito a rottura, il corrispondente campo viene copiato nell'oggetto di rottura. Proseguendo con il precedente esempio, se la pianificazione è a rottura di commessa e l'articolo che si sta trattando è gestito a rottura, il campo H§COMM viene copiato nel codice di rottura (H§CROT).

A questo punto, il successivo programma, che esegue la pianificazione di ogni singolo articolo
 :  : DEC T(OJ) P(*PGM) K(M5M5R0)
tratta separatamente le fonti di ogni coppia articolo/oggetto di rottura.
Quando si  pianifica un nuovo ordine, si scrive l'oggetto di rottura che si sta trattando, oltre che nel campo generico, anche nel campo dello specifico oggetto di rottura; ad esempio, oltre che  in H§CROT, anche in H§COMM. In questo modo viene eseguito il passaggio del campo specifico che contiene l'oggetto di rottura, dai record rilasciati a quelli pianificati.

Dopo aver scritto gli ordini pianificati, se essi sono di produzione o di lavorazione esterna, vengono scritti i relativi impegni pianificati. In essi vengono mantenuti i campi specifici dellì'ordine assieme (commessa, ecc...) ma viene ripulito il campo oggetto di rottura, in quanto non è ancora noto se gli articoli degli impegni saranno, a loro volta gestiti a rottura, e sarebbe altamente inefficiente verificarlo a questo punto, per ogni impegno scritto.
 :  : DEC T(OJ) P(*PGM) K(M5M5W0_SM)
Gli articoli degli impegni, avendo un  livello minimo più alto degli assiemi, saranno trattati successivamente nella pianificazione.

Il programma che scrive le fonti rilasciate, che abbiamo incontrato all'inizio di questa esposizione,
 :  : DEC T(OJ) P(*PGM) K(M5M5R0I)
riceve dalla scansione della disponibilità anche le fonti pianificate (che devono essere presenti nel gruppo fonti).
A questo punto è noto se l'articolo è gestito a rottura (questo controllo viene eseguito una volta per ogni articolo) :  se lo è, il campo specifico (ad esempio la commessa, ereditata dall'assieme) viene copiato nellì'ogggetto di rottura dell'impegno pianificato che, in tal modo, è, per quanto riguarda il riempimento dell'oggetto di rottura, simile alle alle fonti rilasciate.

## Considerazioni generali
Come si è visto, l'oggetto di rottura può essere ereditato, ma, una volta interrotta la catena (incontrando un articolo non gestito a rottura) non può essere più ripristinato. Si può quindi immaginare una linea che divide l'insieme degli articoli :  al di sopra di essa sono gestiti a rottura e al di sotto no.

Nel seguito riportiamo alcune considerazioni specifiche di ogni oggetto di rottura, di natura sia tecnica sia applicativa.

## Commessa
La pianificazione a rottura di commessa rappresenta il caso classico di separazione. Normalmente gli assiemi e i sottoassiemi di primo livello solo gestiti a rottura, mentre, scendendo, si perde questa informazione, in quanto i componenti di più basso livello sono generalmente articoli standard.

## Configurazione
In questo caso, può presentarsi la necessità di "dimagrire" la configuirazione nel passaggio dagli ordini pianificati ai relativi impegni, ad esempio per eliminarne alcune parti  che sono di pertinenza solo dell'assieme. Questa operazione va eseguita nella exit di scrittura dei consigli, quando si incontrano impegni pianificati. A questo punto sono noti tutti i parametri che entrano in gioco :  il codice dell'assieme e del componente, e  la configurazione dell'assieme, e quindi si possono implementare comportamenti specifici per modificare la configurazione del componente.

## Ente
E' il caso della pianificazione "logistica" in cui si determina anche la destinazione (individuata dall'ente) di ordini e impegni.
Tutti i codici devono essere pianificati a rottura.
Si rimanda alla documentazione applicativa per un'esposizione completa di questa modalità.
- [MRP Logistico](Sorgenti/MB/DOC/M5_013)
In questa sede esponiamo alcune particolarità dell'implementazione.
Innanzitutto, negli ordini pianificati non viene copiato, nel programma
 :  : DEC T(OJ) P(*PGM) K(M5M5R0)
l'oggetto di rottura nel campo specifico (in questo caso l'ente), ma questa operazione è demandata al programma di selezione dell'ente dell'ordine pianificato
 :  : DEC T(OJ) P(*PGM) K(M5M5S0_SM)
che riempie il campo ente anche in caso di ordine di produzione. In tal modo si disaccoppia, sugli ordini pianificati il destino (oggetto di rottura) e l'esecutore (l'ente).
Anche in questo caso, come per la commessa, l'ente dell'ordine pianificato viene mantenuto tal quale sugli impegni.

## Esponente di modifica
Questo oggetto di rottura fa eccezione per due aspetti : 
* Sugli impegni pianificati a standard non viene trasferito l'esponente di modifica dell'assieme, ma viene ricalcolato
* La catena di oggetti di rottura, oltre ad essere interrotta, scendendo nei livelli può essere ripristinata

L'esponente di modifica del componente viene determinato nel seguente modo : 
Se l'assieme è gestito a rottura viene determinata la data di ingresso del suo esponente di modifica, che viene utilizzata per calcolare l'esponente di modifica del componente valido a quella data.
In questo modo di garantisce la congruenza costruttiva tra l'assieme e il componente.
Se l'assieme non è gestito a esponente di modifica, si considera il campo "Esponente di modifica del componente" della politica master dell'assieme.
 :  : DEC T(ST) K(M5A)
Questo campo, se presente, indica quale data viene utilizzata per determinare l'esponente di modifica del componente. In  questo modo si può ripristinare la catena interrotta. Un esempio applicativo è il caso di produttori di componentistica, sia di primo impnanto sia di parti di ricambio (con codici diversi). L'esponente di modifica viene trattato solo per i primi codici, che possono condividere con i secondi alcuni componenti, gestiti a loro volta a esponente di modifica.













,
