# Nuovo

## Definizione
Il "Nuovo" permette di rendere accessibile ovunque la creazione degli oggetti più utilizzati.
Queste azioni possono inoltre definire funzioni specifiche per un contesto e definire informazioni
che sono derivate da un oggetto master utilizzate nella creazione dell'oggetto desiderato.

## Obiettivo
Permettere di simulare le funzioni di creazione di un nuovo oggetto.

## Scelta parametri
Nelle prime 2 sottoschede è possibile selezionare : 
- un contesto (facoltativo);
- un oggetto da creare.

## Simulazione
E possibile selezionare un contesto per visualizzare le azioni specifiche.
Non è un parametro obbligatorio, non selezionandone nessuno il default è B£, inoltre pur
selezionandone uno se non è stata definita un'azione specifica per il contesto
viene comunque visualizzate l'azione generica di creazione valida per qualsiasi contesto.
Selezionare infine un oggetto.

Nella parte bassa della scheda viene visualizzata la relativa funzione di creazione, infine
effettuando    un doppio click sulla funzione quest'ultima viene eseguita.

## da Oggetto Master

E' l'oggetto di riferimento nella creazione di un'altro oggetto, pertanto le azioni di creazione
di oggetti possono essere influite dall'oggetto principale.
Tipicamente premendo il tasto destro su un oggetto e cliccando su nuovo è possibile scegliere
l'oggetto da creare ereditando informazioni dall'oggetto su cui si era cliccato (master).

## Obiettivo
Permettere di simulare le funzioni di creazione di un nuovo oggetto partendo da un altro.

## Scelta parametri
Nelle prime 3 sottoschede è possibile selezionare : 
- una classe master (obbligatoria);
- un contesto (facoltativo);
- un oggetto master (facoltativo).

## Simulazione
Dalla combinazione dei 3 parametri selezionati nelle prime 3 sottoschede risultano gli oggetti
che è possibile inserire e le relative funzioni di inserimento oggetto.
E' necessario prima di tutto selezionare una classe, verranno pertanto visualizzate le azioni di
inserimento previste per la classe.
E possibile selezionare poi un contesto, per visualizzare l'azione specifica di un contesto per la
classe selezionata. Non è un parametro obbligatorio, non selezionandone nessuno il default è B£,
inoltre pur selezionandone uno se non è stata definita un'azione specifica per il contesto
viene comunque visualizzate l'azione generica di creazione valida per qualsiasi contesto.
Selezionare infine un oggetto, se non viene selezionato viene considerata solo la classe master.

Nella parte bassa della scheda vengono visualizzati a sinistra gli oggetti che è possibile creare,
cliccando su un oggetto viene visualizzata la relativa funzione di creazione, infine effettuando
un doppio click sulla funzione quest'ultima viene eseguita.

## Set'n Play

Script Standard/Nuovo
Il menù nuovo è definito nel file SCP_MNU membro B£OGGE per definire funzioni correlate tra un
oggetto ed il relativo oggetto master ed eventualmente funzioni specifiche per un contesto.
Il contesto è contenuto nella variabile &CO.CONAP.

Script Standard/da Oggetti Master
Nel membro membro B£OGGE_OG vengono invece definite le azioni di creazione di oggetti generiche,
a prescindere dall'oggetto master e contesto, pertanto visualizzate sempre al fine di facilitare
l'accessibilità alla creazione di un nuovo oggetto.

Script personali
C'è anche la possibilità di definire voci di menù personalizzate nel file SCP_MNUPER per entrambi i
membri di cui sopra.

Gestione delle voci del menù "Nuovo".
La definizione del nuovo oggetto avviene tramite C.NEW, per esempio : 
 :  : C.NEW Pos="M" Ogg="CNNOM" Txt="Account"
Per casi specifici in cui un oggetto può avere diverse funzioni di creazione si può usare  :  : C.MNU indicando la funzione specifica, come in questi 2 casi di esempio sullo
stesso oggetto E3£C1 : 
 :  : C.MNU Pos="M" Txt="Telefonata" Fun="F(EXD;*SCO;) 1(E3;£C1;) 2(MB;SCP_SCH;LOA36)
INPUT(InzDat(N§CAEV(003) N§CTEV(£F1))) P(AziExe(01) FunFin(Reload) &PA.*ALL)"
 :  : C.MNU Pos="M.A" Txt="Mail" Fun="F(EXD;*SCO;) 1(E3;£C1;) 2(MB;SCP_SCH;LOA36)
INPUT(InzDat(N§CAEV(003) N§CTEV(£F1))) P(AziExe(01) FunFin(Reload) &PA.*ALL)"

## Gestione delle azioni "Nuovo"
Le azioni sugli oggetti sono definite nel file SCP_SET nel membro B£GES0. C'è anche la possibilità
di definire azioni personalizzate nel membro B£GES0_U.
Le azioni vengono definite tramite  :  : AZI.FUN indicando Ese="01", per esempio : 
 :  : AZI.FUN Cod="RN" Ese="01" Fun="F(EXD;*SCO;) 1(RN;;) 2(MB;SCP_SCH;LOA36) P(AziExe(01))"
Eventuali parametri specifici per la creazione di un nuovo oggetto da un oggetto master possono
essere definiti tramite  :  : AZI.NEW, per esempio : 
 :  : AZI.NEW Cod="CNNOM" Inp="InzDat(R1COEN(&OG.K2))"
Dai 2 esempi di cui sopra la funzione di creazione di un oggetto RN partendo da un CNNOM sarà : 
F(EXD;*SCO;) 1(RN;;) 2(MB;SCP_SCH;LOA36) P(AziExe(01)) INPUT(InzDat(R1COEN(&OG.K2)))
dove in &OG.K2 verrà inserito il codice oggetto del CNNOM.

Nota :  per ovviare a problemi di performance le autorizzazioni sono gestite a livello di esecuzione
      della funzione, pertanto se un utente non è autorizzato alla creazione di un oggetto la voce
      di menù è visualizzata, anche se la relativa funzione non verrebbe eseguita.
