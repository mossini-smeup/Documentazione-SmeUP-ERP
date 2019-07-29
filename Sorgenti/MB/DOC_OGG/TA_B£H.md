# B£H - Gruppi di azioni di tab B£J
 :  : DEC T(ST) K(B£H)
## OBIETTIVO
Ogni elemento di questa tabella specifica un gruppo di azioni (definito negli elementi presenti in un sottosettore della tabella B£J) che devono essere viste oppure eseguite dall'utilizzatore insieme o in sequenza.
Possiamo avere ad esempio : 
-    Azioni di ricevimento materiali da conto lavoro :  si tratta di una sequenza di azioni che vengono eseguite in successione
-    Azioni di sviluppo del budget :  si tratta di una sequenza di azioni che possono essere lanciate individualmente
-    Azioni, associate ad un oggetto (es. articolo) che l'utente può lanciare dal menù contenstuale delle azioni per oggetto :  si tratta in questo caso di una lista di azioni che vengono presentate (es. lista azioni per aticolo che mostra :  l'esplosione distinta base, l'analisi disponibilità, i dati articolo / magazzino, i parametri di pianificazione, ecc..)
-    Azioni di creazione di un cliente :  si tratta di una sequenza di azioni che si sviluppano all'inserimento di un nuovo codice cliente
-    Ecc.
La composizione della tabella dipende dal tipo di flusso che si sta impostando.
I tipi di flussi sono : 
-    __Flusso batch__, lanciato dai programmi B£GFP10/B£GFP15.
Questo flusso, a differenza dei successivi, non lancia programmi funizzati, ma con un numero di parametri che può equivalere a 0, 1 o 2 (la lunghezza dei parametri è di 15 caratteri).
-    __Flusso avanzato__, lanciato da £FUN01, che ritorna il prossimo passo da eseguire, fino all'esaurimento dei passi (con possibilità di selezionare i soli passi obbligatori). Il lancio effettivo del passo viene compiuto dalla £FUN02.
-    __Flusso di collegamento__, lanciato da B£FUNG, all'atto dell'inserimento/variazione/annullamento/collegamento di un oggetto, con passi eseguiti in modo sequenziale.
-    __Flusso di scelta__, lanciato da B£FUNG :  viene proposta una lista di passi elementari tra i quali l'utente sceglie quello da eseguire.
-    __Flusso di esecuzione__, lanciato da B£AR30.
## CONTENUTO DEI CAMPI
 :  : FLD T$SB£J **Sottosettore azioni**
Indica da quale sottosettore della tabella B£J si devono prendere le azioni da eseguire.
 :  : FLD T$TIAZ **Tipo flusso**
E' significativo nel caso di flusso batch
. Batch - presenta una finestra di scelta con F6+F11.
. Interattivo - lancia subito le azioni scelte.
. Selezione - lancia solo la prima tra le azioni scelte.
 :  : FLD T$L,1 **Limite / Azione**
Elenco di azioni che devono essere applicate durante il flusso. È possibile specificare fino ad un massimo di 5 azioni, oppure mettendo un prefisso che ne specifica il gruppo, si possono identificare tutte le azioni con lo stesso prefisso.
_9_Esempio  : 
- D5*             esegue tutte le azioni con prefisso D5
- FA010          esegue l'azione specifica
 :  : FLD T$B£HA **Programma di abbandono Flusso**
Indica il nome del programma che dev'essere applicato quando il flusso non viene completato correttamente. Ad esempio nei flussi delle spedizioni, se l'utente esegue delle operazioni che non vengono completate (non seleziona nessuna riga da spedire), il programma in questione (V5AT11R) si preoccupa di ripristinare la situazione precedente.
 :  : FLD T$B£HB **Azione d'Impostazione (solo per applicazioni D5 e MP)**
Permette di impostare in automatico il calcolo del : 
-  PERIODO         per il modulo D5
-  PIANO              per il modulo MP
Se è blanks, chiede il Periodo o il Piano obbligatorio, altrimenti l'azione impostata (è un elemento della tabella B£J) fa partire il programma specifico di calcolo del periodo/piano indicato nell'elemento di tabella.
 :  : FLD T$B£HP **Autorizzazione**
Se diverso da ' ' indica che per questo gruppo di azioni si vuole attivare il controllo delle autorizzazioni. Abbiamo i casi seguenti : 

- 1 = Salta; le azioni non autorizzate non vengono presentate nella lista di selezione
- 2 = Inibisci; le azioni non autorizzate vengono presentate nella lista di selezione (Es. lista ottenuta dal menù contestuale di un oggetto) ma non possono essere scelte dall'utente non autorizzato.

La CLASSE di autorizzazione utilizzata è "TABB£J" e la funzione è pari all'elemento di B£H.
Ogni azione (B£J) appartiene ad un gruppo di protezione come specificato nella documentazione
della tabella B£J.
 :  : FLD T$B£HC **Categoria del flusso**
Permette di classificare i flussi secondo dei valori fissi V2 di SME_up. Tale categoria è utilizzata in alcuni programmi per ricercare e controllare se il flusso è sensato nel contesto.
Abbiamo ad esempio le seguenti categorie : 
-    Flussi OBJ, sono quelli connessi alla creazione/cancellazione ecc. di un oggetto
-    Flussi MPS, sono quelli di esecuzione batch di elaborazioni MPS
-    Flussi AD5, sono quelli di esecuzione di elaborazioni connesse all'applicazione D5
 :  : FLD T$B£HD **Non presenta fine flusso**
È un elemento V2 SI/NO :  è significativo nel caso di un flusso avanzato. Se lo si imposta, al termine del flusso non viene presentata la finestra di fine flusso. Va tenuto presente che così facendo si toglie la possibilità di eseguire, a fine flusso, azioni ripetibili o non obbligatorie.
 :  : FLD T$B£HE **Selezione applicabilità flusso**
Rappresenta il criterio di applicabilità del flusso a determinati contesti di elaborazione, mediante il quale i programmi di lancio dell'elaborazione ne controllano la congruenza con il contesto, permettendo la scelta quando i criteri coincidono.
Attualmente è applicabile ai seguenti contesti : 
 __MPS Esecuzione flusso azioni (MPAP00G)__
Può essere utilizzato nel caso in cui si voglia limitare l'utilizzo di elaborazioni di flussi MPS a determinati piani.
Il criterio di selezione di confronto è specificato sulla tabella MPP (Piano).

 :  : FLD T$B£HG **Exit di controllo delle azioni utente**
Attraverso questo campo è possibile indicare un pgm di exit, avente per codice  B£FUN1_xx. Questo pgm verrà richiamato per il controllo delle azioni utente (flussi oggetto A-) e per suo tramite sarà possibile escludere eventuali azioni condizionandole a caratteristiche d'ambiente, dell'utente o dell'istanza stessa.

Si veda il sorgente di esempio B£FUN1_ES.

