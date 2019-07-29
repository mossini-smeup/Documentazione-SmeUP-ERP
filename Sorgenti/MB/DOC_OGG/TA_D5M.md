# D5M - Algoritmi di validazione
 :  : DEC T(ST) K(D5M)
## OBIETTIVO
Impostare il metodo per ricercare gli oggetti della chiave del D5COSO nel quale scrivere i dati. Viene utilizzata congiuntamente alla tabella D5E.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
Deve essere composto in questo modo : 
1. codice dell'elemento della D5E a cui deve essere legato l'algoritmo.
2. carattere '_'
3. tipo e parametro dell'oggetto che si vuole ricercare.
_9_Esempio :  se si vuole legare un algoritmo all'azione (elemento) AZI001 della D5E, per cercare il codice dell'oggetto CC, il nome dell'elemento della D5M dovrà essere AZI001_CC.
È anche possibile utilizzare l'algoritmo per cercare un oggetto necessario per il metodo *CAO specificato nella tabella D5E (vedi help di questa tabella per approfondimenti). In questo caso al posto del tipo e parametro va scritto *CAO (ex. AZI001_*CAO).
 :  : FLD T$D5MA **Metodo**
Specifica il metodo di ricerca dell'oggetto.
*IND :  utilizza un indice di distribuzione (tabella D5I).
*OAV :  lettura da OAV di uno degli oggetti riportati dal sistema conferente.
*PAR :  lettura da parametro di uno degli oggetti riportati dal sistema conferente.
*ASS :  l'oggetto viene direttamente specificato.
*INDDIN :  Come *IND, ma l'indice da utilizzare viene restituito da un OAV.
*INDOAV :  Come *IND, ma l'oggetto da passare all'indice è un OAV di uno degli oggetti riportati dal sistema conferente.
 :  : FLD T$D5MB **Parametro del metodo**
_Metodo : _
*IND :  elemento della tabella D5I.
*OAV :  OAV di un oggetto.
*PAR :  1-3 categoria (C£E) del parametro. 4-6 parametro (B£N).
*ASS :  codice dell'oggetto.
*INDDIN :  OAV di un oggetto che deve restituire un elemento di D5I.
*INDOAV :  01-08  nome dell'indice (elemento della D5I). 09-10 tipo oggetto. 11-20 parametro. 21-30 OAV da applicare all'oggetto sopra specificato
 :  : FLD T$D5MC **Condizione**
Specifica un eventuale condizionamento sull'esecuzione dell'algoritmo.
- B :  l'algoritmo viene eseguito solo se il codice passato dal programma di ripresa da sistema conferente è *BLANKS o è uguale a '**' (codice generico).
- M :  l'algoritmo non viene mai eseguito.
-  F :  l'algoritmo viene eseguito, ma se non viene trovato un codice viene ricercato fra gli oggetti passati dal programma di ripresa.
- *BLANKS  :  l'algoritmo viene sempre eseguito, un eventuale codice passato dal programma di ripresa non viene considerato.
 :  : FLD T$D5MD **Se *BLANKS metti ****
Specifica che, se l'oggetto non viene trovato, deve essere forzato il codice ** (generico).
 :  : FLD T$D5ME **Suff.pgm aggiust.**
Se impostato la £D5A, prima di elaborare l'elemento di D5M, lancia il programma D5D5A0_x (dove x = suff.) che permette di modificare la DS della tabella dinamicamente.

## ESEMPIO
Si vogliono individuare i centri di costo di appartenenza dei dipendenti in modo da distribuirne lo stipendio.
Supponiamo che l'appartenenza di un dipendente ad un centro di costo sia un parametro multiplo (per esempio DIP APP), con data di validità e valore di distribuzione (in questo modo posso indicare che il dipendente 001 è assegnato al 30% al centro di costo 300 e al 70% al centro di costo 700 e indicare pure le date di validità di questa distribuzione).
Il metodo sarà allora *IND con parametro un indice della D5I che, dato un dipendente (DI), mi restituisce una lista di centri di costo (CC) con un'opportuna distribuzione, basandosi sul parametro sopra discusso. Per ulteriori informazioni leggere l'help relativo alla tabella D5I.
Se invece l'appartenenza ad un CC è univoca (cioè al 100%), il metodo sarà *PAR ed il parametro DIPAPP.

