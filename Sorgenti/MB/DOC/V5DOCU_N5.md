# Note di :  credito(clienti) debito(fornitori)
Sono di due tipi : 
 - **Con movimentazione di magazzino**; Tipo modello AE / PU, Flag 18 = blank, Flag 19 = N / n. Viene collegata a magazzino se il numero bolla è diverso da blank (se il documento è "E" la bolla è obbligatoria)
 - **Senza movimentazione di magazzino**; Tipo modello AN / PN, Flag 18 = 9, Flag 19 = N / n. Viene collegata se è eseguita la stampa fattura (presente il campo numero fattura)
