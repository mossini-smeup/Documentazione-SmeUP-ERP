# OBIETTIVO
Questo servizio fornisce le funzionalità necessarie ad operare con i documenti V5 di SME.up.

# FUNZIONI/METODI
## Righe dei documenti (DR)
Restituisce una matrice con le righe dei documenti V5 associati all'Oggetto 1 passato.
Oggetti possibili : 
-Articolo
-Livello delle righe
-Ente intestatario
-Tipo riga
-Data consegna confermata
-Documento (fa vedere solo le righe di tale documento)

NB :  Sono 6, nelle regole se ne possono mettere solo 5

## Documenti di un ente (DO)
Se chiamato con componente 'TRE' : 
Restituisce un albero con i documenti associati all'ente indicato in Oggetto 1.
È possibile specificare in Oggetto 2 un tipo documento su cui restringere la ricerca :  rottura per an
Se non si specifica rottura per tipo/livello/anno.
Se chiamato con componente 'EXB' : 
Come con 'TRE' ma restituisce una matrice con alcuni dati fondamentali...

## Fatture (FT)
Metodo **DO** :  restituisce un albero o una matrice con i documenti V5 associati a una fattura spec
Metodo **CN** :  restituisce un albero con le fatture associate a un ente, specificato in Oggetto 1,
 La ricerca avviene sul C5.
 SVILUPPI
 Indicare parametri opzionali con cui restringere la ricerca : 
 - Registro IVA in Oggetto 2
 - Anno in Oggetto 3 (oppure data inizio e data fine?)
 - Azienda in Oggetto 4


 :  : PRO.SER Cod="DR.1" Tit="Righe di uno o più documenti. " Fun="F(EXB;JATRE_14C;DR) 1(AR;;-(O;;AR;))"

 :  : PRO.SER Cod="DR.2" Tit="Righe di uno o più documenti. " Fun="F(EXC;JATRE_14C;DR)" Ref="DR.1"

 :  : PRO.SER Cod="DO.3" Tit="Documenti di un ente. " Fun="F(EXB;JATRE_14C;DO) 1(CN;;-(O;;CN;Ente)) 2(TA;V5D;-(F;;TAV5D;Tipo documento))"

 :  : PRO.SER Cod="DO.4" Tit="Documenti di un ente. " Fun="F(EXC;JATRE_14C;DO)" Ref="DO.3"

 :  : PRO.SER Cod="DO.5" Tit="Documenti di un ente. " Fun="F(TRE;JATRE_14C;DO)" Ref="DO.3"

 :  : PRO.SER Cod="FT.DO.6" Tit="Fatture. Documenti di una fattura" Fun="F(EXB;JATRE_14C;FT.DO) 1(FT;;-(O;;FT;Fattura))"

 :  : PRO.SER Cod="FT.DO.7" Tit="Fatture. Documenti di una fattura" Fun="F(EXC;JATRE_14C;FT.DO)" Ref="FT.DO.6"

 :  : PRO.SER Cod="FT.DO.8" Tit="Fatture. Documenti di una fattura" Fun="F(TRE;JATRE_14C;FT.DO)" Ref="FT.DO.6"

 :  : PRO.SER Cod="FT.CN.9" Tit="Fatture. Fatture di un ente" Fun="F(TRE;JATRE_14C;FT.CN) 1(CN;;-(O;;CN;Ente))"

