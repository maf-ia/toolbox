import requests

#url = 'http://www.newbiecontest.org/epreuves/hacking/ep2/admin/index.php'
url = 'http://www.newbiecontest.org/epreuves/hacking/Mr_KaLiMaN-htaccess_reloaded/index.php'
cookies = dict(PHPSESSID='7d8a62717e183a6f02d3c52f1d464e38')

# allow_redirects = False

r = requests.get( url, cookies=cookies )
print 'GET'
print r.content

r = requests.post( url, cookies=cookies )
print 'POST'
print r.content

r = requests.put( url, cookies=cookies )
print 'PUT'
print r.content



s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})

# both 'x-test' and 'x-test2' are sent
s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})

# si pb de certif https:
requests.get('https://kennethreitz.org', verify=False)