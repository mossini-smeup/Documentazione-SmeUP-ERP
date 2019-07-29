# Obiettivo
Interfacciare le voci dei menù smeup.

# Funzioni e metodi
* " " Controllo/Decodifica di una singola voce
* "SCA" Scansione delle Voci di un Menù
** "POS" Posizionamento
** "LET" Lettura
* "SCA_OGG" Scansione delle Voci del Menù di un Oggetto
** "POS" Posizionamento
** "LET" Lettura
* "CLR" Pulizia Memoria

**NOTA BENE**
Le differenze fra la funzione SCA e SCA_OGG sono le seguenti : 
* la funzione SCA si basa sul parametro di input "parametro" (£IMEI_VP), corrispondente all'oggetto MP (si veda /COPY £IMP)
* la funzione SCA_OGG si basa invece sui parametri di input Tipo/Codice Oggetto (£IMEI_TP/CD) per i quali il parametro delle voci di menù viene poi derivato (si veda funzione RIT della £IMP)

Questa differenza è importante anche per le voci, in quanto le voci di un certo oggetto potrebbero essere presenti o meno a seconda di certe caratteristiche dell'istanza e per tale motivo il loro reperimento è legato alla particolare istanza (si veda ad esempio il caso dell'azioni legate alla B£H di un oggetto).

# Altri Parametri di Input
* £IMEI_VP :  Parametro Voce
* £IMEI_VO :  Codice Voce
* £IMEI_TP :  Tipo Oggetto di Riferimento (Utilizzato dalla Funzione SCA_OGG)
* £IMEI_CD :  Codice Oggetto di Riferimento (Utilizzato dalla Funzione SCA_OGG)
* £IMEI_CV :  Check validità, vengono tornate solo le voci valide ed autorizzate all'utente di riferimento
* £IMEI_UT :  Indica l'utente di riferimento per il controllo dell'autorizzazione alle voci quando è attivo anche il Check di validità. Se non è passato viene assunto l'utente di job.
* £IMEI_RF :  Forza il ricalcolo di eventuali dati memorizzati nell'interfaccia ai fini del miglioramento delle performance

# Campi di Output

* £IMEO_VP :  Parametro Voce di menù (Oggetto MP)
* £IMEO_TM :  Tipo Oggetto di Riferimento del Menù :  se il menù è il menù di riferimento di un un oggetto viene in questo campo riportata la classe di tale oggetto es. M_B£BASE => TAB£AMO
* £IMEO_CM :  Codice Oggetto di Riferimento del Menù :  se il menù è il menù di riferimento di un un oggetto viene in questo campo riportata l'istanza di tale oggetto es. M_B£BASE => B£BASE
* £IMEI_CO :  Codice per Criterio di Ordinamento (per voci da MEA è dato dal campo ordinamento concatenato al codice dell'elemento, per tutte le altre è l'elemento stesso)
* £IMEI_VO :  Codice Voce di menù
* £IMEI_DE :  Descrizione Voce di Menù
* £IMEO_TR :  Tipo Oggetto di Riferimento della Voce di menù :  se l'azione del menù richiama una funzione che può essere ricollegata ad un'altro oggetto di smeup in questo campo viene ritornato il tipo oggetto di riferimento di tale oggetto. Tale ha particolare importanza ai fini del controllo delle autorizzazioni sulla voce. Es. una voce che richiama il sottosettore X1 della MEA riporterà in tale campo il valore SSMEA (o TAB£A se viene creata l'applicazione X1)
* £IMEO_CR :  Codice Oggetto di Riferimento della Voce di menù :  se l'azione del menù richiama una funzione che può essere ricollegata ad un'altro oggetto di smeup in questo campo viene ritornato il codice oggetto di riferimento di tale oggetto. Tale ha particolare importanza ai fini del controllo delle autorizzazioni sulla voce. Es. una voce che richiama il sottosettore X1 della MEA riporterà in tale campo il valore X1.
* £IMEO_LV :  Indica il livello di annidamento della voce nel menù
* £IMEO_UL :  Indica lo user level di riferimento della voce di menù :  se NON viene passato il controllo delle autorizzazioni, questo campo viene riempito solo con lo userlevel specificatamente indicato per la voce di menù, altrimenti per la sua valorizzazione vengono presi in considerazioni anche gli eventuali oggetti di riferimento collegat :  es. se una voce richiama il menù dell'applicazione A£ quando è attivo il controlle delle autorizzazioni per questo campo viene presa in considerazione anche lo userl level dell'applicazione.
* £IMEO_UI :  Solo per gli elementi della MEA viene riportato il campo T$MEAN
* £IMEO_TI :  Se valorizzato indica che la voce è un titolo
* £IMEO_AU :  In questo campo vengono riportati i riferimenti da prendenre in considerazione per il controllo delle autorizzazioni sulla voce. Questa stringa viene utilizzata ad esempio per la memorizzazione ed il successivo controllo delle voci aggiunte ai preferiti (si veda il pgm B£SER_88)
* £IMEO_OR :  In questo singolo campo viene ritornato il tipo oggetto (primi 12 caratteri) ed il codice oggetto (caratteri successivi ai primi 12) dell'oggetto che sta alla fonte della voce ( può essere ad esempio, una tabella o un programma)
* £IMEO_NA :  Voce non autorizzabile tramite classe MNU :  questo campo indica che la voce non può essere autorizzata/disautorizzata tramite la classe MNU (per vari motivi :  c'è già un'altra classe di riferimento, la voce deve essere presente o meno secondo logiche che non possono essere prefissate, come ad esempio può essere per le azioni generate dal motore del workflow).
* £IMEO_AO :  Qualora alla voce sia collegati degli oggetti (es. la voce richiama il menù di un'applicazione o di un modulo) in questo campo viene riportato il livello massimo di autorizzazione di tali oggetti per la classe OGG.MAS.
* £IMEO_MS :  Codice messaggio ritorno
* £IMEO_FI :  File messaggio ritorno
* £IMEO_35 :  Se On = Codice errato
* £IMEO_36 :  Se On = eseguita ricerca alfabetica


