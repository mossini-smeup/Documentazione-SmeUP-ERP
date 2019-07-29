# Obiettivo
Scrivere dati verso un dispositivo di campo, oppure leggere dati dal dispositivo di campo.

## Procedura
Per testare il corretto funzionamento del colloquio con il campo vi sono due possibiltà : 
-- Da NeroVerde
Dopo aver selezionato la funzione T K10, compilare : 
Funzione SND
Metodo OUT.
Subsezione A37 <NomeLoa37>.<SEZ>.<SUB>
Dove NomeLoa37 sono gli ultimi due caratteri del nome della Loa37 che si vuole interrogare, mentre sez e sub rispettivamente sezione e subsezione dove si trova la variabile.

Nella schermata successiva si inseriscono  Nome (£K10S_NM) della variabile e Valore (£K10S_VA) che le si vuole impostare.
Dando un doppio invio, se l'operazione è andata a buon fine rientrando nella schermata di inserimento si vedranno Nome variabile e valore "true".

Un caso particolare è la lettura del dato dal campo. Per fare questo è sufficiente indicare al posto di Valore, la parola chiave *READ.
Dando doppio invio e rientrando nella schermata di inserimento si vedranno Nome variabile e suo valore attuale.

-- Da LoocUp
Nella spotlight scrivere O V3 LSE <NomeProvider>
Il NomeProvider coincide con il nome della coda che genera.

A sinistra nel menù selezionare LOA37.
A questo punto apparirà l'albero contenente tutte le LOA37 configurate per quel Provider. Selezionare quella di interesse.

Nella parte più a destra vengono presentate le variabili con il loro nome.
Selezionare il tab Simulazione ed inserire
<NomeVariabile>(<Valore>) per scrivere un valore verso il campo
<NomeVariabile>(*READ) per leggere un valore dal campo.
L'invio del comando lo si dà con shift+enter




