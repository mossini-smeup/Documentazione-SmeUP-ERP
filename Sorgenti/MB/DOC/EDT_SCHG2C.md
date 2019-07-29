# G.SUB.TRE :  Albero

All'interno di una sezione è possibile definire una elenco di oggetti.

# Dati

Supporta le funzioni dati relative agli alberi e le funzioni dati di oggetto.

# Setup

Per questo tipo di subsezione è previsto un setup specifico G.SET.TRE

## Icone :  Mostra icone
Questo attributo abilita o disabilita la visualizzazione delle icone nell'albero. I valori possibili sono Yes/No. Il valore di default è Yes.
## SelFirst :  Seleziona il primo
Seleziona automaticamente il primo elemento dell'albero, impostando le relative variabili e facendo scattare i dinamismi collegati. I valori possibili sono Yes/No. Il valore di default è No.
## DynExpand :  Espandibile dinamicamente
Specifica se l'albero è un albero ad espansione dinamica. I valori possibili sono Yes/No. Il valore di default è No.
Nota :  Il servizio che genera i dati deve indicare in ogni nodo dell'albero la chiamata al servizio che genera i dati successivi nell'attributo Exec.
## Recursive :  Esplosione ricorsiva
Specifica se l'albero deve caricare ricorsivamente i dati se trova nodi contenuti uguali a nodi già espansi.  I valori possibili sono Yes/No. Il valore di default è Yes.
## MaxDepth :  Massima profondità
Indica di quanti passi deve essere espanso l'albero in partenza e alla pressione del tasto "Espandi". I valori possibili sono tutti i valori interi. Il valore di default è 1.
## Expanded :  Espansione iniziale
Specifica se l'albero deve apparire in partenza espanso o collassato. I valori possibili sono Yes/No. Il valore di default è Yes.
## NodeText :  Testo nel nodo
Specifica cosa visualizzare nella descrizione del nodo. I valori possibili sono CODE/TEXT/BOTH che indicano rispettivamente il codice dell'oggetto, il testo della descrizione o entrambi. Il valore di default è BOTH.

