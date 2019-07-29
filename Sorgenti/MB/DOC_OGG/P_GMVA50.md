### Generazione da giacenza attuale
Questa funzione parte da una situazione di giacenza e riapplica a ritroso tutti i movimenti fino a ricostruire il saldo presente alla "Data limite" inserita videata di input.
Si considerano solo le giacenze relative alle aree definite come "Area fiscale" all'interno della tabella GMR.

![GMVA50_01](http://localhost:3000/immagini/MBDOC_OGG-P_GMVA50/GMVA50_01.png)
I parametri di lancio della funzione sono : 

- Scenario, rappresenta uno degli elementi che caratterizzano i dati della situazione valorizzata di magazzini, in particolare nella tabella dello scenario si imposta la metodologia di calcolo della giacenza finale della sintesi e si impostano le classificazioni da applicare ai campi di sintesi dell'archivio magazzino valorizzato che verranno utilizzati come campi di raggruppamento nelle successive stampe valorizzate.
- Magazzino fiscale, a fronte del quale viene registrata la sintesi valorizzata
- Tipo Costo, da utilizzare nel calcolo della valorizzazione
- Esercizio, è definito nella tabella PER e rappresenta l'intervallo di tempo a fronte del quale vengono registrati i dati di sintesi
- Data limite, può essere inserita manualmente altrimenti viene derivata dal sistema dall' esercizio inserito.  Se la data è inserita manualmente il sistema controlla che sia compresa nei limiti Data Inizio - Data Fine dell'esercizio.

