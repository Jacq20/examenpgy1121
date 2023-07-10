from os import system
system ("cls")

platinum=["disponible", "disponible", "disponible","disponible", "disponible","disponible", "disponible", "disponible","disponible", "disponible",
          "disponible", "disponible", "disponible","no disponible", "no disponible","no disponible", "disponible", "disponible","disponible", "disponible"]
Gold=["disponible", "disponible", "disponible","disponible", "disponible","disponible", "disponible", "disponible","disponible", "disponible",
      "disponible", "disponible", "no disponible","disponible", "disponible","disponible", "disponible", "disponible","disponible", "disponible",
      "disponible", "disponible", "disponible","disponible", "no disponible","disponible", "disponible", "disponible","disponible", "disponible",
      "disponible", "disponible", "disponible","no disponible", "no disponible","no disponible", "disponible", "disponible","disponible", "disponible",
      "disponible", "disponible", "disponible","disponible", "disponible","disponible", "disponible", "disponible","disponible", "disponible"]
silver=["disponible", "disponible", "disponible","disponible", "disponible","disponible", "disponible", "disponible","disponible", "disponible",
      "disponible", "disponible", "disponible","disponible", "disponible","disponible", "disponible", "disponible","disponible", "disponible",
      "disponible", "disponible", "disponible","disponible", "disponible","disponible", "disponible", "disponible","disponible", "disponible",
      "disponible", "disponible", "disponible","disponible", "disponible","disponible", "disponible", "disponible","disponible", "disponible",
      "disponible", "disponible", "disponible","disponible", "disponible","disponible", "disponible", "disponible","disponible", "disponible"]
reserva=[""]
nombre=[]
Rut=[]
name=[]
run=[]
reserv=[""]
nomb=[]
RUT=[]
reser=[""]
while True:
    opcion=input("""
    1. Comprar entradas.
    2. Mostrar ubicaciones disponibles.
    3. ver listado de asistentes.
    4. Mostrar ganancias totales
    5. Salir
    """)
    while True:
        match opcion:
            case "1":
                  print(f"""
                Platinum $120.000
                Gold $80.000
                Silver $50.000
        
                ******platinum******
                Asiento 1 {platinum[0]}
                Asiento 2 {platinum[1]}
                Asiento 3 {platinum[2]}
                Asiento 4 {platinum[3]}
                Asiento 5 {platinum[4]}
                Asiento 6 {platinum[5]}
                Asiento 7 {platinum[6]}
                Asiento 8 {platinum[7]}
                Asiento 9 {platinum[8]}
                Asiento 10 {platinum[9]}
                Asiento 11 {platinum[10]}
                Asiento 12 {platinum[11]}
                Asiento 13 {platinum[12]}
                Asiento 14 {platinum[13]}
                Asiento 15 {platinum[14]}
                Asiento 16 {platinum[15]}
                Asiento 17 {platinum[16]}
                Asiento 18 {platinum[17]}
                Asiento 19 {platinum[18]}
                Asiento 20 {platinum[19]}

                ******Gold******
                Asiento 21 {Gold[0]}
                Asiento 22 {Gold[1]}
                Asiento 23 {Gold[2]}
                Asiento 24 {Gold[3]}
                Asiento 25 {Gold[4]}
                Asiento 26 {Gold[5]}
                Asiento 27 {Gold[6]}
                Asiento 28 {Gold[7]}
                Asiento 29 {Gold[8]}
                Asiento 30 {Gold[9]}
                Asiento 31 {Gold[10]}
                Asiento 32 {Gold[11]}
                Asiento 33 {Gold[12]}
                Asiento 34 {Gold[13]}
                Asiento 35 {Gold[14]}
                Asiento 36 {Gold[15]}
                Asiento 37 {Gold[16]}
                Asiento 38 {Gold[17]}
                Asiento 39 {Gold[18]}
                Asiento 40 {Gold[19]}
                Asiento 41 {Gold[20]}
                Asiento 42 {Gold[21]}
                Asiento 43 {Gold[22]}
                Asiento 44 {Gold[23]}
                Asiento 45 {Gold[24]}
                Asiento 46 {Gold[25]}
                Asiento 47 {Gold[26]}
                Asiento 48 {Gold[27]}
                Asiento 49 {Gold[28]}
                Asiento 50 {Gold[29]}

                ******Silver******
                Asiento 51 {silver[0]}
                Asiento 52 {silver[1]}
                Asiento 53 {silver[2]}
                Asiento 54 {silver[3]}
                Asiento 55 {silver[4]}
                Asiento 56 {silver[5]}
                Asiento 57 {silver[6]}
                Asiento 58 {silver[7]}
                Asiento 59 {silver[8]}
                Asiento 60 {silver[9]}
                Asiento 61 {silver[10]}
                Asiento 62 {silver[11]}
                Asiento 63 {silver[12]}
                Asiento 64 {silver[13]}
                Asiento 65 {silver[14]}
                Asiento 66 {silver[15]}
                Asiento 67 {silver[16]}
                Asiento 68 {silver[17]}
                Asiento 69 {silver[18]}
                Asiento 70 {silver[19]}
                Asiento 71 {silver[20]}
                Asiento 72 {silver[21]}
                Asiento 73 {silver[22]}
                Asiento 74 {silver[23]}
                Asiento 75 {silver[24]}
                Asiento 76 {silver[25]}
                Asiento 77 {silver[26]}
                Asiento 78 {silver[27]}
                Asiento 79 {silver[28]}
                Asiento 80 {silver[29]}
                Asiento 81 {silver[30]}
                Asiento 82 {silver[31]}
                Asiento 83 {silver[32]}
                Asiento 84 {silver[33]}
                Asiento 85 {silver[34]}
                Asiento 86 {silver[35]}
                Asiento 87 {silver[36]}
                Asiento 88 {silver[37]}
                Asiento 89 {silver[38]}
                Asiento 90 {silver[39]}
                Asiento 91 {silver[40]}
                Asiento 92 {silver[41]}
                Asiento 93 {silver[42]}
                Asiento 94 {silver[43]}
                Asiento 95 {silver[44]}
                Asiento 96 {silver[45]}
                Asiento 97 {silver[46]}
                Asiento 98 {silver[47]}
                Asiento 99 {silver[48]}
                Asiento 100 {silver[49]}
                """)
                  op=input("Escoja su asiento: ")
                  match opcion:
                      case "1":
                          if platinum[0]=="disponible":
                            platinum[0]="no disponible"
                            nombre=input("Ingrese su nombre: ")
                            Rut=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                            reserva.append(platinum)
                            print("Su asiento ha sido reservado con exito.")
                            break
                          else:
                            print("Este asiento ya esta resevado.")
                      case "2":   
                            if platinum[1]=="disponible":
                                platinum[1]="no disponible"
                                nombre=input("Ingrese su nombre: ")
                                Rut=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserva.append(platinum)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                      case "3":
                            if platinum[2]=="disponible":
                                platinum[2]="no disponible"
                                nombre=input("Ingrese su nombre: ")
                                Rut=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserva.append(platinum)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                      case "4":
                            if platinum[3]=="disponible":
                                platinum[3]="no disponible"
                                nombre=input("Ingrese su nombre: ")
                                Rut=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserva.append(platinum)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                      case "5": 
                            if platinum[4]=="disponible":
                                platinum[4]="no disponible"
                                nombre=input("Ingrese su nombre: ")
                                Rut=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserva.append(platinum)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                      case "6": 
                            if platinum[5]=="disponible":
                                platinum[5]="no disponible"
                                nombre=input("Ingrese su nombre: ")
                                Rut=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserva.append(platinum)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                      case "7": 
                            if platinum[6]=="disponible":
                                platinum[6]="no disponible"
                                nombre=input("Ingrese su nombre: ")
                                Rut=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserva.append(platinum)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                      case "8": 
                            if platinum[7]=="disponible":
                                platinum[7]="no disponible"
                                nombre=input("Ingrese su nombre: ")
                                Rut=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserva.append(platinum)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                      case "9": 
                            if platinum[8]=="disponible":
                                platinum[8]="no disponible"
                                nombre=input("Ingrese su nombre: ")
                                Rut=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserva.append(platinum)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                      case "10": 
                            if platinum[9]=="disponible":
                                platinum[9]="no disponible"
                                nombre=input("Ingrese su nombre: ")
                                Rut=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserva.append(platinum)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                      case "11": 
                            if platinum[10]=="disponible":
                                platinum[10]="no disponible"
                                nombre=input("Ingrese su nombre: ")
                                Rut=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserva.append(platinum)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                      case "12": 
                            if platinum[11]=="disponible":
                                platinum[11]="no disponible"
                                nombre=input("Ingrese su nombre: ")
                                Rut=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserva.append(platinum)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                      case "13": 
                            if platinum[12]=="disponible":
                                platinum[12]="no disponible"
                                nombre=input("Ingrese su nombre: ")
                                Rut=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserva.append(platinum)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                      case "14": 
                            if platinum[13]=="disponible":
                                platinum[13]="no disponible"
                                nombre=input("Ingrese su nombre: ")
                                Rut=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserva.append(platinum)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                      case "15": 
                            if platinum[14]=="disponible":
                                platinum[14]="no disponible"
                                nombre=input("Ingrese su nombre: ")
                                Rut=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserva.append(platinum)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                      case "16": 
                            if platinum[15]=="disponible":
                                platinum[15]="no disponible"
                                nombre=input("Ingrese su nombre: ")
                                Rut=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserva.append(platinum)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                      case "17": 
                            if platinum[16]=="disponible":
                                platinum[16]="no disponible"
                                nombre=input("Ingrese su nombre: ")
                                Rut=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserva.append(platinum)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                      case "18": 
                            if platinum[17]=="disponible":
                                platinum[17]="no disponible"
                                nombre=input("Ingrese su nombre: ")
                                Rut=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserva.append(platinum)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")

                            if platinum[18]=="disponible":
                                platinum[18]="no disponible"
                                nombre=input("Ingrese su nombre: ")
                                Rut=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserva.append(platinum)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")

                            if platinum[19]=="disponible":
                                platinum[19]="no disponible"
                                nombre=input("Ingrese su nombre: ")
                                Rut=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserva.append(platinum)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            
                      case "2":
                            if Gold[0]=="disponible":
                                Gold[0]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")

                            if Gold[1]=="disponible":
                                Gold[1]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")

                            if Gold[2]=="disponible":
                                Gold[2]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")

                            if Gold[3]=="disponible":
                                Gold[3]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            
                            if Gold[4]=="disponible":
                                Gold[4]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            
                            if Gold[5]=="disponible":
                                Gold[5]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            
                            if Gold[6]=="disponible":
                                Gold[6]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            
                            if Gold[6]=="disponible":
                                Gold[6]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")

                            if Gold[7]=="disponible":
                                Gold[7]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")

                            if Gold[8]=="disponible":
                                Gold[8]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if Gold[9]=="disponible":
                                Gold[9]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")

                            if Gold[10]=="disponible":
                                Gold[10]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            
                            if Gold[11]=="disponible":
                                Gold[11]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")

                            if Gold[12]=="disponible":
                                Gold[12]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")

                            if Gold[13]=="disponible":
                                Gold[13]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")

                            if Gold[14]=="disponible":
                                Gold[14]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")

                            if Gold[15]=="disponible":
                                Gold[15]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")

                            if Gold[16]=="disponible":
                                Gold[16]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")

                            if Gold[17]=="disponible":
                                Gold[17]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")

                            if Gold[18]=="disponible":
                                Gold[18]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")

                            if Gold[19]=="disponible":
                                Gold[19]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")

                            if Gold[20]=="disponible":
                                Gold[20]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")

                            if Gold[21]=="disponible":
                                Gold[21]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            
                            if Gold[21]=="disponible":
                                Gold[21]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")

                            if Gold[21]=="disponible":
                                Gold[21]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")

                            if Gold[22]=="disponible":
                                Gold[22]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")

                            if Gold[23]=="disponible":
                                Gold[24]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")

                            if Gold[25]=="disponible":
                                Gold[25]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")

                            if Gold[26]=="disponible":
                                Gold[26]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")

                            if Gold[27]=="disponible":
                                Gold[27]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")

                            if Gold[28]=="disponible":
                                Gold[28]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")

                            if Gold[29]=="disponible":
                                Gold[29]="no disponible"
                                name=input("Ingrese su nombre: ")
                                run=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reserv.append(Gold)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")

                      case "3":
                            if silver[0]=="disponible":
                                silver[0]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")

                            if silver[1]=="disponible":
                                silver[1]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            
                            if silver[2]=="disponible":
                                silver[2]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[3]=="disponible":
                                silver[3]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[4]=="disponible":
                                silver[4]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[5]=="disponible":
                                silver[5]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[6]=="disponible":
                                silver[6]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[7]=="disponible":
                                silver[7]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[8]=="disponible":
                                silver[8]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[9]=="disponible":
                                silver[9]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[10]=="disponible":
                                silver[10]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[11]=="disponible":
                                silver[11]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[12]=="disponible":
                                silver[12]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[13]=="disponible":
                                silver[13]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[14]=="disponible":
                                silver[14]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[15]=="disponible":
                                silver[15]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[16]=="disponible":
                                silver[16]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                             
                            if silver[17]=="disponible":
                                silver[17]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[18]=="disponible":
                                silver[18]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[19]=="disponible":
                                silver[19]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[20]=="disponible":
                                silver[20]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[21]=="disponible":
                                silver[21]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[22]=="disponible":
                                silver[22]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[23]=="disponible":
                                silver[23]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[23]=="disponible":
                                silver[23]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[23]=="disponible":
                                silver[23]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[24]=="disponible":
                                silver[24]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[25]=="disponible":
                                silver[25]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[26]=="disponible":
                                silver[26]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[27]=="disponible":
                                silver[27]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[28]=="disponible":
                                silver[28]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[29]=="disponible":
                                silver[29]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[30]=="disponible":
                                silver[30]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[31]=="disponible":
                                silver[31]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[32]=="disponible":
                                silver[32]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[33]=="disponible":
                                silver[33]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[34]=="disponible":
                                silver[34]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[35]=="disponible":
                                silver[35]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[36]=="disponible":
                                silver[36]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[37]=="disponible":
                                silver[37]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[38]=="disponible":
                                silver[38]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[39]=="disponible":
                                silver[39]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[40]=="disponible":
                                silver[40]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[41]=="disponible":
                                silver[41]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[42]=="disponible":
                                silver[42]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[43]=="disponible":
                                silver[43]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[44]=="disponible":
                                silver[44]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[45]=="disponible":
                                silver[45]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[46]=="disponible":
                                silver[46]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[47]=="disponible":
                                silver[47]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[48]=="disponible":
                                silver[48]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
                            if silver[49]=="disponible":
                                silver[49]="no disponible"
                                nomb=input("Ingrese su nombre: ")
                                RUT=input("Ingrese su rut sin numero verificador (ejemplo 21223521): ")
                                reser.append(silver)
                                print("Su asiento ha sido reservado con exito.")
                                break
                            else:
                                print("Este asiento ya esta resevado.")
            case "2": 
                print("""
            La ubicacion de los asientos es la siguiente:
                        Escenario
             1  2  3  4  5  6  7  8  9  10
             11 12 13 x  x  x  17 18 19 20
             21 22 23 24 25 26 27 28 29 30
             31 32 x  34 35 36 37 38 39 40
             41 42 43 44 x  46 47 48 49 50
             51 52 53 54 55 56 57 58 59 60
             61 62 63 64 65 66 67 68 69 70
             71 72 73 74 75 76 77 78 79 80
             81 82 83 84 85 86 87 88 89 90
             91 92 93 94 95 96 97 98 99 100 
             
            Las zonas marcadas con x son asientos no disponibles.""")

                            