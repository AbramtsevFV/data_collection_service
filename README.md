## Управление ##
### Запуск Docker ###
1) Выполняем команду: 
```
  docker-compose up -d
 ```
    
2) Переходим по адресу
```
  http://127.0.0.1:8000/
  ```
  Пользователь админ уже добавлен.
 >User: admin
 >
 >Pass: admin
 
 
 ### Работа с API ###
 1) Список пользователей  и их  репозитории в БД
 ```
 http://127.0.0.1:8000/api/repo_list/
 ```
 2) Обновить/удалить данные по конкретному пользователю
 ```
 http://127.0.0.1:8000/api/repo_detail/<int:pk>
 ```
 <int:pk> - id записи имени пользователя GitHub
 
 3) Добавит нового пользователя и его репозитории из GitHub
 ```
 http://127.0.0.1:8000/api/addrepo/
 ```
 В теле GET запроса передаются данные в формате JSON:
 ```
 {"name": "AbramtsevFV"}
 ```
 4) Добавить уже имеющегося пользователя и его репозитории.
 ```
 http://127.0.0.1:8000/api/repo_create/
 ```
 В тетле POST запроса отправить JSON:
 ```
 {
    "name": "",
    "repository": []
}
```
