import asyncio
import logging
import random
import string
import json

import aiohttp
from colorama import Fore, init

# NOTE: YOU NEED TO GET YOUR OWN USERID FROM EPOMAKER. JUST GO TO THEIR WEBSITE AND LOG IN

# Initialize colorama
init(autoreset=True)

# Configure logging
logging.basicConfig(
    filename="unexpected_responses.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

async def generate_fake_email():
    """Generate a random fake email address."""
    domains = ["gmail.com"]
    name = "".join(random.choices(string.ascii_lowercase, k=10))
    domain = random.choice(domains)
    return f"{name}@{domain}"

async def fetch_coupon(session, url):
    """Fetch coupon data from the given URL."""
    async with session.get(url) as response:
        return await response.json(), response.status

async def main():
    url_template = "https://donumpro.com/api/frontend/huntGame/generateCoupon/epomaker?userId=**PUTURUSERIDHERE**&userEmail={}&eventName=epomaker_christmas&new_year_sales_2024"
    async with aiohttp.ClientSession() as session:
        while True:
            await asyncio.sleep(0.5)
            fake_email = await generate_fake_email()
            url = url_template.format(fake_email)
            try:
                response_json, status = await fetch_coupon(session, url)
                label = response_json["data"].get("label", "Unknown")
                if status != 400 and response_json["status"] != 400:
                    with open("successful_responses.jsonl", "a") as f:
                        json.dump(response_json, f)
                        f.write("\n")
                if label not in ["$3.00", "$5.00", "$8.00"]:
                    logging.info(
                        f"Unexpected response for email {fake_email}: {response_json}"
                    )
                    print(
                        Fore.RED
                        + f"Unexpected response for email {fake_email}: {response_json}"
                    )
                else:
                    print(
                        Fore.GREEN
                        + f"Successful response for email {fake_email}: {response_json}"
                    )
                if (
                    response_json["status"] == 400
                    and response_json["data"].get("message") == "Get counpon rule failed"
                ):
                    logging.info(
                        f"Rate limit hit with email {fake_email}, switching email."
                    )
                    print(
                        Fore.YELLOW
                        + f"Rate limit hit with email {fake_email}, switching email."
                    )
                    await asyncio.sleep(1)
                    continue
            except Exception as e:
                logging.error(f"Error fetching coupon for email {fake_email}: {e}")
                print(Fore.RED + f"Error fetching coupon for email {fake_email}: {e}")


if __name__ == "__main__":
    asyncio.run(main())
