# Django
A Django template for developer

使用前，需要先装好python，更新pip，还要安装virtualenv，这样就可以在虚拟环境中可以安装django：
```bash
pip install Django
```
最后再安装Django：

实现模型变更的三个步骤：

1. 修改你的模型（在models.py文件中）。
2. 运行`python manage.py makemigrations` ，为这些修改创建迁移文件
3. 运行`python manage.py migrate` ，将这些改变更新到数据库中。

每次开启时，使用`python manage.py runserver`运行网页，默认网址：http://localhost:8000/

如果需要运行django中的程序，可以在项目目录下，即安装了virtualenv下，会有一个叫env的文件，在env同级目录下进入env\Scripts\activate
退出虚拟环境可以使用：deactivate


