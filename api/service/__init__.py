import asyncio, aiohttp

class Service(object):
  def __init__(self):
    pass
  
  async def _test(self):
    print("Begain async test...")
    for i in range(10):
      await asyncio.sleep(1)
      print(f"No.{i+1} tick")
    print('test end...')
    
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session: #CS0035
      async with session.get(url="https://www.google.com") as resp:
        res = await resp.text()
        print(res)
    
    return 'Hi Five'
  
  #TODO, NOTE
  def aiotest(self):
    return asyncio.run(self._test())