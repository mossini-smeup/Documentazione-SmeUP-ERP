# BRR - Tipo risorsa
## OBIETTIVI
-    Caratterizzare la tipologia delle risorse.
## INTRODUZIONE
Per ogni tipo risorsa si può definire la tipologia di risorsa cui appartiene (esempio :  i centri di lavoro appartengono ai centri di costo).
## CONTENUTO DEI CAMPI
 :  : FLD T$BRRA __Tipo e parametro risorsa appartenenza__
Tipo e parametro definiscono l'oggetto (elemento della tabella *CN/TT eventualmente tipizzato) che rappresenta il tipo risorsa a cui si può collegare il tipo trattato.
 :  : FLD T$BRRB.T$BRRA Tipo e parametro risorsa appartenenza
 :  : FLD T$BRR1 __Inser.facoltativo__
Se impostato, in inserimento delle risorse di questo tipo, la risorsa di appartenenza è facoltativa. Se lasciato in bianco, è invece obbligatoria.
 :  : FLD T$BRRC __Tipo risorsa dipendente master__
Un tipo risorsa può essere presente, come risorsa di appartenenza, in più di un tipo risorsa.
Ad esempio :  sia il tipo risorsa MAC sia il tipo risorsa OPE possono avere il valore RI/CDL nel campo risorsa di appartenenza.
In questo campo si imposta il tipo di risorsa dipendente master, sulla quale ci si basa, ad esempio, per determinare se la risorsa ha risorse dipendenti.
Nel caso dell'esempio, nell'elemento di tabella CDL, si deve impostare il valore MAC in questo campo.
Questo legame è significativo quando i legami di appartenenza sono tra oggetti di tipo 'RI'.
 :  : FLD T$BRRD __Mag.obbligatorio__
Se impostato questo campo, e l'ambiente è multiplant, è obbligatorio inserire il magazzino nelle risorse di questo tipo.
 :  : FLD T$BRRE __Suff.Parz.Lista__
Il campo rappresenta il suffisso del programma BRRI01L_x  (dove x = al contenuto del campo della tabella).
Valorizzando il campo si abilita il lancio del programma in oggetto che consente di effettuare parzializzazioni
specifiche nella lista delle risorse del tipo in esame (BRRI01L)
 :  : FLD T$BRRF __Natura risorsa__
Se una risorsa è di tipo previsto (presente tra i valori fissi V2 N_BRR) si imposta il relativo elemento.
In caso contrario questo campo va lasciato vuoto.
