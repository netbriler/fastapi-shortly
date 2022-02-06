from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Link, LinkCreate, LinkUpdate


async def get_link(session: AsyncSession, id: int) -> Link:
    result = await session.execute(select(Link).where(Link.id == id).limit(1))
    link = result.scalar_one_or_none()
    return link


async def get_link_by_alias(session: AsyncSession, alias: str) -> Link:
    result = await session.execute(select(Link).where(Link.alias == alias).limit(1))
    link = result.scalar_one_or_none()
    return link


async def get_links(session: AsyncSession, offset: int = 0, limit: int = 100) -> list[Link]:
    result = await session.execute(select(Link).offset(offset).limit(limit))
    links = result.scalars().all()
    return links


async def create_link(session: AsyncSession, link: LinkCreate) -> Link:
    link = Link(title=link.title, alias=link.alias, original_url=link.original_url)
    session.add(link)
    await session.commit()
    await session.refresh(link)
    return link


async def update_link(session: AsyncSession, id: int, link: LinkUpdate) -> Link:
    db_link = await get_link(session, id)
    link_data = link.dict(exclude_unset=True)
    for key, value in link_data.items():
        setattr(db_link, key, value)

    await session.commit()
    await session.refresh(db_link)

    return db_link


async def delete_link(session: AsyncSession, id: int) -> bool:
    result = await session.execute(delete(Link).where(Link.id == id))
    await session.commit()
    return bool(result)
