# C5L - Tipo registrazione analitica
 :  : DEC T(ST) K(C5L)
## OBIETTIVO
Definire le caratteristiche di una riga di registrazione di contabilità analitica.
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC Descrizione
Descrive il tipo registrazione analitica
 :  : FLD T$C5LA **Livello di nascita**
È un elemento TA/B£W00. È il livello assunto nell'inizializzazione della riga di analitica. In assenza viene assunto il livello '2'.
 :  : FLD T$C5LB **Gruppo flag**
È un elemento TA/B£Y. Definisce il gruppo di flag che viene assunto all'atto dell'inizializzazione della riga di analitica.
 :  : FLD T$C5LC **Parametri interni**
È un elemento TA/C£I. Caratterizza i campi liberi (5 alfanumerici e 5 numerici) presenti nella riga che sono a disposizione dell'utente.
 :  : FLD T$C5LD **Parametri espliciti**
È un elemento TA/C£E. Definsce la categoria parametri per aggiungere informazioni alla riga.
 :  : FLD T$C5LE **Obbligatoria quantità**
Se impostato (valore '1'), viene attivata la gestione di rilevazione delle quantità :  sarà, quindi, obbligatorio inserire anche le quantità all'inserimneto di una registrazione di analitica. Lasciandolo bianco è attiva solo la rilevazione dei valori. Se assente, viene assunto il valore a livello generale (tabella C52).
 :  : FLD T$C5LF **Unità di misura assunta**
È un elemento TA/UMS. Se impostata la gesitone quantità, è l'unità di misura che viene proposta per registrazioni di questo tipo.
 :  : FLD T$C5LG **Tipo pratica**
È un oggetto PA. Se impostato, definisce il tipo di pratica/documento assegnabile a registrazioni di questo tipo.
 :  : FLD T$C5LH **Obbligatoria pratica**
È un elemento V2/SI/NO. Se impostato, è obbligatorio impostare una pratica (del tipo definito in questa stessa tabella) all'atto dell'inserimento della registrazione.
 :  : FLD T$C5LI **Exit inizializz. MH**
È il suffisso del programma di aggiustamento dell'inizializzatore/driver dei movimenti di analitica, che innesca il richiamo del programma **C5C5D0_x** (x è il suffisso).
Tale programma viene richiamato dall'api £C5D ad ogni esecuzione in inizializzazione nuovi record o all'aggiornamento per scrittura, aggiornamento e cancellazione.
Il prototipo del programma è costituito dal sorgente C5C5D0_X.
 :  : FLD T$C5LJ **Griglia testata**
E' possibile indicare una griglia di oggetti di analitica che potranno essere imputabili sulla testata della registrazione.
Gli elementi qui indicati verranno applicati su tutte le righe di analitica che prevedono tali dimensioni, senza possibilità di modifica, salvo sia prevista anche la griglia a livello di riga contabile (in questo caso vince quanto indicato a questo livello).
NOTA BENE :  l'attivazione della griglia comporta l'utilizzo dei campi liberi T5AA03/04/05 sarà necessario assicurarsi che non siano stati utilizzzati.
 :  : FLD T$C5LK **Griglia riga**
E' possibile indicare una griglia di oggetti di analitica che potranno essere imputabili sulla riga contabile.
L'attivazione di ogni dimensione avverrà in considerazione delle dimensioni previste sul conto contabile indicato sulla riga (es. se il conto non prevede l'analitica non si attiverà nulla, se il conto prevede solo una delle dimensioni previste sulla griglia sia attiverà solo quella).
Gli elementi qui indicati verranno applicati a tutte le righe di analitica collegate alla riga senza possibilità di modifica.
NOTA BENE :  l'attivazione della griglia comporta l'utilizzo dei campi liberi R5AA03/04/05 sarà necessario assicurarsi che non siano stati utilizzzati.

