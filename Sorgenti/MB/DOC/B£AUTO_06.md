
# Obiettivo
Permettere ad un utente abilitato di modificare il gruppo (o ruolo) a lui assegnato e/o impersonare un utente diverso. Questo permette ad esempio ad un capo di assegnare le attività di un utente assente ad un collega presente.
In Sme.up, infatti, le autorizzazioni a livello di utente si basano su due ogetti :  il codice utente (elemento di tabella B£U) ed il suo gruppo (campo della tabella utenti B£U).
E' possibile far sì che in un intervallo di date uno o entrambi questi valori vengano sostituiti, tramite l'impostazione di opportuni parametri (quindi cella categoria C£E di nome B£U)
Definiamo questa possibilità "switch utente".
-Lo switch sostutisce totalmente il valore originale :  **NON è attiva nessuna risalita**.
-La funzionalità di switch non è attiva per default :  per attivarla è necessario impostare il campo di tabella B£7.

# Effetto
Il programma che reperisce le autorizzazioni, verifica alla partenza la presenza di una riassegnazione e se esiste valida la utilizza in sostituzione. La funzione restituisce i valori utilizzati.

# Come funziona

## Switch potenziale :  chi può diventare
E' possibile impostare degli switch utente "potenziali", vale a dire utenti e gruppi che l'utente può diventare.
Sono parametri multipli variabili per data (estremi non obbligatori), intestati al singolo utente
* £01 = Utenti ammissibili
* £02 = Liste di utenti ammissibili :  (è equivalente all'impostazione, in £01, di tutti gli utenti che appartengono alla lista).
* £03 = Ruoli (o gruppi) ammissibili

## Switch effettivo :  chi diventa in un dato istante
Sono definiti i seguenti parametri, entrambi validi per data e non sovrapponibili (ad una data ne può valere uno solo), anch'essi intestati al singolo utente.
* £11 = Utente di switch
* £12 = Gruppo di switch
Essi possono essere valorizzati manualmente, oppure trascinando elementi validi alla data, rispettivamente utenti (dal parametro Utenti £01 e Lista Utenti £02, quest'ultimo sviluppato in tutti i suoi elementi) e gruppi Utenti (dal parametro £03).
>>> Spiegare, nel trascinamento, come viene valorizzata la data.

## Come lo diventa
Quando si controlla l'autorizzazione, si considerano i soli switch validi in quella data
Se presente un utente di switch, viene assunto.
Per quanto riguarda il gruppo, è attiva la seguente scaletta : 
- se presente il gruppo di switch, viene assunto
- se presente l'utente di switch, viene assunto il suo gruppo
- altrimenti viene assunto il gruppo dell'utente originale.

La seguente tabella esemplifica quanto esposto.


| 
| .COL Txt="Utente" A="L" |
| ---|----|
| 
| .COL Txt="Gruppo" LunAut="1" A="L" |
| 
| .COL Txt="Utente Switch" A="L" |
| 
| .COL Txt="Gruppo Switch" LunAut="1" A="L" |
| 
| .COL Txt="Utente Risultante" A="L" |
| 
| .COL Txt="Gruppo Risultante" LunAut="1" A="L" |
| U1 | G1 | - | - | U1 | G1 |
| U1 | G1 | U2 | - | U2 | G4 |
| U1 | G1 | - | G2 | U1 | G2 |
| U1 | G1 | U2 | G2| U2 | G2 |
| U2 | G4 |  | |U2 |G4 |
| 



## Quando lo diventa
Lo switch viene eseguito durante la gestione delle autorizzazioni.**(N.B. :  Solo se l'utente richiesto coincide con l'utente corrente).
Le autorizzazioni sono persistenti per job, per questo motivo ogni variazione si attiverà solo se la funzione richiesta non è stata ancora utilizzata nel job.
Per questo motivo bisogna scollegarsi dall'ambiente e ricollegarsi, altrimenti si potrebbero avere funzioni non congruenti alla nuova situazione.


