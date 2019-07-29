# Generalità
Questa funzione permette di determinare gli importi da liquidare agli agenti in base al tipo liquidazione previsto per ognuno.
Le tipologie di liquidazione sono : 
 * _2_sul fatturato, all'agente vengono corrisposte le provvigioni in base alle fatture procurate nel periodo preso in esame;
 * _2_sull'incassato (pagato), all'agente vengono corrisposte le provvigioni in base ai pagamenti effettuati nel periodo in esame su fatture da lui precedentemente procurate;
 * _2_sul saldato, all'agente vengono corrisposte le provvigioni in base a fatture da lui precedentemente procurate e saldate nel periodo preso in esame.

Per determinare gli importi delle ultime due tipologie vengono analizzati i movimenti contabili relativi alle singole fatture procurate dall'agente. Ciò avviene tramite la /COPY £G34, che, dando in input il documento e il periodo, ne ritorna i relativi importi.

Il metodo di calcolo può essere suddiviso in % sui diversi metodi, tramite l'utilizzo della tabella V6S, impostabile a livello della tabella Agente, della V58 o dello stesso record della provvigione.
Impostando inoltre il relativo flag sulla tabella V58 è possibile implementare un'exit che, al termine dei calcoli prima dell'aggiornamento del file, può permettere di applicare eventuali considerazioni particolari al risultato dei calcoli standard.

# Come si lancia il Calcolo Provvigioni
Per eseguire il programma di calcolo delle provvigioni occorre impostare i seguenti parametri di lancio : 
**- Periodicità Liquidazione : ** indica se devono essere elaborate le provvigioni con liquidazione mensile, trimestrale, ecc...
**- Data di Elaborazione : ** Vengono prese in considerazione solo le provvigioni con data fattura compresa tra questi limiti.
Solitamente si imposta la data finale uguale all'ultimo giorno del periodo di liquidazione (se sto facendo una liquidazione del secondo trimestre metterò 30 giugno). Si consiglia di non impostare la data iniziale per essere sicuri che vengano elaborate tutte le provvigioni ancora aperte (non completamente liquidate) anche di periodi precedenti a quello che si sta elaborando.
**- Codice Intestatario : ** E' un filtro per limitare il calcolo solo ad alcuni agenti.
**- Data Registrazione Contabile : ** Quando si sta liquidando provvigioni sull'incassato (pagato) o sul saldato, il sistema deve vedere la situazione contabile della fattura, deve cioè determinare quando e per che importo questa fattura è stata pagata. Per fare questo legge le registrazioni contabili. Con questo filtro è possibile fare in modo che eventuali pagamenti successivi alla data finale impostata non vengano presi in considerazione. Solitamente la data iniziale non viene impostata.
**- Data Limite Insoluti : ** Sempre nel caso di liquidazioni sull'incassato o sul saldato è la data in base alla quale vengono incluse nel saldo le sole registrazioni insoluti (o protesti).
Questo al fine di permettere di considerare correttamente le riba che a fine mese sono andate insolute. E' consigliabile quindi inserire qualche giorno successivo alla data limite di calcolo.

# Oggetti
## Pgm del flusso
V5PR02G/V  :  Guida
V5PR02CL   :  Seleziona i record del V5PROV da analizzare
V5PR02C    :  Esecuzione
B£G34G_XX  :  Pgm calcolo importi (dove ad XX va sostituito il codice dell'ambiente di contabilità)
V5PR02C_X  :  Eventuale pgm di exit per aggiustare il record prima che venga aggiornato

## Richiamo pgm Calcolo provvigioni
 :  : INI
 :  : CMD CALL V5PR02G
 :  : FIN

## Tabelle
 :  : DEC T(ST) P() K(V58)
 :  : DEC T(ST) P() K(AGE)
 :  : DEC T(ST) P() K(V6S)

# Punti aperti
Mettere un flag sulla provvigione che indica il tipo di liquidazione.
