# CQ3 - Definizione calcolo costo
 :  : DEC T(ST) K(CQ3)
## OBIETTIVO
Definire quali componenti di costo devono rientrare nella valorizzazione della non conformità. Tali componenti vengono ricercati nella gestione Costi del GESTIONALE.
## CONTENUTO DEI CAMPI
 :  : FLD T$PMAT **Primo materiale**
Costo Primo Materiale. Questo campo può assumere i valori : 
' '  Non viene considerato tale costo nella composizione del costo totale
'X'  Viene considerato come addendo della somma totale del costo della non conformità anche tale costo.
 :  : FLD T$DMAT **Diretto materiale**
Costo Diretto Materiale. Questo campo può assumere i valori : 
' '  Non viene considerato tale costo nella composizione del costo totale
'X'  Viene considerato come addendo della somma totale del costo della non conformità anche tale costo.
 :  : FLD T$PEST **Primo esterno**
Costo Primo Esterno. Questo campo può assumere i valori : 
' '  Non viene considerato tale costo nella composizione del costo totale
'X'  Viene considerato come addendo della somma totale del costo della non conformità anche tale costo.
 :  : FLD T$DEST **Diretto esterno**
Costo Diretto Esterno. Questo campo può assumere i valori : 
' '  Non viene considerato tale costo nella composizione del costo totale
'X'  Viene considerato come addendo della somma totale del costo della non conformità anche tale costo.
 :  : FLD T$PLAV **Primo lavorazione**
Costo Primo Lavorazione. Questo campo può assumere i valori : 
' '  Non viene considerato tale costo nella composizione del costo totale
'X'  Viene considerato come addendo della somma totale del costo della non conformità anche tale costo.
 :  : FLD T$DLAV **Diretto lavorazione**
Costo Diretto Lavorazione. Questo campo può assumere i valori : 
' '  Non viene considerato tale costo nella composizione del costo totale
'X'  Viene considerato come addendo della somma totale del costo della non conformità anche tale costo.
 :  : FLD T$PMAC **Primo macchina**
Costo Primo Macchina. Questo campo può assumere i valori : 
' '  Non viene considerato tale costo nella composizione del costo totale
'X'  Viene considerato come addendo della somma totale del costo della non conformità anche tale costo.
 :  : FLD T$DMAC **Diretto Macchina**
Costo Diretto Macchina. Questo campo può assumere i valori : 
' '  Non viene considerato tale costo nella composizione del costo totale
'X'  Viene considerato come addendo della somma totale del costo della non conformità anche tale costo.
 :  : FLD T$INDU **Costo Industriale**
Costo Industriale. Questo campo può assumere i valori : 
' '  Non viene considerato.
'X'  Viene considerato tale costo come costo della non conformità. In questo caso elimina dalla somma i costi PRIMI e DIRETTI perchè già contenuti.
 :  : FLD T$GENE **Costo Generale**
Costo Generale. Questo campo può assumere i valori : 
' '  Non viene considerato.
'X'  Viene considerato tale costo come costo della non conformità. In questo caso elimina dalla somma i costi PRIMI, DIRETTI, INDUSTRIALE perché già contenuti.
 :  : FLD T$FINA **Prezzo finale**
Prezzo Finale. Questo campo può assumere i valori : 
' '  Non viene considerato.
'X'  Viene considerato tale costo come costo della non conformità. In questo caso elimina dalla somma i costi
PRIMI, DIRETTI, INDUSTRIALE, GENERALE perchè già contenuti.
 :  : FLD T$PRFA **Prezzo Fatturato**
Prezzo Fatturato. Questo campo può assumere i valori : 
' '  Non viene considerato.
'X'  Viene considerato tale costo come costo della non conformità.
 :  : FLD T$RIDU **Riduzione % Prezzo**
Prezzo percentuale del prezzo calcolato per la non conformità.
È un campo numerico che serve per ridurre di una certa percentuale il costo precedentemente calcolato.
