Utilizzo /copy £PHI
La copy £PHI è quella che viene usata per gestire gli eventi di attrezzaggio sia manuali che da macchina. La £PHI è stata creata per semplificare i concetti di inizio/fermo/ripresa.
N.B. La £PHI tra le varie sue funzioni richiama la £G95 che è quella che si occupa di
creare gli eventi di lavoro/attrezzaggio/fermo di produzione.
Tutta la struttura della PHI si basa sulla scrittura di eventi sul P5EVEN di tipo £RI.
Questi eventi una volta consuntivati diverranno poi delle attività produttive

La £PHI è pensata per essere utilizzata o nelle azioni di avanzamento (PH_060) o nei punti in cui abbiamo il collegamento con le macchine.
Ad esempio se dalla macchina arrivano degli stati di ON/OFF questi possono determinare il passaggio dallo stato di lavoro a fermo o viceversa.La £PHI si occupa di tradurre i segnali in eventi.

Tra le funzioni più importanti della £PHI ci sono
* WRI E' l'azione principale e serve per dichiarare un evento(attenzione nel caso di cambio stato da macchina solitamente si richiama poi la £PHI con il metodo CHG)
* EOT Permette di rilevare gli eventi in corso sulla macchina (uno per ogni ordine/fase attivo)
* CHG E'una funzione semplice che permette di generare il cambio stato degli eventi
* STOP Permette di "smontare" l'ordine attualmente in macchina

- [Documentazione PHI](Sorgenti/MB/DOC_OGG/P_TSTPHI)
