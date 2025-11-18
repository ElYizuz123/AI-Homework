# scrape_fb_group_playwright.py
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import json
import time

FACEBOOK_EMAIL = "yisuscolombia123@gmail.com"  # usa cuenta secundaria
FACEBOOK_PASSWORD = "yisuscolombiano123"
GROUP_URL = "https://www.facebook.com/groups/2406893716312968"
OUTPUT = "posts_paro_tec.jsonl"

SCROLL_PAUSES = 3   # segundos entre scrolls
MAX_SCROLLS = 100   # cuántos scrolls hacer (ajusta)


def parse_posts_from_html(html):
    soup = BeautifulSoup(html, "lxml")
    posts = []

    # Los selectores cambian; esto es un punto de partida
    for article in soup.find_all("div", {"role": "article"}):
        # intenta extraer texto y timestamp
        text_el = article.find("div", string=True)
        text = text_el.get_text(" ", strip=True) if text_el else ""
        time_el = article.find("abbr")
        ts = time_el.get("data-utime") if time_el and time_el.get("data-utime") else None

        # intenta obtener post url o id
        link = article.find("a", href=True)
        post_url = link["href"] if link else None

        posts.append({
            "text": text,
            "timestamp": ts,
            "post_url": post_url
        })

    return posts


def main():
    seen = set()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Puedes usar headless=True, pero a veces Facebook detecta headless
        context = browser.new_context()
        page = context.new_page()

        # LOGIN
        page.goto("https://www.facebook.com/login", timeout=60000)
        page.fill('input[name="email"]', FACEBOOK_EMAIL)
        page.fill('input[name="pass"]', FACEBOOK_PASSWORD)
        page.click('button[name="login"]')
        time.sleep(5)  # Esperar a que cargue después del login

        # Ir al grupo
        page.goto(GROUP_URL, timeout=60000)
        time.sleep(5)  # Esperar a que cargue el grupo

        # Scroll y colecta HTML en cada paso
        for i in range(MAX_SCROLLS):
            time.sleep(2)  # Espera 2 segundos a que termine de cargar
            try:
                page.wait_for_selector('div[role="article"]', timeout=10000)
            except Exception:
                print(f"[scroll {i+1}] No se encontraron artículos, continuando...")
                continue

            html = page.content()
            posts = parse_posts_from_html(html)

            new = 0
            with open(OUTPUT, "a", encoding="utf-8") as f:
                for post in posts:
                    key = (post.get("post_url") or post.get("text")[:120])
                    if key in seen:
                        continue
                    seen.add(key)
                    f.write(json.dumps(post, ensure_ascii=False) + "\n")
                    new += 1

            print(f"[scroll {i+1}/{MAX_SCROLLS}] nuevos: {new}")

            # Scroll down
            page.evaluate("window.scrollBy(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSES)

        browser.close()

    print("✅ Terminado.")


if __name__ == "__main__":
    main()
