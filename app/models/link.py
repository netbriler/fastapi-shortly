from typing import Optional

from pydantic import HttpUrl
from sqlmodel import SQLModel, Field


class LinkBase(SQLModel):
    title: str | None = Field(default=None, index=True)
    alias: str = Field(index=True)
    original_url: HttpUrl = Field(index=True)


class Link(LinkBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class LinkCreate(LinkBase):
    pass


class LinkRead(LinkBase):
    id: int


class LinkUpdate(LinkBase):
    pass
