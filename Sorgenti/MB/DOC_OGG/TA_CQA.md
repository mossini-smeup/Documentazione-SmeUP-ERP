# CQA - Azioni sul lotto successivo
 :  : DEC T(ST) K(CQA)
## OBIETTIVO
Codificare le azioni da intraprendere su un analogo lotto dello stesso Fornitore, successivo a quello che si sta collaudando.
## CONTENUTO DEI CAMPI
 :  : FLD T$CQAA **Obbligatorietà certificato di qualità**
Richiede sul prossimo lotto obbligatoriamente il certificato di qualità del fornitore
 :  : FLD T$CQAB **Obbligatorietà lotto di derivazione**
Richiede sul prossimo lotto obbligatoriamente la dichiarazione del lotto di derivazione (es. Lotto di Colata ) o del lotto di materia prima utilizzata per la costruzione del particolare in fornitura.
 :  : FLD T$CQAC **Obbligatorietà lotto fornitore**
Richiede sul prossimo lotto obbligatoriamente la dichiarazione del numero di lotto del particolare in fornitura.
 :  : FLD T$CQAD **Richiesta Audit Prodotto**
Richiede sul prossimo lotto obbligatoriamente la effettuazione di un AUDIT di PRODOTTO. In questo caso, all'entrata del lotto il sistema pretenderà la dichiarazione nella GESTIONE AUDIT dei risultati dell'AUDIT effettuato.
 :  : FLD T$CQAE **Blinking Descrizione**
Se posto a 'X' esegue il lampeggio della richiesta in fase di entrata del prossimo lotto.
