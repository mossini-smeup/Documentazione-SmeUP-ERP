## Codice Oggetto (in TA/*CNTT)
'FO'                                          £FUNT1
Tipo gruppo fonti  (V2/TIPGF)                 £FUNP1
## Chiave primaria
Codice Gruppo fonti                           £FUNK1

Il tipo gruppo fonti specifica se il gruppo è di disponibilità materiali (default) o finanziaria.
 :  : DEC T(V2) P(TIPV2) K(TIPGF)

Fiscamente il gruppo fonti risiede in uma memorizzazione video così individuata : 
Ambiente
- per disponibilità materiali
 :  : DEC T(OJ) P(*PGM) K(M5FO01G)
- per disponibilità finanziaria
 :  : DEC T(OJ) P(*PGM) K(C5C6F0G)
Utente
- Nome dell'MDV

## /COPY gruppo fonti materiali
Filtro disponibilità (£M5F)
 :  : DEC T(MB) P(QILEGEN) K(£M5F)
Cache (£M5B)
 :  : DEC T(MB) P(QILEGEN) K(£M5B)

## /COPY gruppo fonti finanziarie
Filtro disponibilità (£C6F)
 :  : DEC T(MB) P(QILEGEN) K(£C6F)
Cache (£C6B)
 :  : DEC T(MB) P(QILEGEN) K(£C6B)
