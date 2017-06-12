import getPhoto as gp 
import cognitive_face as CF
import glob
from statistics import mean
import time
REF_FOLDERS=glob.glob('./data/reference/*')
REF_FOLDERS.sort()
_, COMP=gp.getPhoto()

def register():
#KEY='ec485be0702142dc9129e2b7619d7e0c'
	KEY='5a2e555569a84e4483b68d3cad9f1f40'
	CF.Key.set(KEY)

def get_img(img_url):
	img=CF.face.detect(img_url)
	img_id=img[0]['faceId']
	return img, img_id

def compare(ref_id, comp_id):
	result=CF.face.verify(ref_id,comp_id)
	check=result['isIdentical']
	confidence=result['confidence']
	#if check==True:
	#	s=''
	#else:
	#	s='do not '
	#ans='The two faces '+s+'belong to same person. The confidence is: '+str(confidence)
	return confidence

def com():
	register()
	#print type(REF)
	#print len(REF)
	for REF_FOLDER in REF_FOLDERS:
		score=[]
		REFS=glob.glob(REF_FOLDER+"/*.jpg")
		REFS.sort()
		for REF in REFS:
			ref, ref_id=get_img(REF)
			comp, comp_id=get_img(COMP)	
			score.append(compare(ref_id, comp_id))
			#time.sleep(10)
			avg=mean(score)
		name=REF_FOLDER[17:]
		if avg >0.5:
			s="belongs to "
		else:
			s="doesn't belong to "

		print "The face "+s+name+". The confidence is: "+str(avg)

if __name__=='__main__':
	com()



