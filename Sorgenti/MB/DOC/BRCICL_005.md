# Generalità
In Sme.up la definizione e l'attivazione delle alternative nell'esecuzione di un ciclo di lavorazione, è possibile in tre diversi modi :  il ciclo prefisso, il ciclo suffisso, e l'attivazione e disattivazione dello stato di ogni singola operazione.

Tramite il ciclo prefisso si definiscono varie versioni del processo di lavorazione :  per ognuna di esse si inseriscono tutte le fasi da eseguire.

E' una modalità che permette una completa separazione tra le alternative, con l'obbligo però di ripetere le operazioni comuni a più cicli.

Nel ciclo suffisso invece si identificano le operazioni alternative impostandovi gli estremi di ciclo (da/a) per cui sono valide, in modo da non ripetere le operazioni comuni.

In entrambe le modalità, all'atto della messa in lavoro dell'oggetto del ciclo, immettendo un ordine di produzione, è possibile eseguire una sola scelta :  il codice ciclo.

Qualora vi fosse, all'interno del processo di lavorazione, più di una scelta possibile, ciascuna indipendente dalle altre (ad esempio due fasi eseguibili all'interno o all'esterno, senza che una scelta influenzi l'altra), si deve gestire manualmente lo stato delle operazioni.

E' possibile inoltre, ed è il tema di questo documento, utilizzare la gestione del gruppo alternativa, con lo scopo di facilitare la definizione e la scelta delle alternative.

Con questo strumento si introduce un legame esplicito tra le alternative, ed inoltre viene facilitata la modifica dello stato (l'attivazione di un'alternativa comporta l'attivazione di tutte le sue fasi e la contemporanea disattivazione delle alternative scartate).

La gestione delle alternative può convivere con il ciclo prefisso :  esso definisce ogni modalità costruttiva intrinsecamente diversa da ogni altra e, all'interno di esso, tramite il gruppo alternativa si impostano le ulteriori scelte esecutive.

Essa è invece meno compatibile con il ciclo suffisso, in quanto sostanzialmente copre le stesse esigenze, anche se in modo meno strutturato (il ciclo può essere codificato in una testata, e quindi controllato, le alternative invece sono inserite liberamente).

La scelta tra l'implementazione del ciclo suffisso oppure del gruppo alternative va fatta in base alle seguenti considerazioni :  se ci sono più scelte indipendenti all'interno dello stesso processo, si deve necessariamente ricorrere al gruppo alternative, se ce n'è una sola, è opportuno ricorrere al ciclo se si vuol tenere traccia, nell'ordine di produzione, della scelta effettuata, (tra i suoi campi viene infatti memorizzato il ciclo selezionato).

A favore del ciclo suffisso c'è inoltre il vantaggio che non è obbligatorio creare il ciclo del documento, in quanto la selezione delle operazioni attive (e quindi la costruzione degli impegni risorse) avviene dinamicamente, anche partendo dal ciclo dell'oggetto.

# Definizioni
In SMEUP si può scegliere tra due modalità di descrizione delle alternative di un ciclo (impostando il campo Alternative cicli multiple in tabella BR1).

## Gestione Alternative base
In questa modalità (ottenuta lasciando in bianco il campo di tabella BR1) si descrivono le alternative tra n e m fasi, ma che non si sviluppano sulle fasi successive).
In ogni riga del ciclo è possibile inserire i seguenti due campi : 

- il gruppo alternativa (campo alfabetico di un carattere) che rappresenta ogni possibile scelta esecutiva all'interno di un ciclo
- l'alternativa (campo numerico di due caratteri) che individua le fasi che devono essere eseguiteinsieme, all'interno dello stesso gruppo alternativa.

Tecnicamente questi due campi vengono memorizzati nel campo gruppo alternativa, separati da un punto (il campo A.01 sta a significare l'alternativa 01 del gruppo alternativa A).


|  Nam="Alternative di base - Esempio" |
| 
| .COL Txt="Gruppo Alternativa" LunAut=" " |
| ---|----|
| 
| .COL Txt="Alternativa" LunAut=" " |
| 
| .COL Txt="Fase" LunAut=" " |
| A | 01 | 0010 |
| A | 02 | 0020 |
| A | 03 | 0030 |
|  |  | 0040 |
| B | 01 | 0050 |
| B | 01 | 0060 |
| B | 02 | 0070 |
| B | 03 | 0080 |
| B | 03 | 0090 |
| B | 03 | 0100 |
| 

Nel gruppo alternativa A, si può eseguire, alternativamente, una fase tra la 0010, la 0020 o la 0030.

La fase 0040 è sempre eseguita (non ha alternative).

Nel gruppo alternativa B, si possono eseguire, alternativamente, le fasi 0050 e 0060, o la 0070 da sola, o le fasi 0080, 0090 e 0100.

In questo modo si riesce a descrivere ogni forma di alternativa, tra 'n' e 'm' fasi distinte.

## Gestione Alternative multiple
In questa modalità, attivata impostando il flag in tabella BR1, si possono descrivere alternative che si sviluppano in serie, su fasi successive.

Per descrivere compiutamente lo sviluppo del ciclo di lavorazione di un articolo, si devono poter rappresentare le alternative tra le varie fasi, vale a dire i diversi modi in cui l'articolo può essere realizzato.

Una rappresentazione potente deve saper trattare le alternative "profonde", che si sviluppano su più stadi, in cui il ciclo rappresenta un percorso (routing) tra l'entrata e l'uscita, dove si possono percorrere tratti in comune (operazioni comuni a più alternative), incontrare bivii (scelta tra più operazioni alternative), seguire percorsi obbligati (operazioni senza alternative).

Questa rappresentazione non si incontra soltanto in attività complesse, ma è necessaria anche per descrivere situazioni di estrema semplicità, quali il caso di un'alternativa tra una fase interna ed una esterna, che, a sua volta, può essere seguita o meno da un'ulteriore fase interna.

Un esempio di percorso complesso è riportato nella figura seguente
![BRCICL_01](http://localhost:3000/immagini/BRCICL_005/BRCICL_01.png)
In questa figura si evidenziano i vari percorsi possibili, ed inoltre si formano due gruppi :  A e B.

_2_Definizione :  _1_un gruppo è la porzione minima del percorso che può essere compresa in una linea chiusa che interseca il percorso in non più di due punti e che contiene al suo interno almeno una diramazione.

Si definiscono esterne le fasi non appartenenti a nessun gruppo.
![BRCICL_02](http://localhost:3000/immagini/BRCICL_005/BRCICL_02.png)
Per descrivere questa struttura (di alternative), si utilizza il gruppo alternativa (un parametro con cinque posizioni) definito per ogni fase del ciclo.

Le fasi esterne ad un gruppo devono avere il gruppo alternativa in bianco. Ciò significa che in questi casi il percorso è definito dalla sequenzialità delle operazioni.

Per le fasi interne ad un gruppo, si opera invece nel seguente modo.

Per ognuna di esse si codifica, in una delle prime quattro posizioni del gruppo alternativa (la posizione è indifferente) un carattere, comune alle fasi in alternativa tra loro.

Il carattere in quinta posizione individua invece la fase successiva da eseguire quando è stata scelta questa fase. Lo stesso carattere sarà presente in una delle prime quattro posizioni nella fase successiva. Se essa è all'esterno di un gruppo, il carattere di prosecuzione dovrà rimanere vuoto.

Ad esempio, il _3_gruppo A
![BRCICL_03](http://localhost:3000/immagini/BRCICL_005/BRCICL_03.png)
si descrive con la tabella "Gruppo A" dove per ogni fase sono presentate le posizioni da 1 a 5 del gruppo alternativa
Il carattere A viene assegnato alle fasi 10 e 20, in alternativa tra di loro.
Il carattere B viene assegnato soltanto alla fase 30 (che non ha nessuna alternativa), ma deve essere individuata come prosecuzione obbligatoria della sola fase 10.
Il carattere C viene assegnato alle fasi 40 e 50, in alternativa tra di loro.


|  Nam="Alternative multiple - Gruppo A" |
| 
| .COL Txt="Operazione" LunAut=" " |
| ---|----|
| 
| .COL Txt="1" LunAut=" " |
| 
| .COL Txt="2" LunAut=" " |
| 
| .COL Txt="3" LunAut=" " |
| 
| .COL Txt="4" LunAut=" " |
| 
| .COL Txt="5" LunAut=" " |
| 10 | A | -- | -- | -- | B |
| 20 | A | -- | -- | -- | C |
| 30 | B | -- | -- | -- | -- |
| 40 | C | -- | -- | -- | -- |
| 50 | C | -- | -- | -- | -- |
| 


Mentre il _3_gruppo B
![BRCICL_04](http://localhost:3000/immagini/BRCICL_005/BRCICL_04.png)si descrive con la tabella  "Gruppo B"


|  Nam="Alternative multiple - Gruppo B" |
| 
| .COL Txt="Operazione" LunAut=" " |
| ---|----|
| 
| .COL Txt="1" LunAut=" " |
| 
| .COL Txt="2" LunAut=" " |
| 
| .COL Txt="3" LunAut=" " |
| 
| .COL Txt="4" LunAut=" " |
| 
| .COL Txt="5" LunAut=" " |
| 60 | D | -- | -- | -- | E |
| 70 | D | -- | -- | -- | F |
| 80 | D | -- | -- | -- | G |
| 90 | E | -- | -- | -- | -- |
| 100 | E | F | -- | -- | -- |
| 110 | G | -- | -- | -- | -- |
| 


La quinta posizione individua la fase successiva :  può verificarsi il caso di più fasi con la stessa prosecuzione, e va quindi specificata per ciascuna di esse.

Il seguente percorso
![BRCICL_05](http://localhost:3000/immagini/BRCICL_005/BRCICL_05.png)si descrive con la tabella  "Gruppo C"


|   Nam="Alternative multiple - Gruppo C" |
| 
| .COL Txt="Operazione" LunAut=" " |
| ---|----|
| 
| .COL Txt="1" LunAut=" " |
| 
| .COL Txt="2" LunAut=" " |
| 
| .COL Txt="3" LunAut=" " |
| 
| .COL Txt="4" LunAut=" " |
| 
| .COL Txt="5" LunAut=" " |
| 10 | A | -- | -- | -- | -- |
| 20 | A | -- | -- | -- | B |
| 30 | A | -- | -- | -- | B |
| 40 | A | -- | -- | -- | B |
| 50 | B | -- | -- | -- | -- |
| 


Il limite dell'implementazione qui esposta (quattro posizioni del gruppo alternativa) è che una fase può provenire al massimo da quattro percorsi diversi.

Nel caso precedente il percorso era uno, in quanto i percorsi si riuniscono a monte della fase 50
![BRCICL_06](http://localhost:3000/immagini/BRCICL_005/BRCICL_06.png)
Un esempio di una fase che proviene da tre percorsi diversi è il seguente : 
![BRCICL_07](http://localhost:3000/immagini/BRCICL_005/BRCICL_07.png)
I punti A, B  e C non coincidono. Se così fosse ci sarebbe una sola alternativa, tra le fasi 80, 90 e 100.
Ingrandendo la zona all'interno del tratteggio si ottiene la seguente rappresentazione : 
![BRCICL_08](http://localhost:3000/immagini/BRCICL_005/BRCICL_08.png)
Si evidenzia così che la fase 40 può essere seguita dalla 80 o dalla 90, la 60 solo dalla 90 e la 30 dalla 90 o dalla 100.
La rappresentazione tabellare è quella del Gruppo D : 

|  Nam="Alternative multiple - Gruppo D" |
| 
| .COL Txt="Operazione" LunAut=" " |
| ---|----|
| 
| .COL Txt="1" LunAut=" " |
| 
| .COL Txt="2" LunAut=" " |
| 
| .COL Txt="3" LunAut=" " |
| 
| .COL Txt="4" LunAut=" " |
| 
| .COL Txt="5" LunAut=" " |
| 10 | A | -- | -- | -- | B |
| 20 | A | -- | -- | -- | C |
| 30 | A | -- | -- | -- | D |
| 40 | B | -- | -- | -- | E |
| 50 | B | -- | -- | -- | -- |
| 60 | C | -- | -- | -- | F |
| 70 | C | -- | -- | -- | -- |
| 80 | E | -- | -- | -- | -- |
| 90 | D | E | F | -- | -- |
| 100 | D | -- | -- | -- | -- |
| 


### Esempio 1 - Fasi raggruppate
Supponiamo di avere le seguenti alternative : 

|  Nam="Fasi raggruppate" |
| 
| .COL Txt="Ciclo Base" LunAut=" " |
| ---|----|
| 
| .COL Txt="Prima fase raggruppata" LunAut=" " |
| 
| .COL Txt="Seconda fase raggruppata" LunAut=" " |
|  10 |.     | 10 |
|  .    | 15 |. |
|  20 |.     |. |
|  .    |.     | 25 |
|  30 | 30 |. |
| 


La rappresentazione grafica del percorso è la seguente : 
![BRCICL_09](http://localhost:3000/immagini/BRCICL_005/BRCICL_09.png)con la tabella "Alternative con fasi raggruppate" : 

|  Nam="Alternative con fasi raggruppate" |
| 
| .COL Txt="Operazione" LunAut=" " |
| ---|----|
| 
| .COL Txt="1" LunAut=" " |
| 
| .COL Txt="2" LunAut=" " |
| 
| .COL Txt="3" LunAut=" " |
| 
| .COL Txt="4" LunAut=" " |
| 
| .COL Txt="5" LunAut=" " |
| 10 | A | -- | -- | -- | B |
| 15 | A | -- | -- | -- | C |
| 20 | B | -- | -- | -- | C |
| 25 | B | -- | -- | -- | -- |
| 30 | C | -- | -- | -- | -- |
| 

Riportiamo la compilazione "passo passo" della tabella relativa a questo esempio.
_3_Definizione della prima alternativa - Passo 1

|  Nam="Passo 1" |
| 
| .COL Txt="Operazione" LunAut=" " |
| ---|----|
| 
| .COL Txt="1" LunAut=" " |
| 
| .COL Txt="2" LunAut=" " |
| 
| .COL Txt="3" LunAut=" " |
| 
| .COL Txt="4" LunAut=" " |
| 
| .COL Txt="5" LunAut=" " |
| 10 | _1_A | -- | -- | -- | -- |
| 15 | _1_A | -- | -- | -- | -- |
| 20 | -- | -- | -- | -- | -- |
| 25 | -- | -- | -- | -- | -- |
| 30 | -- | -- | -- | -- | -- |
| 

_3_Dichiarazione dello sviluppo della fase 10 - Passo 2

|  Nam="Passo 2" |
| 
| .COL Txt="Operazione" LunAut=" " |
| ---|----|
| 
| .COL Txt="1" LunAut=" " |
| 
| .COL Txt="2" LunAut=" " |
| 
| .COL Txt="3" LunAut=" " |
| 
| .COL Txt="4" LunAut=" " |
| 
| .COL Txt="5" LunAut=" " |
| 10 | A | -- | -- | -- | _1_B |
| 15 | A | -- | -- | -- | -- |
| 20 | -- | -- | -- | -- | -- |
| 25 | -- | -- | -- | -- | -- |
| 30 | -- | -- | -- | -- | -- |
| 

_3_Completamento dello sviluppo della fase 10 - Passo 3

|  Nam="Passo 3" |
| 
| .COL Txt="Operazione" LunAut=" " |
| ---|----|
| 
| .COL Txt="1" LunAut=" " |
| 
| .COL Txt="2" LunAut=" " |
| 
| .COL Txt="3" LunAut=" " |
| 
| .COL Txt="4" LunAut=" " |
| 
| .COL Txt="5" LunAut=" " |
| 10 | A | -- | -- | -- | B |
| 15 | A | -- | -- | -- | -- |
| 20 | _1_B | -- | -- | -- | -- |
| 25 | _1_B | -- | -- | -- | -- |
| 30 | -- | -- | -- | -- | -- |
| 

_3_Dichiarazione dello sviluppo della fase 15 - Passo 4

|  Nam="Passo 4" |
| 
| .COL Txt="Operazione" LunAut=" " |
| ---|----|
| 
| .COL Txt="1" LunAut=" " |
| 
| .COL Txt="2" LunAut=" " |
| 
| .COL Txt="3" LunAut=" " |
| 
| .COL Txt="4" LunAut=" " |
| 
| .COL Txt="5" LunAut=" " |
| 10 | A | -- | -- | -- | B |
| 15 | A | -- | -- | -- | C |
| 20 | B | -- | -- | -- | -- |
| 25 | B | -- | -- | -- | -- |
| 30 | _1_C | -- | -- | -- | -- |
| 

_3_Completamento dello sviluppo della fase 15 - Passo 5

|  Nam="Passo 5" |
| 
| .COL Txt="Operazione" LunAut=" " |
| ---|----|
| 
| .COL Txt="1" LunAut=" " |
| 
| .COL Txt="2" LunAut=" " |
| 
| .COL Txt="3" LunAut=" " |
| 
| .COL Txt="4" LunAut=" " |
| 
| .COL Txt="5" LunAut=" " |
| 10 | A | -- | -- | -- | B |
| 15 | A | -- | -- | -- | _1_C |
| 20 | B | -- | -- | -- | -- |
| 25 | B | -- | -- | -- | -- |
| 30 | C | -- | -- | -- | -- |
| 

_3_Dichiarazione dello sviluppo della fase 20 - Passo 6

|  Nam="Passo 6" |
| 
| .COL Txt="Operazione" LunAut=" " |
| ---|----|
| 
| .COL Txt="1" LunAut=" " |
| 
| .COL Txt="2" LunAut=" " |
| 
| .COL Txt="3" LunAut=" " |
| 
| .COL Txt="4" LunAut=" " |
| 
| .COL Txt="5" LunAut=" " |
| 10 | A | -- | -- | -- | B |
| 15 | A | -- | -- | -- | C |
| 20 | B | -- | -- | -- | _1_C |
| 25 | B | -- | -- | -- | -- |
| 30 | -- | -- | -- | -- | -- |
| 

_3_Completamento dello sviluppo della fase 20 - Passo 7
Questa operazione non è necessaria, in quanto la fase 20 ha il completamento C comune alla fase 15, che è già stato eseguito.

### Esempio 2 - Ciclo Interno / Esterno
Supponiamo di avere le seguenti alternative (le fasi interne hanno suffisso I, quelle esterne hanno suffisso E).

| 
| .COL Txt="Tutto Interno" LunAut=" " |
| ---|----|
| 
| .COL Txt="Tutto Esterno" LunAut=" " |
| 
| .COL Txt="Prima fase esterna Seconda fase interna" LunAut=" " |
| 10I |.       |. |
|  .    | 15E | 15E |
|  .    | 20E |. |
| 30I | .      | 30I |
| 

La rappresentazione grafica del percorso è la seguente : 
![BRCICL_10](http://localhost:3000/immagini/BRCICL_005/BRCICL_10.png)con la seguente tabella : 

| 
| .COL Txt="Operazione" LunAut=" " |
| ---|----|
| 
| .COL Txt="1" LunAut=" " |
| 
| .COL Txt="2" LunAut=" " |
| 
| .COL Txt="3" LunAut=" " |
| 
| .COL Txt="4" LunAut=" " |
| 
| .COL Txt="5" LunAut=" " |
| 10I | A | -- | -- | -- | B |
| 15E | A | -- | -- | -- | C |
| 20E | C | -- | -- | -- | -- |
| 30I | B | C | -- | -- | -- |
| 


### Esempio 3 - Alternative multiple
Supponiamo di poter realizzare una lavorazione in un'unica fase, oppure in una sequenza di più fasi, che a loro volta si scompongono in più livelli.


|  R="70" |
| 
| .COL Txt="Codice fase" A="C" |
| ---|----|
| 
| .COL Txt="Descrizione" LunAut="1" A="L" |
| 10-1 | Lavorazione completa :  prima alternativa |
| 10-2 | Lavorazione completa :  seconda alternativa |
| 10-3 | Prima fase :  prima alternativa |
| 10-4 | Prima fase :  seconda alternativa |
| 10-5 | Prima fase :  terza alternativa |
| 20-1 | Seconda fase completa |
| 30-1 | Seconda fase parte prima |
| 30-2 | Seconda fase parte seconda |
| 


La rappresentazione grafica del percorso è la seguente : 
![BRCICL_11](http://localhost:3000/immagini/BRCICL_005/BRCICL_11.png)con la seguente tabella : 


| 
| .COL Txt="Operazione" LunAut=" " |
| ---|----|
| 
| .COL Txt="1" LunAut=" " |
| 
| .COL Txt="2" LunAut=" " |
| 
| .COL Txt="3" LunAut=" " |
| 
| .COL Txt="4" LunAut=" " |
| 
| .COL Txt="5" LunAut=" " |
| 10-1 | A | -- | -- | -- | -- |
| 10-2 | A | -- | -- | -- | -- |
| 10-3 | A | -- | -- | -- | B |
| 10-4 | A | -- | -- | -- | B |
| 10-5 | A | -- | -- | -- | B |
| 20-1 | B | -- | -- | -- | -- |
| 30-1 | B | -- | -- | -- | C |
| 30-2 | C | -- | -- | -- | -- |
| 


### Alternative con "memoria"
Consideriamo il seguente ciclo : 

| 
| .COL Txt="Fase" LunAut=" " |
| ---|----|
| 
| .COL Txt="Operazione" LunAut=" " |
| 10 | Tornitura Completa |
| 20 | Controllo |
| 40 | Finitura |
| 

che ha la seguente alternativa : 


| 
| .COL Txt="Fase" LunAut=" " |
| ---|----|
| 
| .COL Txt="Operazione" LunAut=" " |
| 15 | Tornitura |
| 20 | Controllo |
| 30 | Foratura |
| 40 | Finitura |
| 

Il percorso si rappresenta nel seguente modo : 
![BRCICL_12](http://localhost:3000/immagini/BRCICL_005/BRCICL_12.png)Questa struttura non può essere descritta nel modo fin qui esposto, in quanto la fase 20 non ha una prosecuzione univoca, ma dipendente dal percorso fatto in precedenza :  dovrebbe averne quindi "memoria".

In realtà questa rappresentazione è ambigua. L'oggetto alla fase 20 non rappresenta un'entità univoca :  quando proviene dalla fase 10 è diverso da quando proviene dalla fase 15. Ciò comporta problemi nella costificazione, nella determinazione e nel controllo della giacenza alla fase.

Anche da un punto di vista logistico i due oggetti vanno tenuti distinti, per farli proseguire correttamente.

Per eliminare l'ambiguità, bisogna codificare una nuova fase. Ad esempio, si può modificare in questo modo l'alternativa : 


| 
| .COL Txt="Fase" LunAut=" " |
| ---|----|
| 
| .COL Txt="Operazione" LunAut=" " |
| 15 | Tornitura |
| _1_20 | _1_Controllo |
| 30 | Foratura |
| 40 | Finitura |
| 

Il percorso diventa il seguente : 
![BRCICL_13](http://localhost:3000/immagini/BRCICL_005/BRCICL_13.png)Come si vede, l'ambiguità è stata eliminata :  i percorsi sono ritornati distinti :  al centro che esegue le fasi 25 e 20 si presentano due code diverse.

# Descrizione tecnica e operativa della funzione realizzata
E' stato realizzato il programma BRFUALT, di tipo funizzato, che permette la definizione e la selezione delle alternative di ciclo, legate all'oggetto ricevuto.

Le funzioni possibili sono le seguenti : 
>IMP impostazione alternative e scelta alternative attive
SCE solo scelta alternative attive
VIS solo visualizzazione


Se l'oggetto è un ordine di produzione vi sono anche le funzioni
>IMPRIC
IMPCIE
SCERIC
SCECIE

simili alla IMP e alla VIS con in più la possibilità, se assente il ciclo dell'ordine, di crearlo in modo cieco con la funzione xxxCIE, e previa richiesta con la funzione xxxRIC, in modo tale che, all'atto della selezione delle alternative, esista il ciclo su cui operare.

Viene controllato che l'utente, nelle opzioni IMP e SCE, sia autorizzato alla variazione, e nell'opzione VIS alla visualizzazione del tipo ciclo impostato (nella classe BRCI15).

Il metodo deve contenere, nelle prime tre posizioni, il tipo ciclo (se è un ordine di produzione questo campo deve restare in bianco, in quanto viene assunto il tipo ciclo di memorizzazione del tipo impegno risorse dell'ordine stesso, campo che deve essere presente.)

Se il tipo ciclo prevede un ciclo prefisso (e se l'oggetto non è un ordine di produzione, nel qual caso il codice ciclo, nelle righe delle operazioni, viene sempre lasciato in bianco), si deve stabilire il codice ciclo di scansione. Esso può essere impostato nelle ultime tre posizioni del metodo :  se queste posizioni sono lasciate vuote, viene richiesto in un apposito formato all'ingresso della funzione.

Dato che la funzione rende attive e disattive le righe di ciclo modificandone lo stato, si devono decidere i valori in gioco. Lo stato disattivo è '00', mentre si assume come stato attivo lo stato principale di scansione (del tipo ciclo), se assente si assume lo stato di nascita (sempre del tipo ciclo). Se anche questo campo è assente si emette un messaggio d'errore e si termina la funzione.

# Descrizione operativa della gestione Alternative base
Viene quindi presentata la lista di tutte le operazioni del tipo ciclo e dell'oggetto ricevuto, filtrate dal codice ciclo in caso di ciclo prefisso.

Nella funzione 'IMP', (impostazione alternative) con l'opzione '02' si apre una finestra in cui si impostano il gruppo alternativa e l'alternativa della riga selezionata.

Se si inserisce un nuovo gruppo alternativa, la prima alternativa inserita viene dichiarata attiva, mentre le successive sono dichiarate inattive.

Se si assegna una fase ad una alternativa già attiva (su altre fasi), viene attivata anch'essa.

Se si pulisce il gruppo e l'alternativa su una fase, essa viene resa attiva.

Sia con la funzione 'IMP' sia con la funzione 'SCE' è inoltre possibile definire le alternative attive. Nell'ambito della funzione 'IMP' (applicata verosimilmente al ciclo dell'oggetto) si definiscono le alternative di default, nell'ambito della funzione 'SCE' (applicata al ciclo dell'ordine) si definiscono invece le alternative specifiche, valide solo per l'ordine in esame.

Per le fasi con alternativa, selezionandone una qualsiasi (con il carattere 'A') si ottiene l'effetto di attivare tulle le fasi della stessa alternativa (e dello stesso gruppo) e di disattivare le fasi di tutte le altre alternative dello stesso gruppo.

_3_Esempio : 
Viene riportato l'effetto di due attivazioni, rispettivamente sulla fase 0010 e sulla fase  0090.


| 
| .COL Txt="Gruppo Alternativa" LunAut=" " |
| ---|----|
| 
| .COL Txt="Alternativa" LunAut=" " |
| 
| .COL Txt="Fase" LunAut=" " |
| 
| .COL Txt="Stato Precedente" LunAut=" " |
| 
| .COL Txt="Azione" LunAut=" " |
| 
| .COL Txt="Stato Successivo" LunAut=" " |
| A | 01 | 0010 | 00 | A | 10 |
| A | 02 | 0020 | 00 |.   | 00 |
| A | 03 | 0030 | 10 |.   | 00 |
| .  | .    | 0040 | .    |.   |. |
| B | 01 | 0050 | 10 |.   | 00 |
| B | 01 | 0060 | 10 |.   | 00 |
| B | 02 | 0070 | 00 |.   | 00 |
| B | 03 | 0080 | 00 |.   | 10 |
| B | 03 | 0090 | 00 | A | 10 |
| B | 03 | 0100 | 00 |.   | 10 |
| 

Non è possibile disattivare una fase appartenente ad un gruppo alternativa :  lo si ottiene attivando un'altra fase dello stesso gruppo e di un'altra alternativa.

Le fasi 'singole' possono essere invece attivate e disattivate in modo autonomo, con l'opzione 'A' e 'D'.

Alla conferma dei dati impostati, se l'oggetto è un ordine di produzione, vengono rifasati gli impegni risorse se previsto nel campo rifasatura impegni del tipo impegni risorse (sia in modo cieco sia con richiesta conferma, a seconda del valore di questo campo).

# Descrizione operativa della gestione Alternative multiple
In questa modalità l'impostazione e la scelta delle alternative si eseguono in due formati diversi. Dall'impostazione è comunque sempre possibile passare alla scelta

Nell'impostazione delle alternative si presenta un formato con tutte le fasi e, accanto a ciascuna di esse, vengono riportati i cinque caratteri del gruppo alternativa (i quattro di selezione ed il quinto di prosecuzione). E' riportato inoltre il flag di rilevanza operazione, che può essere manutenzionato in questo formato.

Nella scelta delle alternative vengono invece riportate tutte le combinazioni di percorsi possibili. Viene evidenziato inoltre l'inizio e la fine di ogni gruppo.

Per le fasi interne al gruppo è possibile unicamente attivare un percorso (operando sull'opzione della riga che costituisce la fine di ogni percorso, contrassegnata da una freccia accanto all'opzione). Verranno attivate tutte le fasi del percorso, e disattivate quelle degli altri percorsi dello stesso gruppo (ad eccezione delle fasi in comune al percorso attivato).

Le fasi esterne al gruppo possono invece essere attivate e disattivate autonomamente, con le opzioni "A" e "D".

Riportiamo il formato di attivazione dell'esempio 1.

Si possono attivare solo gli estremi delle alternative (contrassegnati da una freccia). Si ottengono i seguenti risultati, in base al percorso selezionato : 


| 
| .COL Txt="Fase" LunAut=" " |
| ---|----|
| 
| .COL Txt="Scelta A" LunAut=" " |
| 
| .COL Txt="Scelta B" LunAut=" " |
| 
| .COL Txt="Scelta C" LunAut=" " |
| 10 | Attiva | Attiva | _1_Disattiva |
| 15 | _1_Disattiva | _1_Disattiva | Attiva |
| 20 | Attiva | _1_Disattiva | _1_Disattiva |
| 25 | _1_Disattiva | Attiva | _1_Disattiva |
| 30 | Attiva | _1_Disattiva | Attiva |
| 


# Implementazione nella lista delle righe ciclo
Nella lista delle righe del ciclo di un oggetto, (programma BRCI15L) è stato aggiunto il tasto funzionale F15, che lancia la gestione delle alternative in modalità impostazione delle alternative stesse. Nel caso di alternative multiple è attivo anche il tasto F16 che lancia direttamente la scelta dell'alternativa. Se l'oggetto è un ordine di produzione la funzione è 'IMPRIC', vale a dire che si intende passare alla gestione delle alternative con la possibilità, previa conferma dell'operatore, di generare il ciclo dell'ordine se assente.  Il metodo, in questo caso non è significativo. Se invece l'oggetto è di un altro tipo (normalmente un articolo) la funzione è 'IMP', mentre nel metodo si impostano il tipo ciclo ed il ciclo (prefisso) ricevuto. Al ritorno dalla funzione viene ricostruita la lista in modo da presentare il nuovo stato delle righe, che può essere stato modificato dalla funzione stessa.

# Utilizzo nelle funzioni dell'ordine di produzione
Se si desidera che vengano esaminate le fasi da attivare e disattivare, per tutti gli ordini di produzione che si inseriscono, si deve codificare questa funzione, in modalità 'SCECIE' o 'SCERIC', tra le azioni di immissione dell'ordine. In questo caso essa comprende la creazione del ciclo dell'ordine (in modalità cieca o visualizzata), e quindi si presenterà la scelta delle alternative attive. E' opportuno comunque codificare la stessa funzione tra le azioni ammesse dell'ordine, in modo da poter variare le operazioni attive in una fase successiva all'inserimento dell'ordine.
