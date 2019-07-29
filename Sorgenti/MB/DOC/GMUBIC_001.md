_B_Mappa ubicazioni
 Se il codice delle ubicazioni è costruito secondo una struttura che lo lega
 alla posizione fisica (es. Fila/Colonna/Livello)  è  possibile ottenere una
 rappresentazione bidimensionale delle proprie ubicazioni, tramite l'opzione
 a Menù_9_Funzioni sulla Mappa Ubicazioni.
 Da questa 'mappa' è possibile agire sulle ubicazioni non solo visualizzando
 quelle esistenti, ma creandone di nuove (in modo semiautomat.), modificando
 le esistenti, visualizzando il contenuto etc.

 E' necessario  definire  delle  tabelle  per le coordinate utilizzate nella
 creazione dei codici.
 Es. se ho codificato  per_2_Colori,_3_Colonne, _4_Righedovrò avere una tabella
     che contiene le File possibili, una i Livelli e una i Colori.
    :  : DEC T(ST) K(GM*U1) I(_2_Tabella Colori   >>)
    :  : DEC T(ST) K(GM*U2) I(_3_Tabella Colonne  >>)
    :  : DEC T(ST) K(GM*U3) I(_4_Tabella Righe    >>)
