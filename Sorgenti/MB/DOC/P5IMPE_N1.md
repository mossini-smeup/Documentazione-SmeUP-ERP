# Costruzione impegni scarico automatico
## Definizioni
**Tipo impegno (TI)**, tabella P5I legata al documento/ordine, contiene modalità di scarico materiali (MSI) (**V2_MOSMA** :  DO = da documenti senza aggiornamento impegni, IM = tutti gli impegni)
 :  : DEC T(MB) P(DOC_OGG) K(V2_MOSMA)
**Tecnica di gestione (TG)**, tabella GMT legata all'articolo, contiene modalità di scarico componente (MSC) **V2_MOSCA**
- [Modalità scarico materiali](Sorgenti/MB/DOC_OGG/V2_MOSCA)

## Costruzione impegni
Viene eseguita se MSI diversa da DO (scarico secondo distinta) e se c'è qtà residua sull'ordine / documento, viene riportato nella modalità di scarico (Flag 1) il valore MSC, se però MSI = "IM" viene portato "B" (scarico automatico).
Vengono esclusi i componenti con MSC = "A" (nessun scarico :  Floor stock non controllato)

## Scarico automatico
Viene eseguito se MSI = "DO" o "IM" per tutti gli impegni. Negli altri casi se MSC = "B" per i singoli articoli.

La Qtà è sempre relativa alla Qtà dell'assieme che si sta versando. Vengono rifasati automaticamente tutti gli impegni.
Se non è impostata la causale di prelievo non viene eseguito lo scarico.
Si parte sempre dalla distinta del documento.
Viene controllato, per ogni impegno, se esiste un movimento di magazzino di saldo "S" (anche a Qtà = 0), in questo caso non viene eseguito lo scarico automatico.

### Nota tecnica
È lo stesso programma che esegue la costruzione e lo scarico degli impegni (**P5FUIMT**); in scarico, oltre ai parametri della £FUN, riceve anche la DS del movimento di magazzino dell'assieme (Versamento)
