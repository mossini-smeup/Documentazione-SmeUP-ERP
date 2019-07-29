
Vedi anche OG_SP (Oggetto schema di presentazione)

## LA CODIFICA DEGLI SCHEMI
Nel codice dello schema è insita una specifica struttura che implica l'appartenenza ad un gruppo e ad una serie.
Il gruppo di appartenenza indica a quale sottoinsieme degli elementi della tabella INT lo schema fa riferimento :  il gruppo è identificato dal primo carattere dell'elemento della tabella
 INT (es. se uno schema appartiene al gruppo A significa che nello schema posso utilizzare tutti elementi della tabella INT che iniziano per A).
 La serie al contrario indica con quale n° fra i 5 possibili schemi che posso esistere in un determinato gruppo lo schema viene identificato.
Tale n° si riscontra nelle colonne indicate all'interno dell'elemento della tabella INT sotto l'intestazione "** SCHEMI INTERR. **".

> | Schema | Gruppo |  Serie |

     1         A       1
     2         A       2
     3         A       3
     4         A       4
     5         A       5

     6         B       1
     7         B       2
     8         B       3
     9         B       4
     0         B       5

     A         C       1
     B         C       2
     C         C       3
     D         C       4
     E         C       5

     F         D       1
     G         D       2
     H         D       3
     I         D       4
     J         D       5

     K         E       1
     L         E       2
     M         E       3
     N         E       4
     O         E       5

     P         F       1
     Q         F       2
     R         F       3
     S         F       4
     T         F       5



## DEFINIZIONE CAMPI CALCOLATI DA ATTRIBUTI
 Specificando nella descrizione di un elemento della tabella INT la codifica riportata di seguito
 è possibile introdurre nello schema dei campi calcolati in base ad attributi di oggetti utilizzati
 nello schema stesso.

 "&" + xxx + "*" + Tipo + "*" + Parametro + ">" + Codice OAV

 Dove xxx è n° del campo dello schema che da il codice dell'oggetto dell'OAV.

 Se voglio che invece del valore dell'attributo mi venga ritornato la descrizione dell'attributo è
 sufficiente indicare due segni maggiori prima dell'OAV.
Es.
 "&" + xxx + "*" + Tipo + "*" + Parametro + ">>" + Codice OAV

 NOTA BENE :  anche se il parametro è blank va comunque sempre indicato anche il secondo "*"




