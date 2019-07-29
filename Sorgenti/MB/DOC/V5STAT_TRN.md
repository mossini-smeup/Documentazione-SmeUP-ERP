 :  : PRO Cod(PRO) Txt(Gestire i progetti)
 :  : ATT Cod(VAR) Txt(Analizzare le variazioni trimestrali di fatturato in una regione)
01. Primo per selezionare i dati da analizzare applichiamo un filtro per "Dati geografici"/"Codice regione" e assegnamo (AND) il codice 03 = Lombardia

02. Dopo aver impostato il filtro, è possibile interrogare la scheda per "Andamento nel tempo" > "Importo netto".

03. Una volta entrati è possibile scegliere il tipo di valore della vista che si vuole visualizzare, in questo caso l' "Importo netto" e quindi impostare il resto delle condizioni di interrogazione in questo modo : 
 * come parametro verticale :  anno
 * come parametro orizzontale :  trimeste

04. Selezionando come "Valore" l'"Aumento - percentuale su precedente - Importo netto" otteniamo le variazioni percentuali : 

 :  : ATT Cod(INT) Txt(Interrogare il fatturato in lobardia di aprile 2009 per cliente)
01. Impostiamo il filtro con periodo = 200904 e regione = 03 (Lombardia) : 

02. Utizziamo l'Analisi di Pareto" e selezioniamo con asse l'"ente intestatario" e come valore l'"Importo netto", in questo modo si ottiene un  report del fatturato ordinato per cliente in ordine discendente : 

 :  : ATT Cod(MAR) Txt(Visualizzare i margini per provincia / classe contabile articolo)
01. Per analizzare il margine l'interrogazione più appropriata è :  "Analisi tabellare" per "Articolo/Ente".
Si impostino i seguenti parametri
 * Valore :  margine
 * Verticale :  cliente - provincia
 * Orizzontale :  articolo - classe contabile

 :  : ATT Cod(REG) Txt(Controlla la registrazione cui appartiene la riga con massimo importo negativo nel 2010)
01. Impostiamo il filtro per esercizio di competenza = 2010.

02. Usiamo l'"Analisi di pareto" con asse = "numero documento" e come valore = "Importo netto". A questo punto non resta che ordinare in modo crescente la colonna del valore, così da avere gli importi negativi in alto alla matrice : 

03. Per vedere il dettaglio di questo importo negativo, è necessario fare un doppio click sulla riga relativa. In questo modo, è possibile, vedere il dettaglio delle righe riferite ai documenti che compongono questo fatturato negativo.
