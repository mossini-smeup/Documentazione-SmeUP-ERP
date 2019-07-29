# C51 - Impostazioni base keep.up
 :  : DEC T(ST) K(C51)
## OBIETTIVO
Estende i parametri generali relativi all'applicazione Contabilità, rispetto a quelli contenuti nella tabella C51.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Elemento**
È un elemento fisso.
 :  : FLD T$C57A **Valuta Traduzione**
Tramite questo campo è possibile attivare ed al tempo stesso indicare, la valuta aggiuntiva in cui si vorrà gestire il bilancio. Per maggiori dettagli si rimanda alla documentazione del relativo capitolo del modulo di bilancio C5E010.
 :  : FLD T$C57B **Cambio Traduzione**
Indica la metodo generale che verrà applicato ai conti per ottenere il valore tradotto. Tale criterio potrà essere sovrascritto a livello di conto, tramite l'apposito campo previsto sulla tabella C5B. I valori possibili sono i seguenti : 
* 1. Cambio Storico su conti economici, Cambio Attuale su conti patrimoniali
* 2. Cambio Storico su tutti i conti
* 3. Cambio Medio su conti economici, Cambio Attuale su conti patrimoniali
* 4. Cambio Attuale su tutti i conti
Ognuno dei criteri ha il seguente comportamento : 
* Cambio Storico :  viene ripreso il valore memorizzato sulle righe contabili con il cambio valido alla data dell'operazione (alla data documento o alla data registrazione).
* Cambio Attuale :  viene ripreso il cambio valido alla data di interrogazione del bilancio e a quel cambio viene tradotto il saldo del conto
* Cambio Medio :  viene ripreso il cambio medio valido alla data di interrogazione del bilancio e a quel cambio viene tradotto il saldo del conto. NOTA BENE :  il valore del cambio medio va indicato puntualmente nel file dei cambi con il tipo cambio indicato nel campo successivo.
 :  : FLD T$C57C **Tipo Cambio Medio**
Se a livello di tabella C57 o anche solo per eccezione su un conto, viene indicato come metodo di traduzione della valuta il tipo cambio medio è necessario indicare il tipo cambio che si utilizzare per individuare il cambio medio da applicare in bilancio ad una data. Se questo campo non viene valorizzato, ai conti che prevedono l'utilizzo del cambio medio, viene applicato il cambio corrente.
 :  : FLD T$C57D **Exit controllo registrazione**
Il valore di questo flag indica quale è il programma di exit per gli eventuali controlli e  decodifiche della registrazione.
E' possibile col ! ricercare le lettere relative ai programmi disponibili (C5C54__*).
E' disponibile il sorgente del programma di esempio C5C54__X nel file C5SRC della libreria SMEDEV.
 :  : FLD T$C57E **Metodo oscillazione**
Il campo fa riferimento al metodo di trattamento delle oscillazioni aperte alla fine di un esercizio e saldate in esercizi successivi.
* " " :  Storico
** Le oscillazioni di fine esercizio vengono rilevate ed immediatamente stornate al giorno successivo. In questo modo risultano rilevanti per la redazione del bilancio, ma subito annullate per effetto dello storno nel nuovo esercizio.
** Le oscillazioni sugli incassi/pagamenti in corso d'esercizio vengono sempre applicate rispetto al cambio storico delle partite, non tenendo conto degli adeguamenti degli esercizi precedenti.
** Sulla base delle due precedenti affermazioni è necessario considerare che i conti in gioco per la rilevazione delle differenza cambio (tutti confluenti nella medesima linea di riclassifica CEE D13), possono avere nella loro sommatoria un saldo corretto, ma non nella loro composizione. Per tale motivo sfruttando anche la scheda messa a disposizione nel modulo bilanci, sarà necessario effettuare delle rettifiche manuali (direttamente sui saldi totali).
* "1" :  Adeguato
** Le oscillazioni di fine esercizio vengono rilevate e mantenute.
** Le oscillazioni sugli incassi/pagamenti in corso vengono sempre applicate rispetto al cambio adeguato delle partite, alla fine dell'esercizio n-1.
** Non è rilevante quando la registrazione di fine esercizio n-1 sia già stata effettuata, ma è necessario che sia stato inserito il cambio di fine esercizio n-1 (prerequisito senza il quale non è possibile completare le registrazioni dell'esercizio n, se riferite a partite di esercizi precedenti).
** Con questo metodo non è necessario far alcuna rettifica manuale, ne a fine esercizio ne in corso d'esercizio.
** NOTA BENE :  per effetto di questo metodo, se una partita viene chiusa nell'esercizio n fin tanto che non viene effettuata la rilevazione di fine esercizio n-1, la partita sarà chiusa in valuta, ma aperta in valuta di conto (per l'importo dell'oscillazione di fine esercizio n-1).
** NOTA BENE 2 :  sempre per effetto di questo metodo, alla scrittura delle registrazione di fine esercizio n-1, il pgm lancerà anche il ricalcolo nell'esercizio n di tutte le oscillazioni riferite a partite aperte alla fine dell'esercizio n-1. Questo al fine di garantire la perfetta quadratura dei centesimi. Se questa operazione non andasse a buone fine verrebbe segnalato nel log di stampa.
** NOTA BENE 3 :  E' possibile passare da un metodo all'altro solo a partire dalla data inizio di un esercizio e solo dopo che l'esercizio precedente sarà stato chiuso. Sarà necessario riconfermare tutte le registrazioni contenenti oscillazioni cambio già registrate nell'esercizio a partire dal quale si attiva il nuovo metodo.

Qualunque sia il metodo di rilevazione delle oscillazioni si ricorda che il controllo del riallineamento civilistico/fiscale è possibile attraverso una specifica scheda posta nel menù dei bilanci.

 :  : FLD T$C57F **Date Iva**
Se valorizzato ad 1, sia data operazione iva che data competenza iva vengono proposte assumendo la data registrazione. Viceversa : 
* Nelle registrazioni da FE, la data competenza iva viene assunta in base alla data di ricezione e la data di operazione viene assunta dalla data delle bolle o dalla data fattura
* Nelle registrazioni manuali, la data competenza iva viene assunta dalla data registrazione e e la data di operazione viene assunta dalla data fattura

 :  : FLD T$C57G **Periodo Adeguamento**
Tale impostazione si riferisce al metodo di oscillazione adeguato :  nella normativa italiana l'adeguamento cambi viene fatto a fine esercizio. Qualora sorgesse l'esigenza di applicare tale adeguamento anche durante l'esercizio, tramite tale parametro è possibile indicarlo.
NOTA BENE :  è prerequisito che a seguire di tale adeguamento il periodo adeguato venga consolidato (NdA esigenza sorta su ambiente cinese).

 :  : FLD T$C57H **Ctr.Dic.Intento Pas**
Nelle registrazioni di fatture ciclo passivo, questa impostazione abilita il controllo interrattivo delle dichiarazioni di intento.

 :  : FLD T$C57I **Disabilita Forz.F20**
Nelle registrazioni di fatture non è possibile forzare tramite F20 il documento qualora sia già stato registrato a parità di ente, data documento e numero documento.

 :  : FLD T$C57L **Mailing List**
Mailing list utenti. Questa mailing list viene usata per gli alert relativi al controllo quadrature master C5 ed importazione cambi giornalieri tramite SmeUp Provider.

 :  : FLD T$C57M **Tipo Reg. Ft. FE**
Tipo registrazione da applicare come proposta delle registrazioni di fatture fornitori costruite a partire dagli xml della FE passiva.

 :  : FLD T$C57N **Tipo Reg. Nt. FE**
Tipo registrazione da applicare come proposta delle registrazioni di note d'accredito fornitori costruite a partire dagli xml della FE passiva.

 :  : FLD T$C57O **Tipo Reg. Ft.Reverse**
Tipo registrazione da applicare come proposta delle registrazioni di fatture fornitori con iva reverse charge costruite a partire dagli xml della FE passiva.

 :  : FLD T$C57P **Tipo Reg. Nt.Reverse**
Tipo registrazione da applicare come proposta delle registrazioni di note d'accredito con iva revesse charge fornitori costruite a partire dagli xml della FE passiva.

 :  : FLD T$C57Q **Exit FE Passiva**
Exit con prefisso "C5_093_01" che permette di applicare alcune logiche personali al processo di registrazione delle fatture elettroniche passive. Si veda la documentazione applicativa corrispondente per maggiori dettagli.

 :  : FLD T$C57R **Exit FE Pas. Import.**
Indica il suffisso del programma (C5_093M_xx dove xx è il suffisso) utilizzato per poter importare
fatture in formato Xml residenti su una cartella dell'IFS. Esiste un programma di esempio chiamato
C5_093M_01.

 :  : FLD T$C57S **Impon. Passivo LIPE**
Permette di impostare la modalità di estrazione dell'imponibile delle fatture passive all'interno
della liquidazione periodica. L'analisi letterale delle istruzioni del modello indica, infatti, di
indicare nel rigo VP3 l'imponibile delle operazioni rilevate sui registri IVA nel mese in
elaborazione mentre a livello di imposta (rigo VP5) le istruzioni indicano di rilevare le operazioni
detratte nel mese in elaborazione.
Qualche fiscalista ritiene che questo comportamento sia anomalo e, quindi, preferisce indicare nel
rigo VP5 l'imponibile delle operazioni detratte nel mese allineandosi di fatto a quanto rilevato nel
rigo VP3.
Compilando con 1 il campo sarà possibile estrarre l'imponibile delle fatture per data competenza IVA
anzichè per data registrazione.
Esempio :  Fattura del 31/01/XX ricevuta il 05/02/XX. Data registrazione :  05/02/XX, data competenza
IVA :  31/01/XX. L'operazione, quindi, verrà protocollata sui registri IVA di febbraio 20XX e detratta
nella liquidazione IVA di gennaio 20XX.
Lasciando il campo blank l'imponibile dell'operazione verrà estratto nel rigo VP3 del mese di
febbraio mentre l'imposta verrà esposta nel rigo VP5 del mese di gennaio.
Compilando il campo con 1 imponibile e imposta dell'operazione verranno totalizzati rispettivamente
nel rigo VP3 e VP5 del mese di gennaio.
