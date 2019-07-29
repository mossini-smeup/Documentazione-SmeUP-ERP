# Introduzione

Gli ordini di workflow possono agire su oggetti master, decidendo in tabella WFA : 
 * Quali tipi di oggetto vanno considerati (T$WFAB, T$WFAJ).
 * In che punti e in che modi i workflow possono essere attivati, ad esempio dal pop.up degli oggetti trattati (T$WFAO, T$WFAP).

Non sono necessarie ulteriori considerazioni per workflow di utilità, per i quali cioè non è prevista la possibilità di gestire (inserire, modificare, copiare, annullare) gli oggetti trattati.
Per quanto riguarda invece la gestione di oggetti Sme.up all'interno di workflow valgono le considerazioni seguenti, a cominciare dai due possibili gradi di integrazione illustrati di seguito.

## Integrazione DEBOLE

La modalità classica di gestione (guida+dettaglio) non è integrata con il workflow.
In questo caso è possibile gestire oggetti all'interno di un workflow (ad esempio fare partire la modifica di un articolo da una scheda di un impegno), lanciando opportune chiamate in azioni di dichiarazione o azioni esterne, ma esistono modi di farlo esternamente al workflow.
Anche se per un oggetto c'è un workflow aperto (ad esempio un processo di creazione di un articolo) non c'è quindi la garanzia che non si possa accedere sull'oggetto stesso esternamente al workflow.
Per questa casistica non sono necessarie ulteriori considerazioni rispetto a quanto spiegato nel resto della documentazione.

## Integrazione FORTE

Tutte e sole le azioni di gestione su un certo tipo di oggetto vengono effettuate mediante workflow; anche la gestione "normale" da guida + opzione di gestione è comandata dal workflow.
Diventa così possibile disegnare in maniera precisa la vita degli oggetti, con la garanzia che la gestione di un oggetto avvenga solo con le modalità stabilite nel processo.

In particolare : 
 * Il workflow accende e spegne la possibilità di gestire gli oggetti a seconda del punto in cui si trovano nei loro processi. La gestibilità di un oggetto controllata da processo permette di stabilire in maniera precisa quali utenti possono agire su quali dati e in quali momenti (ad esempio, per l'inserimento di un cliente si può dire che prima l'amministrazione inserisce i dati finanziari, poi il commerciale quelli di classificazione statistica).
 * La gestione "normale" (guida + opzione) è attiva per un utente se e solo se è attivo un impegno corrispondente di gestione sull'oggetto.
 * Lo stato degli oggetti non è più gestito dagli utenti ma dal workflow, cioè viene automaticamente impostato a seconda del punto del suo processo in cui si trova l'oggetto.

Vantaggi : 
 * È possibile vincolare gli utenti ad effettuare determinati passi obbligatori, essendo la gestione degli stati automatica (ad esempio imporre che un articolo sia utilizzabile in ordini di vendita solo a stato 10, attribuendo tale stato solo dopo il completamento dei dati tecnici).
  * Dal momento che tutte le operazioni effettuate sull'oggetto avvengono tramite workflow si dispone di un log completo tramite le attività sugli ordini di workflow.

# Integrazione forte

## Requisiti

Condizioni necessarie per attivare un'integrazione forte tra la gestione di un oggetto e il workflow : 
 * Il tipo oggetto deve essere tra quelli integrati, ovvero i suoi programmi principali di gestione sono opportunamente modificati.
 * Deve essere abilitata nuova gestione azioni da tabella B£2.
 * Gli utenti che partecipano alla gestione tramite workflow godono delle necessarie autorizzazioni di oggetto.

## Implementazione

Vanno creati : 
 * 1 processo di lancio, che sostituisce l'inserimento/copia manuale e al suo termine va lanciato il corretto processo di gestione a seconda delle rilevanti proprietà dell'oggetto creato.
 * n processi di gestione specifica (che garantiscano la modifica/annullamento ove necessario, più le specifiche azioni tipo approvazione).
 * 1 processo di gestione + 1 di annullamento "paracadute" :  per garantire modificabilità/annullabilità di casi non previsti / non gestiti a workflow.

Un esempio di questa struttura è dato dalle tabelle £OG* in ambiente modello + gli script £OG* a standard. Sono una buona base di partenza per copiare e specializzare sui tipi oggetto desiderati.

### Note comuni

In tabella WFA : 
 * Si dichiara che il workflow sostituisce la gestione (T$WFAN).
 * Si evidenzia, a livello di processo, il tipo di operazione costituita da un inserimento di ordine di workflow di questo tipo, come ad esempio immissione (T$WFAR).

Nello script : 
 * Si indica, per gli impegni che costituiscono le azioni di gestione quale tipo di operazione rappresentano (es. la modifica dell'oggetto).
 * Si associa alla dichiarazione di tali impegni la chiamata al programma WFAZB£_02, che contestualmente all'operazione (se eseguita con successo) dichiara l'avanzamento del workflow.

### Processo di inserimento/copia

Per convenzione viene chiamato £TipoOggetto01 (es. £AR01). Esso : 
 * Lancia la creazione/copia manuale dell'oggetto.
 * Alla fine dell'inserimento (con loop di completamento dati) lancia un'eventuale selezione e lancio del sottoprocesso di gestione da usare.

Tabella WFA £TipoOggetto01, con : 
 * Disabilita gestione :  sì.
 * Punto di creazione :  pop.up.
 * Modo creazione :  esecuzione diretta.
 * Azione di gestione :  A
Tabella WFA £TipoOggetto03, come lo 01 ma azione di gestione C; gruppo processo = £TipoOggetto01.

Esempio di script :  £OG01.

### Processi di gestione.

Processi (potenzialmente più di 1) chiamati £TipoOggetto02x : 
 * Gestiscono la vita dell'oggetto fino alla sua chiusura/annullamento logico (gestisce le 02 e le 04 logiche).
 * Lanciati da WF di inserimento/copia, se manuale, oppure al termine di una creazione cieca (da programma) di oggetto.

Tabelle WFA con : 
 * Disabilita gestione :  sì.
 * Punto di creazione :  utente (generato da WF o da programmi).
 * Azione di gestione :  B.

Script : 
 * Primo passo con DIC.FUN di modifica, Azg=B.
 * Altro passo, con Azg=D (annullamento) e conseguenza esterna = cambio di stato a 90

### Processi "paracadute"

Processi di gestione/annullamento di default per oggetti per cui non è attivo un WF di gestione, ad esempio : 
 * Perchè creati prima del rilascio del workflow.
 * Perchè non vanno gestiti particolari processi.
Servono a garantire la modificabilità di oggetti, data la sostituzione della normale gestione con quella comandata da workflow.

Tabelle WFA (una per la modifica, una per la cancellazione) : 
 * Punto di creazione :  pop.up.
 * Azione di gestione B/D.

Queste due condizioni triggerano il controllo che non ci devono essere ordini di gestione già attivi sullo stesso oggetto.
Si noti che al termine di un workflow di gestione (chiusura dell'ordine) questi processi si riattivano sull'oggetto il cui workflow è terminato :  per questo può essere necessario strutturare i processi di gestione specifica in modo che non terminino.


## Note tecniche.

Programmi importanti : 
 * B£GES0 e WFAZB£_02 per il lancio delle gestioni e il testing delle autorizzazioni.
 * WFAZB£_05 per i cambi automatici di stato, da piazzare come conseguenza nei punti opportuni dei processi.

Particolarità per oggetti DO : 
 * Le azioni RI e CT devono avere come prerequisito l'autorizzazione su 02 e 03!
 * Su DR non vengono testate le autorizzazioni sul relativo DR (analogamente al caso senza WF).
 * Attenzione all'azione 02 su DR, quando crea l'ordine di WF da processo paracadute crea    l'ordine per l'oggetto DO non per la specifica riga DR.

Attenzione :  nei workflow di inserimento/copia oggetto non è possibile per ora usare la variabile su oggetto master : 
 * Inserimento :  quando vengono risolte le variabili il primo impegno non ha ancora restituito il codice dell'oggetto creato.
 * Copia :  userebbe l'oggetto di partenza, non quello in fase di creazione.
