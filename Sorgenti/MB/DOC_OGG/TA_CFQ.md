# CFQ - Questionario
 :  : DEC T(ST) K(CFQ)
## OBIETTIVO
Definire i questionari del configuratore Build.up
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM  **Codice questionario**
Si consiglia di utilizzare codici di 3 caratteri. Questo perché la /copy £OAV, che scandisce le domande del questionario, si aspetta nel campo £OAVAT (lungo 15) una sintassi di questo tipo :  C/xxx.yyyyyyyyy dove xxx è il codice del questionario e yyyyyyyyy è il codice della domanda. Questo significa anche che è meglio codificare le domande con un codice di al massimo 9 caratteri.
 :  : FLD T$DESC  **Descrizione**
Contiene la descrizione di questo specifico Questionario
 :  : FLD T$CFQA  **Livello**
Serve per attivare o meno il questionario.
 :  : FLD T$CFQB  **Subs.sezioni/domande**
Si inserisce il subsettore della tab. CFS (tabella contenete le sezioni) e della tab. CFD (tabella contenete le domande).
Tutte le sezioni e le domande che vengono presentate nel questionario sono in questi due sottosettori, che devono avere lo stesso nome.
Il questionario non può contenere sezioni o domande che appartengono a sottosettori diversi da quelli al quale è associato.
 :  : FLD T$CFQF  **Metodo costr. sezioni**
In questo campo si inserisce un codice che identifica il criterio con il quale le sezioni vengono aggiunte al questionario creato. I valori possibili sono : 
 - Vuoto (Tutte le sezioni) :  vengono inserite nel questionario tutte le sezioni contenute nel subsettore CFS associato al questionario. L'ordine di inserimento è dato dall'ordine alfabetico del codice delle sezioni.
 - 02 (Definite in parametro) :  alla sezione appartengono le sezioni specificate nel parametro di costruzione delle sez. (campo T$CFQG, vedi dopo)
 - 03 (Con prefisso indicato) :  vengono inserite nel questionario le sezioni che iniziano con il prefisso specificato nel campo T$CFQG (Parame.costr.sezioni)
 - 04 (Definite nello script senza regole) :  vengono inserite nel questionario le sezioni/domande definite nello script specificato nel campo T$CFQG (Parame.costr.sezioni) e presente nel membro
 SCP_CFG. Non c'è la possibilità di definire regole.
 - 05 (Definite nello script con regole) :  come l'opzione 04 ma con la possibilità di definire regole.
 :  : FLD T$CFQG  **Parame.costr.sezioni**
In base al metodo scelto (T$CFQG) in precedente, sono valide le seguenti opzioni.
Se è stato inserito il metodo 02 ("Definite in parametro"), in questo campo deve essere specificato un elemento della tab. B£NTA (parametro). Tipicamete questo parmetro sarà definito come multiplo con tipo oggetto='CS' (elemento di settore) e parametro= 'CFS'. In questo modo le sezioni di questo questionario saranno definte nei parametri del questionario stesso. L'ordine con cui le sezioni vengono aggiunte a questo parametro coincide con l'ordine con cui si presenteranno all'utente che compila il questionario.
Se è stato inserito il metodo 03 ("Con prefisso indicato"), in questo campo va specificata la parte iniziale del codice delle sezioni da inserire nel questionario. Tutte le sezioni esistenti nel subsettore CFS associato al questionario, il cui codice comincia con i caratteri indicati in questo campo, sono mostrate all'utente nel questionario creato.
Se è stato inserito il metodo _R_04 _7_(Definite nello script senza regole) o _9_05 o  (Definite nello script con regole) questo campo conterrà il nome del membro del file SCP_CFG che definirà il questionario.
 :  : FLD T$CFQH  **Programma di stampa**
Indica il programma che viene chiamato per generare l'XML che contiene i dati usati per la stampa PDF. Una volta finita la fase di compilazione del questionario, è data la possibilità all'utente di stampare in formato PDF il risultato della configurazione.
 :  : FLD T$CFQI  **Identificativo**
È un elemento della tabella B£G
Fornisce la chiave d'accesso al file, nel quale sono salvate le configurazioni create (CFVARI0F/B£MEDE0F).
Se questo campo è lasciato vuoto non è possibile salvare le configurazioni.
 :  : FLD T$CFQL  **Gestione configurazione**
Se impostato viene richiamato il programma CFSAV_xx dopo l'operazione di salvataggio della
configurazione.
 :  : FLD T$CFQR  **Eseguire Regole**
Con questo campo è possibile attivare o disattivare le regole del questionario.
- 1 Le regole scattano ad ogni risposta fornita.
- 2 Le regole scattano solo al cambio Sezione - da utilizzare per le compilazioni su WEB.
- 3 Disattivate
 :  : FLD T$CFQS  **Aspetto del questionario**
**NON GESTITO**
La visualizzazione del configuratore non è assunta sulla base di questo parametro ma è assunta in base al tipo di questionario secondo il seguente schema : 
- questionari Q- :  viene visualizzata la prima sezione e un albero per la navigazione.
- questionari T- :  viene visualizzata solo la prima sezione, le altre sono oscurate.
- altri questionari (U-, S-, L-, ecc) :  vengono visualizzate tutte le sezioni in forma tabsheet.
 :  : FLD T$CFQT  **Dati ausiliari**
Con questo campo è possibile aggiungere una sezione contenente informazoini sul questionario in uso, come ad esempio la data di creazione, l'utente di creazione e modifica ecc...
 :  : FLD T$CFQU  **Riepilogo**
Con questo campo è possibile avere un riepilogo finale al completamento del questionario in uso. Utilizzata nelle compilazione su WEB
 :  : FLD T$CFQV  **Struttura in ingresso**
**NON GESTITO** :  il configuratore è in grado di riconosce la struttura in ingresso e di gestirla.
 :  : FLD T$CFQZ  **Struttura in uscita**
**NON UTILIZZARE**il configuratore grafico decide autonomamente quale è il tipo di struttura da restituire in base alla destinazione :  se le risposte devono essere memorizzate nel CFVARI la struttura sarà Risposta, se devono essere memorizzate nel B£MEDE, la struttura sarà Sezione, mentre se si sta manutenendo una tabella, la struttura sarà CDATA.

Con questo campo viene definità la struttura di comunicazione delle risposte da parte del questionario.
- 1 Contenuta nella struttura Risposta
- 2 Contenuta nella struttura CDATA
- 3 Contenuta nella struttura Sezione
 :  : FLD T$CFQQ  **Salvataggio esteso**
Con questo campo viene definita la possibilità di salvare la configurazione in formato XML, così come è stata ricevuta (Verrà depositata sull'archivio B£MEDE0F).
 :  : FLD T$CFQP  **Motore regole**
**NON UTILIZZARE** :  dalla V2R3 quello dinamico è stato esteso e comprende tutte le funzioni di quello statico, svincolandosi dalla necessità di rigenerare il motore.
_r_HELP di LOOCUP V2R2M070214
Con questo campo viene definito il modo in cui eseguire le regole : 
- S Statico
Sono sviluppate tutte le funzioni matematiche. La struttura del questionario non è multi livello (sezioni ripetibili o inclusione di questionari non ammessa)
- D Dinamico
Sono sviluppate tutte le funzioni matematiche. La struttura del questionario può essere multi livello (sezioni ripetibili o inclusione di questionari è possibile)
Lasciare blank o indicare D :   il motore dinamico ha le stesse funzionalità di quello statico ed è quindi consigliato utilizzare sempre quello.
_r_HELP di LOOCUP versioni precedenti
Con questo campo viene definito il modo in cui eseguire le regole : 
- S Statico
Sono sviluppate tutte le funzioni matematiche non è possibile utilizzare più livelli di domanda
- D Dinamico
Sono sviluppate tutte le funzioni matematiche standard (+,-, : ,*) è possibile utilizzare più livelli di domanda.
 :  : FLD T$CFQC  **Formato Numeri**
Consente di definire come i numeri devono essere restituiti.
valori possibili : 
BLANK         Come Manut. Tabelle :  il numero viene restituito a larghezza fissa, come memorizzato nel file tabel00F.
N                  Naturale con virgola :  il numero viene restituito nel formato Naturale, e il separatore dei decimali è con la virgola.
 :  : FLD T$CFQD **Numeratore**
Nel caso in cui il formato di salvataggio sia automatico, vedere B£G, utilizzare questo campo per determinare il numeratore da utilizzare per l'IDOJ.

Se non definito, il sistema utilizza l'IDOJ dell'utlitma configurazione salvata e lo incrementa di 1.

 :  : FLD T$CFQW  **Richiesta Univocita**
**In sviluppo**
Attivo solo se si depositano le risposte sul CFVARI.
Dato il questionario verifica se tutte le risposte sono già state salvate, se così assume la stessa chiave.
Questa modalità deve essere attivata solo se si gestisce il salvataggio in modalità automatica.
