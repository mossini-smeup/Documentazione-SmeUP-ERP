# C6J - Ageing
 :  : DEC T(ST) K(C6J)
## OBIETTIVO
Impostare le colonne di analisi dell'ageing.
Negli esempi in basso si suppine che all'interno della C51 sia stato impostato a 1 il numero di giorni per scaduto.

**Esempio 1 :  intervalli fissi per mese**
Scaduto : 
1° Intervallo : 1   Tipo :  M   gg fisso se mese : 
2° Intervallo : 2   Tipo :  M   gg fisso se mese : 
3° Intervallo : 3   Tipo :  M   gg fisso se mese : 
4° Intervallo : 4   Tipo :  M   gg fisso se mese : 
A scadere : 
1° Intervallo : 1   Tipo :  M   gg fisso se mese : 
2° Intervallo : 2   Tipo :  M   gg fisso se mese : 
3° Intervallo : 3   Tipo :  M   gg fisso se mese : 
4° Intervallo : 4   Tipo :  M   gg fisso se mese : 

Analizzando l'ageing con data situazione 31/12/XX il sistema visualizzarà le colonne : 
 * Scaduto 30gg = data scadenza dal 30/11/XX al 30/12/XX
 * Scaduto 60gg = data scadenza dal 30/10/XX al 29/11/XX
 * Scaduto 90gg = data scadenza dal 30/09/XX al 29/10/XX
 * Scaduto 120gg = data scadenza dal 30/08/XX al 29/09/XX
 * Scaduto oltre 1200gg = data scadenza inferiore al 30/08/XX
 * A scadere 30gg = data scadenza dal 31/12/XX al 30/01/XX+1
 * A scadere 60gg = data scadenza dal 31/01/XX+1 al 28/02/XX+1 (o 29/02 se XX è bisestile)
 * A scadere 90gg = data scadenza dal 01/03/XX+1 al 30/03/XX+1
 * A scadere 120gg = data scadenza dal 31/03/XX+1 al 30/04/XX+1
 * A scadere Oltre 120gg = data scadenza superiore al 30/04/XX+1

**Esempio 2 :  intervalli variabili**
Scaduto : 
1° Intervallo : 15   Tipo :  G   gg fisso se mese : 
2° Intervallo : 1     Tipo :  M   gg fisso se mese : 
3° Intervallo : 2     Tipo :  M   gg fisso se mese : 
4° Intervallo :        Tipo :        gg fisso se mese : 
A scadere : 
1° Intervallo : 15   Tipo :  G   gg fisso se mese : 
2° Intervallo : 1     Tipo :  M   gg fisso se mese : 
3° Intervallo : 2     Tipo :  M   gg fisso se mese : 
4° Intervallo :        Tipo :       gg fisso se mese : 

Analizzando l'ageing con data situazione 31/12/XX il sistema visualizzarà le colonne : 
 * Scaduto 15gg = data scadenza dal 15/12/XX al 30/12/XX
 * Scaduto 1m = data scadenza dal 30/11/XX al 14/12/XX
 * Scaduto 2m = data scadenza dal 30/10/XX al 29/11/XX
 * Scaduto oltre 2m = data scadenza inferiore al 30/10/XX
 * A scadere 15gg = data scadenza dal 31/12/XX al 14/01/XX+1
 * A scadere 1m = data scadenza dal 15/01/XX+1 al 30/01/XX+1
 * A scadere 2m = data scadenza dal 31/01/XX+1 al 28/02/XX+1 (o 29/02 se XX è bisestile)
 * A scadere Oltre 2m = data scadenza superiore al 28/02/XX+1 (o 29/02 se XX è bisestile)

**Esempio 3 :  utilizzo gg fisso**
Scaduto : 
1° Intervallo : 1   Tipo :  M   gg fisso se mese : 5
2° Intervallo : 2   Tipo :  M   gg fisso se mese : 5
A scadere : 
1° Intervallo : 1   Tipo :  M   gg fisso se mese : 5
2° Intervallo : 2   Tipo :  M   gg fisso se mese : 5

Analizzando l'ageing con data situazione 31/12/XX il sistema visualizzarà le colonne : 
 * Scaduto 30gg = data scadenza dal 05/11/XX al 30/12/XX
 * Scaduto 60gg = data scadenza dal 05/10/XX al 04/11/XX
 * Scaduto oltre 60gg = data scadenza inferiore al 05/10/XX
 * A scadere 30gg = data scadenza dal 31/12/XX al 05/01/XX+1
 * A scadere 60gg = data scadenza dal 06/01/XX+1 al 05/02/XX+1
 * A scadere Oltre 60gg = data scadenza superiore al 05/02/XX+1

**Esempio 4 :  utilizzo gg fisso con fine mese**
Scaduto : 
1° Intervallo : 1   Tipo :  M   gg fisso se mese : 31
2° Intervallo : 2   Tipo :  M   gg fisso se mese : 31
A scadere : 
1° Intervallo : 1   Tipo :  M   gg fisso se mese : 31
2° Intervallo : 2   Tipo :  M   gg fisso se mese : 31

Analizzando l'ageing con data situazione 15/12/XX il sistema visualizzarà le colonne : 
 * Scaduto 30gg = data scadenza dal 30/11/XX al 14/12/XX
 * Scaduto 60gg = data scadenza dal 31/10/XX al 29/11/XX
 * Scaduto oltre 60gg = data scadenza inferiore al 31/10/XX
 * A scadere 30gg = data scadenza dal 15/12/XX al 31/01/XX+1
 * A scadere 60gg = data scadenza dal 01/02/XX+1 al 28/02/XX+1 (o 29/02 se XX è bisestile)
 * A scadere Oltre 60gg = data scadenza superiore al 28/02/XX+1 (o 29/02 se XX è bisestile)

**Esempio 5 :  analisi per mese**
Scaduto : 
1° Intervallo :    Tipo :  M   gg fisso se mese : 1
2° Intervallo : 1   Tipo :  M   gg fisso se mese : 1
3° Intervallo : 2   Tipo :  M   gg fisso se mese : 1
4° Intervallo : 3   Tipo :  M   gg fisso se mese : 1
A scadere : 
1° Intervallo :     Tipo :  M   gg fisso se mese : 31
2° Intervallo : 1   Tipo :  M   gg fisso se mese : 31
3° Intervallo : 2   Tipo :  M   gg fisso se mese : 31
4° Intervallo : 3   Tipo :  M   gg fisso se mese : 31

Analizzando l'ageing con data situazione 15/12/XX il sistema visualizzarà le colonne : 
 * Scaduto 0gg=  data scadenza dal 01/12/XX al 14/12/XX
 * Scaduto 30gg = data scadenza dal 01/11/XX al 30/11/XX
 * Scaduto 60gg = data scadenza dal 01/10/XX al 31/11/XX
 * Scaduto 90gg = data scadenza dal 01/09/XX al 30/09/XX
 * Scaduto oltre 90gg = data scadenza inferiore al 01/09/XX
 * A scadere 0gg = data scadenza dal 15/12/XX al 31/12/XX
 * A scadere 30gg = data scadenza dal 01/01/XX+1 al 31/01/XX+1
 * A scadere 60gg = data scadenza dal 01/02/XX+1 al 28/02/XX+1 (o 29/02 se XX è bisestile)
 * A scadere 90gg = data scadenza dal 01/03/XX+1 al 31/03/XX+1
 * A scadere Oltre 90gg = data scadenza superiore al 31/03/XX+1

## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Codice**
Indica il codice dell'ageing.
 :  : FLD T$DESC **Descrizione**
 :  : FLD T$C6JA **1° Intervallo**
Definisce la durata del primo intervallo. Il campo può essere blank (0) solo sul primo intervallo. Insieme a questo campo sarà necessario compilare anche la tipologia di intervallo.
 :  : FLD T$C6JB **Tipo**
Definisce la tipologia dell'intervallo (giorni oppure mesi)
 :  : FLD T$C6JC **gg Fisso se mese**
Nel caso in cui si sia impostata la tipologia mese è possibile forzare uno specifico giorno del mese. In questo caso il sistema andrà al giorno antecedente alla data calcolata. Se nel campo è impostato il valore 31 il sistema andrà sempre alla fine del mese.
Si rimanda agli esempi per maggiori dettagli sull'utilizzo dei campi.
 :  : FLD T$C6JD.T$C6JA
 :  : FLD T$C6JE.T$C6JB
 :  : FLD T$C6JF.T$C6JC
 :  : FLD T$C6JG.T$C6JA
 :  : FLD T$C6JH.T$C6JB
 :  : FLD T$C6JI.T$C6JC

 :  : FLD T$C6JJ.T$C6JA
 :  : FLD T$C6JK.T$C6JB
 :  : FLD T$C6JL **gg Fisso se mese**
Nel caso in cui si sia impostata la tipologia mese è possibile forzare uno specifico giorno del mese. In questo caso il sistema andrà al giorno successivo alla data calcolata.
Si rimanda agli esempi per maggiori dettagli sull'utilizzo dei campi.
 :  : FLD T$C6JM.T$C6JA
 :  : FLD T$C6JN.T$C6JB
 :  : FLD T$C6JO.T$C6JL
 :  : FLD T$C6JP.T$C6JA
 :  : FLD T$C6JQ.T$C6JB
 :  : FLD T$C6JR.T$C6JL
 :  : FLD T$C6JS.T$C6JA
 :  : FLD T$C6JT.T$C6JB
 :  : FLD T$C6JU.T$C6JL
 :  : FLD T$C6JV.T$C6JA
 :  : FLD T$C6JW.T$C6JB
 :  : FLD T$C6JX.T$C6JL
