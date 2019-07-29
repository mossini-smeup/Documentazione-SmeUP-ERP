# Descrizioni di un oggetto

Per ogni oggetto è stato creato uno strumento di analisi delle ricerche.

## Descrizioni degli attributi
E' possibile modificare la descrizione degli attributi per le ricerche. Di norma viene usata la descrizione standard dei file o degli OAV, ma c'è la possibilità di cambiarla per semplificarla o evitare ambiguità. I record vengono scritti sul C£LING0F con le seguenti chiavi : 

T§TIPO :  '**' + oggetto (Es. CNCLI)
T§CODI :  codice dell'attributo (Es. E§FL19)
T§LING :  lingua derivata dalla tabella B£2

## Scelta attributi preferiti
Per ogni oggetto c'è la possibilità di scegliere una serie di attributi preferiti.
Questa selezione permette di visualizzarli in cima all'elenco degli attributi nelle parzializzazioni e permette di averli come primi in caso di autocompletamento ricerca in web.
I preferiti possono essere a livello di utente (C/COL) o a livello di gruppo (G/COL).
I valori sono salvati sul B£MEDE0F con le seguenti chiavi : 

METIPA :  'TAB£U'
MECODI :  Nome utente per i 'C/COL' o '**' per i 'G/COL'
MECOD1 :  'CARRELLO'
MECOD2 :  'OA' + oggetto + '.COL' (Es. OACNCLI.COL)

## Scelta attributi esclusi
Per ogni oggetto c'è la possibilità di scegliere una serie di attributi che possono essere esclusi.
Questa selezione permette di escludere questi attributi dall'elenco nelle parzializzazioni e delle colonne aggiuntive.
I valori sono salvati sul B£MEDE0F con le seguenti chiavi : 

METIPA :  'TAB£U'
MECODI :  '**'
MECOD1 :  'CARRELLO'
MECOD2 :  'OA' + oggetto + '.COLE' (Es. OACNCLI.COLE)

## Descrizioni forzate manualmente
è l'elenco delle descrizioni forzate manualmente per tutti i record relativi all'oggetto.
Queste descrizioni sono archiviate nel file C£LING0F con le seguenti chiavi : 

T§TIPO :  oggetto (Es. CNCLI)
T§CODI :  codice oggetto di cui si vuole forzare la descrizione
T§LING :  lingua derivata dalla tabella B£2

## Database descrizioni normalizzate
è l'elenco delle descrizioni normalizzate per tutti i record relativi all'oggetto.
Queste descrizioni sono archiviate nel file C£ALIA0F ed la normalizzazione varia da oggetto ad oggetto secondo le regole usate dalla /Copy £K40. Le chiavi di scrittura sul file sono le seguenti : 
E$TIP1 :  oggetto (Es. OG)
E$COD1 :  codice oggetto (Es. CNCLI)
E$TIP2 :  '**'
E$COD2 :  Codice elemento codice oggetto (Es. codice cliente)
E$ALIA :  '£DE'
E$SCD2 :  Codice Azienda

## Analisi delle parole
é una scheda riepilogativa che analizza le parole chiave riconducibili all'oggetto e indica quante volte sono state trovate all'interno dei record.

