Come si costruisce una mappa
# Prima di iniziare

## Definizioni delle sezioni


E' possibile impostare l'opzione per il **refresh** della mappa corrente.
E' necessario aggiungere, prima o dopo la definizione delle sezioni, il tag

..G.TIM Ref="10000"

dove '10000' indica (come esempio) il periodo di attesa tra due successivi aggiornamenti espresso in millisecondi.
Se il periodo non è indicato, o è indicato in modo sbagliato, viene impostato il default a 10000ms

# Definizioni delle sezioni.

Una schermata può contenere più sezioni che devono essere per prima cosa definite in cima allo script con **i propri nome, sfondo e coordinate.**
La definizione avviene tramite un tag della forma

..D.SEZ Nam="proprioNome" Bgd="MB;nomefile;nomeFigura" Crd="a,b,c,d"

La struttura del path dell'immagine di sfondo è fissa :  la directory di riferimento contenente tutte le immagini è %HOMELOOCUP%\SmeupSources\LOOCUP_IMG\MB\SCP_MAP\
Ogni immagine, per motivi di stabilità, non deve superare la dimensione di 100KB.
Le coordinate indicano la posizione della sezione all'interno della finestra principale e possono essere espresse in due diversi modi : 

_1_IN MODO RELATIVO  : 
La coppia >(a;b)_ indica la posizione relativa come se la finestra fosse una matrice(riga;colonna).
La coppia >(c;d) indica rispettivamente larghezza e altezza della sezione.
 - es :  Crd="1,1,100,100"

_1_ IN MODO ASSOLUTO : 
La coppia> (a;b) indica le coordinate assolute dell'angolo in alto a sx della sezione all'interno della finestra principale e ogni valore è seguito da x o y.
La coppia >(c;d) indica rispettivamente larghezza e altezza della sezione
  - es :  Crd="100x,100y,100,100".

Le coordinate assolute relative alla posizione del mouse sono sempre riportate in basso a sx, nella barra inferiore di Loocup, alle voci "xModule=, yModule="

## Costruzione delle sezioni
Ogni sezione può contenere più oggetti definiti al suo interno.
Ogni oggetto è definito nel modo seguente : 

  _1_..G.SEZ       Nam="Esempio" Tps="Esempio Sezione".
  _1_..G.SUB       Nam="Esempio oggetto" Tps="Esempio oggetto".
  _1_..G.SET.FRM   Shp="RECT" Crd="221,662,134,233".
  _1_..G.SET.LAY  Fill="ON" Img="OFF" Txt="MOUSEON".
  _1_..G.SET.OBJ        Tip="MB" Par="SCP_MAP" Cod="S8" Exec="F(MAP;JATRE_34C;) 1(MB;SCP_MAP;S8)".
  _1_..G.SET.IMG   Path="MB;SCP_MAP;S8".
  _1_..G.SET.TXT   Text="Esempio oggetto" Crd="225,680" Color="255,0,0" Trsp="100%".

### ..G.SEZ
Indica l'inizio di definizione di una nuova sezione, in particolare la sezione
"Esempio". Tale istruzione può essere tralasciata quando è stata definita un'unica sezione all'interno dello script.
 Nam = Indica il nome di tale sezione
 Tps = Indica il tooltip associato alla sezione e visualizzato al passaggio del mouse nella sezione

### ..G.SUB
Indica l'inizio di definizione di un nuovo oggetto.
 Nam = Indica il nome di tale oggetto
 Tps = Indica il tooltip associato all'oggetto e visualizzato al passaggio del mouse in tale area attiva

### ..G.SET.FRM
Indica la configurazione dell'area attiva
 Shp = Indica la forma dell'area. Essa può essere _7_RECT, POLY, CIRCLE  o Crd = Indica le coordinate dell'area.
 >RECT = xAngoloAltoSx, yAngoloAltoSx, Width, Heigh.
 >CIRCLE = xCentro, yCentro, raggio.
 >POLY = xPunto1,yPunto1,xPunto2,yPunto2" In questo caso posso avere un numero di coppie ordinate a piacere e comporre figure di qualsiasi tipo.
Tutte le coordinate relative agli oggetti possono essere definite osservando il valore assunto da "xPanel" e "yPanel" nella barra inferiore di Loocup che sono espresse in millesimi e si riferiscono alla posizione relativa del mouse all'interno della singola sezione.

### ..G.SET.LAY
Indica le modalità di gestione dell'area attiva.
 _7_Fill >Indica la colorazione dell'interno dell'area
 _7_Img >Indica la presenza di un'immagine ulteriore all'interno dell'area
 _7_Text>Indica la presenza di testo all'interno dell'area
Ognuno di questi attributi può essere impostato a OFF, ALWAYS, MOUSEON a seconda che la caratteristica debba essere presente MAI, SEMPRE, AL PASSAGGIO DEL MOUSE


### ..G.SET.OBJ
Indica (tipo, parametro, codice) dell'oggetto per mantenere la funzionalità di tasto destro caratteristica di Loocup e la funzione da eseguire in corrispondenza del click sx sull'oggetto

### ..G.SET.IMG
Indica il percorso dell'immagine a comparsa nell'area attiva (sempre secondo il path fissato definito in precedenza)

### ..G.SET.TXT
Indica le caratteristiche del testo aggiuntivo : 
 _7_Text  >Contenuto del testo aggiuntivo
 _7_Crd  >Coordinate (x;y) in cui inserire il testo
                  _7_Color >Colore del testo
 _7_Trsp >Trasparenza del testo
