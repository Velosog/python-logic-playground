# 🐍 Python Logic Playground

Repositório de exercícios práticos em Python, focado em lógica de programação, manipulação de dados, arquivos e criação de CLIs interativos. Cada módulo é autossuficiente e pode ser executado diretamente pelo terminal.

---

## 📁 Estrutura do Projeto

```
python-logic-playground/
├── src/
│   ├── funcoes/
│   │   ├── ex01_normalizador.py     # Normalizador de texto
│   │   └── ex02_dinheiro_br.py      # Parser de valores monetários BR
│   ├── fundamentos/
│   │   └── listas_dicts.py          # Operações com listas e dicionários
│   ├── arquivos/
│   │   ├── analisador_txt.py        # Análise estatística de arquivos .txt
│   │   ├── db_json.py               # Mini banco de dados em JSON
│   │   ├── resumo_csv_finance.py    # Resumo financeiro a partir de CSV
│   │   └── data/
│   │       ├── db.json              # Banco de dados persistente
│   │       ├── exemplo.csv          # CSV de exemplo para transações
│   │       └── exemplo.txt          # Texto de exemplo para análise
│   └── controle/
│       ├── cli.py                   # CLI principal (normalizador + dinheiro)
│       └── cli_finance.py           # CLI financeiro completo
├── tests/
│   ├── test_normalizador.py
│   └── test_dinheiro_br.py
├── requirements.txt
└── pytest.ini
```

---

## 🚀 Como rodar

### Pré-requisitos

- Python 3.10+
- pip

### Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/python-logic-playground.git
cd python-logic-playground

# Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
.venv\Scripts\activate           # Windows

# Instale as dependências
pip install -r requirements.txt
```

---

## 🧩 Módulos

### `src/funcoes/ex01_normalizador.py` — Normalizador de Texto

Função que limpa e padroniza strings para uso em sistemas reais.

**Comportamento:**
- Remove espaços extras das bordas e compacta internamente
- Converte para minúsculo (opcional)
- Remove pontuação e símbolos (opcional)

```python
from src.funcoes.ex01_normalizador import normalizar_texto

normalizar_texto("  Oi, Gabi!!!   ")          # → "oi gabi"
normalizar_texto("Oi, Gabi!", lower=False)    # → "Oi Gabi"
normalizar_texto("Python   é   FORTE.")       # → "python é forte"
```

**Rodar diretamente:**
```bash
python src/funcoes/ex01_normalizador.py
```

---

### `src/funcoes/ex02_dinheiro_br.py` — Parser de Dinheiro BR

Converte strings no formato monetário brasileiro para inteiro em centavos.

**Formatos aceitos:**
- `"R$ 1.234,56"` → `123456`
- `"1234,56"` → `123456`
- `"1.234"` → `123400`
- `"10"` → `1000`
- `"0,99"` → `99`
- `",50"` → `50`

```python
from src.funcoes.ex02_dinheiro_br import parse_dinheiro_br

parse_dinheiro_br("R$ 1.234,56")  # → 123456
parse_dinheiro_br("0,99")         # → 99
```

**Rodar diretamente:**
```bash
python src/funcoes/ex02_dinheiro_br.py
```

---

### `src/fundamentos/listas_dicts.py` — Listas e Dicionários

Exercícios com estruturas de dados fundamentais do Python.

| Função | Descrição |
|---|---|
| `contar_pares(lista)` | Conta quantos números pares há na lista |
| `tamanho_dos_nomes(lista)` | Retorna `{nome: len(nome)}` para cada item |
| `frequencia_palavras(texto)` | Conta a frequência de cada palavra no texto |

```bash
python src/fundamentos/listas_dicts.py
```

---

### `src/arquivos/analisador_txt.py` — Analisador de TXT

Lê um arquivo `.txt` e exibe estatísticas completas.

**Saída:**
- Número de linhas, palavras e caracteres
- Frequência de cada palavra (ordenada por ocorrência)

```bash
python -m src.arquivos.analisador_txt
```

---

### `src/arquivos/resumo_csv_finance.py` — Resumo Financeiro (CSV)

Processa um CSV com colunas `data, categoria, descricao, valor` e gera um resumo por categoria.

**Exemplo de CSV:**
```
data,categoria,descricao,valor
2024-01-10,alimentacao,supermercado,"R$ 350,00"
2024-01-12,transporte,uber,"25,50"
```

**Saída:**
```
=== RESUMO FINANCEIRO (CSV) ===
Total geral: R$ 375,50

--- Por categoria (maior -> menor) ---
alimentacao: R$ 350,00
transporte: R$ 25,50
```

```bash
python -m src.arquivos.resumo_csv_finance
```

---

### `src/arquivos/db_json.py` — Mini Banco de Dados JSON

Banco de dados simples e persistente em arquivo `.json`. Cada registro é salvo com `id`, `data`, `categoria`, `descricao` e `valor_centavos`.

**Operações disponíveis:**
- Adicionar registro (com normalização automática do texto e parse do valor)
- Listar todos os registros
- Remover por ID (UUID)

```bash
python -m src.arquivos.db_json
```

---

### `src/controle/cli.py` — CLI Principal

Interface interativa no terminal com as funcionalidades de normalização de texto e conversão de valores monetários.

```bash
python src/controle/cli.py
```

```
=== PYTHON LOGIC PLAYGROUND ===
1 - Converter dinheiro BR para centavos
2 - Normalizar texto
3 - Sair
```

---

### `src/controle/cli_finance.py` — CLI Financeiro

CLI completa para gerenciamento de gastos pessoais. Integra o banco JSON, o parser de dinheiro e o normalizador.

```bash
python -m src.controle.cli_finance
```

```
=== FINANCE CLI ===
1 - Adicionar gasto
2 - Listar gastos
3 - Resumo por categoria
4 - Remover por ID
5 - Sair
```

---

## 🧪 Testes

Os testes cobrem as duas funções principais com casos de uso válidos, inválidos e de tipo.

```bash
# Rodar todos os testes
pytest

# Com output detalhado
pytest -v
```

**Cobertura dos testes:**

| Arquivo | O que testa |
|---|---|
| `test_normalizador.py` | Normalização básica, flags opcionais, tipo inválido |
| `test_dinheiro_br.py` | 9 formatos válidos, 9 entradas inválidas, tipo inválido |

---

## 🛠️ Dependências

| Pacote | Versão | Uso |
|---|---|---|
| `pytest` | 9.0.2 | Framework de testes |
| `rich` | 14.3.3 | Formatação de saída no terminal |
| `pygments` | 2.19.2 | Syntax highlighting |
| `colorama` | 0.4.6 | Cores no terminal (Windows) |

---

## 📐 Convenções

- Todo módulo possui docstring explicando o objetivo e como executá-lo
- Funções usam type hints e validação de tipos com `TypeError`/`ValueError`
- O projeto deve ser executado a partir da raiz para que os imports relativos funcionem corretamente

---

## 📄 Licença

MIT