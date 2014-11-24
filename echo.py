import urllib2

ip = raw_input("what is your ip address?:")
while not ip:
	ip = raw_input("You did not enter an IP. What is your ip address?:")
site = ("http://api.hostip.info/get_html.php?ip=" + ip)
locate = urllib2.urlopen(site)
data = locate.read()
locate.close()
print data

