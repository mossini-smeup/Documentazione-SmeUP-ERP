# Utilizzo in scheda

La funzione di ricerca oggetto e' compatibile con xml di tipo matrice e input panel e può quindi
essere utilizzata all'interno di una scheda o chiamata da menù.

## Utilizzo di un set di query
Se si desidera utilizzare un set di query per un determinato oggetto, è possibile includere
o linkare la seguente funzione : 
F(EXD;*SCO;) 1(OG;;[OG]) 2(MB;SCP_SCH;C_Q1) 4(;;ESE)

La scheda è disponibile per l'oggetto OG (sezione query), accessibile quindi da F4.

## Utilizzo di una singola query
Se si desidera utilizzare una singola query per un determinato oggetto, è possibile includere
o linkare la seguente funzione : 
F(EXD;*SCO;) 1(Q1;[OG];[Q1]) 2(MB;SCP_SCH;Q1) 4(;;ESE)

La scheda è disponibile per l'oggetto Q1 (sezione esecuzione), accessibile quindi da F4.

## Utilizzo della matrice dati
Se si desidera utilizzare la matrice dati di una query per un determinato oggetto,
è possibile includere o linkare la seguente funzione : 
F(EXB;JASER_02L;) 1([TP];[PA];[Q1]) 2([TP];[PA];[Q2]) 3([TP];[PA];[Q3]) 4([TP];[PA];[Q4])
P(Q3_CFG([Q3_CFG]) FLT() NRE([NRE]))

I parametri 2() 3() 4() Q3_CF() FLT() NRE() sono opzionali, in caso di assenza vengono utilizzati
i default della query.
