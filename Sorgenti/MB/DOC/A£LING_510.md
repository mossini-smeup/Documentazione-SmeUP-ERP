# Oggetti da generare

Al fine di un corretto utilizzo di un ambiente in lingua, i seguenti oggetti devono essere compilati in lingua : 
 * File video, se si utilizza il terminale; in caso di utilizzo di Looc.UP essi sono tradotti dinamicamente.
 * Message file.
 * Printer file.

La generazione viene effettuata (interattiva o schedulata) tramite il programma A£TR41 che viene lanciato attraverso una serie di parametri.
* Tipo Parametro :  identifica il tipo di oggetto che si vuole ricercare e poi creare. Le possibilità sono 5; Oltre ai singoli tipi (OJ*PRTF, OJ*DSPF, OJ*MSGF) c'è la possibilità di lanciarli tutti assieme, oppure di specificare una Exit. E' un campo obbligatorio.
* Lingua Traduzione :  è la lingua in cui si vuole creare l'oggetto. E' il secondo campo obbligatorio.
* LIbreria :  In casi di lancio diverso da Exit, è necessario specificare in quale libreria cercare gli oggetti da creare.
* File :  come per la libreria, se il lancio è diverso da Exit occorre specificare in quale file della libreria cercare gli oggetti da creare.
* Ambito :  è l'ambito di destinazione dell'oggetto tradotto. Al lancio del programma viene controllato che l'ambito specificato sia gestibile nel'ambiente corrente (anche in caso di Exit).
* Exit :  se specificato come tipo parametro Exit, diventa un campo necessario. I programmi di exit dell'A£TR41 sono gli stessi utilizzati in estrazione. Quindi si chiameranno A£TR01_xx dove xx sono i due caratteri da specificare nel lancio. Il programma A£TR01_X1 è un esempio. Per i dettagli sull'implementazione di questa exit riferirsi alla documentazione relativa all'estrazione. Una volta lanciato il programma scansisce la exit e per ogni serie di libreria/file/ambito, cerca il tipo oggetto corrispondente e crea il corrispondente oggetto in lingua.
* Libreria di output :  Se presente specifica la libreria in cui creare gli oggetti in lingua. Altrimenti vengono creati in librerie con nomenclatura standard chiamate SME_xxyyzz dove xx è la lingua, yy l'ambito di destinazione e zz l'eventuale suffisso. Se la libreria standard non esiste viene creata.

Il lancio del programma A£tr41 prevede la generazione automatica degli oggetti generati.






