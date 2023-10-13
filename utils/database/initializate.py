import os
from tortoise import Tortoise

async def setup_db():
    await Tortoise.init(
        db_url=os.getenv("DB_URL"),
        modules={'models': ['utils.database.models.users']},
        timezone='Europe/Moscow',
    )
    await Tortoise.generate_schemas()
