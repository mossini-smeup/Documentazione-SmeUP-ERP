# Introduzione
Con l'introduzione dell'assoggettamento IVA al 21% può nascere in smeup una problematica dovuta al fatto di aver fissato un'aliquota al 20% all'interno di uno o più elementi della tabella V5S.

La continuazione della lettura del seguente documento risulta necessaria solo se tale casistica rientra nelle parametrizzazioni del proprio sistema.

# Termini del problema
Esistono sostanzialmente due modi per attribuire una voce di spesa (elemento di V5S) ad un documento e queste due modalità possono coesistere in un' installazione di smeup.

* Scrivendolo direttamente il codice spesa V5S sul documento
* Attribuendo dinamicamente il codice spesa al documento.
In entrambi i casi il cambio dell'aliquota da applicare alla spesa (all'interno della tabella V5S) impatta su tutti i documenti esistenti se l'aliquota  al 20 è stata appunto fissata all'interno dell'elemento della V5S . Di seguito descriviamo come intervenire per la sistemazione di questo problema.

CASO 1 : 
Innanzitutto verificare se questo caso si presenta nella propria installazione di Smeup. Per farlo occorre controllare se sono valorizzati i campi T§SPIM, T§SPTR, T§SPBO, T§SPIN  dell'archivio testate documenti (V5TDOC0F) con elementi della V5S che hanno fissato un assoggettametno ad aliquota 20.  Se l'intervento si rende necessario si consiglia di procedere in questo modo : 
* Creare dei nuovi elementi della V5S che corrispondano ai vecchi, mantenendo per essi l'assoggettamento al 20%, e tenendo traccia della corrispondenza fra di essi.
* Attribuire l'assoggettamento 21% ai vecchi elementi.
* Applicare un aggiornamento delle testate di documento che devono mantenere l'assoggettamento al 20% sostituendo i vecchi codici con i nuovi codici V5S appena creati.

CASO 2 : 
Innanzitutto verificare se questo caso si presenta nella propria installazione di Smeup. Per farlo occorre : 
* Controllare gli elementi delle tabelle V5D e l'elemento della tabella V51. Sulla tabella V5D verificare se sono utilizzati elementi di V5S nei campi Maggiorazione/Sconti (Ma/Sc 1,2,3,4,5) aventi fissato un assoggettamento al 20.
* In tabella V51 verificare se sono valorizzati i campi "Cod.sconto finanz." e/o "Cod.spese di incasso" sempre con assoggettamento al 20.

Se l'intervento si rende necessario si consiglia di procedere apportando al pgm V5V5F0 nella routine CALSPE una personalizzazione, tale per cui, la sostituzione degli assoggettamenti IVA  20/21 venga applicata direttamente dal pgm sulla base della data del documento in oggetto.

# Considerazioni finali
Nel prossimo futuro ci si propone di predisporre una soluzione più idonea, che a causa del breve tempo a disposizione non è stato possibile realizzare.

Si rende noto che questi interventi potrebbero anche non essere applicati qualora si ritenga che l'incongruenza dei calcoli dell'imposta in cui si incorrerebbe sui documenti non abbia rilevanza o che, viceversa, all'evenienza si ritenga sufficiente intervenire manualmente sulla V5S in modo da riportarla al 20 solo per il tempo strettamente necessario.

Di seguito infine viene riportato un esempio delle specifiche che si possono applicare al V5V5F0 per risolvere in caso. In questo esempio ci si aspetta che sulle tabelle V5S sia stato indicato l'assoggettamento al 21, che viene poi sostituito in base alla data con l'assoggettamento al 20 : 

>
C     T$V5SH        IFNE      *BLANK
C                   MOVEL(P)  T$V5SH        £RITEL
V* I PER IVA
V* . Verifico in base alle data se possa essere necessario applicare
V*   la forzatura dell'iva al 20%
C                   CLEAR                   XF20              1
C                   SELECT
V* . _1_ NOTA BENE :  qui vanno eventualmente introdotte le considerazioni specifiche per determinare la data di riferimento valida per le note di accredito (va recuperata la data di riferimento della fattura cui la nota si riferisce)
C                   WHEN      T§DBOL<>0
C                   IF        T§DBOL<20110917
C                   EVAL      XF20='1'
C                   ENDIF
C                   WHEN      T§DFAT<>0
C                   IF        T§DFAT<20110917
C                   EVAL      XF20='1'
C                   ENDIF
C                   OTHER
V* . _1_ NOTA BENE :  in questo caso vanno fatte le dovute considerazioni (es. per la stampa conferma d'ordine si potrebbe valutare di lasciare sempre al 21%) 
C                   IF        T§DTDO<20110917
C                   EVAL      XF20='1'
C                   ENDIF
C                   ENDSL
V* . In caso affermativo applico tabella di trascodifica dei codici 21 in 20
C                   IF        XF20='1'
C                   SELECT
C                   WHEN      £RITEL='21'
C                   EVAL      £RITEL='20'
 V* . => se ci sono altri codici qui vanno aggiunti
C                   ENDSL
C                   ENDIF
V* F PER PIVA




