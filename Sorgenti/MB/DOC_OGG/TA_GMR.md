# GMR - Area
## OBIETTIVO
Identifica un'area di magazzino, fisica o logica, per la quale si vuol tenere, nel sistema, una giacenza.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
Indica il codice dell'area.
 :  : FLD T$DESC Descrizione
 :  : FLD T$GMRA __Area esterna__
Se impostato, l'area è esterna all'azienda, quindi la sua giacenza non contibuirà al computo della giacenza complessiva in azienda.
 :  : FLD T$GMRB __Proprietà di terzi__
Se impostato, l'area contiene materiale non di proprietà dell'azienda, e quindi la sua giacenza non contibuirà al computo della giacenza complessiva di proprietà dell'azienda.
 :  : FLD T$GMRC __Gruppo Area__
È un elemento della tabella GM*/GA. Definisce un'eventuale aggregazione a livello superiore dell'area qui definita.
 :  : FLD T$GMRD __Trattamento Lifo__
Esiste la possibilità di gestire la sintesi annuale Lifo non dai movimenti ma calcolando la giacenza alla data richiesta (normalmente fine anno). In questo caso, il programma considera l'area (e non i movimenti) Fiscale.
**ATTENZIONE** :  in questo caso non è gestita la quantità entrata e uscita ma la differenza tra la giacenza calcolata e quella dell'esercizio precedente. Inoltre non è possibile gestire il tipo area 'S' se si gestisce il magazzino fiscale con il raggruppamento (vedi tabella GM3).
