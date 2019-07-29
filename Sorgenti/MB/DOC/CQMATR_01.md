# Scopo
In base alla matrice interfunzionale delle responsabilità che discrimina per ciascuna delle attività coinvolte nella qualità, il "grado" della responsabilità (se diretta, indiretta o nessuna), il programma  controlla la modalità di accesso ai diversi moduli :  al settore dei controlli e collaudi deve essere assicurata la piena capacità di accesso (interrogazione, modifica, stampa) del modulo relativo ai collaudi e rilievi; deve altresì essere limitata al livello di consultazione, l'accesso al modulo delle verifiche ispettive interne di competenza della Direzione Generale ed Assicurazione Qualità, ecc...
Il programma deve implementare un sistema che faccia da gestore delle responsabilità circa le attività attinenti alla Qualità.


# Definizioni
 * _2_Matrice delle Responsabilità
È utile rendere evidente quali sono le Direzioni Aziendali che concorrono alla responsabilità per ogni attività attinente alla Qualità. In particolare si deve distinguere tra le Direzioni che hanno responsabilità diretta nell'esecuzione delle varie attività da quelle che semplicemente collaborano, o che non hanno alcun tipo di rapporto :  viene in questo modo a definirsi una Matrice Interfunzionale delle Responsabilità.

![CQ_MATR_01](http://localhost:3000/immagini/CQMATR_01/CQ_MATR_01.png)
# Tabelle utilizzate dal modulo : 
### B£P - CLASSI DI AUTORIZZAZIONE
Codifica le classi di autorizzazione, esempi di classe sono :  Liste di Distribuzione, Gestione Lotti, Cicli di collaudo, Strumenti di misura, ecc...
 :  : DEC T(ST) K(B£P)

### B£S - SIGNIFICATI PER CLASSE DI PROTEZIONE
È caratterizzata da una serie di sottosettori richiamati tramite la tabella B£P.
 :  : DEC T(ST) K(B£S)

Ogni sottosettore contiene fino a dieci chiavi che descrivono le righe della matrice.
 * Le colonne rappresentano gli 'n' codici che possono essere inseriti nel sottosettore della  tabella B£S
 * Le righe rappresentano i dieci codici che definiscono le possibilità di scelta per ogni specifica classe di autorizzazione. L' esempio è relativo al sottosettore B£S*DO per la  protezione delle attività di approvazione-rilascio della documentazione


|  | EMISSIONE | APPROVAZIONE | RILASCIO |
| ---|----|----|----|
| CODICE01 | SÌ | SÌ | SÌ |
| CODICE02 | NO | NO | NO |
| CODICE03  | | | |
| CODICE04  | | | |
| CODICE05  | | | |
| CODICE06  | | | |
| CODICE07  | | | |
| CODICE08  | | | |
| CODICE09  | | | |
| CODICE10  | | | |
| 


### Tutte le altre tabelle richiamate in B£P

# Processo di avviamento ed utilizzo
## Attività iniziale
 * Inserimento tabelle relative al modulo
 * Classificazione Classe di autorizzazione
 * Classificazione Funzione della classe di autorizzazione
 * Inserimento  profili generali
 * Inserimento singoli utenti

## Attività periodica
### Manutenzione autorizzazioni
![CQ_MATR_02](http://localhost:3000/immagini/CQMATR_01/CQ_MATR_02.png)
La gestione delle classi di autorizzazione si articola su tre livelli : 
 * _2_Utente, è un campo che identifica con il codice definito nello skill l'utente su cui viene immessa, gestita, ecc.. una specifica classe di autorizzazione. Inserendo il codice ** là autorizzazione viene definita per un profilo utente generico.
 * _2_Funzione, è un campo tabellato che dipende dal tipo di classe selezionata, ad esempio se scegliamo come classe quella dei documenti le possibili funzioni sono le procedure, i cataloghi, i disegni, ecc..
 * _2_Classe, è un campo tabellato B£P che identifica la classe di autorizzazione, esempi di classe sono :  Liste di Distribuzione, Gestione Lotti, Cicli di collaudo, Strumenti di misura, ecc...

Con questi tre campi e le tabelle coinvolte viene data la possibilità di creare la matrice delle responsabilità
![CQ_MATR_03](http://localhost:3000/immagini/CQMATR_01/CQ_MATR_03.png)
In questo esempio nella gestione della documentazione è stata tolta all'utente GC la possibilità di inserire, modificare, copiare o cancellare documenti del tipo "SME".
![CQ_MATR_04](http://localhost:3000/immagini/CQMATR_01/CQ_MATR_04.png)
