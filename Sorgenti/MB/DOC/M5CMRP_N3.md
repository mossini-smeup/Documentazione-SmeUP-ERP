# Trattamento segno

La valorizzazione della quantità fonte (QF) nel record di consiglio (M5CONS) è soggetta alle seguenti considerazioni.
Per le fonti rilasciate l'origine è l'analisi disponibilità che ritorna QF rispettivamente nel campo quantità entrata (QE) e quantità uscita (QU) in funzione del segno fonte di tabella  ST.
Se il segno della quantità è concorde con il segno della fonte, QE e QU sono positive.
Se invece è discorde , esse sono negative.
Ad esempio, una giacenza negativa (ST='+') ha una QE negativa, mentre un recupero (ST='-') ha una QU negativa.

All'atto della scrittura del consiglio, a partire dall'analisi disponibilità, vengono valorizzati, oltre a QF, anche i campi segno fonte (SF) e segno originale fonte (SO), con il seguente criterio : 
Entrata  (ST='+' QE>0)
QF= QE
SF='+'
SO='+'
Entrata negativa (ST='+' QE<0)
QF= -QE
SF='-'
SO='+'
Uscita (ST='-' QU>0)
QF= QU
SF='-'
SO='-'
Uscita negativa (ST='-' QU<0)
QF= -QU
SF='+'
SO='-'

I consigli scritti direttamente sono gli ordini e gli impegni pianificati, di quantità QP.
Gli oridni piaificati hanno obbligatoriamente quantità e segno positivo, e quindi vengono scritti nel seguente modo : 
QF= QP
SF='+'
SO='+'
Gli impegni pianificati effettivi sono scritti nel seguente modo (QP è il valore assoluto dell'impegno o del recupero) : 
QF= QP
SF='-'
SO='-'
Gli impegni pianificati negativi (recuperi)  sono scritti nel seguente modo : 
QF= -QP
SF='-'
SO='-'
Quest'ultimo è l'unico caso in cui la quantità fonte, nell'archivio, è negativa. Il motivo è che gli impegni pianificati vengono scritti direttamente nell'archivio consigli, e non passano, in qeusta fase, dall'analisi disponibilità, che corregge i segni come esposto in precedenza.

_Nota tecnica
Nell'inizializzazione della pianifcazione di ogni articolo, la scansione della disponibilità ha diue scopi :  il caricameneto delle schiere, che tratta tutte le fonti (compresi gli impegni pianificati che quindi, se negativii, vengono trattati come coperture), e la scrittura dell'archivio consigli, che viene fatta solo per le fonti rilasciate (gli impegni pianificati sono stati già scrtitti, all'atto della scrittura dell'ordine pianificato del livello superiore).

Nella matrice di presentazione MRP si costruiscono le seguenti colonne, a partire del record del consiglio :  quantità fonte, quantità entrata e quantità uscita. calcolate nel seguente modo : 
Quantità fonte = quantità fonte dell'archivio, invertita se il segno fonte è diverso dal segno originale (flag 11), in pratica se il suo segno è discorde dalla natura della fonte stessa (giacenze negative, recuperi ...)
Quantità entrata / uscita
Se la quantità fonte dell'archivio è negativa la si inverte e si inverte il segno fonte
Quantità entrata = quantità fonte se il segno fonte è '+'
Quantità uscita =  quantità fonte se il segno fonte è '-'

NB :  in realtà, le considerazioni precedenti, in caso di fonte di origine "PN", vale a dire ordini pianificati, vengono fatte sulla quantità suggerimento (che è sempre positivia, sia come valotre sia come sengo fonte e segno originale).







