import cognitive_face as CF

#input addresses of reference face and comparison face. The addresses can be local address or internet url
REF='./ref.jpeg'
COMP='./comp.jpg'

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
	if check==True:
		s=''
	else:
		s='do not '
	ans='The two faces '+s+'belong to same person. The confidence is: '+str(confidence)
	return ans

def com(r,c):
	register()
	ref, ref_id=get_img(r)
	comp, comp_id=get_img(c)	
	print compare(ref_id, comp_id)

if __name__=='__main__':
	com(REF,COMP)
