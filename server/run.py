from app import app
from data.psql import Database


@app.before_server_start
async def before_server_start(_app, _loop):
    # from settings import Settings
    #
    # await Database.instance().connect(
    #     database=Settings.instance().psql.database,
    #     host=Settings.instance().psql.host,
    #     port=Settings.instance().psql.port,
    #     user=Settings.instance().psql.user,
    #     password=Settings.instance().psql.password,
    # )

    pass


@app.after_server_stop
async def after_server_stop(_app, _loop):
    await Database.instance().close()


if __name__ == '__main__':
    try:
        app.run('0.0.0.0', port=8095, access_log=True)
    except Exception as e:
        print(e)
