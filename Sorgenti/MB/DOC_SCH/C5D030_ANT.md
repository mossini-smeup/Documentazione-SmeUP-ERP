## Obiettivo
Obiettivo di questa scheda è analizzare i finanziamenti  erogati come anticipo su fatture attive evidenziando per ogi fattura presentata gli incassi avvenuti.

![C5D030_054](http://localhost:3000/immagini/MBDOC_SCH-C5D030_ANT/C5D030_054.png)
## Parametri di lancio

* Da data :  permette di definire la data iniziale del periodo di analisi.
* A data :  permette di definire la data finale del periodo di analisi.
* Condizione contabile :  permette di includere o meno i movimenti simulati.
* Rapporto :  permette di limitare le interrogazioni ad un singolo rapporto bancario.
* N° Finanziamento :  permette di limitare le interrogazioni ad un singolo finanziamento.

Al lancio verranno elaborati tutti gli incassi degli anticipi che risultavano aperti alla data di inizio periodo e quelli che sono stati movimentati all'interno del periodo (aperti e chiusi o rimasti aperti alla fine del periodo).

## Dettaglio informazioni

Per ogni scadenza oggetto di un anticipo vengono riportati : 

* Id Scadenza :  è l'id univoco della scadenza
* Data Scadenza
* Valuta
* Data ultimo incasso :  data registrazione in cui è avvenuto l'ultimo incasso della scadenza
* Importo finanziato :  è l'importo finanziato sulla scadenza. Può essere uguale, superiore o inferiore alla scadenza.
* Quota parte incassata nel periodo :  è la percentuale incassata nel periodo indicato dell'importo finanziato. Se, ad esempio, avessimo una scadenza di 1.000¤ su cui è stato effettuato un anticipo di 500¤ e sulla scadenza registrassimo un incasso di 500¤, in questa colonna verrebbe inserito il valore 250¤.
* Quota parte incassata totale :  è la percentuale incassata totale dell'importo finanziato.
* Quota residua del finanziamento :  è la quota residua del finanziamento ovvero la differenza tra l'importo finanziato e la quota parte incassata totale.
* Data scadenza della rata
* Importo scadenza :  è l'importo totale della scadenza. Può essere uguale, maggiore o inferiore all'importo finanziato.
* Incassato in un periodo precedente :  eventuale incasso relativo alla scadenza effettuato in un periodo precedente a quello in analisi.
* Incassato del periodo :  incasso relativo alla scadenza avvenuto nel periodo in esame.
* Importo incassato :  sommatoria degli importi incassato da periodo precedente e incassato del periodo.
* Residuo scadenza :  è l'importo residuo, ancora da incassare della scadenza.
* Data documento
* N° documento
* Ente intestatario della scadenza
* Rapporto bancario
* Numero del finanziamento
* Dettaglio Incassi :  la prima riga di ogni finanziamento viene riempita con una lente di ingradimento. Cliccando sulla lente viene lanciata una finestra in cui verranno messi a confronto i movimenti di incasso delle fatture presentate e i movimenti del conto di finanziamento.
* Segnalazioni :  la loro presenza (normalmente dovuta al riscontro di una differenza fra la quota rimborsabile calcolata teoricamente sulla base degli incassi avvenuti e quella effettiva del conto) implica la colorazione con sfondo rosso della prima scadenza del finanziamento.

**NOTA BENE** :  la prima riga di un finanziamento viene esposta con sfondo rosso se viene riscontrata una squadratura tra il saldo per data operazione del conto anticipi e il valore residuo calcolato sul finanziamento. E' importante, però, notare che : 
* Fra i movimenti di incasso ed i movimenti di rimborso dei finanziamenti può esservi una differenza sulla data di registrazione e, quindi, a parità di data il saldo del conto non coincida con il saldo del finanziamento.
* E' inoltre importante notare che gli incassi si basano sulla data registrazione in cui sono avvenuti, mentre i movimenti del conto anticipi (e, quindi, la determinazione del suo saldo) si basano sulla data operazione in cui sono stati registrati.

## Opzioni
Selezionando la freccetta posta nella prima colonna di ogni riga è possibile accedere : 
 * Alle funzioni di gestione della scadenza (che permettono di visualizzarla, modificarla, ecc.)
 * All'analisi di tutte le scadenze aperte per il cliente (tramite il menù Surf)
 * All'analisi della situazione della partita (tramite il menù Surf)
