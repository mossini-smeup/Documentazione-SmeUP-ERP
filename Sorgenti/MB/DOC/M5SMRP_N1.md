# Applicazione cumulata suggerimenti MRP
Non è prevista l'applicazione cumulata con variazione pre/modifica


|  R="99" |
| 
| .COL Txt="Riga" LunAut="1" A="C" |
| ---|----|
| 
| .COL Txt="Livello" LunAut="1" A="C" |
| 
| .COL Txt="Qtà rilasciata" LunAut="1" A="C" |
| 
| .COL Txt="Numero rilascio" LunAut="1" A="C" |
|  Prima | 8  | Sommatoria qtà | Numero documento |
|  Successive | 8  | 0 | Numero documento |
| 


* Si può modificare solo la prima riga (con "MR")
* Si possono vedere anche le righe successive (con "VR")

**Qtà eccedente MRP** (sempre PN/EL)
 - Fonte presente
 - Fonte futura rilasciata
 - Fonte futura pianificata (flag 1 impostato)

Per ogni articolo della pianificazione c'è un solo suggerimento di questo tipo.
