## Scorta datata
>Se l'origine è SD (scorta datata)
Parametro 1 : 
-    Pos.1/4   come l'origine 'SC' (scorta) nelle fonti esistenti (M5E)

- [&-x2a; M5E - SC - Scorta minima](Sorgenti/MB/DOC_OGG/TA_M5E_SC)
>-    Pos.5     -- ' ' se datata a oggi.
.              -- '1' se datata a oggi + tempo approvvigionamento del livello.
.              -- '2' se datata a oggi + tempo approvvigionamento cumulato.
.              -- '3' se datata a oggi + tempo transito dal plant di competenza al
.                     plant di scansione (0 se coincidenti)
.              -- '4' se datata a oggi + tempo approvvigionamento del livello
.                     + tempo di transito ('1' + '3')
.              -- '5' se datata a oggi + tempo approvvigionamento cumulato + tempo
.                     di transito ('2' + '3')
-    Pos.6/8   Tipo distinta per il reperimento del tempo di approvvigionamento
.              cumulato (se non impostato assume 'ART').
-    Pos.9     Risalita scorta. E' significativa se NON è stata impostata la
.              scorta per Ente. Si inserisce un elemento V2/GM_SM, che guida il
.              modo in cui viene reperita la scorta minima, nei dati
.              magazzino/articolo.

