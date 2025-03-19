from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import json
import os
import httpx
import asyncio


load_dotenv()
mcp = FastMCP()

USER_AGENT = "docs-app/1.0"
SERPER_URL = "https://google.serper.dev/search"
docs_urls = {
    "langchain": "python.langchain.com/docs",
    "llama-index": "docs.llamaindex.ai/en/stable",
    "openai": "platform.openai.com/docs",
}

async def search_web(query: str) -> dict | None:
    """search with serper api"""
    payload = json.dumps({"q": query, "num": 2})
    headers = {
        "X-API-KEY": os.getenv("SERPER_API_KEY"),
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.request(
                "POST",
                SERPER_URL,
                headers=headers,
                data=payload,
            )
            if response.status_code == 200:
                return response.json()
            else:
                return {"organic": []}
        except httpx.TimeoutException:
            return {"organic": []}


def fetch_url():
    """scrape url & get content"""

@mcp.tool()
def get_docs():
    """mcp tool"""


async def main():
    result = await search_web("women images")
    print("result: ", result)


if __name__ == "__main__":
    asyncio.run(main())
