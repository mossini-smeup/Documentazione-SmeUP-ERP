 ### UTILIZZO RICHIESTA PARAMETRI

In queste schede vengono evidenziate le possibilità previste dall'utilizzo della richiesta parametri, in tutte le modalità grafiche previste dall'attributo UirMGr - Modalità Grafica : 
 * C :  Richiedi ed Esegui in Subsezione (Assunto)
 * B :  Richiedi in Finestra, Esegui in Subsezione
 * D :  Richiedi in Subsezione, Esegui in Nuova Finestra
 * E :  Solo Richiesta in Subsezione

 ### NOTE OPERATIVE

Tramite i Tag G.SUB.UPA, G.SET.UPA e D.FUN.UPA è possibile lanciare una funzione, ponendo prima all'utente la richiesta di compilazione (che può essere obbligatoria o meno) di un questionario di domande.

Questa definizione non permette di comprendere la differenza fra i questionari definiti tramite la richiesta di configurazione da quelli previsti tramite le richieste parametri. La differenza sostanziale sta nel fatto che le richieste parametri permettono di definire una serie di domande, con caratterizzazioni limitate, potendo però descrivere le domande direttamente nello script di scheda. Risulta quindi più opportuno rispetto alla richiesta di configurazione qual'ora le domande siano poche e non necessitino di caratteristiche particolari (es. pgm di exit).

* Il tag G.SUB.UPA serve solo per identificare la subsezione, come una un subsezione che presenterà le sopracitate caratteristiche.
* Il tag G.SET.UPA serve per indicare quale sarà il questioni che si andrà utilizzare e varie caratteristiche grafiche tramite le quali, il questionario e la funzione stessa verranno posti all'utente.
* Il tag D.FUN.UPA serve per indicare quale funzione deve essere infine eseguita. Questo tag non si differenzia dal normale tag di funzione D.FUN.STD se non che per un aspetto :  tutte le risposte alle domande del questionario verranno automaticamente passate come parametri di INPUT alla funzione indicata in questo formato "codicedomanda(valorerisposta)", ma è inoltre possibile indicare un utilizzo specifico di tali parametri all'interno della funzione tramite la seguente dicitura $IN.codicedomanda. Quindi ponendo di avere come unica domanda con codice domanda "CD", mi viene richiesto un cliente, se in D.FUN.UCF specifico "F(EXD;*SCO;) 2(MB;SCP_SCP;XXX)" mi verrà eseguita la funzione "F(EXD;*SCO;) 2(MB;SCP_SCH;XXX) INPUT(CD(valorerisposta))", viceversa se specifico "F(EXD;*SCO;) 1(CN;CLI;$IN.CD) 2(MB;SCP_SCP;XXX)" mi verrò eseguita la funzione "F(EXD;*SCO;) 1(CN;CLI;valorerispostaCD) 2(MB;SCP_SCH;XXX) INPUT(CD(valorerisposta))". Quando descritto è possibile anche nelle configurazioni, ma nella richiesta parametri è inoltre possibile definire domande nei sei oggetti della funzione indicando semplicemente un "$" nella definizione di questi oggetti. Il lancio della scheda di un cliente potrebbe anche quindi essere definito in questo modo "F(EXD;*SCO;) 1(CN;CLI;$)". In questo caso verrà posta come unica domanda l'indicazione di un codice cliente.

Per il dettaglio sulle possibilità grafiche si rimanda all'help del wizard G.SET.UPA, mentre ci si sofferma solo sul fatto che è possibile tipizzare dinamicamente le domande indicano nel campo "tipo oggetto" della domanda non un tipo oggetto fisso ma la seguente codifica "(codicedomandaorigine)". In questo modo il campo sarà tipizzando con il valore indicato nella domanda indicata come origine. E' possibile anche avere due campi come riferimento (es. (codicedomandaorigine1)(codicedomandaorigine2)) o avere una tipizzazione parziale (es. CN (codicedomandaorigine1)).

Esempio 1) Lancio scheda di un oggetto qualsiasi
 :  : PAR F(04) L(MON)
G.SEZ Pos(1)
G.SUB.UPA Tit="*NONE"
G.SET.UPA UirCtx="M_LOSUIR\UPA\1" UirMGr="C"
D.FUN.UPA F(EXD;*SCO;) 1($;$;$)

Esempio 2) Lancio di una scheda con parametri di Input
 :  : PAR F(04) L(MON)
G.SUB.UPA Tit="*NONE"
G.SET.UPA UirIPa="Nam(Tip) Ctr(O) Dft(TA) Ogg(OG) Tit(Tipo) Lun(02)|Nam(Par) Ctr(O) Ogg(OG(Tip)) Tit(Parametro) Lun(10)|Nam(Cod) Ctr(O) Ogg((Tip)(Par)) Tit(Codice) Lun(15)|Nam(Dat) Ogg(D8*YYMD) Tit(Data) Lun(10)|Nam(Num) Ogg(NR) Tit(Numero) Lun(10)" UirCtx="M_LOSUIR" UirMGr="C"
D.FUN.UPA F(EXD;*SCO;)  2(MB;SCP_SCHESE;LOSUIR) 4(;;EXDPAR)


 ### NOTE SU ESEMPI

* Negli esempi riportati a seguire vengono evidenziate alcune delle possibilità disponibili nella definizione delle domande.
* La funzione che viene eseguita alla compilazione del questionario è sempre una matrice in cui vengono evidenziati i parametri ricevuti.
