# coding: utf-8
import re
import matplotlib.pyplot as plt
import numpy as np
import qrdrow as qr

def main():
  fp = open("square.txt")
  convert_qr(fp)
  qr.qr_drow()

  fp.close()

def convert_qr(fp):
  s = ""
  for line in fp.readlines():
    line1 = re.sub("[a-z]", '0 ', line)
    line2 = re.sub("[A-Z]", "255 ", line1)
    s+= line2
    s+= "\n"

  with open("qr_data.txt", "w") as f:
    f.write(s)


if __name__=='__main__':
  main()
