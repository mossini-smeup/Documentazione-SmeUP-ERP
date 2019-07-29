# SFR - Ripresa dati per schedulazione
 :  : DEC T(ST) K(SFR)
## OBIETTIVO
Identificare le possibili fonti di ripresa dati che alimentano gli archivi della schedulazione fine.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
Elemento di 3 posizioni a contenuto libero.
 :  : FLD T$DESC Descrizione
 :  : FLD T$SFR1 __Archivio ripresa__
È l'archivio da cui vengono letti i dati da portare nell'archivio della schedulazione fine (SFPCL).
 :  : FLD T$SFR2 __Membro ripresa__
Identifica nell'ambito dell'archivio di ripresa un membro specifico da cui leggere i dati da collegare.
_9_Esempio :  nell'ambiente Gipros sono disponibili diversi ambienti di pianificazione. È possibile tramite questo campo
identificare l'ambiente su cui si desidera analizzare l'impegno delle risorse produttive.
 :  : FLD T$SFR3 __Scelta membro ripresa__
Abilita il programma a gestire la scelta dell'ambiente da cui riprendere i dati.
 :  : FLD T$SFR4 __Gruppo azioni richieste__
Elemento della tabella SFB, identifica il gruppo di azioni che verrà eseguito per il collegamento dei dati dell'archivio impostato.
 :  : FLD T$SFR5 __Parametro__
Campo libero di 50 posizioni. Viene utilizzato per impostare delle scelte come ad esempio membri, parzializzazioni, stati etc. che condizioneranno i programmi, identificati tramite il gruppo azioni Tab. SFB.
