_4_Obiettivo         
 Definire quali tabelle sono gestite nell'ambiente minimale

_7_BASE.up - B£      
 >Impostazioni
   :  : DEC T(ST) K(B£1)   I(**Nome azienda / Interfacce     >>)
   :  : DEC T(ST) K(B£2)   I(**Azienda/Divisa/Lingua         >>)
 >Standard da riprendere da modello
   :  : DEC T(ST) K(*CNAV) I(**Attributi video               >>)
   :  : DEC T(ST) K(B£R)   I(**Funzioni cablate              >>)
   :  : DEC T(ST) K(B£SGD) I(**Funzioni cablate              >>)
   :  : DEC T(ST) K(B£T)   I(**Gestita -parametri cablati-   >>)
 >Altre tabelle proposte
Nota :  Determinati elementi di tabella sono presenti in M/SMEMOD
altri sono presenti nell'ambiente di lavoro.
Si assume che quelli di SMEMOD abbiano valenza generale.

Nell'elenco tabelle seguente c'è una nota che serve come guida
nell'avanzamento dell'attività e ha questi significati : 
Fatta :        La tabella è stata presa in esame e completata
Gestita :      --------
Da gestire :   Deve  essere completata

   :  : DEC T(ST) K(AEB)   I(**Fatta       Dati di esempio   >>)
   :  : DEC T(ST) K(AGE)   I(**Fatta       Dati di esempio   >>)
   :  : DEC T(ST) K(AZI)   I(**Fatta       Gestita Az. = '01'>>)
   :  : DEC T(ST) K(B£G)   I(**Gestita                       >>)
   :  : DEC T(ST) K(B£H)   I(**Gestita                       >>)
   :  : DEC T(ST) K(B£J)   I(**Gestita                       >>)
   :  : DEC T(ST) K(B£N)   I(**Gestita                       >>)
   :  : DEC T(ST) K(B£P)   I(**Gestita  Vedi Autorizzazioni  >>)
   :  : DEC T(ST) K(B£Q)   I(**Gestita                       >>)
   :  : DEC T(ST) K(B£W)   I(**Gestita                       >>)
   :  : DEC T(ST) K(B£Y)   I(**Gestita                       >>)
   :  : DEC T(ST) K(B£4)   I(**Gestita  ctr.nuovi elementi   >>)
   :  : DEC T(ST) K(B§D)   I(**Gestita                       >>)
   :  : DEC T(ST) K(B§L)   I(**Gestita  ctr.nuovi elementi   >>)
   :  : DEC T(ST) K(CLS)   I(**Fatta       Dati di esempio   >>)
   :  : DEC T(ST) K(CCO)   I(**Fatta       Dati di esempio   >>)
   :  : DEC T(ST) K(COA)   I(**Da gestire                    >>)
   :  : DEC T(ST) K(CRN)   I(**Fatta                         >>)
   :  : DEC T(ST) K(IVA)   I(**Fatta       Dati di esempio   >>)
   :  : DEC T(ST) K(NSA)   I(**Gestita  parametri cablati    >>)
   :  : DEC T(ST) K(NSC)   I(**Gestita                       >>)
   :  : DEC T(ST) K(NSI)   I(**Gestita                       >>)
   :  : DEC T(ST) K(OLG)   I(**Gestita                       >>)
   :  : DEC T(ST) K(PAG)   I(**Fatta       Dati di esempio   >>)
   :  : DEC T(ST) K(PER)   I(**Gestita                       >>)
   :  : DEC T(ST) K(SPE)   I(**Fatta       Dati di esempio   >>)
   :  : DEC T(ST) K(TCA)   I(**Gestita  parametri cablati    >>)
   :  : DEC T(ST) K(TRG)   I(**Gestita                       >>)
   :  : DEC T(ST) K(UMS)   I(**Gestita                       >>)
   :  : DEC T(ST) K(VAL)   I(**Gestita                       >>)

_7_BREC.up - BR      
 >Impostazioni
   :  : DEC T(ST) K(BR1)   I(**Fatta                         >>)
 >Standard da riprendere da modello
   :  : DEC T(ST) K(BR*)   I(**Gestita  parametri cablati    >>)
   :  : DEC T(ST) K(BR*CF) I(**Fatta       Dati di esempio   >>)
   :  : DEC T(ST) K(BR*TF) I(**Fatta       Dati di esempio   >>)
 >Altre tabelle proposte
   :  : DEC T(ST) K(BRA)   I(**Fatta                         >>)
   :  : DEC T(ST) K(BRB)   I(**Fatta       Dati di esempio   >>)
   :  : DEC T(ST) K(BRD)   I(**Fatta                         >>)
   :  : DEC T(ST) K(BRE)   I(**Fatta                         >>)
   :  : DEC T(ST) K(BRI)   I(**Gestita  ctr. nuovi elementi  >>)
   :  : DEC T(ST) K(BRL)   I(**Fatta                         >>)
   :  : DEC T(ST) K(BRM)   I(**Fatta                         >>)
   :  : DEC T(ST) K(BRP)   I(**Fatta                         >>)
   :  : DEC T(ST) K(BRQ)   I(**Fatta       Dati di esempio   >>)
   :  : DEC T(ST) K(BRR)   I(**Fatta                         >>)
   :  : DEC T(ST) K(BRT)   I(**Fatta                         >>)
   :  : DEC T(ST) K(BRY)   I(**Fatta       Dati di esempio   >>)
   :  : DEC T(ST) K(BRX)   I(**Fatta                         >>)
   :  : DEC T(ST) K(BRZ)   I(**Fatta                         >>)

_7_KEEP.up - C5      
 >Impostazioni
   :  : DEC T(ST) K(C51)   I(**Fatta                         >>)
 >Standard da riprendere da modello
 >Altre tabelle proposte da modello come esempio
   :  : DEC T(ST) K(C5M)   I(**Fatta       Dati di esempio   >>)
   :  : DEC T(ST) K(C5O)   I(**Fatta       Dati di esempio   >>)
   :  : DEC T(ST) K(C5NBA) I(**Fatta       Dati di esempio   >>)
   :  : DEC T(ST) K(C5NCE) I(**Fatta       Dati di esempio   >>)
   :  : DEC T(ST) K(C5B)   I(**Fatta       Dati di esempio   >>)
   :  : DEC T(ST) K(C5E)   I(**Fatta       Dati di esempio   >>)
   :  : DEC T(ST) K(C5L)   I(**Fatta       Dati di esempio   >>)
   :  : DEC T(ST) K(C5R)   I(**Fatta       Dati di esempio   >>)
   :  : DEC T(ST) K(C5V)   I(**Fatta       Dati di esempio   >>)
   :  : DEC T(ST) K(C5D)   I(**Fatta       Dati di esempio   >>)
   :  : DEC T(ST) K(C5G)   I(**Fatta       Dati di esempio   >>)
   :  : DEC T(ST) K(PAG)   I(**Fatta       Dati di esempio   >>)
   :  : DEC T(ST) K(C5P)   I(**Fatta       Dati di esempio   >>)
   :  : DEC T(ST) K(C5T)   I(**Fatta       Dati di esempio   >>)
   :  : DEC T(ST) K(IVA)   I(**Fatta       Dati di esempio   >>)

_7_CLAS.up - C£      
 >Impostazioni
   :  : DEC T(ST) K(C£1)   I(**Fatta                         >>)
 >Standard da riprendere da modello
   :  : DEC T(ST) K(C£*)   I(**Gestita  parametri cablati    >>)
 >Altre tabelle proposte
   :  : DEC T(ST) K(C£E)   I(**Fatta                         >>)
   :  : DEC T(ST) K(C£F)   I(**Fatta  ctr. nuovi elementi    >>)
   :  : DEC T(ST) K(C£G)   I(**Fatta                         >>)
   :  : DEC T(ST) K(C£H)   I(**Fatta                         >>)
   :  : DEC T(ST) K(C£L)   I(**Fatta                         >>)
   :  : DEC T(ST) K(C£V)   I(**Fatta                         >>)

_7_WARE.up - GM      
 >Impostazioni
   :  : DEC T(ST) K(GM1)   I(**Fatta                         >>)
 >Standard da riprendere da modello
   :  : DEC T(ST) K(GM*)   I(**Gestita  parametri cablati    >>)
 >Altre tabelle proposte
   :  : DEC T(ST) K(GMC)   I(**Fatta                         >>)
   :  : DEC T(ST) K(GMF)   I(**Fatta                         >>)
   :  : DEC T(ST) K(GMQ)   I(**Fatta                         >>)
   :  : DEC T(ST) K(GMR)   I(**Fatta                         >>)

_7_MARP.up - M5      
 >Impostazioni
 >Standard da riprendere da modello
   :  : DEC T(ST) K(M5*)   I(**Gestita  parametri cablati    >>)
 >Altre tabelle proposte
   :  : DEC T(ST) K(M5E)   I(**Gestita                       >>)
   :  : DEC T(ST) K(M5F)   I(**Gestita                       >>)

_7_PROD.up - P5      
 >Impostazioni
   :  : DEC T(ST) K(P51)   I(**Fatta                         >>)
 >Standard da riprendere da modello
   :  : DEC T(ST) K(P5*)   I(**Gestita  parametri cablati    >>)
 >Altre tabelle proposte
   :  : DEC T(ST) K(P5I)   I(**Gestita                       >>)
   :  : DEC T(ST) K(P5T)   I(**Gestita                       >>)
  _9_Gestire Parametro 2P2 con max risalita PRO/** indicando GMC versamento

_7_TRAD.up - V5      
 >Impostazioni
 >Standard da riprendere da modello
   :  : DEC T(ST) K(V5*)   I(**Fatta                         >>)
 >Altre tabelle proposte
   :  : DEC T(ST) K(V5A)   I(**Fatta                         >>)
   :  : DEC T(ST) K(V5BDP) I(**Fatta                         >>)
   :  : DEC T(ST) K(V5D)   I(**Fatta                         >>)
   :  : DEC T(ST) K(V5G)   I(**Fatta                         >>)
   :  : DEC T(ST) K(V5L)   I(**Fatta                         >>)
