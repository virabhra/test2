from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio.exceptions import SessionClosedException
import pandas as pd
import pickle
import warnings
import argparse
warnings.filterwarnings("ignore")

def main():
    inputs = input_group('Addition', [
        input("Enter your 1s number: ", type=NUMBER, name='a'),
        input("Enter your 2nd number: ", type=NUMBER, name='b')
    ])
    if (inputs['a'] >= 0 ) and (inputs['b'] >= 0,):
        sum1 =inputs['a']+inputs['b']
        put_text("Your sum output: {}".format(sum1))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(main, port=args.port)
