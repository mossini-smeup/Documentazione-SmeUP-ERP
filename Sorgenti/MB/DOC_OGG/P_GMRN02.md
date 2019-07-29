# Generalità
La funzione, dato un oggetto di partenza, permette di interrogare
 * tutti i movimenti
 * i movimenti dei componenti (discesa)
 * i movimenti dei prodotti (salita)

# Formato di lancio
![GMRN02_01](http://localhost:3000/immagini/MBDOC_OGG-P_GMRN02/GMRN02_01.png)Sono possibili le seguenti azioni : 
 * _2_Movimenti del lotto, presenta i movimenti dell'ogggetto selezionato
 * _2_Discesa, presenta i movimenti dei componenti dell'ogggetto selezionato
 * _2_Salita, presenta i movimenti dei prodotti dell'ogggetto selezionato

L'oggetto di selezione può essere : 
 * _2_un articolo/lotto,  se il lotto è blank si possono far presentare tutti i lotti dell'articolo
 * _2_un ordine di produzione
 * _2_una riga di un documento del ciclo esterno
 * _2_un lotto di fornitura, è il lotto esterno del fornitore (bisogna anche indicare il codice fornitore)
 * _2_un lotto di derivazione, è il lotto a cui il fornitore fa riferimento (es. la colata utilizzata dal fornitore nella produzione dell'articolo consegnato), anche in questo caso si deve indicare il codice fornitore

# Interrogazione movimenti
Premendo il bottone di "presentazione rintraccibilità" viene mostrata la matrice seguente : 
![GMRN02_04](http://localhost:3000/immagini/MBDOC_OGG-P_GMRN02/GMRN02_04.png)
# Navigazione tracciabilità
Il taso destro sul  lotto attiva un pop-up da cui selezionando _3_Atre funzioni>_3_Tracciabilità, si può navigare nelle varie azioni possibili : 
![GMRN02_03](http://localhost:3000/immagini/MBDOC_OGG-P_GMRN02/GMRN02_03.png)
## Casi particolari
_2_Discesa sintetica, dato un lotto di partenza presenta i movimenti in uscita del lotto, i movimenti degli altri lotti collegati (dei componenti) la rimanenza (differenza tra entrate e uscite) del lotto di partenza
_2_Salita sintetica, dato un lotto di partenza presenta i movimenti in entrata del lotto, i movimenti degli altri lotti collegati (dei prodotti) la rimanenza (differenza tra entrate e uscite) del lotto di partenza
