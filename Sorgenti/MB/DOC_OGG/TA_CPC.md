# CPC - Personalizzazione Gestione Scarti
 :  : DEC T(ST) K(CPC)
DOCUMENTAZIONE IN FASE DI COMPLETAMENTO
## OBIETTIVO
Definire i valori di default che verranno utilizzati nella generazione delle Non Conformità di Produzione e di Resi clienti.
## CONTENUTO DEI CAMPI
 :  : FLD T$NPDI **Codice Difetto**
Codice del difetto da utilizzare per la Non Conformità (campo controllato nella tabella CQD).
 :  : FLD T$NPCC **Codice Causa**
Codice della causa del difetto da utilizzare per la Non Conformità (campo controllato nella tabella CQC).
 :  : FLD T$NPCA **Codice Accertamento Causa**
Codice del grado di accertamento della causa del  difetto da utilizzare per la Non Conformità (campo controllato nella tabella CQN).
 :  : FLD T$NPNC **Tipo Non Conformità**
Codice del tipo Non conformità da utilizzare per la Non Conformità (campo controllato nella tabella CQE).
 :  : FLD T$NPAT **Tipo Addebito/Accredito**
Codice del tipo di addebito/accredito da utilizzare per la Non Conformità (campo controllato nella tabella CQ*AD).
 :  : FLD T$NPAS **Stato Addebito/Accredito**
Codice dello stato dell'addebito/accredito da utilizzare per la Non Conformità (campo controllato nella tabella CQX).
 :  : FLD T$NPFL **Descrizione Fase Lavoro**
Descrizione della fase di lavoro da utilizzare per la Non Conformità.
 :  : FLD T$NPFC **Descrizione Fase Collaudo**
Descrizione della fase di collaudo da utilizzare per la Non Conformità.
 :  : FLD T$NPCO **Tipo Ente Collaudatore**
Tipo ente collaudatore da utilizzare per la Non Conformità.
 :  : FLD T$NPF1 **Tipo Richiamo**
Opzione utilizzata per richiamare il programma di generazione della Non Conformità. I valori validi sono : 
' '   Visualizzazione (la non conformità viene solo visualizzata).
'2'   Modifica (la non conformità viene presentata in revisione).
'N'   Modifica (la non conformità non viene presentata).
 :  : FLD T$NPF2 **Non Visualizzazione**
Opzione utilizzata per non permettere la visualizzazione della non conformità nella fase di inserimento. I valori validi sono : 
' '   Visualizzazione (la non conformità viene visualizzata).
'N'  No Visualizzazione (la non conformità non viene visualizzata).
 :  : FLD T$NPPG **Pgm Interf. Documenti**
Nome del programma da richiamare per la generazione dei documenti da parte del programma di Gestione Verbali Non Conformità. Deve essere un oggetto presente nel sistema.
