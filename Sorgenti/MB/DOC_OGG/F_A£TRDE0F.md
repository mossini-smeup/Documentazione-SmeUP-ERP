## Contenuto

Traduzione nelle diverse lingue delle frasi di Sme.UP.
Queste traduzioni vengono utilizzate : 
 * Per generare/compilare oggetti in lingua (display file, message file, printer file).
 * A run time per tradurre altri oggetti di Sme.UP (ad esempio le frasi nei programmi).

Due tipologie di frasi vengono tradotte : 
 * Frasi presenti in A£TROR0F (frasi standard o personali), con relativi contesti ed ambiti.
 * Frasi personalizzate (frasi in ambito 00 che solo in A£TRDE0F vengono copiate in ambiti >=10 al fine di personalizzare la traduzione, per una lingua specifica).

## Oggettizzazione
Nessuna.

## Impostazioni fisse
Nessuna.

## Autorizzazioni
Nessuna.

## Livelli e stati
Lo stato è "blindato" in un V2 (A£TR2) e indica se la frase è tradotta/da confermare/confermata.

## /COPY
Preparazione dell'archivio delle traduzioni (scrittura frasi da tradurre) : 
 :  : DEC T(MB) P(QILEGEN) K(£A£C)
Reperimento delle traduzioni : 
 :  : DEC T(MB) P(QILEGEN) K(£A£B)

## Note strutturate (Tabella NSC)
Nessuna.

### Parametri (Tabella C£E)
Nessuno.

### Flussi (Tabella B£H)
Nessuno.
