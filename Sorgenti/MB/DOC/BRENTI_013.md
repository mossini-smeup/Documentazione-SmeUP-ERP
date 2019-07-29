# Definizione

Nell'anagrafica Sme.Up è possibile introdurre la gestione di un tipo ente definibile ad un livello superiore a tutti gli altri. Tramite esso è possibile andare a gestire i dati che accomunano più enti in modo che essi possano essere modificati in modo univoco una sola volta.

Il caso tipico è relativo a tutti i dati di identificazione e contatto di un ente (ragione sociale, indirizzo, partita iva/codice fiscale, telefoni ecc.). Al di sopra degli enti clienti e fornitori viene quindi introdotto un ente "nominativo" cui clienti/fornitori risultano collegati in modo che qualsiasi modifica su uno solo dei dati marcati come campi di nominativo comporti l'allineamento di tutti i codici ad esso collegati.

La sua introduzione risulta di particolare utilità quando : 
* Avviene con una certa frequenza il fatto di avere lo stesso soggetto codificato con tipi ente differenti (es. spesso un cliente è anche fornitore e viceversa).
* Avviene con una certa frequenza il fatto di avere lo stesso soggetto codificato con codici differenti (es. perchè hanno codifici differenti a seconda dell'azienda).

# Attivazione
### Definire tipo contatto apposito (BRE/BRZ)
Dovrebbe essere un tipo contatto comune a tutte le aziende (es. NOM).

 :  : DEC T(ST) P() K(BRE) I(**Tabella BRE >>)
 :  : DEC T(ST) P() K(BRZ) I(**Tabella BRZ >>)

 * Definire tramite script i campi che vanno ripresi dal tipo ente nominativo (cfr. "Configurazione dello script").
 * Con questa funzionalità verrà automaticamente attivato anche il data entry V2, per tale motivo è necessario controllare che la sua parametrizzazione sia corretta (cfr. "Configurazione Data Entry V2 ").
 * Creare tramite apposito programma l'anagrafico dei nominativi e la loro relazione con gli enti esistenti dell'ente corrispondente). I programmi predisposti sono il BRUT04A ed il BRUT05A. Entrambi funzionano in stampa e in esecuzione. Il BRUT05A, basandosi sui record che non presentano il riferimento al nominativo, va fatto girare in esecuzione solo dopo che il BRUT04A è già girato in tale modalità.
* Considerazioni aggiuntive : 
** I dati più certi dovrebbero essere quelli dei fornitori, in quanto si ha la possibilità di verificarli sul cartaceo della fattura del fornitore.
** A parità di codice fiscale potrebbero sussistere anche due nominativi : 
*** Uno con la partita iva e uno senza partita iva.

 :  : INI  Programma di Controllo/Generazione Nominativi con riferimenti fiscali
 :  : CMD CALL BRUT04A
 :  : FIN
 :  : INI  Programma di Controllo/Generazione Nominativi senza riferimenti fiscali
 :  : CMD CALL BRUT05A
 :  : FIN

### Attivare la gestione a nominativi sui tipi contatti interessati (tabella BRE)
 :  : DEC T(ST) P() K(BRE) I(**Tabella BRE >>)

Sulla tabella BRE, oltre al campo relativo all'attivazione della gestione nominativi, è presente anche un altro importante campo da prendere in considerazione se per tipo contatto sono anche attivi gli scenari :  "Codice non univoco". Tramite questo campo, infatti, è possibile gestire un'anagrafica enti comune in cui i codici contatto assumono significati differenti a seconda dell'azienda (es. al nominativo di Mario Rossi è collegato il cliente 001 dell'azienda Alfa ed il cliente 103 dell'azienda Beta, mente il cliente 001 dell'azienda Beta corrisponde al nominativo di Franco Verdi ed il cliente 103 dell'azienda Beta al nominativo Alberto Bianchi). Se questo particolare campo non viene gestito viene dato per scontato che i codici per tipo siano univoci a livello di tutta l'anagrafica (e che quindi riprendendo l'esempio il codice cliente rimanga collegato).

 * Inserire il tipo contatto definito nella tabella BR2 (un nominativo viene riconosciuto come tale se corrisponde al tipo contatto indicato in tale tabella).

 :  : DEC T(ST) P() K(BR2)

# Documentazione tecnica
 * Gestione Ente Nominativo
 ** Dati Identificativi Fiscali
 *** Al di là di quale elemento della BRX vada ad indicare i controlli su tali dati verranno effettuati in modo fisso
 ** Inserimento
 *** Si ha una schermata aggiuntiva che dovrebbe permettere di evitare la duplicazione dei nominativi
 ** Modifica
 *** Alloca tutti i soggetti collegati ed alla conferma li va ad aggiornare
 ** Cancellazione
 ** Copia

 * Gestione Ente gestito a Nominativi
 ** I campi/estensioni che vengono derivati dal nominativo, definiti nell'apposito script, non possono mai essere manutenuti dall'ente derivato
 ** Dati Identificativi Fiscali
 *** I controlli al di là che i campi siano collegati al nominativo o meno verranno come attivati in funzione della tabella BRX
 ** Inserimento
 *** Viene chiesto obbligatoriamente di indicare il nominativo di riferimento, se non esiste si può creare al momento
 *** Se anche il codice ente è un campo derivato verrà automaticamente impostato come codice dell'ente il codice del nominativo
 *** I campi e le estensioni definite come da derivare dal nominativo verranno automaticamente caricate con i valori del nominativo
 *** Alloca anche il nominativo stesso in modo che nessuno possa andare a modificare i valori derivati mentre sono in manutenzione
 ** Modifica
 *** Alloca anche il nominativo stesso in modo che nessuno possa andare a modificare i valori derivati mentre sono in manutenzione
