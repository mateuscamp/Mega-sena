from random import sample
from rich import print
from rich.panel import Panel
from rich.rule import Rule
from rich.align import Align
from time import sleep

geral = []
print(Panel.fit('Gerador de jogos [green]MEGA SENNA[/green]', border_style = 'magenta'))
print()
quant = int(input('Quantos jogos gerar? '))

for c in range(0, quant):
    jogo = sorted(sample(range(1, 61), 6))
    geral.append(jogo)
    print(f'[yellow]Jogo {c + 1}:[/yellow] [green]{geral[c]}[/green]')
    print()
    sleep(1)

print()
print(Rule(style="bold cyan"))
print(Rule(title="[bold gold1]🍀 BOA SORTE NO SORTEIO! 💰[/bold gold1]", style="bold green"))
print(Rule(style="bold cyan"))
