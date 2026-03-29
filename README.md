# Gerador de jogos - Mega Sena v2.0

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/mateuscamp/Mega-sena/build.yml?branch=main&style=for-the-badge)
![Python Version](https://img.shields.io/badge/python-3.14+-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey?style=for-the-badge)

## Sobre o projeto
Gerador de jogos para a Mega Sena desenvolvido em **Python**. O objetivo do projeto foi aplicar conceitos de lógica de programação, tratamento de erros e automação de build (CI/CD).
Conceitos básicos aprendidos no cuso de python e aplicados por mim neste projeto.

O software conta com uma interface de terminal estilizada em rich e gera arquivos executáveis de forma automática para usuários windows.

## Funcionalidades
- [x] **Interface rica:** Uso da biblioteca `Rich` para tabelas, painéis e cores no terminal.
- [x] **Loop de interatividade:** O usuário pode gerar múltiplos jogos sem reiniciar o programa.
- [x] **Tratamento de exceções:** Proteção contra entradas de dados inválidas (letras no lugar de números).
- [x] **Build automatizado:** Uso de **GitHub Actions** para compilar o `.exe` automaticamente a cada atualização.

## ecnologias Utilizadas
- **Linguagem:** Python
- **Bibliotecas:** `Rich` (UI), `Random` (Lógica), `PyInstaller` (Build)
- **Infraestrutura:** gitHub actions & fedora linux

## Modo de usar

### Para desenvolvedores (Python)
Clonar o repositório e rodar:
```bash
# Instalar dependências
pip install rich

# Rodar o script
python megasena.py
