from tortoise import Tortoise, run_async, fields
from tortoise.models import Model
from datetime import date
import asyncio
from aiohttp import ClientSession

MAIN_URL = "https://jsonplaceholder.typicode.com"
URL_USERS = MAIN_URL + "/users/"
URL_POSTS = MAIN_URL + "/posts/"


class Users(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    email = fields.TextField()
    phone = fields.TextField()

    def __str__(self):
        return f'{self.__class__.__name__}({self.id}, {self.name})'

    # __repr__ = __str__


class Posts(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.Users', related_name='Posts', null=True)
    title = fields.TextField()
    body = fields.TextField()

    def __str__(self):
        return f'{self.__class__.__name__}({self.id}, {self.title})'


async def dbinit():

    await Tortoise.init(
        db_url="postgres://postgres:1@localhost/Demo_pg",
        modules={'models': ['__main__']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()


async def get_data(url) -> str:
    """
    :param num:
    :return:
    """
    async with ClientSession() as session:
        async with session.get(url) as response:
            result = await response.json()
    return result


async def get_save_users(num) -> str:
    resp_url = await get_data(URL_USERS + str(num))
    # print(resp_url)

    user = await Users.filter(name=resp_url['name']).first()
    # print(user)
    if not user:
        user = Users(
            name=resp_url['name'],
            email=resp_url['email'],
            phone=resp_url['phone']
        )
        await user.save()
        res = f"{user} inserted"
    else:
        res = f"{user} already exists"

    # users = await Users.filter(name__in=['Samuel', 'Ben']).all()
    # print(users)

    # user = Users(name='Samuel', birth_date=date(2001, 1, 23), is_staff=True)
    # await user.save()

    return res


async def get_save_posts(num) -> str:
    resp_url = await get_data(URL_POSTS + str(num))
    post = await Posts.filter(title=resp_url['title']).first()

    if not post:
        # Get user from db
        user = await Users.filter(id=resp_url['userId']).first()

        post = Posts(
            title=resp_url['title'],
            body=resp_url['body'],
            user=user
        )
        await post.save()
        res = f"{post} inserted"
    else:
        res = f"{post} already exists"

    # users = await Users.filter(name__in=['Samuel', 'Ben']).all()
    # print(users)

    # user = Users(name='Samuel', birth_date=date(2001, 1, 23), is_staff=True)
    # await user.save()
    print(res)
    return res


async def async_main():
    await dbinit()

    # Get and save users
    # for x in range(1,9):
    #     await get_save_users(x)

    done, pending = await asyncio.wait(
        [get_save_users(x) for x in range(1, 10)]
    )

    for t in done:
        res = t.result()
        print(res)

    # Get and save posts
    # await get_save_posts(1)

    done, pending = await asyncio.wait(
        [get_save_posts(x) for x in range(1, 20)]
    )

    for t in done:
        res = t.result()
        print(res)

    await Tortoise.close_connections()

if __name__ == "__main__":
    asyncio.run(async_main())
