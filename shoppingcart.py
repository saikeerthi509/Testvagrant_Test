price=0
gstmax=0
product1=""
def cal_gst(product,unitprice,gst,quantity):
	totalprice=unitprice*quantity+gst*(unitprice*quantity)
	if(gst!=0 and unitprice>=500):
		gstmax1=(totalprice-0.05(totalprice))
	
		price+=(totalprice-0.05(totalprice))
		if(gstmax1>gstmax):
			gstmax=gstmax1
			product1=product 
	else:
		price+=totalprice
	return product1
	return gstmax
l=[['leather wallet',1100,0.18,1],['umbrella',900,0.12,1],['cigarette',200,0.28,3],['honey',100,0,2]]
for i in l:
	cal_gst(i)
