import asyncio
from melchior_1 import melchior
from balthasar_2 import balthasar
from casper_3 import casper


class magi_integrating_system:
    async def execute_melchior(self, text: str):
        self.melchior = melchior()
        return await self.melchior.execute(text)

    async def execute_balthasar(self, text: str):
        self.balthasar = balthasar()
        return await self.balthasar.execute(text)

    async def execute_casper(self, text: str):
        self.casper = casper()
        return await self.casper.execute(text)

    async def main(self):
        self.text = input('input:')

        results = await asyncio.gather(
            self.execute_melchior(self.text),
            self.execute_balthasar(self.text),
            self.execute_casper(self.text)
            )
        results = {'melchior': results[0], 'balthasar': results[1], 'casper': results[2]}

        print(results)
        return results


integrate = magi_integrating_system()
asyncio.run(integrate.main())
