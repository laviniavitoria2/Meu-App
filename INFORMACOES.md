# 📋 Informações do Projeto - Meu-App

## 👤 Dados Pessoais
- **GitHub Username:** laviniavitoria2
- **Repositório:** Meu-App
- **URL GitHub:** https://github.com/laviniavitoria2/Meu-App
- **Branch Ativa:** laviniavitoria2-patch-1

---

## 🎯 Informações da Aplicação

**Nome:** Meu-App
**Tipo:** FastAPI Application
**Linguagem:** Python 3
**Licença:** MIT

---

## 📁 Arquivos do Projeto

```
Meu-App/
├── Main.py              ← Código principal
├── requirements.txt     ← pip install fastapi uvicorn
├── Procfile            ← Deploy Heroku
├── replit.nix          ← Deploy Replit
├── run.sh              ← Script para rodar localmente
├── README.md           ← Documentação
├── DEPLOY.md           ← Guia de Deploy
└── LICENSE             ← MIT License
```

---

## 🚀 Endpoints da API

### 1️⃣ GET /
**Resposta:**
```json
{
  "msg": "App rodando no GitHub 🚀"
}
```

---

### 2️⃣ GET /post?tema={tema}
**Exemplo:** `/post?tema=Python`

**Resposta:**
```json
{
  "post": "Python: quem entende isso, sai na frente."
}
```

---

## 🔧 Instalação Local

```bash
pip install fastapi uvicorn
uvicorn Main:app --reload
```

Acesse: http://localhost:8000

---

## 🌐 Deploy Options

### ✅ Render (RECOMENDADO)
- **URL:** https://render.com
- **Build:** `pip install -r requirements.txt`
- **Start:** `uvicorn Main:app --host 0.0.0.0 --port $PORT`

### ✅ Railway
- **URL:** https://railway.app
- Deploy automático via GitHub

### ✅ Heroku
- **URL:** https://heroku.com
- Use o arquivo Procfile incluído

### ✅ Replit
- **URL:** https://replit.com
- Use o arquivo replit.nix incluído

---

## 📱 Após Deploy

Seu app estará em:
```
https://seu-app-name.plataforma.com/
https://seu-app-name.plataforma.com/post?tema=Python
https://seu-app-name.plataforma.com/docs
```

---

## 📞 Suporte

**GitHub:** https://github.com/laviniavitoria2/Meu-App
**Email:** [Seu email aqui]

---

**Data Criação:** 16 de Fevereiro de 2026
**Status:** Pronto para Deploy ✅
