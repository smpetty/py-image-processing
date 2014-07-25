#

def deg2hhmmss(ra,dec):
	ra = ra/15.
	hh = int(ra)
	mm = int((ra-hh)*60.)
	ss = (((ra-hh)*60.)-mm)*60.
	sm = ('%g'%(ss)).split('.')
	if len(sm) > 1: sm = sm[1]
	else: sm = '00'
	dh = int(dec)
	dm = int(abs(dec-dh)*60)
	ds = 60.*(abs(dec-dh)*60 - dm)	
	sm1 = ('%g'%(ds)).split('.')
	if len(sm1) > 1:
		sm1 = sm1[1]
	else: sm1 = '0'
	return '%02d:%i:%02d.%s  %02d:%i:%02d.%s'%(hh,mm,ss,sm[0],dh,dm,ds,sm1[0])
