from random import sample
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from time import sleep

console = Console()

def executar_gerador():
    geral = []
    
    console.print(Panel.fit('Gerador de jogos [green]MEGA SENA[/green]', border_style='magenta'))
    console.print()

    try:
        quant = int(console.input('[bold white]Quantos jogos deseja gerar agora? [/bold white]'))
    except ValueError:
        console.print("[bold red]Opção inválida! Digite apenas números inteiros.[/bold red]")
        return # Volta para o início do loop

    # Loop de geração dos jogos
    for c in range(0, quant):
        jogo = sorted(sample(range(1, 61), 6))
        geral.append(jogo)
        console.print(f'[yellow]Jogo {c + 1}:[/yellow] [green]{geral[c]}[/green]')
        sleep(0.5)

    console.print()
    console.print(Rule(style="bold cyan"))
    console.print(Rule(title="[bold gold1]🍀 BOA SORTE NO SORTEIO! 💰[/bold gold1]", style="bold green"))
    console.print(Rule(style="bold cyan"))

#Loop principal
while True:
    executar_gerador()
    
    print()
    decisao = console.input("[bold cyan]Deseja gerar mais jogos? (s/n): [/bold cyan]").strip().lower()
    
    if decisao != 's':
        console.print("\n[bold magenta]Obrigado por usar o Gerador! Até a próxima.[/bold magenta]")
        sleep(2)
        break
    
    console.clear()