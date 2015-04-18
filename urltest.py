import urllib

print 'Hello!'
file = urllib.urlopen('https://google.com')
file1 = urllib.urlopen('http://www.cmu.edu/hub/')

print file.read()
print file1.read()


