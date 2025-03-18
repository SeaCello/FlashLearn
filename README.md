# FlashLearn  
### Transforme Texto em Conhecimento  

O **FlashLearn** é uma plataforma inovadora que permite criar flashcards personalizados automaticamente a partir de documentos de texto. Ideal para estudantes e profissionais, o FlashLearn combina inteligência artificial e um design responsivo para facilitar o aprendizado e otimizar seu tempo.  

---

## 📃 Índice  
  
1. [🔧 Tecnologias Utilizadas](#-tecnologias-utilizadas)  
2. [⚙️ Requisitos](#️-requisitos)  
3. [📦 Instalação](#-instruções-de-instalação)  
4. [➡️ Instruções de Uso](#️-instruções-de-uso)  
5. [📖 Documentação](#-documentação)  
6. [🖼️ Imagens e Visuais](#-imagens-e-visuais)  
7. [🆘 Informações de Suporte](#-informações-de-suporte)  
8. [📌 Status do Projeto](#-status-do-projeto)  
9. [🤝 Diretrizes para Contribuição](#-diretrizes-para-contribuição)  
10. [👥 Equipe de Desenvolvimento](#-equipe-de-desenvolvimento)  

---
## 🔧 Tecnologias Utilizadas  
### **Frontend**  
- **Tailwind CSS**: Framework de CSS moderno para criar interfaces rápidas e responsivas.  

### **Backend**  
- **Django**: Framework robusto para gerenciar lógica de negócios e comunicação com APIs.  

### **APIs**  
- **OpenAI API**: Processamento de texto para geração de flashcards automáticos.  

---
## ⚙️ Requisitos
Para rodar este projeto, você precisará dos seguintes pré-requisitos:

-   **Sistema Operacional:** Linux, macOS ou Windows.
    
-   **Python:** versão 3.8 ou superior.
    
-   **Bibliotecas Python:** As bibliotecas listadas em `requirements.txt` precisam ser instaladas.

-   **Banco de Dados:** PostgreSQL 12 ou superior.

---
### 📦 Instruções de Instalação

Para instalar e configurar este projeto, siga os passos abaixo:

1. **Clone o repositório** para o seu ambiente local:

   ```bash
   git clone https://github.com/seacello/flashlearn.git
   ```

2. **Acesse o diretório do projeto:**

   ```bash
   cd flashlearn
   ```

3. **Crie um ambiente virtual** (opcional, mas recomendado):

   - Para Python:

     ```bash
     python -m venv venv
     ```

   - Para ativar o ambiente virtual:

     - No Linux/macOS:

       ```bash
       source venv/bin/activate
       ```

     - No Windows:

       ```bash
       .\venv\Scripts\activate
       ```

4. **Instale as dependências** listadas no arquivo `requirements.txt`:

   ```bash
   pip install -r .\requirements.txt
   ```
   
5. **Instale o Tailwind CSS**:
	```bash
	python .\app\manage.py tailwind install
	```
	
6. **Crie as migrações do banco de dados** e aplique-as:

   - Para criar as migrações:

     ```bash
     python .\app\manage.py makemigrations
     ```

   - Para aplicar as migrações:

     ```bash
     python .\app\manage.py migrate
     ```

7. **Crie um superusuário** (opcional, mas recomendado para acessar o painel administrativo do Django):

   ```bash
   python .\app\manage.py createsuperuser
   ```

   Siga as instruções para definir nome de usuário, e-mail e senha.

8. **Inicie o Tailwind CSS**:
	
	```bash
	python .\app\manage.py tailwind start
	```

8. **Inicie o servidor de desenvolvimento do Django**:

   ```bash
   python .\app\manage.py runserver
   ```

9. **Acesse a aplicação**:

   Abra o navegador e vá até `http://127.0.0.1:8000/` para ver a aplicação rodando localmente.

   Para acessar o painel administrativo do Django, vá até `http://127.0.0.1:8000/admin/` e faça login com o superusuário criado.

Após seguir esses passos, o projeto estará pronto para ser utilizado.

---

### ➡️ Instruções de Uso

Após a instalação e configuração do projeto, siga os passos abaixo para utilizar a aplicação:

1. **Acesse o servidor local:**
   
   Se o frontend não estiver em execução, inicie-o com o seguinte comando:
   
   ```bash
	python .\app\manage.py tailwind start
	```
   
   Se o servidor não estiver em execução, inicie-o com o seguinte comando:

   ```bash
   python .\app\manage.py runserver
   ```

   Isso iniciará o servidor de desenvolvimento do Django no endereço `http://127.0.0.1:8000/`.

2. **Navegue pela aplicação:**
   
   Abra o navegador e acesse a URL abaixo para ver a aplicação rodando:

   ```
   http://127.0.0.1:8000/
   ```

3. **Acesse o painel administrativo (opcional):**
   
   Para acessar o painel administrativo do Django e gerenciar os dados do seu projeto, vá até a seguinte URL:

   ```
   http://127.0.0.1:8000/admin/
   ```

   Faça login usando as credenciais do superusuário que você criou anteriormente.

4. **Interaja com a aplicação:**
   
   Dependendo das funcionalidades do seu projeto, você poderá realizar operações como criar, editar ou excluir dados, visualizar informações e interagir com diferentes partes da aplicação através da interface web.

5. **Parar o servidor e frontend:**
   
   Para parar o servidor, basta pressionar **Ctrl + C** nos terminais onde o servidor e frontend estão rodando.

---

### 📖 Documentação  
A documentação completa do **FlashLearn** pode ser encontrada no nosso repositório oficial no GitHub. Ela inclui informações detalhadas sobre a instalação, uso da aplicação, APIs disponíveis e contribuições.  

Para acessar a documentação, visite:  
[🔗 Repositório do FlashLearn](https://github.com/seacello/flashlearn)  

Caso tenha dúvidas ou precise de suporte adicional, consulte a seção de **Informações de Suporte** abaixo.  

---

### 🖼️ Imagens e Visuais
Aqui estão algumas capturas de tela e exemplos da interface do **FlashLearn** para melhor compreensão do sistema:  

📌 **Tela Inicial:** [inserir imagem]  
📌 **Exemplo de Flashcard:** [inserir imagem]  

Mais imagens e vídeos demonstrativos podem ser encontrados na nossa documentação oficial e no repositório do projeto.  

---

### 🆘 Informações de Suporte  
Se você encontrar problemas ao usar o **FlashLearn**, temos várias formas de suporte disponíveis:  

📬 **E-mail:** marcello.eam@gmail.com
🐞 **Relatar um bug:** Abra uma issue no nosso [GitHub](https://github.com/seacello/flashlearn/issues)  

A equipe está disponível para ajudar com dúvidas técnicas, sugestões de melhorias e correções de bugs.  

---

### 📌 Status do Projeto  
O **FlashLearn** está atualmente na **Fase 4 - Deploy**. Estamos trabalhando no deploy final.  

📅 **Última atualização:** 14/03/2025  
🔜 **Próximas melhorias:**  
✔️ Deploy com docker
✔️ Github Actions  
  
---

### 🤝 Diretrizes para Contribuição  
Quer contribuir com o **FlashLearn**? Siga estas diretrizes para garantir um processo organizado e colaborativo:  

1. **Leia a documentação** para entender o funcionamento do projeto.  
2. **Abra uma issue** caso queira sugerir uma funcionalidade ou relatar um problema.  
3. **Crie uma branch** para suas mudanças:  

   ```bash
   git checkout -b feature/minha-contribuicao
   ```  

4. **Faça um pull request** detalhando as alterações realizadas.  
5. **Aguarde a revisão** e possíveis sugestões da equipe de desenvolvimento.  

Agradecemos sua colaboração para tornar o **FlashLearn** ainda melhor! 🚀  

---

## 👥 Equipe de Desenvolvimento  
- **Marcello Menezes** - Líder Técnico  
- **Eduardo Santana** - Fullstack Developer
  
---
