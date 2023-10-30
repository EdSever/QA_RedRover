-- Покажите содержимое списка клиентов
select * from chinook.customer;
-- Покажите содержимое списка клиентов. Вывести Фамилию, Имя, телефон и е-мейл клиента
select firstname, lastname, phone, email from chinook.customer;
-- Покажите  содержимое продаж. Вывести дату покупки, город в которую совершена продажа и стоимость покупки. Стоимость покупки назвать как "Итог"
select invoicedate, billingCity, total, total as Итог from chinook.invoice;
-- Отобрать все музыкальные треки с ценой  меньше 1 доллара.
select * from chinook.track where unitprice < 1;
-- Отобрать все музыкальные треки с ценой больше 1 доллара.
select * from chinook.track where unitprice > 1;
-- Отобрать все музыкальные треки с ценой не равной 0.99 доллара.
select * from chinook.track where unitprice <> 0.99;
-- Покажите  содержимое продаж. Вывести дату покупки, город в которую совершена продажа и стоимость покупки больше 10 долл. Стоимость покупки назвать как "Итог"
select invoicedate, billingcity, total as Итог from chinook.invoice where total > 10;
-- Как зовут работников-продавцов в компании? Показать фамилии и имена в одном столбце назвав FULL_NAME.
select CONCAT(lastname, ' ', firstname) as FULL_NAME from chinook.employee;
-- Отобрать все треки, композиторами которых являются Red Hot Chili Peppers и Nirvana.
select * from chinook.track where composer = 'Red Hot Chili Peppers' OR composer = 'Nirvana';
-- Показать все продажи с ценой больше 1.98 долларов и меньше 4 долларов
select * from chinook.invoice where total > 1.98 and total < 4;
select * from chinook.invoice where total between 1.98 and 3.99;
-- Показать 3 композиторов из таблицы музыкальных треков
select * from chinook.track where composer IN ('Metallica', 'Green Day', 'Astor Piazzolla');
-- Отобрать все треки в названии которых содержится слово night.
select * from chinook.track where name like '%night%';
-- Отобрать все треки, название которых начинается на букву b
select * from chinook.track where name like 'b%';
-- Получить список треков в которых содержится буква b, где композиторы Apocalyptica и AC/DC
select * from chinook.track where name like '%b%' and composer = 'Apocalyptica' OR composer = 'AC/DC';
