# Generalità

Anche per i device mobile, lo script di scheda rappresenta il principale strumento di definizione del contenuto delle videate grafiche.

# Peculiarità

La sintassi di definizione è la medesima prevista per lo sviluppo di script di scheda per il client loocup e per Web.UP. Rispetto a quello che si può fare sul client e sul web, vigono però varie limitazioni ed alcune peculiarità.
A seguire, verrà evidenziato tutto quello che è possibile fare, mentre, rispetto alle limitazioni si può assumere che tutto ciò che non è specificato non sia previsto.

# Sezioni

Nel disegno è possibile sfruttare sia la suddivisione orizzontale che la suddivisione verticale ed ad ogni sezione è inoltre attribuibile una dimensione in % (percentuale) oppure in pixel, come previsto per il client loocup e Web.UP.

NOTA BENE_ :  l'utilizzo di un numero superiore di sezioni rispetto al massimo previsto, invalidano la scheda per il device mobile, che produrrà un messaggio informativo relativo all'invalidità del layout.

# Subsezioni

In una sezione è richiamabile una sola subsezione. Nel caso ne venga richiamata più di una ad eccezione della prima le altre verranno ignorate, senza alcuna segnalazione o malfunzionamento.
Alla subsezione è attribuibile un titolo (compreso il valore *NONE), anche se non è previsto che il tiolo possa essere sovrascritto da servizio o che possa contenere variabili di loocup. Al massimo può contenere quelle da script (cioè quelle con la _&_).

I componenti richiamabili in una subsezione sono praticamente tutti quelli che abbiamo a disposizione come : 
* Alberi
* Matrici
* Input Panel
* Sezioni Htm
* Immagini
* Liste di Immagini
* OutputPanel
* Matrice di aggiornamento
* Calendario
* Grafici
* ProgressBar
Etc.... I pochi componenti non utilizzabili in mobile sono evidenziati nello showcase (Versione mobile), se proveremo a entrare nel loro esempio ci verrà proposto un messaggio informaativo "Componente non ancora supportato in mobile".

Fra i componenti citati, non è inclusa la scheda stessa. Non è infatti possibile richiamare una scheda all'interno di una subsezione.
Per ottenere questo risultato sarà necessario affidarsi a dinamismi o se opportuno attraverso funzionalità di "include" degli script.

NOTA BENE_ :  anche il richiamo di una scheda in una subsezione, invalida la scheda per il device mobile, che produrrà un messaggio informativo relativo all'invalidità del layout.

# Dinamismi

Come per il client loocup e Web.UP è possibile sfruttare i dinamismi per innescare delle funzioni al compimento di alcune azioni. E' quindi possibile sfruttare le istruzioni G.DIN.
Su tali istruzioni è possibile sfruttare le variabili di loocup normalmente previste anche per client (es. su un matrice al click ho a disposizione tutte le variabili corrispondenti ai campi della riga di matrice).
E' inoltre possibile sfruttare l'attributo "Enabled" al fine di condizionare in dinamismo a particolari condizioni.

Sono invece previsti alcuni limiti operativi : 
* Per ogni evento è prevista al massimo l'esecuzione di un solo dinamismo.
* Non tutte le forme di dinamismo sono attive, lo sono quelle previste per i componenti utilizzabili, compatibilmente con le funzionalità del device (es. è previsto il When="Click" ma non il When="DblClick").

Infine di particolare rilevanza e peculiare del device mobile, è il fatto di poter indicare nel dinamismo l'esecuzione di comandi specifici del device mobile. In particolare mettendo all'interno dell'attributo "Exec" una delle seguenti diciture : 
* tel : //nnnnnn
* mailto : //mmmmmm@mmmm.mm
Dove "n" sta per il numero di telefono e "m" per l'indirizzo mail, è possibile far partire una telefonata o appunto l'invio di una mail.

# Variabili

Sono anticipato anche al punto precedente, sono gestite tutte le forme di variabili previste per il client loocup, sia quelle gestite dal server (cioè quelle con la "&"), che quelle gestite dal client (cioè quelle indicate fra parentesi quadra).

Sono quindi utilizzabili le variabili : 
* Create nello script attraverso le istruzioni S.VAR.VAL
* Rese disponibili dai componenti specifici (es. sull'albero, T1, P1, K1, Fu o sulla matrice quelle corrispondenti ad ogni colonna)
* Definite negli script di configurazione SCP_CLO
* Inviate da servizio

#  Gestione di una scheda tramite IF

E' possibile inserire in una scheda di Sme.UP delle condizioni IF, in modo da far assumere comportamenti diversi alla scheda in base al dispositivo dalla quale è stata aperta.

W = Se la scheda è aperta tramite Web.UP
C = Se la scheda è stata aperta tramite il client Looc.UP
T = Se la scheda è stata aperta da un device di tipo tablet
P = Se la scheda è stata aperta da uno smartphone

Vediamo un veloce esempio per capire meglio : 

 :  : I.IF.OPE F1(&AM.DV) OP(LS) F2(W;C;T)
 :  : G.SEZ Pos(1A)
 :  : G.SUB.CHA Tit="Gantt Macchine"
 :  : G.SET.CHA Typ="GANT" Asp="2D"
 :  : D.FUN.STD F(EXA;B£SER_46;WRK.SCP) 1(MB;SCP_SET;WETEST_EXA) 2(;;EXA_015)
 :  : G.SEZ Pos(1B)
 :  : G.SUB.CHA Tit="Gantt Commesse"
 :  : G.SET.CHA Typ="GANT" Asp="2D"
 :  : D.FUN.STD F(EXB;B£SER_46;WRK.SCP) 1(MB;SCP_SET;WETEST_EXA) 2(;;EXA_016)
 :  : I.IF.END

 :  : I.IF.OPE F1(&AM.DV) OP(=) F2(P)
 :  : G.SEZ Pos(1)
 :  : G.SUB.CHA Tit="Gantt Macchine"
 :  : G.SET.CHA Typ="GANT" Asp="2D"
 :  : D.FUN.STD F(EXA;B£SER_46;WRK.SCP) 1(MB;SCP_SET;WETEST_EXA) 2(;;EXA_015)
 :  : G.SEZ Pos(2)
 :  : G.SUB.CHA Tit="Gantt Commesse"
 :  : G.SET.CHA Typ="GANT" Asp="2D"
 :  : D.FUN.STD F(EXB;B£SER_46;WRK.SCP) 1(MB;SCP_SET;WETEST_EXA) 2(;;EXA_016)
 :  : I.IF.END

In pratica con questa condizione di IF dentro lo stesso script possiamo far assumere alla scheda diversi comportmaneti in base al dispositivo da dove la stiamo visualizzando.
Se la scheda la visualizzeremo da web, Client o tablet avremo due grafici uno affianco all'altro, se invece la stessa scheda la visualizziamo da mobile avremo un grafico sotto l'altro.



