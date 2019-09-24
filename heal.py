import win32serviceutil
import sys
import time

sys.stdout = open("c:\\heal_log.txt", "w+")


def level1():
    win32serviceutil.RestartService('BESClient')


time.sleep(5)


def level2():
    from uninstall import uninstall_agent
    uninstall_agent()


time.sleep(5)


def level3():
    from install import install_agent
    install_agent()


print("Let start")
level1()
print("service restarted")
print("Let us now uninstall the client")
level2()
print("Uninstalled the agent")
print("Lets install bigfix client")
level3()
print("Installed the agent")
print("*********END*******")

