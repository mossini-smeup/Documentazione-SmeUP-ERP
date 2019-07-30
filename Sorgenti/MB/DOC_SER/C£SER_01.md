 :  : HEA RESP(LS) STAT(00)
# OBIETTIVO

# FUNZIONI/METODI
## PAR
### VAL
Restituisce tutti i valori dei parametri di una categoria per un oggetto/coppia di oggetti.
### OGG
Restituisce tutti gli oggetti/coppie di oggetti in cui un parametro è valorizzato. Se specificato un valore in chiave 3 filtra solo gli oggetti in cui il parametro assume quel valore.
### ALL
Restituisce tutti i parametri valorizzati di una certa categoria (una riga di matrice per record).
### ORI
Restituisce tutti i parametri valorizzati di una certa categoria (una riga di matrice per oggetto/coppia di oggetti).
NB :  Ad ogni parametro è associata una colonna, parametri multipli vanno quindi nello stesso campo separati da ';'.
### TEM
Dato un parametro in una categoria ed due periodi limite, produce un report con l'evoluzione di tale parametro all'interno dei due periodi per tutti i codici della categoria.
### ATR
Restituisce tutti i codici di parametro per cui è presente almeno un record, data una categoria.

 :  : PRO.SER Cod="PAR.VAL.1" Tit="Parametri. Valori di un oggetto" Fun="F(EXB;C£SER_01;PAR.VAL) 1(TA;C£E;-(O;;TAC£E;Categoria)) 2(**;;-(O;;**;Codice 1)) 3(**;;-(O;;**;Codice 2)) 4(**;;-(F;;**;Parametro))"

 :  : PRO.SER Cod="PAR.OGG.2" Tit="Parametri. Oggetti di un parametro" Fun="F(EXB;C£SER_01;PAR.OGG) 1(TA;C£E;-(O;;TAC£E;Categoria)) 2(**;;-(O;;**;Parametro)) 3(**;;-(F;;**;Codice valore))"

 :  : PRO.SER Cod="PAR.ALL.3" Tit="Parametri. Lista completa verticale" Fun="F(EXB;C£SER_01;PAR.ALL) 1(TA;C£E;-(O;;TAC£E;Categoria))"

 :  : PRO.SER Cod="PAR.ORI.4" Tit="Parametri. Lista completa orizzontale" Fun="F(EXB;C£SER_01;PAR.ORI)" Ref="PAR.ALL.3"

 :  : PRO.SER Cod="PAR.TEM.5" Tit="Parametri. Un parametro nel tempo" Fun="F(EXB;C£SER_01;PAR.TEM) 1(TA;C£E;-(O;;TAC£E;Categoria)) 2(**;;-(O;;**;Parametro)) P( PI(-(F;;TAPER;Periodo Iniziale)) PF(-(F;;TAPER;Periodo Finale)))"

 :  : PRO.SER Cod="PAR.ATR.6" Tit="Parametri. Lista attributi attivi per una categori" Fun="F(EXB;C£SER_01;PAR.ATR)" Ref="PAR.ALL.3"

