# Esecuzione comando SAVSPLF
 :  : I.INC.MBR Lib(SMEDEV) Fil(DOC_OGG) Mem(P_SAVSPL)
 :  : INI
 :  : CMD SAVSPLF
 :  : FIN


# Richiamo B£UT59A
 :  : I.INC.MBR Lib(SMEDEV) Fil(DOC_OGG) Mem(P_B£UT59)
 :  : INI
 :  : CMD CALL PGM(B£UT59A)
 :  : FIN


# Richiamo TSTG53
 :  : I.INC.MBR Lib(SMEDEV) Fil(DOC_OGG) Mem(P_TSTG53)
 :  : INI
 :  : CMD CALL PGM(TSTG53)
 :  : FIN


# Richiamo TSTG80
 :  : I.INC.MBR Lib(SMEDEV) Fil(DOC_OGG) Mem(P_TSTG80)
 :  : INI
 :  : CMD CALL PGM(TSTG80)
 :  : FIN

