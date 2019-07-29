# B£P - Classi Autorizzazione
 :  : DEC T(ST) K(B£P)
## OBIETTIVO
Descrivere le classi di autorizzazione utilizzate nei programmi di controllo e le relazioni con utente/funzione
## CONTENUTO DEI CAMPI
 :  : FLD T$CAAR  **Classe di riferimento**
Permette di recuperare da tale classe le caratteristiche non definite relativamente ai significati e agli oggetti associati alla classe.
 :  : FLD T$SIPR   **Tabella significati**
Permette di definire il sottosettore della B£S dove saranno definiti i significati e le opzioni ammesse per ogni riga.
 :  : FLD T$S,01   **Riga 01**
Significato e valori ammessi per la riga n
 :  : FLD T$S,02   **Riga 02**
 :  : FLD T$S,03   **Riga 03**
 :  : FLD T$S,04   **Riga 04**
 :  : FLD T$S,05   **Riga 05**
 :  : FLD T$S,06   **Riga 06**
 :  : FLD T$S,07   **Riga 07**
 :  : FLD T$S,08   **Riga 08**
 :  : FLD T$S,09   **Riga 09**
 :  : FLD T$S,10   **Riga 10**
 :  : FLD T$KYC1   **Tipo/Param. Utente**
Un oggetto che definisce il chi. Si assume e di fatto normalmente è un utente. Si consiglia TA B£U.
 :  : FLD T$PAR1   **Parametro Utente**
 :  : FLD T$KYC2   **Tipo/Param. Funzione**
Un oggetto che definisce il cosa. Potrò ad esempio indicare un programma o un servizio o una scheda se vorrò poter diversificare le autorizzaioni per uno di questi oggetti.
 :  : FLD T$PAR2   **Parametro funzione**
 :  : FLD T$B£PT   **Sbs gruppo autorizzazione**
Obsoleto. Era utilizzato nelle autorizzazioni per oggetto come modo per definire il gruppo. Ora tali autorizzazioni assumono che il gruppo sia coincidente con l'oggetto 2.
 :  : FLD T$B£PA   **Exit Determinazione**
Se impostato un valore x, durante il reperimento delle autorizzazioni, verrà lanciato il programma B£AUA4_x il quale sostituirà l'attuale reperimento delle autorizzazioni di Sme.UP, questo comportamento può essere evitato ritornando nel messaggio la costante**CONT**.
