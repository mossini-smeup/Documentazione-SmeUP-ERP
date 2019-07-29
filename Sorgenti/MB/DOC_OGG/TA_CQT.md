# CQT - Tipo di misura
 :  : DEC T(ST) K(CQT)
## OBIETTIVO
Definire per il tipo di misura l'intestazione dei valori riportati alla fase del ciclo.
Definire per il tipo di misura l'intestazione dei valori da rilevare nella dichiarazione di collaudo.
Associare al tipo di misura un piano di campionamento di proposto.
## CONTENUTO DEI CAMPI
 :  : FLD T$CQP **Piano di campionamento**
Valore controllato dalla tabella 'CQP' (Piano controllo qualità).
È il piano di campionamento che viene normalmente proposto per il tipo di misura della caratteristica nella fase di impostazione del ciclo di collaudo.
 :  : FLD T$LQP **Livello P.d.C.**
Valore controllato dalla tabella 'CQP' (Piano controllo qualità).
È il livello del piano di campionamento che viene normalmente proposto per il tipo di misura della caratteristica nella fase di impostazione del ciclo di collaudo.
 :  : FLD T$CON1 **Condizione 1/4**
Campo controllato dalla tabella 'CQK' (Definizione dei rilievi). È la descrizione dei campi per i quali si inseriranno nel ciclo di collaudo i valori indicati dalle specifiche costruttive.
 :  : FLD T$SIV1 **Controllo condizione 1/4**
Campo di controllo : 
' '  inserimento facoltativo del valore nella fase del ciclo di collaudo dell'articolo.
'O'  inserimento obbligatorio del valore nella fase del ciclo di collaudo dell'articolo.
 :  : FLD T$CEAU **Sogg.certif.autom.**
Campo libero
 :  : FLD T$NUCA **Num.per.cert.autom.**
Campo libero
 :  : FLD T§SIV1 **Campo rilevato 1/4**
Campo controllato dalla tabella 'CQK' (Definizione dei rilievi). È la descrizione dei campi per i quali si inseriranno, nella fase di dichiarazione dei controlli e collaudi sul lotto, i valori rilevati per quella fase di collaudo descritta nel ciclo. Se il valore richiesto è una sintesi di più valori (es. Media di una popolazione di
misure), il programma, in funzione della descrizione scelta, utilizzerà l'algoritmo di calcolo definito nella tabella 'CQK'.
 :  : FLD T§CON1 **Controllo campo 1/4**
Campo di controllo : 
' '  dichiarazione facoltativa del valore nella registrazione del collaudo, alla fase del ciclo di collaudo dell'articolo.
'O'  dichiarazione obbligatoria del valore nella registrazione del collaudo, alla fase del ciclo di collaudo dell'articolo.
 :  : FLD T§TST1 **Test su rilievo**
Indica se il campo rilevato deve subire un controllo da parte dei valori di riferimento : 
_9_Esempio :  Dimensione nominale, massima e minima sono i valori di riferimento; se come valore del campo rilevato ho la media potrei decidere che il valore della media è a specifica se soddisfa i valori di riferimento. In questo caso metterò una X nel campo.
