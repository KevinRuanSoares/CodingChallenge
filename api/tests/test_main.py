import os
import sys

import pytest
from httpx import ASGITransport, AsyncClient

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src/")))
from main import app  # noqa: E402


@pytest.mark.asyncio
async def test_health_check():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.get("/api/health_check")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


@pytest.mark.asyncio
async def test_count_words():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.post("/api/count_words", json={"text": "Hello world"})
    assert response.status_code == 200
    assert response.json() == {"word_count": 2}


@pytest.mark.asyncio
async def test_count_words_empty_text():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.post("/api/count_words", json={"text": ""})
    assert response.status_code == 400
    assert response.json() == {"detail": "Text must not be empty"}


@pytest.mark.asyncio
async def test_count_words_with_special_characters():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.post("/api/count_words", json={"text": "Hello, world!"})
    assert response.status_code == 200
    assert response.json() == {"word_count": 2}


@pytest.mark.asyncio
async def test_count_words_with_multiple_spaces():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.post("/api/count_words", json={"text": "Hello     world"})
    assert response.status_code == 200
    assert response.json() == {"word_count": 2}
