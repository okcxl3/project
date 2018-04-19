from bs4 import BeautifulSoup
import re
import urlparse
class HtmlParser(object):
    
    
    def _get_new_data(self, soup,prefix):
        res_data={}
        node = soup.find("p",{"class":"heading"})
        if node is None:
            print "nonno"
            return 1
        node = node.find("font")
        split = node.get_text().split()
        course_code = split[0] + " " + split[1]
        res_data["signal"] = 1
        res_data["course_code"] = course_code[(course_code.find("/")+1):]
        res_data["credit"] = split[2]
        concat = ""+split[3][0:]
        for i in range(4,len(split)):
            concat = concat + " " + split[i]
        res_data["title"] = concat
        
        description_node =  node = soup.find("p",{"class":"heading"}).find("font").find_parent().find_parent().find_parent().find_parent().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling()
        description_text_split = description_node.get_text().split()
        description_text = " ".join(description_text_split)
        res_data["description"] = description_text
        nodes = soup.find_all("a",href=re.compile(r""+prefix+"\d+\.3\.10\.23\.\d\.12\.0"))
        profs = set()
        for node in nodes:
            profs.add(node.get_text())
        res_data["professors"] = profs
        return res_data
    
     
    def parse(self,html_cont,prefix):
        if html_cont is None:
            return
        soup = BeautifulSoup(html_cont,"html.parser",from_encoding="utf-8")
        new_data = self._get_new_data(soup,prefix)
        return new_data

    
    def parse_url(self,root_url,html_cont,prefix):
        if html_cont is None:
            return
        soup = BeautifulSoup(html_cont,"html.parser",from_encoding="utf-8")
        new_urls = list()
        links = soup.find_all("a",href=re.compile(r""+prefix+"\d+\.3\.10\.8"))
        for link in links:
            new_url = link["href"]
            print new_url
            new_full_url = urlparse.urljoin(root_url, new_url)
            new_urls.append(new_full_url)
        return new_urls
        
    
    
