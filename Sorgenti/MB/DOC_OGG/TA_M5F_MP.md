## Voce di MPS
>Se l'origine è MP (voce di MPS)
Parametro 1 : 
-    Pos.1/6   Codice piano (obbligatorio)
-    Pos.7/7   Se impostato considera il piano con codice più alto, con radice
.              uguale al codice impostato. Se lasciato in bianco, considera solo
.              il piano impostato.
-    Pos.8/8   È significativa se l'applicazione è multimagazzino; definisce il
.              magazzino a cui appartiene la vista : 
.              ' '  il codice magazzino viene assunto dal magazzino definito nella
.                   tabella piano;
.              '1'  il codice magazzino è la chiave 1 della vista;
.              '2'  il codice magazzino è la chiave 2 della vista.
-    Pos.9/9   Se impostata, l'articolo è la chiave 2, se lasciata in bianco è la
.              chiave 1.
.              NB :  è compito del compilatore delle fonti assicurarsi che ci sia
.              congruenza tra quanto definito nelle posizioni 8 e 9 e le chiavi
.              impostate nella vista :  questa impostazione non viene eseguita nel
.              programma per motivi di prestazioni.
-    Pos.10    Se impostata, questa è la fonte guida per il calcolo delle fonti
.              bilanciate. Se non impostato viene assunta la prima fonte MPS
.              presente nel gruppo fonti.
.              Se impostato per più di una fonte si assume la prima.
Parametro 2 : 
-    Pos.1/3   Codice vista (obbligatoria)
-    Pos.4/4   Se impostato raggruppa in un'unica riga elementi diversi di una
.              stessa vista (che differiscono per la chiave non di articolo), se
.              invece lasciato in bianco mantiene righe diverse.
-    Pos.5/5   '1' se considerare come data fonte la data inizio periodo;
.              ' ' se considerare come data fonte la data fine periodo.
-    Pos.6/6   ' ' se considerare tutti i periodi del piano;
.              '1' se considerare solo i periodi del piano non scaduti (la data di
.                  oggi è considerata scaduta);
.              '2' se considerare solo i periodi del piano non scaduti (la data di
.                  oggi è considerata NON scaduta).
.              Per determinare lo scaduto si utilizza la data di oggi e la data di
.              inizio o fine periodo come specificato dalla posizione 5 del
.              parametro 2.
.              'A' se considerare solo i periodi del piano con data fine maggiore di
.                  oggi.
.              'B' se considerare solo i periodi del piano con data fine maggiore o
.                  uguale ad oggi.
-    Pos.7/7   Se impostato, la chiave della vista diversa dall'articolo viene
.              trattata come oggetto significativo. Questo avviene sia nella
.              parzializzazione, sia come campo ritornato dalla scansione.
.              Se impostata anche la posizione 4, quest'ultima viene pulita.
.
Sono trattati i seguenti campi : 
-    Ente.
-    Commessa.
-    Configurazione.
-    Risorsa.
-    Lotto.

