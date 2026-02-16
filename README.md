# Meu-App 🚀

Uma aplicação simples com FastAPI para gerar posts temáticos.

## Funcionalidades

- ✅ Endpoint raiz que confirma a execução
- ✅ Gerador de posts por tema

## Como usar localmente

1. **Instalar dependências:**
```bash
pip install -r requirements.txt
```

2. **Executar a aplicação:**
```bash
uvicorn Main:app --reload
```

3. **Acessar:**
   - Página inicial: `http://localhost:8000/`
   - Gerar post: `http://localhost:8000/post?tema=Python`
   - Documentação: `http://localhost:8000/docs`

## Endpoints

### GET /
Retorna mensagem de confirmação da aplicação.

**Resposta:**
```json
{
  "msg": "App rodando no GitHub 🚀"
}
```

### GET /post
Gera um post baseado no tema informado.

**Parâmetros:**
- `tema` (string): O tema do post

**Resposta:**
```json
{
  "post": "{tema}: quem entende isso, sai na frente."
}
```

## Deploy

A aplicação está configurada para deploy no Heroku.

## Licença

MIT License - Copyright (c) 2026
