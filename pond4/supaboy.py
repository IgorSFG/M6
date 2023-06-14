# Importação das Bibliotecas
import os
import time
from supabase import create_client, Client

# Credenciais do Supabase
url: str = "https://mysjtevckxeidxonlxuq.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im15c2p0ZXZja3hlaWR4b25seHVxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4NjU5ODYyMiwiZXhwIjoyMDAyMTc0NjIyfQ.SuaR2tl0Xu4FqWUwiVgy62DkT0V54vaSnR9YxgHL0Ls"

# Nome do Bucket onde os arquivos serão armazenados
bucket: str = "Media"
# Lista os arquivos do diretório
media = os.listdir("./media")
# Cria o cliente do Supabase
supabase: Client = create_client(url, key)

# Envia os arquivos do diretório em forma binária para o bucket, com o tempo em que foi realizada a operação
for file in media:
    with open(os.path.join("./media", file), 'rb+') as f:
        data = f.read()
        res = supabase.storage.from_(bucket).upload(f"{time.time()}_{file}", data)
        print(res)
