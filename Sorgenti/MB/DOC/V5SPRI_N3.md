# Deviatore stampa bolle/fatture
è stato realizzato un deviatore V5BOFA, PGM funizzato, che riceve la £V5PDS e quindi il documento che sta trattando.
Il suo scopo è di passare (polimorficamente) alla stampa specifica del documento, senza che l'utente debba sceglierla esplicitamente o il sistemista debba impostare più flussi : 
 * se il documento è un'entrata merci (riconosciuta dal secondo carattere = "E" del tipo modello) NON fa niente (si può mettere qui la stampa BEM come personalizzazione)
 * se il documento è una bolla (flag 18 di testata = blank) lancia la stampa bolla
 * se il documento è una fattura accompagnatoria (flag 18 di testata = 9) lancia la stampa della fattura accompagnatoria
Il fatto che sia una stampa/prestampa/ristampa viene impostato nella funzione di questo passo.
