import mechanize
import cookielib
from bs4 import BeautifulSoup

dojo_url = 'http://chicagolandgames.crystalcommerce.com/'

br = mechanize.Browser()

c_jar = cookielib.LWPCookieJar()
br.set_cookiejar(c_jar)

# set br options, based on the references above
br.set_handle_equiv(True)
br.set_handle_gzip(False)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

try:
    dojo_browser = br.open(dojo_url)
except Exception as e:
    print e

try:
    br.select_form(predicate=lambda f: f.attrs.get('method', None) == 'get')
    card_search = br.form.find_control('query')
    card_search.value = 'dromoka\'s command'
    dojo_browser = br.submit()
    search_results = dojo_browser.geturl()
except Exception as e:
    print e


try:
    search_results_page = br.open(search_results)
    search_html = search_results_page.read()
    search_soup = BeautifulSoup(search_html)
    # Let's us know if they're out
    table = search_soup.findAll('span', {'class': 'info'})
    for t in table:
        print t.text
    # Gets the price
    table = search_soup.findAll('td', {'class': 'price'})
    for t in table:
        print str(t.text).strip()
except Exception as e:
    print e

try:
    search_results_page = br.open(search_results)
    search_html = search_results_page.read()
    search_soup = BeautifulSoup(search_html)
    print search_soup
except Exception as e:
    print e