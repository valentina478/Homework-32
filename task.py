from bs4 import BeautifulSoup

path_to_my_file = 'C:\\Users\\Valentina\\GoITeens\\2 семестр\\tech\\Homeworks\\Homework №32(22.07)\\homework.html'
with open(path_to_my_file) as file:
    soup = BeautifulSoup(file, 'html.parser')
print('Task 1:')
for data in soup.find('h1'):
    print(data.text)
print('\nTask 2:')
for data in soup.select('.services-list > li '):
    print(data.text)
print('\nTask 3:')
for data in soup.select('footer > p'):
    print(data.text)