import json;
import pdfkit
from jinja2 import Template


#Logic: when to queue.
# so a cron will query either from sql/no sql table where last video watched time is more than 5 mins group by userid, if any user found then get last video id, select similar question, 
#format them in following json strcuture and  then queue it against user id/email id
# then in queuing service or caching service.

# This json should be read from a queuing service
problems_json =  '{"data":[{ "question":{"title":"Excercise 1.1",\
"text":"An army contingent of 616 members is to march behind an army band of 32 members in a parade. The two groups are to march in the same number of columns. What is the maximum number of columns in which they can march?", \
"images":[]},\
"answer":{"title":"Solution: ", "type":"Watch video Solution at Doubt Nut",\
"text":"To find the maximum columns use HCF(616,32)=HCF(32,8)=8", \
"images":[]}},\
 {"question":{"title":"Excercise 1.2",\
"text":"Find formed product X is used as:", \
"images":["https://i.ibb.co/wwt7MsT/chem.png"]},\
"answer":{"title":"Solution: ", "type":"Watch video Solution at Doubt Nut",\
"text":"", \
"images":[]}\
},{"question":{"title":"Excercise 1.3",\
"text":"A cement company earns a profit of Rs 8 per bag of white cement sold and a loss of Rs 5 per bag of grey cement sold.(a) The company sells 3,000 bags of white cement and 5,000 bags of grey cement in a month. What is its profit or loss?(b) What is the number of white cement bags it must sell to have neither profit nor loss, if the number of grey bags sold is 6,400 bags?", \
"images":[]},\
"answer":{"title":"Solution: ", "type":"Watch video Solution at Doubt Nut",\
"text":"a) 3000*8+5000*(-5)=> 24000-25000Rs => -1000Rs, so He is in loss. b) 6400*(-5)+x+8=0 => 8x=5*6400 => x=4000 so white cement.", \
"images":[]}\
}]}'

#Parse json
problems = json.loads(problems_json)

#Opening template
template = Template(open('page.jinja').read())

#Rendering template
#if you need math formulas to be printed then we can use mathjax.js
rtemplate=template.render(data=problems['data'])

#Outputing in html As we can cache the output so for the next time, we dont need to render it just convert into pdf

with open('out.html', 'w') as file:
    file.write(rtemplate)

#Suppose we cached at file system then we can read it like this
#pdfkit.from_file('out.html', 'out.pdf')

#Converting rendered template to pdf
pdfkit.from_string(rtemplate, 'out.pdf')
