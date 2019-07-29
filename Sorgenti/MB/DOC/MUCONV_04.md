# Modello di conversione

Cosa intendiamo per conversione?
la conversione è un processo di trasformazione che si può articolare in più fasi in base al tipo di oggetto; tipicamente abbiamo le fasi di esportazione, importazione, restore e compilazione per gli oggetti che lo prevedono (file, moduli e programmi)
Una fase di conversione può essere caratterizzata da uno
 :  : DEC T(SS) P(B£W) K(MU) D(stato) L(1)

![MUCONV_04A](http://localhost:3000/immagini/MUCONV_04/MUCONV_04A.png)![MUCONV_04F](http://localhost:3000/immagini/MUCONV_04/MUCONV_04F.png)
Come da figura, il modello di conversione prevede 3 fasi operative : 


- **T2M (text to model)** :  l'oggetto originario viene trasformato in un modello neutro che ne rappresenta la struttura
- **M2M (model to model)** :  sul modello vengono effettuate una serie di trasformazioni ed ottimizzazioni. Le fasi M2M possono essere
più d'una.
- **M2T (model to text)** :  dal modello ottimizzato prodotto al passo 2 viene generato l'oggetto del sistem di destinazione


Questo modello di conversione a tre fasi è adottato nel processo di conversione di oggetti di tipo diverso.


- **Sorgenti** :  trasformazione di sorgenti (RPG/CL) nel formato di destinazione (Java)

![MUCONV_04B](http://localhost:3000/immagini/MUCONV_04/MUCONV_04B.png)
- **Database** :  trasformazione di tabelle DB nel formato origina (DB2400) nelle corrispettive tabelle del DB di destinazione (DB2, SQLServer o altro..)

![MUCONV_04C](http://localhost:3000/immagini/MUCONV_04/MUCONV_04C.png)
- **Sistema** :  trasformazione oggetti del sistema originario (OS400) nei corrispettivi oggetti nel sistema di destinazione (As.UP)

![MUCONV_04D](http://localhost:3000/immagini/MUCONV_04/MUCONV_04D.png)







