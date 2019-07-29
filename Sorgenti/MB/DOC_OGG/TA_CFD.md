# CFD * Domande del Questionario
 :  : DEC T(ST) K(CFD)
## OBIETTIVO
Definire le domande che compongono un questionario.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM  **Codice domanda**
Si consiglia di utilizzare al massimo 9 caratteri. Questo perché la /copy £OAV che scandisce le domande del questionario si aspetta nel campo £OAVAT (lungo 15) una sintassi di questo tipo :  C/xxx.yyyyyyyyy dove xxx è il codice del questionario e yyyyyyyyy è il codice della domanda. Questo significa, inoltre, che è meglio codificare il questionario con un codice di 3 caratteri.
 :  : FLD T$DESC  **Descrizione**
 :  : FLD T$CFDD  **Categoria Domanda**
 Definisce la tipologia della domanda e come si presenterà all'utente in fase di compilazione del questionario.
 I possibili valori sono : 
 * 01 Valore singolo
All'utente viene mostrata una casella in cui può inserire la risposta. Il valore che si inserisce deve essere compatibile con il tipo di oggetto associato alla domanda (campo T$CFDC)
 * 02 Scelta in lista
L'utente vedrà una lista di possibili risposte dalla quale sceglierà quella desiderata.
La lista sarà composta dagli oggetti il cui tipo è definito nel campo T$CFDC
 * 03 Gestione in lista
L'utente può costruire una lista di valori aggiungendo un campo ad ogni risposta.
Questi valori possono essere filtrati dal tipo oggetto definito nel campo T$CFDC
 * 04 Aggiunta a lista
L'utente aggiunge una risposta alla volta ad una lista di risposte. Il valore che aggiunge può essere in seguito
cancellato, ma non modificato
 * F- File
La domanda è composta da tante domande (posizionate tutte sulla stessa riga, come accade per le domande configurate) quanti sono i campi del file, il cui nome è specificato alla voce Par. presentazione (vedi dopo). Il testo delle domande è costituito dalle descrizioni dei campi del file.
 * T- Tabella
Comportamento analogo ad F-, tranne per il fatto che il testo delle domande è costituito dalle intestazioni dei campi di una tabella, specificata anch'essa nel campo Par. presentazione.
 * Q- Questionario
In questo caso la domanda è composta da tutte le domande del questionario il cui nome è specificato alla voce Par. presentazione.
 * C- Cat.parametri
Il testo delle domande è formato dai parametri di un oggetto specificato alla voce Par. presentazione
 :  : FLD T$CFDL  **Par. Presentazione**
Valori opzionali di personalizzazioni grafiche. Per esempio, si può scegliere di non visualizzare il codice di una risposta, ma di mostrarne solo la descrizione. Nel caso la domanda appartenga alla categoria F-, T-, Q-, o C-, questo campo conterrà rispettivamante il nome di un file, di una tabella, di un questionario o di un oggetto.

 * **Carattere 1**
 ** BLANK Domanda standard
 ** E Gestione Descr. estese (NOTE) :  viene mostrata una casella di testo sopra la domanda
 ** D Solo descrizione domanda  :  viene mostrato solo la descrizione della domanda, usare come separatore di gruppi di domande
 ** F Solo descr. domanda * descr. e
 ** S Solo titolo di una subsezione  :  ha senso solo per domande configurate. La domanda fa ra raggruppatore, ad esempio quando le sue domande figlie sono definite in una sezione ausiliaria
 ** T Solo tit. subsezione * descr.  : 
 * **Cosa emettere**- Solo per domande chiuse - - Con questo parametro definisco la modalità di presentazione delle opzioni. Si può scegliere se mostrare Codice e descrizione, solo il codice solo la descrizione. Inoltre si può decidere se visualizzare anche l'immagine, in quattro dimensioni (piccola, media, grande, default).
 ** BLANK Sia codice che decodifica  : 
 ** D Descrizione in COMBOBOX
 ** C Codice in COMBOBOX
 ** E Codice * Desc.- Immagine default
 ** M Codice * Immagine default
 ** N Desc. * Immagine default
 ** O Codice * Desc.- Immagine piccola (Nota 1)
 ** I Codice * Immagine piccola (Nota 1)
 ** L Desc. * Immagine piccola (Nota 1)
 ** F Codice * Desc.- Immagine media (Nota 2)
 ** G Codice * Immagine media (Nota 2)
 ** H Desc. * Immagine media (Nota 2)
 ** P Codice * Desc.- Immagine grande (Nota 3)
 ** Q Codice * Immagine grande (Nota 3)
 ** R Desc. * Immagine grande (Nota 3)
Nota 1 :  le immagini devono avere suffisso _1
Nota 2 :  le immagini devono avere suffisso _2
Nota 3 :  le immagini devono avere suffisso _3

 ***Nota**
 ** N Gestire la nota
 ** I Gestire la nota come domanda
 ** BLANK Non gestire la nota
 * Tipo compilazione
 ** T In finestra separata (tabella) * Ha senso per le domande configurate a risposta multipla ambito WEB :  viene aperta una finestra apposita
 ** A Lista con 10 elementi * nel caso di risposta chiusa su presenta una lista che mostra 10 elementi, il default è 5
 ** B Lista con 15 elementi * nel caso di risposta chiusa su presenta una lista che mostra 15 elementi, il default è 5
 ** 1 Come check box su 1 colonna * nel caso di risposta chiusa, su presenta le opzioni con dei checkbox disposti su una colonna
 ** 2 Come check box su 2 colonne * nel caso di risposta chiusa, su presenta le opzioni con dei checkbox disposti su 2 colonne
 ** 3 Come check box su 3 colonne * nel caso di risposta chiusa, su presenta le opzioni con dei checkbox disposti su 3 colonne
 ** 4 Come check box su 4 colonne * nel caso di risposta chiusa, su presenta le opzioni con dei checkbox disposti su 4 colonne
 ** Z Come check box pos. autom. * nel caso di risposta chiusa, su presenta le opzioni con dei checkbox disposti in maniera automatica
I seguenti due caratteri lavorano in simbiosi e vanno utilizzati quando un gruppo di domande ha un'unico programma di controllo (induzione dinamica) e desidero un richiamo unico. Il meccanismo di controllo prevede infatti che tutte le domande a induzione dinamica della sezione corrente vengano controllate. Per evitare inutili richiami posso costruire dei gruppi usando questi due campi.  Per effettuare questo legame si andrà a impostare sulla domanda X1, nel campo Soggetto condizionamento un valore, per esempio A, lo stesso valore andrà messo nella definizione della domanda X2, ma nel campo Oggetto condizionamento.
 * **Soggetto condizionamento** identifica la domanda condizionante
 * **Oggetto condizionamento** identifica la domanda condizionata
 ***Protezion**e :  consente di bloccare l'editazione / nascondere il campo
 ** BLANK Modificabile
 ** 1 Non modificabile
 ** 2 Non visualizzato
 * **Ricarica questionario** NON UTILIZZATO
 * **Conversione carattere** :  consente di forzare il formato del carattere dei campi di input
 ** BLANK Non convertire
 ** U Converti in MAIUSCOLO
 ** L Converti in minuscolo
 ***Immagine/Formato**
 ** blank :  Non mostrare immagine
 ** 1 :  Immagine piccola  :  verrà cercata l'immagine "codice_immagine"_1.xxx
 ** 2 :  Immagine media  :  verrà cercata l'immagine "codice_immagine"_2.xxx
 ** 3 :  Immagine grande  :  verrà cercata l'immagine "codice_immagine"_3.xxx
 ** L :  Formato libero  :  verrà cercata l'immagine "codice_immagine".xxx
 ** D :  Dimensioni come default  :  verrà cercata l'immagine "codice_immagine".xxx e impostata la larghezza di 400 pixel, mantenendo le proporzioni.
 L'immagine verrà ricercata secondo le logiche descritte nel documento LOBASE_06, eventualmente effettuando tutte le risalite (se abilitata).
 * **Risalita immagine** :  consente di attivare la risalita, il default è disattiva.
 ***Forzatura regole** :  nel caso una regola sulla domanda blocchi la compilazione è possibile forzare il controllo. Questa informazione viene aggiunta alla risposta.
 * **Ricerca per Descriz**. :  consente di impostare la ricerca per descrizione come predefinita.
 * **Attivato da regole**  :  consente di rendere non visibile la domanda. La sua attivazione sarà condizionata da una regola.

 :  : FLD T$CFDA  **Multipla**
Se impostato a 1, all'utente è permesso l'inserimento di più valori di risposta alla stessa domanda.
 :  : FLD T$CFDB  **Obbligatoria**
Se impostato a 1, la domanda richiede obbligatoriamente una risposta.
 :  : FLD T$CFDM  **Accetta Altro**
Se impostato a '1', accetta risposte libere, su richiesta dell'utente.
 :  : FLD T$CFDC  **Tipo Oggetto**
Si inserisce il tipo oggetto che identifica l'oggetto SmeUp associato alla domanda.
 :  : FLD T$CFDN  **Lunghezza**
In questo campo viene inserito un numero intero che stabilisce il numero massimo di caratteri della risposta. Per tutti gli oggetti SmeUp si suggerisce la lunghezza di 15 caratteri.
 :  : FLD T$CFDO  **Decimali**
Definisce il numero di decimali accettati dalla risposta, nel caso il tipo oggetto di quest'ultima sia un numero.
 :  : FLD T$CFDF  **Filtro Risposta**
In questo campo si immette il tipo dell'oggetto SmeUp utilizzato per parzializzare le possibili scelte dell'utente.
E' possibile filtrare le possibili risposte secondo i seguenti criteri
 *          Nessuno
 * TA        Tabella
 * LI        Lista di oggetti
 * V2        Valori V2 di SME.up
 * PU        Programma utente
 * LD        Lista dinamica
Richiede la compilazione anche del campo seguente.

**NOTA** La coppia di valori **Filtro Risposta** e **Par. Filtro** va ad aggiungere un elenco di scelte alla domanda. La domanda da aperta (posso scegliere tra tutti gli articoli), diventa chiusa (posso scegliere solo tra gli elementi specificati).
La costruzione dei possibili valori avviene prima dell'emissione del configuratore, non è condizionata dalle risposte fornite.
Se si vuole condizionare l'elenco dei valori oppure rendere dinamica la struttura del configuratore in funzione alle risposte fornite va utilizzato il campo T$CFDH.

 :  : FLD T$CFDG  **Par. Filtro**
È necessario inserire il parametro dell'oggetto SmeUp utilizzato per parzializzare le scelte dell'utente, se è stato selezionato un filtro per la risposta, secondo il seguente schema.
Se nel campo **Filtro Risposta**  è stato indicato
 * TA -->  va specificata un settore ed eventualmente il subsettore. Nel caso di valori specifici per il configuratore la tabella CFV è stata creata ad-oc
 * LI  --> va specificata una lista di oggetti
 * V2 --> va indicato uno dei valori V2 di SME.up
 * PU --> va indicato un valore V3 di tipo PPU, cioè un programma CFVPU_&&
 * LD --> va indicato un valore V3 Tipo PLD, cioè un programma CFVLD_&&


 :  : FLD T$CFDE  **Config.Risposta**
Consente di definire se la domanda avrà domande aggiuntive e la sorgente. Nel caso si scelga BA o SE il campo __Par. Config.__ indicherà la sorgente.
 :  : FLD T$CFDI  **Par. Config.**
Specifica quali sono le domande aggiuntive.
Se nel campo **Config.Risposta** ho impostato BA, potrò scegliere tra Quantità/Prezzo/Sconto/Data/Nota. Ad esempio "1 3", aggiungerà Quantità e prezzo, mentre " 23 5" aggiungerà Prezzo, Sconto e Nota
Se nel campo **Config.Risposta** ho impostato SE, indicherò la sezione da cui le domande devono essere prelevate. Normalmente la sezione di appoggio viene nascosta tramite una regola.
 :  : FLD T$CFDH  **Induzione dinamica**
Specifica il suffisso del programma CFVLD_.
Durante la compilazione di un questionario, quando fornisco la risposta a questa domanda, viene richiamato il programma CFVLD_xx. Al programma viene passato l'XML contenente le risposte fornite. Viene restituito un XML che può modificare la struttura del questionario e/o le risposte.

