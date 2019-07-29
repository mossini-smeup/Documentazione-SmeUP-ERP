# C5U - Registrazioni automatiche
 :  : DEC T(ST) K(C5U)
## OBIETTIVO
Definire le impostazioni che guidano la scrittura delle registrazioni automatiche. Il codice dell'elemento di questa tabella deve essere un codice fisso V2/C5AUT, eventualmente con un suffisso, presente (e di un determinato tipo) in funzione dell'elemento.
_9_Esempio :  se il codice fisso è FODCP (differenze cambio positive nel pagamento a fornitori), l'elemento di tabella è FODCPxxx, dove xxx può essere una valuta.
Per un'implementazione di questi valori, riferirsi al S&P delle registrazioni automatiche.
.
. IVAVE     IVA vendite
. IVAAC     IVA acquisti
. IVACR     IVA per corrispettivi
.
.  Definiscono i conti contabili su cui verranno scritte le righe di IVA (vendite/acquisti/corrispettivi)
.
. IVAVK     IVA vendite ad esigibilità differita
. IVAAK     IVA acquisti ad esigibilità differita
.
.  Se presenti definitiscono i conti e le causali utilizzati in sostituzione dei parametri normali
se la registrazione risulta essere ad esibigilità differita
.
. IVAIN     IVA indetraibile

.  Definiscono i conti contabili su cui verranno pilotate le righe di IVA indetraibile ed il suo storno. E' anche possibile definire una causale di registrazione specifica. Nel caso in cui non venga compilato il campo Conto contabile l'IVA indetraibile verrà registrata sul conto IVA definito nella IVAVE per le vendite e nel IVAAC per gli acquisti

. IVACO     Contropart.IVA indetraibile

 Come contropartita Iva indetraibile verrà assunto il conto di costo specificato nell'elemento IVACO. Nel caso in cui questo elemento non sia compilato, il programma costruirà la contropartita utilizzando il conto di costo presente nella registrazione contabile ed associato all'assoggettamento IVA indetraibile.
Se nella registrazione contabile sono presenti più righe di costo il programma procederà ad una ripartizione proporzionale dell'importo dell'IVA indetraibile tra i costi che riportano  l'assoggettamento IVA corrispondente alle righe IVA.
Si deduce da quanto detto che in una registrazione di fattura con assoggetamenti IVA indetraibile, sarà OBBLIGATORIO inserire sulle righe di costo che compongono l'imponibile per l'IVA indetraibile, i relativi assoggettamenti.

. IVAED     Incasso/Pagamento IVA esigibilità differita
. IVAEA     Incasso/Pagamento IVA esigibilità differita su acquisti
. IVAEV     Incasso/Pagamento IVA esigibilità differita su vendite
.
.  Definisce il conto contabile su cui verranno registrate le righe di storno dell'iva ad esigibilità differita. Viene utilizzato l'elemento IVAED se non vengono codificati i due specifici.
.
. IVACE     Contropart.IVA Intracomunititaria

Definisce i conti contabili su cui verranno registrate le righe per lo storno dell'IVA intracomunitaria. Nel campo Conto contabile andrà inserito il conto IVA vendite intracomunitarie che deve pareggiare il conto IVA acquisti intracomunitari.

. IVARE     Contropart.IVA Reverse Charge
.
.  Definisce le righe per lo storno dell'IVA con reverse charge. Nel campo Conto contabile andrà inserito il conto IVA vendite che deve pareggiare il conto IVA acquisti.
.
. IVARP     Compensazione IVA Conto Erario
. IVARV     Compensazione IVA Contropartita
.
.  Definiscono le righe per la scrittura della registrazione di compensazione automatica del credito IVA verso un'altra azienda dell'eventuale gruppo aziendale
.
. IVAGC     Giroconto liquidazione
.
.  Definisce le righe utilizzate in liquidazione per la scrittura della registrazione automatica di chiusura dell'IVA verso l'erario. E' necessario indicare il tipo e la causale della registrazione generata e il codice del conto contabile su cui verrà riportata la differenza  tra IVA vendite e acquisti.
.
. PADAA     Altra Pratica di Pagamento Clienti
. PADAB     Bonifici a Clienti
. PADA$     Bonifico estero a Clienti
. PADAC     Presentaz.Titoli
. PADAD     Presentaz.Assegni
. PADAM     M.Av. Clienti
. PADAP     Contrassegni
. PADAR     R.I.D. Clienti
. PADAS     Cessione Factoring
. PADAT     Presentaz.Tratte
. PADAZ     Presentaz.Altri Titoli
. PADA2     Presentaz.RiBa Salvo Buon Fine
. PADA3     Presentaz.RiBa all'Incasso
. PADA4     Presentaz.RiBa allo Sconto
. PADA5     Presentaz.Anticipi su Effetti
. PADA9     Contabilizzazione Effetti
. PADA£     Presentaz.Anticipi su Fatture
. PADPA     Altra Pratica di Pagamento Fornitor
. PADPB     Bonifico a Fornitori
. PADP$     Bonifico estero a Fornitori
. PADPC     Presentaz.Cessioni
. PADPD     Presentaz.Assegni
. PADPZ     Presentaz.Altri Titoli
. PADP3     Ritiro RiBa Fornitori
.
.  Definiscono le righe utilizzate nella creazione delle registrazioni automatiche di pagamento tramite pratica. NB. per tutti elementi è prevista un'estensione che punti al tipo rapporto, fa eccezione l'elemento PADAS che come estensione ha fisso "0" se il rapporto è pro-solvendo e "1" se pro-soluto.
.
. DARCR     Dare per corrispettivi
. AVECR     Avere per corrispettivi
.
.  Definiscono le righe di dare/avere utilizzate nella registrazione dei corrispettivi
.
. CLDCP     Pag.cli. Diff.Cambio Att.
. CLDCN     Pag.cli. Diff.Cambio Pass.
.
.  Definiscono le righe di oscillazione cambio di soggetti clienti
.
. CODCP     Doc.Con. Diff.Cambio Att.
. CODCN     Doc.Con. Diff.Cambio Pass.
.
. CLABP     Pag.cli. Abbuono Attivo
. CLABN     Pag.cli. Abbuono Passivo
.
.  Definiscono le righe di abbuono a soggetti clienti
.
. FODCP     Pag.forn. Diff.Cambio Att.
. FODCN     Pag.forn. Diff.Cambio Pass.
.
.  Definiscono le righe di oscillazione cambio di soggetti fornitori
.
. FOABP     Pag.forn. Abbuono Attivo
. FOABN     Pag.forn. Abbuono Passivo
.
.  Definiscono le righe di abbuono a soggetti fornitori
.
. ENASA     Enasarco carico ente
. ENASC     Enasarco clienti
. ENAAZ     Enasarco azienda
. ENAAC     Enasarco azienda - contropar.
. ENAAN     Enasarco azienda - anticipo
. ENACN     Enasarco azienda - controp.anticipo
. ENACO     Contropartita in contabilizzazione fatture
.
. INSOL     Insoluti
.
. CHIEC     Chiusura economico
. CHIPA     Chiusura patrimoniale
. APEPA     Apertura patrimoniale
.
.  Definiscono le righe relative alla registrazione automatica di chiusura del conto economico dello stato patrimoniale e l'apertura dello stato patrimoniale
.
. PARUT     Pass.risultato :  utile
. PARPE     Pass.risultato :  perdita
.
.  Assumono due significati differenti a seconda che siano state codificate anche le registrazioni automatiche PARUP e PARPP : 
.  A) PARUP e PARPP NON Codificate
.     Definiscono le righe relative alla rilevazione del conto patrimoniale del risultato d'esercizio
.  A) PARUP e PARPP Codificate
.     Definiscono le righe relative alla rilevazione del conto economico del risultato d'esercizio
.
. PARUP     Pass.risultato :  utile
. PARPP     Pass.risultato :  perdita
.
.  Definiscono le righe relative alla rilevazione del conto patrimoniale del risultato d'esercizio
.
. RITEN     Ritenuta
. RITPR     Ritenuta previdenziale
.
.  Definiscono le righe relative alla rilevazione del versamento di ritenute di soggetti fornitori. Come suffisso dell'elemento è accettato il codice prestazione (ad esempio l'elemento RITEN1040 definirà la registrazione contabile per percipienti con codice tributo 1040)
Anche se non è indicato nel pgm di gestione delle righe automatiche è inoltre possibile specificare come ulteriore desinenza la causale prestazinoe (es. se creo l'elemento RITEN1040M, questo elemento è il primo ad essere preso in considerazione se viene utilizzato il codice tributo 1040 con la causale prestazione M).
.
. RITEC     Ritenuta clienti
. RITPC     Ritenuta previd.clienti
.
.  Definiscono le righe relative alla rilevazione del versamento di ritenute di soggetti clienti
.
. ONPRE     Oneri previdenziali
.
. CAINS     Generazione Insoluto
. CAPRO     Generazione Protesto
. CARIC     Generazione Richiamo RiBa
.
.  Definiscono le righe per la scrittura delle registrazioni di insoluto/protesto/richiamo
.
. CASPI     Gen.Spese Insoluto Azienda
. CASPP     Gen.Spese Protesto Azienda
. CASPR     Gen.Spese Richiamo Azienda
. CASPA     Gen.Spese Amministrative
.
.  Definiscono le righe delle spese di insoluto/protesto/richiamo e le eventuali spese aggiuntive.
.
. CACOP     Gen.Contr.Spese carico Sog.
.
.  Definiscono la riga di contropartita nel caso le sopradette spese vengano addebitate al cliente
.
. CASPB     Gen.Spese Bancarie
.
.  Definiscono le righe delle spese bancarie rilevate tramite la tesoreria
.
. SCFAT     Sconto Finanziario Attivo
. SCFPA     Sconto Finanziario Passivo
.
.  Definiscono le righe relative all'applicazione dello sconto finanziario
.
. PGIMM     Pagamento immediato
.
.  Definiscono le righe di contropartita della registrazione di pagamento immediato
.
. STADA     Stanziamento immediato dare
. STAAV     Stanziamento immediato avere
.
.  Definiscono le righe per la scrittura delle registrazioni di stanziamento immediato
.
. GFANT     Giroconto finanziamento anticipo
.
. RISAT     Risconti attivo
. RISPA     Risconti passivo
. RATAT     Ratei attivo
. RATPA     Ratei passivo
.
.  Definiscono le righe per la scrittura delle registrazioni di risconti/ratei di fine anno.
.
. FATDG     Fattura Dogana
.
.  Definisce il tipo registrazione da utilizzare per derivare la fattura della dogana a partire da una fattura fornitore. Vanno impostati il tipo e la causale registrazione mentre il conto viene
determinato a partire dal codice IVA.
.
. FIRR      Contabilizzazione Firr
. FIRRC     Contropartita contabilizzazione Firr
. PRAGE     Agente per contabilizzazione Liquidazione delle provvigioni
. PRPRO     Liquidazione provvigioni
. COAGE     Agente per contabilizzazione costo provvigioni
. COPRO     Costo per provvigioni
.
.  Definiscono le righe per le contabilizzazioni dal modulo provvigioni
.
. RBAN      Riconciliazione Estratto Conto
.
.  Definisce il tipo registrazione da utilizzare nella generazioni di movimenti a partire da dai movimenti trasmessi tramite remote banking dagli istituti di credito.
.
. FINRA     Finanziamenti - Rate
. FINES     Finanziamenti - Estinzione
. FINSP     Finanziamenti - Spese
.
.  Definisce i tipi di registrazione/conti da utilizzare nella generazioni di movimenti del piano di ammortamento dei finanziamenti.
.
.
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC **Descrizione**
Descrive la registrazione automatica
 :  : FLD T$C5UA **Tipo registrazione**
È un elemento TA/C5D. In alcuni casi (in funzione dell'elemento V2/C5AUT), si genera una registrazione automatica (ad esempio per le fatture doganali), in altri solo delle righe che si accodano ad una registrazione esistente (ad esempio abbuoni, iva indetraibile, ecc.).
Nel primo caso si inserisce in questo campo il tipo registrazione che si andrà a generare.
 :  : FLD T$C5UB **Causale registrazione**
È un elemento TA/C5V. Si imposta nel caso in cui si generino solo righe automatiche, che assumono come causale questo valore.
 :  : FLD T$C5UC **Conto contabile**
È un elemento TA/C5B. Si imposta il conto che si inserisce nella riga automatica. La contropartita verrà assunta in modo specifico per ogni tipo di registrazione automatica.
Inoltre, per gli elementi riguardanti la contabilizzazione delle pratiche, se tale conto risulta collegato ad un tipo contatto, provoca la contabilizzazione dettagliata per ente del conto stesso.
 :  : FLD T$C5UD **Importo associato**
Si inserisce in questo campo il valore che, in alcuni tipi di registrazione automatica, si ha la necessità di associare alla registrazione.
_9_Esempio :  nel caso degli abbuoni, si inserisce l'importo massimo che è consentito abbuonare.
Riferirsi al S&P per il dettaglio dei casi previsti.
 :  : FLD T$C5UF **Contabilizzazione dettagliata**
La contabilizzazione di un pratica genera una registrazione di pagato a fronte di rate di dovuto. Se dettagliata per ogni rata di pagato, si genera una riga di registrazione. Se non dettagliata, si generano tante righe di registrazione quanti sono gli enti presenti nelle rate; le rate appartenenti allo stesso ente sono associate alla corrispondente riga di registrazione.
 :  : FLD T$C5UG **Contabilizzazione Maturazione Effetti**
È un elemento V2SI/NO. Se valorizzato, indica solo per gli elementi che rappresentano una pratica che è prevista la contabilizzazione della maturazione degli effetti, cioè l'accredito sul c/c dell'importo degli effetti alla data di maturazione degli stessi. Se viene impostato il relativo flag sulla tabella verrà gestita anche la registrazione di presentazione effetti con carico del conto sbf.
 :  : FLD T$C5UH **Tipo registrazione banca**
È un elemento TA/C5D. Viene utilizzata nelle pratiche quando si esegue la contabilzzazione banca.
 :  : FLD T$C5UI **Causale registrazione banca**
È un elemento TA/C5V. Viene utilizzata nelle pratiche quando si esegue la contabilizzazione banca.
 :  : FLD T$C5UL **Dettaglio contropartita**
Indica il valore di default che definisce il tipo di dettaglio per le contropartite che si vuole utilizzare nella contabilizzazione delle pratiche aperte. Può assumere i seguenti valori : 
- ' '=Unica
- '1'=Dettaglio
- '2'=Scadenza
- '3'=Mese di scadenza
 :  : FLD T$C5UM **Contabilizzazione Interattiva**
È un elemento V2SI/NO. Se valorizzato, al momento della contabilizzazione premendo F06 il lavoro non verrà eseguito sottomendolo in batch, ma interattivamente con la possibilità di entrare direttamente in gestione della registrazione che si sta inserendo.
 :  : FLD T$C5UN **Da non stampare**
Per gli elementi che identificano i parametri di contabilizzazione di una pratica indica se per
la pratica viene gestita o meno la stampa della stessa.
 :  : FLD T$C5UO **Da non trasmettere**
Per gli elementi che identificano i parametri di contabilizzazione di una pratica indica se per
la pratica viene gestita o meno la trasmissione della stessa.
 :  : FLD T$C5UP **Da non contabiliz.**
Per gli elementi che identificano i parametri di contabilizzazione di una pratica indica se per
la pratica viene gestita o meno la contabilizzazione della stessa.
 :  : FLD T$C5UQ **Data inizio validità**
Per alcuni elementi identifica la data registrazione da cui l'automatismo inizia ad essere attivo.
Attualmente l'unico elemento per cui questo risulta rilevante è l'elemento INCIC
