# D9AP_09C - Estrattore da Viaggi e spedizioni
Estrae dall'archivio V5TRP0F, relativo ai viaggi e spedizioni


_2_Parametri origine

- Tipo viaggio tabella V5T specifica il tipo viaggio su cui si estrae. Chiave del file
- Livello :  se compilato estrae solo i viaggi con il livello indicato
- Tipo data :  si imposta a quale data del viaggio si fa riferimenuto
- Data inizio :  determina l'inizio dell'intervallo di estrazione ed è relativo al tipo data specificato prima
- Data fine determina la fine dell'intervallo di estrazione ed è relativo al tipo data specificato prima

_2_Oggetti origine

- Codice Viaggio (oggetto Vg par Tipo Viaggio)
- Mezzo di trasporto (tabella V5U)
- Livello (tabella B£W00)
- Data (Specificata nei parametri origine)

_2_Oggetti aggiuntivi piatti
Non gestiti in questo tipo di estrazione

_2_Valori origine

- Volume previsto
- Volume effettivo
- Peso Previsto
- Peso Effettivo
- Costo Previsto
- Costo Effettivo
- Numero viaggi

_2_Parametri dinamici
Non gestiti in questo tipo di estrazione
