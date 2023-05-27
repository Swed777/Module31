# TODO здесь писать код
import requests
import json
import re
from typing import List

# В данном случае запрос request.get заменен на загрзку сайта из файла html
with open('examples.html', 'r') as f:
    text = f.read()
# По итогу вы так же получаете код сайта в виде одной строки


pattern = r'<h3>(.*)</h3>'      # (.*) - поиск всего содержимого между точкой входа и выхода
final : List[str] = re.findall(pattern, text)
print(final)




#_____________________
 # тренировка get запроса
# req = requests.get('http://www.columbia.edu/~fdc/sample.html')
# req1 = requests.get("https://swapi.dev/api/people/3/")
# req_dict = json.loads(req1.text)
# print(req_dict)

'''
Задача 5. Web scraping
Что нужно сделать
Дан несложный пример HTML-страницы: Sample Web Page.
Изучите код этой страницы и реализуйте программу, которая получает список всех подзаголовков сайта
 (они заключены в теги <h3>).

Ожидаемый результат:

['CONTENTS', '1. Creating a Web Page', '2. HTML Syntax', '3. Special Characters', '4. Converting Plain Text to HTML', 
'5. Effects', '6. Lists', '7. Links', '8. Tables', '9. Viewing Your Web Page',
 '10. Installing Your Web Page on the Internet', '11. Where to go from here', '12. Postscript: Cell Phones']

Сделайте так, чтобы программа работала для любого сайта, где есть такие теги.'''