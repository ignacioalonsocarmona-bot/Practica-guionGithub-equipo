def login(usuario, password): 
    if not password:
        return False    
    print(f"Iniciando sesion para {usuario}")
    return True