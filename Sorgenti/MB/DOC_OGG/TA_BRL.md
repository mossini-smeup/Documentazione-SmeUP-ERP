# BRL - Tipo distinta
 :  : DEC T(ST) K(BRL)
## OBIETTIVO
Identifica il tipo di distinta base che si assegna ad un assieme. Diversificando tale tipo, si possono ottenere, per lo stesso assieme, più distinte base (ad es :  distinta di produzione, distinta attrezzature, ecc..). Il valore di default è ART.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Codice**
Indica il tipo distinta.
 :  : FLD T$BRL1 **Seq.Distinta Pr. O/F**
Definisce se la sequenza di ordinamento che precede il componente è obbligatoria (O), facoltativa (F), oppure non gestita (se carattere lasciato a blanks).
 :  : FLD T$BRL2 **Seq.Distinta Su. O/F**
Definisce se la sequenza di ordinamento che segue il componente è obbligatoria (O), facoltativa (F), oppure non gestita (se carattere lasciato a blanks).
 :  : FLD T$BRL3 **Gestione Operaz. O/F**
Definisce se l'operazione d'impiego del componente del legame è obbligatoria (O), facoltativa (F), oppure non gestita (se carattere lasciato a blanks).
 :  : FLD T$BRL4 **Gestione Selez. O/F**
Definisce se il criterio di selezione nel legame è obbligatorio (O), facoltativo (F), oppure non gestito (se carattere lasciato a blanks).
 :  : FLD T$BRL5 **Ass.gestione completa**
Questo campo può assumere i seguenti valori : 
Blanks  viene presentato in forma ridotta (1 riga) 80 colonne
1. il formato di gestione a righe viene presentato in forma completa (3 righe) 80 colonne
E. il formato di gestione a righe viene presentato in forma Estese a  132 colonne per    decodificare in modo completo gli articoli
 :  : FLD T$BRLN **Contenitore note**
È un elemento della tabella NSC che definisce il contenitore in cui verranno memorizzate le note relative ai legami di questo tipo.
 :  : FLD T$BRLL **Calcolo dinamico llc (low-level-code)**
Se questo campo è valorizzato, il ricalcolo del low-level-code (livello minimo di distinta), verrà eseguito dinamicamente all'atto della memorizzazione del legame.
 :  : FLD T$BRL6 **Ammesso Coeff. Zero**
Se questo campo è valorizzato, è possibile inserire un legame di distinta con coefficiente d'impiego uguale a 0, in caso contrario sarà sempre obbligatorio specificare un valore diverso da 0.
 :  : FLD T$BRL7 **Conferma uscita**
Se questo campo è valorizzato, in caso di abbandono con il tasto F12 durante la modifica di una distinta, verrà richiesta conferma.
La conferma verrà richiesta inoltre per ogni operazione che possa comportare una perdita dei dati non memorizzati.
 :  : FLD T$BRL8 **Tipo Assieme**
Definisce il tipo oggetto dell'assieme. Questo campo è controllato dalla tabella *CNTT. Per il tipo distinta ART, questo campo viene assunto al valore AR (Articolo). L'assunzione al valore AR avviene anche nel caso in cui questo campo venga lasciato vuoto.
 :  : FLD T$BRL9 **Parametro Assieme**
Parametro associato al tipo definito nel campo precedente.
 :  : FLD T$BRLA **Tipo Componente**
Definisce il tipo oggetto del componente. Questo campo è controllato dalla tabella *CNTT. Per il tipo distinta ART, questo campo viene assunto al valore AR (Articolo). L'assunzione al valore AR avviene anche nel caso in cui questo campo venga lasciato vuoto.
 :  : FLD T$BRLB **Parametro Componente**
Parametro associato al tipo definito nel campo precedente.
 :  : FLD T$BRLM **Stato di nascita**
È un elemento della tabella B£WDB. Se inserito il legame di distinta base viene inizializzato con questo valore.
 :  : FLD T$BRLC **Tipo Fase Ciclo**
È un elemento della tabella BRT. Definisce il tipo ciclo che viene usato nella ricerca dell'operazione di impiego, nella manutenzione di distinta base. Se non inserito viene assunto 'ART'.
 :  : FLD T$BRLT **Coeff. impiego per Lotto**
Se questo campo è valorizzato ed è presente nell'assieme il lotto di riferimento, il coefficiente di impiego è riferito a quest'ultimo.
 :  : FLD T$BRLP **Stato principale per scansione**
È un elemento della tabella B£W/DB :  se presente viene assunto nell'esplosione di produzione, se non specificato uno stato diverso.
 :  : FLD T$BRLU **Pgm.aggiustamento**
Se impostato un valore x, nelle esplosioni di produzione verrà lanciato il programma B£IDIB_x, prima e dopo il controllo di configurazione. Con esso si potrà sia escludere il legame, sia variare i campi. L'effetto è di avere un criterio di configurazione 'implicito' su tutti i legami del tipo distinta.
 :  : FLD T$BRLI **Suffisso per implosione di produzione**
Se impostato, questo codice sostituirà il codice dell'ambiente dell'applicazione distinta base nell'implosione di produzione, produzione totale e in quelle che ad esse si appoggiano (riepilogata, ai prodotti finiti, ecc...).
Tramite questo ridirezionamento si potranno realizzare funzioni di implosione specifiche che tengano conto di realtà particolari, quali la configurazione per parametri, con gruppi distinta, che la normale implosione non è in grado di contemplare.
 :  : FLD T$BRLQ **Sviluppo quantità default**
Definisce il valore dello sviluppo quantità da impostare per questo tipo di distinta
 :  : FLD T$BRLO **Attributo x riepliogo**
Se impostato, le scansioni riepilogate verranno eseguite secondo questo attibuto.
Ad esempio, in una distinta di articoli, si può impostare che l'esplosione riepilogata venga eseguita in ordine di tipo articolo.
 :  : FLD T$BRLS **Salto fittizi in passaggio a configurazione**
La funzione che tratta la configurazione riceve : 
-    il legame 'fisico' della distinta
-    il codice dell'assieme che si sta esplodendo (che può essere diverso dall'assieme presente nel legame in caso di gruppo distinta)
-    la configurazione (che può essere sia ricevuta dall'esterno sia assunta dall'assieme).
Nel caso in cui l'assieme sia un fittizio, la configurazione, se assente, viene ereditata dal livello superiore.
Se impostato questo campo di tabella e se l'assieme è un fittizio, viene impostato anche nell'assieme quello del livello superiore. In questo modo la funzione che tratta la configurazione ha, tra i suoi parametri, l'assieme 'reale' del legame.
 :  : FLD T$BRLZ **Configurazione passante**
Se impostato, nelle esplosioni e implosioni di produzione totale e collegate (ai materiali di base, ai prodotti finiti, ecc..), verrà assunta a tutti i livelli la configurazione impostata all'atto della scansione. Questa modalità è da usarsi nel caso in cui la configurazione sia un oggetto di selezione comune a tutta la distinta (ad esempio il codice di commessa presente sui legami di tutti i livelli).
 :  : FLD T$BRLX **Ammesso ricircolo**
Se impostato, nella manutenzione della distinta base non viene controllato che un legame introduca un ricircolo.
NB :  il ricircolo viene controllato unicamenterisalendo i legami di distinta base
(implosione scalare). Non sono presi in considerazione nè il gruppo distinta, nè ricircoli
introdotti da variazione del codice legati alla configurazione.

Nelle funzioni di esplosione e implosione non al livello, il ramo si interrompe al verificarsi di un ricircolo.
 :  : FLD T$BRLD **Suffisso programma di controllo**
Se impostato un valore x, nella manutenzione della distinta viene eseguito il programma BRDI06D_x, in cui si possono introdurre controlli specifici, in aggiunta a quelli eseguiti dal programma standard.
 :  : FLD T$BRLE **Ambiente distinta**
È un elemento della tabella *CN/AA :  se impostato, questo ambiente si sovrappone all'ambiente originale definito nella tabella di impostazioni (B£1) per la scansione della distinta.
In questo modo si possono codificare le distinte su diversi ambienti. Può essere utile, ad esempio, definire ambienti 'proprietari' (X1/X9) con cui scandire la distinta di pianificazione, ottenuta realizzando l'opportuno programma d'interfaccia. Questo programma reperirà le informazioni in modo totalmente eterogeneo (ad esempio sui parametri dell'oggetto, sui legami, su archivi personali) e le restituirà normalizzate alle funzioni che eseguono la scansione della distinta.
_Nota tecnica_
La ridirezione dell'ambiente nello standard è eseguita nel programma di scansione dell'ambiente SM :  B£IDIB_SM. Se si vuol eseguire una ridirezione a partire da un altro ambiente occorre modificare il programma di scansione prendendo come esempio quanto fatto in quel programma.
La deviazione non viene eseguita se l'ambiente di deviazione è lo stesso dell'ambiente chiamante. Viene inoltre eseguita allo stesso livello del programma chiamante :  ad esempio B£IDIB_SMA, se deviato su X1, lancia il programma B£IDIB_X1A. In questo modo ci si protegge dalle ricorsioni. Si devono però realizzare tante copie del programma di deviazione quante previste nel programma di duplicazione (B£DP01).
 :  : FLD T$BRLH **Anche in gestione**
Consente di definire se il precedente campo ambiente distinta è significativo anche in fase di gestione e non solo in fase di scansione della distinta. Tecnicamente il programma di gestione della distinta base legge e scrive il file delle distinte base, attraverso un programma di interfaccia BRDI01W_xx, dove xx rappresenta l'ambiente distinta.
Normalmente tale valore viene letto dalla tabella B£1. Se questo campo è impostato, l'ambiente distinta (ovvero il valore di xx) viene letto dal campo precedente. Ovviamente, è necessario scrivere l'apposito programma d'interfaccia che abbia comportamenti analoghi al programma standard BRDI01W_SM.
 :  : FLD T$BRLF **Suff.pgm di aggiustamento per calcolo Low Level Code**
Se impostato un valore x, dopo il calcolo del L.L.Code, verrà lanciato il programma BRRLCA_x. Con esso si potranno indurre comportamenti speciali.
_9_Esempio di utilizzo :  nel caso di sviluppo distinta secondo un criterio di sostituzione componenti, il pgm std non sarebbe in grado di determinare il livello minimo del componente sostituente. Viceversa è in grado di determinare il L.L.C. del sostituito, per cui si potrebbe assegnare al sostituente il livello calcolato per il sostituito.
 :  : FLD T$BRLG **Suff.pgm di aggiustamento post gestione**
Se impostato un valore x, dopo aver eseguito l'aggiornamento della distinta, verrà lanciato il programma BRDI01F_x, che consente di eseguire azioni specifiche, con l'archivio distinte già aggiornato.
Utilizzando lo stesso valore, prima di aver eseguito l'aggiornamento della distinta, verrà lanciato il programma BRDI01F_Px, che consente di eseguire azioni specifiche, prima che l'archivio distinte venga aggiornato.
 :  : FLD T$BRLV **Sequenze da fittizio**
Se impostato, i componenti appartenenti ad un padre fittizio erediteranno da questo il valore dei campi sequenza.
Questo consente di mantenere la medesima sequenza di distinta con cui viene utilizzato un componente fittizio. È valido solo per esplosioni di produzione. Se impostato al valore BLANK le sequenze non verranno ereditate dal padre fittizio.
Se impostato a '1' le sequenze verranno ereditate dal padre fittizio. Se impostato al valore '2' le sequenze verranno ereditate dal padre fittizio solo se non impostate sul legame stesso
 :  : FLD T$BRL0 **Distinta speciale**
In fase di sviluppo
