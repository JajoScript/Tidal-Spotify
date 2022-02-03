# Dependencias.
from dotenv import load_dotenv;
import os;
import tidalapi;

# Cargar variables de entorno.
config = load_dotenv(".env");
my_session_id:str = os.environ['SESSION_ID'];
my_token_type:str = os.environ['TOKEN_TYPE'];
my_access_token:str = os.environ['ACCESS_TOKEN'];
my_refresh_token:str = os.environ['REFRESH_TOKEN'];
my_playlist_uri:str = os.environ['PLAYLIST_URI'];



# Funciones.
def main() -> None:
    # Inicio de sesión.
    session = tidalapi.Session();
    session.load_oauth_session(session_id=my_session_id, token_type=my_token_type, access_token=my_access_token, refresh_token=my_refresh_token);

    if session.check_login():
        print("[DEV] Sesion iniciada.");

        # Obtener información de la playlist.
        mi_playlist = session.get_playlist(my_playlist_uri);
        print(5*"-" + "PLAYLIST" + 5*"-");
        print(f"[DEV] nombre: {mi_playlist.name}");
        print(f"[DEV] description: {mi_playlist.description}");
        print(f"[DEV] numero de temas: {mi_playlist.num_tracks}");
        print(f"[DEV] duracion: {mi_playlist.duration}");
    else:
        print("[DEV] Sesion no iniciada.");

# Calls.
if __name__ == '__main__':
    main();