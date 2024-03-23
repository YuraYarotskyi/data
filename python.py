import sys
import create_user

inp = sys.argv[1]
inp2 = sys.argv[2]
inp3 = sys.argv[3]
inp4 = sys.argv[4]


if inp == "login":
    print(create_user.login_usr(inp2, inp3, inp4))
elif inp == "register":
    print(create_user.create_usr(inp2, inp3, inp4))


sys.stdout.flush()