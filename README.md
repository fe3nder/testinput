# Test input
# Test with Python task
<h2>Задача 1 </h2>
<h3> Дан массив целых чисел nums и целое число target. Необходимо вернуть индексы двух чисел таких, чтобы их сумма равна target.
Имеется ровно одно решение. </h3>
<h4>** Один и тот же элемент нельзя использовать дважды.
Результат можно вернуть в любом порядке.** </h4>
<div> Пример 1: </div>
<div> Вход: nums = [2,7,11,15], target = 9 </div>
<div> Выход: [0,1] </div>
Объяснение: Так как nums[0] + nums[1] == 9, возвращаем [0, 1].
 <div> </div>
<div> Пример 2: </div>
<div> Вход: nums = [3,2,4], target = 6</div>
<div> Выход: [1,2]</div>
 <div> </div>
<div> Пример 3:</div>
<div> Вход: nums = [3,3], target = 6</div>
<div> Выход: [0,1] </div>

<h2> Ограничения:
<div> 2 <= nums.length <= 104 </div> 
<div> -109 <= nums[i] <= 109 </div>
<div> -109 <= target <= 109 </div>
</h2>
Необходимо предоставить анализ сложности по времени и памяти в нотации O.
Реализуйте метод solve и сохраните решение в файле <b> test_1.py </b>
 
def solve(nums: List[int], target: int) -> List[int]:
   pass

<h1>Задача 2</h1>

Вы продукт-менеджер и в настоящее время возглавляете команду по разработке нового продукта. К сожалению, последняя версия вашего продукта не прошла проверку качества. Поскольку каждая версия разрабатывается на основе предыдущей версии, все версии после сломанной версии тоже сломаны.
Предположим, у вас есть n версий [1, 2, ..., n] и вы хотите найти первую сломанную версию, из-за которой все последующие будут сломаны.
Вам предоставляется bool API isBrokenVersion (версия), который возвращает, является ли версия сломанной. Реализуйте функцию для поиска первой сломанной версии. Вы должны свести к минимуму количество обращений к API.
 
<div>Пример 1:
<div>Вход: n = 5, bad = 4
<div>Выход: 4
<div> Объяснение: </div>
<div> вызов isBrokenVersion(3) -> false </div>
<div> вызов isBrokenVersion(5) -> true </div>
<div> вызов isBrokenVersion(4) -> true </div>
<div> 4 - первая сломанная версия. </div>
 <div></div>
 <div> Пример 2: </div>
 <div> Вход: n = 1, bad = 1 </div>
 <div> Выход: 1 </div>
 
Ограничения:
1 <= bad <= n <= 231 - 1
Необходимо предоставить анализ сложности по времени и памяти в нотации O.
Реализуйте метод solve и сохраните решение в файле test_2.py
 
# isBrokenVersion API уже реализован.
# def isBrokenVersion(version: int) -> bool:
def solve(n: int) -> int:
   pass​
