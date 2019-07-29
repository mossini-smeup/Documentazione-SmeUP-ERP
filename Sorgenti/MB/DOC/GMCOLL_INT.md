Con la  gestione dei colli è possibile movimentare il materiale attraverso quella che è l'unità minima di movimentazione (confezione), al fine, ad esempio, di  mantenere la rintracciabilità  dei propri lotti di produzione.

Il>numeratore dei colliè definito nella tabella>CRNGM, ed è da inserire nella tabella generale>GM1 : 
 :  : DEC T(ST) K(CRNGM)
 :  : DEC T(TA) P(GM1) K(*) I(Tabella GM1 >>)

 * _1_Tipologia collo, come per tutti gli oggetti di Sme.up anche per il collo si deve definire la Tipologia (Es.MP collo Materia Prima,PF collo Prodotto Finito), con la quale definire comportamenti  diversi nella gestione dei colli o nella movimentazione.
 :  : DEC T(ST) K(GMD)

 * _1_I parametri, anche  ai colli è possibile assegnare una categoria parametri per Tipo collo (sempre all'interno della Tabella GMD).

 * _1_I movimenti, affinché i movimenti prevedano la gestione del collo, è necessario che essi abbiano un Tipo giacenza che preveda la gestione dei contenitori/colli. Fra le varie modalità di interrogazione dei movimenti vi è anche quella per collo.
