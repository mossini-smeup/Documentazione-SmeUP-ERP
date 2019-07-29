
# STRUTTURA XML DI UNA MATRICE

## STRUTTURA XML DI UNA MATRICE

La struttura XML di una matrice si presenta in questo modo : 

<Griglia>
 <Colonna Cod="E§RAGS" Txt="Articolo" Tip="" Lun="15" IO="O" Ogg="AR" Dpy="" Aut=""/>
 <Colonna Cod="T§X01E" Txt="Descrizione" Tip="" Lun="50" IO="O" Ogg="" Dpy="" Aut=""/>
 <Colonna Cod="T§X01B" Txt="Data" Tip="" Lun="8" IO="O" Ogg="D8*YYMD" Dpy="" Aut=""/>
 <Colonna Cod="I" Txt="Importo" Tip="" Lun="10;2" IO="O" Ogg="NR" Dpy="" Aut=""/>
 <Colonna Cod="§Q08" Txt="Quantita" Tip="" Lun="10" IO="O" Ogg="NR" Dpy="" Aut=""/>
 <Colonna Cod="TSMEDI" Txt="Prezzo|Medio" Tip="" Lun="10" IO="O" Ogg="NR"   Formula="[I]/[§Q08]" Dpy="" Aut=""/>
 <Colonna Cod="TSPROB" Txt="Proiezione|Bassa" Tip="" Lun="10" IO="O" Ogg="NR"   Formula="[TSMEDI]*[§Q08]*2" Dpy="" Aut=""/>
 <Colonna Cod="§Q07" Txt="Differenza" Tip="" Lun="10;2" IO="O" Ogg="NR"   Formula="[I]-[§Q08]" Dpy="" Aut=""/>
 <Colonna Cod="INTSUM" Txt="Somma record" Tip="" Lun="10;2" IO="O" Ogg="NR"   Formula="[SUM]" Dpy="" Aut=""/>
</Griglia>
<Righe>
 <Riga Fld="A01|20060101||-100"/>
 <Riga Fld="A01|20060101|-100|-1"/>
</Righe>



Per degli esempi dettagliati sui Setup riferirsi a
**My LoocUp --> Per lo sviluppatore --> Esempi --> Capire LoocUp --> 01.CMP --> 01.CMP.EXB :  Matrice --> Matrice - Setup Matrice,
**My LoocUp --> Per lo sviluppatore --> Esempi --> Capire LoocUp --> 01.CMP --> 01.CMP.EXB :  Matrice --> Colonne - Setup Colonna ,
**My LoocUp --> Per lo sviluppatore --> Esempi --> Capire LoocUp --> 01.CMP --> 01.CMP.EXB :  Matrice --> Righe - Setup Riga e
**My LoocUp --> Per lo sviluppatore --> Esempi --> Capire LoocUp --> 01.CMP --> 01.CMP.EXB :  Matrice --> Cella - Setup Cella


# Varie Esempi
 Per vari esempi sulle matrici riferirsi inoltre a
**My LoocUp-->Per lo sviluppatore-->Esempi-->Capire LoocUp-->01.CMP-->01.CMP.EXB :  Matrice-->Matrice - Esempi generici











