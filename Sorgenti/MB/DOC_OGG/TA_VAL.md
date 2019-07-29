# VAL - Codici divisa
 :  : DEC T(ST) K(VAL)
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC Descrizione divisa
 :  : FLD T$VAL6 __Ordine di inser.__
È utilizzato dalla gestione cambi SME_up, ed indica l'ordine di gestione delle valute nella manutenzione giornaliera dei cambi.
 :  : FLD T$VALE __Sigla valuta__
È la sigla con cui viene identificata la valuta, normalmente è la sigla internazionale (campo presente nella tabella).
 :  : FLD T$CC,1 __Conto 1 (dare)__
Si può inserire un conto contabile da utilizzare nella gestione di contabilità industriale.
 :  : FLD T$CC,2 __Conto 2 (avere)__
Si può inserire un conto contabile da utilizzare nella gestione di contabilità industriale.
 :  : FLD T$VALB __Cambio Bgt__
Esiste la possibilità di inserire un cambio budget per la valuta.
Da notare che la gestione di questo campo è resa superflua dalla gestione cambi (vedi i tipi cambi)
 :  : FLD T$VALA __Cambio std__
Esiste la possibilità di inserire un cambio standard per la valuta.
Da notare che la gestione di questo campo è resa superflua dalla gestione cambi (vedi i tipi cambi)
 :  : FLD T$VALC __Cambio eff__
Esiste la possibilità di inserire un cambio effettivo per la valuta. Da notare che la gestione di questo campo è resa superflua dalla gestione cambi (vedi i tipi cambi).
 :  : FLD T$DIVR __Divisa principale o di riferimento__
Utilizzata per parzializzare gestioni, interrogazioni e stampe.
 :  : FLD T$VAL2 __Data ingresso EURO__
Definisce la data oltre la quale la valuta verrà considerata a cambio fisso. Nelle conversioni dopo tale data, in cui è coinvolta la divisa in essere, il valore del cambio utilizzato sarà quello fisso valido alla data (nel file dei cambi SMEUP tipo cambio 'E'). Nella gestione dell'anagrafico CAMBI, l'attivazione del cambio fisso comporta l'impossibilità di inserire un tipo cambio diverso da questo, dopo la data di attivazione.
 :  : FLD T$VAL4 __Decimali di arrot.__
Indica quanti decimali si devono utilizzare nei calcoli di conversione degli importi da una valuta alla valuta a cui si riferisce la tabella (ad es. calcoli di fattura)
 :  : FLD T$VALD __Nessun decimale (arrotondamento all'intero)__
Da 1 a 6 = da 1 a 6 decimali.
Il campo è di immissione obbligatoria. Tuttavia, nel caso non sia specificato alcun valore (tipicamente tabella deviata), viene effettuato arrotondamento sempre per eccesso con 0 decimali per la valuta corrente, e arrotondamento eccesso/difetto al 5, per valute diverse dalla corrente (vecchio metodo di arrotondamento).
 :  : FLD T$VAL5 __Tipo arrotondamento__
Indica il modo di arrotondare i valori nei calcoli di conversione di valuta; questo valore è vincolato dalla scelta del numero di decimali ed i valori possibili sono : 
- + = sempre per eccesso;
- - = sempre per difetto;
- H = Per eccesso o difetto al "5";
- T = Per trascinamento. La differenza del valore creatasi con l'arrotondamento viene portata sulla riga successiva.

Il campo è di immissione obbligatoria, ma nel caso non sia specificato alcun valore, il valore assunto per tale campo è H, salvo che non sia specificato alcun valore per il campo "decimali in arrotond.".
 :  : FLD T$VAL8 __Tipo arrotond.IVA__
Indica il modo di arrotondare i valori nel calcolo dell'IVA; questo valore è vincolato dalla scelta del numero di decimali ed i valori possibili sono : 
- + = sempre per eccesso;
- - = sempre per difetto;
- H = Per eccesso o difetto al "5".
Il campo non è di immissione obbligatoria, con le seguenti considerazioni : 
- modulo applicativo C5 :  campo necessario;
- modulo applicativo V5 :  se non specificato alcun valore, viene utilizzato il corrispondente campo della tabella 'V51'.
 :  : FLD T$VALF __Codice standard__
È la sigla internazionale della valuta (elemento tabella V§*DI).
 :  : FLD T$VAL9 __Tolleranza Co.Ge.__
L'importo qui indicato è quello che viene preso in sostituzione al limite previsto di default per la forzatura della quadratura delle registrazioni della contabilità smeup.
Es. ponendo di indicare 2, se la registrazione squadra per un importo <=2 unità, tale differenza verrà automaticamente corretta, mentre un importo superiore verrà segnalato come errore.
 :  : FLD T$VAL9 __Tolleranza Iva__
L'importo qui indicato è quello che viene preso in sostituzione al limite previsto di default (0,01) per la forzatura della quadratura dei calcoli Iva della contabilità smeup.
