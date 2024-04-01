import turtle


print("______         _                                 _____                     _                \n");
print("| ___ \       | |                               /  __ \                   | |               \n");
print("| |_/ /  ___  | | _   _   __ _   ___   _ __     | /  \/ _ __   ___   __ _ | |_   ___   _ __ \n");
print("|  __/  / _ \ | || | | | / _` | / _ \ | '_ \    | |    | '__| / _ \ / _` || __| / _ \ | '__|\n");
print("| |    | (_) || || |_| || (_| || (_) || | | |   | \__/\| |   |  __/| (_| || |_ | (_) || |   \n");
print("\_|     \___/ |_| \__, | \__, | \___/ |_| |_|    \____/|_|    \___| \__,_| \__| \___/ |_|   \n");
print("                   __/ |  __/ |                                                             \n");
print("                  |___/  |___/                                                              \n");


angles = int(input("Specify the number of angles:"));


turtle.reset();


for i in range(angles):
    turtle.forward(100);
    turtle.right(360/angles);