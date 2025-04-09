from abc import ABC, abstractmethod
from typing import Optional, List, TypeVar, Generic, Dict
from app.extensions import db

T = TypeVar('T')

class Repository(ABC, Generic[T]):
    @abstractmethod
    def add(self, obj: T) -> None:
        pass

    @abstractmethod
    def get(self, obj_id: int) -> Optional[T]:
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        pass

    @abstractmethod
    def update(self, obj_id: int, data: dict) -> Optional[T]:
        pass

    @abstractmethod
    def delete(self, obj_id: int) -> None:
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name: str, attr_value) -> Optional[T]:
        pass


class InMemoryRepository(Repository[T]):
    def __init__(self):
        self._storage: Dict[int, T] = {}
        self._current_id: int = 0

    def add(self, obj: T) -> None:
        self._current_id += 1
        self._storage[self._current_id] = obj

    def get(self, obj_id: int) -> Optional[T]:
        return self._storage.get(obj_id)

    def get_all(self) -> List[T]:
        return list(self._storage.values())

    def update(self, obj_id: int, data: dict) -> Optional[T]:
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
            self._storage[obj_id] = obj
        return obj

    def delete(self, obj_id: int) -> None:
        if obj_id in self._storage:
            del self._storage[obj_id]

    def get_by_attribute(self, attr_name: str, attr_value) -> Optional[T]:
        return next((obj for obj in self._storage.values() if getattr(obj, attr_name) == attr_value), None)


class SQLAlchemyRepository(Repository[T]):
    def __init__(self, model: T):
        self.model = model
        
    def add(self, obj: T) -> Optional[T]:
        db.session.add(obj)
        db.session.commit()
        return obj

    def get(self, obj_id: int) -> Optional[T]:
        return self.model.query.get(obj_id)

    def get_all(self) -> List[T]:
        return self.model.query.all()

    def update(self, obj_id: int, data: dict) -> Optional[T]:
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
            db.session.commit()
        return obj

    def delete(self, obj_id: int) -> None:
        obj = self.get(obj_id)
        if obj:
            db.session.delete(obj)
            db.session.commit()

    def get_by_attribute(self, attr_name: str, attr_value) -> Optional[T]:
        return self.model.query.filter_by(**{attr_name: attr_value}).first()