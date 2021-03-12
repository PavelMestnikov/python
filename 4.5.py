import utils
import sys

argv = sys.argv
for i in range(len(argv)-1):
    print(argv[i+1], "{:.2f}".format(utils.get_currency_rate(argv[i+1], 1)))