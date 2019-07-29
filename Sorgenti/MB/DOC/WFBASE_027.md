# Presentazione

Descriviamo di seguito le modalità disponibili per rendere più flessibili i processi di workflow : 
 * Spegnimento di alcuni impegni tramite le funzioni di salto impegni.
 * Errori sull'ordine :  ordini da riportare in una situazione di consistenza, ad esempio per improprio avanzamento da parte di un utente, tramite le funzioni di annullamento attività.
 * Eccezioni di processo :  ordini che richiedono comportamenti non previsti/prevedibili dal modello iniziale di workflow.

## Salto impegni

È possibile definire alcuni impegni come "saltabili" (automaticamente oppure tramite forzatura utente).
In questo modo è possibile disegnare dei processi completi (che comprendano la maggior parte delle casistiche) e fare sì che in fase di esecuzione vengano ridotti solo al necessario.

Se un impegno viene saltato : 
 * Non viene presentato ai relativi utenti per l'esecuzione.
 * Lascia traccia nel log delle attività, scrivendo delle attività particolari di "Salto impegno".
 * Non vengono eseguite le sue conseguenze esterne.

### Salto automatico

Nello script di transizione è possibile condizionare il salto automatico tramite il flag di "Salto impegno".
Impostando il valore di tale flag ('1' per il salto) tramite un OAV dell'impegno è possibile ad esempio condizionare il processo in base a proprietà dell'oggetto su cui si sta lavorando.

### Salto forzato

Si può anche definire (tramite la tabella WFF) degli insiemi di utenti abilitati a forzare il salto su un particolare impegno, legando questa informazione tramite il flag "Forzabilità salto da parte dell'utente".
Gli utenti che hanno questa possibilità possono in ogni momento forzare il salto dell'impegno tramite pop.up dell'impegno stesso :  da Worklist, da Situazione ordine, da Rappresentazione grafica dell'ordine...
Come caso particolare, quando anche gli esecutori dell'impegno sono abilitati al salto è presente anche un bottone esplicito nella scheda dell'impegno quando è in esecuzione.

## Errori di ordine :  annullamento di attività.

L'annullamento attività su un ordine consente di riposizionarsi all'indietro sull'ordine stesso.
Attenzione :  si tratta di un semplice riposizionamento, non viene annullato nessuno degli effetti che possono essere scaturiti dall'avanzamento (es. invio mail, cambi di stato di oggetti di Sme.up, ...); questi, se necessario e possibile, vanno annullati a mano!
Per motivi di consistenza se si annulla un'attività vengono annullate automaticamente tutte le attività successive; lo stato dell'ordine viene automaticamente ricostruito sulla base della nuova "storia" (tutte le attività fino alla prima annullata esclusa).

### Annullamento da utente qualsiasi

Un'attività è annullabile da parte di un utente se : 
 * L'attività è stata eseguita dall'utente;
 * L'attività è annullabile;
 * Tutte le attività successive sono annullabili.

Un'attività è annullabile se : 
 * È stata eseguita dall'utente;
 * Se attività di PRC/DIC è previsto (tramite opportuno flag) che sia annullabile;
 * Se attività di assegnazione o riassegnazione è sempre annullabile.
 * Se attività automatica è sempre annullabile.

Un utente può fare cominciare l'annullamento solo dalle attività che ha eseguito.

L'annullamento utente può essere eseguito, quando consentito dalle regole appena esposte : 
 * Dalla scheda di un impegno in esecuzione, in basso a destra (ad esempio per annullare una presa in carico);
 * Dalla sottoscheda "Attività" della scheda utente di workflow;
 * Dalla sotto-scheda "Log attività" della scheda di un ordine di workflow.

### Annullamento da utente master

L'annullamento dalla sottoscheda "Gestione master" della scheda di un ordine è sempre abilitato per tutti gli utenti master.
In questo caso non vengono effettuati controlli sull'annullabilità delle attività, lasciando alla discrezione dell'utente master la valutazione dell'opportunità di effettuare l'annullamento.

Attenzione :  l'annullamento di attività su ordini in modalità libera non è testato!

## Gestione delle eccezioni di processo

### Impegni extra-rete
Per determinati impegni, in punti particolarmente complessi, variabili o non chiari di un processo, si può prevedere la possibilità di generare impegni extra-rete, per alimentare le worklist di altri utenti con impegni non previsti in fase di modellazione del processo.
Questo offre come benefici, se non l'automatizzazione di certe azioni o il controllo stretto del processo da parte del motore di workflow, il log di TUTTE le attività svolte e tutti i vantaggi di comunicazione dati dall'utilizzo di impegni di workflow.

### Modalità libera
Per ordini "anomali", ovvero nei quali la sequenza delle operazioni non rispetta l'insieme di casistiche previsto in fase di modellazione del processo, una soluzione consiste nello "sblocco" dell'ordine in modalità libera.
Nell'ordine : 
 * Un utente master (O2 sulla classe WFORTE per il processo) può sbloccare l'ordine dalla sottoscheda "Gestione master" della scheda dell'ordine (operazione NON REVERSIBILE!).
 * Da quel momento gli impegni non vengono più attivati dal motore di workflow, ma da esso resi eventualmente "attivabili" (solo come segnalazione) :  dalla stessa scheda di sblocco si può attivare/disattivare gli impegni al momento opportuno con un doppio click.

