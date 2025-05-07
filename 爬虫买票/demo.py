from DrissionPage import ChromiumPage
from DrissionPage import ChromiumOptions

path = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
ChromiumOptions().set_browser_path(path).save()
