# Boox-Note-Converter

这是一个用于将文石（Boox）阅读器导出的笔记文件（`.txt` 格式）转换为结构化 Markdown 格式的工具。

## 功能

-   解析文石笔记 `.txt` 文件，提取书名、章节、笔记内容、批注、时间和页码。
-   将解析后的内容转换为易于阅读和管理的 Markdown 格式。
-   自动将转换后的 Markdown 文件保存到 `output` 子文件夹中。

## 使用说明

### 1. 前提条件

-   确保您的系统已安装 Python 3。

### 2. 文件结构

请将您的文石笔记 `.txt` 文件放置在 `Boox-Note-Converter` 文件夹内，或者 `sample_notes` 子文件夹中。

```
E:/Cursor-Projects/Boox-Note-Converter/
├───output/
├───sample_notes/
│   └───sample_note.txt
├───convert_notes.py
└───你的笔记文件.txt
```

`sample_notes/sample_note.txt` 是一个示例文件，展示了笔记的预期格式。

### 3. 运行转换脚本

打开命令行或终端，导航到 `E:/Cursor-Projects/` 目录，然后运行以下命令：

```bash
python Boox-Note-Converter/convert_notes.py
```

脚本将自动查找 `Boox-Note-Converter` 文件夹中所有的 `.txt` 文件（除了 `conversion_log.txt`），并将其转换为 Markdown 格式。

### 4. 查看转换结果

转换后的 Markdown 文件将保存在 `Boox-Note-Converter/output/` 文件夹中。每个 `.txt` 文件将对应生成一个同名的 `.md` 文件（例如，`我们为什么上瘾-annotation-2025-06-28_10_23_39.txt` 将转换为 `我们为什么上瘾.md`）。

### 5. 输入文件格式示例

脚本期望的 `.txt` 笔记文件格式如下：

```
读书笔记 | <<书名>>作者
章节标题（可选）
日期 时间 | 页码：XXX
笔记内容...
【批注】批注内容（可选）
-------------------
另一个笔记条目...
```

### 6. 输出文件格式示例

转换后的 Markdown 文件将遵循以下结构：

```markdown
# 书名

**章节标题**

**时间：** 日期 时间 | **页码：** XXX

> 笔记内容...

**批注：** 批注内容（如果存在）

**时间：** 日期 时间 | **页码：** YYY

> 另一个笔记内容...
```

## 注意事项

-   请确保您的 `.txt` 笔记文件是 UTF-8 编码，以避免中文乱码问题。
-   脚本会尝试根据 `<<书名>>` 提取书名作为 Markdown 文件的标题和文件名。如果未找到，将使用 `.txt` 文件名作为替代。
-   脚本会忽略名为 `conversion_log.txt` 的文件，因为它通常是调试日志文件。

希望这份说明能帮助您更好地使用这个工具！
