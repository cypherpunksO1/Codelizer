# Codelyzer

Projects researcher

# .codelizer_ignore

Позволяет указать файлы и директории, которые не должны включаться в статистику

#### Как это работает

Представим проект с файловой структурой:

```gitignore
src
| folder 
| | config.yaml
| somefile.txt
| code.py
the_big_docs.txt
the_big_docs2.txt
the_big_doc3.txt
app.py
```

Мы видим нежелательные для подсчёта .txt и .yaml файлы, но мы не хотим добавлять их в статистику. 

Эту дилемму призван решать `.cdl_ignore` — специальный файл игнорирования.

#### Указываем игнорируемый файл

Мы можем указать игнорируемый файл:

```gitignore
# .cdl_ignore

code.py
```

Так выглядела структура проекта для `codelizer` до обновления `.cdl_ignore`:

```gitignore
src
| folder 
| | config.yaml
| somefile.txt
| code.py
the_big_docs.txt
the_big_docs2.txt
the_big_doc3.txt
app.py
```

Так после:

```gitignore
src
| folder 
| | config.yaml
| somefile.txt
the_big_docs.txt
the_big_docs2.txt
the_big_doc3.txt
app.py
```

#### Указываем игнорируемое расширение файла

В нашем проекте развелось весьма приличное количество .txt файлов. Мы можем не указывать каждый из них по отдельности, а указать игнорируемый тип:

```gitignore
# .cdl_ignore

*.txt
```

Так выглядела структура проекта для `codelizer` до обновления `.cdl_ignore`:

```gitignore
src
| folder 
| | config.yaml
| somefile.txt
| code.py
the_big_docs.txt
the_big_docs2.txt
the_big_doc3.txt
app.py
```

Так после:

```gitignore
src
| folder 
| | config.yaml
| code.py
app.py
```

Как мы видим, ненужные файлы пропали. 
Убедиться в этом мы также можем написав
`./codelizer --tree`

```python
+-------------+-------+
|     File    | Lines |
+-------------+-------+
| config.yaml |   0   |
|   code.py   |   0   |
|    app.py   |   0   |
+-------------+-------+
```


#### Указываем папку для игнорирования:
Мы можем также игнорировать папку полностью, указывая `/` после названия папки:

```gitignore
# .cdl_ignore

folder/
```

Так выглядела структура проекта для `codelizer` до обновления `.cdl_ignore`:

```gitignore
src
| folder 
| | config.yaml
| somefile.txt
| code.py
the_big_docs.txt
the_big_docs2.txt
the_big_doc3.txt
app.py
```

Так после:

```gitignore
src
| somefile.txt
| code.py
the_big_docs.txt
the_big_docs2.txt
the_big_doc3.txt
app.py
```

# Flags
- -dir — позволяет просмотреть указанную директорию
- --file — позволяет просмотреть указанный файл

- --exd — исключает статистику директорий
- --exf — исключает статистикую файлов
- --exl - исключает статистику количества строк


# Установка codelizer в систему

Разрешите выполнение файла через chmod:
```bash
chmod +x weather
```

Создайте ярлык на скрипт:
```bash
sudo ln -s $(pwd)/weather /usr/local/bin/
```