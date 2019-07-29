# GESTIONE PARAMETRI ESECUZIONE
Con questa funzione, presente nel menù di funzioni applicative si definiscono i parametri di esecuzione dei programmi e le autorizzazioni alla modifica concesse agli utenti.
# SCELTA
In questo formato si inseriscono il programma da eseguire e l'utente che lo immette, che devono essere oggetti presenti nel sistema.
L'inserimento di '**' identifica l'utente o il programma generico.
Nel secondo formato si inseriscono i parametri di esecuzione e le autorizzazioni alla modifica :  accanto ai campi da inserire vengono proposti i valori assunti dai livelli superiori, secondo l'ordine seguente : 
Livello   1)  Utente  / Programma
"      2)  **      / Programma
"      3)  Utente  / **
"      4)  **      / **
Se il parametro esecuzione è " " va a livello superiore.
Se rimane comunque " " prende il valore della *JOBD.
Autorizzazione :      " " Va al livello superiore
"S" Autorizzato
"N" Non Autorizzato
Se rimane comunque  " " si assume "S".
Si definiscono i seguenti campi : 
Nome campo                Valori        Significato
----------                ------        -----------
ESECUZIONE INTERATTIVA   "S" "N" " "    Stabilisce se l'utente può eseguire il programma in modo
interattivo
***********************************
I seguenti campi sono sognificativi se il programma viene eseguito in in coda lavori.
***********************************
CODA LAVORI AUTORIZZAZ.  "S" "N" " "    Stabilisce se l'utente può modificare la
coda lavori in cui verrà eseguito il programma
CODA LAVORI              Oggetto di     Determina il nome della coda sistema lavori in cui verrà eseguito il programma
PRIORITA' CODA LAVORI    "S" "N" " "    Stabilisce se l'utente può
AUTORIZZAZ.                             modificare la priorità con cui verrà inserito in coda lavori
il programma
PRIORITA' CODA LAVORI    Da 1 a 9       Determina la priorità con cui verrà inserito in coda
lavori                                       il programma
LAVORO CONGELATO         "S" "N" " "    Stabilisce se il lavoro verrà inserito in coda lavori come
congelato
*******************************
I seguenti campi sono
significativi se il programma
ha uscite in stampa : 
i parametri di
esecuzione vengono suddivisi
tra quelli relativi alle stampe a 132 ed a 198 caratteri.
*******************************
CODA STAMPA AUTORIZZAZ.  "S" "N" " "    Stabilisce se l'utente può modificare la coda stampa in
cui scriverà il programma.
CODA STAMPA              Oggetto di     Determina il nome della coda sistema lavori in cui scriverà
il programma
PRIORITA' CODA STAMPA    "S" "N" " "    Stabilisce se l'utente può
AUTORIZZAZ.                             modificare la priorità con cui verrà inserita in coda la stampa del programma
PRIORITA' CODA STAMPA    Da 1 a 9       Determina la priorità con cui verrà inserita in coda la stampa del programma
STAMPA CONGELATA         "S" "N" " "    Stabilisce se la stampa verrà inserito in coda come congelata
STAMPA IMMEDIATA         "S" "N" " "    Stabilisce se la stampa verrà eseguita in modo immediato,
senza passare dalla coda.
SALVATAGGIO STAMPA       "S" "N" " "    Stabilisce se la stampa verra' inserita in coda come salvata
NUMERO COPIE             da 1 a 99      Determina il numero di copie da stampare. Se spazio viene
assunto 1.
TIPO MODULO              10 caratteri   Determina il nome del modulo liberi di stampa.
