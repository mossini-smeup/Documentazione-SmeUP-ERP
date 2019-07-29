# DEFINIZIONE PARZIALIZZAZIONI
# Standard di parzializzazione
I campi di parzializzazione (inferiore e superiore) per interrogazioni e stampe hanno il seguente comportamento : 
Se il campo inferiore è lasciato a spazio si assume come blanks per alfanmerici, zero per numerici positivi, -9999 per
numerici positivi o negativi.
Se il campo superiore è lasciato a spazio e il campo superiore è pure spazio si assume 9999.
Se il campo superiore è lasciato a spazio e il campo inferiore non è spazio si riporta il campo inferiore in quello
superiore.
Si controlla che il campo superiore sia maggiore o uguale al campo inferiore.
# Routine di parzializzazione
Per eseguire automaticamente tutte le funzioni di parzializzazione, (ricerche alfabetiche, controlli formali,
controlli congruenza limiti, impostazione valori di parzializzazione secondo gli standard esposti nel paragrafo
precedente, impostazione di indicatori di ritorno e del codice del messaggio d'errore), si esegue la routine standard
£PRZ, richiamata con i seguenti parametri : 
£PRZTC :  Tipo Campo (8 caratteri)
I primi due caratteri definiscono il tipo di campo codificato nella tabella *CN, con le seguenti aggiunte : 
'  ' Carattere libero
'DT' Data
'NP' Numero positivo
'NZ' Numero negativo o positivo
Il terzo carattere definisce se il campi sono da controllare, secondo questa regola : 
'D'            E' obbligatorio il campo 'DA'
'A'            E' obbligatorio il campo 'A'
'altro'   Car' Sono obbligatori entrambi.
Ad esempio, ARD significa che il campo inferiore digitato non può essere a blanks e che inoltre deve esistere
nell'anagrafica articoli dell'applicazione, DTx significa invece che le date minime e massime non possono essere a
zero, oltre ad essere formalmente valide (cosa che, per le date, è sempre controllata :  non si può infatti inserire una
data non valida).
I caratteri dal quarto all'ottavo, se il campo è una tabella, devono contenere il settore (2 carattrei) ed il
subsettore (3 caratteri), se la Tabella è SMEUP.
£PRZLI     :     Attiva la gestione delle liste per il campo. Attivando questa funzione se il primo carattere del campo è un "_"  il parzializzatore invece che puntare all'oggetto passato, punterà ad un lista dell'oggetto passato.
Viene inoltre dato come assunto che la lista del campo inferiore identifica una lista di selezione, mentre la lista
del lato superiore identifica una lista di omissione.
£PRZWN     :     Campo inferiore alfanumerico del video (30 caratteri)
£PRZWX     :     Campo superiore alfanumerico del video (30 caratteri)
£PRZVN     :     Campo inferiore numerico del video (30.9) £PRZVX     :     Campo superiore numerico del video (30.9)
Se è stata effettuata la ricerca alfabetica, questi campi, all'uscita della routine, sono riempiti con la scelta
effettuata.
In output sono anche riempiti i seguenti campi : 
£PRZAN     :     Campo inferiore alfanumerico da muovere in
LDA (30 caratteri)
£PRZAX     :     Campo superiore alfanumerico da muovere in
LDA (30 caratteri)
£PRZNN     :     Campo inferiore numerico da muovere in
LDA (30.9)
£PRZNX     :     Campo superiore numerico da muovere in
LDA (30.9)
£PRZDN     :     Decodifica del campo inferiore (40 caratteri) £PRZDX     :     Decodifica del campo superiore (40
caratteri) £PRZME     :     Codice del messaggio d'errore secondo gli standard SMEUP (8 caratteri)
ON      :     Errore sul campo inferiore
36 ON      :     Eseguita ricerca alfabetica 37 ON      :     Errore sul campo superiore
