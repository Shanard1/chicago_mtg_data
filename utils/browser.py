import mechanize
import cookielib

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