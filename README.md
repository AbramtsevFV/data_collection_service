## Управление ##
### Запуск Docker ###
1) Выполняем команду: 
```
  docker-compose up -d
 ```
    
2) Переходим по адресу:
```
  http://127.0.0.1:8000/
  ```
  Пользователь админ уже добавлен.
 >User: admin
 >
 >Pass: admin
 ### Heroku ###
 '''
 https://servicegithubapi.herokuapp.com/
 '''
 
 ### Работа с API ###
 1) Список пользователей  и их  репозитории в БД:
 
 Docker
 ```
 http://127.0.0.1:8000/api/repo_list/
 ```
 Heroku
 ```
 https://servicegithubapi.herokuapp.com/api/repo_list/
 ```
 2) Обновить/удалить данные по конкретному пользователю:
 
 Docker
 ```
 http://127.0.0.1:8000/api/repo_detail/<int:pk>
 ```
 Heroku
 ```
 https://servicegithubapi.herokuapp.com/api/repo_detail/3
 ```
 <int:pk> - id записи имени пользователя GitHub
 
 3) Добавить нового пользователя и его репозитории из GitHub:
 
 Docker
 ```
 http://127.0.0.1:8000/api/addrepo/
 ```
 Heroku
 ```
 https://servicegithubapi.herokuapp.com/api/addrepo/
 ```
 В теле GET запроса передаются данные в формате JSON:
 ```
 {"name": "AbramtsevFV"}
 ```
 4) Добавить уже имеющегося пользователя и его репозитории:
 
 Docker
 ```
 http://127.0.0.1:8000/api/repo_create/
 ```
 Heroku
 ```
  https://servicegithubapi.herokuapp.com/apirepo_create/
  ```
 В теле POST запроса отправить JSON:
 ```
 {
    "name": "",
    "repository": []
}
```
### Запуск Тестов из  Docker ###
1. Выполняем команду
```
  docker-compose run --rm api ./manage.py test
```
