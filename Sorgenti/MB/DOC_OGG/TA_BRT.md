# BRT - Tipo ciclo
 :  : DEC T(ST) K(BRT)
## CONTENUTO DEI CAMPI
 :  : FLD T$KYC1 **Significato/Parametro codice**
Indica l'oggetto (tipo e parametro) intestatario del ciclo di lavorazione.
 :  : FLD T$PAR1.T$KYC1
 :  : FLD T$BRTT **Tipo derivazione**
È un altro elemento di questa tabella BRT. Se codificato, indica da quale tipo ciclo verranno derivate le informazioni.
 :  : FLD T$BRTA **Cicli alternativi (P/S)**
Definisce il modo in cui il codice ciclo entra nella sequenza delle fasi del ciclo.
Questo campo assume i seguenti valori : 
P =  Il codice ciclo è un prefisso delle operazioni, quindi un'operazione appartiene ad un solo ciclo.
     _9_Esempio : 
     Articolo Cod. ciclo Operazione Ecc.
     ART1     001              0010
              ,,               0020
              ,,               0025
              002              0010
              ,,               0015
              ,,               0020


S =  Il codice ciclo è un suffisso delle operazioni, quindi un'operazione appartiene a più cicli, da quello iniziale a quello finale (uno o entrambi possono essere assenti).
     Esempio : 
     Articolo Operazione Cod.Ciclo iniz. Cod. Ciclo finale
     ART1     0010
              0015            002
              0020            002                 004
              0025                                003
              0030            003                 003

    In questo esempio : 
    -    l'operazione 0010 è valida per tutti i cicli
    -         ,,      0015 è valida a partire dal ciclo 002 in poi
    -         ,,      0020 è valida dal ciclo 002 al ciclo 004
    -         ,,      0025 è valida fino al ciclo 003
    -         ,,      0030 è valida solo per il ciclo 003
 :  : FLD T$BRTF **Gruppo ciclo autonomo**
Se valorizzato ed il codice non ha un gruppo ciclo proprio, non viene assunto il gruppo distinta, come avviene di default.
 :  : FLD T$KYC2 **Tipo/Parametro risorsa**
Indica l'oggetto (tipo e parametro) in cui vengono eseguite le operazioni di questo tipo ciclo.
 :  : FLD T$PAR2.T$KYC2
 :  : FLD T$BRTS **Sequenza  O=Obbl/F=Fac**
Indica se si vuole attivare la gestione della sequenza.
     'F' =     Facoltativa (Accetta anche sequenza bianca)
     'O' =     Obbligatoria
     ' ' =     Non Presentata
 :  : FLD T$BRTX **Forza ciclo gruppo**
Se impostato ed il codice ha un gruppo ciclo (sia questo un gruppo ciclo proprio o un gruppo ciclo ereditato dal gruppo distinta,vedi campo T$BRTF Gruppo ciclo autonomo), verrà utilizzato SEMPRE il ciclo associato al gruppo, anche se l'articolo stesso dovesse avere un ciclo proprio.
N.B. Il comportamento standard della routine di scansione del ciclo prevede di utilizzare il ciclo proprio dell'articolo, quando questo è presente, anche nel caso in cui sia presente il gruppo ciclo. Questo campo forza la routine di scansione a considerare in ogni caso il ciclo del gruppo.
 :  : FLD T$BRTG **Ambiente ciclo**
È un elemento della tabella *CN/AA :  se impostato, questo ambiente si sovrappone all'ambiente originale definito nella tabella di impostazioni (B£1) per la scansione del ciclo. In questo modo si possono codificare i cicli su diversi ambienti.
Può essere utile, ad esempio, definire ambienti 'proprietari' (X1/X9), con cui scandire il ciclo delle risorse critiche, ottenuto realizzando l'opportuno programma di interfaccia. Questo programma reperisce le informazioni in modo totalmente eterogeneo (ad esempio sui parametri dell'oggetto, sui legami, su archivi personali) e le restituisce normalizzate alle funzioni che eseguono la scansione del ciclo.
**Nota tecnica**
La ridirezione dell'ambiente nello standard è eseguita nel programma di scansione dell'ambiente SM :  B£ICIR_SM. Se si vuol eseguire una ridirezione a partire da un altro ambiente occorre modificare il programma di scansione prendendo come esempio quanto fatto in quel programma.
La deviazione non viene eseguita se l'ambiente di deviazione è lo stesso dell'ambiente chiamante. Viene inoltre eseguita allo stesso livello del programma chiamante :  ad esempio B£ICIR_SMA, se deviato su X1, lancia il programma B£ICIR_X1A. In questo modo ci si protegge dalle ricorsioni. Si devono però realizzare tante copie del programma di deviazione quante previste nel programma di duplicazione (B£DP01).
 :  : FLD T$BRTI **Significato della sequenza**
Si può inserire un'intestazione per descrivere in modo libero la sequenza delle operazioni.
 :  : FLD T$BRTH **Pgm aggiustamento**
Se impostato un valore x, nelle esplosioni di produzione verrà lanciato il programma B£ICIR_x, prima e dopo il controllo di configurazione. Con esso si potrà sia escludere la riga di ciclo, sia variarne i campi. Il risultato è avere un criterio di configurazione 'implicito' su tutte le righe del tipo ciclo.
 :  : FLD T$BRTD **Derivazione sequenza**
È un elemento di questa stessa tabella BRT; se codificato, indica da quale tipo ciclo si deriva la sequenza.
 :  : FLD T$BRTL **Lunghezza codice**
Si indica la lunghezza massima del codice a cui è intestato il ciclo :  ad esempio, se il tipo ciclo è una sequenza (ed avrà quindi derivazioni), la lunghezza massima è 6 (lunghezza della sequenza).
 :  : FLD T$BRTW **Posizione ciclo in configurazione**
Se questo campo viene impostato, nella scansione del ciclo logistico (operazioni e materiali) il codice del ciclo verrà inserito nella configurazione con cui si scandirà la distinta base, a partire dalla posizione qui digitata, in modo che i materiali possano essere condizionati dal ciclo selezionato.
È necessario ricordare che la scansione logistica viene utilizzata per la costruzione degli impegni materiali di un ordine di produzione :  essi potranno quindi variare in funzione del ciclo impostato nella testata dell'ordine stesso.
 :  : FLD T$BRTO **Tipo controllo testata ciclo**
     1= è attivata la gestione delle testate dei cicli.
        Se il ciclo alternativo è 'P', deve esistere in testata.
        Se il ciclo alternativo è 'S', deve esistere in testata se non lasciato in bianco.
     2= il codice ciclo è valido se è un codice assegnato all'articolo "**". Tale tecnica è
        utilizzata se si vogliono distinguere, ad esempio, solo il ciclo base e il ciclo esterno
        oppure un ciclo non più valido per i costi, per tutti gli articoli
 :  : FLD T$BRTB **Tipo Operazione proposta**
È un elemento della tabella BRD; se codificato, in immissione della riga, viene proposto (se assenti sia il valore di copia sia il valore di derivazione).
 :  : FLD T$BRTC **Obbligatoria risorsa**
Se valorizzato la risorsa è obbligatoria.
 :  : FLD T$BRTU **Tempi facoltativi**
Se valorizzato, i 10 tempi che caratterizzano ogni riga del ciclo sono facoltativi, indipendentemente da quanto impostato nella tabella tipo operazione. In questo modo è così possibile, ad esempio, differenziare il controllo tra cicli base, in cui si codificano le operazioni (in cui è verosimile che i tempi non siano significativi) e i cicli tecnici di articolo, in cui l'obbligatorietà è guidata dai campi del tipo operazione, mantenendo il medesimo tipo operazione.
 :  : FLD T$BRTE **Obbligatoria derivazione**
Se valorizzato, il codice di derivazione è obbligatorio :  è significativo se presente il tipo derivazione.
 :  : FLD T$BRTP **Stato principale per scansione**
È un elemento della tabella B£W/CI :  se presente viene assunto nell'esplosione di produzione, se non specificato uno stato diverso.
 :  : FLD T$BRTQ **Contenitore note di testata**
È un elemento della tabella NSC :  definisce il contenitore delle note legate alle testate dei cicli di questo tipo.
 :  : FLD T$BRTR **Stato di nascita**
È un elemento della tabella B£W/CI :  se presente viene proposto all'atto dell'immissione delle righe.
 :  : FLD T$BRTM **Suff.pgm contro**
Se impostato un valore x, in gestione del dettaglio dell'operazione, viene chiamato il programma BRCI15D_x, attraverso il quale è possibile effettuare dei controlli specifici.
Questo programma è richiamato dal dettaglio (BRCI15D) in due punti : 
- dopo aver eseguito i controllii normali (con funzione CTR)
- prima di eseguire l'inserimento, la variazione, o l'annullamento sull'archivio effettivo (con funzione AGG).
In questo secondo caso, dato che viene passata la DS dell'archivio, è possibile modificarla.
E' inoltre possibile, dato che è nota l'azione (inserimento, variazione, annullamento, in base allo stato degli indicatori, che sono tutti passati) eseguire delle azioni specifiche su altri archivi, ottenendo un comportamento simile all'esecuzione di un flusso (di inserimento, modifica o annullamento), sia pure cablato.
 :  : FLD T$BRTV **Oggetto clclo
In caso di ciclo prefisso, se si imposta in questo campo un oggetto (tipo + parametro), verrà controllato che il codice
ciclo sia un oggetto di questo tipo.
Quando si inserisce una riga di ciclo per oggetti di questo tipo viene assunto il codice ciclo uguale all'oggetto.
Inoltre non viene controllato che ne esista la testata ciclo.
Ad esempio, se si definisce un tipo ciclo
 :  : FLD T$BRTZ **Ciclo gruppo
E' significativo solo in caso di ciclo prefisso.
Se impostato, la testata ciclo viene utilizzata come gruppo ciclo, in assenza del campo omonimo in anagrafica articoli.
 :  : FLD T$BRTY **Tipo oggetto coll.
Se impostato un tipo oggetto (tramite una griglia), esso tipizza il campo "Codice Collegato" della testata ciclo.
