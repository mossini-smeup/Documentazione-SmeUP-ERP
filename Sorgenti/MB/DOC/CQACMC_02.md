# Matricole Strumenti
## Definizione
Sono definite matricole strumenti tutti i singoli apparecchi di misura presenti in azienda.
La matricola contiene i dati anagrafici dello strumento stato attuale dello strumento scadenze e storico delle tarature.
Le matricole strumenti di misura sono l'oggetto Sme.UP
 :  : DEC T(OG) P() K(MS)

![CQACMC_MS01](http://localhost:3000/immagini/CQACMC_02/CQACMC_MS01.png)
Le matricole si inseriscono/modificano attraverso le azioni raggiungibili dal menù strumenti oppure dalle funzioni dell'oggetto.
Caratterizzano una matricola le seguenti informazioni : 
![CQACMC_MS02](http://localhost:3000/immagini/CQACMC_02/CQACMC_MS02.png)
A finaco di dati prettamente anagrafici quali nome, marca matricola fornitore, certificato fornitore e relative date, dalla matricola ricaviamo Enti persone responsabili e dati relativi alla reperibilità e stato attuale dello strumento.

Categoria strumento
 :  : DEC T(OG) P() K(SM)
 definisce la famiglia di appartenenza e ne eredita i comportamenti principali

Sui singoli strumenti sono definibili delle eccezioni alle regole previste per la famiglia strumenti quali

Intervallo di controllo
 indica in gg di calendario la frequenza prevista per la taratura

Nr decimali gestiti
 utilizzato per stabilire in caso di taratura interna o di utilizzo sui piani di controllo(ciclo di collaudo) il numero di decimali con cui verranno espresse le misure

Nr Rilievi
 In caso di tatatura interna stabilisce in fase di controllo quante misure devono essere registrate per ogni caratteristica del ciclo

Procedura di controllo
 :  : DEC T(OG) P() K(DQ)
è il link alla documentazione qualità di riferimento (Istruzioni operative, procedura di riferimento)

