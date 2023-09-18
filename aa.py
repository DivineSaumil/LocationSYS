import winrt.windows.devices.geolocation as wdg, asyncio

async def getCoords():
        locator = wdg.Geolocator()
        pos = await locator.get_geoposition_async()
        return [pos.coordinate.latitude, pos.coordinate.longitude]
    
def getLoc():
    return ascyncio.run(getCoords())
print(getLoc()[0])