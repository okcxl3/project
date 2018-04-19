import urllib2
import urllib

class HtmlDownloader(object):
    
    
    def download_url(self,url,option):
        if url is None:
            return None
       
        request = urllib2.Request(url)
        data = urllib.urlencode({"sessionPopUp":0, "subjectPopUp":option, "3.10.7.5":"Search Courses"})
        request.add_data(data)
        response = urllib2.urlopen(request)
        
        if (response.getcode() != 200):
            print "code != 200"
            return None
       
        return response.read()
    
    def download(self,url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        
        if (response.getcode() != 200):
            return None
        
        return response.read()
    
    



