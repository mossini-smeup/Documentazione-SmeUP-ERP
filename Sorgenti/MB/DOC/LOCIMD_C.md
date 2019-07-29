# Esecuzione dei test
Per i test fare riferimento alla scheda del componente sezione esempi


## Cosa il componente è in grado di generare

Il componente IMG è un generatore di immagini dinamiche.
Data un F del tipo F(IMD;Servizio,funzione.metodo) .... il componente restituisce un XML di forma albero oppure matrice.
Nell'XML restituito viene indicato il percorso dell'immagine o delle immagini generate.

Il formato di restituzione è sempre albero a meno che non venga indicato il formato matrice.
Il formato dell'XML coincide con i componenti, pertanto verrà utilizzato per definire il campo Componete della funzione
scritta nell'XML.
Quindi se viene indicato di avere, ad esempio FBK come formato XML di risposta varemo che verrà restituito un XML di tipo albero
e nella F (scritta nello'XML) avremo :  F(FBK;....;...) ....



## Ambienti e script
I setup di default sono definiti, come per gli altri componenti, nel mebro J3_SET_STD.

Il tag che definisce i setup del componente è G.SET.IMD

