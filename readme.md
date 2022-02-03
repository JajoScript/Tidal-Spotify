# Tidal to Spotify

## Variables de entorno
Para el correcto funcionamiento del programa, son necesarias las siguiente variables de entorno:
*   ACCESS_TOKEN
*   REFRESH_TOKEN
*   SESSION_ID
*   TOKEN_TYPE="bearer"
*   PLAYLIST_URI

Las variables son obtenidas desde el sitio: [Tidal](https://listen.tidal.com/). Desde inspeccionar elementos:
    
ir a la pestaña *Application* => *Storage* => *Local Storage* => *_TIDAL_activeSession2* y *_TIDAL_clientUniqueKey*

* La variable SESSION_ID, se encuentra en *_TIDAL_clientUniqueKey*
* Las variables ACCESS_TOKEN, REFRESH_TOKEN, se encuentran en *_TIDAL_activeSession2*
