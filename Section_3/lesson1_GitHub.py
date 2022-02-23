"""

1) Для начала нужно скопировать к себе только что созданный репозиторий. Для этого применяется термин "склонировать".
На страничке своего проекта нажмите на зеленую кнопку Clone or download и скопируйте адрес из строки:
Чтобы склонировать к себе введите в консоли:

    git clone *адрес вашего репозитория*

Чтобы перейти в каталог репозитория, введите:

    cd *имя репозитория *

2) Чтобы Git отслеживал изменения в ваших файлах, нужно их "добавить". Это специальная команда, которая говорит Git, на какие файлы нужно смотреть и записывать их изменения, а все остальные файлы будут игнорироваться.

Для того чтобы добавить файлы под бдительный взор Git, нужно выполнить команду:

    git add README.md

3) Для того чтобы зафиксировать и сохранить свою работу нужно выполнить "коммит"
Чтобы сделать коммит, нужно ввести команду:

    git commit -m "тут ваше сообщение о коммите"

4) Сейчас у вашего репозитория есть две разные копии — одна локальная, которая уже содержит изменения в файле, и удаленная — на гитхабе. Необходимо наши локальные коммиты положить в удаленный репозиторий. Для этого есть специальная команда git push <репозиторий><название ветки>.

    git push origin main
"""
