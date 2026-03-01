# Antennas 📡

### Geovisualização Interativa para Dados do Sistema MOSAICO da ANATEL

Uma aplicação construída em Django para visualizar os dados de antenas do [sistema MOSAICO da ANATEL](https://sistemas.anatel.gov.br/se/public/view/b/licenciamento.php) em um mapa interativo.

## 🚀 Funcionalidades

- **Upload de CSV**: Faça o upload de forma fácil das exportações de dados de antenas (em formato CSV) do sistema MOSAICO.
- **Processamento de Dados**: Limpeza e validação automáticas dos dados utilizando a biblioteca Pandas.
- **Mapa Interativo**: Visualize a localização exata das antenas através de marcadores no mapa.
- **Filtros Personalizados**: Filtre as antenas exibidas por **Tecnologia** e **Entidade**.
- **Agrupamento (Clustering)**: Agrupa antenas com as mesmas coordenadas, melhorando a clareza e a legibilidade do mapa.

## ⚙️ Instalação e Configuração

### Pré-requisitos

Certifique-se de ter os seguintes requisitos instalados:
- Python 3.8+
- Django
- Pandas

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/luissaster/antennas.git
   cd antennas
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Aplique as migrações do banco de dados:**
   ```bash
   python manage.py migrate
   ```

4. **Inicie o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

5. Acesse a aplicação em seu navegador através do endereço `http://127.0.0.1:8000/`.

## 📖 Como Usar

1. Acesse a página de **Upload** na aplicação.
2. Selecione um arquivo CSV contendo os dados das antenas exportados do painel MOSAICO.
3. Após o envio do arquivo, você será redirecionado automaticamente para a visualização do **Mapa**.
4. Utilize os filtros disponíveis na interface para refinar a visualização por tecnologia ou por entidade conforme sua necessidade.

## 🐳 Suporte ao Docker

Se preferir, você pode executar o projeto de forma rápida utilizando contêineres Docker:

```bash
docker-compose up --build
```
