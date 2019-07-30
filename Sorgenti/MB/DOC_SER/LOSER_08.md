 :  : HEA RESP(CC) STAT(10)
# OBIETTIVO
 Obiettivo del servizio è rappresentare una matrice di oggetti "navigabile" in base ai parametri
 man mano scelti.
 La matrice viene caricata tramite uno script. Per precisione nello script è possibile
 inserire n matrici diverse. Ogni matrice viene impostata tramite una sezione.
 I dinamismi sulle matrici sono implementati fissando man mano i parametri
 sugli assi. Tutte le possibili combinazioni impostate sono definite da sottosettori.
 Per ogni combinazione abbiamo un possibile range di valori.
 Esempi sono : 
 - matrice di ubicazioni in cui vengono mostrate le giacenze una volta fissati 2 parametri

# FUNZIONI/METODI

# Struttura del programma specifico
## Nome del programma
xxSPA_nn dove xx è il nome dell'applicazione di appartenenza

### Funzioni e metodi
 * XML.GRI - Restituisce le righe della griglia
 * XML.POS/LET - Restituisce le righe della matrice
 * SPA.POS/LET - Restituisce gli spazi
 * ATT.POS/LET

# Struttura dello SCRIPT
## Nome dello SCRIPT
Per ora si assume LO_MATOGG (Da definire)
## Elementi
### T.SEZ = Sezioni
 * Cod = Codice identificativo
 * Txt = Testo
 * Pgm = Programma

Una sezione può contenere un insieme di spazi omogenei per i quali cioè la struttura della  stringa è sempre uguale e definita dalle chiavi.
### T.SUB = Subsezioni
 * ModAtt = Modo di presentazione degli attributi di dettaglio
   - INT  = Tutti quelli definiti all'interno dello SCRIPT
### T.SUB = Sezioni
