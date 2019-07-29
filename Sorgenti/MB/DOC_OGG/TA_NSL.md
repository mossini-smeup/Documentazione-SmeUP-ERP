# NSL - LISTE DI DISTRIBUZIONE
 :  : DEC T(ST) K(NSL)
## N.B.
Per il buon funzionamento dell'applicazione, codificare come primo elemento della lista NSLxx il progressivo "**". Questo
identifica il tipo standard degli elementi che saranno contenuti nella lista.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM __Progressivo__
Il campo progressivo ha la funzione di rendere univoco un record di lista. Infatti, potendo caricare nella stessa lista
oggetti diversi (Esempio :  dei dipendenti e dei centri di lavoro o altri), si può introdurre lo stesso
elemento AAA001, il quale corrisponde sia ad un dipendente che ad un centro di lavoro.
 :  : FLD T$DESC __Descrizione__
Descrizione elemento in fase di imputazione dell'elemento viene decodificata tramite un apposito PGM.
 :  : FLD T$TCEL __Tipo codice__
Decodificato nella tabella *CNTT. Può identificare la tipologia del codice utilizzato (DI=Dipendente, CL=Cliente...).
 :  : FLD T$PCEL __Parametro__
È un completamento del tipo codice. _9_Esempio :  se tipo codice
è  tabella, il parametro specifica quale TA DIP tabella dipendenti.
 :  : FLD T$COEL __Codice elemento__
Fa parte dei codici identificati dal tipo codice e dal parametro. Se TA + DIP, l'elemento non può essere altro che un
elemento della tabella dipendenti.
 :  : FLD T$ATAU __Attribuzione automatica__
Mettendo una X in questo campo, si avrà l'attribuzione automatica dell'opzione di invio quando si accede alle funzioni
di distribuzione. In pratica, questo campo serve per impostare i destinatari fissi delle distribuzioni.
 :  : FLD T$VRAU __Domanda di default__
Inserire in questo campo il codice della domanda che dovrà apparire per default sulla videata di dettaglio di un
invio.
 :  : FLD T$VRFI __Domanda fissa__
Inserendo una X in questo campo, il campo "Domanda della videata di dettaglio della distribuzione" sarà protetto e quindi
non modificabile. Questo campo deve essere utilizzato in combinazione con il campo "Domanda di default".
 :  : FLD T$NOCO __Ometti conferma__
Inserendo una X in questo campo, in fase di invio non verrà presentata la videata di dettaglio, se è stata specificata
la domanda di default.
Inserendo una X in questo campo, il campo "Data richiesta risposta" sarà di immissione obbligatoria.
 :  : FLD T$VSAU __Risposta di default__
Inserire in questo campo il codice della risposta che dovrà apparire per default sulla videata di dettaglio di
risposta alle distribuzioni.
 :  : FLD T$VSFI __Risposta fissa__
Inserendo una X in questo campo, il campo "Risposta della videata di dettaglio delle risposte alle distribuzioni" sarà
protetto e quindi non modificabile. Questo campo deve essere utilizzato in combinazione con il campo "Risposta di default".
 :  : FLD T$DSAU __Data risposta automatica__
Inserendo una X in questo campo, il campo "Data risposta" sarà automaticamente compilato con la data odierna.
 :  : FLD T$DSFI __Data risposta fissa__
Inserendo una X in questo campo, il campo "Data risposta" sarà protetto e non modificabile.
 :  : FLD T$CLAU __Classe Autorizzazione__
Specifica la classe di autorizzazione legata all'elemento.
 :  : FLD T$TIIN __Tipologia Inoltro__
Specifica la tipologia di notifica dell'avvenuta distribuzione al destinatario (Per esempio messaggio o posta Office).
 :  : FLD T$P1IN __Parametri Inoltro__
Specifica i parametri di inoltro della distribuzione al destinatario, qualora non si utilizzi come tipo codice
destinatario un oggetto UP o CN (nel qual caso i parametri di inoltro vengono ricavati direttamente dal sistema),
oppure si vuole forzare un indirizzo diverso da quello definito nell'anagrafica enti.
I parametri sono da considerare come un campo unico, risultante dalla concatenazione dei 3.
Se l'indirizzo così formato non contiene la '@', il nome del dominio verrà ereditato dal secondo parametro della
tabella A£I.
 :  : FLD T$P2IN.T$P1IN __Parametri Inoltro__
 :  : FLD T$P3IN.T$P1IN __Parametri Inoltro__
