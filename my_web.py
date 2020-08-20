import requests as rq

s = rq.get('http://www.i.ua')
print(s.encoding)
print(s.headers)
print(s.url)
content = str(s.content)

content = content.split('class="news"')[1]
content = content.split('</div>')[0]
link_lines = content.split('href="')

for line in link_lines:
    if 'http' in line and 'click' in line:
        print(line.split('"')[0])

#print(content)


# for i in s.iter_lines():
#    if 'http:/' in str(i):
        #print(str(i))
#        print(str(i)[str(i).find('http'):str(i).find('"', str(i).find('http') + 1)])

