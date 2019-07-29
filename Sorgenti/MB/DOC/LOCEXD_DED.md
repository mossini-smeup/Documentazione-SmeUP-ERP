## Scheda
E' possibile utilizzare il Drag & Drop solo su alberi e matrici.
Occorre nel setup del componente definire l'abilitazione al Drag

![LOCEXD_047](http://localhost:3000/immagini/LOCEXD_DED/LOCEXD_047.png)
e successivamente indicare nel dinamismo quale azione deve essere eseguita al Drop.

![LOCEXD_048](http://localhost:3000/immagini/LOCEXD_DED/LOCEXD_048.png)

## Variabili
Per la gestione del Drag & Drop e' stata utilizzata la logica delle variabili array di LoocUp, in questo caso viene passata una variabile che in realta' e' l'elenco di piu' istanze separate da un ; .
![03COMEXD10](http://localhost:3000/immagini/LOCEXD_DED/03COMEXD10.png)In caso di selezione multipla su una matrice, vengono create delle variabili di Sezione nominate FROM.NomeColonnaMatrice. In caso di albero la logica e' la stessa di quella appena esposta;
l'unica differenza e' che nell'albero, non essendoci i nomi colonne come nella matrice, le variabili di sezione si chiamano FROM.SELECTED.T1, FROM : SELECTED.P1, FROM.SELECTED.K1.
Esempio 1 :  Abbiamo una matrice contenente una lista di Fornitori (CNFOR) e ne selezioniamo 3 :      
Le colonne
![LOCEXD_043](http://localhost:3000/immagini/LOCEXD_DED/LOCEXD_043.png)Le colonne della matrice si chiamano : ID_TP per il tipo (colonna nascosta), ID_OG per il codice e ID_DE per la descrizione. Nell'immagine sotto in evidenza le variabili che ci interessano : 
![LOCEXD_044](http://localhost:3000/immagini/LOCEXD_DED/LOCEXD_044.png)
Esempio 2 :  Abbiamo un albero contenente una lista di Collaboratori (CNCOL) e ne selezioniamo 5
![LOCEXD_045](http://localhost:3000/immagini/LOCEXD_DED/LOCEXD_045.png)
Il contenuto delle variabili sara' : 
![LOCEXD_046](http://localhost:3000/immagini/LOCEXD_DED/LOCEXD_046.png)

