# ELENCO DI OGGETTI DI TIPO DEFINITO
Questo programma di test permette di visualizzare le funzioni svolte dalla B£DEC4.
FUNZIONE DI LETTURA
Lo scopo di questa funzione e quello di selezionare all'interno di un determinato archivio un certo numero di elementi. Tali elementi sono ritornati mediante due schiere di 999 elementi contenenti rispettivamente i codice elemento e le rispettiva descizione. Tramite il limite iniziale e finale è possibile selezionare sono una parte degli elementi contenuti in un archivio.
E' possibile fissare il numero massimo di elementi in Output.Il programma che effettua la selezione degli elementi (B£DEC4) attualmente gestisce solo i seguenti tipi di oggetto : 
 * AR :  Esegue la selezione degli articoli utilizzando la £IFART
 * TA :  Esegue tale selezione leggendo il file TABEL0P
 * RI :  Esegue tale selezione utilizzando la £IFCDL
 * V2 :  Esegue tale selezione utilizzando la £G15.
 * ST :  Restituisce i settori delle tabelle SMEUP. E' possibile fissare un limite iniziale e finale.
 * SS : Restituisce dato un settore di tabella SMEUP i sottosettori definiti per essa. Anche in questo caso e' possibile fissare un limite inf e sup
 * D8 : Restituisce una schiera di massimo 100 date distanti di un certo scostamento utilizzando il seguente metodo : 
 ** Data Partenza :  Data odierna
 ** Limite iniziale :  Fissa il num. giorni da considerare prima della data di partenza.
 ** Limite Finale :    Fissa il numero di giorni da considerare dopo la data di partenza.
 ** Numero elementi :  Fissa il numero date da ricevere in Output.
Viene calcolato lo scostamento tra le date in questo modo : 
 ** Lim. inz. + Lim. fin. / Num. Elem.

FORMATI GESTITI :  *YMD, *DMY, *YYMD, *DMYY.
Per i rimanenti tipo di oggetto utilizza il B£DEMO_DEM. In quasto caso per vedere da dove carica i valori e necessario vedere il sorgente di tale PGM. In esso alcuni tipi vengono gestiti utilizzando gli archivi SMEUP e altri caricando dei valori cablati definiti per tipo nella schiera in fondo a tale PGM.

E' stato introdotto un metodo denominato ULU che restituisce fissato un limite inziale l'ultimo elemento per quel tipo con codice contente il valore fissato nel limite. Tale  elemento è presente nel 1° elemento della schiera di Output SCO con la rispettiva descizione nell'elemento
