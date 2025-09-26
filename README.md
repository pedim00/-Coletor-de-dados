# -Coletor-de-dados
esse programa pega alguns comentários de um site feito para scrap, por isso a escolha.

HAT (O que está sendo feito?)
O que: Extração de frases, autores e tags do site "Quotes to Scrape"

O que produz: Um arquivo CSV chamado "quotes.csv" com os dados extraídos

WHY (Por que está sendo feito?)
Por que: Para coletar dados de citações de forma automatizada

Objetivo: Criar um dataset estruturado para análise ou uso posterior

WHERE (Onde está sendo feito?)
Onde: Do site http://quotes.toscrape.com

Onde salva: No diretório local do script como "quotes.csv"

WHEN (Quando é feito?)
Quando: No momento da execução do script (tempo real)

Frequência: Execução única (não é agendada)

WHO (Quem/por quem é feito?)
Quem executa: O script Python

Quem fornece os dados: O site Quotes to Scrape

Quem usa: Desenvolvedor/analista que executa o código

HOW (Como é feito?)
Como: Através de web scraping usando:

requests para fazer HTTP requests

BeautifulSoup para parsing do HTML

pandas para estruturação dos dados em DataFrame

Seletores CSS para localizar elementos específicos
