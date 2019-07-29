# SF1 - Parametri schedulazione fine
 :  : DEC T(ST) K(SF1)
## OBIETTIVO
Riunire tutte le condizioni di impostazione ambiente per la schedulazione fine.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
Valore fisso = *
 :  : FLD T$DESC Descrizione
 :  : FLD T$CATR __Causale attrezzaggio__
Viene controllata sulla tabella CAP ed utilizzata dall'azione AT.
 :  : FLD T$GEFC __Gestione efficienza centri di lavoro__
Se contiene 'S', nei calcoli di schedulazione si tiene conto dell'efficienza del centro di lavoro :  il tempo totale richiesto per completare l'operazione ???.....
 :  : FLD T$DGCL __Differenza giorni Calendario/Lavorativi__
Se contiene 'C', la differenza giorni tra due date viene espressa in giorni di calendario, altrimenti viene espressa in giorni lavorativi.
 :  : FLD T$SDRI __Stampa disponibilità risorsa__
Se non è in bianco, la stampa grafica della schedulazione viene preceduta dalla stampa della disponibilità della risorsa.
