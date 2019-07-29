# Avvio della funzione ricerca in finestra
La principale funzione di ricerca può essere avviata dall'utente a partire da qualsiasi campo di imputazione oggettizzato, tramite l'indicazione nel primo carattere di uno dei seguenti caratteri "speciali" predisposti in smeup per identificare la volontà di eseguire una ricerca  : 
* "** : **" per lanciare la query ordinata per il codice dell'oggetto di riferimento, con possibilità di indicare un filtro sul contenuto di codice/descrizione
* "**!**" per lanciare la query ordinata per il codice dell'oggetto di riferimento, con possibilità di indicare un filtro sul posizionamento per codice
* "**?**" per lanciare la query ordinata per descrizione dell'oggetto di riferimento (se l'oggetto non prevede una ricerca per descrizione verrà eseguita la ricerca per codice) con possibilità di indicare un filtro sul posizionamento per codice
* "**+**" per lanciare una delle altre query di ricerca eventualmente previste per l'oggetto oltre a quelle per codice e descrizione.
* "**/**" questo carattere, salvo sia esplicitamente espresso, ha valenza particolare solo sulle date, per le quali permette la costruzione guidata delle forme dinamiche (es. &OGI00 corrisponde alla data odierna). Per i restanti casi il comportamento è del tutto simile a quello del carattere "+".

![B£EQRY_01](http://localhost:3000/immagini/B£EQRYA02A/BXEQRY_01.png)
A seguire, a tale carattere speciale, sarà inoltre possibile indicare dei caratteri che potranno poi essere interpretati dalla particolare query di ricerca. Si menziona qui in particolare che : 
* i caratteri che seguono i "** : **" vengono utilizzati come filtro all'interno dei caratteri che definiscono il codice e la descrizione (es.  : BICI, verranno cercati i codici che nel codice stesso o nella descrizione contengono tale parola)
* i caratteri che seguono il "**!**" vengono utilizzati come posizionamento sulla ricerca per codice (es. !003, vengono presentati tutti i codici >= a 003)
* i caratteri che seguono il "**?**" vengono utilizzati come posizionamento sulla ricerca per descrizione (es. ?BICI, vengono presentati tutti i codici aventi descrizione >= a BICI)
* i caratteri che seguono il "**+**" possono indicare alternativamente : 
** il codice di una particolare ricerca, tale codice può essere a sua volta seguito da uno o più parametri di puntamento della ricerca, suddivisi dal carattere "**.**", qualora la ricerca lo preveda. In alternativa al codice "." possono essere utilizzate le parentesi tonde **()** , qualora sorga ad esempio la necessità di indicare dei parametri che contengano a loro volta il carattere "."
** direttamente i parametri della ricerca predisposta come default. Se i parametri sono multipli questi possono essere suddivisi dal carattere ".". Come descritto poc'anzi in alternativa al punto possono essere utilizzate le parentesi tonde. E' importante notare che per quel che riguarda la determinazione della query di default, viene fatta la seguente risalita :  se è stata impostata una query di default grafica viene presa in considerazione quella, viceversa viene presa in considerazione la ricerca di default dell'emulazione.

![B£EQRY_02](http://localhost:3000/immagini/B£EQRYA02A/BXEQRY_02.png)
Va inoltre osservato che ove sia stato previsto, se alla sinistra del campo di imputazione è stata prevista un'icona, il click con il mouse sull'icona attiva la funzione di ricerca.

![B£EQRY_03](http://localhost:3000/immagini/B£EQRYA02A/BXEQRY_03.png)
![B£EQRY_04](http://localhost:3000/immagini/B£EQRYA02A/BXEQRY_04.png)
In qualsiasi campo di imputazione è inoltre previsto l'utilizzo del tasto funzione F04 per l'avvio della funzione di ricerca.

# La risoluzione della ricerca
Data indicazione della volontà di eseguire una ricerca, questa potrà essere risolta in due modalità : 
* Una specifica della singola classe
* Una generale di tutte le classi che non hanno una ricerca specifica.

Nel primo caso rientrano solo alcune classi particolari per le quali viene prevista una forma di ricerca particolare. Rientrano in questa casistica le date e gli oggetti esterni (cartelle e file di server)

![B£EQRY_07](http://localhost:3000/immagini/B£EQRYA02A/BXEQRY_07.png)![B£EQRY_08](http://localhost:3000/immagini/B£EQRYA02A/BXEQRY_08.png)
Per tutte le altre (e quindi per la stragrande maggioranza delle classi) la funzione di ricerca viene svolta nel medesimo modo. A seguire viene riporta l'operatività della scheda di ricerca generale.

 :  : I.INC.MBR Fil(DOC_SCH) Mem(B£EQRY_SEA)

# Le ricerche speciali storiche
Per compatibilità con il passato, per alcuni oggetti sono state mantenuti alcuni caratteri di ricerca speciali. Tali caratteri di ricerca iniziano sempre con il carattere "+" e l'elenco di tali combinazioni può essere evidenziando indicando i caratteri "++". Attraverso questi caratteri oltre che poter vedere l'elenco di tutti i caratteri speciali sarà inoltre possibile selezionare una ricerca di default fra di esse. In questo caso scrivendo solo il carattere "+" seguito dai caratteri previsti dalla ricerca specifica, sarà possibile avviare la ricerca specifica selezionata come default.

NOTA BENE :  questa funzionalità viene presa in considerazione solo se i caratteri successivi al "+" non corrispondono al codice di una query grafica e solo se dalla scheda di ricerca grafica non è stata prevista a sua volta una ricerca di default.

Questo l'elenco degli oggetti che ancora oggi prevedono delle ricerche speciali con 5250 : 
 :  : DEC T(OG) K(AR)
 :  : DEC T(OG) K(CN)
 :  : DEC T(OG) K(CZ)
 :  : DEC T(OG) K(DO)
 :  : DEC T(OG) K(LO)
 :  : DEC T(OG) K(MT)
 :  : DEC T(OG) K(TA)
 :  : DEC T(OG) K(OJ*FILE)
 :  : DEC T(OG) K(OR)
 :  : DEC T(OG) K(UB)

Esempio di ricerche speciali sull'oggetto CN

![B£EQRY_09](http://localhost:3000/immagini/B£EQRYA02A/BXEQRY_09.png)