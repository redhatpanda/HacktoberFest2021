import urllib.request #using urllib module
url="file:///C:/Users/NFate/Desktop/demo.html" #html file
site=urllib.request.urlopen(url)
data=site.read().decode('utf-8')
print(data) # to read content
