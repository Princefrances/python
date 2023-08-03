print("PHYSICS CALCULATOR MENU")
print("1] Force\n2] Momentum\n3] Velocity\n4] Acceleration\n5] Exit\n\n")

i = int(input("Choose [1/2/3/4/5]\n"))

if i == 1:
    mass = float(input("Please enter the value for Mass: "))
    acceleration = float(input("Please enter the value for Acceleration: "))

    force = mass * acceleration

    print("************************************************")
    print("The Mass is:", mass, "\nThe Acceleration is:", acceleration, "\nThe Force is:", force)
    print("Thank you :)")
    print("************************************************")

elif i == 2:
    mass = float(input("Please enter the value for Mass: "))
    velocity = float(input("Please enter the value for Velocity: "))

    momentum = mass * velocity

    print("************************************************")
    print("The Mass is:", mass, "\nThe Velocity is:", velocity, "\nThe Momentum is:", momentum)
    print("Thank you :)")
    print("************************************************")

elif i == 3:
    displacement = float(input("Please enter the value for Displacement: "))
    time = float(input("Please enter the value for Time: "))

    velocity = displacement * time

    print("************************************************")
    print("The Displacement is:", displacement, "\nThe Time is:", time, "\nThe Velocity is:", velocity)
    print("Thank you :)")
    print("************************************************")

elif i == 4:
    initial = float(input("Please enter the value for Initial Velocity: "))
    final = float(input("Please enter the value for Final Velocity: "))
    time = float(input("Please enter the value for Time: "))

    acceleration = (final - initial) / time

    print("************************************************")
    print("The Initial Velocity is:", initial, "\nThe Final Velocity is:", final, "\nThe Time is:", time,
          "\nThe Acceleration is:", acceleration)
    print("Thank you :)")
    print("************************************************")

else:
    print("************************************************")
    print("Thank you for using the Calculator")
    print("************************************************")

