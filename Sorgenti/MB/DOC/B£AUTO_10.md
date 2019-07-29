# Autorizzazioni a Livello Campo
Per controllare che un utente possa vedere o modificare il contenuto di un campo si utilizza la classe PLC-xxxxxx, dove xxxxxx è il nome del file (es. BRARTI) a cui si vogliono applicare le autorizzazioni.

L'autorizzazione a livello campo deve essere attivata in tabella B£2 (campo ££B£2P - Attivazione PROTEZIONE a Livello campo).

Per la gestione vengono utilizzati 10 indicatori (da 01 a 10) con il seguente significato : 
 * 01 Visualizza  Gruppo 1
 * 02 Modifica  Gruppo 1
 * 03 Visualizza Gruppo 2
 * 04 Modifica  Gruppo 2
 * 05 Visualizza Gruppo 3
 * 06 Modifica  Gruppo 3
 * 07 Visualizza Gruppo 4
 * 08 Modifica  Gruppo 4
 * 09 Visualizza Gruppo 5
 * 10 Modifica  Gruppo 5

I programmi di visualizzazione (es. V5DO5$CV) possono associare questi indicatori a gruppi di campi, quindi si possono creare fino a 5 gruppi a cui associare 2 indicatori :  il primo che governa la visualizzazione ed il successivo che governa la modifica ad esempio nel programma di cui sopra il campo W$VAL1  appartiene al gruppo 1 quindi l'indicatore 01 ne controlla la visualizzazione e l'indicatore 02 la possibilità di modifica.
