# OBIETTIVO
Fornire informazioni relative ai Solleciti di pagamento.

# FUNZIONI/METODI

## TABELLE
Con la Funzione TAB il servizio monitorizza la situazione della tabella  **C5X **(situazione solleciti) e in parte quella della **C53**(Impostazioni Base Pagamenti).

### TAB.C5X
Costruisce un'albero che riporta i tipi di sollecito caricati nella tabella **C5X**  (tipi sollecito);
l'abero è costruito su più livelli :  ogni livello rappresenta il sollecito base da cui discendono quelli più gravi, mantenendo così la logica con cui i solleciti stessi sono concepiti.
Per la chiamata della funzione, l'unico oggetto necessario è _9_l'oggetto1, in cui passo l'oggetto TA e il settore C5X.

### TAB.C53
Cotruisce una matrice che ritorna alcuni campi significativi dal punto di vista dell'analisi dei solleciti impostati nella tabella **C53**;
 essi sono : 
T$C53C : Primo Sollecito;
T$C53D : Spese Amm.x Soll.;
T$C53E : % Interessi di mora;
Per la chiamata della funzione, l'unico oggetto necessario è _9_l'oggetto1, in cui passo l'oggetto TA e il settore C53.

## HELP
La funzione Help mi serve ad ottenere informazioni sulla modalità di composizione delle lettere di sollecito.

### HLP.DOC
Questa funzione mi costruisce un componente Editor di tipo HTM in cui ottengo la documentazione di help della lettera di sollecito.
Per fare questo viene utilizzata la /copy **£C5H** con la funzione >HLP** con metodo >POS per il posizionamento e poi >SCA per la scanzione ed il ritorno in £C5HTE del contenuto della riga di help. Questa funzione è stata appositamente creata.
Per la chiamata della funzione, non è necessario alcun oggetto.

## SOLLECITI
Questa funzione mi permette di ottenere informazioni sullo stato dei solleciti, riproducendo cioé interrogazione, estrazione e lettera di sollecito.

### SOL.EST
Costruisce una matrice che riproduce i dati leggibili dalla estrazione solleciti ottenuta dal menù "C5 109005" (Contabilità generale-solleciti di pagamento).
Per ottenere i dati viene utilizza la /copy **£IRR** , e ricalcando il processo seguito dal programma generatore (C5NARRL).
Per la chiamata della funzione, l'unico oggetto necessario è _9_l'oggetto1, in cui passo l'oggetto CN.
Inoltre è necessario specificare anche il _9_paramentro, che è composto da due variabili :   metodo(_3_MET) e chiavi(_3_KEY). Tali due variabili possono assumere 2 (per ora) valori diversi, a seconda del risultato che voglio ottenere; se voglio ottenere l'estrazione di tutti i solleciti, utilizzerò  il metodo 4L con 2 chiavi (S5FL12 e S5AZIE), se invece voglio ottenere l'estrazione dei soli solleciti di un contatto specifico, utilizzerò il metodo 3L con 2 chiavi (S5TPOG e S5CDOG).

### SOL.INT
Se chiamata col componente MAT, costruisce una matrice che riproduce i dati leggibili dalla interrogazione solleciti ottenuta dal menù "C5 109015" (Contabilità generale-solleciti di pagamento).
Se chiamata col componente EXA costruisce un grafico a torta in cui vengono riportati i valori percentuali di un tipo sollecito rispetto all'importo totale da sollecitare per quel contatto. In realtà questa funzione può anche essere chiamata da una subsezione di tipo matrice, nel qual caso si ottiene la matrice dei tipi solleciti con i relativi pesi percentuali e importi totalizzati.
Per la chiamata della funzione, l'unico oggetto necessario è _9_l'oggetto1, in cui passo l'oggetto CN.



 :  : PRO.SER Cod="SOL.SIN.1" Tit="Solleciti. Sintesi" Fun="F(EXB;C5SER_12;SOL.SIN)"

 :  : PRO.SER Cod="SOL.EST.2" Tit="Solleciti. Estrazione" Fun="F(MAT;C5SER_12;SOL.EST) 2(CN;;-(F;;CN;Contatto)) P( MET(-(F;;**;Metodo)) KEY(-(F;;NR;Chiavi)))"

 :  : PRO.SER Cod="SOL.EST.3" Tit="Solleciti. Estrazione" Fun="F(EXA;C5SER_12;SOL.EST)" Ref="SOL.EST.2"

 :  : PRO.SER Cod="SOL.INT.4" Tit="Solleciti. Interrogazione" Fun="F(MAT;C5SER_12;SOL.INT) 2(CN;;-(F;;CN;Contatto))"

 :  : PRO.SER Cod="SOL.INT.5" Tit="Solleciti. Interrogazione" Fun="F(EXA;C5SER_12;SOL.INT)" Ref="SOL.INT.4"

 :  : PRO.SER Cod="HLP.DOC.6" Tit="Help. Lettere sollecito" Fun="F(HTM;C5SER_12;HLP.DOC)" Ref="SOL.INT.4"

