## Principali comandi per la gestione del file
 * Creazione del printer file :  CRTPRTF = (Create Printer File)
 * Cambiamento parametri del printer fle :  CHGPRTF = (Change Printer File)
 * Cambiamento temporaneo dei parametri del printer file :  OVRPRTF = (Override Printer File)

## Principali istruzioni per la definizione della stampa
### Crea un BOX nella stampa
La sintassi del comando è : 
>BOX(punto di partenza verticale <blank> punto di partenza orizzontale <blank> punto di fine verticale <blank> punto di fine orizzontale <blank> spessore della linea <blank>(colore)(ombreggiatura))

I valori consentiti per le coordinate e per lo spessore della linea (dipendono dall'unità di misura definita con il comando *UOM durante la creazione del printer file; nel caso la misura indicata superi le misure valide, verrà segnalato nel file di spool) vanno da 0.0001 a 59.790 cm, ma per definire lo spessore della linea possono essere usati anche dei valori speciali : 
 * *NARROW = sottile (0.022 cm)
 * *MEDIUM = medio (0.042 cm.)
 * *WIDE   = largo (0.064 cm.)
Per definire il colore viene utilizzata l'istruzione (*COLOR <colore>), per l'ombreggiatura l'istruzione (*SHADE <intensità>) e per l'intensità possono essere usati i valori compresi tra 0 e 100 o, in alternativa, dei caratteri speciali : 
 * *XLIGHT
 * *LIGHT
 * *MEDIUM
 * *DARK
 * *XDARK

Se il comando BOX è definito a livello di record, tutti i campi del record devono essere posizionati usando il comando POSITION.
Per generare un BOX nella stampa è necessario indicare DEVTYPE(*AFPDS) nelle definizioni del printer file.
Nello stesso record in cui ho usato il comando BOX non posso usare i comandi SPACEB, SPACEA, SKIPA, SKIPB.

_ Esempio : _
R BOX1                      BOX(1.2 0.5 5.1 6.3 0.2)

R BOX2                      BOX(2 5 5.0 3.33 *WIDE)

R BOX3                      BOX(1.2 0.5 5.1 6.3 *MEDIUM (*COLOR RED) (*SHADE 50))

### Crea una LINEA della stampa
La sintassi del comando è : 
>LINE(punto di partenza verticale <blank> punto di partenza orizzontale <blank> lunghezza della linea <blank> spessore della linea <blank> direzione della linea <blank>(colore))

I valori consentiti per le coordinate e per lo spessore della linea (dipendono dall'unità di misura definita con il comando *UOM durante la creazione del printer file; nel caso la misura indicata superi le misure valide, verrà segnalato nel file di spool) vanno da 0.0001 a 59.790 cm, ma per definire lo spessore della linea possono essere usati anche dei valori speciali : 
 * *NARROW = sottile (0.022 cm)
 * *MEDIUM = medio (0.042 cm.)
 * *WIDE   = largo (0.064 cm.)
Per definire la direzione della linea si possono usare i valori *HRZ (orizzontale) e *VRT (verticale), mentre per il colore l'istruzione (*COLOR <colore>).

Se il comando LINE è definito a livello di record, tutti i campi del record devono essere posizionati usando il comando POSITION.
Per generare una LINE nella stampa deve essere indicato DEVTYPE(*AFPDS) nelle definizioni del printer file.
Nello stesso record in cui viene usato il comando LINE non possono essere usati i comandi SPACEB, SPACEA, SKIPA, SKIPB.

_Esempio_
R REC1                      LINE(1.5 3.0 4.25 *HRZ 0.2 *TOP)

R REC2                      LINE(1.5 3.0 *MEDIUM *HRZ (*COLOR RED))

### Applica il grassetto (HIGHLIGHT) ad un campo o ad un record
(se specificato a livello di record, tutti i campi del record saranno in grassetto)
Per utilizzare HIGHLIGHT nella stampa, deve essere indicato DEVTYPE(*AFPDS) nelle definizioni del printer file.
Se utilizzato contemporaneamente al comando CHRSIZ o al comando UNDERLINE, il grassetto non verrà applicato.

_Esempio : _
R RECORD1
       01                                  HIGHLIGHT
R RECORD2
  CAMPO1             3A    11 HIGHLIGHT

### Applica la sottolineatura (UNDERLINE) ad un campo o ad un record
(se specificato a livello di record, tutti i campi del record saranno sottolineati)
Se utilizzato contemporaneamente al comando CHRSIZ, il grassetto non verrà applicato.

_Esempio : _
R RECORD1
       01                                  UNDERLINE
R RECORD2
  CAMPO1             3A    11 UNDERLINE

### Varia la larghezza e l'altezza (CHRSIZ) dei caratteri di un campo o di un record
(se specificato a livello di record, la variazione sarà applicata a tutti i campi)
La sintassi del comando è : 
>CHRSIZ(larghezza altezza)

I valori validi per la larghezza e per l'altezza vanno da 1.0 a 20.0 e di default sono settati a Altezza=1 Larghezza=1.
Utilizzando CHRSIZ si raccomanda di non utilizzare FONT(*DEVD) nelle definizioni del file e, in caso contrario, i valori di default vengono settati a 10 (sia per l'altezza che per la larghezza).

_Esempio : _
R RECORD1                   CHRSIZ(3  3)
  01
R RECORD2
  CAMPO1             3A    11 CHRSIZ(2.5 2)

### Posiziona i campi di un file nella pagina (POSITION)
La sintassi del comando è : 
>POSITION(punto di partenza verticale | punto di partenza orizzontale)

I valori consentiti per le coordinate (dipendono dall'unità di misura definita con il comando *UOM durante la creazione del printer file; nel caso la misura indicata superi le misure valide verrà, segnalato nel file di spool) vanno da 0.0001 a 59.790 cm.
Se il comando POSITION è utilizzato per definire la posizione dei un campo, tutti i campi di quel record devono utilizzare il comando POSITION per il posizionamento.
Per utilizzare tale comando in stampa, deve essere indicato DEVTYPE(*AFPDS) nelle definizioni del printer file e, nel medesimo record in cui è stato utilizzato il comando LINE, non si può ricorrere ai comandi SPACEB, SPACEA, SKIPA, SKIPB.

_Esempio : _
R RECORD1
                                   CAMPO1          6S 2       POSITION(2.0 1.983)

### Inserimento righe (SPACEB; SPACEA)
Questo comando specifica il numeri di righe 'di spaziatura' che verranno inserite prima (SPACEB) o dopo (SPACEA) la stampa della riga successiva.

La sintassi del comando è : 
>SPACEB/A (numero di righe)

Il valore consentito per il numero di righe deve essere compreso tra 0 e 255.
Se il comando viene specificato a livello di record, gli spazi tra le righe verranno applicati ad ogni riga associata al record stesso; il comando deve essere specificato solo una volta a livello di record o una volta per ogni livello di campo e non sarà valido nel caso nei campi sia stato specificato il numero di linea di posizionamento (posizioni dalla 39 alla 41).

>N.B. :  Non definendo il numero di linea o il comando SPACEA/B, i campi e i record verranno sovrascritti.
Il comando non è valido nè a livello di record nè a livello di campo se a livello di record sono stati utilizzati i comandi BOX, ENDPAGE, GDF, LINE, OVERLAY, PAGSEG o POSITION.

_Esempio : _
R RECORD1                   SPACEA(1)
                                   FIELDA       132         1
R RECORD2                   SPACEB(2)
                                   FIELDA       132         1

## Salta a (SKIPB; SKIPA)
Questo comando definisce a quale specifico numero successivo (SKIPA) o precedente (SKIPB) di riga dovrà saltare la stampante dopo aver stampato una riga.

La sintassi del comando è : 
>SKIPB/A(numero di righe)

Il valore consentito per il numero di righe deve essere compreso tra 0 e 255 e, nel caso esso venga specificato a livello di record, gli spazi tra le righe verranno applicati ad ogni riga associata al     record stesso; inoltre, il comando deve essere specificato solo una volta a livello di record o una volta per ogni livello di campo e non sarà valido se nei campi è stato specificato il numero di linea di posizionamento (posizioni dalla 39 alla 41).

>N.B. :  Non definendo il numero di linea o il comando SKIPA/B, i campi e i record verranno sovrascritti.
Il comando non è valido nè a livello di record nè a livello di campo se a livello di record sono stati utilizzati i comandi BOX, ENDPAGE, GDF, LINE, OVERLAY, PAGSEG o POSITION.

_Esempio : _
R RECORD1                   SKIPA(10)
R RECORD2                   SKIPB(8)

### Barcode
### CPI (Characters Per Inch)
Questo comando viene utilizzato per specificare la densità orizzontale della stampa (se inserito nelle definizioni iniziali) dei record o dei singoli campi e, in particolare per : 
 * inserire maggior volume di dati in una stampa;
 * dare alla stampa la 'forma' desiderata.

La sintassi del comando è : 
>CPI (numero di caratteri per inch)

_Esempio : _
R RECORD1
                                    CPI(15)

###   LPI (Lines Per Inch)
Questo comando viene utilizzato per definire il numero di righe per pollice (e quindi definire l'altezza della riga).

La sintassi del comando è : 
>LPI(numero di righe)

I valori consentiti per il numero di righe sono :  4, 6, 8, 10, 12.

_Esempio : _
R RECORD1           LPI(6)

### Inserimento data (DATE)
Questo comando viene utilizzato per inserire nella stampa la data corrente o la data di sistema in formato 6 o 8 caratteri.

La sintassi del comando è : 
>DATE(*JOB o *SYS<blank>*Y o *YY)

L'attributo  *JOB viene utilizzato per stampare la data del JOB in corso, SYS per stampare la data di sistema (se non specificato nessun attributo, viene impostato *JOB), *Y per indicare il formato dell'anno con 2 cifre, mentre*YY per indicare il formato dell'anno con 4 cifre (se non specificato nesun attributo, viene utilizzato di default *Y).

_Esempio : _
R REC01
                              CAMPO1                            DATE
                              CAMPO2                            DATE(*JOB *Y)

### Stampa fronte-retro (DUPLEX)
Questo comando viene utilizzato per indicare se la stampa sarà in formato foglio singolo o fronte-retro.

La sintassi del comando é : 
>DUPLEX(valore | valore) : 

I valori consentiti nel comando DUPLEX sono : 
 * *NO = stampa solo su u lato del foglio
 * *YES = stampa fronte-retro ideale per impaginazione laterale
 * *TUMBLE = stampa fronte-retro ideale per impaginazione dall'alto

Per utilizzare il comando per l'uscita di stampa deve essere indicato DEVTYPE(*AFPDS) nelle definizioni del printer file.

_ Esempio : _
R RECORD1                      DUPLEX(*YES)

### Cambio Font
Questo comando viene utilizzato per associare un determinato tipo di font a un campo del record.

La sintassi del comando è : 
>FONT(identificativo del font <blank> (*POINTSIZE altezza del font ))

L'identicativo del font può essere un identificativo numerico (Es. :  222= Gothic 15) o un nome di font grafico (CZN20L= Times New Roman).
Il parametro *POINTSIZE è utilizzato solo per i font proporzionali per definire uno specifico font relativo ad una grandezza.

_Esempio : _
R RECORD1
                           FONT(222)
CAMPO1
         FONT(ADMMVSS)

### Inserimento Overlay
Questo comando viene utilizzato per inserire un overlay nella stampa.

La sintassi del comando è : 
>OVERLAY(indirizzo del file di overlay | punto di partenza verticale | punto di partenza orizzontale)

Per utilizzare il comando OVERLAY nella stampa, deve essere indicato DEVTYPE(*AFPDS) nelle definizioni del printer file.
Se il comando OVERLAY è definito a livello di record, tutti i campi del record devono essere posizionati mediante il comando POSITION.
Nello stesso record in cui è stato utilizzato il comando OVERLAY non possono essere usati i comandi SPACEB, SPACEA, SKIPA, SKIPB.

_ Esempio : _
R RECORD1                      OVERLAY(MYLIB/OVL04 1.234 14.62)

### Inserimento immagine o segmento di pagina (PAGSEG)
Questo comando viene utilizzato per inserire un'immagine o un segmento di un'altra pagina nella stampa.

La sintassi de comando è : 
>PAGSEG(indirizzo del file immagine <blank> punto di partenza verticale <blank> punto di partenza orizzontale (*SIZE larghezza     <blank>altezza ) (*ROTATION ))

I valori consentiti per la definizione dei punti di partenza (verticale e orizzontale), della larghezza e dell'altezza sono compresi 0 a 57,79 e quelli relativi alla rotazione tra 0, 90, 180, 270.
Per utilizzare il comando PAGSEG nella stampa, deve essere indicato DEVTYPE(*AFPDS) nelle definizioni del printer file.
Se il comando PAGSEG è definito a livello di record, tutti i campi del record devono essere posizionati usando il comando POSITION.
Esso può essere utilizzato più volte a livello di record, anche se **non può essere usato più di 10 volte per ogni pagina di stampa.
Nello stesso record in cui ho usato il comando OVERLAY non posso usare i comandi SPACEB, SPACEA, SKIPA, SKIPB.

_Esempio : _
R RECORD1                    PAGSEG(MYLIB/PAGSEG5 3.527 4.162)
R RECORD2                    PAGSEG(MYSEG 0.0 3.759)
     PAGSEG(YOURSEG 0.0 5.233)

### Rotazione di pagina (PAGRTT)
Questo comando viene utilizzato per definire il grado di rotazione del testo rispetto alla pagina caricata nella stampante (stampa orizzontale o verticale).

La sintassi del comando è : 
>PAGRTT(valore)

Gli unici parametri validi per il comando sono 0, 90, 180, 270.
I comandi PAGRTT, SKIP e SPACE sono utilizzati con il seguente ordine di esecuzione : 
 - SKIPB
 - SPACEB
 - PAGRTT
 - SPACEA
 - SKIPA
Il comando PAGRTT rimane effettivo per tutte le pagine successive a quella in cui è definito.
Quando una pagina viene ruotata, le dimensioni di larghezza e di altezza vengono invertite (nel caso non possano essere invertite, viene segnalato con un messaggio di errore)

_Esempio : _
R RECORD1                PAGRTT(270)

### Rotazione di testo (TXTRTT)
Questo comando viene utilizzato per definire il grado di rotazione del testo in una campo di record.

La sintassi del comando è : 
>TXTRTT(grado di rotazione)

I valori consentiti per il grado di rotazione sono :  0, 90, 180, 270.
Per utilizzare il comando TXTRTT nella stampa, deve essere indicato DEVTYPE(*AFPDS) nelle definizioni del printer file.
Non è possibile utilizzare il comando TXTRTT in combinazione con il comando CHRSIZ.

_Esempio : _
R RECORD1
 CAMPO1        10     35 15TXTRTT(90)
