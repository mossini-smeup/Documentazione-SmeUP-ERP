# Impostazione chiavi GMRRIM
Le chiavi identificative del documento dipendono dal tipo origine : 


|  Nam="Chiavi indentificative del documento" R="1" |
| 
| .COL Txt="FUNK1 Tipo origine (Nota 1)" LunAut="1" |
| ---|----|
| 
| .COL Txt="K2 Tipo documento (Nota 1)" LunAut="1" |
| 
| .COL Txt="K3 Numero documento (Nota 1)" LunAut="1" |
| 
| .COL Txt="K4 N. Riga / Sequenza (Nota 1)" LunAut="1" |
| 
| .COL Txt="K5 Seq. 2 (Nota 2)" LunAut="1" |
| 
| .COL Txt="K6 Fase (Nota 2)" LunAut="1" |
|  (V2_GMTMO) |   |   |   |   |   | |
|  VP = Versamento produzione | - | Ordine Produzione | - | - | - | |
|  PP = Impegno produzione | - | Ordine Produzione | Seq. 1 | Seq. 2 | - | |
|  PE = Impegno esterno | Tipo Documento | Numero documento | N. Riga | - | Fase (3) | |
|  DO = Documento esterno | Tipo Documento | Numero documento | N. Riga | - | - | |
|  TR = Trasferimento tra aree | - | - | - | - | - | |
| 

**Nota (1)**, Campi validi per ordine e impegno
**Nota (2)**, Campi validi solo per impegno
**Nota (3)**, la fase è significativa solo nel caso di un impegno esterno, per individuare l'oggetto articolo/fase, che è gestito solo in questo ambito

La gestione di queste key è a cura della routine £GMK.

A tutte si aggiunge in £FUN16 il codice dell'articolo (serve per gli impegni), viene trattato solo se PP/PE nella £GMR, nei PGM specifici la key è completa.
