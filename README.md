# Flappy_bird em Python com Pygame
Clone do Clássico Flappy Bird, desenvolvido como primeiro projeto pessoal com foco em estruturação de código, Pygame, e versionamento com Git. Todo código foi modularizado e adaptado a partir de um tutorial guiado, com melhorias e organização feitas por mim.
feito em Python com Pygame.

## Tecnologias usadas
- **Python 3.13+**
- **Pygame** - biblioteca para criação de jogos 2D
- **Git** - Controle de versão
- **GitHub** - hospedagem e documentação

## Estrutura do projeto
'''bash
   flappy_bird_pygame/
   ├── src/
   │   ├── _bird.py           # Classe Bird (controle do personagem)
   │   ├── _floor.py          # Classe Floor (chão do jogo)
   │   ├── _pipe.py           # Classe Pipe (canos)
   │   └── Flappy_bird_0.1.py # Código principal do jogo
   │
   ├── assets/
   │   ├── images/            # Sprites: pássaro, fundo, canos, chão
   │   └── sounds/            # Sons do jogo (a inserir)
   │
   ├── README.md              # Documentação do projeto
   └── requirements.txt       # Dependências do projeto
'''

## Instalação
1. Clone o repositório:
   '''bash
      git clone https://github.com/seu-usuario/flappy-bird-pygame.git
   '''
   
2. Acesse a pasta:
   '''bash
      cd flappy-bird-pygame
   '''

3. Crie e ative um ambiente virtual (opcional, mas recomendado):
   '''bash
      python -m venv venv
      source venv/bin/activate  # no Linux/macOS
      venv\Scripts\activate     # no Windows
   '''
4. Instale as dependências:
   '''bash
      pip install -r requirements.txt
   '''




## Como jogar
- Execute o script principal:
   '''bash
      python src/Flappy_bird.py
   '''
- Precione **ESPAÇO** para fazer o pássaro voar.
- Evite colidir com os canos e o chão.
- A pontuação aparece no canto superior direito.

## Testes
- Teste manuais. 

## Aprendizados e Objetivos
- Manipulação gráfica e física com Pygame.
- Organização de pastas (assets e src).
- Estrutura modular com múltiplos arquivos.
- Controle de versão com Git.
- Documentação para repositórios públicos.

## Melhorias futuras
- Implementar do telas (inicial, fim de jogo, Ranking de placares);
- Implementar de niveis de dificuldade;
- criar menus (principal e de configurações);
- 

## Contribuições
- Este é um projeto pessoal de estudo, mas sugestões ou melhorias são bem-vindas.
Sinta-se à vontade para abrir uma issue ou um pull request.

## Licença
- O projeto está licenciado sob a licença MIT.

**Autor:** Gabriel Pereira Barbosa
**LinkedIn:** https://linkedin.com/in/gpb0194/
