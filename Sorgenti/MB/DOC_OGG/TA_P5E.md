# P5E - Causale evento
 :  : DEC T(ST) K(P5E)
## OBIETTIVO
Definsice la causale che caratterizza un evento e che va impostata all'atto della dichiarazione dell'evento.
## SOTTOSETTORI
È possibile suddividerla in sottosettori, assegnati al tipo di evento (tabella P5D)
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
 :  : FLD T$DESC Descrizione
 :  : FLD T$P5EA __Sottosettore esito evento RE (CRM)__
E' un campo utilizzato esclusivamente nel modulo attività del CRM, per il quale vengono gestiti eventi di tipo standard £C1, che rappresentano attività CRM (telefonate, mail, ecc.).
Definisce il sottosettore della tabella REK, nel quale vengono definiti gli esiti dell'attività di CRM, che possono essere quindi diversificate in base alla causale evento, ottenendo possibili esiti diversificati ad esempio per telefonate, mail, ecc. .
