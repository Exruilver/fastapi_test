from typing import Dict
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI


"""                        迁移配置文件 TORTOISE_ORM                        """

app = FastAPI()


#######################             SQLite 和 MYSql 的区别             #######################
# SQLite 是一个轻量级的嵌入式数据库，适合小型应用和开发环境，而 MySQL 是一个功能强大的关系型数据库管理系统，适合大型应用和生产环境。
# SQLite 不需要单独的服务器进程，数据存储在单个文件中，易于设置和使用；MySQL 需要安装和配置服务器，支持多用户并发访问和复杂查询。
#######################          SQLite 适用场景          #######################
# 1. 开发和测试环境：SQLite 易于设置和使用，适合快速开发和测试。
# 2. 小型应用：对于小型应用或嵌入式系统，SQLite 提供了足够的功能和性能。
# 3. 单用户应用：SQLite 适合单用户应用程序，因为它不支持多用户并发访问。



TORTOISE_ORM: Dict = {
    "connections": {
        # 开发环境使用 SQLite 数据库
        # "default": "sqlite://db.sqlite3",
        # 生产环境使用 MySQL 数据库
        "default": "mysql://root:123456@127.0.0.1:3306/fastapi_study_db",
        # 生产环境示例：PostgreSQL 数据库
        # "default": "postgres://user:password@host:port/database"
    },
    "apps": {
        # models 配置，指定数据库模型的位置
        "models": {     
            "models": ["model_fastapi_study", "aerich.models"],  
            # "models": ["aerich.models", "your_app.models"],  # 应该写这个
            # 第二个 models 用于指定你自己的数据库模型位置
            # 第一个 models 是必须的，用于 aerich 进行数据库迁移管理
            "default_connection": "default",
        }
    },
    # 连接池配置（可选）
    "use_connection_pool": True,
    "db_pool":{
        "min_size": 1,      # 最大连接数
        "max_size": 10,     # 最小连接数
        "idle_timeout": 30  # 连接空闲超时时间，单位为秒
    }
}


# 注册 Tortoise ORM 与 FastAPI 应用
register_tortoise(
    app,                    # 链接的 FastAPI 应用实例
    config=TORTOISE_ORM,    # ORM 配置字典
    generate_schemas=True,   # 自动生成数据库表结构
    add_exception_handlers=True  # 添加默认异常处理
    )


# 注意要在项目的根路径下面运行这些命令
# 以上配置完成后，可以使用 aerich 工具进行数据库迁移管理


# 1. 初始化 aerich 配置：aerich init -t 配置文件路径.TORTOISE_ORM  
#   这条命令会生成两个文件：pyproject.toml 和 migrations 目录
#   toml 文件用于 aerich 的配置，migrations 目录用于存放迁移文件（就是生成的 SQL 语句文件）    

# 2. 创建初始迁移：aerich init-db
#   这条命令会根据当前的模型生成初始的数据库表结构

# 3. 创建新的迁移：aerich migrate -n "migration_name"
#   这条命令会根据模型的变化生成新的迁移文件，比如说想要删除字段
#   例如：
#        aerich migrate -n "remove_date_of_birth_from_user"
#        同时注意在模型中也要删除对应的字段定义

# 4. 应用迁移到数据库：aerich upgrade
#   这条命令会将所有未应用的迁移文件执行到数据库中，更新数据库结构  

# 5. 回滚迁移（如果需要）：aerich downgrade