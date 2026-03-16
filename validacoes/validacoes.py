def validar_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    return True

def validar_telefone(telefone):
    if len(telefone) < 10 or len(telefone) > 11 or not telefone.isdigit():
        return False
    return True