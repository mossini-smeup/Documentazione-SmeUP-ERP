# 07   D9AP_07C - Estrattore Non Conformità
Estrae dall'archivio CQNOCO0F, relativo alle non conformità


_2_Parametri origine

- Data inizio :  determina la data iniziale del documenuto su cui si vuole fare l'estrazione
- Data fine :  determina la data finale del documenuto su cui si vuole fare l'estrazione

_2_Oggetti origine

- Data Documenuto della non conformità
- Articolo non conforme
- Codice Difetto (tabella CQD)
- Lotto
- Codice ente addebito (può essere un cliente, fornitore dipendente o altro)
- Commessa
- Work center (oggetto RÌ)

_2_Oggetti aggiuntivi piatti

- Fase lavoro (oggetto OP)
- Causa difetto (tabella CQC)
- Fase ciclo collaudo (generico)
- Tipo ente addebito (*CNTT)
- Tipo scarto (tabella CQE)
- Azione correttiva (generico)

_2_Valori origine

Sono fissi : 

Qta lotto (N§LOTÌ), solo al cambio lotto; Qta Controllata (N§QCNT); Qta Selezionata (N§QSEL); Qta Non Conforme(N§QNOC); Qta Scartata (N§QSCA); Qta Rilavorata (N§QRLV); Costo Non Conformità (N§VACP); Ricorrenza Difetto(N§QRÌD); Nr. Non Conformita (contatore record)


_2_Parametri dinamici
Se compilato il campo nella D9B relativo ai parametri dinamici prima del lancio si potranno compilare dei filtri su tutti gli oggetti origine e quelli piatti. Compilando il campo l'estrazione viene fatta tenendo conto solo dei record che hanno quel particolare valore dell'oggetto, se non compilati vengono accettati
