import abc

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

import model


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    async def add(self, batch: model.Batch):
        raise NotImplementedError

    @abc.abstractmethod
    async def get(self, reference) -> model.Batch:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, batch):
        self.session.add(batch)

    async def get(self, reference):
        return (
            await self.session.execute(
                select(model.Batch)
                .options(selectinload(model.Batch._allocations))
                .filter_by(reference=reference)
            )
        ).scalar_one()

    async def list(self):
        return (
            (
                await self.session.execute(
                    select(model.Batch).options(selectinload(model.Batch.allocations))
                )
            )
            .scalars()
            .all()
        )
