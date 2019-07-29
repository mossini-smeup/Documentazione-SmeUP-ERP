# OBIETTIVO
Estrarre o sostuire attributi/valori di un tag in una stringa di testo o in una stringa XML

# PREREQUISITI
C/COPY QILEGEN,£JAX_PC1

# NOTE AGGIUNTIVE

## CARATTERI SPECIALI XML E LORO TRASFORMAZIONE

_&_ = _&_amp;
' = _&_apos;
< = _&_lt;
> = _&_gt;

# PARAMETRI

## PARAMETRI DI INPUT

### Procedura
 :  : PAR
1) RxATT   :  Estrae attributi tra due caratteri
   - Il cointenuto da estrarre deve essere compreso tra due caratteri :      un carattere di aperura ed uno di chiusura. Es. (   ) oppure '   '
2) RxVAL   :  Estrae attributi tra " "
3) RxELE   :  Estrae il contenuto di un elemento richiesto
4) RxATV   :  Lista attributi/valori di un TAG
5) RxSOS   :  Sostituzione caratteri speciali
6) RxSOC   :  Estrae il valore di un attributo da una stringa XML
7) RxLATE  :  Sostituzione elementi all'interno di una stringa
7) RxSPL   :  Split di una stringa su più righe con '|'

## ANALISI PROCEDURE

### 1) RxATT
La procedura si occupa di estrarre l'attributo presente tra due caratteri, è necessario che i due caratteri siano rispettivamente un carattere di apertura ed un carattere di chiusura.

Es. :  Estrazione attributo FUN presente in una stringa

TIPFUN=P_RxATT(STRINGA : 'FUN(' : ' ')

Nell'istruzione di chiamata della RxATT è possibile indicare se la variabile (solamente nel caso fosse vuota) deve essere riempita con un valore predefinito o specificare un indicatore che si accenda nel caso il tag che si vuole estrarre non sia presente.

### 2) RxVAL
La procedura si occupa di estrarre l'attributo presente tra due doppi apici (")

Es. :  Estrazione attributo FUN presente in una stringa

TIPFUN=P_RxATT(STRINGA : 'FUN')

### 1) RxELE
La procedura si occupa di restituire il contenuto di un elemento richiesto in una stringa XML, specificando l'azione (posizionamento "POS" o scansione " ") ed il livello.

VALELE=P_RxELE('Sec' : 'POS' : 02 : AAATMP)
VALELE=P_RxELE('Sec' : '   ' : 02 : AAATMP)

### 1) RxATV
La procedura si occupa di estrarre gli attributi di una stringa ed il loro rispettivo valore. In output viene emessa una schiera con un numero di elementi pari al numero degli attributi in cui a destra viene indicato il nome dell'attributo mentre a sinistra viene indicato il suo valore.

Es. di input :  Estrazione attributo di una stringa

ESTAT=P_RxATV(STRINGA)

Es. di output :  Schiera risultante

ESTAT(1)='Id                                                       02  '
ESTAT(2)='Cont                                                  False  '

### 1) RxSOS
La procedura si occupa di estrarre sostituire e decodificare i caratteri speciali presenti in una stringa XML

Input : 
STRINGA=<Line Id="3" Op="V">

Elaborazione :  Sostituzione caratteri speciali di una stringa
STRNEW=(P_RxSOS(STRINGA))

Output : 
STRNEW=Lt;Line Id=quot;3 quot; Op= quot;V quot; gt;

Nota Bene : 
La funzione RxSOS controlla se la stringa in ingresso è già una stringa trasformata.
Esempio1 :  se in ingresso riceve "xxx_&_amp;apos;xxx" non darà in output "xxxx_&_amp;amp;apos;xxx" perchè assume che
la stringa è già stata trasformata (_&_amp;apos; equivale all'apostrofo) quindi ritornerà ancora "xxx_&_amp;apos;xxx".

Esempio2 :  se in ingresso riceve "_&_amp;xxx_&_amp;apos;xxx" darà in output "_&_amp;amp;xxx_&_amp;amp;apos;xxx" perchè assume che
la stringa non ha subito nessuno trasformazione e anche se _&_amp;apos; significa apostrofo esso verrà trasformato in _&_amp;amp;apos;
O la stringa non è da trasformare o è da trasformare del tutto

### 1) RxSOC
La procedura si occupa di estrarre il valore di un attributo presente in una stringa XML

STRINGA=<Line Id="3" Op="V">

Es. di input :  Estrazione attributo in una stringa

VALATT=(P_RxSOS(STRINGA))

Output : 

VALATT=3

### 1) RxLATE
La procedura si occupa di sostituire tutte le occorrenze di una stringa in un'altra stringa.

Es. di input

NUOVASTRI=P_RxLATE(STRINGA : VECCHIO ELEMENTO : NUOVO ELEMENTO : SOSTITUZIONE SINGOLA)

Il parametro facoltativo "SOSTITUZIONE SINGOLA", se impostato a '1' consente di sostituire solo la prima occorrenza trovata
nella stringa iniziale.


### 1) RxSPL
La procedura cerca di splittare su più righe (di intestazione di matrice) una stringa contenente spazi o punti.
Per ora è implementata la sola modalità '1', che introduce un '|' se possibile, più vicino possibile a metà stringa, privilegiando la prima riga più lunga.

Es. di input : 

STRINGA=P_RxSPL(STRINGA : '1')

Es. con STRINGA='Giacenza risultante' -> STRINGA='Giacenza|risultante'
