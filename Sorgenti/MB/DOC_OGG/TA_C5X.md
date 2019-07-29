# C5X - Tipi Sollecito
 :  : DEC T(ST) K(C5X)
## OBIETTIVO
Definire i caratteri generali dei tipi di sollecito gestiti nel sistema.
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC **Descrizione**
Contiene la descrizione di questo specifico tipo di sollecito.
 :  : FLD T$C5XA **Tipo sollecito successivo**
Indica qule sarà il tipo di sollecito successivo.
 :  : FLD T$C5XB **Intervallo in Giorni**
Indica dopo quanti giorni scatterà il tipo sollecito successivo partendo dalla data del sollecito precedente
 :  : FLD T$C5XC **Livello Iniziale**
Indica il livello con cui verrà inizializzato il sollecito
 :  : FLD T$C5XE **Stampa numero pagina**
Indica se nella lettera dovrà essere indicato il numero di pagina
 :  : FLD T$C5XG **Riapre per residuo**
Indica se dovrà essere riaperto il sollecito se dopo un pagamento esiste un residuo
