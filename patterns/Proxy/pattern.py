# proxy.py
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def query(self, sql):
        pass

class RealDatabase(Database):
    def query(self, sql):
        print(f"Выполнение запроса: {sql}")
        return f"Результат запроса: {sql}"

class DatabaseProxy(Database):
    def __init__(self, real_database, user_role):
        self._real_database = real_database
        self._user_role = user_role
        self._cache = {}
    
    def query(self, sql):
        if self._user_role != "admin" and "DELETE" in sql.upper():
            print("Ошибка: У вас нет прав для выполнения DELETE запросов")
            return None
        
        if sql in self._cache:
            print(f"Возвращаем результат из кеша: {sql}")
            return self._cache[sql]
    
        print(f"Логирование: пользователь {self._user_role} выполнил запрос")

        result = self._real_database.query(sql)
        
        self._cache[sql] = result
        
        return result