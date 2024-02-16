import asyncio
from melchior import melchior
from balthasar import balthasar
from casper import casper

class magi_integrate_system():
    async def execute_melchior(text):
        await melchior.execute(text)
        return "Melchior task completed."

    async def execute_balthasar(text):
        await balthasar.execute(text)
        return "Balthasar task completed."

    async def execute_casper(text):
        await casper.execute(text)
        return "Casper task completed."

    async def main(self):
        text = input('input:')
        # 非同期で関数を実行
        results = await asyncio.gather(self.execute_melchior(text), self.execute_balthasar(text), self.execute_casper(text))
        # 結果をプリント
        print(results)


# メイン関数を実行
integrate = magi_integrate_system()
asyncio.run(integrate.main())
