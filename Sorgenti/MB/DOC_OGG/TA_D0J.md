# D0J - Fonti totaliz.costo eventi
 :  : DEC T(ST) K(D0J)
## OBIETTIVO
Questa tabella serve per definire le fonti per la totalizzazione del costo di un articolo.
## UTILIZZO
L'elemento definisce una fonte.
Le fonti attualmente gestite sono :  Movimenti, Documenti, Ordini produzione e lotti.
Oltre a definire l'origine la fonte ne detemina le caratteistiche : 
* l'azione che indica se agisce su quantità, valore o entrambi;
* il segno che indica se agisce in modo positivo o negativo nella totalizzazione.
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC DESCRIZIONE
Si inserisce la descrizione della fonte.
 :  : FLD T$D0JA **TIPO FONTE**
Indica l'origine della fonte.
Può assumere i seguenti valori
1 = Movimenti                                                          lcolo : 
2 = Documenti riga
3 = Ordine produzione
4 = Lotti
 :  : FLD T$D0JB **KEY**
Indica il campo dell'evento con cui sarà letta la tabella.
Per i movimenti è la causale di tranzazione;
Per i documenti è tipo documento, modello documento e tipo riga;
Per gli ordini di produzione è il tipo ordine : 
Per i lotti è il tipo lotto.
 :  : FLD T$D0JC **PARAMETRO FONTE**
E' un parametro che consente di specificare la lettura di un evento.
Per i movimenti non è gestito
Per i documenti definisce la data di competenza dell'evento.
Per gli ordini di produzione definisce la data di competenza dell'evento.
Per i lotti definisce la data di competenza dell'evento.
 :  : FLD T$D0JD **AZIONE FONTE**
Può contenere i seguenti valori : 
Q = Quantità
V = Valore
T = Quantità e valore
Indica l'azione della fonte sulla totalizzazione del costo.
Se quantità totalizza solo la quantità dell'evento, se vaore totalizza solo il valore dell'evento, se entrambi totalizza sia la quantità che il valore.
 :  : FLD T$D0JE **SEGNO FONTE**
Può contenere i seguenti valori : 
N = Negativo
P = Positivo
Indica il segno con cui agisce la fonte sulla totalizzazione del costo.
Se positivo viene sommato, se negativo viene sottratto.
 :  : FLD T$D0JF **INVERSIONE DISTINTA LLC**
Può contenere i seguenti valori : 
  = No
1 = Si
E' possibile attivando questo campo fare in modo che quando si crea
la distinta per il calcolo low-level code si inverta assieme e componente
