# OBIETTIVO
Trattamento e trasformazione numeri in stringhe, numeri romani, stringhe editate e viceversa.

# PREREQUISITI
D/COPY QILEGEN,£TNUE
C/COPY QILEGEN,£TNU

# PARAMETRI
## PARAMETRI DI INPUT
### Funzione :  _campo £TNUTP_ Tipo di input
    N) Trasformare un numero in un campo editato
    X) Trasformare un numero in una stringadi lettere XAB (riporta il numero XAB dell'eventuale bolla emessa)
    A) Trasformare una stringa in un numero
    L) Trasformare un numero in una stringa di livello
    S) Trasformare una stringa in un campo editato
    Z) Trasformare un numero in un campo editato ma formatta anche il numero 0
    R) Trasformare un numero in un numero romano
### Parametro di controllo :  _campo £TNUPD_
Formato :  pd --> dove **p** è il numero di punti separatori (0-4) e **d** è il numero dei decimali (0-7)
### Separatore decimali :  _campo £TNUSD**
'  '(blanks)=virgola
'.'=punto
### Numero :  campo £TNUNR
numero da convertire in stringa
### Allineamento :  _campo £TNUAL**
--> Se 'S' restituisce il campo editato ed allineato a sinistra
--> Se 'X' restituisce il campo editato ed allineato a sinistra rimuovendo gli zero non significativi
### Campo non editato :  _campo £TNUNE**
In funzione 'N' o 'Z' se diverso da '  ' ritorna anche il campo non editato
In funzione 'A' se diverso da '  ' esclude i caratteri non editati
### Formato rappresentazione segno
'  ' = segno - a destra
'S' = segno - a sinistra
## PARAMETRI DI OUTPUT
### _campo £TN_
Numero editato e allineato a dx (schiera)
### _campo £TNUSX_
Numero editato e allineato a sx
### _campo £TNUED_
Numero non editato

# ESEMPI DI FLUSSI

## FLUSSO (caso 1)
 Riceve un numero e un parametro di controllo e restituisce
 una schiera di 30 caratteri contenente il numero allineato
 a destra (con il segno, blank o meno, a posizione 30),
 senza gli zeri non significativi e con il numero voluto
 di decimali e di punti separatori delle migliaia.
### Input :   £TNUTP   Tipo di input :  N=numerico
           £TNUPD   Parametro controllo. Formato :  pd, dove
                      p = numero di punti separatori (0-4)
                      d = numero di decimali (0-7)
           £TNUSD   Separatore decimali
                      ' '= virgola  altro= punto
           £TNUNR   Numero da editare
           £TNUAL   Se 'S' restituisce anche il campo editato
                   Se 'X' come 'S' e rimozione zeri non significativi
          £TNUNE   Se diverso da ' ' ritorna anche il campo
                     non editato
          £TNUFS   Formato rappresentazione segno
                     ' ' = segno - a destra
                     'S' = segno - a sinistra
### Output :  £TN      Numero editato e allineato a dx (schiera)
          £TNUSX   Numero editato e allineato a sx
          £TNUED   Numero non editato

Esempi : 
         £TNUNR        £TNUPD           _______ £TN ________
  111222333444,555        33   --->     111.222.333.444,555
  111222333444,555        12               111222333.444,55
         -123456,7        33                    123.456,700-
         -123456,7        00                         123456-
             0,001        32                           0,00
                 0        32                   (blank)

## FLUSSO (caso 2)
Riceve una schiera di caratteri e restituisce un numero.
Vengono trattati i soli caratteri numerici, si intercetta
la virgola per l'impostazione dei decimali.
 : T03 Input :   £TNUTP   Tipo di input :  A=alfanumerico
             £TNUSD   Separatore decimali
                      ' '= virgola  altro= punto
             £TN      Schiera con numero da convertire
      N.B.
       Per garantire continuità con il passato, se vengono
       impostati £TNUAL e/o £TNUNE, la funzione £TNUTP viene
       forzata a "S" (caso 3)
### Output :  £TNUNR   Numero ottenuto

 Esempi : 
_______ £TN_________    £TNUPD                    £TNUNR
       A2 0/1.AA4,-        ..                           2014-   *NB
               1-          ..                              1
111.222.333.444,555        ..               111222333444,555
   111222333.444,55        ..                111222333444,55
       123.456,700-        ..                     123456,700-
           -123456-        ..                         123456-
              00,00        ..                              0
            (blank)        ..                              0

*NB : 
Se l'ultimo carattere della stringa è uno tra 'èJKLMNOPQR' la copy
lo interpreta come un carattere non editato e aggiunge alla
stringa rispettivamente (0-,1-,2-,3-,4-,5-,6-,7-,8- o 9-)
per evitare questo comportamento impostare £TNUNE='1' e l'ultimo
carattere verrà escluso
 Esempi : 
_______ £TN_________    £TNUNE                    £TNUNR
              100L         .                      1003-
              100R         .                      1009-
              100L         1                       100
              100R         1                       100

## FLUSSO (caso 3)
 Riceve una schiera di caratteri e un parametro di controllo
 e restituisce un campo editato.
###  Input :   £TNUTP   Tipo di input :  S=alfanumerico
          £TNUPD   Parametro controllo. Formato :  pd, dove
                     p = numero di punti separatori (0-4)
                     d = numero di decimali (0-7)
          £TNUSD   Separatore decimali
                     ' '= virgola  altro= punto
          £TN      Schiera con numero da convertire
          £TNUAL   Se 'S' restituisce anche il campo editat
                     e allineato a sinistra
          £TNUNE   Se diverso da ' ' ritorna anche il campo
                     non editato
          £TNUFS   Formato rappresentazione segno
                     ' ' = segno - a destra
                     'S' = segno - a sinistra
 : T03  Output :  £TN      Numero editato e allineato a dx (schiera
          £TNUSX   Numero editato e allineato a sx
          £TNUED   Numero non editato
          £TNUNR   Numero ottenuto
## FLUSSO (caso 4)
Riceve un numero e restituisce una schiera contenente una
stringa di lettere per XAB
### Input :   £TNUTP   Tipo di input :  X=lettere per XAB
          £TNUPD   Parametro controllo. Formato :  pd, dove
                     p = numero di punti separatori (0-4)
                     d = numero di decimali (0-7)
          £TNUSD   Separatore decimali
                     ' '= virgola  altro= punto
          £TNUNR   Numero da editare
          £TNUAL   Allineamento : 
                     'D'= a destra   altro= a sinistra
###  Output :  £TNUNX   Numero editato per XAB

Esempi : 
         £TNUNR       £TNUPD        _________£TNUNX__________
    1000000,100         13   --->  '            AZZZ.ZZZ,AZZ '


 : T02 FLUSSO (caso 5)
 Riceve un numero, un carattere di riempimento (default '.')
 e una lunghezza massima, e lo traforma in una stringa di
 livello.
### Input :   £TNUTP   Tipo di input :  L=stringa di livello
           £TNUNR   Numero da editare  (max 99)
           £TNULL   Lunghezza totale (min. 2 max.30)
           £TNULC   ' ' Riempimento '.'
                    'x' Riempimento carattere x
###   Output :  £TNUSX   Stringa di composizione del livello

 Esempi : 
 £TNUNR   £TNULC       £TNULL          £TNUSX
                                       1---+----+--...
     1                     5           1
     3                     5           ..3
     6                     5           ....6
     1      -              5           1
     3      -              5           --3
     6      -              5           ----6
### FLUSSO (caso 6)
Uguale a flusso 1 se £TNUNR è diverso da 0.
Se £TNUNR uguale a 0 restituisce una stringa formattata
Esempi : 
         £TNUNR        £TNUPD           _______ £TN ________
                 0        32                           0,00
                 0        30                              0


### FLUSSO (caso 7)
Riceve un numero (da 1 a 9999) e lo trastorma in una stringa
contenente il numero romano
Se il numero è maggiore di 9999 in £TNUSX ritorna blanks
Esempi : 
         £TNUNR                         £TNUSX
               123                      CXXIII



# ESEMPIO DI CHIAMATA (Caso 1)
                     MOVEL'N'       £TNUTP
                     Z-ADD<numero>  £TNUNR
                     Z-ADD<pd>      £TNUPD
                     EXSR £TNU
                     MOVEA£TN       <stringa>

_1_==============================================================================================
ATTENZIONE !!  :  £TN è una schiera quindi la stringa va inserita con un MOVEA non solo con un MOVE, pena l'overflow. è consigliabile pulire la schiera £TN con un CLEAR prima di valorizzarla.
==============================================================================================
