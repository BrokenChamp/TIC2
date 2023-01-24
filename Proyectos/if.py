def http_error(status):
    match status:
        case 400:
            return "Solicitud incorrecta"
        case 404:
            return"No encontrado"
        case 410:
            return"Soy una tetera"
        case _:
            return"Algo anda mal en internet"