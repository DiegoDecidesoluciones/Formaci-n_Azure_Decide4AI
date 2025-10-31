import logging
import os  # <-- Importante: añadir la librería 'os'
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Función que responde a una petición HTTP y lee un secreto.
    """
    logging.info('Python HTTP trigger function processed a request.')

    # --- ESTE ES EL BLOQUE NUEVO QUE AÑADIMOS ---
    # Leemos la variable de entorno que la pipeline de DevOps ha creado para nosotros.
    api_key = os.environ.get("MI_API_KEY_SECRETA")

    # Comprobamos si el secreto existe y devolvemos un error si no.
    if not api_key:
        logging.error("La variable de entorno MI_API_KEY_SECRETA no está configurada.")
        return func.HttpResponse(
             "Error de configuración del servidor. El secreto no se ha encontrado.",
             status_code=500
        )

    # Mostramos solo una parte de la clave por seguridad en los logs
    logging.info(f"La clave de API obtenida de forma segura comienza con: {api_key[:5]}...")
    # --- FIN DEL BLOQUE NUEVO ---

    name = req.params.get('name')
    if name:
        return func.HttpResponse(f"Hello, {name}. La clave secreta ha sido leída correctamente.")
    else:
        return func.HttpResponse(
             "La función se ha ejecutado y ha leído la clave secreta correctamente.",
             status_code=200
        )