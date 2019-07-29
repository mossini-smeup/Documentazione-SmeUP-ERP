# D5I - Indici di distribuzione
 :  : DEC T(ST) K(D5I)
## OBIETTIVO
Restituire una lista di oggetti e di valori associati, che vengono utilizzati dagli algoritmi di validazione (tabella D5M) come indici di distribuzione dei valori riportati dai programmi di ripresa dei sistemi conferenti.
Viene utilizzata congiuntamente alla tabella D5M.
## ESEMPIO
Si vogliono individuare i centri di costo di appartenenza dei dipendenti, in modo da distribuire il loro stipendio.
Supponiamo che l'appartenenza di un dipendente ad un centro di costo sia un parametro multiplo (per esempio DIP APP) con data di validità e valore di distribuzione (in questo modo posso indicare che il dipendente 001 è assegnato al 30% al centro di costo 300 e al 70% al centro di costo 700 e indicare pure le date di validità di questa distribuzione).
Il tipo oggetto 1 sarà DI, il tipo oggetto 2 sarà *blanks e il tipo oggetto risultato sarà CC.
Il metodo da utilizzare è in questo caso *PARA con parametro DIPAPP che, dato un dipendente (DI), mi restituisce una lista di centri di costo (CC) con un'opportuna distribuzione creata leggendo i valori contenuti nel parametro.
Se invece si volesse creare un indice basandosi sulla metratura di un centro di costo (per esempio per distribuire i costi del riscaldamento), si utilizzerà il metodo *OAV con tipo oggetto risultato CC (centro di costo) e come parametro un OAV che restituisca la metratura del singolo CC (che potrà essere memorizzata, per esempio, in un parametro). Andrà inoltre messa la C nel campo "Calcola la %".
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
Nome dell'indice
 :  : FLD T$DESC Descrizione
 :  : FLD T$D5IA **Tipo oggetto 1 origine**
Specificare il tipo del primo oggetto da utilizzare per la ricerca della distribuzione.
 :  : FLD T$D5I1 **Parametro oggetto 1 origine**
Specificare il parametro del primo oggetto da utilizzare per la ricerca della distribuzione.
 :  : FLD T$D5IB **Tipo oggetto 2 origine**
Specificare il tipo dell'eventuale secondo oggetto da utilizzare per la ricerca della distribuzione.
 :  : FLD T$D5I2 **Parametro oggetto 2 origine**
Specificare il parametro del secondo oggetto da utilizzare per la ricerca della distribuzione.
 :  : FLD T$D5IC **Tipo oggetto risultato**
Specificare il tipo degli oggetti che verranno restituiti dall'indice.
 :  : FLD T$D5I3 **Parametro oggetto risultato**
Specificare il parametro degli oggetti che verranno restituiti dall'indice
 :  : FLD T$D5ID **Metodo/programma**
*PARA :  la distribuzione è contenuta in un parametro che avrà una griglia con tipi oggetti uguali a quelli definiti come tipi oggetti origine.
*PGM :   la distribuzione è creata da un programma utente. Vedere come template il file D5D5I_1 nel D5SRC.
*OAV :   la distribuzione viene effettuata applicando un OAV numerico a tutti gli oggetti del tipo oggetto specificato nel tipo/parametro oggetto risultato e, se impostato, rapportando il valore del singolo oggetto rispetto al totale.
I tipi oggetto ammessi sono quelli gestiti dalla B£DEC4 e il numero di oggetti ritornati è limitato a 999 (escludendo quelli a valore 0).
Dovendo leggere tutti gli oggetti di un certo tipo l'indice potrebbe essere abbastanza oneroso.
*OAVD5I :  la distribuzione viene effettuata recuperando un altro elemento della D5I recuperato tramite l'applicazione di un OAV alfa a tutti gli oggetti (o coppie di oggetti) indicati nei campi "Tipo/Par. Oggetto" origine 1/2 (es. un parametro intestato al tipo oggetto o alla coppia di oggetti).
*COSO :  IN SVILUPPO
 :  : FLD T$D5IE **Parametro del metodo**
_Metodo_
*PARA :  1-3 categoria (C£E) del parametro. 4-6 parametro (B£N).
*PGM :   nome del programma utente *OAV :   attributo del tipo/parametro oggetto risultato *COSO :  IN SVILUPPO
 :  : FLD T$D5IF **Calcola la percentuale**
Se viene inserito C, i valori trovati (per esempio nel parametro) vengono trasformati in percentuali rispetto al loro totale, altrimenti vengono considerati già come percentuali.
