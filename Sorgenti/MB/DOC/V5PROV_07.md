# Premesse

Tramite la funzione di contabilizzazione delle pro-forma è possibile contabilizzare in modo massivo tutte i documenti di attesa creati nell'apposita procedura.

**NOTA BENE** :  questa funzione prevede che tali documenti vengono contabilizzati solo in maniera provvisoria.

# Impostazione

Per procedere correttamente con la procedura di contabilizzazione è necessario che vengano adottatti alcuni accorgimenti aggiuntivi a livello di tipo provvigione : 
* Deve essere attribuito al tipo provvigione un modello di documento (**V5Axx_) che preveda a sua volta all'associazione di una causale contabile (C5A) che corrisponda ad un tipo registrazione simulato (C5D) che sia già predispoto per finire sul registro iva corretto.
* Nell'eventualità che possano coesistere nello stesso periodo quote di liquidazione positive e negative, è importante che venga inoltre attribuito anche il campo "Tipo provvigione Nt/Ft", dove è possibile indicare il tipo provvigione da utilizzare nel caso in cui saldo sia di segno opposto.
* A disposizione anche solo per il documento pro-forma, ma ancora più utili per la contabilizzazione i campi "Iva" e "Conto".

