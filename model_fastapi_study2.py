


"""                        数据库模型定义文件 model_fastapi_study                        """



from tortoise.models import Model
from tortoise.fields import CharField, DateField, BooleanField


class User(Model):
    id = CharField(pk=True, max_length=36)
    name = CharField(max_length=50)
    email = CharField(max_length=100, unique=True)
    is_active = BooleanField(default=True)
    created_at = DateField(auto_now_add=True)

    class Meta:
        table = "users"                 # 指定数据库表名
        ordering = ["-created_at"]      # 默认排序方式，按创建时间降序排列


    def __str__(self):
        return self.name   

