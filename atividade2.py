os.system("clear")

nome = str(input("DIgite seu nome:"))
sexo = str(input("Digite o seu sexo(M/F):"))


match sexo:
    case "f":
        estado_civil =str(input("Digite seu estado civil:"))
        if estado_civil == "casada":
            ano = int(input("Digite o ano de casados:"))
            print(f"{nome} do sexo {sexo} e {estado_civil} a {ano} anos")
        else:
            print(f"{nome} estado civil solteira(o)")
    case "m":
        estado_civil = str(input("Digite seu estado civil:"))
        if estado_civil == "casado":
            ano = int(input("DIGITE O ANO DE CASADOS:"))
            print(f"{nome} do sexo {sexo} é {estado_civil} a {ano} anos")

        else:
         print(f"{nome}estado civil solteira(o)")
    case _:
        print("algo esta errado")