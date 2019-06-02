

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
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)


#########################

#########################

#########################

#########################

#########################



