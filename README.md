# subgrab
Subgrab finds, probes, and then takes screenshots of subdomains for a given target or set of targets.

![subgrab2](https://user-images.githubusercontent.com/54566106/132619263-601c15f3-9205-466a-816f-bce983311c01.png)

## Installation
`git clone https://github.com/brianbutchart/subgrab.git`

## Dependencies
Install pyppeteer before running subgrab:

`pip install pyppeteer`

## Usage
```
usage: subgrab.py [-h] {single,multiple} domain

positional arguments:
  {single, multiple}  Either input a single domain name or a file with multiple newline-
                      seperated domain names
  domain              The domain name(s) to search for

optional arguments:
  -h --help           show this help message and exit
```
## Examples
`py subgrab.py single website.com`

`py subgrab.py multiple websites.txt`
