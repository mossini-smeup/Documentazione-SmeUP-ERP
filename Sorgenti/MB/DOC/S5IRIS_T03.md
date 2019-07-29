
# Scenario di schedulazione
         L'elemento '**' della tabella S5B definisce  i comportamenti principali della nostra schedulazione
         Nello scenario definiamo i seguenti aspetti della schedulazione : 
 1. Risorsa da schedulare. Nel campo risorsa principale mettiamo 'CDL' , nel campo risorsa specifica se scheduliamo i centri di lavoro impostiamo 'CDL' (non abbiamo CDL composti di più macchine) se scheduliamo le macchine 'MAC'
 2. Oggetto Priorità. Definisce la priorità con cui a parità di istante di esecuzione di un Job viene scelto quello con priorità più alta. Le regole implementate ci permettono di scegliere tra 'N'    valori     ognuno dei quali permette di ottimizzare un diverso indice (saturazione,  numero ordini elaborati, etc..)
- [Criterio ordinamento schedulazione BCD](Sorgenti/MB/DOC_OGG/V2_CRORD)
3.  E' possibile attivare un flag con cui considerare i tempi di attrezzaggio
4.  E' possibile attivare un flag con cui considerare se esiste la sovrapposizione tra le fasi impostata o a livello di fase di ciclo oppure di gruppo risorsa.
5.  E' possibile attivare un flag con cui attivare l'utlizzo delle code. In una schedulazione a capacità finita le code sono considerate solo per i centri di lavoro schedulati a capacità infinita.


![S5IRIS_04](http://localhost:3000/immagini/S5IRIS_T03/S5IRIS_04.png)
Questi sono i set.up minimali dello scenario, per una trattazione completa è possibile fare riferimento all'help della tabella.







