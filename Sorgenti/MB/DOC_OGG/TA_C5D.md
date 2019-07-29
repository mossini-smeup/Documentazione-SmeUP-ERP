# C5D - Tipo registrazione contabile
 :  : DEC T(ST) K(C5D)
## OBIETTIVO
Definire le tipologie di movimentazione per indirizzare i programmi di acquisizione dei movimenti contabili.
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC **Descrizione**
Descrive il tipo registrazione contabile
 :  : FLD T$C5DA **Modello registrazione**
È un elemento V2/C5FUA. Definisce i vari tipi di registrazione che sono riconosciute da Sme.up.
Sulla base del contenuto di questo campo, ad esempio, la gestione della registrazione contabile assume forme diverse (con iva, diversi a diversi, ecc..).
 :  : FLD T$C5DB **Oggetto gestito**
Si imposta un tipo/parametro oggetto che individua l'oggetto che viene richiesto all'atto dell'inserimento della registrazione.
 :  : FLD T$C5DJ **Oggetto modificabile**
È un valore V2 SI/NO. Se impostato, all'inserimento della registrazione, il tipo oggetto definito nel campo precedente è proposto ma modificabile.
 :  : FLD T$C5DK **Oggetto obbligatorio**
È un valore V2 SI/NO. È significativo se è presente il tipo oggetto. Se impostato, nell'inserimento della registrazione l'oggetto è obbligatorio. In questo modo, ad esempio, si può far sì che nella registrazione di una fattura sia obbligatorio impostare un ente.
 :  : FLD T$C5DC **Codice registro IVA**
È un elemento TA/C5R. Se la registrazione è con IVA (in base al modello), definisce il registro su cui essa verrà stampata.
 :  : FLD T$C5DD **Causale contabile**
È un elemento TA/C5V. Se impostata, viene proposta all'atto dell'inserimento delle testate e delle righe.
 :  : FLD T$C5DE **Tipo rata**
È un elemento TA/C5E. Se la registrazione prevede lo sviluppo in rate (di dovuto), definisce il tipo di rata che verrà scritta nell'archivio delle rate.
Poichè tra le caratteristiche del tipo rata vi è quella di definire se è di tipo contabile o extracontabile, la scelta è fondamentale per la gestione dello scadenzario.
 :  : FLD T$C5DH **Tipo analitica**
È un elemento TA/C5L. Se la riga di registrazione (in base al suo conto) prevede lo sviluppo in analitica, definisce il tipo di registrazione analitica che verrà proposto all'atto dell'inserimento della registrazione, (o che verrà assunto nel caso di un caricamento cieco).
 :  : FLD T$C5DP **Divisione associata**
È un elemento TA/C5Q. Serve per impostare a quale divisione è associata la registrazione nel caso in cui si gestiscano più divisioni.
 :  : FLD T$C5DF **Livello di nascita testata**
È un elemento TA/B£W00. È il livello assunto in inizializzazione della testata della registrazione. In assenza viene assunto il livello '2'.
 :  : FLD T$C5DG **Livello di nascita righe**
È un elemento TA/B£W00. È il livello assunto in inizializzazione della testata della registrazione. In assenza viene assunto il livello '2'.
 :  : FLD T$C5DL **Gruppo flag testata**
È un elemento TA/B£Y. Definisce il gruppo di flag che viene assunto all'atto dell'inizializzazione della testata della registrazione.
 :  : FLD T$C5DM **Gruppo flag riga**
È un elemento TA/B£Y. Definisce il gruppo di flag che viene assunto all'atto dell'inizializzazione della riga della registrazione.
 :  : FLD T$C5DN **Parametri interni**
È un elemento TA/C£I. Caratterizza i campi liberi (5 alfanumerici e 5 numerici) presenti nell'archivio delle registrazioni (testate e righe), che sono a disposizione dell'utente.
 :  : FLD T$C5DO **Parametri espliciti**
È un elemento TA/C£E. Definsce la categoria parametri per aggiungere informazioni alle testate e alle righe di registrazione.
 :  : FLD T$C5DQ **Segno Documento**
È un elemento V2/SEGNO. Se la registrazione è di tipo 01 o 02 o 07, ne identifica il segno. Viene riportato nella testata della registrazione, all'atto dell'inizializzazione.
 :  : FLD T$C5DI **Condiz. scelta caus.**
È un elemento TA/C5*CR. Se impostato, definisce il criterio di selezione mediante il quale vengono effettuati ricerca e controllo validità sulla causale di riga di una registrazione.
 :  : FLD T$C5DR **Suffisso programma exit di inizializzazione**
Se impostato in questo campo il valore x, nella manutenzionde delle registrazioni contabili verrà eseguito il programma C5E501L_x, in cui è possibile implementare comportamenti specifici (controlli e forzature).
 :  : FLD T$C5DT **Suffisso programma exit di immissione**
Se impostato in questo campo il valore x, nell'inserimento delle registrazioni contabili verrà eseguito il programma C5E501I_x, in cui è possibile inizializzare opportunamente le righe.
 :  : FLD T$C5DU **Documento senza ritenute**
È un elemento V2/SI/NO. Normalmente, una fattura di un ente percipiente richiede la compilazione contestuale della ritenuta. Se impostato questo campo, non viene eseguito questo collegamento. In tal modo è possibile registrare fatture di percipienti totalmente non soggette a ritenute (ad esempio quelle dei rimborsi spese).
Va ricordato che, se una fattura è parzialmente soggetta, si specifica la parte non soggetta nel campo opportuno della ritenuta.
 :  : FLD T$C5DS **Ingresso in lista**
È significativo se la registrazione è di pagamento (modello 05/06). I valori che può assumere sono : 
1=Si, all'immissione della registrazione viene presentata la manutenzione in lista, invece di entrare in immissione del saldaconto
2=SDC, questa opzione fa si che anche in modifica la prima schermata che viene presentata sia quella del saldaconto
 :  : FLD T$C5D1 **Ingresso in testata**
È significativo se la registrazione è di contabilità generale.
 :  : FLD T$C5D2 **Tipo Giornale**
Permette di raggruppare i tipi registrazioni in classi. Tipicamente viene utilizzato nella stampa dei giornali francesi.
 :  : FLD T$C5D3 **Quadratura IVA**
Nelle registrazioni con Tipo Modello "Registrazioni con IVA",  permettere di introdurre delle eccezioni al calcolo della quadratura dell'IVA :  se valorizzato con "1" sarà possibile scrivere un imponibile che non quadra con la somma delle contropartite, anche se sarà comunque necessario scriverne almeno una; mentre se valorizzato "2", sarà possibile inserire la riga di IVA anche senza avere alcuna contropartita.
Se valorizzato a "3", sarà possibile inserire imponibile, codice iva, imposta discordanti.
 :  : FLD T$C5D4 **Modello Subfile**
Questo flag permette di utilizzare una visualizzazione specifica per la registrazione, che si sostituisce a quella standard prevista per il modello di registrazione.
- " " = Utilizza la visualizzazione standard desumibile dal modello di registrazione.
- "2" = Utilizza un visualizzazione del subfile che evidenzia la valorizzazione di data documento/data valuta (questa visualizzazione dovrebbe essere applicata ai tipi registrazione utilizzati nelle operazioni bancarie nel caso in cui sia stata attivata la tesoreria)
 :  : FLD T$C5D7 **Tipo protocollo**
Il tipo protocollo viene utilizzato per identificare le registrazioni con una numerazione separata a seconda del tipo registrazione.
In fase di registrazione il numero protocollo verrà preso in automatico se sarà compilata la tabella dei numeratori (tabella CRN sottosettore C5)
 :  : FLD T$C5D5 **Exit inizializzazione E4**
È il suffisso del programma di aggiustamento dell'inizializzatore/driver delle testate registrazioni contabili, che innesca il richiamo del programma _7_C5C5A0_x (x è il suffisso).
Tale programma viene richiamato dall'api £C5A ad ogni esecuzione in inizializzazione nuovi record o all'aggiornamento per scrittura, aggiornamento e cancellazione.
Il prototipo del programma è costituito dal sorgente C5C5A0_X.
 :  : FLD T$C5D6 **Exit inizializzazione E5**
È il suffisso del programma di aggiustamento dell'inizializzatore/driver delle righe di registrazione contabile, che innesca il richiamo del programma _7_C5C5B0_x (x è il suffisso).
Tale programma viene richiamato dall'api £C5B ad ogni esecuzione in inizializzazione nuovi record o all'aggiornamento per scrittura, aggiornamento e cancellazione.
Il prototipo del programma è costituito dal sorgente C5C5AB_X.
 :  : FLD T$C5D8 **Controllo fatture**
Se impostato attiva la gestione del controllo fatture. Presenta le fonti in attesa di contabilizzazione e già contabilizzate, legate alla fattura. È operativo sia per il ciclo attivo, che passivo. Nel primo caso l'immissione della registrazione è batch dal gestionale. Creata la registrazione è ammessa solo la modifica del conto contabile o valori di analitica che saranno poi aggiornati su gestionale. La cancellazione della registrazione scontabilizza le fonti collegate del gestionale.
Per il ciclo passivo, il controllo fatture avviene completamente all'interno del flusso di gestione della registrazione contabile. Vengono presentate tutte le fonti in attesa di contabilizzazione, che possono essere modificate e scelte. Andranno a comporre le righe di contropartita della registrazione. È sempre possibile modificare la registrazione che provvede a rifasare le fonti del gestionale collegato.
 :  : FLD T$C5D9 **Competenza**
Definisce gli automatisti relativi all'attribuzione dei costi/ricavi in funzione del principio della competenza.
* "1"=In presenza di conti con rilevanza stanziamento, viene attivata la creazione degli stanziamenti automatici
* "2"=In presenza di una data competenza iniziale/finale differente dalla data registrazione di almeno un mese viene attivata la creazione degli stanziamenti automatici
* "3"=In presenza di una data competenza iniziale/finale a livello di testata o di riga differente di almeno un mese dalla data registrazione viene attivata la creazione di registrazioni automatiche di rateo/risconto distribuendo i valori in base ai mesi di competenza.
* "4"=Forza NO, se impostato il flag di forzatura nella tabella C51 questo valore permette di gestire le eccezioni
* "5"=Come il valore 3, ma i valori vengono distribuiti in base ai giorni invece che dei mesi di competenza.
* "6"=Come il valore 3, ma crea la registrazioni solo se i ratei/risconti sono infraesercizio
* "7"=Come il valore 5, ma crea la registrazioni solo se i ratei/risconti sono infraesercizio
* " "=Vengono applicate le logiche previste dal campo della tabella C51

Nei primi due casi la creazione delle registrazioni di stanziamento avviene tramite il lancio di un lavoro batch
indipendente i cui parametri di esecuzione sono modificabili tramite il comando UP GPE impostando come programma
"C5E413E". Dovranno inoltre essere definiti gli elementi della tabella C5U STADA e STAAV.
 :  : FLD T$C5D0 **Reg.Dogana (SV)**
Se impostato il campo con valori da 1 a 3 (vedere tabella sottostante per il singolo significato), alla conferma di una registrazione di fattura estera viene lanciata in automatico la creazione della registrazione della fattura della dogana, riprendendo i dati della registrazione origine. Affinche l'automatismo funzioni è necessario definire l'elemento FATDG nella C5U.
Se impostato il valore D, alla chiusura della registrazione della fattura verrà presentata una schermata per collegare il documento doganale alle rispettive fatture fornitori.
Possibili valori : 
* "1"=Si. Crea la registrazione della bolla doganale e la stessa è collegata alla registrazione della fattura fornitore attraverso il campo n. registrazione origine;
* "2"=Si, Rip.Prot. Crea la registrazione della bolla doganale e la stessa è collegata alla registrazione della fattura fornitore attraverso il campo n. registrazione origine, con ripresa del protocollo;
* "3"==Si, Rip.Pr/Doc. Crea la registrazione della bolla doganale e la stessa è collegata alla registrazione della fattura fornitore attraverso il campo n. registrazione origine, con ripresa del protocollo e del n. documento;
* "D"=Colleg. Doc. Forn. In inserimento della registrazione della bolla doganale permette di inserire i riferimenti della/e fatture e codici fornitori a cui si riferisce attraverso dei parametri.
 :  : FLD T$C5DZ **Autostorno**
Se impostato, la registrazione verrà automaticamente cancellata il giorno  successivo alla data di registrazione.
 :  : FLD T$C5DW **Annulla quadratura automatica**
Quando questo campo non è valorizzato, se è presente una riga della registrazione senza importo, ma con l'indicazione del conto contabile, dando invio su questa riga viene automaticamente imputato l'importo
che fa quadrare la registrazione. Perciò se imputo 1 questo automatismo viene disattivato.
 :  : FLD T$C5DX **Divisione**
Se attiva la gestione della divisione permette di impostare una divisione fissa per il tipo di registrazione.
 :  : FLD T$C5DY **No Volume d'affari**
Se impostata permette di escludere il tipo registrazione dal calcolo del volume d'affari.
