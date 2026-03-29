# Gerador de jogos - Mega Sena v2.0

| Status de build | versão python | plataformas |
| :--- | :--- | :--- |
| ![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/mateuscamp/Mega-sena/build.yml?branch=main&label=build&style=for-the-badge) | ![Python Version](https://img.shields.io/badge/python-3.14+-blue?style=for-the-badge&logo=python) | ![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey?style=for-the-badge) |

## Sobre o projeto
Este é um gerador de jogos interativo para a Mega Sena desenvolvido em **Python** como parte de estudos de lógica de programação e automação de compilação (CI/CD). O projeto foca em oferecer uma experiência de usuário rica no terminal e geração automática de executáveis para Windows.

## Funcionalidades
- [x] **Interface Rica:** Visualização colorida e organizada com painéis e tabelas usando a biblioteca `Rich`.
- [x] **Loop Principal Interativo:** O programa permite que o usuário gere múltiplos jogos sem a necessidade de reiniciá-lo.
- [x] **Tratamento de Exceções:** Proteção contra erros de entrada, avisando o usuário sobre valores inválidos (por exemplo, letras no lugar de números).
- [x] **Automação de Build:** Integração com **GitHub Actions** para compilar automaticamente o executável Windows (`.exe`) a cada atualização no código.

## Tecnologias Uuilizadas
- **Linguagem:** Python
- **Bibliotecas:** `Rich` (UI de Terminal), `Random` (Lógica de sorteio), `PyInstaller` (Build)
- **Infraestrutura:** GitHub Actions, Fedora Linux

## Como usar

### Para desenvolvedores (Python)
Para clonar e rodar o projeto localmente:
```bash
# Instalar dependências (Rich)
pip install rich

# Rodar o script
python megasena.py
