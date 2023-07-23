# Задание №6
# На семинаре 13 был создан проект по работе с
# пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.

import pytest
from Task4 import User1
from Task5 import Project


@pytest.fixture
def user_create():
    return User1(123, 'Kate')
    
    
@pytest.fixture
def project():
    return Project.load('users.json')


def test_new_User():
    assert User1(123, 'Kate').__str__() == "self.id = 123, self.name = 'Kate', self.level=None"


def test_eq(user_create):
    assert (user_create == User1(123, 'Kate')) == True
    
    
def test_set_level(user_create):
    user_create.set_level(3)
    assert user_create.get_level() == "self.level = 3"
    
    
def test_add(project):
    assert project.add_new_user(3,'Olya', 4321) == "в список пользователей добален пользователь self.id = 4321, self.name = 'Olya', self.level=3"


if __name__ == '__main__':
    pytest.main()