#file.3.py
#creates a csv file of various temprature from Celcius to farenheit

def c2f(cel):
    far = float(cel) * 1.8 + 32
    return(far)

f = open('temp.csv','w')

i = [12,54,545,20,-2,-268,-986,-20,0,100,200]
f.write("celcius,farenheit \n")

for data in i:
    if data > -273.16 :
        f.write(str(data) +','+str(c2f(data))+'\n' )
    else:
        f.write(str(data) +','+'Impractical temprature value'+'\n' )

f.close()
