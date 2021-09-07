# subgrab
Subgrab finds, probes, and then takes screenshots of subdomains for a given target or set of targets.

![subrab](https://user-images.githubusercontent.com/54566106/132284474-e914457e-7187-4848-ba03-ceabd0d5a113.png)

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
