# OBIETTIVO
Questo servizio fornisce le funzionalità necessarie alla modifica da LOOC.up di documentazione SME.u

# FUNZIONI/METODI
## Editing di un documento (chiamata con *EDTLET nel programma)
...
DA VERIFICARE
...
Questa funzione consente di visualizzare (metodo VIS) o modificare (metodo MOD) un documento.
A seconda del tipo di documentazione trattata (passata nell'oggetto 1) sono necessari diversi parame
 -**NOTE** (Oggetto 1 di tipo TANSC) :  i primi 5 oggetti formano la chiave delle note, quindi : 
   C$TIPC - Contenitore note (TANSC)
   C$KYC1 - Chiave 1 (**)
   C$KYC2 - Chiave 2 (**)
   C$KYC3 - Chiave 3 (**)
   C$TIPI - Tipo nota (TANSI)
 -**MEMBRO** (Oggetto 1 di tipo MB) :  nel secondo oggetto si può specificare opzionalmente la libre
 -**DOCUMENTI PER OGGETTO** (Oggetto 1 **) JADOCU, FARE
 -**DOC. PGM?** è gestita dal 29?


 :  : PRO.SER Cod="*FREE.1" Tit="Solo alcuni metodi documentati. " Fun="F(EXB;JATRE_29C;*FREE)"

 :  : PRO.SER Cod="DOC.VIS.2" Tit="Editing di un documento. Visualizza" Fun="F(EDT;JATRE_29C;DOC.VIS) 1(MB;;-(O;;MB;Membro))"

 :  : PRO.SER Cod="DOC.MOD.3" Tit="Editing di un documento. Modifica" Fun="F(HTM;JATRE_29C;DOC.MOD)" Ref="DOC.VIS.2"

 :  : PRO.SER Cod="OGG.MBR.4" Tit="Albero degli oggetti in un doc. Membri referenziati" Fun="F(TRE;JATRE_29C;OGG.MBR) 1(MB;;-(O;;MB;Membro)) P()"

 :  : PRO.SER Cod="OGG.OTH.5" Tit="Albero degli oggetti in un doc. Altri oggetti" Fun="F(TRE;JATRE_29C;OGG.OTH)" Ref="OGG.MBR.4"

