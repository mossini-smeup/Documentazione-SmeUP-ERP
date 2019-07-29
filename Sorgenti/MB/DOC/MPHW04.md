# Cosa cambia rispetto a un Holt Winters "normale"

Holt Winters può gestire il dettaglio di un secondo oggetto (tra quelli gestiti come codice di rottura nell'MRP - CM, CN, CF, EM).

Le previsioni e il conseguente D5COSO/£P1 devono essere generati con il dettaglio del secondo oggetto.
La fonte "scorta minima" deve tornare tutti i valori di scorta per tutte le combinazioni di AR/secondo oggetto.

Note varie : 
 * Gli OAV di tipo J/H* vengono disabilitati, non avendo senso in questo contesto.
 * Le forzature sulla scorta minima a standard sono solo sull'AR (£GMA su AR/TAMAG). Se attivo AR/secondo oggetto non gestisco a standard forzature di scorta minima (eventualmente aggirabile mediante una fonte ulteriore).
 * Le forzature sul livello di servizio sono in un parametro £M1 di AR, non AR/secondo oggetto. Per adesso lasciamo così, se si vogliono utilizzare avranno effetto su tutte le combinazioni AR/secondo oggetto.
 * Se scorta datata :  i lead time nella fonte SD per ora vengono letti solo per AR, non eventualmente per AR/CF (l'eventuale riferimento, FUNK3, non è per adesso passato).
 * Anche nella lettura del lead time cumulato per ora si ragiona solo a livello di AR, non di AR/CF.
 * Tutti gli OAV J/H* dell'oggetto AR vengono spenti, non avendo senso ora solo sull'articolo.

## Configurazione dell'ambiente

A partire dal modello (impostazione standard dell'Holt Winters), ipotizzando un secondo oggetto = CF, cambiano le seguenti cose : 
 * TAD5OAR/£P1 va impostato con CF in Oggetto 2. Questa è la condizione che attiva l'HW con secondo oggetto di rottura.
 * Le TAMPC per Holt Winters devono avere la seconda chiave CF.
 * Dato che la seconda chiave è CF non può essere TAMAG, quindi dovrò creare diverse TAMPP se voglio differenziare tra diversi TAMAG.
 *  La fonte previsione (es. a modello la fonte F10) va impostata per tornare il secondo oggetto (Ritorna altra chiave='1' nei parametri specifici della fonte di tipo 'MP')

Si presti attenzione al fatto che deve essere compilato il nuovo logico D5COSO5L.
