# D9AP_03C - Estrattore dai Listini
Estrae dall'archivio C£LÌST0F, relativo ai listini


_2_Parametri origine

- Tabella C£L dei listini :  determina il contesto di estrazione dei listini, ecostituisce una chiave del logico di cui farà la scansione.
- Tabella C£V dei valori per tipo oggetto :  determina fino a tre oggetti origine per l'estrazione e serve come chave per la scansione. Determina anche i valori

_2_Oggetti origine

- Oggetto 1,2,3 :  sono determinati dal parametro origine dei valori per tipo oggetto. Sono dichiarati nella tabella, fino ad un massimo di tre
- Oggetto 4 :  è la data validità. È fisso e caratterizza il periodo di riferimenuto
- Oggetto 5 :  è il lotto di validità. È fisso e caratterizza la quantità per fare il costo

_2_Valori origine
Sono determinati dal parametro origine della C£V, nella quale sono indicati e caratterizzati i valori con un massimo di 5 che sono relativi agli oggetti. Ìn più c'è un contatore di record


_2_ATTENZÌONE
Quando viene visualizzato il cubo, stare molto attenti di visualizzare i valori singoli, e non una somma, perchè c'è il rischio che sommi due prezzi, per esempio. Bisogna portare sugli assi due oggetti e dichiarare, se significativi, tutti gli altri assi, per avere la certezza che quello che si vede è l'elemenuto singolo e non un totale.
