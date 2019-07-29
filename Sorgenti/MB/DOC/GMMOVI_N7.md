# Movimenti collegati a Ordini-Documenti/Lavorazione

|  Nam="Movimenti collegati PP / V5 (C/lavoro)" |
| 
| .COL |
| ---|----|
| 
| .COL Txt="Tipo Movimento" LunAut="1" A="C" |
| 
| .COL Txt="Operazione" LunAut="1" A="C" |
| 
| .COL Txt="Numero ordine 2" LunAut="1" A="L" |
|  **Spedizione in C/Lavoro** | DO | Fase di V5 | blank |
|  **Ricevimento da C/Lavoro (1)** | DO | Fase di V5 | Lotto di V5 se oggetto in campo lotto è Ordine |
|  **Prelievo componenti di C/Lavoro** | PE | Fase di V5 | Ordine origine di P5IMPE se attivo collegamento prelievi V5 > P5 e se fase = blank |
|  **Prelievo produzione** | PP | blank | blank |
| 

(1) Se non attivo il collegamento al versamento V5 > P5 nel flag 1 dei movimenti è impostato "1"
