from fastapi import Depends, HTTPException, FastAPI, status
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.routers import link
from app.services.link import get_link_by_alias

app = FastAPI(title='Shortly')

app.include_router(link.router)


@app.get('/{short_link}', response_description='Redirect', status_code=status.HTTP_307_TEMPORARY_REDIRECT)
async def _redirect(short_link: str, session: AsyncSession = Depends(get_session)):
    link = await get_link_by_alias(session, short_link)
    if link is None:
        raise HTTPException(404, 'Link does not exist.')

    return RedirectResponse(url=link.original_url)
