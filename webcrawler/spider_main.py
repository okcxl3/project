from spider import html_downloader, url_manager, outputer, html_parser
import urllib2
from bs4 import BeautifulSoup
import re
import urlparse
import urllib



class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = outputer.Outputer()
    
    def crawl(self,root_url):
        options = range(187)
        for option in options:
            request = urllib2.Request(root_url)
            request.add_header("user-agent", "Mozilla/5.0")
            response = urllib2.urlopen(request)
            html_cont = response.read()
            soup = BeautifulSoup(html_cont,"html.parser",from_encoding="utf-8")
            href = soup.find("p",{"class":"subheading"}).find_next_sibling().find("a")["href"]
            sub = "0.3.10.21"
            prefix = href[:href.find(sub)]
            pre_url = urlparse.urljoin(root_url, href)
            post_url = urlparse.urljoin(root_url, prefix+"1.3.10.7")
            
            pre_request = urllib2.Request(pre_url)
            pre_request.add_header("user-agent", "Mozilla/5.0")
            pre_response = urllib2.urlopen(pre_request)
            pre_html_cont = pre_response.read()
            soup = BeautifulSoup(pre_html_cont,"html.parser",from_encoding="utf-8")
            c = soup.find_all("select")[1].find("option",value=option).get_text().split("-")
            subject_code = c[0][:len(c[0])-1]
            subject_title = c[1][1:len(c[1])-1]
            new_data={}
            new_data["course_code"] = subject_code
            new_data["title"] = subject_title
            new_data["signal"] = 0
            new_data["credit"] = 0
            new_data["professors"] = 0
            new_data["description"] = 0
            post_request = urllib2.Request(post_url)
            post_request.add_header("user-agent", "Mozilla/5.0")
            data = urllib.urlencode({"sessionPopUp":0, "subjectPopUp":option, "3.10.7.5":"Search Courses"})
            post_request.add_data(data)
            response = urllib2.urlopen(post_request)
            html_cont = response.read()
            
            new_urls = self.parser.parse_url(root_url, html_cont,prefix)
            self.urls.add_new_urls(new_urls)
            
            self.outputer.collect_data(new_data)
            while (self.urls.has_new_url()):
                new_url = self.urls.get_new_url()
                print "crawl %s :" % (new_url)
                html_cont = self.downloader.download(new_url)
                new_data = self.parser.parse(html_cont,prefix)
                self.outputer.collect_data(new_data)
        self.outputer.output_html()
        self.outputer.output_xml()
            
            
            
        
if __name__ == "__main__":
        root_url = "https://w2prod.sis.yorku.ca/Apps/WebObjects/cdm"
        spider = SpiderMain()
        spider.crawl(root_url)