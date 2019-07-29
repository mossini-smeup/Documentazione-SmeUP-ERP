# LA PAGINAZIONE

### La Paginazione

E' possibile inserire una suddivisione in pagine della matrice, una funzione  molto utile soprattutto se la matrice contiene svariate righe.
Per poter utilizzare questa funzionalità nella creazione di una matrice è necessario utilizzare il tag 'Codice="*NEXT" ' nella £JaxCp quando vogliamo che venga effettuato il salto pagina (quindi dopo aver deciso il numero di record che vorremmo caricare per ogni singola pagina), ed associare questa funzione ad oggetto di J1 e ad un parametro di tipo *KEY .
Esempio : £JAXCP='<Oggetto Tipo="J1" Parametro="KEY" 'Codice="*NEXT" Testo="SEGUE...."  />'
E' anche possibile inserire una funzionalità della matrice che mi consenta di caricare tutti i record della matrice contemporaneamente, per ottenere questo risultato è necessario utilizzare la /copy J03 N.B. :  Le istruzione per qualsiasi tasto relativo alla paginazione devono essere inserite all'interno un PopUp.

Nel sorgente LOSERMAT è possibile vedere un esempio di utilizzo applicativo delle istruzioni



