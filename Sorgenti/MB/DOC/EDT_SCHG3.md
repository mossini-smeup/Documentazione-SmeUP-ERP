# G.DIN Target dinamico

Tramite questa funzione è possibile instaurare delle relazioni dinamiche fra il
contenuto di una subsezione e quello delle altre. In sostanza tramite essa è possibile
condizionare l'esecuzione e/o il contenuto di un'altra subsezione.

Questa specifica va indicata al di sotto della specifica di definizione di subsezione
( :   :  G.SUB) della subsezione a partire dalla quale di vuole condizionare un'altra subsezione.
Le relazioni per ogni subsezione possono essere multiple perciò per ognuna di essere
posso definire più di una specifica di questo tipo.

# Parametri

## Where - Dove
Definisce l'ID o il Titolo (nel caso il primo sia assente) della subsezione che si vuole
condizionare.

Obbligatorio = NO
Default = Nullo

## When - Quando

Definisce l'azione che scatena il condizionamento dell'altra subsezione, se non viene
specificata alcuna azione il condizionamento viene eseguito ogni volta che viene eseguita
una qualsiasi azione sul contenuto della subsezione originaria.
I valori definiti per questo parametro : 

.Change         Allo scorrimento (se matrice o albero)
.Click          Al click del mouse
.DblClick       Al doppio click del mouse
.Return         Al ritorno da un richiamo funzione
.Expand         All'espansione di un nodo dell'albero
.ChangeRow      Al cambio di riga (se matrice)
.ChangeCol      Al cambio di colonna (se matrice)
.Drop           Al DROP (files system)
.Init           Crea solo le variabili sulla sezione corrente
.*ALL           Sempre

Obbligatorio = NO
Default = *ALL

## Sync - Sincrono
Stabilisce se la subsezione deve ricaricarsi al verificarsi dell'evento o solo quando esplicitamente richiesto.

Obbligatorio = NO
Default = Yes

## OnlyFocus - Visualizza solo la sezione

TODO EDT_SCHG3

Obbligatorio = NO
Default = ???

## NoTransVar - Trasferisci le Variabili

Consente di impedire il trasferimento delle variabili sulla subsezione di destinazione.
Il comportamento di default prevede il trasferimento delle variabili.

Obbligatorio = NO
Default = No

## Load - Caricamento

Questo parametro definisce se il condizionamento deve avvenire immediatamente
dopo l'avverarsi dell'azione definita dal parametro When oppure solo al momento
del riaggiornamento della subsezione condizionata.

I valori definiti per questo parametro : 

.I              Immediato
.D              Differito

Obbligatorio = NO
Default = I

## Title - Titolo

Condizionando una subsezione può tornare utile ridenomirla in funzione del
contenuto della subsezione originaria. In sostanza posso ridefinire il titolo
in modo dinamico utilizzando il valore di una più variabili contenute nella
subsezione originaria.

Inoltre nel caso di alberi, la subsezione assume automaticamente come titolo,
salvo l'utilizzo di questo parametro, la descrizione del nodo di riferimento.

Obbligatorio = NO
Default = Nullo

## TitleLock - Blocca il cambio di titolo

Fa in modo che il titolo della subsezione condizionata rimanga invariato.

Obbligatorio = NO
Default = No

## Sec.Var/Sch.Var/Com.Var/Loo.Var - Variabili di Sezione/Scheda/Componente/Loocup

Dal momento che più sezioni nella stessa scheda possono valorizzare le stesse
variabili (ad. es. K1 viene valorizzata sia da una matrice che da un albero, oppure
possono essere presenti più alberi...) è possibile valorizzare nuove variabili dal
nome arbitrario sulla base delle variabili standard dei componenti.
Facendo dipendere le sezioni dinamiche da variabili ridenominate piuttosto che
da quelle standard non si avranno interferenze tra sezioni.

es. G.DIN Sch.Var="KX([K1])"

In questo modo la variabile K1 viene ridenominata KX, sarà questo il nome che
verrà utilizzato nella subsezione condizionata.

Le variabili istanziate dipendono dal componente. Vedi capitolo "Variabili e dinamicità"

Queste variabili non vengono create nel caso di evento "Return"

- [Servizi correlati](Sorgenti/MB/DOC/LOCEXD_B)

Obbligatorio = NO
Default = Nullo

## Exec - Esegui Funzione (se ammessa)

Questo parametro va utilizzato in alternativa al parametro Where, tramite al verificarsi
dell'azione definita dal parametro When, non verrà instaurata una relazione con un'altra
sezione, ma verrà eseguita una funzione ex-novo.

Obbligatorio = NO
Default = Nullo

## Base -  Sezione base destinazione

        **                      030   D
## Mode  - Modalita' Dinamismo

.VDin.Mode              030   D
## Source  - Sorgente del dinamismo

      **                      100
## Focus - Dai il fuoco alla sottosezione

.VYes.No                030   D
## Action - Definisce un'azione

         **                      100


# Dinamicità multiple
Utilizzando più istruzioni G.DIN è possibile scatenare più dinamicità. E' possibile associare le dinamicità a eventi diversi oppure allo stesso evento.
Ad esempio è possibile indurre una certa dinamicità facendo click su una matrice oppure indurre una dinamicità diversa facendovi doppioclick.
Oppure è possibile con un solo click scatenare n dinamicità verso n sezioni differenti. In questo caso bisogna sottolineare che non è garantito l'ordine con cui verranno indotte le varie dinamicità. L'orine con cui scrivo le istruzioni G.DIN non è quindi garantito essere lo stesso ordine con cui vengono indotte le dinamicità e quindi eseguiti i programmi.
