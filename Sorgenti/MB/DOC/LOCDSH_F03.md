## Gestione valori Dash
E' possibile passare i valori da mostrare al componente dash in vari modi.
Il primo è tramite una FUN che passa al componente una griglia con 4 colonne che devono contenere, in ordine, valore, unità di misura, descrizione e icona.
Il secondo è tramite una FUN che restituisce una matrice anche con molte colonne, in questo caso tramite gli attributi di setup del componente (IconColName, ValueColName, TextColName e UmColName) si possono specificare i nomi delle colonne da cui prendere i dati da mostrare nel dash.
L'ultima possibilità è, sempre tramite attributi di setup (ForceIcon, ForceValue, ForceUM e ForceText) passare direttamente noi cosa mostrare.
