## Cos'è un Q1

L'oggetto Q1 una matrice di dati (nel senso matematico del termine) costituite da un elenco di righe facenti riferimento ad istanze della medesima classe (un elenco di articoli, di clienti, di movimenti di magazzino ecc.).

In questa accezione una query può essere rappresentata come un'aggregazione di 4 elementi : 
 :  : DEC T(OG) P() K(Q5)      I(_7_Fonte dati              )
 :  : DEC T(OG) P() K(Q2)      I(_7_Schema                  )
 :  : DEC T(OG) P() K(Q3)      I(_7_Filtro                  )
 :  : DEC T(OG) P() K(Q4)      I(_7_Ordinamento             )

La fonte dati rappresenta l'origine dei dati in cui ricercare gli oggetti, fornisce delle query che è possibile eseguire per lo specifico contenitore.
Lo schema imposta le proprietà dell'oggetto che arricchiscono il record restituito. Il filtro parzializza i record da restituire. L'ordinamento sequenzia i record.

Nella formulazione più generica, dato un tipo oggetto, la fonte, lo schema, il filtro e l'ordinamento possono venire definiti separatamente e indipendentemente. In fase di interrogazione  potrei scegliere liberamente quale ordinamento dare ai miei dati,  quali proprietà visualizzare, e quali record escludere.
Esigenze di velocità di calcolo o di opportunità applicativa possono invece portare  alla definizione di schemi e filtri specifici a certe fonti di dati.

**NOTA BENE** :  rispetto a questa definizione esistono però delle eccezioni per le quali la query, non è dato dalla composizione di schema/filtro/ordinamento/fonte, ma semplicemente da una funzione grafica che produce una matrice di dati.
In questa tipologia di query rientrano in particolare, le principali query fornite dallo standard :  cioè le fonti "F/" da surf (fonte *G46).

# La Codifica delle query

La gestione dell'oggetto Q1 si basa sulla struttura ramificata comune a tutti gli oggetti Qx. Per tale motivo esistono varie nature di schemi definite in modo eterogeneo (per fare un esempio confrontando la gestione dei Qx con le interfacce degli oggetti smeup, per queste, mentre posso avere attivi o gli articoli di smeup o gli articoli di un'altra applicazione, per gli oggetti Qx è come se avessi la possibilità di avere contemporaneamente sia gli articoli smeup che gli articoli di altre applicazioni nella medesima interfaccia. L'univocità del codice in tale struttura viene garantita dal fatto che ad ogni istanza, rispetto al suo codice originale, viene/vengono anteposti uno o due caratteri di prefisso, univoci per ogni fonte.

In smeup si possono trovare sia istanze di schema fornite dallo standard che istanze di schema creati appositamente nell'ambiente cliente.

Le tipologie delle query standard sono varie e definite dai pgm di fonte. A seguire ci si focalizza sulle query che possono essere invece implementate nell'ambiente cliente.

## Creare nuove query nell'ambiente cliente

A fianco delle query distribuite dallo standard possono essere implementate delle query create appositamente nell'ambiente cliente.

Queste query vengono definite all'interno degli script dei file SCP_QRY (per lo standard), SCP_QRYPER (per le personalizzazioni).
Il nome dello script deve corrispondere al nome dell'oggetto della lista; nel caso in cui esista un membro il cui nome corrisponda a TipoParametroOggetto il sistema analizza quello in caso contrario cerca un membro con nome corrispondente al solo Tipo Oggetto. Ad esempio se si tratta di uno schema sui clienti verrà prima cercato il membro CNCLI e quindi il CN.
Quando si vuole quindi implementare un nuovo schema sarà innanzitutto necessario : 
* Verificare se esiste già uno file sorgente SCP_QRY nella libreria di personalizzazione dell'ambiente.
** In caso contrario crearlo (copia ad esempio quello della DEV)
** In caso affermativo verificando la presenza del sorgente corrispondente alla classe interessata (facendo le dovute considerazioni sul tipo/parametro)
** Se opportuno prendere in considerazione la possibilità di sfruttare le istruzioni dello script INC.SCP per includere in differenti script le stesse istruzioni
Fatto questo si può passare alla compilazione dello script. In questo senso è' importante notare che all'interno di questi script possono essere definiti, non solo le query, ma anche tutte quelle informazioni utilizzabili poi nella costruzione della query stessa (schemi, filtri, ordinamenti).

Nel wizard di questi script sussistono quindi vari tag non tutti immediatamente correlati
alla definizione di una query. Può essere catalogato come tale esclusivamente il tag **QRY** : 
attraverso il quale può essere definita una nuova istanza di query.

Per caratterizzare la query è però di fatto necessario definire almeno anche i tag che fanno riferimento ai suo componenti :  filtro, ordinamento.

Per ognuno di questo si rimanda alla documentazione specifica.

- [Documentazione Classe Q3 - Utilizzo](Sorgenti/MB/DOC_OGG/OG_Q3)
- [Documentazione Classe Q4 - Ordinamenti](Sorgenti/MB/DOC_OGG/OG_Q4)

In concomitanza possono essere inoltre definiti nuovi schemi. Anche per questi rimanda alla documentazione specifica.
- [Documentazione Classe Q2 - Schema - Utilizzo](Sorgenti/MB/DOC_OGG/OG_Q2)

Si riporta inoltre che in tutti gli script QRY è possibile sfruttare inoltre queste variabili : 
* &OG.T1 :  tipo oggetto della query (es. se l'oggetto della query è CNCLI, la variabile varrà CN)
* &OG.P1 :  parametro oggetto della query (es. se l'oggetto della query è CNCLI, la variabile varrà CLI)
* &OG.E1 :  oggetto della query (es. se l'oggetto della query è CNCLI, la variabile varrà CNCLI)
* Tutte le variabili di ambiente (le variabili "_&_AM." gestite alla /COPY £G91, es. "_&_AM.AZ" è l'azienda, "_&_AM.UT" è l'utente corrente ecc.)

## Sovrascrivere/Integrare query standard

E' inoltre previsto, attraverso lo script, di poter aggiungere delle informazioni alle query standard (es. schema di default). Vanno però fatte alcune considerazioni : 
* Per le query standard non è possibile sovrascrivere la fonte originale (es. per *KEY ed *DEC la fonte deve rimanere *INT)
* Per le query *KEY ed *DEC non è possibile definire ordinamenti differenti da quelli corrispondenti alle chiavi di codice/descrizione.




