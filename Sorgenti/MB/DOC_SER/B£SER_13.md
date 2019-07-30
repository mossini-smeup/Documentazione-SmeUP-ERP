 :  : HEA RESP(FD) STAT(10) USAG(FD)
# OBIETTIVO
Fornire tutte le informazioni realtive agli Indirizzi (**oggetto IN**) dato un contatto o dato un indirizzo.

# Funzioni e Metodi

## ESP ESPLOSIONE

Dato un contatto e un tipo indirizzo, ottenere i valori presenti per quel contatto relativi
a quel tipo indirizzo.
In Oggetto 1 passo il tipo contatto e il codice;
in Oggetto 2 passo il tipo indirizzo.

Dato un contatto ottenere tutti i tipi indirizzo e i relativi valori presenti per quel
contatto.
In Oggetto 1 passo il tipo contatto e il codice;
in Oggetto 2 non passo nulla;

Il servizio in entrambi i casi torna una matrice contenete le informazioni relative ai due oggetti in questione.

## IMP IMPLOSIONE

Dato un tipo indirizzo e un valore, ottenere il tipo e codice contatto cui appartiene.
In Oggetto 1 non passo né il tipo contatto né il codice;
in Oggetto 2 passo il tipo e il codice indirizzo.

Dato un tipo indirizzo ottenere tutti i valori di tutti i contatti relativamente a quel tipo
indirizzo.
In Oggetto 1 non passo né il tipo contatto né il codice;
in Oggetto 2 passo il tipo indirizzo.

Il servizio in entrambi i casi torna una matrice contenete le informazioni relative ai due oggetti in questione.

## EST ESPLOSIONE TIPO

Dato un contatto ottenere tutti i tipi indirizzo presenti per quel contatto.
In Oggetto 1 passo il tipo e il codice contatto;
Il servizio restituisce un albero contenente tipo parametro e codice degli indirizzi presenti.







 :  : PRO.SER Cod="ESP.1" Tit="Esplosione. " Fun="F(EXB;B£SER_13;ESP) 1(CN;;-(O;;CN;Contatto)) 2(IN;;-(F;;IN;Indirizzo))"

 :  : PRO.SER Cod="IMP.2" Tit="Implosione. " Fun="F(EXB;B£SER_13;IMP) 1(CN;;-(F;;CN;Contatto)) 2(IN;;-(O;;IN;Indirizzo))"

 :  : PRO.SER Cod="EST.3" Tit="Esplosione tipo. " Fun="F(TRE;B£SER_13;EST) 1(CN;;-(O;;CN;Contatto))"

