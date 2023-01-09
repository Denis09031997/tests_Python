from car import is_Korea_car


if is_Korea_car('KIA') != 'Да, это корейская машина':
    raise Exception('Упс! Что-то пошло не так.')