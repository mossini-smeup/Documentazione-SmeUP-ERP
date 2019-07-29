# D5O - Temi cose oggetto
 :  : DEC T(ST) K(D5O)
## OBIETTIVO
Determinare la chiave del D5COSO e il significato dei valori.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
Ha lunghezza massima di 3 caratteri.
 :  : FLD T$DESC Descrizione
 :  : FLD T$D5OA **Codice 1/2/3 e parametro 1/2/3**
Nei campi Codice 1/2/3 e parametro 1/2/3, è possibile specificare delle ulteriori chiavi in cui si sviluppa il tema (oltre al codice primario definito dal contesto), specificando il tipo/parametro dell'oggetto che si vuole aggiungere.
Se, per esempio, si volesse differenziare il contesto AR anche per tipo costo, bisognerebbe aggiungere in Codice 1 'TA' e in Parametro codice 1 'TCO', indicando così che il codice 1 del tema sarà un elemento della tabella TCO dei tipi costo.
 :  : FLD T$D5O1.T$D5OA Codice 1
 :  : FLD T$D5O2.T$D5OA Codice 2
 :  : FLD T$D5O3.T$D5OA Codice 3
 :  : FLD T$D5OB.T$D5OA Parametro codice 2
 :  : FLD T$D5OC.T$D5OA Parametro codice 3
 :  : FLD T$D5OF **Suffisso pgm specifico**
Normalmente, il significato dei valori del tema viene specificato tramite gli elementi di un sottosettore della tabella IGI. È possibile però "simulare" gli elementi della IGI e il loro relativo calcolo tramite un programma RPG, denominato D5CO_xx dove xx è un suffisso libero (Ex pgm D5CO_A1). Nella libreria standard sono presenti vari pgm di esempio.
 :  : FLD T$D5OD **S/S indici**
Specifica il sottosettore della tabella IGI nel quale sono presenti gli elementi che caratterizzano i valori del tema.
Il campo precedente (suffisso pgm specifico) deve essere vuoto.
 :  : FLD T$D5OE **Data/periodo**
Valori possibili : 
- D :  il tema si sviluppa per data.
- P :  il tema si sviluppa per periodo (elemento della tabella PER).
- blanks :  il tema non si sviluppa ulteriormente.
 :  : FLD T$D5OG **Tipo periodo**
Se in data/periodo è stato specificato P (tema che si sviluppa per periodo), è possibile in questo campo definire anche il tipo periodo (elemento della tabella *CNTT).
Questa opzione è controllata solo nei programmi inerenti i costi per oggetto.
 :  : FLD T$D5OH **Punti sep./decimali**
È possibile specificare il numero di punti separatori (max. 4) e di decimali (max. 6) da utilizzare nella visualizzazione del record del D5COSO. Tutti i valori utilizzeranno questa impostazione, a meno che non ne venga specificata una diversa nel singolo elemento della tabella IGI. Se non viene specificato nulla, vengono assunti 2 punti separatori e 2 decimali.
