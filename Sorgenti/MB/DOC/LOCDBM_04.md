# Esportazione
In questo capitolo illustreremo come scrivere dati letti da una matrice o un file S01 in un DB generico.

## Esportazione in un file S01
Dalla versione V3R1 di LoocuUp è stata aggiunta la possibilità di salvare l'XML che descrive una matrice in un file S01.
Un file S01 è un formato proprietario di Loocup, di fatto, si tratta di un file in formato l'XML.
L'XML è un formato testuale, scritto secondo determinati standard.

Per gestire questo formato, è stato creato l'oggetto apposito di tipo J7, parametro S01.
Il codice è il path.
Questo primo passo, consente ad esempio di condividere le informazioni con altri utenti, senza che si debbano collegare allo stesso AS400.

E' inoltre possibile separare la parte di lettura dei dati dal loro successivo trattamento.

## Esportazione di un file S01
Una volta esportati i dati della matrice in un file S01, è possibile elaborarlo con il servizio JA_00_39.
Questo servizio nasce per completare le funzionalità del servizio JA_00_19 e per facilitarne l'utilizzo :  tutte le elaborazioni vengono svolte sull'oggetto 1 e questo è sempre un file.

L'esportazione di un file S01 è possibile tramite il servizio JA_00_39, metodo XML.DBE.


## Esportazione di una matrice.
Il servizio JA_00_19, con il metodo EXP.JDB, estende le funzionalità del servizio JA_00_39, metodo XML.DBE :  l'origine dei dati può essere
 - un file S01 definito nell'oggetto 1 o nel parametro DBMFILE.
 - un XML di una matrice inserito nel campo di input.
 - una Fun che restituisca un XML di matrice, fornita nel campo di input.


## Definizione della destinazione
La scrittura della tabella di destinazione avviene utilizzando la tecnologia JDBC.
Questa tecnologia consente di agganciarsi praticamente a qualunque database.

Il servizio JA_00_39, facilita l'utilizzo :  è stato infatti predisposto l'accesso ai database più comuni.
E' sufficiente indicare l'indirizzo IP della macchina su cui risiede il DB, il catalogo, l'utente, la password e il nome della tabella in cui scrivere.

Nel caso in cui si desideri scrivere in un database non incluso in quell'elenco, è necessario procurarsi il driver (un file .jar da posizionare nella cartella di installazione di LoocUp, cartella libs, sottocartella JDBC), e la stringa di connessione.
In questo caso andrà utilizzato il servizio JA_00_39, metodo EXP.JDB.
Questo servizio estende le funzionalità ma per contro è più complesso da utilizzare.

## Le schede e i menù contestuali
Data una qualunque matrice, tramite la voce Visualizza come, Scheda file dati, si accede ad una scheda orientata all'utilizzo dei dati letti.
In questa scheda potro', ad esempio, salvare in formato Excel, file S01 oppure salvare su AS400 in un file o scrivere in un DB.

Altre schede di esempio e di training sono legate al modulo LOCDBM.

