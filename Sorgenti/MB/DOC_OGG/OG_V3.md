# Valori dinamici di Sme.Up.
I valori dinamici di SME.up sono oggetti il cui codice dipende dalla presenza di un altro oggetto, la cui creazione
provoca la contemporanea creazione di un oggetto V3.

Un esempio è dato dalla classe PED, che comprende i programmi delle fonti MAIL_up, e tecnoicamente è composta dai
programmi di nome EDAP_&&_C, dove && è un valore qualsias, che cosititisce anche il valore dell'oggetto.
Quando si crea il programma EDAP_XYC, automaticamente si ottiene anche l'oggetto V3PED XY.

Dettagli implementativi
- [Dettaglio Valori dinamici SME.up](Sorgenti/MB/DOC_OGG/OG_V3_D)
