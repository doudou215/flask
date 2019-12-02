#encoding: utf-8

from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from app import app
from exts import db
from models import User


manager = Manager(app)
#使用 Migrate 绑定 app db

migrate = Migrate(app,db)

#添加脚本迁移的命令到manager中

manager.add_command('db',MigrateCommand)

if __name__ == "__main__":
    manager.run()


