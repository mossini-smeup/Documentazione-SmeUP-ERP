# Introduzione
SME.up in termini generali vede gli oggetti e ne esegue le funzioni disponibili. Esempi banali di funzioni sono la verifica di validità di un oggetto oppure la ricerca alfabetica. Ogni oggetto ha come proprietà quella dell'ambiente in cui è definito, quindi la funzione viene eseguita dall'applicazione dell'ambiente che lo possiede. Naturalmente tali funzioni devono essere presenti sul sistema così come i dati.
Diremo che esistono le interfacce per un ambiente se sono state scritti i programmi che sentono le chiamate di SME.up e rispondono opportunamente dopo aver letto gli archivi opportuni (o richiamato le funzioni di ogni ambiente)

## Esempi di interfacce
 * Articoli (verifica, ricerca, scansione, ecc)
 * Clienti
 * Fornitori
 * Conti contabili
 * Registrazioni contabili
 * Distinta base
 * Ecc.

## Esempi di utilizzo delle funzioni
- Interrogo la distinta base in SME.up, la distinta base è gestita in ACG ma gli articoli sono stati personalizzati. La distinta è fornita dall'ambiente "A7", le decodifiche degli articoli sono fornite dall'ambiente "XX" (Personalizzato). Il programma di interrogazione è in SME.up, la distinta può essere vista nella scheda standard di LOOC.up, presentarsi in modo grafico o essere utilizzata nel calcolo fabbisogni dell'MPS.

## Interfacce in LOOC.up e in SURF.up
Se una funzione nell'ambiente "xx" emette un formato video, questo non funziona in LOOC.up poichè dovrei disporre del sorgente e ricompilarlo ma non è fra gli obiettivi di LOOC.up eseguire tutti i programmi di tutti gli ambienti. SURF.up è pensato per un accesso diretto ai dati a prescindere dalle interfacce. Si veda a tal fine la documentazione di SURF.up

# Dettaglio degli ambienti
- [Interfacce ACG&-x2f;V7 (IBM](Sorgenti/MB/DOC/B£INTE_IA7)
- [Interfacce ACG&-x2f;V8 (IBM](Sorgenti/MB/DOC/B£INTE_IA8)
- [Interfacce Gipros (THERA](Sorgenti/MB/DOC/B£INTE_IG6)
