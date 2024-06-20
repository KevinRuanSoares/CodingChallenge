"""Word Counter API Router."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

word_counter_router = APIRouter(tags=["Word Counter"])


class TextDTO(BaseModel):
    """Data transfer object for the text input."""

    text: str


class WordCountDTO(BaseModel):
    """Data transfer object for the word count."""

    word_count: int


@word_counter_router.post(
    "/count_words",
    response_model=WordCountDTO,
    summary="Count the number of words in a given text.",
)
async def count_words(text_dto: TextDTO) -> WordCountDTO:
    """Count the number of words in a given text."""
    if not text_dto.text.strip():
        raise HTTPException(status_code=400, detail="Text must not be empty")

    word_count = len(text_dto.text.split())
    return WordCountDTO(word_count=word_count)
