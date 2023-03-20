# dssrecovery
Small tool to parser .DS_Store files


#### install 

```
$ pipenv shell
$ pipenv install -r Pipfile
$ python3 dssrecovery -p .DS_Store

```

```
usage: dssecovery.py [-h] -p PATH [-t TYPE]

options:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Path to the DS_Store file
  -t TYPE, --type TYPE  Type : Iloc, bwsp, lsvp, lsvP, icvp

```

#### Usage

```bash

python3 dssrecovery.py -p $(curl https://example.com/.DS_Store > DS_Store; echo `pwd`/assets

#or 

python3 dssrecovery.py -p .DS_Store

```
