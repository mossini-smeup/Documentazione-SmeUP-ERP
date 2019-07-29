# FORMULE

### Definizione Generale
Esiste anche la possibilità di specificare formule per definire campi calcolati all'interno di una matrice.
Le formule possono essere specificate sia nell'Xml di definizione dei campi della matrice che in un attributo del setup di sezione.
I totali (generali e degli eventuali raggruppamenti) di colonne con formule rispetteranno la formula stessa, ignorando quindi la funzione di totalizzazione.
### Come specificare una formula nell'Xml della Matrice
Occorre definire una colonna aggiuntiva (nello stesso modo in cui viene definita una colonna "standard"), nella quale specificare un attributo "Formula" in cui dovrà essere indicata la formula desiderata.

Gli eventuali campi della tabella coinvolti nella formula devono essere specificati nel formato "[nomecampo]".
Esempio : 
'<Colonna Cod="T$MED1" Txt="Media1" Tip="" Lun="10" IO="O" Ogg="NR" Formula="[T$X01C]/[T$X01D]"/>' '<Colonna Cod="T$MED2" Txt="Media2" Tip="" Lun="10" IO="O" Ogg="NR" Formula="([T$X01C]/[T$X01D])+5*[T$MED1]"/>'
Dove T$X01C e T$X01D sono due campi della tabella.

### Come specificare una formula nel setup di una matrice
Occorre indicare nel nuovo attributo "Formulas" la/e formula/e desiderate utilizzando la seguente sintassi : 
Formulas="<DescrittoreFormula(1)>|< DescrittoreFormula(2)>|...|< DescrittoreFormula(n)>"

Dove :  DescrittoreFormula(x)="<CodiceColonna>;<TitoloColonna>;<Formula>;<Lunghezza>;[<Decimali>];[<Oggetto>]"

CodiceColonna non deve essere già presente tra i campi della matrice. Decimali è ovviamente facoltativo; nel caso di colonne alfanumeriche lasciarlo in bianco.

Esempio (analogo al precedente) : 
Formulas="T$MED1;Media1; [T$X01C]/[T$X01D];10;0;NR|T$MED2;Media2;([T$X01C]/[T$X01D])+5*[T$MED1];10;0;NR"

La risoluzione delle formule, a livello di singolo record, avviene all'atto della costruzione della tabella in memoria. Nel caso quindi di Matrici di Aggiornamento non verrà aggiornato il valore di una colonna calcolata se modificati I valori delle colonne coinvolte.
Come si vede dagli esempi, una formula può fare riferimento ad altre colonne "calcolate"
Attenzione a non specificare riferimenti circolari (es :  A=B ... B=A).
Per attivare da script i totali su di una colonna calcolata è necessario specificare almeno una funzione sulla colonna (es :  SUM(<campo>)). La formula verrà comunque ignorata e verrà eseguita la formula utilizzando i valori dei campi di totale.



