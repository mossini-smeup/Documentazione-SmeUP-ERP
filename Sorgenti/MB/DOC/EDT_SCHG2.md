# G.SUB Sottosezione

Definiscono il componente da utilizzare per la rappresentazione dei dati di una sezione.
In base alla forma richiesta vengono eseguiti controlli di compatibilità per i dati immessi.
La forma DYN è speciale perchè indica che ove possibile la forma grafica deriva dal tipo
di dati ricevuti. In tal modo in una stessa subsezione potrò inserire alberi, matrici, ecc.

## Parametri

Questa istruzione non può esistere senza aver specificato il tipo di subsezione, ma tutte le
tipologie presentano dei parametri in comune.

## Tit - Intestazione

Nome della subsezione. Può anche contenere il valore *NONE nel caso non voglia visualizzare
l'etichetta della subsezione.

Obbligatorio = SI
Default = Nullo

## Id  - Identificativo

Questa campo serve per identificare la subsezione nel caso sia stato utilizzato il codice *NONE
per la subsezione, o nel caso voglia utilizzare la stessa intestazione per più subsezioni.

Obbligatorio = NO
Default = Intestazione

## Aut - Codice di Protezione

Tramite questo parametro è possibile indicare un livello di autorizzazione necessario ad un utente
per poter visualizzare la subsezione.

Obbligatorio = NO
Default = Intestazione

## UserSetup - Abilita Setup Utente

IN SVILUPPO

## SetupName - SetupName

IN SVILUPPO

## Focus - Forza il fuoco
![03COMEXD03](http://localhost:3000/immagini/EDT_SCHG2/03COMEXD03.png)La sua funzione e' quella di fare in modo che alla subsezione venga dato il fuoco alla sua apertura. Il campo e' presente per qualsiasi componente (quindi lo vedo anche nel G.SUB.TRE ad esempio). Se do il fuoco a piu' subsezioni di una stessa sezione mi viene considerato l'ultimo messo nello script (quindi quello più in basso) Nella G : SUB.SCH non ha senso, le SUB.SCH non hanno la proprieta' di tenere il fuoco

# G.SET.xxx - Setup

Definiscono le caratteristiche grafiche tipiche del componente, è infatti presente un
istruzione specifica per quasi ogni componente. Esistono inoltre due istruzioni di setup
applicabili ad ogni componente : 

## G.SET.DFT Setup di Default

Questo setup oltre a poter essere applicato alle subsezioni di componenti che non hanno un setup
specifico, può risultare valido per qualsiasi tipologia di subsezione, visto che include tutte
le opzioni comuni ai vari setup.

### Load :  Caricamento

Definisce il momento di caricamento della subsezione. I valori definiti per questo parametro : 

.I              Immediato
.D              Differito

Obbligatorio = NO
Default = I

### Refresh :  Refresh

Si ha la possibilità, dopo aver scelto un limite di tempo a proprio piacimento, di ricaricare i
dati della subsezione facendo riapparire la sezione aggiornata.

Obbligatorio = NO
Default = Nullo

### Name :  Nome

Imposta un nome per il setup. L'utilizzo di questo parametro mi permette di definire più
setup contemporaneamente, in questo caso nel piede della subsezione sara presente una
bottoniera tramite la quale poter selezionare il setup che si vuole utilizzare fra quelli
definiti. Questo parametro diventa perciò obbligatorio con requisito di univocità in
caso di presenza di più setup.

Obbligatorio = NO
Default = Nullo

### Parent :  Riprendi da

Utilizzando questo parametro non è più necessario specificare altri parametri, in quanto
tramite esso è possibile indicare il setup da riprendere fra quelli predefiniti a standard.

Obbligatorio = NO
Default = Nullo

## G.SET.PGM Programma

Questo setup permette di rendere dinamica qualsiasi tipologia di setup in funzione del valore
di una o più variabili della scheda.

Rispetto al precedente sono presenti i seguenti parametri : 

### Pgm :  Programma

Indica il nome del programma che ritorna il setup.

Obbligatorio = SI
Default = Nullo

### Fun/Met :  Funzione/Metodo

Indicano la funzione/metodo con cui il programma viene richiamato.

Obbligatorio = NO
Default = Nullo

### Ent :  Entry

Indica se il programma gestisce ulteriori parametri oltre la funzione/metodo.

Obbligatorio = NO
Default =NO

### Par :  Parametri

Specifica i parametri da passare al programma. I valori possibili sono stringe alfanumeriche.

Obbligatorio = NO
Default =NO

## Sezioni/Setup specifici per componente

- [G.SUB.SEZ Scheda Oggetto](Sorgenti/MB/DOC/EDT_SCHG2A)
- [G.SUB.IMG Immagine](Sorgenti/MB/DOC/EDT_SCHG2O)
- [G.SUB.IML Lista immagini](Sorgenti/MB/DOC/EDT_SCHG2F)
- [G.SUB.TRE Albero](Sorgenti/MB/DOC/EDT_SCHG2C)
- [G.SUB.TRA Tab albero](Sorgenti/MB/DOC/EDT_SCHG2B)
- [G.SUB.HTM HTML](Sorgenti/MB/DOC/EDT_SCHG2N)
- [G.SUB.PDF PDF](Sorgenti/MB/DOC/EDT_SCHG2H)
- [G.SUB.MAT Matrice](Sorgenti/MB/DOC/EDT_SCHG2G)
- [G.SUB.SEM Semaforo](Sorgenti/MB/DOC/EDT_SCHG2I)
- [G.SUB.GAU Cruscotto](Sorgenti/MB/DOC/EDT_SCHG2L)
- [G.SUB.GRA Grafico](Sorgenti/MB/DOC/EDT_SCHG2D)
- [G.SUB.BTN Bottoneria](Sorgenti/MB/DOC/EDT_SCHG2M)
- [G.SUB.LAB Label](Sorgenti/MB/DOC/EDT_SCHG2E)
