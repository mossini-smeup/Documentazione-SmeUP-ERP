# Modalità di traduzione

Per effettuare le traduzioni è possibile utilizzare la scheda apposita che si trova nel menù del modulo.

# Autorizzazioni
Mediante la classe di autorizzazione A£LING_TRA è possibile decidere quali utenti sono abilitati a tradurre, su quali lingue e con quale grado di affidabilità.

# Completamento delle traduzioni
Tramite le apposite voci di menù del modulo è possibile completare le traduzioni mancanti a partire da traduzioni già esistenti (ma fatte su contesti differenti), oppure a partire da una seconda lingua.

# Nota
Non si dovrebbe MAI inserire a mano traduzioni (es. SQL, upddta...)
Gli unici programmi abilitati al completamento di traduzioni sono : 
 * A£UTX05 - passaggio da pre-V4R1. Scrive traduzioni con S2STDE='05' e S2FTTR='3'
 * A£TR12A, A£TR13B - ripresa traduzioni da altri record (altre lingue o altri contesti). Scrivono traduzioni con S2STDE='05' e S2FTTR='4'
 * A£SUP_01 - compilazione manuale traduzioni da schede del modulo A£LING. Scrive traduzioni con S2STDE controllato dall'utente (tipicamente 10/20) e S2FTTR='2'.

