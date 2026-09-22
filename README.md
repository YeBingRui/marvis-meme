# Marvis 表情包二创工坊（Meme Studio）

针对 Marvis 产品的表情包 / 梗图二创工具。内置 21 张无字底图，支持单图 / 上下双图 / 四宫格结构、文字位置与字号调整、贴图叠加、一键导出 PNG。

## 快速使用（无需安装）

打开成品网页即可使用：

- **在线版**：<GitHub Pages 链接，推送后回填>
- **本地版**：双击本仓库根目录的 `index.html`（单文件、内含全部素材，无需服务器）

## 功能

- 图片结构：单图 / 上下双图（竖版正方形格子）/ 四宫格
- 文字：位置（靠上 / 居中 / 靠下）、字号滑块、颜色（白 / 黑 / 描边）
- 每格独立配图配文，选中底图后自动填充素材名作为文案
- 贴图：示例贴图 + 上传自定义贴图，支持拖拽移动 / 缩放 / 删除
- 底部 Marvis 水印（可开关，文字不可改）
- 导出 PNG（单图 / 四宫格 1200×1200、上下双图 600×1200）、复制、重置

## 安装为 WorkBuddy Skill

本仓库本身就是一个 WorkBuddy skill，安装方法：

1. 克隆或下载本仓库，放到 `~/.workbuddy/skills/marvis-meme/`
2. 重启 WorkBuddy，在对话中提到「表情包二创 / meme」即可触发

## 目录结构

- `SKILL.md`：skill 定义
- `index.html`：成品网页（由 `scripts/build.py` 生成）
- `assets/memes/*.webp`：21 张内置无字底图
- `assets/template.html`：网页模板（含 `__MEMES_DATA__` 占位符）
- `scripts/build.py`：合成单文件 HTML
- `scripts/compress_memes.py`：新素材压缩入库（依赖 Pillow）

## 加新素材

1. 把新底图放入一个临时目录，运行：
   ```
   python scripts/compress_memes.py <素材目录> [尺寸] [质量]
   ```
2. 重新生成网页：
   ```
   python scripts/build.py index.html
   ```

## 约定

- 素材文件名即文案（命名用有情绪感的词，如「不急」「难绷」）。
- 三种结构默认底图均为「不急」，可在 `assets/template.html` 的 `DEFAULT_MEME_NAME` 常量中修改。

## 许可证

- 代码（`SKILL.md`、`scripts/`、`assets/template.html`）采用 MIT 许可证，详见 `LICENSE`。
- `assets/memes/` 内的图片素材为 Marvis 产品形象，版权归 Marvis 所有，仅限在 Marvis 相关场景使用。
