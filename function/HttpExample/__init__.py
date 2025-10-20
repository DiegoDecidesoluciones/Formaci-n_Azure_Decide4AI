import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Función de ejemplo que responde a una petición HTTP.
    """
    logging.info('Python HTTP trigger function processed a request.')

    # Intenta obtener el parámetro 'name' de la URL
    name = req.params.get('name')
    if not name:
        try:
            # Si no está en la URL, lo busca en el cuerpo de la petición (JSON)
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )