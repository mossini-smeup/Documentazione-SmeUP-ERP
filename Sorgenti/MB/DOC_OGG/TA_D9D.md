# D9D - Modelli di valori
 :  : DEC T(ST) K(D9D)
## OBIETTIVO
Consente di aggiungere delle formule per calcolare nuovi valori. Permette inoltre di specificare il formato e, in caso, cambiare nome al valore origine da portare in Databeacon.
È controllata dal programma specifico B£TD9D
## STRUTTURA DEGLI ELEMENTI
Il primo carattere contiene il modello da associare alla fonte nell'elemento della tabella D9B.
- >X        È la base che determina il modello. In questo elemento definisco il nome dell'asse dei valori e il formato standard dei valori, dove non specificato.
- >X.000     Per modificare nome e formato di un valore origine passato dal programma. Il numero di tre cifre che segue il punto deve corrispondere al numero di ordine del valore.
- >X.AAABB   Se segue al punto una stringa che inizia con un carattere, contiene un valore calcolato
## ESEMPIO DI COSTRUZIONE DI GERARCHIA
- A               Valori Non Conformi     BASE DEL MODELLO.
- A.C01           Costo Medio NC          FORMULA DI CALCOLO.
- A.PERCCTR       Perc. Controllata    FORMULA DI CALCOLO.
- A.001           Quant. Lotto            MODIFICA VALORE ORIGINE.
- A.004           Qtà prova              MODIFICA VALORE ORIGINE.
- A.007           Costo NC                MODIFICA VALORE ORIGINE.
- A.CONTART       Contatore Articoli      FORMULA DI CONTATORE.
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC Descrizione
Contiene la descrizione dell'elemento della gerarchia di valori per Cube_up. Corrisponde al nome che vedrò nel Databeacon
 :  : FLD T$D9DA **Tipo Espressione**
Permette di tipizzare il valore. Sono gestiti i seguenti casi : 
- ' '     Standard, valore originale o formula di valori con espressione indicata.
- 'M'     Calcola la media sul valore originale.
- 'A'     Calcola il minimo valore su valore originale.
- 'Z'     Calcola il massimo valore su valore originale.
- 'C'     Contatore della categoria specificata nel campo espressione o di tutte le righe lasciato bianco. Il contatore può essere applicato solamente a categorie che non hanno al di sotto altre categorie.
- 'F'     Permette di posizionare una formula alla posizione indicata nell'espressione.
- 'O'     Permette di aggiungere un valore ricavato dall'OAV numerico di un oggetto della gerarchia. Ad esempio :  se il programma estrae le righe documento, posso agganciare un OAV della riga documento che mi ritorna un valore, ed utilizzarlo come un qualsiasi valore del cubo.
Quale OAV e a quale oggetto collegarlo, lo scrivo nel campo Espressione, che mi guida se imputo il "!".
 :  : FLD T$D9DB **Espressione**
Può variare a seconda del campo tipo espressione. Contiene la sintassi delle formule di valori. Si può costruire una formula matematica ()-+*/. Per usare i valori origine si mette la codifica "&001" con il numero con 3 cifre che rappresenta il numero d'ordine del valore origine. Per inserire  valori calcolati  o valori origine modificati si scrive pari pari l'elemento della D9D in questione.
Le costanti usate con i decimali vanno usate con il separatore decimale "."
_9_Es. di A.PERCCTR.
(&002 / A.001) * 100.
_9_Es. di A.FATTEURO.
(&010 / 1936.27).
_7_Nota particolare :  se il campo fosse troppo stretto per contenere tutta l'espressione, si può utilizzare la seguente tecnica. Compilare il campo con la stringa speciale &NOTA& e gestire l'espressione estesa nella nota di tabella.
 Il contenitore standard è il B£E, verificare che sia presente l'elemento.
 :  : FLD T$D9DC **Formato maschera**
In base alla scelta da tabella D9B/V1 si decide come deve essere formattato il valore nel Databeacon :  si può decidere se visualizzare la valuta, il simbolo percentuale, ecc..
 :  : FLD T$D9DD **Formato numerico**
In base alla scelta da tabella D9B/V2, si decide come deve essere visualizzato il formato numerico del valore nel Databeacon :  si può decidere come separare le migliaia, i decimali ecc..
Dalla versione Databeacon 5.3 in avanti, si può utilizzare la costruzione del formato valori. Basta compilare questo campo con un elemento che non abbia radice "N" della tabella D9*V2, e preoccuparsi che nel parametro di questa tabella sia indicata la sintassi del formato di output.
- _9_Ad es. EUR-.--0,00  costituisce un formato tipo Euro 100.200,25
- _9_Ad es. ---0,00000   costituisce un formato tipo 100000,00022
- _9_Ad es. 0.00%        costituisce un formati tipo 12,23 %
 :  : FLD T$D9DE **Non Visualizzare**
Permette se compilato di non visualizzare nel Databeacon il valore specificato nell'elemento della tabella, ma è possibile utilizzarlo per il calcolo di formule e per la visualizzazione del dettaglio record.
 :  : FLD T$D9DF **Numero Max decimali**
Da compilare solo sulla base del modello valori. Permette di specificare il numero massimo di decimali significativi. Il default è 2.
Se ne servissero di più, mettere il numero di decimali e preoccuparsi nel formato numerico del singolo valore, in modo che vengano visualizzati i decimali.
