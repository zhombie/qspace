from typing import Optional, List

import ujson
from asyncpg import create_pool, Pool, Record

from server.core.logging import loggable

_database_instance = None


class Database(object):
    pool: Optional[Pool] = None

    @classmethod
    def instance(cls):
        global _database_instance
        if not _database_instance:
            _database_instance = cls()
        return _database_instance

    def __init__(self):
        self.pool = None

    async def connect(self, params):
        async def _init_database(connection):
            await connection.execute('SET TIME ZONE UTC')

            await connection.set_type_codec(
                'jsonb',
                encoder=ujson.dumps,
                decoder=ujson.loads,
                schema='pg_catalog'
            )

            await connection.set_type_codec(
                'json',
                encoder=ujson.dumps,
                decoder=ujson.loads,
                schema='pg_catalog'
            )

        try:
            self.pool = await create_pool(
                database=params['database'],
                host=params['host'],
                port=params['port'],
                user=params['user'],
                password=params['password'],
                init=_init_database,
                max_size=max(params.get('max_connections', 0), 5),
                min_size=3,
                max_inactive_connection_lifetime=0,
                command_timeout=60
            )
        except ConnectionRefusedError:
            raise RuntimeError(f'{self.__name__}: connection refused to database')

    @loggable
    async def execute(self, *args, **kwargs):
        async with self.pool.acquire() as connection:
            return await connection.execute(*args, **kwargs)

    @loggable
    async def fetch(self, *args, **kwargs) -> List[Record]:
        async with self.pool.acquire() as connection:
            return await connection.fetch(*args, **kwargs)

    @loggable
    async def fetchrow(self, *args, **kwargs) -> Record:
        async with self.pool.acquire() as connection:
            return await connection.fetchrow(*args, **kwargs)

    @loggable
    async def fetchval(self, *args, **kwargs):
        async with self.pool.acquire() as connection:
            return await connection.fetchval(*args, **kwargs)

    async def close(self):
        if self.pool:
            if hasattr(self.pool, 'terminate'):
                self.pool.terminate()
            self.pool = None
