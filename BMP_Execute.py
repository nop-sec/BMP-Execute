#!/bin/python3

import sys, getopt, binascii, re
from pwn import *

def main(argv):
   cmd = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hc:",['cmd=""'])
   except getopt.GetoptError:
      print('BMP_Exectute.py -c <command>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('BMP_Convert.py -c <command>')
         sys.exit()
      elif opt in ("-c", "--cmd"):
         cmd = arg
   print('Command is ', cmd)
   ConvertToHex(cmd)

def ConvertToHex(cmd):
   hex = ''
   hex = binascii.hexlify(cmd.encode())
   print("Cmd in hex is: ", hex)
   SplitHex(hex)

def SplitHex(hex):
    hex = hex
    chunks = [hex[i:i+6] for i in range(0, len(hex), 6)]
    header = b'0A0000'
    print('RGB =', tuple(int(header[i:i+2], 16) for i in (0, 2, 4)))
    header = b'0D0A0D'
    print('RGB =', tuple(int(header[i:i+2], 16) for i in (0, 2, 4)))
    for i in chunks:
       elen = len(i) % 3
       if elen:
           i = i + ("00"*elen).encode()
       i = i.decode()
       i.encode()
       hex = p32(int(i,16))
       hex = hex.strip()[:3]
       hex = binascii.hexlify(hex)
       print('RGB =', tuple(int(hex[i:i+2], 16) for i in (0, 2, 4)))

if __name__ == "__main__":
   main(sys.argv[1:])
