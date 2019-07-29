# V5H  -  TIPO PAGAMENTO  -
## OBIETTIVO
Definire le modalità di gestione degli anticipi e dei loro recuperi.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM __Tipo Riga Anticipo__
E' il tipo riga anticipo deve esistere nella tabella V5B
 :  : FLD T$DESC __Descrizione__
Riporta la descrizione del tipo riga anticipo modificabile
 :  : FLD T$V5HA __SS T.riga rec. Or.__
Indica il subsettore che contiene il tipo riga di recupero acconto da inserire
nell'ordine.
Il campo è obbligatorio.
 :  : FLD T$V5HB __Tipo riga rec. Or.__
Indica il tipo riga che verrà utilizzato per inserire il recupero acconto
nell'ordine.
Il campo è obbligatorio.
 :  : FLD T$V5HC __Recupero Propor.(SV)__
Indica se il recupero deve avvenire in proporzione all'acconto, se non
valorizzato verrà recuperato tutto il recuperabile fino ad azzerare la bolla
**NB** :  Ancora in sviluppo
 :  : FLD T$V5HD __Cod. Oggetto Rec.Or.__
Indica il codice oggetto che verrà inserito nella riga di recupero acconto
nell'ordine, deve essere un elemento della tabella V5S.
Il campo è obbligatorio.
 :  : FLD T$V5HE __Suff. pgm controllo__
Se impostato in questo campo il valore x, verrà eseguito il programma
V5FUANT_X, in cui è possibile implementare comportamenti specifici per ogni
funzione del programma.
 :  : FLD T$V5HF __Unità di misura__
Contiene l'unita di misura da riportare sulle righe di recupero acconto
sia dell'ordine che della bolla deve esistere sulla tabella UMS.
Il campo è obbligatorio.
 :  : FLD T$V5HG __SS T.riga rec. De.__
Indica il subsettore che contiene il tipo riga di recupero acconto da inserire
nella bolla.
Il campo è obbligatorio.
 :  : FLD T$V5HH __Tipo riga rec. De.__
Indica il tipo riga che verrà utilizzato per inserire il recupero acconto
nella bolla.
Il campo è obbligatorio.
 :  : FLD T$V5HI __Cod. Oggetto Rec.De.__
Indica il codice oggetto che verrà inserito nella riga di recupero acconto
nella bolla, deve essere un elemento della tabella V5S.
Il campo è obbligatorio.
