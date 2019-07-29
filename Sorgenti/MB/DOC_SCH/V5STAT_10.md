# Scheda Controlli globali
La scheda esegue delle funzioni di controllo : 
## Verifiche di correttezza
Permette di verificare la correttezza delle informazioni presenti ne file delle statistiche ed in particolare : 

### Sintesi date aggiornamento
Dato un intervallo di date, mostra le date di aggiornamento delle estrazioni
![V5STAT_063](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_10/V5STAT_063.png)
### Stato aggiornamento per data/utente
Mostra la lista delle varie estrazioni con l'indicazione di data / utente
![V5STAT_064](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_10/V5STAT_064.png)
### Numeri protocollo
Dato un intervallo di date, elenca le fatture per numero di protocollo
![V5STAT_065](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_10/V5STAT_065.png)
### Registrazioni
Dato un intervallo di date, elenca le registrazioni per numero registrazione
![V5STAT_066](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_10/V5STAT_066.png)
### Fatture
Dato un intervallo di date, elenca le fatture registrate per numero fattura
![V5STAT_067](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_10/V5STAT_067.png)
### Bolle
Dato un intervallo di date, elenca le bolle fatturate in ordine di data
![V5STAT_068](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_10/V5STAT_068.png)
### Continuità numeri protocollo
Dato un intervallo di date, segnala eventuali numeri di protocollo mancanti
![V5STAT_069](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_10/V5STAT_069.png)
### Integrità Contabilizzato - Documenti mancanti
Dato un intervallo di date, segnala eventuali documenti mancanti presenti come registrazione contabile ma mancanti come documento nel gestionale
![V5STAT_070](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_10/V5STAT_070.png)
### Integrità Contabilizzato - Documenti da eliminare
Dato un intervallo di date, segnala eventuali documenti da eliminare presenti come decomento nel gestionale ma mancanti come registrazione in contabilità
![V5STAT_071](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_10/V5STAT_071.png)
### Integrità Contabilizzato - Scostamenti
Dato un intervallo di date, segnala eventuali scostamenti tra contabilità e statistiche
![V5STAT_072](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_10/V5STAT_072.png)
### Costi nulli
Dato un intervallo di date, segnala eventuali righe documento con costo del venduto = 0
![V5STAT_073](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_10/V5STAT_073.png)
### Controllo Margini
Dato un intervallo di date, calcola e presenta il margine precentuale tra fatturato e costo delle righe documento
![V5STAT_074](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_10/V5STAT_074.png)
### Consegna rispettata
Elenca tutte le righe bolla e determina la differenza tra la la data bolla e la data consegna confermata. le qtà postive rappresentano i ritardi
_3_Nota bene le qtà positive rappresentano i ritardi
![V5STAT_075](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_10/V5STAT_075.png)
### Consegna non rispettata
Come il precedente, le qtà negative rappresentano i ritardi
![V5STAT_076](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_10/V5STAT_076.png)
### Quadrature delta <> 0
Elenca le fatture per le quali esiste una differenza tra importo fattura e importo contabilizzato. Il confronto viente effettuato sugli importi merce (l'iva viene esclusa).
![V5STAT_077](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_10/V5STAT_077.png)
## Verifiche di congruenza
![V5STAT_078](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_10/V5STAT_078.png)
## Verifiche di completezza
![V5STAT_079](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_10/V5STAT_079.png)
## Verifiche per oggetto
![V5STAT_080](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_10/V5STAT_080.png)
## Verifiche per commessa
