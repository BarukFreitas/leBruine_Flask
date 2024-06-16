Projeto Integrador

leBruine

Criado e desenvolvido por:

Thiago Anízio Miranda

Yuri Baruk Lima Freitas Souto

1. Introdução

O objetivo deste trabalho é especificar as funções e requisitos do sistema leBruine, fornecendo aos
usuários informações essenciais para uso e implementação. Destina-se a empreendedores do ramo
alimentício e seus consumidores. O escopo do projeto inclui a elicitação de requisitos da aplicação
web leBruine, desenvolvendo uma aplicação que facilita o agendamento de reservas em restaurantes.
leBruine é uma solução inovadora que busca modernizar e otimizar o processo de reservas em
restaurantes. Tradicionalmente, consumidores enfrentam desafios como longas filas, a necessidade de
fazer ligações ou esperar por respostas em chats. leBruine elimina esses inconvenientes,
proporcionando uma experiência de agendamento rápida e eficiente.
Com poucos e simples passos, os usuários podem agendar uma reserva diretamente pelo aplicativo,
evitando esperas desnecessárias. A interface do leBruine foi projetada para ser descomplicada e
amigável, garantindo que os usuários não se percam em funcionalidades complexas. A aplicação é
intuitiva, permitindo que até mesmo pessoas com pouca familiaridade com tecnologia possam utilizála
sem dificuldades.
Os usuários finais do sistema são tanto os consumidores quanto os donos de restaurantes. Para os
consumidores, o sistema oferece a possibilidade de explorar e reservar mesas em diversos restaurantes
de forma prática e rápida. Para os empreendedores, leBruine oferece ferramentas de gestão que
permitem cadastrar, editar e gerenciar informações sobre seus estabelecimentos, proporcionando
maior controle e visibilidade sobre as reservas e a operação do restaurante.
O desenvolvimento do leBruine priorizou a simplicidade e a eficiência, utilizando tecnologias
robustas que garantem um desempenho confiável. A escolha do Flask como framework principal para
o back-end foi motivada por sua leveza e facilidade de uso, permitindo uma rápida implementação das
funcionalidades necessárias. A interface foi construída com HTML, TailwindCSS e JavaScript,
garantindo uma experiência agradável e responsiva para o usuário.

2. Metodologia
O desenvolvimento do leBruine seguiu uma abordagem de simplicidade e eficiência, utilizando Flask,
um framework web para Python. As etapas principais incluíram:

1. Configuração do Ambiente: Instalação de Python e Flask com todas as dependências
necessárias.
2. Modelagem do Banco de Dados: Criação de um banco de dados em MySQL para armazenar
informações de usuários, restaurantes e reservas, utilizando SQLAlchemy.
3. Desenvolvimento da Interface: Implementação de uma interface com HTML, TailwindCSS
e JavaScript.
4. Implementação das Funcionalidades: Desenvolvimento das principais funcionalidades,
como cadastro de usuários, listagem de restaurantes e gerenciamento de reservas.
5. Testes: Realização de testes para garantir a funcionalidade e a segurança do sistema.

2.1 Requisitos Funcionais
Os requisitos funcionais especificam as funcionalidades que o sistema deve realizar. Eles descrevem
as operações e comportamentos esperados do software, focando nas necessidades dos usuários e nas
interações diretas com o sistema.

1. Cadastro de Restaurantes: Permitir o cadastro de novos restaurantes.
2. Edição de Cadastro: Permitir que usuários editem seus dados.
3. Excluir Conta: Permitir que usuários excluam suas contas.
4. Login/Logout: Permitir que usuários façam login e logout.
5. Visualização e Gerenciamento de Restaurantes: Permitir a visualização, edição e exclusão
de restaurantes.
6. Cadastro e Edição de Usuários: Permitir o cadastro, edição e exclusão de usuários.

2.2 Requisitos Não Funcionais
Os requisitos não funcionais descrevem as características e atributos de qualidade do sistema. Eles
definem como o sistema deve se comportar, focando em aspectos como desempenho, usabilidade,
segurança e confiabilidade.

1. Criptografia de Senha: As senhas dos usuários devem ser criptografadas.
2. Autenticação: Somente usuários autenticados podem criar postagens de projetos.
3. Padrão MTV: Seguir o padrão Model, Template e View.
4. Disponibilidade: O sistema deve estar operacional 98% do tempo.
5. Recuperação: O tempo de inatividade após uma falha não deve exceder 1 hora.
6. Backup: Realizar backups periódicos dos dados.
7. Usabilidade: Acesso às informações com até 3 cliques e responsividade para vários tamanhos
de tela.
8. Eficiência: Suportar até 100 usuários simultâneos.
9. Manutenibilidade: Permitir mudanças na base de dados sem grandes alterações.
10. Portabilidade: Suportar execução em ambientes Android e iOS.
3. Discussão

Durante o desenvolvimento do projeto leBruine, enfrentamos diversos desafios, incluindo mudanças
na tecnologia utilizada e a implementação de medidas de segurança robustas. Nossa escolha final
recaiu sobre o Flask, um microframework web para Python, após considerarmos outras alternativas
como ReactJS e NextJS.

3.1 Mudanças Tecnológicas
Inicialmente, exploramos o uso de ReactJS e NextJS. O ReactJS é uma biblioteca JavaScript para
construir interfaces de usuário, particularmente populares para aplicações de página única (SPAs). É
conhecido por sua eficiência e flexibilidade, permitindo a criação de interfaces interativas e dinâmicas
. NextJS, um framework React que facilita a renderização do lado do servidor (SSR) e a geração
estática de páginas, oferece uma melhor performance e SEO (Search Engine Optimization) para nossa
aplicação.
Eventualmente, decidimos utilizar Flask devido à sua simplicidade e eficácia em projetos que
necessitam de um backend robusto e eficiente. Flask é um microframework de Python que fornece as
ferramentas essenciais para o desenvolvimento de aplicações web sem impor muita complexidade. Ele
é altamente extensível, permitindo a adição de bibliotecas conforme a necessidade, e é ideal para
projetos que requerem um controle preciso sobre as componentes do servidor.

3.2 Segurança
A segurança foi uma das principais preocupações durante o desenvolvimento. Implementamos
medidas como a criptografia de senhas e a autenticação dos usuários. Utilizamos a função
generate_password_hash para criptografar senhas e a função check_password_hash para verificar as
senhas fornecidas pelos usuários. Esses métodos, disponíveis na biblioteca Werkzeug, garantem que
as senhas armazenadas no banco de dados sejam protegidas contra acessos não autorizados.

3.3 Escalabilidade e Confiabilidade
A escalabilidade do sistema foi planejada para suportar um número significativo de usuários
simultâneos. Isso envolveu a utilização de um banco de dados robusto e a implementação de
estratégias de caching para melhorar a performance. A confiabilidade do sistema também foi uma
prioridade, com um objetivo de manter um tempo de inatividade mínimo. Estratégias de backup
regular e a capacidade de recuperação rápida após falhas foram implementadas para garantir a
integridade dos dados e a continuidade do serviço.
Esses desafios e soluções implementadas destacam a importância de uma abordagem flexível e
adaptável no desenvolvimento de software. Através dessas experiências, conseguimos criar um
sistema funcional e eficiente, que atende às necessidades dos usuários finais, ao mesmo tempo em que
garante segurança e confiabilidade.

4. Conclusão
O projeto leBruine atingiu com sucesso seus objetivos principais, oferecendo uma solução prática e
eficiente para reservas em restaurantes. O sistema foi projetado com foco em segurança, usabilidade e
suporte a múltiplos usuários, garantindo a proteção dos dados e a satisfação dos usuários.

4.1 Desafios e Soluções
Durante o desenvolvimento, enfrentamos desafios significativos, como a necessidade de incorporar
medidas de segurança robustas e a adaptação às mudanças tecnológicas. A segurança foi aprimorada
com a implementação de autenticação segura e planejamento da escalabilidade do sistema para
suportar um grande número de usuários.

4.2 Recomendações Futuras
Para futuras melhorias, recomendamos um foco contínuo na otimização da usabilidade através de
testes de experiência do usuário (UX) e ajustes baseados em feedback. Aumentar a portabilidade da
aplicação para suportar uma variedade ainda maior de dispositivos e sistemas operacionais também
pode melhorar significativamente a experiência do usuário. Implementar um design responsivo e
adaptar a interface para diferentes tamanhos de tela são passos importantes nesse sentido.

4.3 Experiência de Aprendizado
O desenvolvimento do leBruine proporcionou uma experiência rica de aprendizado, destacando a
importância de uma abordagem flexível e adaptável no desenvolvimento de software. Através dos
desafios enfrentados e das soluções implementadas, conseguimos criar um sistema funcional e
eficiente que atende às necessidades dos usuários finais. Este projeto sublinhou a importância de
equilibrar inovação e praticidade, garantindo que a escolha das tecnologias e a implementação de
práticas de segurança sejam fundamentais para o sucesso de um sistema de reservas de alta qualidade.
Continuamos comprometidos em melhorar a aplicação e em atender às expectativas dos usuários,
adaptando-nos às mudanças e incorporando novas tecnologias conforme necessário.

5. Referências:

1. Guru99. "Functional vs Non-Functional Requirements: Key Differences". Disponível em:
Guru99
2. Stack Overflow. "What are the main differences between Flask and Django?". Disponível em:
Stack Overflow
3. MDN Web Docs. "React: A JavaScript library for building user interfaces". Disponível em:
MDN Web Docs
4. Next.js Documentation. "Why Next.js". Disponível em: Next.js Documentation
5. Flask Documentation. "Password Hashing". Disponível em: Flask Documentation
6. Real Python. "How to Secure Your Python REST API with JSON Web Tokens". Disponível
em: Real Python