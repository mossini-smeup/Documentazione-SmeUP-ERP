# OBIETTIVO
Ritornare i percorsi di accesso alle immagini degli oggetti a secondo della loro natura.
In particolare l'oggetto può essere : 
* Standard   (Immagine non modificabile)
* Personale  (Viene proposta un'immagine che può essere modificata creandone una copia in una
              struttura di risalita a livelli)

# DETERMINAZIONE DELLA NATURA DELL'IMMAGINE
Attraverso l'api K04 è possibile ritornare le informazioni sulla natura dell'immagine dell'oggetto
ed in particolare : 
* Presenza di una immagine per istanza
* Immagine Standard
* Tipo di estensione
* Classe di riferimento

## CLASSE DI RIFERIMENTO
Alcuni oggetti vengono ridefiniti verso una classe comune di riferimento, ad oggi gli oggetti che
possiedono una classe di riferimento sono i seguenti : 

 :  : PAR
Oggetto|Classe di riferimento
AZ|CNAZI
CL|CNCLI
FO|CNFOR
AM|AR
PG|OJ*PGM
UT|OJ*USRPRF
UP|TAB£U
TA*CNTT|OG


## IMMAGINE CON ISTANZA
Tutte le immagini sono definite per classe, fanno eccezione questi oggetti : 
* TAB£AMO
* TAB£A
* ST
* DI
* OJ*USRPRF
* UT
* TAB£U
* UP
* OG
* SE
* AR
* CN
* VO

## IMMAGINI STANDARD
Gli oggetti definiti standard sono i seguenti : 
* V2
* V3
* TAB£A
* TAB£AMO

## TIPO DI ESTENSIONE
L'unica estensione ammessa è il formato PNG.

# RICERCA IMMAGINE A LIVELLI
Le immagini non definte standard saranno ricercate in una risalita a tre livelli.
Questi livelli sono dei percoirsi definiti nelle seguenti variabili : 
* IMG.003 - 1 livello di ricerca
* IMG.002 - 2 livello di ricerca
* IMG.001 - 3 livello di ricerca
* IMG.STD - 4 livello di ricerca (Immagine standard)

Per ognuno di questi livelli l'immagine sarà ricercata risalendo la struttura stessa dell'oggetto.
* Se presente l'istanza
** <Tipo>\<Parametro>\<Istanza>.PNG
* Se presente il parametro
** OG\<Tipo>\<Parametro>.PNG
* Altrimenti
** OG\OG\<Tipo>.PNG

Se l'oggetto standard inizia con il carattere X, la ricerca verrà estesa a tutti i livelli

# FUNZIONI/METODI

