# 🚀 Deploy Completo na Vercel (Frontend + Backend)

## ✅ Sim! O backend PODE funcionar na Vercel

A Vercel suporta Python através de **Serverless Functions**, então você pode hospedar tanto frontend quanto backend na mesma plataforma.

---

## ⚠️ Limitações da Vercel para Backend

1. **Timeout:** 10 segundos (plano Hobby) ou 60 segundos (plano Pro)
2. **Cold Start:** Primeira requisição pode ser mais lenta
3. **Memória:** Limitada (1GB no plano Hobby)
4. **Não ideal para:** Aplicações que precisam manter conexões persistentes

**Para este projeto de pagamentos, funciona bem!** ✅

---

## 📋 Configuração Completa

### 1. Estrutura Criada

```
projeto/
├── api/
│   └── index.py          # Serverless Function (backend)
├── frontend/             # Arquivos HTML/CSS/JS
├── backend/              # Código do FastAPI
├── vercel.json           # Configuração da Vercel
└── requirements.txt      # Dependências Python
```

### 2. Como Funciona

- **Frontend:** Servido como arquivos estáticos
- **Backend:** Executado como Serverless Function em `/api/*`
- **Rotas:**
  - `/` → `frontend/index.html`
  - `/api/payments/*` → `api/index.py` (backend)

---

## 🔧 Configuração na Vercel

### Passo 1: Remover Root Directory

1. Acesse: https://vercel.com/rafaels-projects-bc90a5e9/curly-octo-enigma
2. Vá em **Settings** → **General**
3. **Root Directory:** Deixe **VAZIO** (não coloque `frontend`)
4. Salve

### Passo 2: Configurar Variáveis de Ambiente

1. Vá em **Settings** → **Environment Variables**
2. Adicione:
   ```
   MERCADOPAGO_ACCESS_TOKEN=APP_USR-6061834737027144-100216-686a6893aafd59eccf38db11db199080-577440377
   ```
3. Selecione todos os ambientes (Production, Preview, Development)
4. Salve

### Passo 3: Fazer Deploy

1. Vá em **Deployments**
2. Clique em **Redeploy** no último deploy
3. Ou faça push de novo código (deploy automático)

---

## 🧪 Testando

Após o deploy:

### Frontend:
- ✅ `https://seu-projeto.vercel.app/` → index.html
- ✅ `https://seu-projeto.vercel.app/finalizar.html` → página de pagamento

### Backend:
- ✅ `https://seu-projeto.vercel.app/api/` → informações da API
- ✅ `https://seu-projeto.vercel.app/api/docs` → documentação Swagger
- ✅ `https://seu-projeto.vercel.app/api/payments/create` → endpoint de pagamento

---

## ⚙️ Atualizar Frontend para Usar Backend na Vercel

**Arquivo:** `frontend/finalizar.html` (linha ~967)

**Altere:**
```javascript
const API_BASE_URL = 'http://localhost:8001/api/payments';
```

**Para:**
```javascript
// Usar o mesmo domínio da Vercel
const API_BASE_URL = '/api/payments';
// ou
const API_BASE_URL = window.location.origin + '/api/payments';
```

Isso faz com que o frontend use o backend na mesma Vercel automaticamente!

---

## 📝 Checklist

- [ ] Root Directory está **VAZIO** na Vercel
- [ ] Variável `MERCADOPAGO_ACCESS_TOKEN` configurada
- [ ] Arquivo `vercel.json` está na raiz
- [ ] Arquivo `api/index.py` existe
- [ ] Arquivo `requirements.txt` está na raiz
- [ ] URL da API no frontend atualizada para `/api/payments`
- [ ] Deploy realizado
- [ ] Teste: Frontend carrega
- [ ] Teste: Backend responde em `/api/`
- [ ] Teste: Pagamento funciona

---

## 🆘 Problemas Comuns

### ❌ Erro: "Module not found"

**Solução:** Verifique se `requirements.txt` está na raiz e tem todas as dependências

### ❌ Erro: "Timeout"

**Solução:** 
- Verifique se as requisições estão demorando muito
- Considere usar Railway/Render para backend (mais estável)

### ❌ Erro: "Cold start"

**Solução:** 
- É normal na primeira requisição
- Requisições subsequentes são mais rápidas

---

## 💡 Recomendação

**Para produção, considere:**
- **Frontend:** Vercel ✅ (perfeito)
- **Backend:** Railway ou Render ✅ (mais estável para APIs)

Mas se quiser tudo na Vercel, funciona! Só tenha em mente as limitações de timeout.

---

## 🎯 Resumo

1. ✅ Backend pode funcionar na Vercel via Serverless Functions
2. ✅ Frontend e backend na mesma plataforma
3. ⚠️ Limitações de timeout e cold start
4. ✅ Funciona bem para este projeto de pagamentos

**Próximo passo:** Remova o Root Directory, configure as variáveis e faça deploy!

