# Funzioni su Autorizzazioni Oggetto

Questa api gestisce una serie di funzionalità sulle autorizzazioni per oggetto.

# Assunzioni

Se non vengono passati i campi classe ed utente vengono riportati come a seguire : 
* **Classe autorizzazione** :  OGG.MAS (Ingressi Master)
* **Utente** :  Utente del Job

Per tutti gli altri oggetti viene testata, l'autorizzazione per l'istanza, se per l'istanza, la funzione di autorizzazione recuperata è generica (cioè non c'è un'autorizzazione specifica per l'istanza o basata su una sua caratteristica), viene testata anche l'autorizzazione sull'oggetto classe. Per la classe, il parametro se presente viene verificato, solo qualora il parametro risulti obbligatorio. Es.
* Test sull'articolo A01 di tipo ART (dove il parametro è facoltativo) : 
** Se la funzione ritornata dal test sull'istanza è AR;;A01 => viene tenuta valida questa
** Se la funzione ritornata dal test sull'istanza è ** => viene testata l'autorizzazione su OG;;AR
* Test sul cliente 001 (dove il parametro è obbligatorio)
** Se la funzione ritornata dal test sull'istanza è CN;CLI;001 => viene tenuta valida questa
** Se la funzione ritornata dal test sull'istanza è ** => viene testata l'autorizzazione su OG;;CNCLI

Infine, sempre per la classe OGG.MAS su qualsiasi oggetto viene sempre testato la classe USRLVL, confrontata con il livello operativo previsto per l'oggetto. Se l'utente ha un valore inferiore tutti i livelli dell'oggetto vengono forzati al minimo. Tale user level viene reperito nei seguenti
modi : 
* Per gli oggetti TAB£A e TAB£AMO dal relativo campo di tabella
* Per tutti gli altri oggetti, in base a quanto risulta dalla /COPY £K04

# Eccezioni

* Qualora l'oggetto sia un sottosettore di MEA (cioè l'istanza di un oggetto SSMEA, tipicamente utilizzato per verificare le autorizzazioni dei menù di accesso) se il sottosettore corrisponde ad un elemento della tabella MEA la verifica della classe viene automaticamente spostata sull'applicazione.
Es. se devo testare "SS;MEA;C5", viene testato "TA;B£A;C5", viceversa se devo testare "SS;MEA;00",
viene mantenuto questo oggetto come verifica.
Rispetto a quanto citato in precedenza per effetto della particolare impostazione dei menù dell'applicazione V5 (che a differenza di tutte le altre applicazioni è suddivisa nei menù V4/V5/V6), per il sottosettore V5 questa risalita non è prevista. Quindi "SS;MEA;V5" rimane tale
e NON risale all'applicazione "TA;B£A;V5".

* Qualora l'oggetto sia di classe TAB£AMO e la classe autorizzazione sia OGG.MAS oltre alle autorizzazione per l'oggetto vengono testate anche le autorizzazioni per la corrispondente applicazione (TAB£A). Fra i due risultati viene considerato il valore più restrittivo (se il modulo è autorizzato, ma l'applicazione no, il modulo è considerato non autorizzato)
NOTA BENE :  per questo caso non viene eseguito il test sulla classe :  viene verificata l'istanza
TA;B£A;ap dell'applicazione corrispondente al modulo e l'istanza TA;B£AMO;apxxxx, ma non la classe
OG;;TAB£AMO.

# Funzioni / Metodi

* **RIT** - Ritorno livello di autorizzazione :  dato un oggetto viene ritornato il suo livello di autorizzazione. In base al metodo viene fissata l'area di verifica del livello stesso. Il risultato è un istanza dell'oggetto V2AUTOG.
** **VIS** - Visualizzazione :  viene verificato il livello di autorizzazione dell'oggetto, in merito alla sua visibilità.
*** Autorizzato :  99
*** Selezionabile :  96
*** Visibile / Non selezionabile :  93
*** Non Autorizzato :  91
** **GES** - Gestione :  viene verificato il livello di autorizzazione dell'oggetto, in merito alla gestione dell'oggetto stesso.
*** Gestione dati :  89
*** Visibilità dati :  85
*** Dati nascosti :  81
** **COL** - Dati Collegati :  viene verificato il livello di autorizzazione dell'oggetto, in merito alla gestione dei dati allegati all'oggetto.
*** Gestione note, parametri, ecc :  79
*** Visibilità note, parametri, ecc :  75
*** Note, parametri, ecc nascosti :  71
** **IMG** - Accesso Immagine :  viene determinato se si è autorizzati all'immagine dell'oggetto
*** Immagine accessibile :  69
*** Immagine non accessibile :  61
** **PRW** - Accesso Preview :  viene determinato se si è autorizzati alla preview dell'oggetto
*** Preview accessibile :  59
*** Preview non accessibile :  51
** **FLR** - Accesso Cartella :  viene determinato se si è autorizzati alla cartella dell'oggetto
*** Cartella accessibile :  49
*** Cartella non accessibile :  41
