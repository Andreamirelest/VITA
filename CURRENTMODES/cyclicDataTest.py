import os
from collections import namedtuple


_ntuple_diskusage = namedtuple("usage", "total used free")


def diskUsage(path):
	st = os.statvfs(path)
	free = st.f_bavail * st.f_frsize
	total = st.f_blocks * st.f_frsize
	used = ((st.f_blocks - st.f_bfree) * st.f_frsize)
	return _ntuple_diskusage(total, used, free)

def cyclicCheck():
	cyclicThreashold = 300 		#free remaining data limmit - currently randomly chosen number - need to set
	path = os.system("pwd")
	available = diskUsage(path)
	freeData = available[2]

	if freeData <= cyclicThreashold:
		return False
	else:
		return True



#for testing
#path = os.system("pwd")
#available = diskUsage(path)
#print("path checked")
#print(path)
#print(available[2])

#freeData = available[2]

#if freeData <= cyclicThreashold:
#	print("need to reset indexes")


#returns if over set threshold
#print(cyclicCheck(cyclicThreashold))
