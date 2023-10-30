-- Посчитать количество строк в таблице customer
select * from chinook.customer;
select count(*) from chinook.customer;
select count(Company) from chinook.customer;
select * from chinook.customer where Company is not null;
-- найти все счет-фактуры
select * from chinook.invoice;
-- подсчитать общее количество счет-фактур
select count(*) from chinook.invoice;
-- подсчитать количество покупок, где ИД покупателя 1. Назвать столбец - кол-во покупок
select count(*) 'кол-во_покупок' from chinook.invoice where CustomerId = 1;
-- Просуммировать стоимость покупок по всем счет-фактурам
select sum(total) as 'сумма с-ф' from chinook.invoice;
-- Найти максимальную сумму среди счет-фактур
select max(total) as 'сумма с-ф' from chinook.invoice;
-- найти среднюю сумму среди счет-фактур
select avg(total) as 'сумма с-ф' from chinook.invoice;
-- ceiling
select ceiling(avg(total)) as 'сумма с-ф' from chinook.invoice;
select avg(total * 0.95) as 'сумма с-ф' from chinook.invoice;
select ceiling(avg(total * 0.95)) as 'сумма с-ф' from chinook.invoice;
-- floor
select floor(avg(total)) as 'сумма с-ф' from chinook.invoice;
select avg(total * 0.95) as 'сумма с-ф' from chinook.invoice;
select floor(avg(total * 0.95)) as 'сумма с-ф' from chinook.invoice;
-- round
select round(avg(total)) as 'сумма с-ф' from chinook.invoice;
select avg(total * 0.95) as 'сумма с-ф' from chinook.invoice;
select round(avg(total * 0.95)) as 'сумма с-ф' from chinook.invoice;
select power(round(avg(total * 0.95)), 2) as 'сумма с-ф' from chinook.invoice;
select round(avg(total * 0.95), 2) as 'сумма с-ф' from chinook.invoice;
-- Отсортируйте страны в порядке возрастания/убывания 
select * from chinook.customer;
select Country from chinook.customer ORDER BY Country;
select Country from chinook.customer ORDER BY Country DESC;
-- Отсортируйте уникальные страны в порядке возрастания/убывания
select distinct Country from chinook.customer ORDER BY Country;
-- Посчитайте количество покупателей из каждой страны
select distinct country from chinook.customer;
select country, customerId from chinook.customer group by country;
-- ??
 select distinct country, count(*)  from chinook.customer;
 select country, count(*) from chinook.customer group by country;
-- показать всех исполнителей и посчитать общую стоимость треков. Столбцу unitPrice дать название total
select * from chinook.artist;
select composer, sum(UnitPrice) as total from chinook.track group by composer;
-- HAVING
/* Найдите счета-фактуры выставленные в страны с общей суммой более 100 долларов. 
Выведите страну и стоимость. Столбцу total дать название total_sum */
select * from chinook.invoice;
select BillingCountry, sum(total) total_sum from chinook.invoice where sum(total) > 100 group by BillingCountry;
select BillingCountry, sum(total) total_sum from chinook.invoice group by BillingCountry having total_sum > 100;
-- LIMIT
select * from chinook.invoice LIMIT 3;
-- покажите сотрудника, который старше всех 
select * from chinook.employee order by BirthDate LIMIT 1;
-- покажите 3 сотрудников, которые старше всех
select * from chinook.employee order by BirthDate LIMIT 3;
