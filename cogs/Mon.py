from util.BotComs import Coms
from util.BotComs import nextcord
import nextcord
from nextcord.ext import commands
import random
import pokebase

class Mon(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def mon(self, ctx):
        async with ctx.typing():
            mon = random.randint(1, 898)

            pk = pokebase.pokemon(mon)
            namesplit = pk.name.split("-")[0]
            namespace = pk.name.replace("-", " ")
            print(pk.name)

            embed = nextcord.Embed(title = "Guess that Mon!", colour = 0xff0000)
            embed.set_image(url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{}.png".format(mon))

            await ctx.send(embed = embed)

        i=0
        while i < 63:
            message = await self.client.wait_for("message")
            msg = message.content.lower()
            if (msg == pk.name or msg == namesplit or msg == namespace) and msg != "tapu" and msg != "mr" and msg != "mime":
                await Coms.generic_embed(ctx, title = f"Correct! {namespace.title()}", desc = f"{message.author.name} got it!")
                break
            elif msg == "d!idk":
                await Coms.generic_embed(ctx, title = f"It's ||{namespace.title()}!||")
                break
            elif msg == "d!hint":
                await Coms.generic_embed(ctx, title = f"It starts with the letter '{pk.name[0]}'")
            elif msg == "d!len":
                await Coms.generic_embed(ctx, title = f"It's name is {len(namesplit)} letters long")
            elif msg == "d!mon":
                break
            i+=1

def setup(client):
    client.add_cog(Mon(client))