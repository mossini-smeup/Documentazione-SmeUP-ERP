Le istruzioni di tipo "D" indicano alla scheda come riempire le sezioni, cioè forniscono i dati veri e propri che verranno visualizzati nella scheda.

Concettualmente si dividono in due categorie : 
 * Chiamate a programmi esterni :  l'XML dei dati viene restituito da un programma esterno
 * Fornitori di dati interni alla scheda :  l'XML viene costruito una volta per tutte alla prima visualizzazione della scheda dal servizio della scheda stessa.

Le chiamate a programmi esterni possono essere variabili in funzione ad azioni effettuate dall'utente dopo la prima visualizzazione della scheda (ad esempio la scelta dell'elemento di un albero). Dopo ogni azione è possibile richiamare il servizio, cambiandone i parametri di ingresso.
I fornitori di dati interni, invece, creano l'XML una volta sola al momento della costruzione della scheda :  non è possibile condizionarli con variabili scelte dall'utente.

Si veda anche : 
 :  : DEC T(MB) P(DOC) K(LOCEXD_06) I(_7_Variabili                     >>)

# Chiamate a programmi esterni
## D.FUN - Funzioni Looc.up
Definisce una chiamata a un servizio secondo le modalità standard di Looc.up.

### Metodi ammessi
 * STD Standard (vedere il Set'n'Play UP SER per la costruzione)
 * Formato XML valido (qualsiasi, purchè compatibile con il tipo di subsezione come specificato nella documentazione delle subsezioni)
Si veda anche : 
- [Caratteri non validi nelle password lunghe](Sorgenti/MB/DOC/LOBASE_05)

## D.PGM - Programma
Richiama un programma che fornisce direttamente l'XML che sarà aggiunto.
Per i parametri di ingresso vedere l'help di I.INC.PGM.

# Fornitori di dati interni alla scheda
## D.SCH - Sottoscheda
Carica una sottoscheda definita nello stesso membro della scheda corrente.
Il nome della sottoscheda è nell'attributo Nam.
La chiamata alla sottoscheda avviene dando direttamente il membro della scheda corrente nell'Oggetto2 e il nome della sottoscheda in Oggetto 4 :  è percio possibile ridefinire, rispetto alla chiamata della scheda corrente, l'Oggetto 1 e il Parametro.

## D.IMG - Immagini
Presenta l'immagine dell'oggetto definito

>N.B. :  solo immagini di tipo JPG!!!

Metodi ammessi
 * OGG Dell'oggetto
 * OG2 Percorso da tabella B§D
 * ATR Di un attributo dell'oggetto

## D.LAB - Label
Presenta una scritta

Metodi ammessi
 * STD Standard (come oggetto)

Formato XML valido
 * Una riga di albero
Esempio :   < Oggetto Tipo="AR" Parametro="" Codice="A01" Testo=""/ > (senza spazio dopo il '<' e prima del '>')

## D.OGG - Oggetto
Aggiunge un oggetto a una lista di oggetti, trattabile da qualunque componente accetti elenchi di oggetti nei Dati (alberi, label, immagini...)

## D.SEM.XML - Semaforo
Visualizza un semaforo. Sono necessarie due soglie numeriche (tra rosso e giallo e tra giallo e verde) e un valore in base al quale viene accesa la luce del semaforo.

## D.GAU.XML - Cruscotto
Visualizza un cruscotto. Sono necessarie due soglie numeriche (tra rosso e giallo e tra giallo e verde), i valori di fondo scala inferiore e superiore e un valore in base al quale viene posizionata la lancetta sul cruscotto.

## D.FUN.A15 - Reportistica
Carica una sottoscheda contenente il report richiesto, deve essere inserito in una sezione di SCHEDA.
Prevede i seguenti parametri, tutti obbligatori : 
R Nome del report
E Tipo di emissione del Report

## D.HTM.URL - Pagina web
Visualizza una pagina web, di cui va specificato l'indirizzo.
