 :  : HEA RESP(FD) STAT(10)
# OBIETTIVO
Fornire tramite i componenti semaforo, label e gauge lo stato del cespite alla data di oggi.
Il servizio tiene conto, per fornire lo stato, della linea ammortamento passata.
Oggetto1 = cespite
Oggetto2 = linea ammortamento (TAA5C)
# FUNZIONI/METODI
##    STATO CESPITE
### STA.SEM
Costruisce un semaforo.
Le luci del semaforo rappresentano lo stato del cespite con il seguente significato : 

- VERDE :   il cespite è in Ammortamento;
- GIALLO :  il cespite è stato già interamente ammortizzato;
- ROSSO :   il cespite è stato Alienato/Venduto;

All'interno della luce del semaforo compare inoltre un valore che assume significati diversi per le diverse luci : 

- VERDE :   quota già ammortizzata ad oggi;
- GIALLO :  quota già ammortizzata ad oggi (corrisponde in questo caso al valore del cespite stesso);
- ROSSO :   quota con cui il cespite è stato venduto/alienato;

### STA.LAB
Costruisce una label.
La label indica lo stato del cespite distinguendo i casi di : 

- cespite ammortizzato;
- cespite in ammortamento;
- cespite venduto;
- cespite alienato;

### STA.GAU
Costruisce un cruscotto.
Il cruscotto riporta solamente due casistiche : 

- cespite in ammortamento
 Il valore minimo del cruscotto è zero, mentre il valore massimo è il valore del cespite.
 L'ago punta al valore già ammortizzato ad oggi.
- cespite ammortizzato
 Il valore minimo del cruscotto è zero, mentre il valore massimo è il valore del cespite.
 L'ago punta al valore massimo.

### STA.MAT
Crea la matrice dei valori del cespite. Sfruttando la /COPY £A5E estrae i dati alla data di oggi.
##    SCHEDA CESPITE
### SCH.LIN
Costruisce una matrice o un grafico riproducendo il piano ammortamento del cespite per la linea passata.
Posso decidere di non passargli la linea; in questo ultimo, ottengo la matrice completa di tutti i movimenti per
tutte le linee.
### SCH.GRA
Costruisce il grafico comparativo di tutte le linee con cui è stato inserito il cespite utilizzando come asse il tempo,
e come serie i residui di ogni linea alla data.
##    MOVIMENTI
### MOV.ELE
Crea una matrice che estrae l'elenco dei movimenti del cespite chiamato dalla scheda
##    REGISTRAZIONI
### REG.TES
Crea una matrice che riporta i dati della testata della registrazione relativa ad un movimento scelto.
### REG.RIG
Crea una matrice che riporta i dati delle righe di registrazione relative alla testata scelta.
### REG.DOC
Crea una matrice che risale al documento legato alla registrazione del movimento relativo al cespite.
Vengono esposti il tipo, numero, data documento e il tipo, numero, pratica protocollo.
# SCHEDE CONTENENTI ESEMPI DI CHIAMATE
 :  : DEC T(MB) P(SCP_SCH) K(CE)

 :  : PRO.SER Cod="STA.SEM.1" Tit="STATO CESPITE. Semaforo" Fun="F(EXB;A5SER_01;STA.SEM) 1(CE;;-(O;;CE;Cespite)) 2(TA;A5C;-(O;;TAA5C;Linea)) P()"

 :  : PRO.SER Cod="STA.LAB.2" Tit="STATO CESPITE. Label" Fun="F(EXB;A5SER_01;STA.LAB)" Ref="STA.SEM.1"

 :  : PRO.SER Cod="STA.GAU.3" Tit="STATO CESPITE. Cruscotto" Fun="F(EXB;A5SER_01;STA.GAU)" Ref="STA.SEM.1"

 :  : PRO.SER Cod="STA.MAT.4" Tit="STATO CESPITE. Matrice" Fun="F(EXB;A5SER_01;STA.MAT)" Ref="STA.SEM.1"

 :  : PRO.SER Cod="STA.MAT.5" Tit="STATO CESPITE. Matrice" Fun="F(EXA;A5SER_01;STA.MAT)" Ref="STA.SEM.1"

 :  : PRO.SER Cod="SCH.LIN.6" Tit="SCHEDA CESPITE. matrice/grafico della/delle linea/linee" Fun="F(EXB;A5SER_01;SCH.LIN) 1(CE;;-(O;;CE;Cespite)) 2(TA;A5C;-(F;;TAA5C;Linea)) P()"

 :  : PRO.SER Cod="SCH.LIN.7" Tit="SCHEDA CESPITE. matrice/grafico della/delle linea/linee" Fun="F(EXA;A5SER_01;SCH.LIN)" Ref="SCH.LIN.6"

 :  : PRO.SER Cod="SCH.GRA.8" Tit="SCHEDA CESPITE. grafico comparativo delle linee" Fun="F(EXB;A5SER_01;SCH.GRA) 1(CE;;-(O;;CE;Cespite)) P()"

 :  : PRO.SER Cod="SCH.GRA.9" Tit="SCHEDA CESPITE. grafico comparativo delle linee" Fun="F(EXA;A5SER_01;SCH.GRA)" Ref="SCH.GRA.8"

 :  : PRO.SER Cod="MOV.ELE.10" Tit="MOVIMENTI CESPITE. Elenco" Fun="F(EXB;A5SER_01;MOV.ELE) 1(CE;;-(O;;CE;Cespite)) P()"

 :  : PRO.SER Cod="REG.TES.11" Tit="REGISTRAZIONI. Testata" Fun="F(EXB;A5SER_01;REG.TES) 1(E4;;-(O;;E4;Reg.contabile)) P()"

 :  : PRO.SER Cod="REG.RIG.12" Tit="REGISTRAZIONI. Righe" Fun="F(EXB;A5SER_01;REG.RIG) 1(E5;;-(O;;E5;Riga Registraz.)) P()"

 :  : PRO.SER Cod="REG.DOC.13" Tit="REGISTRAZIONI. Documento" Fun="F(EXB;A5SER_01;REG.DOC) 1(E4;;-(O;;E4;Reg.contabile)) P()"

