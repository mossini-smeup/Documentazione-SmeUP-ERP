# Obiettivo
Nell'utilizzo di Loocup rendere coerenti le funzionalità disponibili per ogni utente con il suo livello di utilizzo di Sme.up.
Ad esempio, evitare che ad un utente "normale" di tipo operativo vengano presentate schede di configurazione, set'n play e simili.

Questo : 
 * Specificando una sola volta per utente il suo livello di operatività sul gestionale.
 * Specificando in maniera omogenea nei vari punti di Sme.up / Looc.up (pop.up, chiavi di menù, schede) il tipo di funzionalità proposto, da confrontare con il livello di operativià dell'utente.
 * Liberando tutte le altre classi di autorizzazioni APPLICATIVA da utilizzi di questo tipo.

# Implementazione e funzionamento
Viene riservata una classe di autorizzazioni USRLVL (funzione **) a cui corrispondono 4 livelli di operatività sul sistema : 
 * 00 - Operativo :  gli utenti finali di Sme.up dal punto di vista solo applicativo.
 * 01 - Gestore / EDP :  utenti intermedi tra l'operativo e l'installatore di Sme.up a cui presentare, ad esempio, azioni di gestione del sistema ma non azioni
di configurazione di Sme.up.
 * 02 - Implementatore :  questo è il livello da attribuire agli installatori Sme.up nelle installazioni dai clienti. Questo livello conferisce il massimo grado di utilizzo di Sme.up.
 * 03 - Sviluppatore (test) :  con questo livello si attivano anche funzioni in fase di test.

Nel caricare una scheda, pop.up, menù bar di Looc.up (menù File / Strumenti / Servizi....) il livello operativo di ogni voce viene confrontato con quello dell'utente :  se il livello operativo utente è minore di quello definito nello script la voce non viene presentata all'utente. Si noti che una voce si intende autorizzata se e solo se l'utente è autorizzato sia a livello operativo che applicativo.


## Attribuzione dei livelli operativi negli script
I livelli operativi vengono sempre impostati specificando l'attributo Usr="nn", dove nn=00, 01, 02, 03.

I livelli operativi si possono impostare negli script : 
 * SCP_SCH - Scheda :  istruzioni G.SEZ, G.SUB. Le subsezioni ereditano il livello operativo delle rispettive sezioni se non ne hanno uno proprio. In ogni caso se una subsezione di livello 00 è contenuta in una sezione a livello 01, un utente con autorizzazione 00 non potrà vederla.
 * SCP_SCHPOP - Pop.up :  istruzioni G.SUB. Si noti che questo si ripercuote su cosa un utente vede in 5250 se è attiva la nuova gestione azioni con £G99.
 * SCP_CLO - Menù iniziali di Looc.up :  istruzioni C.MNU.

Se il livello operativo non è specificato per un utente (da autorizzazioni) esso viene assunto per default a 02.
Se il livello operativo non è indicato per una voce (nello script esso) viene assunto a 00 :  di conseguenza le voci per cui non è impostato il livello operativo sono visibili da tutti.


# Limiti
I livelli operativi sono sequenziali. Questo vuol dire che non è possibile rendere un utente solo "operativo" (livello 00) e contemporaneamente attribuirgli funzioni di test (magari applicativo) (livello 03).
