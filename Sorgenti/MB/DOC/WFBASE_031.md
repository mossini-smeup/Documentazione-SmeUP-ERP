Compilando opportunamente gli attributi delle transizioni (istruzioni ..TRA) è possibile impostare gli insiemi di utenti abilitati ad agire sui singoli passi di workflow. Fare riferimento al wizard nell'editor degli script.

# Utente esecutore

Compilando il campo "Codice esecutore" (Tip/Par/Cod) è possibile assegnare l'impegno : 
 * In maniera statica, cablando nello script l'utente che dovrà eseguirlo.
 * In maniera dinamica, come variabile istanziata nel corso dell'esecuzione dell'ordine di workflow.

In questi casi si assume che all'attivazione dell'impegno il codice dell'esecutore sia risolto, quindi l'impegno viene portato nello stato di "Pronto" e finisce nella worklist di un singolo utente.

# Classe di esecutori

Compilando i campi Tipo, Parametro e Codice (Tce/Pce/Cce) della "Classe esecutore" è possibile determinare l'insieme di utenti che possono eseguire l'impegno.
Se il campo "utente esecutore" non è pre-compilato questo indica l'insieme degli utenti a cui può essere assegnato (in push o in pull) l'impegno :  all'attivazione dell'impegno questo viene portato nello stato di "Assegnabile"; da qui si può, a seconda dei casi, procedere mediante Assegnazione (push) o Presa in carico (pull).
Se il campo "utente esecutore" è pre-compilato il comportamento dipende dall'impostazione del "backup" (si veda di seguito).

NB - Se nè l'utente nè la classe esecutori sono compilati l'impegno è implicitamente definito come "automatico" :  in tal caso alla sua attivazione il motore di workflow eseguira implicitamente anche la sua dichiarazione, avanzandolo.

## Backup

Normalmente il codice esecutore "vince" sulla classe, nel senso che una volta che viene impostato il codice esecutore solo quell'utente (e non tutti gli utenti della classe) vede l'impegno in worklist e lo può eseguire.
Agendo sul parametro Backup, impostabile per ogni transizione, è possibile modificare questo comportamento standard, facendo sì che anche dopo l'individuazione di un esecutore univoco (esecutore principale) gli altri appartenenti alla classe (esecutori secondari) possano comunque vedere ed eseguire l'impegno.
In particolare si può configurare : 
 * fino a quando l'impegno rimane eseguibile dagli altri (assegnazione/presa in carico).
 * dove viene visto questo impegno (worklist normale, worklist separata di backup).
Note : 
 * se un impegno è di backup non ne viene proposta automaticamente l'esecuzione all'avanzamento.
Si faccia anche riferimento alla documentazione dell'attributo Bak nel wizard di script.

# Responsabile assegnazione

Compilando i campi Tipo, Parametro e Codice (Tre/Pre/Cre) del "Responsabile assegnazione" si può identificare un insieme di utenti abilitati ad effettuare l'assegnazione dell'impegno, ovvero a compilare il campo "Codice esecutore" rispettando i vincoli imposti nella "Classe esecutore".

# Casi gestiti.

Questi sono i casi gestiti dal programma WFUTE_01, che ha il compito di calcolare gli insiemi di utenti per tutto il workflow : 
 * Nel codice esecutore si può impostare : 
 ** TA/B£U/codice utente (statico o calcolato) :  in questo caso si definisce l'esecutore (unico o principale) per l'impegno. La classe, se impostata, definisce l'insieme totale di esecutori :  l'esecutore principale deve appartenervi, tutti gli altri sono esecutori secondari.
 ** OJ/*PGM/nome programma :  serve a riservare l'impegno per un'esecuzione fatta da un programma specifico. Questo impegno non finisce in worklist ma è comunque avanzabile eseguendo il programma. NB :  WFUTE_01 torna tutti gli utenti abilitati (serve per il test and lock), £WFD esclude.
 * Nella classe esecutore e classe del responsabile di assegnazione sono gestite le seguenti casistiche : 
 ** niente tipo, niente parametro, codice="**" :  tutti gli utenti della TAB£U.
 ** TA/B£*GU/gruppo utenti.
 ** LI/TAB£U/lista utenti, costruita e calcolata tramite la £G40.
 ** TA/B£P/classe autorizzazioni :  funzione e valore possono essere passati esplicitamente, oppure vengono usati valori standard (funzione=transizione, valore=T1 per assegnatori, T2 per esecutori).
 ** altri oggetti = autorizzazioni di gestione oggetto :  la classe da testare viene ricavata automaticamente, mentre il valore è l'azione di gestione da testare; ad esempio - AR//A01, valore 02 :  l'utente può eseguire l'impegno se è autorizzato alla modifica dell'articolo A01.

Nello script è anche possibile impostare un suffisso di un programma di aggiustamento, che viene chiamato dopo che il WFUTE_01 ha calcolato un insieme di utenti e può modificare tale insieme.
Fare riferimento all'esempio WFUTE_01A in WFSRC.

# Note

E' possibile disabilitare il pull (forzando l'assegnazione da parte di un responsabile di assegnazione) mediante l'opportuno parametro.
Il push viene invece disabilitato non compilando i campi relativi al responsabile di assegnazione.

# Esempi

 * Codice esecutore cablato :  Tip="TA" Par="B£U" Cod="UTENTE1".
 * Classe di esecutori :  Tce="TA" Pce="B£*GU" Cce="ADM" :  l'impegno può essere assegnato a un utente la cui classe sia "ADM", in B£U.
 * Codice esecutore risolto dinamicamente, ad esempio :  Cce="&AWF.OOW" (l'owner dell'ordine, cioè chi ha creato l'ordine).
 ** E' possibile, per ciascuno di questi casi, far calcolare oav a catena, mediante il separatore '%', ad esempio &AWF.NWF%U/OAV1%U/OAV2.
