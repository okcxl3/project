import xml.dom.minidom
class Outputer(object):
    
    
    def __init__(self):
        self.datas = []

    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    
    def output_html(self):
        fout = open("output.html","w")
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            if data == 1:
                fout.write("<tr>")
                fout.write("<td>%d</td>" % data)
                fout.write("<td>%d</td>" % data)
                fout.write("<td>%d</td>" % data)
                fout.write("</tr>")
            else:
                if data["signal"] == 0:
                    fout.write("<tr>")
                    fout.write("<td>%s</td>" % (data["course_code"]).encode("utf-8"))
                    fout.write("<td>%s</td>" % (data["title"]).encode("utf-8"))
                    fout.write("</tr>")
                else:
                    fout.write("<tr>")
                    fout.write("<td>%s</td>" % (data["course_code"]).encode("utf-8"))
                    fout.write("<td>%s</td>" % (data["credit"]).encode("utf-8"))
                    fout.write("<td>%s</td>" % (data["title"]).encode("utf-8"))
                    fout.write("<td>%s</td>" % (data["description"]).encode("utf-8"))
                    for prof in data["professors"]:
                        fout.write("<td>%s</td>" % (prof.encode("utf-8")))
                    fout.write("</tr>")
        
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
   
    def output_xml(self):
        fout = open("output.xml","w")
        fout.write('<?xml version="1.0" encoding="UTF-8"?>')
        fout.write("<courseSet>")
        count = 0
        length = len(self.datas)
        for data in self.datas:
            if (data["signal"] == 0 and count == 0):
                fout.write("<courseSubject>")
                fout.write("<courseSubjectCode>")
                fout.write(data["course_code"].encode("utf-8"))
                fout.write("</courseSubjectCode>")
                
                fout.write("<courseSubjectTitle>")
                fout.write(data["title"].encode("utf-8"))
                fout.write("</courseSubjectTitle>")
            
            
            elif data["signal"] == 1: 
                fout.write("<course>")
                fout.write("<courseCode>")
                fout.write(data["course_code"].encode("utf-8"))
                fout.write("</courseCode>")
                
                fout.write("<credit>")
                fout.write(data["credit"])
                fout.write("</credit>")
                
                fout.write("<courseTitle>")
                fout.write(data["title"].encode("utf-8"))
                fout.write("</courseTitle>")
                
                fout.write("<description>")
                fout.write(data["description"].encode("utf-8"))
                fout.write("</description>")
                
                for prof in data["professors"]:
                    fout.write("<professor>")
                    fout.write(prof.encode("utf-8"))
                    fout.write("</professor>")
                fout.write("</course>")
                if count == length - 1:
                    fout.write("</courseSubject>")
           
            elif (data["signal"] == 0 and count != 1):
                fout.write("</courseSubject>")
                fout.write("<courseSubject>")
                fout.write("<courseSubjectCode>")
                fout.write(data["course_code"].encode("utf-8"))
                fout.write("</courseSubjectCode>")
                fout.write("<courseSubjectTitle>")
                fout.write(data["title"].encode("utf-8"))
                fout.write("</courseSubjectTitle>")
            
            
            count = count + 1
        fout.write("</courseSet>")
        fout.close()
        
    
        
    
    
    
    
    
    



