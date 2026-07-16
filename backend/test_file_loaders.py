import asyncio
from app.utils.file_handler import word_loader, ppt_loader
import os

async def test_word_loader():
    """测试 word_loader"""
    print("=== 测试 word_loader ===")
    # 创建一个测试 docx 文件
    test_file = "test_word.docx"
    if os.path.exists(test_file):
        try:
            docs = await word_loader(test_file)
            print(f"成功加载 {len(docs)} 个文档")
            if docs:
                print(f"内容预览: {docs[0].page_content[:200]}")
        except Exception as e:
            print(f"word_loader 失败: {e}")
            import traceback
            traceback.print_exc()
    else:
        print(f"测试文件 {test_file} 不存在")

async def test_ppt_loader():
    """测试 ppt_loader"""
    print("\n=== 测试 ppt_loader ===")
    # 创建一个测试 pptx 文件
    test_file = "test_ppt.pptx"
    if os.path.exists(test_file):
        try:
            docs = await ppt_loader(test_file)
            print(f"成功加载 {len(docs)} 个文档")
            if docs:
                print(f"内容预览: {docs[0].page_content[:200]}")
        except Exception as e:
            print(f"ppt_loader 失败: {e}")
            import traceback
            traceback.print_exc()
    else:
        print(f"测试文件 {test_file} 不存在")

if __name__ == '__main__':
    asyncio.run(test_word_loader())
    asyncio.run(test_ppt_loader())