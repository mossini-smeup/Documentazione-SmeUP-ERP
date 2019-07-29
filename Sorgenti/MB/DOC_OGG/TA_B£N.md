# B£N - Parametri variabili
 :  : DEC T(ST) K(B£N)
## OBIETTIVO
Permettere di catalogare tutti i valori a significato variabile che possono essere associati ad una o più entità.
Il parametro potrà essere : 
-    Alfanumerico
.    Libero
.    Codificato come entità nel DATABASE
-    Numerico
## UTILIZZO
Un gruppo di valori può essere associato ad un tipo di oggetto definito nella tabella C£E.
Esempi
_1_1   Associazione dei fornitori a cui è assegnato un componente di acquisto.
-    L'entità a cui si associa l'informazione è un l'articolo di acquisto.
-    L'oggetto associato è un fornitore e sono ammesse più righe (quindi più fornitori) per un articolo
-    Il valore rappresenta la quota di assegnazione.
_1_2   Temperatura minima di una macchina per lavorare un articolo.
-    L'informazione viene associata alla coppia articolo/macchina
-    Non esiste alcun oggetto associato.
-    Il valore rappresenta la temperatura
## SOTTOSETTORI
I sottosettori permettono di suddividere i gruppi di parametri.
## CONTENUTO DEI CAMPI
 :  : FLD T$B£NA **Gestione oggetto**
Indica il tipo di controllo per il campo.
-    Bianco    = il campo non viene presentato
-    F         = presentato ma accetta anche il valore bianco
-    O         = obbligatorio
 :  : FLD T$B£NB **Caratteristiche oggetto**
Permette di definire caratteristiche specifiche quando si presenta. Abbiamo : 
-    M         = Sono ammessi più oggetti del tipo sotto definito.
 :  : FLD T$B£NC **Tipo oggetto**
-    Indica se l'oggetto deve essere controllato come oggetto presente sul sistema : 
--    Articoli
--    Attrezzature
--    Modalità di pagamento
--    Altra tabella a piacere
-    Il valore ** indica che è ammesso un valore di opzione non controllato. Si userà tale valore per indicare un'opzione libera.
 :  : FLD T$B£ND **Parametro tipo oggetto**
Alcuni tipi di oggetto permettono l'indicazione di un sottotipo.
Questo è in particolare il caso della tabella.
Si possono utilizzare le parole chiave *1 e *2 per usare come parametro variabile il codice 1 o il codice 2. Ad esempio per gestire il parametro dell'oggetto UB, se il plant è variabile ed è indicato sul codice 1, si può imputare *1.
 :  : FLD T$B£NE **Gestione valore**
Indica il tipo di controllo per il campo.
-    Bianco    = il campo non viene presentato
-    F         = presentato ma accetta anche il valore bianco
-    O         = obbligatorio
 :  : FLD T$B£NF **Caratteristiche valore**
Permette di definire caratteristiche specifiche quando si presenta. Abbiamo : 
-    C         = In presenza di valori multipli controlla che la somma dei valori abbia come risultato 100.
 :  : FLD T$B£NG **Trattamento valore**
Previsto per l'utilizzo da parte dei programmi che trattano il valore. Indica se il valore è una percentuale, un moltiplicatore, un valore assoluto, un valore per giorno o altro ancora.
 :  : FLD T$B£NH **Limite iniziale**
Permette di vincolare il valore immesso. Se, ad esempio, tale valore è una percentuale, definiremo limiti fra 1 e 100.
 :  : FLD T$B£NI.T$B£NH **Limite finale**
 :  : FLD T$B£NL **Condizione di Selezione**
Campo libero. Permette di specificare una condizione di selezione per il singolo parametro che viene confrontata con i limiti definiti nella tab. C£E  : 
- Limiti di selezione iniziale e finale
 :  : FLD T$B£NO **Sequenza ordinamento**
Campo libero. Permette di specificare una sequenza di ordinamento dei parametri, diversa da quella definita attraverso il codice del parametro. I programmi di gestione dei paramentri presenteranno a video i parametri ordinati, secondo l'ordine derivante dalla concatenazione della sequenza con il codice del parametro. Se questo campo ha valore blanks verrà ovviamente utilizzato l'ordinamento definito dal codice del parametro.
 :  : FLD T$B£NP **Livello di protezione**
Dipende da come è impostata la categoria parametri : 
* se è attiva la protezione per stati allora al livello di protezione possiamo assegnare un valore variabile fra 01 e 99, definito nella tabella degli stati.
Se il valore è presente, il programma di presentazione dei parametri, verificherà l'autorizzazione assegnata all'utente nella classe "STATI", e nella funzione "PA";
* se è attiva le protezione PLC, allora le autorizzazioni sono controllate dalla classe "PLC-C£CONR" e dalla funzione = elemento della C£E, il livello di protezione deve essere un valore compreso tra 01 e 05 (corrispondente al gruppo autorizzazione).
 :  : FLD T$B£NQ **Risalita**
Indica se per il parametro richiesto la funzione che restituisce il valore deve risalire al codice "**", quando al parametro non è assegnato un valore.
Questa risalita, se impostata, ha la precedenza su quella definita nella categoria parametri.
La ricerca nei parametri viene effettuata secondo questi passi : 
__Tipo risalita 1__
 Codice 1       Codice 2
 **           Codice 2
__Tipo risalita 2__
 Codice 1       Codice 2
 Codice 1         **
__Tipo risalita A__
 Codice 1       Codice 2
 **           Codice 2
 Codice 1         **
 **             **
__Tipo risalita B__
 Codice 1       Codice 2
 Codice 1         **
 **           Codice 2
 **             **
 :  : FLD T$B£NK **Suffisso controllo parametro**
Se specificato, attiva la gestione di controlli specifici esterni sul singolo parametro, chiamando il programma C£CR01D_x, dove x è il suffisso specificato.
La gestione controllo esterno, è fornita in : 
-    Parametri per oggetto, singolo, multiplo e per data
-    Parametri impliciti, attraverso la funzione £G28 richiamata nei vari punti specifici.
Per la documentazione sui campi gestiti e modalità, riferirsi al sorgente C£CR01D_x, fornito come prototipo/esempio di controllo esterno.
 :  : FLD T$B£NW **Attributo Visualizzazione**
Permette di assegnare un attributo di visualizzazione particolare a ogni singolo Parametro.
Viene utilizzato solo se definito in tabella C£E (CATEGORIA PARAMETRI) la modalità " Visualizzazione estesa ".
