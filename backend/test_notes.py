import asyncio
from app.db.db_config import AsyncSessionLocal
from app.services.note_service import note_service

async def test_notes():
    async with AsyncSessionLocal() as db:
        notes, total = await note_service.list_notes(db, 'test_user_id', 1, 20, None, None)
        print(f'笔记数量: {total}')
        if total > 0:
            print('笔记列表:')
            for note in notes:
                print(f"  - {note.title}")
        else:
            print('没有笔记')
        
        # 检查所有用户的笔记
        print('\n--- 检查所有用户 ---')
        from sqlalchemy import text
        result = await db.execute(text("SELECT user_id, COUNT(*) as cnt FROM notes GROUP BY user_id"))
        rows = result.fetchall()
        for row in rows:
            print(f"用户 {row.user_id}: {row.cnt} 篇笔记")

if __name__ == '__main__':
    asyncio.run(test_notes())
