import urllib.request
from xml.etree.ElementTree import XML

response = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?route=22&stop=14787')
# reading the data from response.
data = response.read()
# parsing this data into an xml document.
document = XML(data)
for pt in document.findall('.//pt'):
    print(pt.text)
