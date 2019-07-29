# D9AP_02C - Estrattore dal D5COSO
Estrae dall'archivio D5COSO0F, relativo ai costi per oggetto (DELT_UP)

_2_Parametri origine

- Tabella D5S dei contesti per oggetto :  determina il contesto di estrazione, il primo oggetto origine dato dal codice dell'elemento di tabella e la chiave del logico di cui farà la scansione. Determina anche l'intestazione e il significato dei valori
- Tabella D5O dei temi cose per oggetto :  determina fino a tre oggetti origine per l'estrazione e serve come chiave per la scansione
- Opzione se fermarsi ai totali o dettagliare quelle voci di costo che si possono esplodere
- Due date di intervallo estrazione

_2_Oggetti origine

- Oggetto 1 :  è determinato dal parametro origine del contesto per oggetto. È ricavato dal codice dell'elemento, e rappresenta l'oggetto principale di caratterizzazione dei costi
- Oggetto 2,3,4 :  è determinato dal parametro origine del tema cose per oggetto. Sono dichiarati nella tabella, fino ad un massimo di tre
- Oggetto 5 :  è il periodo (TA-PER). È fisso e caratterizza il periodo di riferimento
- Oggetto 6 :  è l'oggetto generico che contiene le voci di dettaglio di un valore

_2_Oggetti aggiuntivi piatti

- Tipo Voce dettaglio :  descrive il tipo oggetto generico numero 6


_2_Valori origine
Sono determinati dai due parametri origine, ragionando con la stessa logica con cui ragiona il modulo D5
