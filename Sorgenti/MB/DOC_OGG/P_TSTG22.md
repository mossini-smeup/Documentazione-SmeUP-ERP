# ESEMPI  1. CONTROLLARE INIZIO E FINE IMMESSI IN ORE/MINUTI
# GESTIONE FUNZIONI DI ORARIO
# FUNZIONI / METODI
Il dettaglio delle funzioni è visibile attraverso il programma di simulazione
.    Convertire
.    Controllare
.    Calcolare
.    Funzioni multiple o composte
.    Visualizzare
# SIGNIFICATO DEI CAMPI
Inizio/Fine/Intervallo
# ALTRE CONDIZIONI
Formati di input/output
Codice orario
Sostituzione centesimi/secondi per input/output
# OUTPUT
Viene calcolato solo se richiesto un formato di output
# INFORMAZIONI CORRELATE
.    Nella tabella di personalizzazione B£2 è indicato il valore assunto per la gestione di ore o minuti nella forma
centesimale o per minuti/secondi.
Tale tabella è accessibile con funzione VIS->MAT
# ESEMPI
1.   CONTROLLARE INIZIO E FINE IMMESSI IN ORE/MINUTI OTTENENDO IL
RISULTATO DELLA DIFFERENZA IN ORE/CENTESIMI
Utilizziamo la funzione MUL ed il metodo CCC.
Come altre condizioni immettiamo  : 
- formato input           H
- formato output          H
- input in ore/minuti     S
- output in ore/centesimi C
Immettiamo ora inizio e fine; la funzione effettuerà prima i necessari controlli sull'input, quindi calcolerà la
differenza convertendola in ore/centesimi.
Input               Output
Inizio         15,5000             15,8333
Fine           17,0000             17,0000
Intervallo                          1,1667
2.   Trasformare ora/centesimi in minuti.
Utilizziamo la funzione MUL ed il metodo C C
Come altre condizioni immettiamo  : 
- formato input           H
- formato output          M
- input in ora/centesimi  C
- output in minuti        S
Immettiamo ora l'ora e la funzione dopo avere effettuato gli opportuni controlli la convertirà in minuti.
Input               Output
Inizio         10,3000             618,0000
Fine
Intervallo
3.   Controllare la correttezza formale di un'ora.
Utilizziamo la funzione CNV ed il metodo FOR.
4.   Verificare la compatibilità di un orario con i turni definiti in un codice orario in tabella OLG.
Utilizziamo la funzione CNV ed il metodo OLG.
5.   Calcolare l'intervallo tra ore a cavallo della mezzanotte.
Utilizziamo la funzione CAL ed il metodo INT.
Immettiamo i dati di input e come altre condizioni imponiamo la gestione della mezzanotte.
Input
Inizio             21,5000
Fine                3,0000
Intervallo          5,5000 (calcolato)
