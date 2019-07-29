# Obiettivo
Descrive come personalizzare le variabili, la funzione iniziale, la posizione di icone e immagini e come configurare i server esterni. Sono presenti anche riferimenti a autorizzazioni, servizi interni e documentazione del programma JACFG1.

# Risalita configurazioni
Le configurazioni si possono differenziare per : 
 * Utente
 * Gruppo di appartenenza
 * Ambiente (B£B)
 * Azienda
 * Per tutti
Nota :  I livelli Ambiente e Azienda diventano doppi in caso l'ambiente sia di test.

Sono scritte su AS400 nei membri del file SCP_CLO. Hanno i seguenti nomi : 
 * Utente
 * G_ + Gruppo utente
 * A_ + Ambiente
 * S_ + Azienda _T (solo per ambienti di test)
 * S_ + Azienda
 * S_ALL _T (solo per ambienti di test)
 * S_ALL
 * DEFAULT (da non personalizzare MAI)

__ESEMPIO__
Se sono presenti i seguenti membri : 
 * XX
 * G_SVILU
 * A_SVI
 * S_01_T
 * S_01
 * S_ALL
 * DEFAULT

otterrò che : 

| 
| .COL Txt="**user**" A="L" |
| ---|----|
| 
| .COL Txt="**gruppo**" A="L" |
| 
| .COL Txt="**amb.**" A="L" |
| 
| .COL Txt="**amb. di test (££B£2Z)?**" A="L" |
| 
| .COL Txt="**Az.**" A="L" |
| 
| .COL Txt="**script caricati**" LunAut="1" |
| XX|SVILU|SVI|No|01|XX+G_SVILU+ A_SVI + S_01 + S_ALL + DEFAULT |
| XX|SVILU|TST|Sì|01|XX+G_SVILU+ S_01_T + S_01 + S_ALL + DEFAULT |
| XY|SVILU|SVI|No|02|G_SVILU+ A_SVI + S_ALL + DEFAULT |
| XZ|ADM|SVI2|No| 03| S_ALL + DEFAULT |
| 


**NOTE** : 
 * In ogni setup saranno anche presenti le voci cablate nel programma (JACFG1) che si occupa della costruzione del setup.
 * Le voci sono sempre in aggiunta.
 * Hanno precedenza le voci definite nei membri più specifici.
 * Il gruppo di appartenenza dell'utente viene letto dalla tabella B£U dell'ambiente selezionato e se si associa parte del setup al gruppo bisogna avere l'accortezza di riportare nella B£U dell'ambiente i record degli utenti.

## Sintassi degli script
Gli script sono divisi per sezioni :  una riservata alla definizione dei server, una alle variabili, una ai percorsi e una alle voci dei menù la struttura sarà pertanto del tipo : 
>..  C.SEZ Cod="Server"
..  C.SER .....
..  C.SEZ COD="Varialbe"
..  C.VAR ....


### I tag
_2_C.SER :  definizione Server
In questa sezione vengono definiti tutti i server a cui LoocUp può connettersi per ottenere informazioni. Un server riceve richieste in formato XML e risponde in formato XML. Sia la richiesta che la risposta sono secondo lo standard di LoocUp. Un server è definito come oggetto **V3**-**CSE** la lunghezza massima del codice è di 10 caratteri.

Ogni Server definito dentro uno script viene aggiunto all'elenco degli oggetti V3-CSE
 :  : DEC T(OG) P(V3) K(CSE)  L(1)
Per maggiori dettagli riguardo i server esterni consultare il documento "Gestione dei server esterni"
Per maggiori dettagli sul formato degli XML consultare il documento "Struttura XML di Looc.up"

_2_C.PAT :  Definizione Percorsi
Consentono di definire i percorsi che Looc.up utilizza per localizzare file quali ad esempio immagini, icone.

_2_C.VAR :  Definizione variabili
Le variabili sono d'ambiente e una volta caricato il client non sono modificabili (se non da script). Una variabile è definita come oggetto **V3**-**CVA** la lunghezza massima del codice è di 10 caratteri. Ogni variabile definita dentro gli script viene aggiunta all'elenco degli oggetti V3-CVA

Sono di due tipi :  di sistema e di setup. Quelle di setup possono avere valori predefiniti.

Variabili di sistema : 
 * ***COD_CONN** :  Codice connessione AS/400
 * ***SESSION_ID** :  Codice sessione
 * ***SYSTEM** :  Codice server AS/400
 * ***USER** :  Utente
 * ***VERSION** :  Versione client loocup

Variabili di setup che assumono valori di default : 
 * *IMAGE_PATH :  Specifica la cartella dove recuperare le immagini. Valore di default **cartella istallazione loocup\LOOCUP_IMG\ambiente**
 * *ICON_PATH** :  Specifica la cartella dove recuperare le icone. Valore di default **cartella istallazione loocup\LOOCUP_ICO_n
 * *SEARCH_MODE :   Specifica la modalità di ricerca oggetti. Valore predefinito _H_ADVANCED
 * *SFUNCTION :   Specifica la funzione iniziale da chiamare dopo che LoocUp è stato avviato.

Sono visualizzabili nella finestra principale di LoocUp e comprendono oltre ai due tipi sopra definiti anche tutti i percorsi :  ogni definizione di percorso viene convertita in una variabile.

## Documentazione particolare
Per approfondire il funzionamento del programma JACFG1 vedere il documento seguente : 
 :  : DEC T(OJ) P(*PGM) K(JACFG1)

# Impostazione colore  di base che dovrà avere Looc.UP

Dalla versione **V4R1M151024** di Looc.UP è possibile impostare il colore di base.

Il modo in cui è possibile farlo dipende dal rilascio di Sme.UP installato.

Se il rilascio è un V4R1 con data pari almeno al 27/10/2015, allora è possibile impostare il colore direttamente sull'ambiente o sull'ingresso utente dal comando UP UT5.
Per ulteriori dettagli è possibile riferirsi alla documentazione della configurazione ambienti : 

 :  : DEC T(MB) P(DOC) K(P_B£UT55)

Se il rilascio di Sme.UP è un V4R1 antecedente al 27/10/2015 oppure una versione precedente alla V4R1, è possibile agire in modo "manuale".

E' sufficiente definire la variabile ***HEADERCOLOR** all'interno dello script **SCP_CLO** più opportuno (a seconda che si voglia impostare il colore sull'ambiente o su altro).
La variabile deve avere un valore nella forma __RxxxGyyyBzzz__.

_Nota_
Questa soluzione è valida, come detto, solo per rilasci antecedenti al 27/10/2015. Una volta installata una versione successiva, questo meccanismo diverrà inefficace e sarà quindi necessario utilizzare la modalità descritta al punto precedente (ci sarà un'apposita PTF a ricordarlo).
Si consiglia quindi l'impostazione di questa variabile in script di ambiente, per non rendere troppo difficoltosa la futura migrazione alla modalità standard (UP UT5).
