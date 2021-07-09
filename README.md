# Game of life!

Идея была в том, чтобы сделать игру, в которой есть клетки, которые едят еду и размножаются. Клетка должна была двигаться по полю матрицы, в которой есть еда <f>, мусор <j>, пустое пространство и другие клетки.

Далее, я хотел симулировать процесс мутаций в коде, для чего я подумал, что стоить создать некий мета-питон - то есть код, который кодирует код, а-ля последовательность аминокислот. Этот код нужен был затем, чтобы мутации были более осмысленны, чтобы можно было бы добавить for loop или while проще, в меньшее количество знаков. Начал этим заниматься и как-то подзабил.

Структура: 

herbivotousMother.py - скрипт первой клетки-матери. 
herbivotous119.py - пример клетки, созданной матерью.
createEnvi.py - создает энваермент (матрицу) с едой, мусором и пустотами.
Был еще metaPython.py, в котором были мои попытки создать код, который бы репрезентировал код питона в более компактно виде, но он был перезаписан, к сожалению.
decodeLib.py - библиотека, в которой содержится перевод из моего кода и код питона.