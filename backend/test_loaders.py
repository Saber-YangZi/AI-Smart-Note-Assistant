import asyncio
import os
from app.utils.file_handler import word_loader, ppt_loader

async def test_loaders():
    # 测试 word_loader
    print("=== 测试 word_loader ===")
    try:
        docs = await word_loader("test.docx")
        print(f"成功加载 {len(docs)} 个文档")
        if docs:
            print(f"内容预览: {docs[0].page_content[:200]}")
    except Exception as e:
        print(f"word_loader 失败: {e}")
    
    # 测试 ppt_loader
    print("\n=== 测试 ppt_loader ===")
    try:
        docs = await ppt_loader("test.pptx")
        print(f"成功加载 {len(docs)} 个文档")
        if docs:
            print(f"内容预览: {docs[0].page_content[:200]}")
    except Exception as e:
        print(f"ppt_loader 失败: {e}")

if __name__ == '__main__':
    asyncio.run(test_loaders())