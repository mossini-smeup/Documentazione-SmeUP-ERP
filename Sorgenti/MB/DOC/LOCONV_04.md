La compilazione di tutti i programmi deve avvenire con l'opzione 'CO' del SEU, in modo da ottenere un oggetto che opera sia in ambiente carattere sia in ambiente grafico.

Per i programmi che non contengono un video (non hanno una specifica 'F' WORKSTN) il comportamento di questo comando è simile all'opzione 14.

Per i programmi che invece contengono il video, viene creato un menbro sorgente intermedio nel file sorgente £UI_SRC, nella stessa libreria in cui risiederà l'oggetto, che è il sorgente che viene effettivamente compilato, e che è necessario per poter eseguire il DEBUG dei programmi con video.

Se il file £UI_SRC non esiste, esso viene creato in modo automatico. Nello standard verrà reso disponibile questo sorgente, nelle librerie SMEUP_OBJ e SMEUP_DEV.

Presso il cliente, la compilazione con 'CO' dei programmi personalizzati e specifici, necessaria per il loro funzionamento in ambiente grafico, avrà quindi come effetto che anche nella libreria di personalizzazione risiederà il file sorgente £UI_SRC.
