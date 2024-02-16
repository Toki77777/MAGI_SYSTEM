import asyncio, eel
from melchior_1 import melchior
from balthasar_2 import balthasar
from casper_3 import casper


class magi_central_integrating_system:
    async def execute_melchior(self, text: str):
        self.melchior = melchior()
        return await self.melchior.execute(text)

    async def execute_balthasar(self, text: str):
        self.balthasar = balthasar()
        return await self.balthasar.execute(text)

    async def execute_casper(self, text: str):
        self.casper = casper()
        return await self.casper.execute(text)

    async def integrate(self, text: str):
        results = await asyncio.gather(self.execute_melchior(text), self.execute_balthasar(text), self.execute_casper(text))

        if results[0]!=results[1] and results[1]!=results[2] and results[2]!=results[0]:
            if (500 in results) and (-1 in results):
                results.append(-1)
        else:
            counts = {result: results.count(result) for result in results}
            majority =  max(counts, key=counts.get)
            results.append(majority)

        results = {'melchior': results[0], 'balthasar': results[1], 'casper': results[2], 'conclusion': results[3]}
        print(results)
        return results


eel.init('web')
eel.start('main.html', mode='chrome-app', port=8080)
