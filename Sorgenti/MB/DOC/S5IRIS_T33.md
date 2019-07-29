Nel seguente documento suggeriamo quali exit utilizzare al fine di ottenere alcuni comportamenti
applicativi.
E' da notare che le exit il cui ultimo carattere NON è una X sono da intendersi come soluzioni applicative standard già pronte per l'utilizzo.


|  Nam="Set.up parametri" |
| 
| .COL Txt="Descrzione  " LunAut="1" |
| ---|----|
| 
| .COL Txt="Numero Parametro" LunAut="1" |
| 
| .COL Txt="Exit " LunAut="1" |
| 
| .COL Txt="Nota " LunAut="1" |
| Modificare il Criterio di ordinamento all'interno dello schedulatore|12|S5SMX_02X |
| Accodare all'operazione schedulata operazioni con lo stesso Attrezzo|12|S5SMX_03B|Forzare in campo S6AA01 il codice attrezzo (pgm aggiustamento S5FURIT_X) ed impostare parametro 1  par_scp a 1 |
| Accodare all'operazione schedulata operazioni con la stessa materia prima| 12|S5SMX_03B|Forzare in campo S6AA01 il codice materia prima proncipale(pm aggiustamento S5FURIT_X) ed impostare parametro 1  par_scp a 1 |
| Accodare all'operazione schedulata operazioni che devono avere stesso istante di spedizione da magazzino|12|S5SMX_03B|Forzare in campo S6AA01 data di spedizione (pm aggiustamento S5FURIT_X) impostare parametro 1  par_scp a 1 |
| Accodare all'operazione schedulata operazioni con ordine di scala cromatica|12|S5SMX_03B|Forzare in campo S6AA01 scala cromatica  (pm aggiustamento S5FURIT_X) impostare parametro 1  par_scp a 1 |
| Accostamento operazioni consecutive  stesso ordine produzione se da eseguire su stessa risorsa|12|S5SMX_031 |
| Filtro operazioni da schedulare personale|7|S5SMX_02X |
| Data inizio ordine produzione uguale data inizio prima operazione|33|S5SMX_08X |
| Modifica date Ordine Produzione sulla base dei risultati della schedulazione|33|S5SMX_08X |
| Data fabbisogno cliente come riferimento per calcolo anticipi /ritardi |74|S5SMX_15X |
| L'attrezzaggio viene eliminato se articolo e fase uguali ai precedenti eseguiti su stessa risorsa|14|S5SMX_041 |
| Calcolo Termpo Attrezzaggio in base a caratteristiche dimensionali dell'articolo|14|S5SMX_04X |
| Modifica Data fine schedulata operazione al termine sua schedulazione|3|S5SMX_01X |
| Forzatura Risorsa specifica operazione successiva in funzione dell'operazione appena schedulato|3|S5SMX_01X |
| Creazione di gruppi temporanei definiti a parità di oggetto rifiremento su S5IRIS|3|S5SMX_01X |
| Impostazione Tiro su parte congelata x spostare l'intero gruppo congelato|3|S5SMX_01G |
| Partenza schedulazione da data S5IRIS|77|S5SMX_161 |
| Partenza schedulazione da ultima dichiarazione P5ATTI|77|S5SMX_162 |
| Partenza schedulazione data fine evento P5ATTI|77|S5SMX_163 |
|  |
|  |
| 



