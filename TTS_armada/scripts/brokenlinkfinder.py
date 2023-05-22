import re, sys
import urllib.request
from urllib.parse import urlparse
from multiprocessing import Pool
import unittest

checked = {}
badunique = []
LINK_REGEX = re.compile(r'[\"\'](http.*?)[\\]?[\"\']')
class ImgurRedirectHandler(urllib.request.HTTPRedirectHandler):
    # def http_error_301(self, req, fp, code, msg, headers):
    #     infourl = urllib.response.addinfourl(fp, headers, req.get_full_url(), code)
    #     return infourl  # let 301 redirect go through

    def http_error_302(self, req, fp, code, msg, headers):
        infourl = urllib.response.addinfourl(fp, headers, req.get_full_url(), code)
        if "Location" in headers:
            destination_url = headers["Location"]
            if destination_url.endswith('removed.png'):
                raise urllib.error.HTTPError(req.get_full_url(), 404, "Not Found", headers, fp)
        return infourl  # let 302 redirect go through
    http_error_303 = http_error_307 = http_error_302

opener = urllib.request.build_opener(ImgurRedirectHandler())
urllib.request.install_opener(opener)

def link_getcode(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        return response.getcode()
    
def checklink(url):
    try:
        code = link_getcode(url)
        if code != 200:
            return False
    except urllib.error.URLError as e:
        return False
    return True

def filterbad(url):
    if checklink(url):
        return None
    return url
    
def checkbroken(line):
    bad = []
    if "http" in line: # and "githubusercontent" not in line
        results = LINK_REGEX.findall(line)
        for link in results:
            if link in checked or "githubusercontent" in link:
                continue
            checked[link] = True
            if not checklink(link):
                bad.append(link)
            # Check if link is valid
            # req = urllib.request.Request(link)
            # try:
            #     with urllib.request.urlopen(req) as response:
            #         # if response.getcode() != 200:
            #         #     bad.append(link)
            #         pass
            # except urllib.error.URLError as e:
            #     bad.append(link)
    return bad

def main():
    savefile = r'C:\Users\berge\OneDrive\Documents\My Games\Tabletop Simulator\Saves\TS_Save_1102.json'
    print(f"Checking {savefile}")
    with open(savefile, 'r') as f:
        # For line in file, use regex to find all links
        lines = f.readlines()
        link_arrays = [LINK_REGEX.findall(line) for line in lines]
        links = [item for sublist in link_arrays for item in sublist]
        links = list(set(links))
        with Pool(60) as p:
            results = p.map(filterbad, links)
            results = [r for r in results if r!=None]
            # flat_results = [item for sublist in results for item in sublist]
            for link in results:
                if link not in badunique:
                    badunique.append(link)
                    print(link)
        # for line in f.readlines():
        #     if "http" in line and "githubusercontent" not in line:
        #         results = LINK_REGEX.findall(line)
        #         for link in results:
        #             if link in checked:
        #                 continue
        #             checked[link] = True
        #             # Check if link is valid
        #             req = urllib.request.Request(link)
        #             try:
        #                 with urllib.request.urlopen(req) as response:
        #                     if response.getcode() != 200:
        #                         bad.append(link)
        #                         print()
        #                         print(link)
        #             except urllib.error.URLError as e:
        #                 bad.append(link)
        #                 print()
        #                 print(link)
        #                 print(e.reason)
        #             print(f"\r   {len(checked):>4} Checked, {len(bad):>4} Bad",end="")

class TestGetAreaRectangle(unittest.TestCase):
    # def test_filterbad_bad(self):
    #     self.assertEqual(filterbad("https://imgur.com/D48HkVa.jpg"),"https://imgur.com/D48HkVa.jpg")
    # def test_filterbad_good(self):
    #     self.assertEqual(filterbad("http://i.imgur.com/WQJNmkt.png"),None)
    # def test_404(self):
    #     self.assertRaises(urllib.error.HTTPError, link_getcode, "https://imgur.com/D48HkVa.jpg")
    # def test_200(self):
    #     self.assertEqual(link_getcode("http://i.imgur.com/WQJNmkt.png"), 200)
    # def test_removed(self):
    #     # self.assertRaises(BaseException, checkbroken, "https://imgur.com/D48HkVa.jpg")
    #     self.assertFalse(checklink("https://imgur.com/D48HkVa.jpg"))
    # def test_removed2(self):
    #     self.assertFalse(checklink("https://imgur.com/JKJUB8L.png"))
    # def test_good(self):
    #     self.assertTrue(checklink("http://i.imgur.com/WQJNmkt.png"))
    def test_badmodel(self):
        self.assertTrue(checklink("https://paste.ee/r/6LYTT"))
        
        
if __name__ == '__main__':
    if len(sys.argv)>1 and sys.argv[1] == "test":
        sys.argv = sys.argv[:1]
        unittest.main()
    else:
        main()