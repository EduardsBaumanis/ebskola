"""Exercise the actual starter HTML and representative completed student tasks."""
from contextlib import contextmanager
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os
import threading

from playwright.sync_api import sync_playwright
from check_datorika9 import ROOT, COURSE, check


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def main():
    check()
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(ROOT)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{server.server_port}"
    errors = []
    try:
        with sync_playwright() as p:
            chrome = os.environ.get("DATORIKA_CHROME", "/usr/bin/google-chrome")
            options = {"executable_path": chrome} if Path(chrome).exists() else {}
            browser = p.chromium.launch(headless=True, args=["--no-sandbox"], **options)
            context = browser.new_context(viewport={"width": 1280, "height": 900})

            @contextmanager
            def example(n, changes=()):
                page = context.new_page()
                page.on("pageerror", lambda error: errors.append(f"{n}: {error}"))
                url = f"{base}/datorika9/sakuma-kodi/{n}.html"
                if changes:
                    source = (COURSE / "sakuma-kodi" / f"{n}.html").read_text()
                    for old, new in changes:
                        assert old in source, f"Student edit target missing in {n}: {old}"
                        source = source.replace(old, new)
                    page.route(url, lambda route: route.fulfill(status=200, content_type="text/html", body=source))
                page.goto(url)
                yield page
                page.close()

            # Every baseline must load without JavaScript failures or missing media.
            for path in sorted((COURSE / "sakuma-kodi").glob("[1-5][1-6].html")):
                with example(int(path.stem)) as page:
                    assert page.locator("h1").count() == 1
                    for image in page.locator("img").all():
                        assert image.evaluate("img => img.complete && img.naturalWidth > 0"), path
                    for audio in page.locator("audio").all():
                        audio.evaluate("a => a.load()")
                        page.wait_for_function("Array.from(document.querySelectorAll('audio')).every(a => a.readyState >= 1)")

            for n in (13,):
                with example(n) as page:
                    page.get_by_role("button", name="Sākt spēli", exact=True).click()
                    assert page.locator("#atbilde").inner_text() == "Spēle sākta!"
            for n in (15, 16):
                with example(n) as page:
                    page.get_by_role("button", name="Sākt spēli", exact=True).click()
                    assert page.locator("#laukums").is_visible()
                    assert not page.locator("#sakums").is_visible()
                    page.get_by_role("button", name="Atpakaļ", exact=True).click()
                    assert page.locator("#sakums").is_visible()
            for n in (25, 26):
                with example(n) as page:
                    for _ in range(3):
                        page.get_by_role("button", name="Savākt zvaigzni", exact=True).click()
                    assert page.locator("#punkti").inner_text() == "Punkti: 3"

            with example(31, [("let punkti = 0;", "let punkti = 20;"), ("// ŠEIT APRĒĶINS", "punkti = punkti + 7;\ndzivibas = dzivibas - 1;")]) as page:
                assert page.locator("#punkti").inner_text() == "Punkti: 27"
                assert page.locator("#dzivibas").inner_text() == "Dzīvības: 2"

            with example(32, [("const punkti = skaits * 5;", "const punkti = skaits * 10 + 5;")]) as page:
                page.locator("#vards").fill("Lote")
                for value, expected in (("0", "5"), ("3", "35")):
                    page.locator("#skaits").fill(value)
                    page.get_by_role("button").click()
                    assert page.locator("#atbilde").inner_text() == f"Lote: {expected} punkti"

            with example(33, [("if (punkti >= 10)", 'if (punkti < 0) { zina = "Punkti nevar būt negatīvi."; } else if (punkti >= 20)')]) as page:
                for value, expected in (("-1", "Punkti nevar būt negatīvi."), ("19", "Turpini spēli!"), ("20", "Uzvara!")):
                    page.locator("#skaits").fill(value)
                    page.get_by_role("button").click()
                    assert page.locator("#atbilde").inner_text() == expected

            with example(34, [('const manta = ["karte", "lukturis"];', 'const manta = ["karte", "lukturis", "virve"];'), ('<p id="soma">', '<p id="pirmais"></p>\n<p id="soma">'), ('function paradit() {', 'function paradit() { document.getElementById("pirmais").textContent = "Pirmais: " + manta[0];')]) as page:
                assert page.locator("#pirmais").inner_text() == "Pirmais: karte"
                assert page.locator("#skaits").inner_text() == "Priekšmetu skaits: 3"
                page.get_by_role("button").click(click_count=2)
                assert page.locator("#skaits").inner_text() == "Priekšmetu skaits: 5"

            with example(35, [('const vietas = ["Mežs", "Upe", "Pils"];', 'const vietas = ["Mežs", "Upe", "Pils", "Tornis", "Ala"];')]) as page:
                assert page.locator("#pogas button").count() == 5
                for index in range(3):
                    page.locator("#pogas button").nth(index).click()
                assert page.locator("#gajieni").inner_text() == "Gājieni: 3"
                page.get_by_role("button", name="Sākt no jauna", exact=True).click()
                assert page.locator("#gajieni").inner_text() == "Gājieni: 0"

            with example(36) as page:
                page.get_by_role("button", name="Pils", exact=True).click()
                assert "Uzvara" in page.locator("#atbilde").inner_text()
                page.get_by_role("button", name="Mežs", exact=True).click()
                assert page.locator("#gajieni").inner_text() == "Gājieni: 1"
                page.get_by_role("button", name="Sākt no jauna", exact=True).click()
                for _ in range(3):
                    page.get_by_role("button", name="Upe", exact=True).click()
                assert "Gājieni beigušies" in page.locator("#atbilde").inner_text()

            with example(41, [('<!-- ŠEIT OTRĀ POGA -->', '<button onclick="pieskaitit(5)">+5</button><button onclick="pieskaitit(-2)">-2</button>')]) as page:
                for name in ("+1 punkts", "+5", "-2"):
                    page.get_by_role("button", name=name, exact=True).click()
                assert page.locator("#punkti").inner_text() == "Punkti: 4"
                page.get_by_role("button", name="Sākt no jauna", exact=True).click()
                assert page.locator("#punkti").inner_text() == "Punkti: 0"

            with example(42, [("const solis = 10;", "const solis = 20;"), ("// ŠEIT KREISĀ BULTIŅA", 'if (notikums.key === "ArrowLeft") { notikums.preventDefault(); kustinat(-1); }')]) as page:
                page.keyboard.press("ArrowRight")
                assert page.locator("#vieta").inner_text() == "X: 40"
                page.keyboard.press("ArrowLeft")
                assert page.locator("#vieta").inner_text() == "X: 20"
                for _ in range(20):
                    page.keyboard.press("ArrowLeft")
                assert page.locator("#vieta").inner_text() == "X: 0"
                for _ in range(20):
                    page.locator("#paLabi").click()
                assert page.locator("#vieta").inner_text() == "X: 270"

            with example(43, [("let x = 20;", "let x = 40;"), ("let y = 160;", "let y = 100;"), ("<!-- ŠEIT VERTIKĀLĀS POGAS -->", '<button onclick="kustinat(0, -10)">↑</button><button onclick="kustinat(0, 10)">↓</button><button onclick="location.reload()">Sākuma vieta</button>')]) as page:
                page.get_by_role("button", name="→", exact=True).click()
                page.get_by_role("button", name="↑", exact=True).click()
                assert page.locator("#vieta").inner_text() == "X: 50, Y: 90"
                page.get_by_role("button", name="Sākuma vieta", exact=True).click()
                assert page.locator("#vieta").inner_text() == "X: 40, Y: 100"

            # Fake time verifies intervals deterministically without long real waits.
            with example(44) as page:
                page.clock.install(time=1700000000000)
                page.clock.pause_at(1700000000001)
                page.locator("#sakt").click()
                page.clock.run_for(300)
                assert page.evaluate("x") == 20
                for _ in range(4):
                    page.locator("#sakt").click()
                page.clock.run_for(300)
                assert page.evaluate("x") == 40, "Repeated start created extra timers"
                page.locator("#apturet").click()
                page.clock.run_for(300)
                assert page.evaluate("x") == 40

            for n in (45, 46, 51):
                with example(n) as page:
                    page.clock.install(time=1700000000000)
                    page.clock.pause_at(1700000000001)
                    page.locator("#sakt").click()
                    for _ in range(8):
                        page.keyboard.press("ArrowUp")
                    page.clock.run_for(3000)
                    assert page.evaluate("punkti") >= 1, f"Unreachable score in {n}"
                    assert page.evaluate("aktiva") is True
                    # Arrange a collision then verify the real movement/end handlers.
                    page.evaluate("x = pretiniekaX; y = 160; paradit(); parbaudit();")
                    assert page.evaluate("aktiva") is False
                    old_x = page.evaluate("x")
                    page.locator("#paLabi").click()
                    assert page.evaluate("x") == old_x
                    page.locator("#atjaunot").click()
                    assert page.evaluate("punkti") == 0

            for n in (52, 53, 54, 55, 56):
                with example(n) as page:
                    page.clock.install(time=1700000000000)
                    page.clock.pause_at(1700000000001)
                    assert page.locator("#sakumaEkrans").is_visible()
                    assert not page.locator("#spelesEkrans").is_visible()
                    page.locator("#sakt").click()
                    assert page.locator("#spelesEkrans").is_visible()
                    assert page.evaluate("spele.dzivibas") == 3
                    # A collision costs exactly one life and moves the player clear.
                    page.evaluate("spele.x = spele.pretiniekaX; spele.y = 160; paradit(); parbaudit();")
                    assert page.evaluate("spele.dzivibas") == 2
                    page.evaluate("parbaudit();")
                    assert page.evaluate("spele.dzivibas") == 2
                    if n >= 54:
                        page.evaluate("moneta.style.left = spele.x + 'px'; moneta.style.top = spele.y + 'px'; parbaudit();")
                        assert page.evaluate("spele.punkti === bonusaPunkti")
                        assert page.locator("#moneta").evaluate("el => el.offsetLeft >= 0 && el.offsetLeft <= el.parentElement.clientWidth - 30 && el.offsetTop >= 0 && el.offsetTop <= el.parentElement.clientHeight - 30")
                    page.locator("#beigt").click()
                    old = page.evaluate("JSON.stringify(spele)")
                    page.keyboard.press("ArrowRight")
                    page.clock.run_for(300)
                    assert page.evaluate("JSON.stringify(spele)") == old
                    assert page.locator("#beiguEkrans").is_visible()
                    page.locator("#velreiz").click()
                    assert page.evaluate("spele.punkti") == 0
                    assert page.evaluate("spele.dzivibas") == 3
                    # Both actual end conditions must reach the visible end screen.
                    page.evaluate("spele.punkti = uzvarasPunkti; parbaudit();")
                    assert page.locator("#beiguZina").inner_text() == "Uzvara!"
                    page.locator("#velreiz").click()
                    page.evaluate("spele.dzivibas = 1; spele.x = spele.pretiniekaX; spele.y = 160; paradit(); parbaudit();")
                    assert page.locator("#beiguZina").inner_text() == "Dzīvības beigušās!"

            # Course UI: keyboard, persisted progress, full-code copying and narrow view.
            page = context.new_page()
            page.on("pageerror", lambda error: errors.append(f"course UI: {error}"))
            for path in sorted(COURSE.glob("*.html")):
                page.goto(f"{base}/datorika9/{path.name}")
                assert page.locator("h1").count() == 1
                page.set_viewport_size({"width": 375, "height": 850})
                assert page.evaluate("document.documentElement.scrollWidth <= innerWidth"), f"Mobile overflow: {path}"
            page.goto(f"{base}/datorika9/dat9_31.html")
            page.locator(".step-check").first.check()
            page.reload()
            assert page.locator(".step-check").first.is_checked()
            page.get_by_role("button", name="Noņemt soļu atzīmes").click()
            assert not page.locator(".step-check").first.is_checked()
            context.grant_permissions(["clipboard-read", "clipboard-write"])
            page.get_by_role("button", name="Kopēt sākuma kodu").click()
            assert page.evaluate("navigator.clipboard.readText()") == (COURSE / "sakuma-kodi/31.html").read_text()
            page.evaluate("() => { navigator.clipboard.writeText = async () => { throw new Error('Clipboard blocked'); }; }")
            page.get_by_role("button", name="Kopēt sākuma kodu").click()
            assert page.locator(".starter-source").get_attribute("open") is not None
            assert page.evaluate("window.getSelection().toString()").rstrip("\n") == (COURSE / "sakuma-kodi/31.html").read_text().rstrip("\n")
            assert "Ctrl+C" in page.locator(".copy-status").inner_text()
            page.goto(f"{base}/datorika9/dat9_12.html")
            assert page.locator(".lesson-jumps").count() == 0
            assert page.locator(".logic-box.lesson-task").count() == 3
            assert page.locator("#teorija .html-tags").count() == 6
            page.locator(".html-tags").evaluate_all("items => items.forEach(item => item.open = true)")
            assert page.evaluate("document.documentElement.scrollWidth <= innerWidth"), "HTML reference overflows on mobile"
            page.screenshot(path="/tmp/ebskola-datorika9-12-mobile.png", full_page=True)
            page.set_viewport_size({"width": 1280, "height": 900})
            page.locator(".html-tags").evaluate_all("items => items.forEach(item => item.open = false)")
            page.locator("#uzdevums-1").screenshot(path="/tmp/ebskola-datorika9-task-box.png")
            page.close()
            assert not errors, "\n".join(errors)
            browser.close()
            print("PASS: all starter pages; student edit scenarios; controls, scoring, collisions, restarts, timers, media; course UI and mobile widths")
    finally:
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    main()
