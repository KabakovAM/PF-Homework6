import uvicorn
from fastapi import FastAPI, HTTPException
from base_model import *
from data_base import *
from typing import List


app = FastAPI()


@app.post('/users/', response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(**user.model_dump())
    last_record_id = await database.execute(query)
    return {**user.model_dump(), 'u_id': last_record_id}


@app.get('/users/', response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get('/users/{u_id}/', response_model=User)
async def read_user(u_id: int):
    query = users.select().where(users.c.u_id == u_id)
    record = await database.fetch_one(query)
    if record == None:
        raise HTTPException(
            status_code=404, detail="Пользователя с таким id не существует")
    return record


@app.put('/users/{u_id}/', response_model=User)
async def update_user(u_id: int, new_order: UserIn):
    query = users.select().where(users.c.u_id == u_id)
    record = await database.fetch_one(query)
    if record == None:
        raise HTTPException(
            status_code=404, detail="Пользователя с таким id не существует")
    query = users.update().where(users.c.u_id == u_id).values(**new_order.model_dump())
    await database.execute(query)
    return {**new_order.model_dump(), 'u_id': u_id}


@app.delete('/users/{u_id}/')
async def delete_user(u_id: int):
    query = users.select().where(users.c.u_id == u_id)
    record = await database.fetch_one(query)
    if record == None:
        raise HTTPException(
            status_code=404, detail="Пользователя с таким id не существует")
    query = users.delete().where(users.c.u_id == u_id)
    await database.execute(query)
    return {u_id: 'Пользователь удален'}


@app.post('/orders/', response_model=Order)
async def create_order(order: OrderIn):
    query = goods.select().where(users.c.u_id == order.u_id)
    record = await database.fetch_one(query)
    if record == None:
        raise HTTPException(
            status_code=404, detail="Пользователя с таким id не существует")
    query = orders.insert().values(**order.model_dump())
    last_record_id = await database.execute(query)
    return {**order.model_dump(), 'o_id': last_record_id}


@app.get('/orders/', response_model=List[Order])
async def read_orders():
    query = orders.select()
    return await database.fetch_all(query)


@app.get('/orders/{o_id}/', response_model=Order)
async def read_order(o_id: int):
    query = orders.select().where(orders.c.o_id == o_id)
    record = await database.fetch_one(query)
    if record == None:
        raise HTTPException(
            status_code=404, detail="Заказа с таким id не существует")
    return record


@app.put('/orders/{o_id}/', response_model=Order)
async def update_order(o_id: int, new_order: OrderIn):
    query = orders.select().where(orders.c.o_id == o_id)
    record = await database.fetch_one(query)
    if record == None:
        raise HTTPException(
            status_code=404, detail="Заказа с таким id не существует")
    query = orders.update().where(orders.c.o_id == o_id).values(**new_order.model_dump())
    await database.execute(query)
    return {**new_order.model_dump(), 'o_id': o_id}


@app.delete('/orders/{o_id}/')
async def delete_order(o_id: int):
    query = orders.select().where(orders.c.o_id == o_id)
    record = await database.fetch_one(query)
    if record == None:
        raise HTTPException(
            status_code=404, detail="Заказа с таким id не существует")
    query = orders.delete().where(orders.c.o_id == o_id)
    await database.execute(query)
    return {o_id: 'Заказ удален'}


@app.post('/goods/', response_model=Good)
async def create_good(good: GoodIn):
    query = goods.insert().values(**good.model_dump())
    last_record_id = await database.execute(query)
    return {**good.model_dump(), 'g_id': last_record_id}


@app.get('/goods/', response_model=List[Good])
async def read_goods():
    query = goods.select()
    return await database.fetch_all(query)


@app.get('/goods/{g_id}/', response_model=Good)
async def read_good(g_id: int):
    query = goods.select().where(goods.c.g_id == g_id)
    record = await database.fetch_one(query)
    if record == None:
        raise HTTPException(
            status_code=404, detail="Товара с таким id не существует")
    return record


@app.put('/goods/{g_id}/', response_model=Good)
async def update_good(g_id: int, new_good: GoodIn):
    query = goods.select().where(goods.c.g_id == g_id)
    record = await database.fetch_one(query)
    if record == None:
        raise HTTPException(
            status_code=404, detail="Товара с таким id не существует")
    query = goods.update().where(goods.c.g_id == g_id).values(**new_good.model_dump())
    await database.execute(query)
    return {**new_good.model_dump(), 'g_id': g_id}


@app.delete('/goods/{g_id}/')
async def delete_good(g_id: int):
    query = goods.select().where(goods.c.g_id == g_id)
    record = await database.fetch_one(query)
    if record == None:
        raise HTTPException(
            status_code=404, detail="Товара с таким id не существует")
    query = goods.delete().where(goods.c.g_id == g_id)
    await database.execute(query)
    return {g_id: 'Товар удален'}

if __name__ == '__main__':
    uvicorn.run('engine:app', host='localhost', port=8000, reload=True)
