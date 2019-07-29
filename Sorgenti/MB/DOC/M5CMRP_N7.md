## Struttura D5COSO per memorizzazione indici

Nella pianificazione si possono memorizzare due categorie di indici (su D5COSO).
- Indici globali relativi all'intera pianificazione
- Indici di istanza relativi a ordini pianificati

## Indici globali
Vengono calcolati, ad ogni MRP completo, se impostato nello scenario M5B il flag costruzione indici
 :  : DEC T(VO) P(T.M5B) K(T$M5BQ)
Si definisce il contesto (D5S) TAS5B, con tema (D5O/sst M5) £I2, con il plant nel codice 1, e con progressivo 14 della definizione indici
 :  : DEC T(OJ) P(*PGM) K(D5CO_14)
Viene calcolato con il programma
 :  : DEC T(OJ) P(*PGM) K(M5MRP0I)

## Indici di ordini pianificati
Vengono calcolati, per ogni ordine pianificato, i valori di schedulazione a partire dagli impegni risorse.
Sono calcolati solo per lo scenario '**'
Deve essere impostato, nello scenario di pianificazione M5B lo scenario degli impegni risorse.
 :  : DEC T(VO) P(T.M5B) K(T$M5BK)
la cui presenza attiva la costruzione degli impegni risorse pianificati.
Deve essere inoltre codificato in modo opportuno il flag di memorizzazione indici dello scenario S5B.
 :  : DEC T(VO) P(T.S5B) K(T$S5BQ)
Si definisce il contesto (D5S) M5, con tema (D5O/sst M5) £I1, con il tipo origine nel codice 1 e l'abito nel codice 1, e con progressivo 10 della definizione indici
 :  : DEC T(OJ) P(*PGM) K(D5CO_10)
Viene calcolato con il programma
 :  : DEC T(OJ) P(*PGM) K(S5FURIT_SC)
lanciato dalla rifasatura degli impegni risorse pianificati
 :  : DEC T(OJ) P(*PGM) K(M5FURIT).




