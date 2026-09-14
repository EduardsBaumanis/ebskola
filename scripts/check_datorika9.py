"""Check course links, lesson contracts, downloadable code and media archives."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "datorika9"


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.refs = []
        self.source = []
        self.in_source = False
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag in ("a", "link", "script", "img", "audio"):
            ref = attrs.get("href") or attrs.get("src")
            if ref:
                self.refs.append(ref)
        if tag == "code" and attrs.get("id") == "pilnais-kods":
            self.in_source = True

    def handle_endtag(self, tag):
        if tag == "code":
            self.in_source = False

    def handle_data(self, data):
        if self.in_source:
            self.source.append(data)


def check():
    lessons = sorted(COURSE.glob("dat9_[1-5][1-6].html"))
    assert len(lessons) == 30, "Expected 30 lessons"
    all_pages = sorted(COURSE.rglob("*.html"))
    for path in all_pages:
        source = path.read_text()
        page = Page(source)
        assert len(page.ids) == len(set(page.ids)), f"Duplicate id: {path}"
        assert '<html lang="lv">' in source, f"Language missing: {path}"
        for ref in page.refs:
            url = urlsplit(ref)
            if url.scheme or url.netloc:
                continue
            relative = unquote(url.path)
            target = (ROOT / relative.lstrip("/")) if relative.startswith("/") else path.parent / relative
            if not relative:
                target = path
            if not target.exists() and not target.suffix:
                target = target.with_suffix(".html")
            assert target.exists(), f"Missing local target: {path.name}: {ref}"
            if url.fragment and target.suffix == ".html":
                assert unquote(url.fragment) in Page(target.read_text()).ids, f"Missing anchor: {path.name}: {ref}"
        if path in lessons:
            n = path.stem.removeprefix("dat9_")
            assert all(f"uzdevums-{i}" in page.ids for i in (1, 2, 3)), path
            assert source.count('class="logic-box lesson-task"') == 3, path
            assert 'lesson-jumps' not in source, path
            assert 'class="submission"' in source, path
            assert 'class="assessment-checks"' in source, path
            assert ''.join(page.source) == (COURSE / "sakuma-kodi" / f"{n}.html").read_text(), f"Starter drift: {path}"
            assert not re.search(r"git\s+(?:add|commit|push|init|config)\b", source), f"Terminal instruction: {path}"
            assert not re.search(r"[Pp]ieraksti(?:</?[^>]+>|\s)+(?:vienu\s+)?secinājumu", source), path
    for n in (25, 26):
        with zipfile.ZipFile(COURSE / "sakuma-kodi" / f"{n}.zip") as archive:
            html_name = "25.html" if n == 25 else "index.html"
            starter = archive.read(html_name).decode()
            assert starter == (COURSE / "sakuma-kodi" / f"{n}.html").read_text()
            for ref in Page(starter).refs:
                if not urlsplit(ref).scheme:
                    assert ref in archive.namelist(), f"Missing ZIP resource: {n}: {ref}"
            assert not any(".git/" in name for name in archive.namelist())
    print(f"PASS: {len(lessons)} lessons, {len(all_pages)} HTML pages, local links, matching starter code and both ZIP bundles")


if __name__ == "__main__":
    check()
