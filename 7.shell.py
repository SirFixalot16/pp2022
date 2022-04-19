import os
import subprocess
import signal
import sys

# Function to handle executing commands and handle piping
def execute_command(command):
    try:
        if "|" in command:
            # Save for restoring later on
            s_in, s_out = (0, 0)
            s_in = os.dup(0)
            s_out = os.dup(1)

            # First command takes commandut from stdin
            fdin = os.dup(s_in)

            # Iterate over all the commands that are piped
            for cmd in command.split("|"):
                # fdin will be stdin if it's the first iteration
                # and the readable end of the pipe if not.
                os.dup2(fdin, 0)
                os.close(fdin)

                # Restore stdout if this is the last command
                if cmd == command.split("|")[-1]:
                    fdout = os.dup(s_out)
                else:
                    fdin, fdout = os.pipe()

                # Redirect stdout to pipe
                os.dup2(fdout, 1)
                os.close(fdout)

                try:
                    subprocess.run(cmd.strip().split())
                except Exception:
                    print("psh: command not found: {}".format(cmd.strip()))

            # Restore stdout and stdin
            os.dup2(s_in, 0)
            os.dup2(s_out, 1)
            os.close(s_in)
            os.close(s_out)
        else:
            subprocess.run(command.split(" "))
    except Exception:
        print("psh: command not found: {}".format(command))

# Function to convert to absolute path and change directory
def psh_cd(path):
    try:
        os.chdir(os.path.abspath(path))
    except Exception:
        print("cd: no such file or directory: {}".format(path))


def psh_help():
    print("""psh: shell implementation in Python.
          Supports all basic shell commands.""")

# Function eliminate KeyboardInterrupt
def signal_handler(signal, frame):
  sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

def main():
    while True:
        inp = input("[dinkpachinko@localhost ~]$ ")
        if inp == "exit":
            break
        elif inp[:3] == "cd ":
            psh_cd(inp[3:])
        elif inp == "help":
            psh_help()
        else:
            execute_command(inp)


if '__main__' == __name__:
    main()