import pytest
from sqlalchemy import select, text
import model

@pytest.mark.asyncio
async def test_orderline_mapper_can_load_lines(session):
    await session.execute(
        text(
            "INSERT INTO order_lines (orderid, sku, qty) VALUES "
            '("order1", "RED-CHAIR", 12),'
            '("order1", "RED-TABLE", 13),'
            '("order2", "BLUE-LIPSTICK", 14)'
        )
    )
    expected = [
        model.OrderLine("order1", "RED-CHAIR", 12),
        model.OrderLine("order1", "RED-TABLE", 13),
        model.OrderLine("order2", "BLUE-LIPSTICK", 14),
    ]
    assert (await session.execute(select(model.OrderLine))).scalars().all() == expected


@pytest.mark.asyncio
async def test_orderline_mapper_can_save_lines(session):
    new_line = model.OrderLine("order1", "DECORATIVE-WIDGET", 12)
    session.add(new_line)
    await session.commit()

    rows = list(await session.execute(text('SELECT orderid, sku, qty FROM "order_lines"')))
    assert rows == [("order1", "DECORATIVE-WIDGET", 12)]
