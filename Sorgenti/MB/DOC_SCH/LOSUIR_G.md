 ### UTILIZZO RICHIESTA QUERY

In queste schede vengono evidenziate le possibilità previste dall'utilizzo della richiesta di una query, in tutte le modalità grafiche previste dall'attributo UirMGr - Modalità Grafica : 
 * C :  Richiedi ed Esegui in Subsezione (Assunto)
 * B :  Richiedi in Finestra, Esegui in Subsezione
 * D :  Richiedi in Subsezione, Esegui in Nuova Finestra
 * E :  Solo Richiesta in Subsezione

 ### NOTE OPERATIVE

 :  : R01 Struttura di Richiamo

Tramite i Tag G.SUB.UQR, G.SET.UQR è possibile lanciare una query, ponendo prima all'utente le domane necessarie per la sua esecuzione. A tali tag si può aggiungere il tag D.FUN.UQR, che salvo necessità particolari, si assume corrisponda alla funzione di esecuzione di una query in formato matrice (cioè F(EXB;LOA10_SE;EQR)) ed è quindi opzionale.

* Il tag G.SUB.UQR serve solo per identificare la subsezione, come una un subsezione che presenterà le sopracitate caratteristiche.
* Il tag G.SET.UQR serve per indicare quale sarà il questioni che si andrà utilizzare e varie caratteristiche grafiche tramite le quali, il questionario e la funzione stessa verranno posti all'utente.
* Il tag D.FUN.UQR serve per indicare quale funzione deve essere infine eseguita, in sostituzione alla funzione assunta per l'esecuzione di una query in scheda.. Questo tag non si differenzia dal normale tag di funzione D.FUN.STD se non che per un aspetto :  tutte le risposte alle domande del questionario verranno automaticamente passate come parametri di INPUT alla funzione indicata in questo formato "codicedomanda(valorerisposta)", ma è inoltre possibile indicare un utilizzo specifico di tali parametri all'interno della funzione tramite la seguente dicitura $IN.codicedomanda. Quindi ponendo di avere come unica domanda con codice domanda "CD", mi viene richiesto un cliente, se in D.FUN.UCF specifico "F(EXD;*SCO;) 2(MB;SCP_SCP;XXX)" mi verrà eseguita la funzione "F(EXD;*SCO;) 2(MB;SCP_SCH;XXX) INPUT(CD(valorerisposta))", viceversa se specifico "F(EXD;*SCO;) 1(CN;CLI;$IN.CD) 2(MB;SCP_SCP;XXX)" mi verrò eseguita la funzione "F(EXD;*SCO;) 1(CN;CLI;valorerispostaCD) 2(MB;SCP_SCH;XXX) INPUT(CD(valorerisposta))"

Esempio 1) - Con funzione assunta
 :  : PAR F(04) L(MON)
G.SEZ Pos(1)
G.SUB.UQR Tit="*NONE"
G.SET.UQR UirQTO="TA" UirQPO="B£AMO" UirQQR="*KEY" UirMGr="C"


Esempio 2) - Con funzione esplicita
 :  : PAR F(04) L(MON)
G.SEZ Pos(1)
G.SUB.UQR Tit="*NONE"
G.SET.UQR UirQTO="TA" UirQPO="B£AMO" UirQQR="*KEY" UirMGr="C"
D.FUN.UQR F(EXD;*SCO;) 2(MB;SCP_SCHESE;LOSUIR) 4(;;EXDPAR)


 :  : R01 Le Domande della Query

Per il dettaglio sulle possibilità grafiche si rimanda all'help del wizard G.SET.UQR, mentre per quel che riguarda la struttura di richiesta ed esecuzione della query si rimanda al documentazione del modulo specifico. B£EQRY.

 :  : DEC T(TA) P(B£AMO) K(B£EQRY) L(1)

 ### NOTE SU ESEMPI

* La query richiesta è sempre la query *KEY dell'oggetto TA/B£AMO
* Gli esempi sono suddivisi in tre gruppi : 
** Il primo gruppo evidenzia l'esecuzione della funzione assunta della query in tutte le modalità grafiche possibili
** Il secondo gruppo evidenzia l'esecuzione di una funzione esplicita (nello specifico una scheda in cui attraverso una matrice vengono evidenziati i parametri ricevuti) della query in tutte le modalità grafiche possibili
** Il terzo gruppo infine è solo una replica del primo gruppo, ma con la forzatura dell'applicazione immediata.

