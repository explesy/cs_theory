Урок 4. О-нотация.
==================

Сложность алгоритмов сортировк selection sort и insertion sort сотавляет O(n^2). Доказательство этого полностью повторяет доказательство сложности алгоритма bubble sort из урока.

Слияние двух массивов со скоростью O(n).

В предоженоом алгоритме представлен цикл, который выполнятеся c = a + b раз, где a - длинна первого массива, b - длинна второго массива. Внутри цикла мы имеем пять условий, во время каждой из итераций выполянтеся лишь одно из них и внутри этих условий происходит одно либо два добавление элементов в результирующий массив. Таким образом в худшем случае, когда у нас два совпадающих массива, получаем с\*alpha\*2 операций, alpha - время выполнения вставки в массив. Из урока нам известно, что alpha = O(n), константы мы можем опустить по определению и в итоге получаем, что сложность представленного алгоритма O(n). 