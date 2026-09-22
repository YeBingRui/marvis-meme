#!/usr/bin/env python3
"""构建单文件表情包二创工具 HTML。

读取 assets/template.html 和 assets/memes/ 下的素材图片，
将素材转成 base64 数据注入模板，输出一个自包含的单文件 HTML。

用法：
    python build.py [输出路径]
    输出路径缺省时为当前工作目录下的 marvis-meme-studio.html
"""
import os, sys, glob, base64, json

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(SKILL_DIR, "assets", "template.html")
MEMES_DIR = os.path.join(SKILL_DIR, "assets", "memes")

MIME = {
    ".webp": "image/webp",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif": "image/gif",
}


def build(out_path):
    if not os.path.exists(TEMPLATE):
        raise SystemExit("错误：找不到 " + TEMPLATE)
    html = open(TEMPLATE, encoding="utf-8").read()

    files = []
    for ext in MIME:
        files += glob.glob(os.path.join(MEMES_DIR, "*" + ext))
        files += glob.glob(os.path.join(MEMES_DIR, "*" + ext.upper()))
    files = sorted(set(files))

    entries = []
    for f in files:
        name = os.path.splitext(os.path.basename(f))[0]
        raw = open(f, "rb").read()
        ext = os.path.splitext(f)[1].lower()
        data = "data:{};base64,".format(MIME.get(ext, "image/png")) + base64.b64encode(raw).decode()
        entries.append({"name": name, "data": data})

    js = "const MEMES_DATA = " + json.dumps(entries, ensure_ascii=False) + ";"
    if "__MEMES_DATA__" not in html:
        raise SystemExit("错误：template.html 缺少 __MEMES_DATA__ 占位符")
    html = html.replace("__MEMES_DATA__", js)

    out_dir = os.path.dirname(os.path.abspath(out_path))
    os.makedirs(out_dir, exist_ok=True)
    open(out_path, "w", encoding="utf-8").write(html)
    size_kb = os.path.getsize(out_path) / 1024
    print("OK：已生成 {}（内置 {} 张素材，{:.0f} KB）".format(out_path, len(entries), size_kb))


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.getcwd(), "marvis-meme-studio.html")
    build(out)
