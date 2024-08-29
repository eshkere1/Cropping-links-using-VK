# Обрезка ссылок с помощью VK

Этот код может сократить ссылку или показать количество переходоа по ней, если сразу ввести короткую ссылку

### Как установить
.
Вам понадобится сервисный ключ доступа в vk. Вот [документация](https://dev.vk.com/ru/api/access-token/getting-started). О том как его получить.
Далее после того как вы получили ключ в папке с проектом нужно создать переменную окружения VK_TOKEN="", где в кавычках будет ваш ключ. Вот [статья](https://learn.microsoft.com/ru-ru/sql/integration-services/lesson-1-1-creating-working-folders-and-environment-variables?view=sql-server-ver16) о том как создать переменную среды. Это нужно, для того чтобы скрыть ваш ключ от других пользователей.

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Пример использывания кода

Если ввести полную ссылку
```
PS C:\Users\piv17\api2> python main.py https://www.example.com/
https://vk.cc/cA3kq4
PS C:\Users\piv17\api2> 
```
Если ввести кароткую ссылку
```
PS C:\Users\piv17\api2> python main.py https://vk.cc/cx0cHv
1
PS C:\Users\piv17\api2> 
```
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
 
