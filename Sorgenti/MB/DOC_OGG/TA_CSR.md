# CSR - Famiglie ricariche
 :  : DEC T(ST) K(CSR)
## OBIETTIVO
Questa tabella può essere associata ad ogni classe. Definisce il metodo di attribuzione dei costi fissi ai materiali, alle lavorazioni esterne e delle ricariche per calcolare i costi industriali e generali.
È inoltre possibile definire il criterio per la determinazione del prezzo minimo di vendita.
Ogni valore può essere una percentuale; in questo caso, la sua applicazione sarà guidata dalla tabella CSA, oppure un valore unitario dipendente dal volume o peso.
Risulta evidente che tale impostazione permette, con una semplice modifica al programma, di far dipendere tale imputazione da altri valori specifici.
## SOTTOSETTORE
Permette di gestire diversi valori per la stessa famiglia di ricariche (quindi per la stessa classe articolo).
_9_Esempio
Può essere utilizzato per memorizzare i valori di anni diversi.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Elemento**
È il codice famiglia di ricariche che viene letto dalla tabella classi materiale (CLS).
 :  : FLD T$I,1 **Incidenza**
Indica la percentuale o un valore unitario da applicare nel calcolo costi. Per le lire, il valore va specificato in migliaia di lire con eventuali decimali.
 :  : FLD T$I,2.T$I,1 Incidenza
 :  : FLD T$I,3.T$I,1 Incidenza
 :  : FLD T$I,4.T$I,1 Incidenza
 :  : FLD T$I,5.T$I,1 Incidenza
 :  : FLD T$I,6.T$I,1 Incidenza
 :  : FLD T$I,7.T$I,1 Incidenza
 :  : FLD T$I,8.T$I,1 Incidenza
 :  : FLD T$I,9.T$I,1 Incidenza
 :  : FLD T$I,10.T$I,1 Incidenza
 :  : FLD T$I,11.T$I,1 Incidenza
 :  : FLD T$T,1 **Tipo incidenza**
Il tipo di incidenza può assumere i seguenti valori : 
- '%'  Percentualmente sul valore del costo. Il valore su cui si applica la percentuale dipende dalla compilazione della tabella CSA.
- 'P'  se calcolata sul peso del particolare.
- 'V'  se calcolata sul volume del particolare in esame.
- '£'  Valore assoluto. Da inserire in valore assoluto.
- '1'  Valore assoluto. Da inserire /1000.
- '2'  Valore assoluto. Da inserire /1000000.
- 'U'  Exit utente D0CR01_UT
 :  : FLD T$T,2.T$T,1 Tipo incidenza
 :  : FLD T$T,3.T$T,1 Tipo incidenza
 :  : FLD T$T,4.T$T,1 Tipo incidenza
 :  : FLD T$T,5.T$T,1 Tipo incidenza
 :  : FLD T$T,6.T$T,1 Tipo incidenza
 :  : FLD T$T,7.T$T,1 Tipo incidenza
 :  : FLD T$T,8.T$T,1 Tipo incidenza
 :  : FLD T$T,9.T$T,1 Tipo incidenza
 :  : FLD T$T,10.T$T,1 Tipo incidenza
 :  : FLD T$T,11.T$T,1 Tipo incidenza
 :  : FLD T$EXRI **Escludere da ricariche**
Se si immette un carattere qualsiasi, i costi del componente non vengono considerati per la loro quota di costo nel calcolo delle ricariche all'interno del prodotto a cui appartengono.
Questa tecnica è applicabile, ad esempio, nel caso si abbiano all'interno di un prodotto finito componenti (specialmente se di elevato valore) forniti dal cliente stesso (motori di una macchina di lavorazione ecc.)
_9_Esempio : 
Cod. Cls  F.Ric     % Mat     % Gen     Escluso   Costo
A    01   A1        10        20        SI        Calcolato
B    02   A2        30        40        NO        100
C    03   A3        50        60        SI        200
A è composto di B e C entrambi di acquisto.
Se calcoliamo il costo di A abbiamo : 
Variabili Ausiliari Totale
Acquisto  Acquisto
B         100        30       130
C         200       100       300
------------------------------------
A         300       130       430
Variabili di acquisto    300
Ausiliari di acquisto    130
Generali                  26
26 è il 20% di 130, cioè del solo costo di B. Le 300 del costo di C non sono considerate, in quanto C appartiene alla classe 03 che appartiene alla classe di ricariche A3, per cui si è definita l'esclusione dal calcolo delle ricariche.
