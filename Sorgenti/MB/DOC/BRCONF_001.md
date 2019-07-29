# Configurazione
Serve per descrivere adeguatamente un prodotto, quando questo può essere fornito in diverse varianti, senza dover essere costretti a moltiplicare le distinte e i cicli.

La configurazione può essere vista sotto due aspetti : 
 * _2_la descrizione del prodotto, che ne specifica le caratteristiche e le qualità
 * _2_la costruzione del prodotto, che definisce il ciclo e la distinta necessari alla realizzazione del prodotto

## Descrizione del prodotto
In anagrafico articoli dovrà essere indicato il _2_"Criterio di configurazione", che è un elemento della tabella BRC a cui si rimanda per una descrizione più approfondita.
 :  : DEC T(ST) K(BRC)
In base alle impostazioni della tabella BRC viene stabilito : 
 * il tipo di configurazione adottato (orizzontale / verticale),
 * nel caso di configurazione orizzontale il metodo di formattazione del codice configurazione,
 * se il codice configurazione è obbligatorio in anagrafico articoli (esiste una configurazione preferenziale) oppure solo nei documenti,
 * il questionario da utilizzare quando deve essere definita una nuova configurazione

## Costruzione del prodotto
### Gestione distinta
Nella determinazione della distinta di produzione un legame è configurato quando, a seconda del valore della configurazione, può essere valido o non valido, può assumere un codice articolo diverso, può cambiare il coefficiente di impiego, può essere una combinazione delle precedenti.

Il legame diventa configurato quando c'è un valore nel campo _2_"Criterio di configurazione", che è un elemento della tabella BRS a cui si rimanda per una descrizione più approfondita.
 :  : DEC T(ST) K(BRS)
Nella tabella BRS viene stabilito : 
 * il programma da utilizzare come criterio di selezione; (**Nota**; in BRSRC c'è una serie di programmi BRSCOxxx utilizzabili quali criteri di configurazione oppure come esempio per lo sviluppo di programmi utente per implementare logiche particolari)
 * il parametro di controllo del programma di cui sopra

### Gestione ciclo
Ha un trattamento del tutto analiogo a quello spiegato per la distinta.

## Memorizzazione delle configurazioni
Le configurazioni possono essere memorizzate nel file C£VARI0F
 :  : DEC T(OJ) P(*FILE) K(C£VARI0F)
La memorizzazione è controllata dalla tabella C£B a cui si rimanda per una trattazione più approfondita
 :  : DEC T(ST) K(C£B)
l'opportuno elemento della C£B deve essere richiamato nel modello di configurazione (tabella BRC).

# Esempio
Abbiamo un prodotto che può essere venduto in diverse colorazioni, vogliamo anche stabilire quali siano le colorazioni in modo che in fase di gestione ordine di vendita si possa scegliere una delle colorazioni predefinite.
La diistinta tecnica è unica, costituita dall'articolo da verniciare e dalle diverse vernici che saranno selezionate automaticamente in funzione della colorazione scelta.

- Prima di tutto dobbiamo definire un elemento della tabella C£B che guidi la memorizzazione delle configurazioni nell'archivio C£VARI0F : 

![BRCONF_01](http://localhost:3000/immagini/BRCONF_001/BRCONF_01.png)
- Quindi deve essere definito il modello di configurazione che sarà inserito in anagrafico del  prodotto. Il modello di configurazione è un elemento della tabella BRC : 

![BRCONF_02](http://localhost:3000/immagini/BRCONF_001/BRCONF_02.png)
- Adesso si crea l'articolo in anagrafico articoli associando il modello di configurazione nel campo "Criterio di configurazione" : 

![BRCONF_03](http://localhost:3000/immagini/BRCONF_001/BRCONF_03.png)
- Per l'articolo inserito si definiscono le varie colorazioni ammesse, dalla manutenzione anagrafica si seleziona il campo a destra del criterio di configurazione e si compila la tabella che si presenta : 

![BRCONF_04](http://localhost:3000/immagini/BRCONF_001/BRCONF_04.png)
- Per la gestione della distinta configurata si deve prima creare un elemento della tabella BRS con programma  e parametro da utilizzare come criterio di configurazione : 

![BRCONF_05](http://localhost:3000/immagini/BRCONF_001/BRCONF_05.png)
- Si crea la distinta associando ad ogni legame relativo alle vernici il criterio di configurazione : 

![BRCONF_06](http://localhost:3000/immagini/BRCONF_001/BRCONF_06.png)![BRCONF_07](http://localhost:3000/immagini/BRCONF_001/BRCONF_07.png)
- Selezionando il campo a destra del criterio di configurazione si apre un formato di impostazione delle regole di validità : 

![BRCONF_08](http://localhost:3000/immagini/BRCONF_001/BRCONF_08.png)
- L'interrogazione distinta di produzione darà risultati diversi a seconda della configurazione in input : 

![BRCONF_09](http://localhost:3000/immagini/BRCONF_001/BRCONF_09.png)![BRCONF_10](http://localhost:3000/immagini/BRCONF_001/BRCONF_10.png)![BRCONF_11](http://localhost:3000/immagini/BRCONF_001/BRCONF_11.png)