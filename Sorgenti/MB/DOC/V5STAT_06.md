# Programma exit utente

## Programma V5STA05_U
Il programma di EXIT utente è **V5STA05_U**.

Un prototipo di questo programma si trova V5SRC/SMEDEV : 
V5STA05_U      RPGLE_ES       STAT  Esempio exit aggiustamento

Il programma di EXIT viene richiamato dal programma V5STA05 in vari momenti, riceve il record statistico V5STATR e lo modifica prima della scrittura.

Riceve in entrata una "Funzione" tra le seguenti : 

- _2_PRE,  utilizzata prima della cancellazione e creazione della statistica.
- _2_AGG, aggiornamento valori.
- _2_POST, richiamabile alla fine dell'elaborazione della statistica.



### Funzione PRE

La funzione PRE può essere richiamata con i seguenti metodi : 
 * **DO** :   Chiamato dopo aver riempito i soli campi legati alla testata (a inizio documento)
 ** Il record V5TDOC NON è valorizzato.
 ** Il record V5RDOC NON è valorizzato.
 ** Il record V5STAT è valorizzato solo per alcuni campi (D6TIPC, D6TPRO, D6NPRO, D6TDOC, D6NDOC, D6PROG, valorizzati secondo il contesto).

 * **FT** :   Chiamato dopo aver riempito i soli campi legati alla testata (a inizio documento)
 ** Il record V5TDOC NON è valorizzato.
 ** Il record V5RDOC NON è valorizzato.
 ** Il record V5STAT è valorizzato solo per alcuni campi (D6TIPC, D6TPRO, D6NPRO, D6TDOC, D6NDOC, D6PROG, valorizzati secondo il contesto).

 * **E4** :   Chiamato dopo aver riempito i soli campi legati alla testata (a inizio documento)
 ** Il record V5TDOC NON è valorizzato.
 ** Il record V5RDOC NON è valorizzato.
 ** Il record V5STAT è valorizzato solo per alcuni campi (D6TIPC, D6TPRO, D6NPRO, D6TDOC, D6NDOC, D6PROG, valorizzati secondo il contesto).

Da D6TIPC (=Tipo Statistica) del record V5STAT, è sempre possibile determinare il tipo di statistica elaborata e condizionare eventualmente le azioni dell'EXIT.
Se il tipo oggetto in elaborazione è DO (metodo=DO), i riferimenti sono in D6TDOC/D6NDOC. Se il tipo oggetto in elaborazione è FT (metodo=FT), i riferimenti sono in D6TPRO/D6NPRO. Se il tipo oggetto in elaborazione è E4 (metodo=E4), i riferimenti sono in D6PROG.


### Funzione AGG
La funziona AGG può essere richiamata con i seguenti metodi : 
 * **TES** :   Chiamato dopo aver riempito i soli campi legati alla testata (a inizio documento)
 ** Il record V5TDOC è valorizzato.
 ** Il record V5RDOC NON è valorizzato.
 ** Il record V5STAT è valorizzato con i campi di testata.

 * **RIG** :   Chiamato appena prima di scrivere un record riga
 ** Il record V5TDOC è valorizzato.
 ** Il record V5RDOC è valorizzato.
 ** Il record V5STAT è valorizzato con tutti i campi in attesa di scrittura.

 * **SPE** :   Chiamato appena prima di scrivere un record spesa/sconto (a fine documento)
 ** Il record V5TDOC è valorizzato.
 ** Il record V5RDOC NON è valorizzato.
 ** Il record V5STAT è valorizzato con tutti i campi in attesa di scrittura.

 * **REG** :   Chiamato dopo aver riempito i soli campi legati alla testata (a partire da Reg.E4)
 ** Il record V5TDOC NON è valorizzato.
 ** Il record V5RDOC NON è valorizzato.
 ** Il record V5STAT è valorizzato con i campi di testata della Registrazione.

 * **CON** :   Chiamato appena prima di scrivere un record da Reg.'E4' o da 'C5Y'
 ** Il record V5TDOC NON è valorizzato.
 ** Il record V5RDOC NON è valorizzato.
 ** Il record V5STAT è valorizzato con tutti i campi in attesa di scrittura.

 * **QUA** :   Chiamato appena prima di scrivere un record di Quadratura Contabile '**'
 ** Il record V5TDOC NON è valorizzato.
 ** Il record V5RDOC NON è valorizzato.
 ** Il record V5STAT è valorizzato con tutti i campi in attesa di scrittura.


### Funzione POST
La funzione POST può essere richiamata con i seguenti metodi : 
 * **DO** :   Chiamato dopo aver riempito i soli campi legati alla testata (a inizio documento)
 ** Il record V5TDOC NON è valorizzato.
 ** Il record V5RDOC NON è valorizzato.
 ** Il record V5STAT è valorizzato con i campi della testata del documento elaborato.

 * **FT** :   Chiamato dopo aver riempito i soli campi legati alla testata (a inizio documento)
 ** Il record V5TDOC NON è valorizzato.
 ** Il record V5RDOC NON è valorizzato.
 ** Il record V5STAT è valorizzato con i campi della testata del documento elaborato.

 * **E4** :   Chiamato dopo aver riempito i soli campi legati alla testata (a inizio documento)
 ** Il record V5TDOC NON è valorizzato.
 ** Il record V5RDOC NON è valorizzato.
 ** Il record V5STAT è valorizzato con i campi della testata del documento elaborato.

NB. Nel caso dell'elaborazione di un oggetto di tipo FT, che fa riferimento a più documenti collegati, il record V5STAT fa riferimento all'ultima testata elaborata.


Il programma di EXIT può essere utilizzato inoltre per gestire particolari esclusioni dalla statistica. Valorizzando il tipo statistica con "ER" (D6TIPC='ER'), il record non verrà scritto in statistica. Se questo avviene con il metodo "TES", viene escluso dalla statistica tutto il documento  (utile ad esempio se si vogliono escludere tutte le fatture di un cliente).
