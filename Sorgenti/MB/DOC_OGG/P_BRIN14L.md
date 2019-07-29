# OBIETTIVO

Collegare le registrazioni contabili alle dichiarazioni d'intento.

# Funzione "Gestione assegnazione"

# DATI DI TESTATA

Una volta entrati in questa funzione, nel frontespizio leggeremo le seguenti voci : 

* **Imponibile con IVA**, è la quota d'importo fattura alla quale viene applicata l'IVA normalmente, è un campo popolato nel caso in cui esistano importi superiori al plafond residuo;
* **Senza IVA in dich**, è la quota d'importo fattura che rientra nell'esenzione mediante dichiarazione d'intento;
* **Senza IVA non in dich**, è la quota d'importo fattura che ancora non è stata associata ad una dichiarazione d'intento, quando agganceremo la fattura del fornitore alla dichiarazione d'intento questo campo verrà svuotato;
* **Altri importi esenti**, sono altre quote d'importo della fattura che sono esenti per assoggettamenti diversi da quello dedicato alle dichiarazioni d'intento (ad es. il bollo);
* **Totale imponibile**, è la quota che risulterà soggetta ad IVA.


# DATI DI DETTAGLIO

Sotto la sezione soprariportata viene descritta la dichiarazione con i propri dettagli : 

* **Inizio**, è la data più recente tra la data di emissione e la data d'inizio dell'anno oggetto di dichiarazione;
* **Fine**, è la data che determina il termine di utilizzo della dichiarazione, sia per scadenza naturale che per sospensione voluta dal dichiarante;
* **N° Protocollo**, è il numero di protocollo utilizzato;
* **Tipologia di dichiarazione**, viene indicato anche il tipo di dichiarazione ricevuta e quindi se si tratta di quella fino a raggiungimento di un importo o per singola operazione;
* **Importo Limite**, è l'importo totale del plafond;
* **Importo Utilizzo**, è la quota di plafond utilizzata;
* **Importo Residuo**, è la quota di plafond residua.




# OPZIONI DI RIGA

Sotto queste voci saranno presenti i riferimenti dei documenti che compongono la fattura o la nota di credito e nelle righe sottostanti ci saranno le dichiarazioni d'intento attive per il cliente.


Selezionando con **S** le dichiarazioni il sistema distribuirà l'importo presente nel campo "Senza IVA in dich" e andrà a popolare il campo "Senza IVA in dich" con la sommatoria degli importi di quelle righe che hanno un importo inferiore al plafond residuo e con assoggettamento dedicato all'esenzione per dichiarazione. Se esistono quote imponibili e quindi con righe che presentano l'assoggettamento imponibile, destinerà gli importi nel campo "Imponibile con IVA", mentre gli importi delle righe con assoggettamenti esenti per altri motivi (es. bollo) verranno scritti nel campo "Altri importi Esenti". In "Totale Imponibile" ci saranno gli importi effettivamente imponibili.

Questa funzione è l'unica che permette di associare o dissociare le dichiarazioni d'intento d'esenzione per singola operazione.
Lo stesso trattamento viene applicato alle note di credito.

# TASTI FUNZIONE

Nella parte alta della schermata troviamo i tasti funzioni, questi si alternano a seconda che i documenti siano collegati o meno : 

F15 :  con questa funzione il sistema assegnerà in modo autonomo i documenti alla dichiarazione d'intento, questo comando non sarà attivabile nel caso in cui vorremo gestire l'assegnazione di una nota di credito o di una dichiarazione per singola operazione. Ha la stessa funzione della S quando si hanno più dichiarazioni.

F16 :  digitando questo tasto viene annullato il collegamento tra la dichiarazione d'intento e un documento.

