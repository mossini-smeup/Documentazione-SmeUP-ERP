 :  : HEA CLAS(B) STAT(10)
# OBIETTIVO
Ritornare una matrice con gli attributi di un oggetto, specificato in Oggetto1.
Oggetto6, di tipo SI/NO, indica se tornare la matrice completa con informazioni tecniche (categoria/


# FUNZIONI/METODI
## OAV (OAV)
Restituisce una matrice o un albero con gli OAV di un oggetto.
Metodo ***BLANKS**
Tutti
Metodo **GRU**
Restituisce gli attributi appartenenti a un gruppo.
Si ricorda che un gruppo di attributi è un MDV costruito con il programma B£OAV2L.
Di conseguenza un attributo può appartenere a più gruppi.
Metodo **CAT**
Restituisce gli attributi appartenenti a una categoria.
La categoria è una proprietà uniovoca di un attributo. Si imposta con GES/02 dal tstoav.
Metodo **LIM**
Restituisce tutti gli attributi il cui nome sia compreso tra due estremi.
Metodo **SC2**
Restituisce tutti gli attributi il cui nome sia compreso tra due estremi, utilizzando la funzione SC
in questo modo sul B£SLOT non viene controllato il 2° oggetto passato, ma per il calcolo viene consi
Metodo **NXT**
Restituisce il prossimo elemento nella lista di oggetti identificata dal tipo e parametro dell'oggetto 1 della funzione. Arrivato alla fine dell'elenco ricomincia dal primo. Viene memorizzato l'ultimo elemento fornito ed al successivo richiamo viene tornato il prossimi. Se fra due successivi richiami l'ultimo elemento fornito viene eliminato l'elenco ricomincia da capo. Il risultato viene tornato sotto forma di matrice con due colonne (A e B) corrispondenti a codice e descrizione. La matrice sarà costituita da una singola riga con i valori relativi al prossimo elemento.

## Tabella (TBL)
Ritorna una lista di oggetti di un certo tipo. Il tipo oggetto è specificato in Oggetto 1.
Se l'Oggetto 1 è OJ*FILE in Oggetto 2 si può specificare la libreria, vengono restituiti i membri di

 SVILUPPI

 :  : PRO.SER Cod="OAV..1" Tit="scansione OAV. TUTTI" Fun="F(EXB;JATRE_17C;OAV.)"

 :  : PRO.SER Cod="OAV..2" Tit="scansione OAV. TUTTI" Fun="F(TRE;JATRE_17C;OAV.)"

 :  : PRO.SER Cod="OAV.GRU.3" Tit="scansione OAV. per gruppo" Fun="F(EXB;JATRE_17C;OAV.GRU) P( GRU(-(F;;**;Gruppo)))"

 :  : PRO.SER Cod="OAV.GRU.4" Tit="scansione OAV. per gruppo" Fun="F(TRE;JATRE_17C;OAV.GRU)" Ref="OAV.GRU.3"

 :  : PRO.SER Cod="OAV.CAT.5" Tit="scansione OAV. per categoria" Fun="F(EXB;JATRE_17C;OAV.CAT) P( CAT(-(F;;**;Categoria)))"

 :  : PRO.SER Cod="OAV.CAT.6" Tit="scansione OAV. per categoria" Fun="F(TRE;JATRE_17C;OAV.CAT)" Ref="OAV.CAT.5"

 :  : PRO.SER Cod="OAV.LIM.7" Tit="scansione OAV. entro certi limiti" Fun="F(EXB;JATRE_17C;OAV.LIM) P( DA(-(F;;**;Limite inferiore)) A(-(F;;**;Limite superiore)))"

 :  : PRO.SER Cod="OAV.LIM.8" Tit="scansione OAV. entro certi limiti" Fun="F(TRE;JATRE_17C;OAV.LIM)" Ref="OAV.LIM.7"

 :  : PRO.SER Cod="OAV.SC2.9" Tit="scansione OAV. entro certi limiti con SC2" Fun="F(EXB;JATRE_17C;OAV.SC2)" Ref="OAV.LIM.7"

 :  : PRO.SER Cod="OAV.SC2.10" Tit="scansione OAV. entro certi limiti con SC2" Fun="F(TRE;JATRE_17C;OAV.SC2)" Ref="OAV.LIM.7"

 :  : PRO.SER Cod="TBL.11" Tit="Tabella. " Fun="F(EXB;JATRE_17C;TBL)"

 :  : PRO.SER Cod="NXT.01" Tit="Prossimo elemento nell'elenco dei servizi" Fun="F(EXB;JATRE_17C;NXT) 1(V3;ASE;)"

 :  : PRO.SER Cod="NXT.02" Tit="Prossimo elemento nell'elenco dei collaboratore" Fun="F(EXB;JATRE_17C;NXT) 1(CN;COL;)"

