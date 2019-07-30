 :  : HEA RESP(AS) STAT(80)
# OBIETTIVO
Questo servizio fornisce le funzionalità aggiuntive di interrogazione dei costi D5.

# FUNZIONI/METODI
## R2K Da ID record a chiavi del file
Restituisce una matrice con le chiavi del file relative all'ID del record ricevuta in ingresso.
## K2R Da chiavi del file a ID record
Restituisce un albero con un solo elemento contenente l'ID del record associato alla chiave ricevuta in input. E' necessario specificare la chiave completa.
## CFR Effettua alcuni confronti
### Metodo COD
Costruisce la matrice dei confronti per codice (D$CODI). E' possibile effettuare delle totalizzazioni :  se non passo tutti i codici gestiti nel tema, totalizzo per quelli passati in input. Ad esempio se nel tema sono gestiti tutti e tre i codici e vengono passati in input solo i primi due, viene considerato ininfluente il terzo e vengono quindi sommati i valori disinteressandosi del terzo codice. Analogamente è possibile fare con la data/periodo di validità :  se non specifico tale dato non lo uso come filtro.
## CEP Controllo numero codici gestiti e data/periodo validità
Viene resituita una matrice con una riga e due colonne :  nella prima colonna è indicato il numero di codici gestiti nel contesto/tema, nella seconda colonna invece è indicata la presenza o meno della data/periodo di validità nel tema/contesto.

 :  : PRO.SER Cod="R2K.1" Tit="Dall'ID alle chiavi. " Fun="F(EXB;D5SER_02;R2K) 1(ID;D5COSO0F;-(O;;IDD5COSO0F;ID record))"

 :  : PRO.SER Cod="K2R.2" Tit="Dalle chiavi all'ID. " Fun="F(TRE;D5SER_02;K2R) 1(**;;-(O;;**;Contesto/codice)) 2(TA;D5O**;-(O;;TAD5O**;Tema)) 3(**;;-(F;;**;Codice 1)) 4(**;;-(F;;**;Codice 2)) 5(**;;-(F;;**;Codice 3)) 6(**;;-(F;;**;Data/periodo))"

 :  : PRO.SER Cod="CFR.COD.3" Tit="Confronti totalizzati. Confronto per codici" Fun="F(EXA;D5SER_02;CFR.COD) 1(**;;-( ;;**;Contesto)) 2(TA;D5O**;-(O;;TAD5O**;Tema)) 3(**;;-(F;;**;Codice 1)) 4(**;;-(F;;**;Codice 2)) 5(**;;-(F;;**;Codice 3)) 6(**;;-(F;;**;Data/periodo))"

 :  : PRO.SER Cod="CFR.COD.4" Tit="Confronti totalizzati. Confronto per codici" Fun="F(EXB;D5SER_02;CFR.COD)" Ref="CFR.COD.3"

 :  : PRO.SER Cod="CEP.5" Tit="Controllo codici e data. " Fun="F(EXB;D5SER_02;CEP) 1(**;;-( ;;**;Contesto)) 2(TA;D5O**;-(O;;TAD5O**;Tema))"

