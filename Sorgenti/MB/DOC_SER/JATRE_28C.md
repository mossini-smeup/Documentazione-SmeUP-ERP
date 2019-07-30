# OBIETTIVO
Fornire funzioni per contatti e articoli.





# FUNZIONI/METODI
## FOG - Funzioni specifiche di oggetto
Metodi **ADF,ADM,ADG**

Metodo **ADD**

Metodi **SCA,PAR**

Metodo **DIS**

Metodo **DRA**

Metodo **ES1**

## GOG - Grafici di oggetto
Metodo **ADF**

Metodo **SCA**

Metodo **DIS**


 :  : PRO.SER Cod="FOG.ADF.1" Tit="Funzioni specifiche dell'oggetto. ADF - Riepilogo" Fun="F(TRE;JATRE_28C;FOG.ADF) 1(CN;;-(O;;CN;Ente)) 2(MD;C5C6F0G;-(O;;MDC5C6F0G;Memorizz.))"

 :  : PRO.SER Cod="FOG.ADF.2" Tit="Funzioni specifiche dell'oggetto. ADF - Riepilogo" Fun="F(EXB;JATRE_28C;FOG.ADF)" Ref="FOG.ADF.1"

 :  : PRO.SER Cod="FOG.ADM.3" Tit="Funzioni specifiche dell'oggetto. ADF - Analisi mensile" Fun="F(EXA;JATRE_28C;FOG.ADM)" Ref="FOG.ADF.1"

 :  : PRO.SER Cod="FOG.ADT.4" Tit="Funzioni specifiche dell'oggetto. ADF - Analisi giornaliera" Fun="F(EXA;JATRE_28C;FOG.ADT)" Ref="FOG.ADF.1"

 :  : PRO.SER Cod="FOG.SCA.5" Tit="Funzioni specifiche dell'oggetto. Scadenzario" Fun="F(EXB;JATRE_28C;FOG.SCA) 1(CN;;-(F;;CN;Ente))"

 :  : PRO.SER Cod="FOG.PAR.6" Tit="Funzioni specifiche dell'oggetto. Partitario" Fun="F(EXB;JATRE_28C;FOG.PAR)" Ref="FOG.SCA.5"

 :  : PRO.SER Cod="FOG.DIS.7" Tit="Funzioni specifiche dell'oggetto. Analisi disponibilità materiali" Fun="F(EXB;JATRE_28C;FOG.DIS) 1(AR;;-(F;;AR;Articolo)) P( FON(-(F;;MDM5FO01G;Gruppo fonti)))"

 :  : PRO.SER Cod="FOG.DRA.8" Tit="Funzioni specifiche dell'oggetto. Righe documento oggetto" Fun="F(EXB;JATRE_28C;FOG.DRA) 1(AR;;-(F;;AR;Articolo)) P( TIP(-(F;;TAV5D;Tipo documento)) MAG(-(F;;MG;Codice magazzino)) OGG(-(F;;TAB£G;Griglia oggetto)))"

 :  : PRO.SER Cod="FOG.ES1.9" Tit="Funzioni specifiche dell'oggetto. Estensione contatti" Fun="F(TRE;JATRE_28C;FOG.ES1) 1(CN;;-(O;;CN;Ente)) 2(TA;BRI;-(F;;TABRI;Estensione)) 3(**;;-(F;;**;))"

 :  : PRO.SER Cod="FOG.ES1.10" Tit="Funzioni specifiche dell'oggetto. Estensione contatti" Fun="F(EXB;JATRE_28C;FOG.ES1)" Ref="FOG.ES1.9"

 :  : PRO.SER Cod="GOG.ADF.11" Tit="Grafici dell'oggetto. Analisi disponibilità finanziaria" Fun="F(EXA;JATRE_28C;GOG.ADF)" Ref="FOG.ADF.1"

 :  : PRO.SER Cod="GOG.SCA.12" Tit="Grafici dell'oggetto. Scadenzario" Fun="F(EXA;JATRE_28C;GOG.SCA)" Ref="FOG.SCA.5"

 :  : PRO.SER Cod="GOG.DIS.13" Tit="Grafici dell'oggetto. Analisi disponibilità materiali" Fun="F(EXA;JATRE_28C;GOG.DIS)" Ref="FOG.DIS.7"

