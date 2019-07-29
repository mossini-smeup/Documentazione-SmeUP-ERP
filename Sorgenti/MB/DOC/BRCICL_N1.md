# Scansione ciclo con data di validità
La scansione di produzione esegue un filtro sulla data di validità : 
 * se data = 0 assume oggi;
 * se data = 99999999 non esegue il filtro e ritorna tutte le fasi (esegue gli altri filtri :  ciclo, configurazione, stato, ..)

Modalità di appartenenza di una fase ad un periodo (in scansione £CRT) : 

![BRCICL_22](http://localhost:3000/immagini/BRCICL_N1/BRCICL_22.png)
**Nota Bene**; gli estremi sono compresi :  è cura di chi definisce i periodi evitare le sovrapposizioni

Una fase appartiene ad un periodo se l'inizio validità è =< della fine del periodo e la fine validità è >= dell'inizio del periodo. Non si fanno calcoli di appartenenza parziale.
