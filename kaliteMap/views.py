from django.shortcuts import render_to_response
import requests
import re
import pygeoip

def mappage(request):
	gic = pygeoip.GeoIP('/Users/Matterhorn/Downloads/GeoLiteCity.dat')
	raw = requests.get("http://kalite.adhocsync.com/static/data/ips.txt").content
	ips = re.findall(".+", raw)
	latlng = []
	for item in ips:
		record = gic.record_by_addr(item)
		if record:
			lat = record['latitude']
			lng = record['longitude']
			latlnglist = lat , lng
			latlng.append(latlnglist)
	return render_to_response('kalite_map.html', {"latlng": latlng})