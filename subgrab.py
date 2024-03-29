import requests, re, asyncio, os, time, argparse
from pyppeteer import launch

TIMEOUT = 10

async def take_screenshot(subdomain, path):
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto(url=f'https://{subdomain}', timeout=TIMEOUT*1000)
    await asyncio.wait_for(page.screenshot(path=f'{path}\\{subdomain}.png', fullPage=True), timeout=TIMEOUT)
    await browser.close()

parser = argparse.ArgumentParser()
parser.add_argument(
    'input',
    choices=['single', 'multiple'],
    help='Either input a single domain name or a file with multiple newline-seperated domain names')
parser.add_argument('domain', help='The domain name(s) to search for')
    
args = parser.parse_args()

sites = []
if args.input == 'multiple':
    file = open(args.domain, 'r')
    sites = [x.strip().replace('https://', '').replace('http://', '') for x in file.readlines()]
else:
    sites.append(args.domain.replace('https://', ''))

num_sites = len(sites)

for i, site in enumerate(sites, start=1):
    print('*******************')
    print(f'{i}/{num_sites} Sites')
    site = site.replace('https://', '')

    print('...Searching')
    page = requests.get(f'https://crt.sh/?q={site}')

    wd = os.getcwd()
    path = os.path.join(wd, site + '-' + str(int(time.time())))
    os.mkdir(path)

    print('...Parsing Results')
    site = site.replace('.', '\\.')
    result = re.findall(f"[^>'= ]*{site}", str(page.content))
    result = set([x.replace('*.', '') for x in result])
    num_subs = len(result)

    print('...Testing Subdomains')
    for j, subdomain in enumerate(result, start=1):
        try:
            response = requests.get(f'https://{subdomain}', timeout=TIMEOUT)
            print(f'({j}/{num_subs}) {subdomain}: {response}')
            try:
                print('***TAKING SCREENSHOT***')
                asyncio.get_event_loop().run_until_complete(take_screenshot(subdomain, path))
                print('***SCREENSHOT TAKEN***')
            except:
                print('Unable to take screenshot')
        except:
            print(f'({j}/{num_subs}) {subdomain} failed to connect')



    print('*******************\n')
    
print('Done!')
