## Obiettivo
Permettere di analizzare tutte le proprietà di una applicazione (o di un modulo) evidenziandone rilevanza, obbligatorietà ecc. al fine di indicare ciò che manca e determinarne un livello di completamento.
## Struttura matrice
![A£LABS_000](http://localhost:3000/immagini/A£LABS_06/AXLABS_000.png)
## A FRONTE DI UN CONTESTO APPLICAZIONE/MODULO, SONO FORNITE INFORMAZIONI (COLONNE) RELATIVE A : 
* descrizione
* obbligatorietà :  (Si :  ratio=1  No :  ratio=2)
* coefficiente
* peso :  coefficiente x ratio (default 1)
* quota :  valorizzato se presente attributo
* progressivo peso
* progressivo quota
* progressivo rating
* gruppo (Laboratorio/Formazione/Documentazione)

Inoltre sono stati aggiunti nella sezione "Con Indici" anche  : 
* Indice
* Progressivo Indice

## I VALORI (RIGHE) A SEGUIRE, CONCORRONO AL CALCOLO DEL RATING : 
* codice :  applicazioni/moduli
* descrizione
* responsabile
* esplorazione :  programma di navigazione del modulo
* schemi standard
* funzioni applicazione :  programma che espone le funzioni del modulo
* associazione oggeti
* presenza Scheda
* presenza Menù
* presenza Glossario
* presenza Faq
* presenza Presentazioni
* cruscotto
* documento Sviluppo
* training
* visione
* Corsi
* Video
## N.B. : qualora un attributo definito obbligatorio, non sia valorizzato, la cella viene rappresentata di colore rosso.

## Calcolo del rating
Qualora il valore sia obbligatorio e sia presente, il peso assume un valore doppio :  peso=coefficiente * ratio, (dove ratio=2).
Il calcolo del rating è determinato dal rapporto tra la sommatoria delle quote di ogni singola proprietà del Applicazione/modulo e la sommatoria dei rispettivi pesi.
Il Cruscotto rappresenta in modalità grafica il valore del rating complessivo.

## Calcolo Indice
A differenza del Rating che è un valore percentuale, l'Indice tenta di classificare i moduli e le applicazioni in base ad un valore assoluto.
Per il calcolo dell'indice concorrono sia le quote assegnate alle singole proprietà che gli script a cui fanno riferimento (se esistono).
Il progressivo dell'indice è calcolato sommando il valore maggiore tra quota e indice di ogni singola proprietà

## Sintesi applicazioni
A differenza del rating dell'applicazione che calcola i valori delle proprietà dell'applicazione, la sintesi applicazioni calcola i valori del rating e dell'indice come insieme dei moduli che la compongono

