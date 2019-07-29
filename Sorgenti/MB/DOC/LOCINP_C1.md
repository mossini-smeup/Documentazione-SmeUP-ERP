# Prima di iniziare
 :  : PAR
E' possibile impostare l'opzione per il **refresh** della mappa corrente.
E' necessario aggiungere, prima o dopo la definizione delle sezioni, il tag

  ..G.TIM Ref="10000"

dove '10000' indica (come esempio) il periodo di attesa tra due successivi aggiornamenti espresso in millisecondi.
Se il periodo non è indicato, o è indicato in modo sbagliato, viene impostato il default a 10000ms


# Definizioni delle sezioni.
 :  : PAR
Una schermata può contenere più sezioni che devono essere per prima cosa definite in cima allo script con **i propri nome, sfondo e coordinate.**
La definizione avviene tramite un tag della forma

 ..D.SEZ Nam="proprioNome" Bgd="MB;nomefile;nomeFigura" Crd="a,b,c,d"

La struttura del path dell'immagine di sfondo è fissa :  la directory di riferimento contenente tutte le immagini è %HOMELOOCUP%\SmeupSources\LOOCUP_IMG\MB\SCP_MAP\
Ogni immagine, per motivi di stabilità, non deve superare la dimensione di 100KB.
Le coordinate indicano la posizione della sezione all'interno della finestra principale e possono essere espresse in due diversi modi : 


_1_IN MODO RELATIVO  : 
 :  : PAR
 La coppia >(a;b)_ indica la posizione relativa come se la finestra fosse una matrice(riga;colonna).
  La coppia >(c;d) indica rispettivamente larghezza e altezza della sezione.
  - es :  Crd="1,1,100,100"


_1_ IN MODO ASSOLUTO : 
 :  : PAR
La coppia> (a;b) indica le coordinate assolute dell'angolo in alto a sx della sezione all'interno della finestra principale e ogni valore è seguito da x o y.
La coppia >(c;d) indica rispettivamente larghezza e altezza della sezione
  - es :  Crd="100x,100y,100,100".

Le coordinate assolute relative alla posizione del mouse sono sempre riportate in basso a sx, nella barra inferiore di Loocup, alle voci "xModule=, yModule="

