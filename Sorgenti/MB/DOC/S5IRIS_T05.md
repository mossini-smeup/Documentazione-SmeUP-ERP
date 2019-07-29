# Generalità
Si definisce batch un insieme di impegni risorse (IR) che vengono eseguiti contemporaneamente sulla stessa risorsa :  hanno l'attrezzaggio comune, iniziano e finiscono contemporaneamente.
Un esempio di batch è costituito da uno stampo multiplo, che contiene più di un tipo di impronta (ad esempio n impronte dell'articolo A, e M impronte dell'articolo B).
Un altro esempio è costituito da un forno, in cui possono essere caricati impegni che hanno le stesse caratteristiche di temperatura e di durata, con il limite di carico costituito dalla capacità del forrno.

La gestione di un batch si compone di due attività : 
- composizione del batch, con gli impegni risorse opportuni, rispettando i vincoli produttivi (riempimento del forno, compatibilità degli articoli sullo stesso stampo ...).
- schedulazione del batch, come se fosse un solo impegno, e conseguente datazione degli impegni che lo compongono.

Quando, all'interno della schedulazione, si interviene manualmente per modificarne i risultati (congelamento, forzatura, risequenziazione, spostamento da una risorsa all'altra) si agisce sul batch nella sua interezza, come se fosse un solo impegno. Ad esempio, quando si sposa un impegno da una risorsa (specifica) ad un'altra, tutti gli impegni del batch vengono spostati solidalmente.


# Impostazioni
L'attivazione dei batch è impostata a livello di risorsa principale, attribuendogli un gruppo risorsa che abbia valorizzati i due flag che li definiscono : 
* Classe batch :  definisce le condizioni di raggruppabilità degli impegni risorse per comoprre un batch
* Tipo batch :  definisce il modo in cui vengono datati, nella schedulazione fine, gli impegni risorse appartenetti ad un batch.
Se quindi si vuol diversificare la modalità con cui si raggruppano gli impegni, si definiscono più classi batch, e conseguentemente più gruppi risorse.Il tipo batch va impostato in base alle caratteristiche tecnologiche del processo che si descrive.
Si possono avere quindi, gruppi risorsa con classi batch diverse ed uguale tipo batch (ad esempio presse diverse che hanno modalità diverse di composizione dei batch ma con lo stesso modo di datazione).
Non è invece consistente avere gruppi risorsa con la stessa classe batch ma diversi tipi batch, in quanto si potrebbero costruire batch con impegni che presentano diverse modalità di datazione.

## Classe batch
E' l'elemento base per il raggruppemento degli impegni che costituiscono una famiglia batch (tutti gli impegni che possono comporre lo stesso batch).
E' un oggetto di tipo
 :  : DEC T(SS) P(*CN) K(S6) L(1)
E' memorizzato nel flag 18 di S5IRIS
 :  : DEC T(VO) P(F.S5IRIS0F) K(S6FL18)
E' il suffisso di tutte le exit che sono state messe a disposizione nella gestione dei batch.
Se si desidera, per motivi particolari, escludere un impegno dal processo di formazione di un batch, è sufficiente, nell'exit della costruzione degli impegni risorse, pulire il campo S6FL18 :  in tal modo questo impegno risulterà isolato.

## Tipo batch
Individua il modo in cui viene attribuito l'istante di inizio e di fine degli impegni risorse appartenenti ad un batch.
E' un oggetto di tipo
 :  : DEC T(OG) K(V2S5_TB) L(1)
E' memorizzato nel flag 14 di S5IRIS
 :  : DEC T(VO) P(F.S5IRIS0F) K(S6FL14)

## Famiglia batch
Individua tutti gli impegni che potenzialmente potrebbero essere riuniti per comporre un batch. Dà luogo alla compatibilità statica (condizione necessaria, precedente al processo di costruzione).
E' composta logicamente dai seguenti campi di S5IRIS
* Scenario (fisso **)
* Tipo origine
* Classe batch (Flag 18) :  non è ridondante, rispetto al campo successivo di risorsa principale (che apaprtiene ad un gruppo risorsa, che a sua volta contiene una class batch), in quanto potrebbe essere stato pulito dalla exit di S5IRIS0F.
* Tipo e codice risorsa principale
* Codice libero 4 e Codice libero 5. Questi campi vengono riempiti dall'exit S5BCH01_x, dove x è la classe batch.
 :  : DEC T(MB) P(S5SRC) K(S5BCH01_X) L(1)
 E' quindi possibile decidere che, ad esempio, l'elemento di compatibilità è lo stampo dell'articolo. Se l'exit è assente, questi codici rimangono vuoti :  ciò significa che tutti gli impegni di questa risorsa possono essere raggruppati in un batch (ad esempio in un processo di lavaggio tutti gli impegni possono essere raggruppati fino all limite del volume, caso che sarà trattato nel seguito nella compatibilità dinamica). Naturalmente è sempre possibile riempire i codici liberi 4 e 5 nell'exit generale di S5IRIS, ma in questo caso, oltre a rendere la compatibilità più nascosta, se il riempimento avviene in modo differenziato per le diverse classi batch, si dovranno introdurre comportamenti cablati in modo esplicito.
Tecnicamente è la parte iniziale (fino al campo libero 5 compreso) del logico
 :  : DEC T(OJ) P(*FILE) K(S5IRIS7L)

## Raggruppamento
Individua gli impegni che compongono un batch. In sostanza è un sinonimo di quest'ultimo termine.
Viene costruito (essenzialmente il codice dell'oggetto di raggruppamento) nella composizione del batch (automatica o manuale, come verrà esposto nel seguito).
E' composto dai seguenti campi di S5IRIS
* Scenario (fisso **)
* Tipo origine
* Tipo oggetto di raggruppamento (fisso "IR")
* Parametro oggetto di raggruppamento (fisso bianco)
* Codice oggetto di raggruppamento :  è l'IDOJ dell'impegno master (vedi sotto) del raggruppamento
Tecnicamente è la parte iniziale (fino al campo oggetto di raggruppamento compreso) del logico
 :  : DEC T(OJ) P(*FILE) K(S5IRIS8L)

## Tipo impegni batch
E' una caratteristica dell'impegno di un batch, memorizzato nel flag 16 di S5IRIS
 :  : DEC T(VO) P(F.S5IRIS0F) K(S6FL16)
e viene valorizzato anch'esso nel processo di composizione del batch.
Se rimante vuoto l'impegno è isolato (l'oggetto di raggruppamento è anch'esso vuoto).
Se vale 'M' individua l'impegno master del batch, vale a dire quello che ha CROR più basso. E' l'impegno che viene schedulato e che 'tira' gli altri impegni, slave.
Tecnicamente il suo IDOJ individua il batch. Nel campo oggetto di raggruppamento viene riportato questo valore.
Se vale 'S' individua un impagno slave. Nel campo oggetto di raggruppamento viene riportato l'IDOJ dell'impegno master.

## Congelamento impegno
In schedulazione definisce una sequenza di schedulazione su una risorsa specifica che viene mantenuta nelle successive schedulazioni, all'inizio della coda della risorsa specifica, immediatamente dopo gli eventuali impegni in corso.
Un batch viene congelato (e scongelato) nella sua interezza, con progressivi contigui a partire dal master.

## Forzatura impegno
In schedulazione definisce una risorsa specifica su cui viene eseguito obbligatoriamente un impegno.
Un batch viene forzato (e "sforzato") nella sua interezza.

## Congelamento batch
Nella funzione di gestione manuale del batch, è possibile "congelare" la composizione di un batch, vale a dire che esso viene mantenuto tal quale in una successiva ricostruzione automatica dei batch.
E' una caratteristica dell'impegno di un batch, memorizzato nel flag 19 di S5IRIS.
 :  : DEC T(VO) P(F.S5IRIS0F) K(S6FL19)
Un batch con gli impegni congelati, forzati o iniziati è implicitamente congelato.



# Costruzione batch
La costruzione di un batch può avvenire in modo automatico oppure manuale.
Nel primo modo si elabora sempre un'intera famiglia, in quanto
Nel secondo modo




## Compatibilità statica




## Compatibilità dinamica




## Compatibilità di alternative (risorse specifiche)
Tutti gli impegni di un batch devono poter essere eseguiti sullo stesso insieme di risorse specifiche, se queste sono attive.

## Compatiibilità di risorse secondarie
Attualmente, per la composizione di un batch, NON è verificata la compatibilità di risorse secondarie, nè di segnalazione nè di vincolo.





## Incompatibilità per forzatura
Non è possibile comporre un batch con impegni forzati, ed un batch con impegni forzati viene considerato congelato implicitamente.
Il motivo è che si potrebbe introdurre un'incongruenza di risorse specifiche.
Esempio 1
Consideriamo gli impegni Ixx, ciascuno eseguibile sulle risorse specifiche Rxx : 
I01 - R01 / R02 / R03 (master)
I02 - R02 / R03
I03 - R02 / R04
Supponiamo di forzarli tutti sulla R02.
Trascurando il fatto che è presente una forzatura, la compatibilità di alternative (risorse specifiche) sarebbe vertificata, quindi si potrebbe costruire (sia manualmente sia automaticamente) il batch B01, che risulterebbe forzarto sulla risorsa 02.
Come esposto in precedenza, un batch può essere forzato e "sforzato" nella sua interezza, quindi, nel presente caso, la "sforzatura" del batch B01 (mantenendolo costruito) porterebbe alla violazione della compatibilità. Infatti, se I02 trovasse, come prima risorsa disponibile, R01, non potrebbe "tirarvi" gli altri due impegni, che non sono eseguibili su quella risorsa.
Questo dimostra l'assunto di partenza :  la forzatura nasconde la compatibilità di alternative.

## Incompatibilità per congelamento impegni
Non è possibile costruire un batch con impegni congelati. Infatti se ne dovrebbe controllarne la contiguità. Questo risulterebbe molto laborioso nella stesura dell'algoritmo di compatibilità dinamica.
Un batch con impegni congelati viene considerato congelato implicitamente, in quanto, se così non fosse, si ricadrebbe, nella successiva costruzione, nel caso precedente.

## Scomposizione batch
Nella ricostruzione automatica dei batch, vengono "sciolti" e resi disponibili per ricomporre altri batch, i batch non congelati esplicitamente (nella gestione manuale) o implicitamente (se gli impegni sono iniziati, congelati o forzati).
Nella gestione manuale è possibile "sciogliere" i batch congelati soltanto se i loro impegni non sono iniziati, congelati o forzati.

























