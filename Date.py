import datetime

def date():
	t=datetime.datetime.now()
	t.strftime('%Y%m%d')
	t = str(t)
	date = t[:4]+t[5:7]+t[8:10]
	return date

