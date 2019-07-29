# CALCOLO DATE DA TEMPI DI APPROVVIGIONAMENTO
## Obiettivo
Partendo da una data, da una quantità e dai tempi di approvvigionamento, applica questi tempi per determinare le
rimanenti date coinvolte nell'attività.
## Definizioni
Nella pianificazione di una attività produttiva, sono coinvolte le seguenti date, collegate tra loro dai tempi di
approvvigionamento : 
Data inizio attività
+    Tempo approvvig. totale =
Data fine attività
+    Tempo approvvig. rettifica =
Data disponibilità
## Funzioni
'AVANTI'  A partire dalla data inizio vengono calcolate le altre due date
'INDIET'  A partire dalla data disponibilità vengono calcolate le altre due date
'RETTIF'  A partire dalla data fine vengono calcolate le altre due date
## Metodi
Definiscono l'attività che andrà datata :  servono per decidere se tener conto dei giorni lavorativi o di calendario
(vedi paragrafo relativo); valgono per tutte le funzioni, e corrispondono ai codici suggerimenti della pianificazione
(codici V2/M5SUG)
'PR' ordine di produzione
'AQ' ordine di acquisto
'LV' ordine di lavorazione
## Input
Magazzino :  serve per puntare al calendario definito in esso.
Tipo/Codice risorsa :  per puntare ad uno specifico calendario
Quantità calcolo :  è la quantità che deve essere realizzata nell'attività
Quantità riferimento :  è la quantità relativa al tempo di approvvigionamento variabile
Tempi approvviginamento fisso, variabile e rettifica
Data :  è la data da cui derivare le rimanenti :  dipende dal metodo impostato
## Output
Data inizio attività
Data fine attività
Data disponibilità
Tempo di approvvigionam.totale
## Determinazione tempo approvvig.totale
E' composto dal tempo di approvvigionamento fisso, che esprime la quota di tempo che serve ad ogni ordine
indipendentemente dalla quantità da realizzare (comprende, per gli ordini interni i tempi di spostamento, di riposo,
le code, gli attrezzaggi, ecc.., per quelli esterni i tempi di preparazione dell'ordine e del trasporto).
Ad esso si somma il tempo dipendente dalla quantità, dato da : 
(Qtà Calcolo/Qtà Riferimento) x T.appr.variabile
Il risultato è approssimato all'intero superiore.
Se la quantità di riferimento è zero questo tempo viene trascurato.
## Uso dei giorni di calendario o lavorativi
Per determinare se usare, nel calcolo, i giorni lavorativi piuttosto che quelli di calendario, si seguono le seguenti
regole.
Se il metodo è tra quelli previsti (produzione / acquisto / lavorazione) si legge, in tabella M51, se trattare i tempi
in giorni lavorativi o meno.
Se invece il metodo è blanks, si usano i giorni lavorativi se ricevuti il tipo/codice risorsa, altrimenti i giorni di
calendario
Si determina poi quale calendario usare : 
Se ricevuti il tipo/codice risorsa si assumono per leggere il calendario.
Altrimenti si leggono il tipo/codice risorsa contenuti nella tabella del magazzino ricevuto :  se in essa sono blanks,
oppure se non è stato passato un magazzino, si assumono comunque giorni di calendario.
## Spostamento in giorni lavorativi
Nel caso in cui lo spostamento sia in giorni lavorativi, come prima cosa, la data di input viene spostata al primo
giorno lavorativo precedente o successivo ad essa, in funzione di quanto impostato nella tabella di personalizzazione
M51, e da questa data eseguiti gli spostamenti, con l'arrivo sempre in un giorno lavorativo.
 :  : DEC T(VO) P(T.M51) K(T$M51O)
Viene calcolato un calendario di 999 elementi attorno alla data odierna (da oggi - 180 giorni a oggi + 818 giorni). Se
si verifica uno sfondamento di queste date, si assumerà la prima nei calcoli all'indietro, e l'ultima nei calcoli in
avanti.
Se invece si verificano errori nel reperimento del calendario (anno non definito, ecc..) si calcoleranno comunque le
date di calendario, e se ne darà segnalazione nel messaggio.
