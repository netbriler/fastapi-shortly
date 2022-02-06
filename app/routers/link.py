from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.models import LinkRead, LinkCreate, LinkUpdate
from app.services.link import create_link, get_links, get_link, delete_link, update_link

router = APIRouter(tags=['Link'])


@router.post('/links/', response_model=LinkRead, status_code=status.HTTP_201_CREATED)
async def _add_link(link: LinkCreate, session: AsyncSession = Depends(get_session)):
    return await create_link(session, link)


@router.get('/links/', response_model=list[LinkRead], status_code=status.HTTP_206_PARTIAL_CONTENT)
async def _get_links(offset: int = Query(default=0, ge=0), limit: int = Query(default=100, ge=0),
                     session: AsyncSession = Depends(get_session)):
    return await get_links(session, offset, limit)


@router.get('/link/{id}', response_model=LinkRead, status_code=status.HTTP_206_PARTIAL_CONTENT)
async def _get_link(id: int, session: AsyncSession = Depends(get_session)):
    return await get_link(session, id)


@router.patch('/link/{id}', response_model=LinkRead)
async def _update_link(id: int, link: LinkUpdate, session: AsyncSession = Depends(get_session)):
    if not await get_link(session, id):
        raise HTTPException(status_code=404, detail='Link not found')

    return await update_link(session, id, link)


@router.delete('/link/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def _delete_link(id: int, session: AsyncSession = Depends(get_session)):
    link = await get_link(session, id)
    if not link:
        raise HTTPException(status_code=404, detail='Link not found')

    await delete_link(session, id)
