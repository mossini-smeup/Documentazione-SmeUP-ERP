# SPIEGAZIONE CALCOLI

## SU SCADENZARIO ATTIVO
* Importo Documenti  :  totale importo movimenti con tipo movimento causale <= 03 (Documenti)
* Abbuoni  :  totale importo movimenti con tipo movimento causale 06
* Sconti  :  totale importo movimenti con tipo movimento causale 11
* Perdite  :  totale importo movimenti con tipo movimento causale 08
* Rischio  :  totale importi scadenze in rischio
* Saldato  :  somma di tutti i movimenti che non rientrano nei casi precedenti
* Residuo  :  differenza importo documenti e tutte le tipologie successive
* Scaduto  :  residuo con data scadenza <= data di riferimento
* Insoluti / Protesti  :  somma di tutti i movimenti con tipo movimento 04 o 09
* Totale Ritardo  :  somma di tutti i movimenti di incasso/pagamento effettuati in ritardo e dei residui con data scadenza <= data di riferimento
* Costo Ritardo  :  importo calcolato applicando al ritardo il costo del denaro fissato dalla tabella C51 con divisore 360
* GG Ritardo su Ritardo  :  media dei giorni di ritardo sui soli movimenti di ritardo. I giorni di ritardo vengono calcolati dalla differenza fra la data scadenza originale e la data di effettuazione del pagamento (data scadenza per gli effetti, data valuta se indicata o in risalita data registrazione)
* GG Ritardo su Saldato + Residuo  :  media dei giorni di ritardo su movimenti di incasso / pagamento sommati agli importi residui.
* Costo Incasso  :  importo calcolato applicando al ritardo il costo del denaro fissato dalla tabella C51 con divisore 360
* GG Medi di Incasso  :  media dei giorni di incasso calcolati dalla differenza fra la data documento e la data di scadenza sui movimenti di documento
* Costo Totale  :  importo dato da la somma del costo del ritardo e dell'incasso

## SU SCADENZARIO PASSIVO
* Importo Documenti  :  totale importo movimenti con tipo movimento causale <= 03 (Documenti)
* Abbuoni  :  totale importo movimenti con tipo movimento causale 06
* Sconti  :  totale importo movimenti con tipo movimento causale 11
* Saldato  :  somma di tutti i movimenti che non rientrano nei casi precedenti
* Residuo  :  differenza importo documenti e tutte le tipologie successive
* Scaduto  :  residuo con data scadenza <= data di riferimento
* Ricavo Pagamento  :  importo calcolato applicando al ritardo il costo del denaro fissato dalla tabella C51 con divisore 360
* GG Medi di Pagamento  :  media dei giorni di pagamento calcolati dalla differenza fra la data documento e la data di scadenza sui movimenti di documento
