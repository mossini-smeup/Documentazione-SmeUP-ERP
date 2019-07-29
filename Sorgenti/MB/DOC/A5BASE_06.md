# VERIFICHE E AZIONI PRELIMINARI

## COMPLETAMENTO TABELLE
### TABELLE COMUNI DI BASE
* TABELLA PER
Creare gli elementi della tabella PER con sottosettore azienda tramite l'utility PE8 con funzione MAN e metodo CRE

 * TABELLA B£4
Creare gli elementi della tabella B£4
 * TABELLA B£Y
Verificare presenza gruppo flag A5*
 :  : DEC T(ST) K(B£Y)

### TABELLE DI BASE

* A51
Impostare la tabella : 
 :  : DEC T(ST) K(A51)

* CATEGORIE FISCALI
Impostare la tabella : 
 :  : DEC T(ST) K(A5A)

* CAUSALI CESPITI
Riprendere la tabella : 
 :  : DEC T(ST) K(A5B)

* LINEE DI AMMORTAMENTO
Impostare la tabella : 
 :  : DEC T(ST) K(A5C)

* CAUSALI DI COLLEGAMENTO CON CONTABILITA'
Impostare la tabella con le causali utilizzate nelle registrazioni contabili (elementi della C5V) : 
 :  : DEC T(ST) K(A5F)

* CAUSALI COLLEGATE
Riprendere la tabella : 
 :  : DEC T(ST) K(A5G)

* INIZIALIZZAZIONI A5
Riprendere la tabella : 
 :  : DEC T(ST) K(A5W)


## COMPLETAMENTO DATI GENERALI

### DATI AZIENDALI

Controllare parametri specifici azienda impostando dati per stampa libro cespiti

### DATE/PERIODI CHIUSURE/ESERCIZI
Verifica impostazione date consolidamento per ogni azienda e linea

### NUMERATORI E PROGRESSIVI CONTABILI
Verifica e impostazione numeratori anagrafica cespiti e movimenti cespiti

### PIANO DEI CONTI e BILANCI
Verificare che sui conti relativi a immobilizzazioni sia impostato il campo 'Rilevanza cespiti'


### ATTIVAZIONE COLLEGAMENTO CESPITI DA CONTABILITA'

Impostare il campo 'Coll. autom. cespiti' della tabella C51.
In particolare, il codice 1 effettuerà un collegamento differito (la gestione dei cespiti verrà lanciata in un momento diverso rispetto all'immissione della registrazione contabile), il codice 2 effettuerà un collegamento interrattivo (alla chiusura della registrazione contabile verrà immediatamente mostrata l'immissione cespiti).

Per fare in modo che il sistema determini in automatico la categoria fiscale di un nuovo cespite a partire dal conto su cui è stato registrato l'acquisto  impostare i parametri £A6.




