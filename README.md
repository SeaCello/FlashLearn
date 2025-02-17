
# FlashLearn  
### Transforme Texto em Conhecimento  

O **FlashLearn** é uma plataforma inovadora que permite criar flashcards personalizados automaticamente a partir de documentos de texto. Ideal para estudantes e profissionais, o FlashLearn combina inteligência artificial e um design responsivo para facilitar o aprendizado e otimizar seu tempo.  

---

## 📃 Índice  
X Tech used
X Requirements
X Install instruct
X usage instruct
documentation
visuals
support info
project status
contribution guidelines

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
   pip install -r requirements.txt
   ```

5. **Crie as migrações do banco de dados** e aplique-as:

   - Para criar as migrações:

     ```bash
     python manage.py makemigrations
     ```

   - Para aplicar as migrações:

     ```bash
     python manage.py migrate
     ```

6. **Crie um superusuário** (opcional, mas recomendado para acessar o painel administrativo do Django):

   ```bash
   python manage.py createsuperuser
   ```

   Siga as instruções para definir nome de usuário, e-mail e senha.

7. **Inicie o servidor de desenvolvimento do Django**:

   ```bash
   python manage.py runserver
   ```

8. **Acesse a aplicação**:

   Abra o navegador e vá até `http://127.0.0.1:8000/` para ver a aplicação rodando localmente.

   Para acessar o painel administrativo do Django, vá até `http://127.0.0.1:8000/admin/` e faça login com o superusuário criado.

Após seguir esses passos, o projeto estará pronto para ser utilizado.

---

### ➡️ Instruções de Uso

Após a instalação e configuração do projeto, siga os passos abaixo para utilizar a aplicação:

1. **Acesse o servidor local:**
   
   Se o servidor não estiver em execução, inicie-o com o seguinte comando:

   ```bash
   python manage.py runserver
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

5. **Parar o servidor:**
   
   Para parar o servidor, basta pressionar **Ctrl + C** no terminal onde o servidor está rodando.

---

## 🚀 Roadmap do Desenvolvimento  
### **Fase 1 - MVP (Produto Mínimo Viável)**  
- Funcionalidades principais: upload de documentos, geração automática de flashcards e interface básica.  
- Lançamento para grupo limitado de usuários para testes e feedback.  

### **Fase 2 - Expansão de Funcionalidades**  
- Adição de edição avançada, organização de flashcards e integração com APIs de arte.  

### **Fase 3 - Escala e Finalização**  
- Testes de carga e segurança, lançamento público e suporte técnico completo.  

---

## 🛠️ Contribuindo  
Contribuições são bem-vindas!  
1. Faça um fork do projeto.  
2. Crie uma branch para sua funcionalidade (`git checkout -b feature/nova-funcionalidade`).  
3. Submeta um pull request para revisão.  

---

## 👥 Equipe de Desenvolvimento  
- **Marcello Menezes** - Líder Técnico  
- **Eduardo Santana** - Fullstack Developer  
- **Rodrigo Sales** - Front-End Developer  
- **Severino Murilo da Silva** - Back-End Developer  
---


## Apps Instalados
user: Gerenciamento de usuários
home: Página inicial
flashcards: Sistema de flashcards
gpt: Integração com GPT
