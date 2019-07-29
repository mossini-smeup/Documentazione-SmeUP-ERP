# Cosa è un setup.
Un Setup è la configurazione di un componente grafico.

Esistono due tipi di setup : 
 * predefiniti
 * utente

Entrambi questi tipi di setup possono essere applicati (utilizzati).
I setup predefiniti non sono modificabili. Sono definiti in fase di implementazione dal programmatore.

I setup utente sono liberamente modificabili. Si possono quindi anche cancellare, copiare o crearne di nuovi.

Il componente che sfrutta maggiormante la possibilità di essere configurato, cioè di avere dei setup, è la matrice.
Negli esempi che seguono ci riferiremo spesso all'utilizzo dei setup applicati a questo componente.

# Cosa posso personalizzare con un setup.
Un setup mi permette di configurare la visualizzazione e il comportamento di un componente grafico.
Le possibilità di personalizzare un componente dipendono dal componente stesso.
Bisogna quindi fare riferimento ai capitoli dei singoli componenti.

# Come sono gestiti i setup utente.
I Setup sono gestiti tramite un apposito modulo.

# Come sono organizzati
I setup sono associati ad un componente di una subsezione.
Ad esempio la matrice della disponibilità avrà dei setup differenti dalòla matrice degli ordini.
I setup utente sono normalmente personali,  lutente BIANCHI avrà quindi setup diversi dall'utente ROSSI sulla medesima matrice.
I setup predefiniti saranno invece gli stessi (anche se non è vero in assoluto) per utenti differenti che usino la stessa subsezione.

# Come applicare un setup
Quando un componente di una subsezione ha associato  uno o più setup compariranno dei pulsanti o delle combo box con le quali impostare il setup.
Nel caso di matrici e di grafici avrò tanti pulsanti quanti sono i setup (utente o predefiniti) mentre nel caso di alberi avrò una combo box.
La presenza di questi elementi grafici (pulsanti o combo) ci informerà della presenza dei setup e ci consentirà di applicarli.

Si possono distinguere i setup utente dai setup predefiniti perchè i primi sono posizionati in ....
-- inserire immagine presa da esempi, capire loocup, disegnare una scheda,  ereditarietà e setup, matrice ---

# Gestione dei setup utente
**NOTA** Da questo punto in poi del manuale ogni volta che si utilizzerà il termine **setup** si intenderà **setup utente** in qunto i setup predefiniti non si possono copiare, modificare o cancellare.

I setup sono gestiti mediante un apposito modulo.

Per aprire il gestore esistono tre possibilità : 
 * cliccando con il tasto destro su una subsezione, selezionare la voce **Impostazioni** e poi **Gestione Setup**
 * utilizzando l'apposito pulsante --inserire immagine F17--
 * utilizzare il tasto **F17** quando la subsezione di cui si vuole gestire il setup ha il fuoco.

Una volta avviato il modulo che vediamo in figura
![LOBASE_180](http://localhost:3000/immagini/MBDOC_OPE-LOCSETOLD/LOBASE_180.png)
Verranno mostrati tutti i setup salvati, filtrati per subsezione, utente.
Non vedrò quindi tutti i setup del componente matrice ma solo i setup relativi alla matrice di quella subsezione per l'utente corrente e l'utente generico.
Ho però la possibilità di visuali

Questa finestra di dialogo consente di : 
 * copiare un setup esistente
 * modificare un setup esistente
 * creare un setup nuovo
 * eliminare un setup
 * ricercare i setup di altri utenti

## Copiare un setup

Per copiare un setup bisogna prima selzionare un setup tra quelli presenti nella lista e poi cliccare su copia.
Comparirà la dialog di definizione delle chiavi, vedi immagine seguente.
--inserire immagine della dialog di salvataggio di una configurazione--
Le informazioni obbligatorie sono le chiavi 2 e 3.
La chiave 1 non è modificabile in quanto il setup è associato ad una specifica subsezione.
Nella chiave 2 verrà proposto il codice dell'utente corrente. Se si desidera che il setup valga anche per altri utenti inserirò il codice ******.
Nella chiave 3 va posto il codice del setup. Se verrà posto codice ****** significherà che il setup creato è quello di default, cioè il setup caricato quando verrà visualizzata la subsezione in oggetto.
Il campo descrizione è facoltativo, va utilizzato per facilitare il riconoscimento di un setup da un'altro.

Premendo su OK il setup verrà salvato. Se esiste già un setup con le chiavi indicate l'utente potrà sovrascriverlo.


## Creare un nuovo setup.
Se non c'è nessun setup salvato o ne voglio creare uno ex-novo utilizzarò il pulsante **Nuovo**. Comparirà una finestra di dialogo con le domande e i pulsanti OK, ANNULLA. Una volta inserite le risposte necessarie e confermate con l'OK mi comparirà una finestra in cui dovrò inserire le chiavi di salvataggio del setup.
--inserire immagine della dialog di salvataggio di una configurazione--
Le informazioni obbligatori e sono le chiavi 2 e 3.
La chiave 1 non è modificabile in quanto il setup è associato ad una specifica subsezione.
Nella chiave 2 verrà proposto il codice dell'utente corrente. Se si desidera che il setup valga anche per altri utenti inserirò il codice ******.
Nella chiave 3 va posto il codice del setup. Se verrà posto codice ****** significherà che il setup creato è quello di default, cioè il setup caricato quando verrà visualizzata la subsezione in oggetto.
Il campo descrizione è facoltativo, va utilizzato per facilitare il riconoscimento di un setup da un'altro.

Premendo su OK il setup verrà salvato. Se esiste già un setup con le chiavi indicate l'utente potrà sovrascriverlo.

## Modificare un utente esistente

Per modificare un setup esistente bisogna selezionarlo nell'elenco cliccandoci sopra. Poi, mediante il pulsante **Modifica**  si aprirà una finestra di dialogo con le domande. Cliccando su OK il setup verrà salvato.

## Eliminare un setup
Per eliminare un setup bisogna selezionarlo cliccandoci sopra e poi premere il pulsante elimina e poi confermare.

**NOTA** :  Una volta eliminato il setup non è più recuperabile

## Ricercare un setup
Il gestore dei setup quando si avvia parte sempre con impostato un filtro di ricerca sui setup.
Il filtro ha come parametri : 
 * il codice della subsezione
 * l'utente corrente
 * l'utente generico
Verranno quindi mostrati  solo i setup filtrati secondo questi criteri.

La presenza del filtro è evidenziata dal colore giallo del pulsante **Filtro**.

Se si desidera visualizzare tutti i setup definiti da tutti gli utenti su quella subsezione cliccare sul pulsante filtro.
Comparirà la seguente finestra di dialogo : 

![LOBASE_179](http://localhost:3000/immagini/MBDOC_OPE-LOCSETOLD/LOBASE_179.png)
Inserire ** come nome utente e confermare.
Non si può modificare il campo **Contesto** in quanto un setup risulta associato ad una specifica subsezione e non si può pensare di

Il pulsante **Filtro** tornerà di colore grigio e compariranno tutti i setup di tutti gli utenti (se ve ne sono definiti).

Si potrà quindi operare sui vari setup.


# la gestione dei setup nel componente matrice
La matrice ha una possibilità in più rispetto agli altri componenti di definire dei setup :  permette di salvare le impostazioni create in modo grafico.
Questo significa che se ad esempio filtro la matrice in base ad una colonna, eseguo un raggruppamento e nascondo alcune colonne posso salvare queste impostazioni, senza dover passare per la finestra di dialogo con le domande di configurazione.

Le impostazioni possono essere salvate in tre modi : 
 * mediante il comando **Salva** sovrascriverò il setup utente correntemente utilizzato. Se la matrice non sta utilizzando un setup utente verranno chieste le chiavi di salvataggio e verrà creato un setup nuovo.
 * mediante il comando **Salva con nome**  verranno chieste le chiavi di salvataggio e verrà creato un setup nuovo.
 * mediante il comando **Salva setup come Default** verrà salvato il setup di default per quella matrice per quell'utente.

I comandi **Salva**, **Salva con nome** e **Salva come Default** sono presenti sotto la matrice oppure sono accessibili  cliccando con il tasto destro sulla linguetta della subsezione e poi selezionare **Impostazioni**.


# Setup comuni a più utenti
E' possibile condividere lo stesso setup tra più utenti :  va salvato mettendo come codice utente ******. Il codice ****** indica che è un setup che vale per tutti gli utenti. Se l'utente ROSSI salva il setup mettendo invece dell'utente ROSSI ** avrà che tale setup sarà visto anche dall'utente BIANCHI.


# F.A.Q. - Domande Frequenti
D :  Perchè se cambio ambiente e non vedo più i setup utente definiti su una subsesione?
R :  Questo può succedere perchè il file dove sono memorizzati i setup non è condiviso tra i due ambienti.
S :  Chiedere al responsabile EDP di copiare il record dal B£MEDE di un ambiente all'altro.


# Come sono organizzati - visione tecnica - (T)
I setup sono organizzati per subsezione,  per utente e per nome.
Questo consente di
 * differenziare i setup di uno stesso componente (es. matrice) in funzione del loro utilizzo. Potrò quindi avere matrici diverse (stesso componente) con setup differenti in base alla subsezione di appartenenza.
 * differenziare i setup in funzione degli utenti. Potrò avere rappresentazioni diverse degli stessi dati in funzione dell'utente che li sta consultando.
 * avere più setup per uno stesso componente e per uno stesso utente, questi ad esempio consente di creare differenti visualizzazzioni su una stessa matrice per lo stesso utente.

Utilizzando un terminologia tecnica avrò che : 
 * non potrò associare lo stesso setup a componenti differenti (il setup di un albero non è significativo per una matrice)
 * il componente di tipo A della subsezione X avrà un setup diverso dal componente di tipo A della subsezione Y. Avremo pertanto che la matrice della subsezione X avrà un setup differente dalla matrice della subsezione Y
 * il setup del componente di tipo A della subsezione X dell'utente Z sarà diverso il setup del componente di tipo A della subsezione X dell'utente K. Avrò quindi la possibilità di salvare setup diversi per la stessa matrice ma per utenti diversi.


# Dove sono salvati - (T)
I setup utente sono memorizzati sul file B£MEDE0F


# la modalità avanzata della gestione dei setup (T)
Quando il gestore è aperto premendo i tasti **Ctrl+F5** si attiva la modilità di gestione avanzata.
Questa modalità è riservata allo sviluppatore di Loocup
