from opsdroid.matchers import match_regex

@match_regex(r'.*dance.*')
async def how_are_you(opsdroid, config, message):
    await message.respond('Good thanks! My load average is 0.2, 0.1, 0.1.')