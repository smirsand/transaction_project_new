<a id="anchor"></a>

____Project_transaction____  

__Назначение проекта__

Проект для чтения банковских операций и вывода 5 последних выполненных клиентом операций, в формате:

> <дата перевода> <описание перевода>  
<откуда> -> <куда>  
<сумма перевода><валюта>

__Описание проекта__

Проект предназначен для чтения данных из файла и вывода последних 5 операций в формате, понятном для пользователя.
Он читает файл в формате JSON.

__Начало работы__

Для начала работы с проектом, вам необходимо склонировать его репозиторий на свое устройство и установить зависимости
с помощью менеджера пакетов. Файл с банковскими операциями в формате JSON находится в проекте.

__Использование__

Чтобы запустить проект, необходимо запустить файл number_of_transaction.py.
Затем он прочитает файл и выведет последние 5 операций, выполненных клиентом.

__Примеры__

Пример вывода для одной операции:

> 14.10.2018 Перевод организации  
> Visa Platinum 7000 79** **** 6361 -> Счет **9638  
> 82771.72 руб.

[Вверх](#anchor)