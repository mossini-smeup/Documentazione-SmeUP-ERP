# DEFINIZIONE

La lista è l'oggetto di Smeup che permette di definire un insieme omogeneo di istanze.

# MODALITA' DI DEFINIZIONE DELLE LISTE
Le liste possono essere definite in varie modalità : 
 * Tramite un elenco puntuale di elementi
 * Tramite la definizione di un filtro su elenco di oav della classe dell'oggetto
 * Tramite forme di caricamento specifiche dell'oggetto (cui corrispondono domande di composizione specifiche)
 * Tramite la composizione di cartelle di carrellli (riconoscibili fra le liste dal suffisso C/)
 * Tramite un filtro Q3 (riconoscibili fra le liste dal suffisso E/)

Fra le istanze delle liste ne sono presenti alcune che non possono essere oggetto di manutenzione nè diretta (gestione dei suoi elementi) nè indiretta (modifica delle sue caratteristiche :  ad esempio variazione del filtro Q3), in quanto il loro modo di costruirsi è definito nel loro codice.
 * La lista * esiste sempre e definisce l'insieme di tutti gli elementi della classe
 * Le liste con suffisso T/ sono liste già predisposte nello standard smeup. Esse sono codificate negli script del file SCP_SET tramite i membri aventi nome "LI" + Tipo Oggetto (+ Parametro Oggetto)
 * E' possibile costruire dei codici lista dinamici tramite l'utilizzo di codici dinamici
 ** "*%stringa"  :  definisce una lista costituita dagli elementi che iniziano con la i caratteri indicati in sostituzione della parola "stringa"
 ** "*stringa%"  :  definisce una lista costituita dagli elementi che finiscono con i caratteri indicati  in sostituzione della parola "stringa"
 ** "*%stringa%"  :  definisce una lista costituita dagli elementi che contengono i caratteri indicati in sostituzione della parola "stringa"
 ** "*stringa1;stringa2"  :  definisce una lista costituita dagli elementi suddivisi dal carattere ";"
 ** "*stringa"  :  definisce una lista costituita dal solo elemento corrispondente ai caratteri della parola "stringa"

# CLASSI D'AUTORIZZAZIONE
All'oggetto lista è applicata la classe d'autorizzazione LI, ma oltre a questa vengono considerate anche le classi d'autorizzazione specifiche del tipo di definzione della lista, nonchè la classe USRLVL che può essere attribuita a livello di fonte.

# INTERFACCIA
La /COPY di interfaccia delle liste è la £G40
 :  : DEC T(MB) P(QILEGEN) K(£G40)

