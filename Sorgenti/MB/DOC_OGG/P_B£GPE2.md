# Generalità
Questa è la funzione che determina i parametri delle elaborazioni batch (es. stampe documenti, lancio flussi esecuzione, elaborazione MRP, ecc..).
I parametri possono essere stabiliti a priori, attraverso un apposito formato di guida, oppure possono essere modificati (per gli utenti autorizzati) al momento del lancio attraverso il comando funzione F11 eventuialmente presente.

# Formato guida
![B£_08_01](http://localhost:3000/immagini/MBDOC_OGG-P_B£GPE2/BX_08_01.png)
# Formato impostazione parametri
![B£_08_01A](http://localhost:3000/immagini/MBDOC_OGG-P_B£GPE2/BX_08_01A.png)
Se autorizzati si può scegliere se lanciare l'elaborazione in interattivo o batch.

Si possono impostare anche gli altri parametri di esecuzione tra i quali : 

- la coda lavori
- la coda di stampa
- la schedulazione (data/ora di elaborazione)


# Impostazioni generali
Oltre alle impostazioni sulla singola elaborazione si possono definire delle impostazioni generali che il programma utilizza ogni volta che viene eseguito, tra le impostazioni generali ci sono anche le autorizzazioni alla modifica concesse agli utenti.

# Scelta
In questo formato si inseriscono il programma da eseguire e l'utente che lo immette, che devono essere oggetti presenti nel sistema.
L'inserimento di '**' identifica l'utente o il programma generico.

Nel formato di dettaglio si inseriscono i parametri di esecuzione e le autorizzazioni alla modifica : 
accanto ai campi da inserire vengono proposti i valori assunti dai livelli superiori, secondo
l'ordine seguente : 


| 
| .COL Txt="Livello" LunAut="1" A="L" |
| ---|----|
| 
| .COL Txt="Utente" LunAut="1" A="L" |
| 
| .COL Txt="Programma" LunAut="1" A="L" |
|  1 | Utente | Programma |
|  2 | ** | Programma |
|  3 | Utente | ** |
|  4 | ** | ** |
| 


Se il parametro esecuzione è " " va a livello superiore. Se rimane comunque " " prende il valore della *JOBD.

_2_Autorizzazione : 
 :  : PAR (L(PUN)
- " " Va al livello superiore
- "S" Autorizzato
- "N" Non Autorizzato

Se rimane comunque  " " si assume "S".

Si definiscono i seguenti campi : 

| 
| .COL Txt="Nome campo" |
| ---|----|
| 
| .COL Txt="Valori" |
| 
| .COL Txt="Significato=" LunAut="1" A="L" |
|  ESECUZIONE INTERATTIVA | S - N - blank | Stabilisce se l'utente può eseguire il programma in modo interattivo |
| 

_1_I seguenti campi sono significativi se il programma viene eseguito in coda lavori.

| 
| .COL Txt="Nome campo" |
| ---|----|
| 
| .COL Txt="Valori" |
| 
| .COL Txt="Significato=" LunAut="1" A="L" |
|  CODA LAVORI AUTORIZZAZ. | S - N - blank | Stabilisce se l'utente può modificare la coda lavori in cui verrà eseguito il programma |
|  CODA LAVORI | Oggetto di sistema | Determina il nome della coda lavori in cui verrà eseguito il programma |
|  PRIORITA' CODA LAVORI AUTORIZZAZ. | S - N - blank | Stabilisce se l'utente può modificare la priorità con cui verrà inserito in coda lavori il programma |
|  PRIORITA' CODA LAVORI | Da 1 a 9 | Determina la priorità con cui verrà inserito in coda lavori il programma |
|  LAVORO CONGELATO | S - N - blank | Stabilisce se il lavoro verrà inserito in coda lavori come congelato |
| 

_1_I seguenti campi sono significativi se il programma ha uscite in stampa :  i parametri di esecuzione vengono suddivisi tra quelli relativi alle stampe a 132 ed a 198 caratteri.

| 
| .COL Txt="Nome campo" |
| ---|----|
| 
| .COL Txt="Valori" |
| 
| .COL Txt="Significato=" LunAut="1" A="L" |
| CODA STAMPA AUTORIZZAZ. | S - N - blank | Stabilisce se l'utente può modificare la coda stampa in cui scriverà il programma. |
| CODA STAMPA | Oggetto di sistema | Determina il nome della coda lavori in cui scriverà il programma |
| PRIORITA' CODA STAMPA AUTORIZZAZ. | S - N - blank | Stabilisce se l'utente può modificare la priorità con cui verrà inserita in coda la stampa del programma |
| PRIORITA' CODA STAMPA | Da 1 a 9 | Determina la priorità con cui verrà inserita in coda la stampa del programma |
| STAMPA CONGELATA | S - N - blank | Stabilisce se la stampa verrà inserito in coda come  congelata |
| STAMPA IMMEDIATA | S - N - blank | Stabilisce se la stampa verrà eseguita in modo immediato,  senza passare dalla coda. |
| SALVATAGGIO STAMPA | S - N - blank | Stabilisce se la stampa verra' inserita in coda come salvata |
| NUMERO COPIE | da 1 a 99 | Determina il numero di copie da stampare. Se spazio viene assunto 1. |
| TIPO MODULO | 10 caratteri liberi | Determina il nome del modulo di stampa. |
| 

