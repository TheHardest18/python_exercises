vacaciones = True
descansos = True

# if vacaciones or descansos:
#     print("Puede Asistir al juego")
# else:
#     print("Esta ocupado no puede asistir al juego")

if not vacaciones or not descansos:
    print("Esta ocupado no puede asistir al juego")
else:
    print("Puede Asistir al juego")