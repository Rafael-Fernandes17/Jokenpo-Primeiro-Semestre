# 🎮 Jokenpô Terminal Edition
  Um simulador clássico de Pedra, Papel e Tesoura desenvolvido como projeto prático durante o primeiro semestre na PUCPR. O foco principal foi a aplicação de lógica de programação em Python, explorando a criação de uma interface interativa via terminal através de sequências de escape ANSI para uma experiência de usuário (UX) mais visual e intuitiva.

## ✨ Funcionalidades
O jogo oferece quatro opções principais no menu inicial:

<font color= "#00BFFF">Player vs Player (Local):</font> Implementado como prova de conceito para lógica de confronto. Por ser um projeto de primeiro semestre focado em lógica de terminal, este modo é ilustrativo, uma vez que o ambiente de entrada de dados (input) não permite a ocultação das jogadas entre dois usuários no mesmo teclado.

<font color= "#00BFFF">Player vs Computador:</font> Teste sua sorte contra a máquina (escolhas aleatórias).

<font color= "#00BFFF">Computador vs Computador:</font> Assista a uma simulação de batalha entre duas IAs.

<font color= "#00BFFF">Sistema de Placar: </font> Contagem dinâmica de vitórias durante a sessão.

<font color= "#00BFFF">Interface Colorida: </font> Uso de sequências de escape ANSI para uma experiência visual aprimorada no terminal.

## 🛠️ Tecnologias Utilizadas
Python 3: Linguagem base do projeto.

Biblioteca random: Utilizada para gerar as jogadas automáticas do computador.

ANSI Escape Codes: Uso de Sequências de Escape ANSI para feedback visual imediato (Vitória/Derrota/Empate).

## 🚀 Como Executar
Certifique-se de ter o Python instalado em sua máquina.

Clone este repositório: git clone https://github.com/Rafael-Fernandes17/Jokenpo-Primeiro-Semestre.git

Navegue até a pasta do projeto e execute: 
python3     jokenpo.py

## 📝 Lógica de Validação
O projeto implementa uma lógica de repetição (while True) que garante que o jogo continue até que o usuário decida sair, além de tratar entradas inválidas para evitar erros de execução.

### 👥 Desenvolvedores
Este projeto foi desenvolvido como parte de um estudo acadêmico por: Felipe Bresciani, Pedro Henrique Junqueira e Rafael Eliezer.