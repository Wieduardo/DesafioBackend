Projeto deselvolvido usando django rest framewok.

Essa Aplicação trabalha com o upload de um arquivo CNAB.txt que ficara salvo em um diretório criado de forma automatica. O arquivo é então aberto, lido, e suas informações são salvas no banco de dados.

O arquivo deve ser enviado em POST de formato "Multipart form" com a chave de nome "cnab_doc" na URL "localhost:8000/api/cnab/".

A visualização das operações salvas podem ser acessadas usando o método get na URL "localhost:8000/api/cnab/"

A lista de operações referente a cada loja assim como o saldo em conta podem ser acessados por meio de método GET, bastando apenas passar o CPF na URL. Exemplo: "localhost:8000/api/cnab/cpf/9620676017/"