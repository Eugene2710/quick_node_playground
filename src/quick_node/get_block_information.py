from typing import Any
from dotenv import load_dotenv
import requests
import json
import os

from src.quick_node.get_latest_block import get_latest_block_number
from src.utils.get_previous_block import decrement_block_number

load_dotenv()


def get_block_information(block_number: str) -> dict[str, Any]:
    url: str = os.getenv("QUICK_NODE_URL")
    payload: str = json.dumps(
        {
            "method": "eth_getBlockByNumber",
            "params": ["0xc5043f", False],
            "id": 1,
            "jsonrpc": "2.0",
        }
    )
    headers: dict[str, str] = {"Content-Type": "application/json"}

    response: requests.Response = requests.request(
        "POST", url, headers=headers, data=payload
    )
    response_dict: dict[str, Any] = response.json()
    return response_dict


if __name__ == "__main__":
    latest_block: str = get_latest_block_number()
    latest_block_information: dict[str, Any] = get_block_information(latest_block)
    print(f"latest_block_information for {latest_block}:")
    print(latest_block_information)
    previous_block: str = decrement_block_number(latest_block)
    print(f"previous_block: {previous_block}")
    previous_block_information: dict[str, Any] = get_block_information(previous_block)
    print(f"previous_block_information for {previous_block}:")
    print(previous_block_information)