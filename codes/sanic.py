from sanic import Sanic, text
import aiofiles
import time

app = Sanic(__name__)

@app.get("/")
async def index(request):
    return text("Hello, world!")

@app.post("/post")
async def post(request):
    async with aiofiles.open("post.txt", "a") as f:

def main():
    app.run(host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()