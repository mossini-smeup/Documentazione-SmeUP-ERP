
#  Set.up Motore di schedulazione
La schedulazione consiste nell'eseguire un motore BCD di cui viene richiesto il codice (elemento della tabella B§G), all'atto del lancio.
La tabella B§G  deve essere impostata come nella figura seguente : 

![S5IRIS_03](http://localhost:3000/immagini/S5IRIS_T04/S5IRIS_03.png)
Dobbiamo copiare lo script PAR_SCP da smedev alla libreria dei sorgenti personali del cliente con eventuale ridenominazione. Nello script PAR_SCP possiamo impostare  i set.up previsti dal motore di schedulazione standard di sme.up
Lo script INT è invece lo script che esegue il loop di caricamente delle aree di memoria temporanee , lancia la schedulazione e ne salva i risultati sui file di produzione. Normalmente a meno di esigenze particolari non viene modificato.



- [Guida all&-x27;impostazione Parametri](Sorgenti/MB/DOC/S5IRIS_T32)




