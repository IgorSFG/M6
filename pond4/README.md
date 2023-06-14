# Projeto SUPABOY
O Supaboy tem como objetivo mandar imagens para um banco de dados do supabase.

# Como o SUPABOY funciona?
- Primeiramente, tive que criar uma organização no supabase e um 'bucket' para armazenar o conteúdo a ser enviado.
- No código, foram necessárias as bibliotecas de 'os', para manipulação dos diretórios, de 'time', para obtenção da data atual, e do supabase, mais específicamente as funções de 'Client' e 'crate_client' para a comunicação com o database do supabase.
- Para a comunicação com o supabase foram necessárias usar algumas das minhas credenciais, como a url e a chave da organização que eu havia criado, dessa forma sendo possível instanciar um cliente. Também defini o nome do bucket para onde eu queria enviar meus dados.
- A mídia que será enviada deve estar armazenada no diretorio 'media'. Ela é listada com o método 'listdir()' da biblioteca os, e será percorrida passando por todos os arquivos em formato binário. Eles serão enviadas por padrão com a data do envio e o nome do arquivo de imagem.

# SUPABOY em Ação!
Para enviar imagens para o meu supabase, basta executar o arquivo python com:
```
python3 supaboy.py
```
O resultado serão as imagens armazenas no meu bucket no supase:
[RESULTADO](https://drive.google.com/file/d/1jPnchb5qHIdCEe81gQ6nrc8FkR9QWlF6/view?usp=sharing)