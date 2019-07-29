#  Insiemi, relazioni e proposizioni
In Teoria degli Insiemi, con il termine "relazione" si intende un qualsiasi tipo di associazione che si può stabilire tra gli elementi di due insiemi arbitrari.
Così, per esempio, se prendiamo l'insieme degli articoli e l'insieme dei componenti che li costituiscono, è possibile stabilire la relazione "l'articolo X possiede il componente Y" o, viceversa, "il componente Y è posseduto dall'articolo X". Un'associazione simile si può stabilire anche tra i magazzini e i movimenti o tra la testata di una bolla e le sue righe e in generale tra tutte le tipologie di oggetti (anche di oggetti con se stessi).
Le relazioni sono alla base di ogni ragionamento umano e la loro articolazione genera conoscenza.

E' possibile classificare diversi tipi di relazione con cui si può interrogare e organizzare il reale : 
 - relazioni di appartenenza e di possesso
 - relazioni di confronto (per quantità, qualità, forma...)
 - relazioni di causa - effetto
 - relazioni di scopo - fine
 - relazioni di luogo (stato in, moto a/da/per)
 - relazioni di tempo (sequenzialità di un evento...)
 - relazioni di affinità
 - relazioni di ereditarietà - provenienza

Poichè il ragionamento si esprime attraverso un linguaggio, esiste un corrispettivo linguistico delle relazioni che è costituito dalla "proposizione", componente elementare del discorso.
Ogni proposizione è caratterizzata da almeno tre elementi : 
 * il soggetto, che è un elemento del primo insieme,
 * il complemento, che è un elemento del secondo insieme
 * il verbo che qualifica il tipo di relazione.

Il verbo è determinante per caratterizzare e qualificare il tipo di relazione (ad ognuno si può quindi far corrispodere un tipo di verbo).

# Relazioni inverse e Operatori
Per ogni relazione e quindi anche per ogni funzione può esistere una relazione / funzione inversa, generalmente espressa con il verbo in forma passiva ("L'articolo X possiede il componente" Y--> "Y è posseduto da X"), ma non necessariamente. Ad esempio, la relazione "Tizio è padre di Caio" ha come inversa "Caio è figlio di Tizio".
In ogni caso il tipo verbo di una relazione e della sua inversa non cambia.

Le relazioni su una stessa coppia di insiemi possono a loro volta essere viste come insiemi su cui è possibile costruire altre relazioni.
Le __relazioni di relazioni__ sono dette __Operatori__.
Ad esempio l'operatore di implicazione "-->"  o quelle di equivalenza logica "<->" agiscono su proposizioni e dunque su relazioni P(X) --> Q(x)
Gli operatori logici AND OR sono pure relazioni, che associano ad una coppia di proposizioni un'unica proposizione
Cosa simile fa l'operatore logico NOT, che, concatenando implicazioni e operatori logici ottiene i ragionamenti : 
(P(X) --> Q(x)   AND Q(x) --> R(x) ) --> P(X)-->R(x)

Il discorso si articolerebbe ulteriormente, ma ciò che vogliamo evidenziare è che uno strumento informatico, che consente di manipolare relazioni significative tra insiemi e costruire ragionamenti tramite operatori, costituisce un potente mezzo di indagine.

# Modelli dinamici e relazioni
Creare un modello dinamico significa costruire un'architettura descrittiva di relazioni significative tra oggetti applicativi che possa essere ricostruita ogni volta in tempo reale e interrogata in maniera veloce e ricorsiva.
Concretamente, una volta stabilito l'ambiente e le relazioni significative, si tratta di archiviare su file le proposizioni che le descrivono, separando su colonne diverse le componenti logiche del discorso :  Soggetto, Verbo e complemento.
La potenzialità enorme di questa tecnologia sta, oltre che nella sua semplicità, nel fatto che queste tre componenti cioè soggetto verbo e complemento come visto sopra, sono le componenti elementari di qualsiasi discorso umano e di qualsiasi logica ed esprimono l'ingranaggio elementare di ogni processo mentale.
Si potrebbe in sintesi vedere il modello dinamico come una sovrastruttura o meta-struttura dell'applicativo che ne descrive le principali relazioni.
