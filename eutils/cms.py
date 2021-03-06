from backend.cgi import *
from lxml import etree

class cms(cgi):
    
    def __init__(self, siteName):
        return super(cms, self).__init__("http://cms.ncbi.nlm.nih.gov/"+siteName+"/")
        
    def get(self, page):
        page = super(cms, self).get(page+'.xml')
        if (page.status_code == 200):
            root = etree.fromstring(page.content)
            page.title = root.xpath('/html/head/title/text()')[0]
            page.head = etree.tostring(root.xpath('/html/head')[0])
            page.body = etree.tostring(root.xpath('/html/body')[0])
            
        return page
