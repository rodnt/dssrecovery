# -*- encoding: utf-8 -*-

from ds_store import DSStore
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="Path to the DS_Store file", required=True)
parser.add_argument("-t", "--type", help="Type : Iloc, bwsp, lsvp, lsvP, icvp", default='Iloc')
args = parser.parse_args()

dsstore = DSStore.open(args.path, 'r+')
for data in tqdm(dsstore):
    data = str(data)
    entry = data.translate(None, "<>")
    entry = entry.split(' ')

    if(entry[1] == args.type):
        print(entry[0])

