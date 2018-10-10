#### 启动

config.py  数据库配置

```python
# 开发环境配置
class DevelopConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/uploaddev?charset=utf8'
```

新建 myslq uploaddev 库

```python
# 数据库初始化
python manage.py db init
# 生成迁移文件
python manage.py db migrate
# 执行迁移
python manage.py db upgrade
```

启动

```python
python manage.py runserver
```

访问

```python
http://127.0.0.1:5000/user/upload/   POST
# form表单数据
photo           图片文件
user_id         xxx
icon_type       xxx
```

返回数据

```python
# 
```

