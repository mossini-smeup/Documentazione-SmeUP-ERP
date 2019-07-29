GESTIONE MULTI-SCENARI
GESTIONE MULTI-SCENARI
# OBIETTIVO
La gestione multi-scenari consente ai programmi di un'applicazione di accedere a diversi set di dati (tecnicamente a diversi membri dei file), ad esempio per effettuare delle simulazioni.
# GENERALITA'
E' possibile attivare o disattivare la gestione multi-scenari sia a livello generale, sia per una singola applicazione, agendo sulle tabelle di personalizzazione.
Inoltre, per ogni file multi-scenario dell'applicazione, si può forzare l'utilizzo di uno scenario diverso in due modi : 
1.  Fissando il nome dello scenario in tabella B§F :  in tal modo il file verrà utilizzato come se fosse mono-scenario.
2.  Indicando nel programma un sottogruppo di appartenenza :  per ogni file che non ha tale sottogruppo tra quelli validi viene assunto lo scenario alternativo presente in tabella B§S.
# B£SCE0 - PROGRAMMA GESTIONE MULTI-SCENARI
# Codice applicazione
E' il codice del sottosettore delle tabelle B§S e B§F.
Nota bene :  Nel seguito verrà indicato con &&.
# Sottogruppo
E' un campo facoltativo che indica il sottogruppo a cui appartiene una particolare funzione applicativa e che può condizionare la scelta dello scenario per alcuni file.
# Funz. MUL - Stato attivaz. multi-scenari
## GEN - Att/Dis Generale
Consente la manutenzione della tabella B£2, che contiene il flag di attivazione generale della gestione multi-scenari.
## APP - Att/Dis specifica Applicazione
Consente la manutenzione della tabella &&1 di personalizzazione dell'applicazione, che contiene il flag di attivazione della gestione multi-scenari, con i seguenti valori : 
" " disattiva
"1" attiva
"2" attiva, con possibilità di forzare lo scenario da tab B§F
## VER - Verifica attivazione
Verifica se la gestione multi-scenari è attiva o disattiva per l'applicazione scelta e visualizza un messaggio.
# Funz. GES - Gestione scenari
Permette di eseguire tutte le funzioni di gestione degli scenari dell'applicazione : 
- Creazione di un nuovo scenario :  inserisce un elemento in tabella
B§S e aggiunge un membro a tutti i file multi-scenario.
- Modifica o Interrogazione della tabella B§S.
- Cancellazione di uno scenario esistente :  annulla l'elemento in tabella B§S e rimuove il membro dai file multi-scenario.
- Richiamo del programma &&SCEO specifico dell'applicazione (se esistente), per eseguire azioni particolari su uno scenario, come ad esempio copia, ripresa dati da altre applicazioni, e così via.
Nota tecnica :  Questa funzione può essere messa a menù, con il comando CALL B£SCE3 PARM('&&').
# Funz. SEL - Selezione scenario
## ATT - Attivazione scenario
Consente di scegliere uno scenario, se si preme F20 o se non c'è ancora uno scenario attivo, e di attivarlo.
Nota tecnica :  Esegue una ovrdbf su ogni file multi-scenario.
## DIS - Disattivazione scenario
Consente di disattivare lo scenario attivo.
Nota tecnica :  Esegue una dltovr *all.
# Funz. VER - Verifica scenario attivo
## 90 - Visualizza solo nomi (senza controlli)
Visualizza i nomi dei file definiti come multi-scenario e i nomi dei rispettivi membri utilizzati dallo scenario attivo, ma senza eseguire nessun controllo.
## 80 - Vis. nomi e controllo esistenza
Visualizza i nomi dei file e dei membri (come il punto precedente) ed inoltre verifica l'esistenza di entrambi.
## 70 - Vis. nomi, controllo esistenza e logici
Visualizza i nomi dei file e dei membri, ne controlla l'esistenza (come il punto precedente) ed inoltre verifica che per ogni file fisico vengano gestiti tutti i file logici esistenti.
## - Tutti i controlli
Esegue tutti i controlli previsti ai punti precedenti.
# NOTE TECNICHE
# Attivazione multi-scenario per un'applicazione
Passi da eseguire per attivare la gestione multi-scenario in una applicazione (la cui sigla, ricordiamo, sarà indicata con &&) : 
-  Creare il subsettore B§S&& per gli scenari.
-  (Facoltativo) Creare il subsettore B§F&& per i file speciali, solo se per qualche file si vuole utilizzare un membro fisso, valido per tutti gli scenari.
-  Aggiungere un flag alla tabella di personalizzazione, di solito
è &&1, per definire lo stato di attivazione della gestione multi-scenari.
-  Creare il pgm &&SCEN, utilizzando per documentazione e come modello il sorgente XXSCEN che si trova in SMESRC/SRC.
-  (Facoltativo) Creare il pgm &&SCEO, che riceve in input il nome di uno scenario e permette di eseguire su di esso
delle azioni dipendenti dall'applicazione.
-  Con il pgm B£SCE0, attivare la gestione, creare uno scenario e verificarlo.
-  NOTA BENE :  Al fine di evitare possibili conflitti è consigliabile costruire gli scenari con nomi diversi dal file fisico.
# Modifica formati video e programmi dell'applicazione
## Formati video
Modificare tutti i formati di ingresso in una funzione (formato guida o formato di richiesta parametri) : 
-  Aggiungere il campo W$B£2S (2A  O  1 21) che evidenzia se la gestione multi-scenari è attiva.
-  Aggiungere il campo £UDDMB (30A  O  2 26) per visualizzare la descrizione dello scenario attivo.
-  Attivare il tasto funzionale CF20, con scritta "F20=Scenari", per consentire di cambiare lo scenario attivo.
## Programmi rpg
Modificare tutti i programmi rpg di lancio di una funzione : 
-  Verificare che il pgm esegua la £INZSR (NB :  non la £INZSRLT) e quindi legga la £UDLDA e la tabella B£2.
-  Verificare che il campo contenente il codice tasto premuto sia definito con il nome £KEY.
-  Aggiungere all'inizio del programma (facoltativo) e nella routine di controllo del formato guida (obbligatorio) il richiamo della routine di verifica / attivazione dello scenario : 
MOVEL'&&'      £SCEAP
MOVEL<s/gruppo>£SCESG       facoltativo
EXSR £SCE
SETON                    60
Nota Bene Se la routine segnala che lo scenario attivo è stato cambiato, tutti i file multi-scenario eventualmente aperti dal programma devono essere chiusi e poi riaperti per rendere effettivi i nuovi ovrdbf : 
£SCECH    IFEQ 'Y'
CLOSE<file1>
OPEN <file1>
ENDIF
## Programmi batch
Modificare tutti i programmi, rpg o clp, che potrebbero essere eseguiti all'inizio di un'elaborazione batch.
N.B. :  Questo è necessario perchè l'attivazione dello scenario (OVRDBF) eseguita dal programma di lancio in interattivo non viene "sentita" dall'esecuzione batch.
-  Verificare che il programma interattivo di lancio esegua la £SCE per impostare in modo corretto la £UDLDA (campo £UDMBR e ultimi 4 caratteri a destra del campo £UDDMB).
-  Se il primo programma batch è un clp, aggiungere all'inizio il richiamo del programma che attiva lo scenario in ambiente batch : 
CALL   PGM(B£SCE4CL)
-  Se il primo programma batch è un rpg, aggiungere il richiamo del programma che attiva lo scenario in ambiente batch e spostare l'apertura di eventuali file multi-scenario gestiti da questo programma dopo tale chiamata : 
CALL 'B£SCE4CL'
OPEN <file1>
OPEN <file2>
-  In alternativa ai punti precedenti, ad esempio nel caso in cui si intenda attivare uno scenario da un programma batch ma non vi sia un programma interattivo di lancio che imposta la £UDLDA, è possibile eseguire il programma B£SCE4 invece che B£SCE4CL (con le stesse avvertenze) : 
CALL   PGM(B£SCE4) PARM('<scen.>' '&&' '  ') (oppure)
CALL 'B£SCE4'
PARM <scenario>$$SCE  10
PARM '&&'      $$APP   2
PARM <s/gr>    $$SGR   2     (facoltativo)
