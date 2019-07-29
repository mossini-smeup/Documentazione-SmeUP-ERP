# V57 - Condizioni di confezionamento
 :  : DEC T(ST) K(V57)
## OBIETTIVO
Definisce le modalità con cui si esegue la gestione e l'interrogazione dei parametri di confezionamento Articolo/Ente.
## CONTENUTO DEI CAMPI
 :  : FLD T$V57A **Cap. Note articolo**
Permette di visualizzare un particolare capitolo note articolo in "Interrogazione dati di confezionamento".
In caso non venga definito, si assume il capitolo utilizzato in anagrafica articoli.
 :  : FLD T$V57B **Cap. Note Ente**
Permette di visualizzare un particolare capitolo note ente in "Interrogazione dati di confezionamento".
In caso non venga definito, si assume il capitolo utilizzato in anagrafica enti.
 :  : FLD T$V57C **Cap. Note Ente/Articolo**
Permette di visualizzare un particolare capitolo note Articolo/Ente in "Interrogazione dati di confezionamento".
In caso non venga definito, si assume il capitolo utilizzato in anagrafica Ente/Articolo.
 :  : FLD T$V57D **Suff. pgm dati confezionamento**
Se il calcolo dei parametri di confezionamento Articolo/Ente standard non soddisfa le esigenze richieste dal cliente, è possibile inserire un suffisso in questa tabella, affichè il reperimento dei dati venga deviato su questo programma.
Il progamma dovrà chiamarsi :  B£G440_X, dove X indica il suffisso.
Il programma dovrà avere le caratteristiche del programma B£G440.
