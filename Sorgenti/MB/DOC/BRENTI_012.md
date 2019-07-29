# Definizione
La gestione multiazienda/scenario permettere di gestire un anagrafico contatti multiaziendale e contestualizzato, in modo da poter avere soggetti validi per un certo contesto/azienda e non per altri, e di ottimizzare la gestione dei dati comuni, con l'opportunità di poter gestire contiguamente i dati contestualizzati.

L'attivazione della gestione dello scenario avviene a livello di tipo contatto, tramite la tabella BRE. Possono perciò coesistere tipi contatto contestualizzati (es. clienti, fornitori) e tipi contatto decontestualizzati (es. banche).

La codifica degli scenari possibili è anch'essa definita a livello di tipo contatto, indicando il sottosettore della tabella BRG che elenca tali codici. Tale codifica è libera, ma deve seguire una struttura precisa predefinita già dal flag di attivazione della tabella BRE.

Nello specifico il codice scenario può assumere le seguenti configurazioni : 
1. lo scenario è l'azienda (perciò i codici della BRG corrispondo ai codici azienda).
2. lo scenario è l'azienda + più un'altra informazione di contesto (es. linea o filiale, perciò i codici della BRG corrispondono ai codici azienda + quest'altra informazione di contesto).
3. lo scenario può essere una delle due possibilità precedenti.

Quando è attivata la gestione degli scenari l'interfaccia dei contatti è in grado sia di recepire lo scenario di riferimento che di risalire a quello da utilizzare nel caso questo non venga direttamente passato.

Attualmente a standard è completamente recepita la prima configurazione mentre la altre comportano la gestione di apposite exit, nell'interfaccia per la gestione delle risalite (indicata nella tabella BR2) e nelle gestioni aziendali che richiedono tale specifica contestualizzazione (es. se si vuole riprendere il codice pagamento in funzione di una linea prodotto nell'inserimento di un documento, si dovrà fare in modo che nelle exit dei documenti nel richiamo dell'interfaccia venga passato il relativo scenario dato da azienda + linea).

# Attivazione scenari
Il passaggio da differenti anagrafici ad un unico anagrafico comune comporta una serie di considerazioni e di elaborazioni abbastanza complesse. Di seguito vengono spiegate quelle che dovrebbero essere le fasi di attivazione.

- Verifica ed eventuale ricodifica dei codici non univoci :  per l'attivazione degli scenari è comunque presente il vincolo per il quale uno stesso codice non può avere significati differenti per i vari scenari. Per questo va fatta un'analisi dei codici duplicati e sulla base dei risultati di questa analisi decidere come trattarli. All'attivazione finale non dovranno quindi sussistere dei duplicati.

- Definizione di un sottosettore della CRN che sia comune a tutti gli ambienti da impostare nella BR2 per avere un numeratore comune dei record (nel caso il sottosettore, BR che è il default, non lo sia già). Gli elementi sono OG.BRENTI e OG.BRESCO.
 :  : DEC T(ST) P() K(BR2)

- Definizione dei tipi contatto che andranno gestiti a scenario ed in che modo indicando il relativo flag sulla tabella BRE.
 :  : DEC T(ST) P() K(BRE)

- Con questa funzionalità verrà automaticamente attivato anche il data entry a formato esteso, per tale motivo è necessario controllare che la sua parametrizzazione sia corretta (cfr. "Configurazione Data Entry V2")

- Definizione dei codici scenario e relativi sottosettori da associare ad ogni tipo contatto. In quest'ambito è importante notare che alla definizione dei sottosettori è legata anche la configurazione dei parametri per scenario di ogni scenario. Per lo specifico si rimanda al capitolo riportato di seguito.
 :  : DEC T(ST) P() K(BRE)
 :  : DEC T(ST) P() K(BRG)

- Fusione degli anagrafici, cioè il popolamento di un unico file contenente tutti i record anagrafici dei file di partenza, con l'indicazione del relativo scenario di appartenza. A standard è fornito il programma BRUT06A, che permette di andare a fondere un file alla volta con la possibilità di utilizzare come scenario l'azienda di origine. Tale azienda verrà impostata come scenario per i soli tipi contatto che nella tabella BRE prevedono la gestione a scenari. Per tutti gli altri il campo scenario rimarrà blank.
 :  : INI Programma di fusione degli anagrafici
 :  : CMD CALL BRUT06A
 :  : FIN
### Nota
Una volta effettuata la fusione sarà necessario controllare le differenze presenti a parità di tipo contatto/codice. Tale controllo ha la duplice funzione di evidenziare i dati che sono valorizzati in modo differente per scenario e sui quali perciò la gestione dovrebbe essere attivata, e di evidenziare quei dati che dovrebbero invece essere comuni ma che invece risultano differentemente valorizzati. E' da notare che in caso di presenza di codici uguali facenti riferimento a persone fisiche/giuridiche completamente differenti a seconda dello scenario, uno dei due codici andrà cambiato.
 :  : INI  Controllo Differenze per Scenario a livello di Anagrafico
 :  : CMD CALL BRUT01A
 :  : FIN
 :  : INI  Controllo Differenze per Scenario a livello di estensioni
 :  : CMD CALL BRUT02A
 :  : FIN
### Nota
Definizione tramite script dei campi/estensioni di ogni tipo contatto dei campi che vanno contestualizzati per scenario, considerando che tutti gli altri verranno codificati univocamente per tutti gli scenari (es. se si contestualizza il codice pagamento, si dovrà indicare il codice pagamento di ogni scenario, se non si contestualizzano le coordinate bancarie queste andranno indicate un'unica volta per tutti gli scenari). (Cfr. "Configurazione dello script").

 :  : DEC T(TA) P(B£P) K(TABRG[SS.BRG]) I(**Classe Autorizzazione scenari >>)

Verificare che il file delle transazioni anagrafiche sia diverso per ogni ambiente e fondere anch'esso in un unico file (in questo caso il file dovrebbe essere sempre vuoto perciò basta che esista un unico file per tutti gli ambienti).
 :  : DEC T(TA) P(BR2) K(*)

- Attivazione degli scenari nellta tabella BR2
 :  : DEC T(TA) P(BR2) K(*)

# Parametri per scenario
## Configurazione
Le possibilità di configurazioni dei parametri si dovrebbero riassumere nei seguenti punti : 

a) Esistono parametri comuni per tutti gli scenari ==> tale categoria di parametri va impostata sulla tabella BRZ/BRE.
 :  : DEC T(ST) P() K(BRZ)
 :  : DEC T(ST) P() K(BRE)

b) Esistono parametri specifici per gli scenari, identici per definizione, ma differenti per contenuto ==> sulle BRG indicare sempre la stessa categoria parametri (cui devono corrispondere identiche tabelle di definizione C£E/B£N) e nella B£G indicare che i due oggetti della categoria sono CN+tipo contatto e TABRG+relativo sottosettore.
 :  : DEC T(ST) P() K(BRE)
 :  : DEC T(ST) P() K(BRZ)
 :  : DEC T(ST) P() K(BRG[SS.BRG])

c) Esistono parametri specifici per gli scenari differenti sia nella definizione che nel contenuto ==> in questo caso ogni BRG riporterà una categoria parametri differente (a questo punto il fatto di mettere lo scenario nel B£G della categoria è opzionale).
 :  : DEC T(ST) P() K(BRE)
 :  : DEC T(ST) P() K(BRZ)
 :  : DEC T(ST) P() K(B£G)
 :  : DEC T(ST) P() K(BRG[SS.BRG])

Si ricorda inoltre che per poter gestire i parametri già in fase di inserimento del data entry è necessario indicare nella griglia della categoria parametri il fatto che venga accettato il valore **.

## Utilizzo
I parametri dei tipi contatto vanno poi richiamati nei programmi in funzione della configurazione predisposta (es. se si vuol leggere un parametro comune si deve utilizzare la categoria della BRE/BRZ, se si vuol leggere un parametro specifico di uno scenario si deve leggere la relativa categoria passando o meno anche la seconda chiave).

Una facilitazione a tale lettura si può avere impostando una categoria parametri che abbia lo stesso codice del tipo contatto e attivando su di essa l'exit "£A". Chiamando con questa categoria così impostata la £C£6, comunque sia impostata la struttura dei parametri questa verrà risolta dall'exit. Perciò, sia che si stia trattando un parametro comune che uno specifico, si lancerà la £C£6 sempre con la categoria = al codice del tipo contattto. L'exit si occuperà di andare a leggere le categorie indicate nella BRE/BRZ/BRG e lanciare con la corretta configurazione la £C£6.
