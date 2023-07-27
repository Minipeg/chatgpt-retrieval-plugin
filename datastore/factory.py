from datastore.datastore import DataStore
from datastore.providers.postgres_datastore import PostgresDataStore


async def get_datastore() -> DataStore:
    return PostgresDataStore()
