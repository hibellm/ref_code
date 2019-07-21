

# FLASK FILTERS


#########################
# SEMANTIC UI ICON DICTIONARY

icontypes = 
{
'file audio': 'm4a,mp3,oga,ogg,webma,wav',
'file archive': '7z,zip,rar,gz,tar',
'file picture': 'gif,ico,jpe,jpeg,jpg,png,svg,webp',
'file pdf': 'pdf', 'file word': 'doc,docx', 'file excel': 'xls,xlsx',
'file film': '3g2,3gp,3gp2,3gpp,mov,qt',
'file code': 'atom,plist,bat,bash,c,cmd,coffee,css,hml,js,json,java,less,markdown,md,php,pl,py,rb,rss,sass,scpt,swift,scss,sh,xml,yml',
'file text': 'txt', 'file video': 'mp4,m4v,ogv,webm',
'globe': 'htm,html,mhtm,mhtml,xhtm,xhtml'
}

# FILTERS THAT CAN BE USED IN A FLASK JINJA TEMPLATE
@app.template_filter('icon_fmt')
def icon_fmt(filename):
    i = 'fa-file-o'
    for icon, exts in icontypes.items():
        if filename.lower().split('.')[-1] in exts:
            i = icon
    return i
    
#########################
# FLATTERN A LIST
mainlist=[["1","2","3"],["8","9","10"]]
flat_list = [item for sublist in mainlist for item in sublist]
print(flat_list)
#########################
# ZIP 2 LISTS
list1=["1","2","3"]
list2=["8","9","10"]
print(f'{list(zip(list1,list2))}')
print(f'{(list1+list2)}')
#########################
# LISTS

print(f"{x for x in 'abracadabra' if x not in 'abc'}")
print(f"{set('abracadabra')}")


#########################
# DICTIONARIES
mydict={}
#Inserting/Updating a single value
mydict['key']='value'
mydict['key2']='value2'
del mydict['key2']

x=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
y=dict(sape=4139, guido=4127, jack=4098)

list(x.keys())
sorted(x.keys())

#########################
#LOOPING
mylist = ['ket','kful','gether']
game = ['tic', 'tac', 'toe']
for i, v in enumerate(game):
    print(i, v)

zlist=list(zip(game,mylist))
for i in zlist:
    print(f"{i[0]}{i[1]}")

#########################

ignore_data = ['dm_','ae_']
datalist = ['dm_','ae','cm_','ec_','demo','dm','ae_','AE_']

for ds in datalist:
    if ds in ignore_data:
        print(f'Ignoring {ds}')
    else:
        print(f'Processing {ds}')



#########################
# Repeat 10 times some code, with a wait of 5 seconds
import time
for i in range(1,11):
        try:
            print(f'{x}worked')
        except Exception as e:
            print(f'Try {i} Failed - {e}')
            time.sleep(5)
            continue
        break

#########################
# REF https://www.programiz.com/python-programming/datetime/strptime
import time
import datetime

# DATETIME DATATYPE
x = datetime.datetime.utcnow()
y=str(x)

# READ IN A STRING INTO A DATETIME"
x2= datetime.datetime.strptime(y,format("%Y-%m-%d %H:%M:%S.%f"))
x3= datetime.datetime.strptime('2019-12-31',format("%Y-%m-%d"))
x4= datetime.datetime.strptime('2019-12-31 10:21:12',format("%Y-%m-%d %I:%M:%S"))


# PRINTING OUT A DATETIME DATATYPE IN DIFFERENT FORMATS
print(f'{x.strftime("%A, %d. %B %Y %I:%M%p")}')
print(f'{x.strftime("%A, %d. %B %Y %I:%M%p %Z")}')
print(f"{x.isoformat()}")
print(f"{x.timetuple()}")


# DIFFERENCE BETWEEN DATES (TIME DELTA)
delta1 = x4-x2
indays = delta1.days

#########################
import unicodedata
a = 'pýtĥöñ is awesome\n'
b = unicodedata.normalize('NFD', a)
b.encode('ascii', 'ignore').decode('ascii')
print(b)

#########################



