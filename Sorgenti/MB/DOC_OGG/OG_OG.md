Le attività svolte dai Sistemi Informativi Gestionali devono poter avere comportamenti eterogenei sia per potersi adeguare alle naturali evoluzioni che per rappresentare al meglio una realtà aziendale. Possiamo sintetizzare le operazioni in due attività principali : 

- inserimento di un'informazione :  questa attività può comportare sia delle verifiche precedenti, su informazioni già presenti, che abilitano l'esecuzione dell'inserimento o la condizionano a seconda dell'azione che si intende effettuare, oppure genera effetti successivi;
- reperimento di un'informazione :  questa attività può essere concretizzata attraverso diverse vie, come l'inserimento dall'utente o la derivazione da altre informazioni attraverso calcoli.
Per permettere il normale svolgimento delle attività, nonostante la complessità che ne deriva, è sufficiente non predefinire in modo rigido i vincoli e le modalità in cui l'informazione entra nel sistema o nel modo in cui viene ottenuta.
Centralizzando il punto in cui l'informazione è introdotta o ritornata stabilendo un'entità che si occupa di inserire l'informazione ed un'altra che si occupa di reperirla, si ottiene un beneficio percepito da tutto il sistema informativo perchè chi ritorna l'informazione può avere la necessità di chiedere informazioni ad altri implementando un colloquio a più livelli. In questo modo è possibile non variare la richiesta anche nel caso in cui cambi il modo di soddisfarla. In Sme.up abbiamo chiamato queste entità Oggetti Applicativi.
Gli Oggetti risiedono permanentemente nel sistema; sono le entità con cui gli utenti interagiscono quotidianamente :  gli articoli, gli ordini, i movimenti di magazzino. Ogni oggetto è individuato dalla classe di appartenenza e, per alcune classi, dalla sottoclasse e dall'identificativo, che è univoco all'interno della classe/sottoclasse. Si possono definire, al livello di classe, azioni eseguibili all'atto dell'inserimento, variazione, copia e annullamento di un oggetto. Sono inoltre definite delle funzioni sia specifiche della classe, sia generali, tramite le quali si eseguono variazioni ai singoli attributi di un oggetto. La classe interviene inoltre nel reperimento delle informazioni di un oggetto :  per ogni classe esiste un insieme di attributi primari, il cui reperimento avviene tramite un'interfaccia predefinita. Si possono inoltre definire liberamente ulteriori attributi, inseriti dall'utente, e attributi derivati, di cui si imposta la modalità di reperimento.

# Caratteristiche
* Elemento :  corrisponde ad uno degli elementi definiti dalla tabella *CNTT
* File Master :  file di database che definisce gli elementi della classe. La sua determinazione dipende da quanto definito da :  pgm B£G60G, Tabella B§O, pgm B£IVD0.
* Oggetto Parametro :  definzione delle sottoclassi. La sua determinazione dipende da quanto descritto nel programma B£DEC3.
* Interfaccia :  api/programma di controllo determinazione degli elementi della classe. La sua determinazione dipende dal richiamo specifico della £DEC.
* Classe d'Autorizzazione :  definisce la classe di autorizzazione utilizzata per il controllo delle azioni di gestione sugli elementi della classe. La sua determinazione dipende dal pgm B£GES0.
* Funzione d'Autorizzazione :  definisce la funzione d'autorizzazione da applicare alla classe d'autorizzazione. La sua determinazione dipende dal pgm B£GES0.
* Deviatore :  programma che gestisce a basso livello l'esecuzione delle funzioni di gestione sull'oggetto. La sua determinazione dipende dal pgm B£GES0.
* Tipo Tracciato :  definizione degli attributi intrinseci di ogni elemento della classe. La sua determinazione dipende dalla £IVD.
* Libreria File :  se l'oggetto corrisponde ad un file indica la libreria in cui il file è stato trovato. La sua determinazione dipende dalla £IVD.
* Codice ID :  se l'oggetto corrisponde ad un file indica il campo del tracciato che definisce in modo univoco l'elemento della classe. La sua determinazione dipende dalla £IVD.
* Descrizione ID :  se l'oggetto corrisponde ad un file indica il campo del tracciato che definisce la descrizione dell'elemento della classe. La sua determinazione dipende dalla £IVD.
* Filtro Job Attivo :  indica se al momento il filtro di job per l'oggetto è valorizzato o meno.
* Classi di Parametri :  integrano le informazioni intrinseche della classe. La loro determinazione è legata ai parametri P/ dell'oggetto.
* Contenitore Note :  indica il contenitore utilizzato per le note degli elementi della classe.

# Creare un nuovo Oggetto

* inserire l'oggetto come elemento nella tabella *CNTT :  dato che la *CNTT è una tabella cablata, se il nuovo oggetto è standard va aggiunto nel pgm B£AR14, se invece è un oggetto personale forzare l'inserimento in tabella con codice Xn (a questo punto verrà scritto nel TABEL relativo)
* se l'oggetto è standard definire il modulo proprietario dell'oggetto inserendolo nel programma B£K01G.
* creare il programma B£FUN0_XX, dove XX è il tipo oggetto per attaccare le funzioni specifiche dell'oggetto presentate nel popup, nonchè per tornare classe parametri e contenitore note
* nel pgm B£OAV9 la logica per la determinazione del contenitore note del punto precedente, va qui replicata
* modificare il programma B£G60T, implementando come per gli altri oggetti il reperimento delle informazioni di accesso al database (se l'oggetto appartiene ad un archivio). Casomai sorgesse la necessità di implementare logiche che esulano le possibilità previste dalla struttura del B£G60T, possono essere inserite particolare logiche nella £IVD (cioè il pgm B£IVD0, per il quale si veda ad esempio nel B£IVD0 le considerazioni sull'oggetto CN)
* creare il programma B£OA_XX, dove XX è il tipo oggetto, per gestire gli attributi dell'oggetto
* creare l'interfaccia dell'oggetto, tendenzialmente £IXX, dove XX è il tipo oggetto, sempre che il nome non sia già usato. creare anche il relativo TST.
* inserire l'oggetto nella £DEC andando a modificare il B£DEC0 (è da notare che è attraverso tale implementazione che viene anche riconosciuta l'API che gestisce l'interfaccia dell'oggetto).
* inserire l'oggetto nel B£DEC3 per definirne il parametro
* inserire l'oggetto nel B£DEC4 (se l'oggetto non è un campo di file) o (se l'oggetto è un campo di file) nel B£G60T (se standard) o nella tabella B§O (se personale) per la £G60 e le ricerche in Loocup
* inserire ulteriori caratterizzazioni dell'oggetto nella /COPY £K04 (es. presenza della descrizione, utilizzo del campo negli input panel ecc.)
* se l'oggetto corrisponde ad un archivio mantuenzionabile in Smeup implementarne la relativa struttura : 
** attivare il campo £K04O_GE nella £K04
** implementare nelle schiere in fondo al pgm B£GES0/B£GES0_x (T$B£7E in B£7) l'eventuale modalità di risoluzione delle azioni di gestione (immissione/modifica/copia/cancellazione/interrogazione). Sarà necessario prevedere una combinazione di classe/funzione d'autorizzazioni (tabella B£P da mettere a modello) e probabilmente prevedere il pgm deviatore per la gestione 5250.
** implementare il programma di controllo B£K89_XX, riprendendo il sorgente di esempio in SMESRC B£K89_XX.
** implementare il sorgente del file SCP_A36 avente come codice il tipo oggetto. Si consiglia di partire con la copia del sorgente dell'oggetto AR. In tale script si vedranno presi in considerazione gli script SCP_LAY per i quali nello standard si prevede la codifica tipooggetto_nnn, dove nnn è un progressivo numerico di 3 caratteri. Guardando l'SCP_A36 si evincerà la possibilità di prevedere un SCP_LAY diverso per device. E' inoltre importante che tutti gli scp_lay standard (salvo quello dedicato alla pre-immissione) prevedano l'impiego delle istruzioni I.Fld Tip="NOT" e I.Fld Tip="PAR".
** inserire nello script B£GES0/B£GES0_U in SCP_SET il richiamo della scheda di gestione dell'oggetto che corrisponderà direttamente alla scheda A36, o consisterà in una scheda più complessa che per la manutenzione dati richiamerà la scheda A36.
** Per un maggior dettaglio si rimanda anche al documento applicativo relativo alle azioni di gestione di un oggetto, previsto dal modulo B£BASE
* inserire nello script B£OGGE_OG/B£OGGE in SCP_MNU l'eventuale gestione del "nuovo" per l'oggetto
* se opportuno implementare : 
** lo schema di default da applicare nelle matrici dove sono elencate le istanze dell'oggetto (es. nelle ricerche) attraverso l'oggetto Q2. Si veda la documentazione della relativa classe.
** lo schema T/Q3 da applicare nella funzione di filtro generale in modo nell'F13 vengano presentati nell'ordine ed eventualmente solo i campi ritenuti opportuni.
* documentare l'oggetto in DOC_OGG
* se il nuovo oggetto comporta la creazione di nuove tabelle standard, aggiungerle nel pgm B£OA_ST3 in modo la definizione della tabella venga distribuita nel modello.


# Gli oggetti custom
Gli oggetti custom possono essere creati attraverso la classe oggetto *D, di cui si riporta a seguire il link alla documentazione.
- [Oggetti da Definizione Utente (UFO](Sorgenti/MB/DOC_OGG/OG__D)

# Dettagli implementativi
- [Definizione](Sorgenti/MB/DOC_OGG/OG_OG_D)

