#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-


import http.cookiejar, urllib.request


def testCookie():
	opener = get_opener()
	response = opener.open('http://www.baidu.com')
	for item in cookie:
		print('Name = ' + item.name)
		print('Value = ' + item.value)




def get_opener():
	cj = http.cookiejar.CookieJar()
	opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
	response = opener.open("http://www.baidu.com")
	print('Name = ')

	
	for item in cj:
		print('Name = ' + item.name)
		print('Value = ' + item.value)
	return opener



if __name__ == "__main__":
	get_opener()



