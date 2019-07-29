# CQD - Tabella difetti
 :  : DEC T(ST) K(CQD)
## OBIETTIVO
Raccogliere e codificare le difettosità rilevate.
Assegnare un moltiplicatore di gravità al parametro di demerito del difetto.
## CONTENUTO DEI CAMPI
 :  : FLD T$CLDI **Classe Difetto**
Questo campo è controllato in tabella CQF (Classi Difetto).
Rappresenta "l'importanza" del difetto.
 :  : FLD T$GRDI **Gravità difetto**
Campo che differenzia, a parità di difetto, la gravità che questo assume nell'ambito del prodotto in esame. Tale valore viene proposto nel campo 'Gravità  : ' del modulo 'Gestione Non Conformità.
Per ogni classe di difetto, considerato che ogni difetto può presentare un diverso grado di gravità, è opportuno considerare una scala di livelli di gravità da 0 a 9 come da seguenti indicazioni : 
LIVELLO DI GRAVITA' 9
identifica il difetto che risulta al livello superiore della rispettiva classe.
LIVELLO DI GRAVITA' 1
identifica il difetto che è collocabile in una determinata classe, ma che, dal punto di vista gravità, vi rientra appena.
_9_Esempio : 
L'insufficiente gioco nell'accoppiamento, sempre in presa con :  spinotto, cuscinetti, rasamenti, ecc. è un difetto da considerarsi critico (Classe Difetto=Critica).
Se l'insufficienza di gioco è tale da comportare grippaggi nel primo periodo di funzionamento con possibili danneggiamenti al cambio, il difetto è da considerarsi ad un livello di gravità 9.
Se l'insufficienza di gioco può portare unicamente a problemi di indurimenti, rumorosità, usura precoce,ecc., ma non compromette la funzionalità del cambio, il difetto è da considerarsi ad un livello di gravità 1.
 :  : FLD T$RCL1 **Riclassifica 1/2/3**
Campo controllato dalla tabella 'CQ*RD' (Riclassifica Difetti).
Viene utilizzato nelle analisi statistiche.
 :  : FLD T$RCL2.T$RCL1 **Riclassifica 1/2/3**
 :  : FLD T$RCL3.T$RCL1 **Riclassifica 1/2/3**
 :  : FLD T$SCAU **Sottosettore Cause**
Campo controllato dal SubSettore della tabella 'CQC' (Cause Difetti).
Condizioni Possibili : 
- 'aa' Permette l'assegnazione di più cause ad un difetto.
Viene utilizzato nel programma 'Gestione Non Conformità proponendo, a fronte di un difetto scelto, una serie di cause specifiche contenute nel SubSettore collegato a questo campo.
- '  ' Se tale campo è lasciato 'blank' allora il programma si collega direttamente alla tabella 'CQC' generale.
 :  : FLD T$CQDA **Non ammesso esito conforme**
Se previsto dalla tabella CR1, non accetta esito con tipo accettazione conforme nella dichiarazione di collaudo
