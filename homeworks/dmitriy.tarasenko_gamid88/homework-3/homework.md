# Объект реального мира : "Коньяк"

#### Класс
Коньяк
        
#### Объект
Коньяк 5*

#### Наследственность 
Коньяк ХО (Экстра олд) или же коньяк 7*. От родителя взято все самое лучшее, 
увеличен срок выстаивания в дубовых бочках

#### Полиморфизм
Коньяки производства Франции, Грузии, Армении. Различия в процессах и рецептуре производства
Суть остается одна - получается и в одном и другом случае коньяк

#### Инкапсуляция
Для коньяка не важно, какой рукой (левой или правой) или какими ножницами стригся виноград
для его производства, кто посадил дуб и чем в последствии скалачивали из него бочку.
Не важно на какой глубине находился погреб в котором напиток обретал свою выдержку.

## SOLID — принципы объекто-ориентированного программирования

#### Single responsibility (принцип единственной ответственности)
Коньяк должен приносить удовольствие производителю, человеку вложившему в него свой труд и душу,
и конечному потребителю, не нужно им промывать сток в раковине или натирать пятки :)

#### Open-closed (принцип открытости / закрытости)
Вы можете оформить бутылку как вам угодно, можете добавлять его в коктейль или выпечку

#### Liskov substitution (принцип подстановки Барбары Лисков)
Как от коньяка 3-хлетней выдержки можно захмелеть при чрезмерном употреблении,
так и от самых редких и дорогих представителей его рода с выдержкой не в один десяток лет

#### Interface segregation (принцип разделения интерфейса)
Опытный производитель конька по маркировке на бутылке может определить из какого винограда,
где выращивался виноград, какие ингридиенты добавлялись в процессе изготовления.

#### Dependency inversion (принцип инверсии зависимостей)
Коньяк принадлежит к классу объектов "Алкогольные напитки", а в свою очередь Коньяк 5*
имеет принадлежность к классу "Коньяк", т.к. является одним из его подтипов