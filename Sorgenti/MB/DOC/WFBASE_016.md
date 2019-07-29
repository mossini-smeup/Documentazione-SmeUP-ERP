# Files fisici
WFORTE0F, WFIMPE0F, WFATTI0F, WFHIST0F, WFPROM0F e relativi logici

# Files sorgente
Definizioni funzionali dei processi : 
   :  : DEC T(OJ) P(*FILE) K(SCP_WFA)
Istruzioni da presentare passo-passo agli utenti che eseguono i workflow : 
   :  : DEC T(OJ) P(*FILE) K(DOC_WFA)

# Tabelle

Si ricorda che è possibile importare dal modello tutte le tabelle richieste.

## Tabelle specifiche

   :  : DEC T(ST) K(WFA)
   :  : DEC T(ST) K(WFW)
   :  : DEC T(ST) K(WFI)
   :  : DEC T(ST) K(WF1)
   :  : DEC T(ST) K(WFS)
   :  : DEC T(ST) K(WFP)

## Impostazioni

Tutti gli utenti che partecipano a workflow devono essere codificati in B£U : 
   :  : DEC T(ST) K(B£U)

Devono essere compilati applicazione (WF in B£A) e modulo (WFBASE in B£AMO) : 
   :  : DEC T(TA) P(B£A) K(WF)
   :  : DEC T(TA) P(B£AMO) K(WFBASE)


## Oggetti

In CN*TT devono essere codificati F1, F2, F3, F4, F5, F6 : 
   :  : DEC T(TA) P(*CNTT) K(F1)
   :  : DEC T(TA) P(*CNTT) K(F2)
   :  : DEC T(TA) P(*CNTT) K(F3)
   :  : DEC T(TA) P(*CNTT) K(F4)
   :  : DEC T(TA) P(*CNTT) K(F5)
   :  : DEC T(TA) P(*CNTT) K(F6)

Devono essere costruiti gli oav di F1, F2, F4.


## Note

Contenitori standard :  WF1, WF : 
   :  : DEC T(TA) P(NSC) K(WF1)
   :  : DEC T(TA) P(NSC) K(WF2)

Relative NSIWF, NSIW2.


## Numeratori

In CRNWF vanno definiti OG.F1, OG.F2, OG.F3, OG.F4 : 
   :  : DEC T(TA) P(CRNWF) K(OG.F1)
   :  : DEC T(TA) P(CRNWF) K(OG.F2)
   :  : DEC T(TA) P(CRNWF) K(OG.F3)
   :  : DEC T(TA) P(CRNWF) K(OG.F4)


## Classi di autorizzazione

Indispensabile la classe WFORTE in B£P e relativa B£SWF : 
   :  : DEC T(TA) P(B£P) K(WFORTE)

Classi singole per autorizzazioni su transizioni dei processi (opzionali)


# Attivazione promemoria

Per attivare i promemoria riferirsi al documento : 
- [Promemoria](Sorgenti/MB/DOC/WFBASE_039)
