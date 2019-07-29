# MODELLO STANDARD ANALITICA
Il modello di analitica gestisce le modalità di costruzione delle righe di analitica. Può essere a codici fissi o dinamici. I codici dinamici possono essere al massimo 2, e deve essere indicato esplicitamente l'ordinamento di distribuzione. Non è possibile utilizzare due stesse tipologie di codici dinamici tranne per quelle utente.

# CODICI FISSI
Si indica per ciascun oggetto che compone l'analitica i valori che andranno a comporre le righe di analitica. La percentuale su ciascuna riga del modello permetterà di distribuirne automaticamente l'importo. Se un oggetto à stato definito obbligatorio può non essere inserito nel modello ma sarà richesto nella gestione dell'analitica.

Es 1 : 
Conto CONT01
>.Voce di spesa   Centro di costo    Importo.
.-----------------------------------------------------.
.   V01__________C01_______________ 30____.
.   V02__________C02________________70____.


Alla conferma della registrazione automaticamente per il conto CONTO01 si creerà l'analitica. Il corrispondente importo di riga verrà distribuito in percentuale sulle due righe di analitica costruite come nel modello.

Es 2 : 
Conto CONT01
>.Voce di spesa   Centro di costo    Importo.
.-----------------------------------------------------.
.    _____________C01______________ 30____.
.    _____________C02_______________70____.


Alla conferma della registrazione automaticamente per il conto CONTO01 si creerà l'analitica. Il corrispondente importo di riga verrà distribuito in percentuale sulle due righe di analitica costruite come nel modello. Se la voce di spesa è stata definita obbligatoria ne verrà richiesto l'inserimento.

# CODICI VARIABILI
L'utilizzo di codici variabili nel modello permette di costruire righe di analitica che non sono esplicitamente definite nel modello, ma dipendono dalla tipologia del codice variabile e dal contenuto dei valori che ricevono.

I codici variabili possono essere di quattro tipologie : 
 * _7_Indici di distribuzione
 * _7_Lista oggetto
 * _7_Parametri
 * _7_Utente

Con un '+' sul campo ne viene guidata la costruzione.

# INDICI DI DISTRIBUZIONE
Gli indici di distribuzione permettono di distribuire due oggetti di analitica su un terzo oggetto. L'oggetto indice deve essere costruito nel seguente modo :  _7_ _&_I,Z,XXXdove Z è l'ordinamento e XXX è l'elemento della tabella D5I E' controllata la congruenza fra gli oggetti dell'analitica e gli oggetti che costituiscono l'indice.

Es 1 : 
Conto CONT01

>.Voce di spesa   Centro di costo   Importo.
.----------------------------------------------------.
.    ___________ _&_I,1,IND______ 100___.

Indice di distribuzione IND
>. A) V01   C01    20
...........C02    80
. B) V02   C01    10
...........C02    40
...........C03    50

Alla conferma della registrazione verrà richiesta la voce di spesa. Se si inserisce la V01 il sistema creeà due righe di analitica come A), se V02 come B). L'importo verrà distribuito secondo le percentuali definite nei due casi.

Es 2 : 
Conto CONT01
>.Voce di spesa   Centro di costo   Importo.
.----------------------------------------------------.
.   V01_________ _&_I,1,IND________100____.

In queso caso il sistema sarà in grado di costruire automaticamente le righe di analitica come A). Questo sistema a differenza dell'analitica a codici fissi ha il vantaggio che modificando l'indice di distribuzione ne vengono modificati tutti i modelli ad esso associati.

Es 3 : 
Conto CONT01
>.Voce di spesa   Centro di costo   Importo.
.----------------------------------------------------.
. _____________ _&_I,1,IND_________50____.
. _____________ _&_I,1,IND_________50____.

In queso caso alla conferma della registrazione verranno richieste due voci di spesa. Se si inserisce prima V01 e poi V02 saranno costruite le righe sia come A) che come B), ma con le percentuali che subiranno una ridistribuzione percentuale sulla base del valore presente nelle due righe del modello.
Il risultato sarà un'analitica cosi composta (con importo 100) : 
>.Voce di spesa   Centro di costo   Importo.
.----------------------------------------------------.
.   V01_________ C01______________ 10____
.   V01_________ C02______________ 40____
.   V02_________ C01______________ 05____
.   V02_________ C02______________ 20____
.   V02_________ C03______________ 25____


# LISTA
La lista permette di esplodere la riga di analitica su tutti gli elementi che la compongono.
L'oggetto lista deve essere costruito nel seguente modo :  _7_ _&_L,Z,XXXdove Z è l'ordinamento e XXX è l'elemento della lista. E' controllata la congruenza fra l'oggetto analitica e l'oggetto della lista. Poichè la lista è solo relativa a codici non potrà esserci alcuna distribuzione dell'importo.

Es 1 : 
Conto CONT01
>.Voce di spesa   Centro di costo     Importo.
.------------------------------------------------------.
.               _&_L,1,LIS___ ______ 100_____.
. Lista LIS :  V01
............ V02

Alla conferma della registrazione si creeranno due righe di analitica con le due voci di spesa della lista. L'importo deve essere gestito manualmente.

# PARAMETRI
I parametri permettono di distrbuire la riga di analitica su tutti gli elementi che compongono il parametro dell'oggetto stesso. L'oggetto parametro deve essere costruito nel seguente modo : 
_7_ _&_P,Z,XXXYYYdove Z è l'ordinamento, XXX è la categoria e YYY il parametro E' controllata la congruenza fra l'oggetto analitica e l'oggetto del parametro.

Es 1 : 
Conto CONT01.
>. Voce di spesa   Centro di costo   Importo.
. ----------------------------------------------------.
.                 _&_P,1,PARPPP ____100____.

Parametro :  categoria PAR, parametro PPP
>.A) X00     V01    20
........... V02    80
.B) Y00     V01    20
............V02    20
............V03    60

Alla conferma della registrazione verrà richiesta la voce di spesa. Se si inserisce la X00 il sistema creeà due righe di analitica come A), se X02 come B). L'importo verrà distribuito secondo le percentuali definite nei due casi.

# UTENTE
Il codice dinamico utente permette di distribuire gli oggetti di analitica sull'oggetto stesso definito utente. L'oggetto utente deve essere costruito nel seguente modo :  _7_ _&_U,Z,XXYYYYdove Z è l'ordinamento, XX è il sottosettore della tabella B£J e YYY l'elemento della tabella B£J. Nella tabella B£J è da inserire il programma utente che ritorna una schiera di codici e percentuali relative al prorpio oggetto.

Es 1 : 
Conto CONT01.
>.Voce di spesa   Centro di costo   Importo.
.----------------------------------------------------.
.   ___________ _&_U,1,TAUTE ______100____.

Utente :  Sottosettore TA della B£J , Elmento UTE della B£J il programma utente da B£JTA,UTE : 
>.A) V01     C01    20
............C02    80
.B) V02     C01    10
............C02    40
............C03    50

Alla conferma della registrazione verrà richiesta la voce di spesa. Se si inserisce la V01 il sistema creerà due righe di analitica come A), se V02 come B). L'importo verrà distribuito secondo le percentuali definite nei due casi.

# CODICI VARIABILI INTERDIPENDENTI
E' possibile anche inserire due codici dinamici interdipenti : 

Es 1 : 
Conto CONT01.
>.Voce di spesa      Centro di costo     Importo.
.---------------------------------------------------------.
.__P,1,PARPPP____   &_I,1,CDC_________  100____.

Parametro :  categoria PAR, parametro PPP
>.A) X00     V01    50
............V02    50

Indice di distribuzione CDC
>.B) V01     C01    20
............C02    80
.C) V02     C01    10
............C02    40
........... C03    50

In queso caso alla conferma della registrazione verrà richiesta la voce di spesa. Se si inserisce X00 saranno costruite le righe di analitica che da A) elaboreranno per la 1° riga B) e per la 2° riga C), e subiranno le rispettive ridistribuzioni percentuale dal 1° livello al 2°. Il risultato sarà un'analitica cosi composta (con importo 100) : 
>.Voce di spesa     Centro di costo    Importo.
.------------------------------------------------------.
.    V01__________ C01_______________ 10____.
.    V01__________ C02_______________ 40____.
.    V02__________ C01_______________ 05____.
.    V02__________ C02_______________ 20____.
.    V02__________ C03_______________ 25____.


# DOCUMENTAZIONE DINAMICA
E' possibile verificare in anteprima l'effetto di un modello dinamico. Per simulare è sufficiente eseguire l'opzione 'DD' dal set'n'play.

# RICHIAMO MODELLI A VALORI DINAMICI
Per i modelli dinamici il risultato di un modello può dipendere da un valore ricevuto in ingresso.
E' possibile definire se ricostruire sempre l'analtica da un modello dinamico o se mantenere i valori ricevuti in ingresso.

Es 1 : 
Conto CONT01.
>. Voce di spesa   Centro di costo   Importo.
. -----------------------------------------------------.
.   ____________ _&_I,1,IND_________100____.

Indice di distribuzione IND
>.A) V01     C01    20
............C02    80

Se passo V01 in sistema ricostruirà automaticamente l'analitica sulla base dell'indice di distribuzione IND come A). Se oltre alla V01 passo anche il centro di costo C03 si può decidere se mantenere l'analitica ricevuta come : 
>.Voce di spesa   Centro di costo   Importo.
.----------------------------------------------------.
.   V01_________ C03_______________100___.

oppure indipendentemente dal fatto di aver ricevut C03 ricostruire comunque l'analitica dall'indice di distribuzione IND come A).
