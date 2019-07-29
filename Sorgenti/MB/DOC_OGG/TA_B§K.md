# B§K - Impostazioni base Loocup
 :  : DEC T(ST) K(B§K)
## OBIETTIVO
Contiene le informazioni che permettono di modificare la presentazione delle schede di moduli e oggetti.
Viene fornita con i sottosettori standard £O (per gli oggetti) e £M (per i moduli e le applicazioni)
## CONTENUTO DEI CAMPI

 :  : FLD T$ELEM **Elemento**
Nel sottosettore £O, questo campo deve contenere un oggetto, nel sottosettore £M deve contenere o un modulo.
E' possibile impostare un default valido per tutti le istanze inserendo l'elemento ***ALL**.
Se inserito nel £M vale per tutti i moduli, se inserito in £O, vale per tutti gli oggetti ad eccezione dei moduli.
Nel sottosettore £O è può essere indicato il tipo oggetto o il tipo con il parametro se previsto.

 :  : FLD T$B§KA **Exit per focus**
E' il suffisso del programma che, se presente, permette di modificare l'eventuale presentazione del focus (eliminare, modificare o aggiungere righe).
Per l'applicazione aa, il modulo mmmm, l'oggetto oo, e la exit x, il programma avrà il nome
Applicazione :  aaK9_x
Modulo :  aaK9mmmm_x
Oggetto :  aaK9oo_x

 :  : FLD T$B§KB **Scheda My Smeup**
Tramite questo campo è possibile fissare l'utilizzo della scheda personale "standard" dell'oggetto o del modulo.
Tale scheda è identificata dallo script avente nomescriptstandard+"_X". Es. per gli articoli abbiamo AR_X, per il modulo degli articoli BRARTI_X.

Tale campo può assumere i seguenti valori : 
* 1 = Scheda. La scheda personale viene presentata in sostituzione della scheda standard, quando viene eseguita la funzione "scheda oggetto".
* 2 = Scheda + F20. L'opzione è simile a quella del punto precedente con la sola differenza che viene aggiunto alla scheda il tasto funzione F20 che permette di richiamare il menù dell'oggetto.
* 3 = Specifiche Menù. Tramite questo valore, la scheda personale verrà automaticamente aggiunta alla voce di menù "Specifiche" (se assente apparirà in automatico) del menù dell'oggetto.
* 4 = Scheda Dashboard. La scheda personale verrà presentata come scheda dashboard nel menù dell'oggetto.

 :  : FLD T$B§KC **Scheda Iniziale**
Se la scheda dell'oggetto o del modulo è in modalità hypermenu, è possibile condizionare la modalità di presentazione di una scheda sulla sezione di destra.
Si possono impostare i seguenti valori : 
* 'N' = La sezione rimane vuota
* 'Y' = Viene presentata la voce "Dashboard" all'atto del caricamento della scheda
* 'I' = Viene presentata la voce "Info" all'atto del caricamento della scheda
* ' ' = Assunto. Per le istanze di oggetti e moduli, viene assunto il valore impostato nell'elemento *ALL, rispettivamente del sottosettore £O e £M.
Con questa impostazione, ad esempio : 
* Sottosettore £O, elemento AR     :  Valore 'Y'
* Sottosettore £O, elemento *ALL   :  Valore 'N'
si ottiene il seguete comportamento : 
Per gli articoli i dashboard viene presentato al caricamento
Per tutti gli altri oggetti viene presentato a richiesta.
