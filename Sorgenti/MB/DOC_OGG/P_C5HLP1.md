### Parametri fissi azienda (Dati base - Contabilità)

![C5BASE_006](http://localhost:3000/immagini/MBDOC_OGG-P_C5HLP1/C5BASE_006.png)
Per quanto riguarda l'azienda, è necessario definire altri parametri, racchiusi sotto la voce 'Parametri fissi' : 

![C5BASE_007](http://localhost:3000/immagini/MBDOC_OGG-P_C5HLP1/C5BASE_007.png)
Questa voce permette di accedere alla definizione di alcuni parametri legati alla vita dell'azienda. I dati sono divisi in categorie :  Dati generali, Dati IVA, Dati giornale, Identificazione, Concessioni, Fonti fisse ADF, Cespiti, Varie.
                                                                                                  Analizzeremo qui di seguito alcuni dei campi principali di questa schermata : 
### DATE GENERALI
 * La **Divisione unica**  (elemento della tabella C5Q) è un campo significativo per la contabilità, che individua la presenza di settori nell'azienda, questo viene fatto allo scopo di suddividere l'attività contabile.
 * La **Divisione fiscale**  è un campo creato allo scopo di suddividere i registri IVA, ed altri aspetti fiscali, per quelle aziende che si dividono in più settori d'attività. E' un campo che può assumere valore SI/NO.
 * Il campo **Lista librerie** elenca le librerie utilizzate dall'applicazione (elementi della B£B).

### DATI IVA
 * I campi :  **Periodo/Giorno Liquidazione IVA** e **% Interessi Liquid.**, riguardano i dati relativi all'IVA, ovvero il periodo di liquidazione (mensile, trimestrale o annuale), l'indicazione del giorno in cui l'IVA va liquidata e l'eventuale tasso di interesse da calcolare sul modello F24 in caso di ritardato pagamento dell'IVA stessa.
 * L' **Azienda compensazione IVA**, riporta il codice della capogruppo che verserà l'IVA al fisco, ovvero quella su cui confluiranno crediti e debiti delle altre aziende del gruppo.
 * Se i campi **Dati integrativi registri IVA** e **Sintesi registri riepilogativi IVA** hanno valore 1 (SI), in fondo alla stampa del registro IVA verrà riportato un breve riepilogo.
 * **Plafond mobile** :  è sostanzialmente il tetto massimo di acquisti che possono essere effettuati senza assoggettamento IVA, e può essere inteso come plafond mensile o annuale. Questo campo nasce dall'esigenza delle aziende che esportano molto, e che hanno quindi difficoltà a recuperare l'IVA (perchè i clienti esteri non la pagano). Lo Stato allora mette a disposizione la possibilità di dichiarare la percentuale di fatturato dovuto alle esportazioni e chiedere ai fornitori di emettere fatture esenti IVA (art. 8/c legge 633/72) fino al raggiungimento di un certo importo attraverso una dichiarazione d'intento. Le aziende che effettuano sia prestazioni esenti da IVA, che prestazioni soggette a IVA, non possono detrarre completamente l'IVA degli acquisti dall'ammontare che devono pagare al Fisco ma possono detrarne solo una % proporzionale al volume di prestazioni soggette a IVA (art. 19bis DPR 633/72). Questa percentuale è chiamata pro-rata ed è determinata una volta all'anno basandosi sulle operazioni eseguite l'anno precedente con la seguente formula :  A/(A+B) dove A sono le operazioni che danno diritto a detrazione e B quelle esenti. Se a fine anno la % risulta differente si dovrà effettuare un conguaglio. Riassumento in questo campo va semplicemente indicato se vi è questa possibilità a disposizione dell'azienda.
 * La **% Pro-rata** serve alla aziende, come già detto sopra, per definire la percentuale di detrazione dell'IVA acquisti da applicare nel caso siano presenti vendite che non danno diritto a detrazioni.
 * Il campo **Registri Riferimento Esigibilità Differita**, se presente, è un elemento della C5R che riporta il registro su cui vengono riportate le registrazioni di IVA differita; in poche parole, le aziende che hanno come clienti enti pubblici hanno la possibilità di pagare l'IVA sulle fatture emesse al verificarsi del pagamento della fattura stessa (che spesso avviene anni dopo l'emissione). Viene, quindi, creato un registro IVA apposito in cui vengono riportate le registrazioni di IVA differita, il sistema è in grado di gestire in modo differente queste registrazioni pagando l'IVA solamente nel momento in cui viene incassata la fattura.
 * La **Cessione del credito IVA**  viene fatta al fine di coprire un debito, ad esempio anticipo i soldi ad un fornitore cedendogli la mia IVA a credito.
 * Il **Plafond in liquidazione IVA**  è un campo nato con lo scopo di aggiungere al documento IVA, un'ulteriore informazione relativa al plafond usato.

### DATI GIORNALE
Nascono allo scopo ultimo della contabilità e sono l'elenco cronologico di tutte le registrazioni effettuate nel periodo. Il libro giornale è un libro obbligatorio e soggetto a bollatura.
 * La **Stampa bollato estesa** permette di impostare il numero di caratteri stampati per riga sul libro giornale. (se è flaggato a SI è possibile stampare a 198 caratteri, altrimenti a 132).
 * **Paginazione bollato** :  riguarda la stampa del numero di pagina.
 * **Descrizioni aggiuntive su bollato** :  permette di aggiungere descizioni sul libro giornale.
 * **Note E4/E5 su bollato** :  rispettivamente gli oggetti E4 e E5 sono l'oggetto di testata (file C5TREG0F) e l'oggetto riga (file C5RREG0F) delle registrazioni contabili, ai quali possono essere associate delle note, che possono o meno essere riportate sul libro giornale impostando questi campi.
 * Il campo **Anno riferimento da data inizio** riporta l'anno a cui si riferisce il giornale, è un campo non utilizzato.
 * I campi **Progressivo giornale**, **Ultima riga giornale** e **Ultima pagina giornale** si riferiscono alle informazioni di chiusura di un giornale e che devono essere riprese sul giornale successivo.
 * Il libro giornale deve essere bollato ma non su tutte le pagine :  con il campo **Pagina Bolli su Bollato posso dichiarare su quali pagine è stato messo il bollo.

### IDENTIFICAZIONE
E' caratterizzato dall'insieme dei campi di identificazione della società :  capitale sociale, data inizio attività, casella postale, dati della camera di commercio, ecc.

### CONCESSIONI
Qui invece sono riportate tutte le informazioni circa le concessioni dell'azienda.

### FONTI FISSE ADF
Le fonti fisse ADF sono relative ai flussi di cassa, e quindi più in generale riguardano l'analisi della disponibilità finanziaria. In particolare le fonti fisse sono i dati minimi (le informazioni sui clienti, fornitori e sui conti), nello specifico sono gli estratti conto e gli scadenziari di clienti e fornitori, la situzione di cassa e i pagamenti attesi.

### CESPITI
Nel campo **Dettaglio movimenti stampa libro** viene deciso se riportare a libro giornale tutti i movimenti dettagliati dei cespiti.

### VARIE
Sotto questa voce vengono riportati diversi parametri relativi all'azienda come il contenitore delle note o il rappresentante legale (ovvero chi è autorizzato a depositare bilanci e altre dichiarazioni telematiche).
