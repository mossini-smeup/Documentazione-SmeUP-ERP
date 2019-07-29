# Generalità
La foto permette di fissare una situazione istantanea della giacenza ad una data, la giacenza salvata può essere valorizzata anche con regole dipendenti dall'area/tipo giacenza.
Sono possibili varie modalità di creazione della foto : 

| 
| .COL Txt="Cod." A="L" |
| ---|----|
| 
| .COL Txt="Funzione" A="L" |
| 
| .COL Txt="Azione eseguita" LunAut="1" A="L" |
| - A | Dalla fine all'indietro| Parte dalla giacenza attuale e ricostruisce, elaborando i movimenti a ritroso, la giacenza alla data. |
| - B | Dall'inizio in avanti| Parte da zero e ricostruisce la giacenza alla data elaborando in avanti tutti i movimenti dall'inizio fino alla data. |
| - C | A partire da una foto| Chiede la foto e data di partenza e calcola la nuova foto applicando i movimenti. |
| - D | Differenza tra due foto| Chiede 2 foto e data di partenza e calcola la nuova foto come differenza tra le altre due. |
| - E | Differenza tra foto e giacenza| Chiede la foto e data di partenza e calcola la nuova foto come differenza tra la foto e la giacenza corrente. |
| - F | Differenza tra giacenza e foto| Come la precedente invertendo i fattori. |
| - G | Direttamente da giacenza| Congela direttamente la giacenza. |
| - H | Differenza tra foto e LIFO| Chiede la foto e data di partenza ed Esercizio, Scenario e Magazzino fiscale e calcola la nuova foto come differenza tra la foto e magazzino fiscale. |
| - I | Copia del LIFO| Congela una copia del magazzino fiscale. |
| - L | Cancellazione foto| Cancella la foto in input |
| 


# Archivio utilizzato
 :  : DEC T(OJ) P(*FILE) K(GMFOTO0F)

# Tabelle necessarie
 :  : DEC T(ST) K(GMW)
 :  : DEC T(ST) K(GMY)

_2_ATTENZIONE
Per garantire la congruenza dei dati è opportuno costruire la foto in un momento in cui non vengono registrati movimenti di magazzino.
