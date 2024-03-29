

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

print(f"{[x for x in 'abracadabra' if x not in 'abc']}")
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

# USING MASTER LIST OF VARIABLE INFO

sdtm= [['Event type','DM','USUBJID','Unique subject Id','Identifier','Char','20'],
       ['Event type','DM','AGE','Age at baseline','Identifier','Num','8'],
       ['Event type','DM','BIRTHDT','Birthdate','Time','Char','20'],
       ['Event type','DM','RACE','Race','Identifier','Char','20']
       ]

varlist = [['DM','USUBJID'],['DM','AGE'],['DM','AGEU'],['DM','BIRTHDT'],['DM','ETHNIC'],['CO','USUBJID']]

for var in varlist:
    for ent in sdtm:
        if var[0] in ent[1] and var[1] in ent[2]:
            print(f"A match is {ent[1]}, {ent[2]}")
        elif var[0] in ent[1]:
            print(f"No match is {ent[1]}, {ent[2]}")


###
# YAML
import yaml
import io

#yaml.dump(data, encoding=('utf-8'))
# Write YAML file
# Define data
data = {'a list': [1, 42, 3.141, 1337, 'help', u'€'],
        'a string': 'bla',
        'another dict': {'foo': 'bar',
                         'key': 'value',
                         'the answer': 42,
                         'mylist': ['a','b','c']}}

with io.open('data.yml', 'w', encoding='utf8') as outfile:
    yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)

# Read YAML file
with open("data.yml", 'r') as stream:
    todoproc = yaml.safe_load(stream)


with open("./ref_code/configtest.yml", 'r') as stream:
    configtest = yaml.safe_load(stream)


if configtest['withdl']:
    print('Going to load data')
if configtest['makecsv']:
    print('Going to make csv files')
if configtest['log']['logname']:
    print(f"Going to make log file as {configtest['log']['logname']}")

######################
# TESTING SCHEMA VALIDATION
from schema import Schema, And, Use, Optional

data = [{'name': 'Sue', 'age': '28', 'gender': 'Squid'},
        {'name': 'Sam', 'age': '42'},
        {'name': 'Sacha', 'age': '20', 'gender': 'KID'}]

schema = Schema([{'name': And(str, len),
                  'age':  And(Use(int), lambda n: 18 <= n <= 99),
                  Optional('gender'): And(str, Use(str.lower),lambda s: s in ('squid', 'kid'))}])

validated = schema.validate(data)
print(f"valid? {schema.is_valid(data)}")



data = [{'flags': True ,
         'all': ''}]
schema = Schema([{'flags': bool,
                  'all': And(str,len)}])
validated = schema.validate(data)
print(f"valid? {schema.is_valid(data)}")




# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue. This returns an SQS.Queue instance
queue = sqs.get_queue_by_name(QueueName='test')



# Create a new message
response = queue.send_message(MessageBody='world')

# The response is NOT a resource, but gives you a message ID and MD5
print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))


queue.send_message(MessageBody='boto3', MessageAttributes={
    'Author': {
        'StringValue': 'Daniel',
        'DataType': 'String'
    }
})

# Process messages by printing out body and optional author name
for message in queue.receive_messages(MessageAttributeNames=['Author']):
    # Get the custom author message attribute if it was set
    author_text = ''
    if message.message_attributes is not None:
        author_name = message.message_attributes.get('Author').get('StringValue')
        if author_name:
            author_text = ' ({0})'.format(author_name)

    # Print out the body and author (if set)
    print('Hello, {0}!{1}'.format(message.body, author_text))

    
    # Let the queue know that the message is processed
    message.delete()


import boto3

# Create SQS client
sqs = boto3.client('sqs')

queue_url = 'SQS_QUEUE_URL'

# Receive message from SQS queue
response = sqs.receive_message(
    QueueUrl=queue_url,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=0,
    WaitTimeSeconds=0
)

message = response['Messages'][0]
receipt_handle = message['ReceiptHandle']

# Delete received message from queue
sqs.delete_message(
    QueueUrl=queue_url,
    ReceiptHandle=receipt_handle
)
print('Received and deleted message: %s' % message)
