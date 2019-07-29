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

