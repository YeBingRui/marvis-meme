#!/usr/bin/env python3
"""把原始素材图片批量压缩为 WebP，存入 skill 的 assets/memes/ 目录。

当用户提供新一批表情包底图时使用。压缩后即可被 build.py 打包进单文件 HTML。

用法：
    python compress_memes.py <原始素材文件夹> [输出尺寸] [质量]
    默认输出尺寸 1100px、质量 88，输出到 assets/memes/
"""
import os, sys, glob
from PIL import Image

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(SKILL_DIR, "assets", "memes")
EXT = (".png", ".jpg", ".jpeg", ".webp", ".gif")


def main(src_dir, size=1100, quality=88):
    if not os.path.isdir(src_dir):
        raise SystemExit("错误：素材文件夹不存在 " + src_dir)
    os.makedirs(OUT_DIR, exist_ok=True)
    files = sorted(glob.glob(os.path.join(src_dir, "*.*")))
    files = [f for f in files if f.lower().endswith(EXT)]
    if not files:
        raise SystemExit("错误：文件夹里没有可识别的图片（png/jpg/webp）")

    for f in files:
        name = os.path.splitext(os.path.basename(f))[0]
        try:
            im = Image.open(f).convert("RGBA")
            if im.getchannel("A").getextrema() == (255, 255):
                im = im.convert("RGB")
            im = im.resize((size, size), Image.LANCZOS)
            im.save(os.path.join(OUT_DIR, name + ".webp"), format="WEBP", quality=quality, method=6)
            print("已压缩：", name)
        except Exception as e:
            print("跳过 {}：{}".format(name, e))
    print("完成。素材已存入 assets/memes/，接下来运行 build.py 生成网页。")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("用法：python compress_memes.py <原始素材文件夹> [尺寸] [质量]")
    src = sys.argv[1]
    size = int(sys.argv[2]) if len(sys.argv) > 2 else 1100
    quality = int(sys.argv[3]) if len(sys.argv) > 3 else 88
    main(src, size, quality)
