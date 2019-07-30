 :  : HEA RESP(LS) STAT(10)
## OBIETTIVO
Riunire le funzioni di scansione operazioni e materiali per un ordine di produzione

## FUNZIONI/METODI

### Sui materiali

### Sulle risorse

 :  : PRO.SER Cod="GEN.DAT.1" Tit="Generale. Presenta date" Fun="F(EXB;P5SER_02;GEN.DAT)"

 :  : PRO.SER Cod="GEN.QTA.2" Tit="Generale. Presenta quantità" Fun="F(EXB;P5SER_02;GEN.QTA)"

 :  : PRO.SER Cod="GEN.SIT.3" Tit="Generale. Presenta situazione" Fun="F(EXB;P5SER_02;GEN.SIT)"

 :  : PRO.SER Cod="MAT.LISD.4" Tit="Materiali. Lista di dettaglio" Fun="F(EXB;P5SER_02;MAT.LISD) 1(OR;;-(F;;OR;Ordine))"

 :  : PRO.SER Cod="MAT.LISR.5" Tit="Materiali. Lista rieilogata" Fun="F(EXB;P5SER_02;MAT.LISR)" Ref="MAT.LISD.4"

 :  : PRO.SER Cod="RIS.LIS.6" Tit="Risorse. Lista" Fun="F(EXB;P5SER_02;RIS.LIS)" Ref="MAT.LISD.4"

 :  : PRO.SER Cod="IMT.SIT.7" Tit="Impegno materiale. Situazione" Fun="F(EXB;P5SER_02;IMT.SIT) 1(IT;;-(F;;IT;Ordine))"

